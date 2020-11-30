from flask import Flask, redirect, url_for, request, render_template, make_response, session, send_from_directory, send_file
import uuid
import datetime
import io
import grpc
import prototype_pb2_grpc
import prototype_pb2
import base64
import json
from prometheus_client import Counter, start_http_server
import os

app = Flask(__name__)
app.config["DEBUG"] = False

REQUESTS = Counter('http_requests_total', 'Total number of requests to this API.')

PICTURES_CONN_STRING = os.environ['PICTURES']
SPECS_CONN_STRING = os.environ['SPECS']
CART_CONN_STRING = os.environ['CART']
CHECKOUT_CONN_STRING = os.environ['CHECKOUT']

@app.route('/')
def index():
    REQUESTS.inc()
    if not 'userid' in request.cookies:
        userid = uuid.uuid4().hex
    else:
        userid = request.cookies['userid']
    response = make_response(render_template('index.html', id=userid))
    expires = datetime.datetime.now() + datetime.timedelta(days=90)
    response.set_cookie('userid', userid, expires=expires)
    return response

@app.route('/addproduct', methods = ['POST'])
def add_product_post():
    REQUESTS.inc()
    if not 'userid' in request.cookies:
        return redirect(url_for('/'))
    f = request.files['image']
    image_contents = f.read()
    product_dict = dict()
    productid = uuid.uuid4().hex
    product_dict['productid'] = productid
    product_dict['name'] = request.form['name']
    product_dict['description'] = request.form['description']
    with grpc.insecure_channel(SPECS_CONN_STRING) as channel:
        stub = prototype_pb2_grpc.SpecsStub(channel)
        req = prototype_pb2.SpecsRequest(content=json.dumps(product_dict))
        stub.AddProduct(req)
    with grpc.insecure_channel(PICTURES_CONN_STRING) as channel:
        stub = prototype_pb2_grpc.PicturesStub(channel)
        req = prototype_pb2.AddPictureRequest(productid=productid, content=image_contents)
        stub.AddPicture(req)
    return 'Product added successfully'

@app.route('/addtocart',methods = ['POST'])
def add_to_cart():
    REQUESTS.inc()
    if not 'userid' in request.cookies:
        return redirect(url_for('/'))
    productid = request.form['productid']
    userid = request.cookies['userid']
    with grpc.insecure_channel(CART_CONN_STRING) as channel:
        stub = prototype_pb2_grpc.CartStub(channel)
        req = prototype_pb2.CartRequest(userid=userid, productid=productid)
        stub.AddProduct(req)
    return 'Product successfully added to the cart!'

@app.route('/listcart',methods = ['GET'])
def list_cart():
    REQUESTS.inc()
    if not 'userid' in request.cookies:
        return redirect(url_for('/'))
    response = None
    userid = request.cookies['userid']
    with grpc.insecure_channel(CART_CONN_STRING) as channel:
        stub = prototype_pb2_grpc.CartStub(channel)
        req = prototype_pb2.CartRequest(userid=userid)
        response = stub.ListProducts(req)
    products_dict = json.loads(response.content)
    products_list = products_dict['list']
    products = dict()
    for product in products_list:
        with grpc.insecure_channel(SPECS_CONN_STRING) as channel:
            stub = prototype_pb2_grpc.SpecsStub(channel)
            req = prototype_pb2.CartRequest(content=product)
            response = stub.GetProduct(req)
            response = json.loads(response.content)
            products[response['productid']] = response
    return render_template('listcart.html', userid=userid, products_dict=products)

@app.route('/checkoutcart',methods = ['GET'])
def checkout_cart():
    REQUESTS.inc()
    if not 'userid' in request.cookies:
        return redirect(url_for('/'))
    response = None
    userid = request.cookies['userid']
    with grpc.insecure_channel(CART_CONN_STRING) as channel:
        stub = prototype_pb2_grpc.CartStub(channel)
        req = prototype_pb2.CartRequest(userid=userid)
        response = stub.CheckoutCart(req)
    print(response.content)
    with grpc.insecure_channel(CHECKOUT_CONN_STRING) as channel:
        stub = prototype_pb2_grpc.CheckoutStub(channel)
        req = prototype_pb2.CheckoutRequest(userid=userid, content=response.content)
        response = stub.AddCart(req)
    return 'You have successfully checked out your cart!'

@app.route('/listcheckouts', methods = ['GET'])
def list_checkouts():
    REQUESTS.inc()
    userid = request.cookies['userid']
    if not 'userid' in request.cookies:
        return redirect(url_for('/'))
    response = None
    with grpc.insecure_channel(CHECKOUT_CONN_STRING) as channel:
        stub = prototype_pb2_grpc.CheckoutStub(channel)
        req = prototype_pb2.CheckoutRequest()
        response = stub.ListCheckouts(req)
    print(response.content)
    return render_template('listcheckouts.html', userid=userid, checkouts_dict=json.loads(response.content))

@app.route('/addproduct',methods = ['GET'])
def add_product_get():
    REQUESTS.inc()
    if not 'userid' in request.cookies:
        return redirect(url_for('/'))
    return render_template('addproduct.html')

@app.route('/listproducts', methods = ['GET'])
def list_products():
    REQUESTS.inc()
    if not 'userid' in request.cookies:
        return redirect(url_for('/'))
    userid = request.cookies['userid']
    response = None
    with grpc.insecure_channel(SPECS_CONN_STRING) as channel:
        stub = prototype_pb2_grpc.SpecsStub(channel)
        req = prototype_pb2.SpecsRequest()
        response = stub.ListProducts(req)
    products_dict = json.loads(response.content)
    return render_template('listproducts.html', userid=userid, products_dict=products_dict)

@app.route('/checkout', methods = ['GET'])
def checkout():
    REQUESTS.inc()
    if not 'userid' in request.cookies:
        return redirect(url_for('/'))
    userid = request.cookies['userid']
    response = None
    with grpc.insecure_channel(CART_CONN_STRING) as channel:
        stub = prototype_pb2_grpc.CartStub(channel)
        req = prototype_pb2.CartRequest(userid=userid)
        response = stub.ListProducts(req)
    with grpc.insecure_channel(CART_CONN_STRING) as channel:
        stub = prototype_pb2_grpc.CartStub(channel)
        req = prototype_pb2.CartRequest(userid=userid)
        stub.CheckoutCart(req)
    with grpc.insecure_channel(CHECKOUT_CONN_STRING) as channel:
        stub = prototype_pb2_grpc.CheckoutStub(channel)
        req = prototype_pb2.CheckoutRequest(content=response.content)
        response = stub.AddCart(req)

    return 'You have successfully checked out your cart!'

@app.route('/logout/')
def logout():
    REQUESTS.inc()
    if not 'userid' in request.cookies:
        return redirect(url_for('/'))
    response = make_response(render_template('logout.html'))
    response.set_cookie('userid', '', expires=0)
    return response

@app.route('/images/<productid>')
def images(productid):
    REQUESTS.inc()
    response = None
    with grpc.insecure_channel(PICTURES_CONN_STRING) as channel:
        stub = prototype_pb2_grpc.PicturesStub(channel)
        request = prototype_pb2.PictureRequest(productid=productid)
        response = stub.GetPicture(request)
    response = make_response(send_file(io.BytesIO(response.content), mimetype='image/jpg'))
    return response 

if __name__ == '__main__':
    print(PICTURES_CONN_STRING)
    print(SPECS_CONN_STRING)
    print(CART_CONN_STRING)
    print(CHECKOUT_CONN_STRING)
    start_http_server(8000)
    app.run('0.0.0.0', port=80)