# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: prototype.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='prototype.proto',
  package='prototype',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fprototype.proto\x12\tprototype\"#\n\x0ePictureRequest\x12\x11\n\tproductid\x18\x01 \x01(\t\"7\n\x11\x41\x64\x64PictureRequest\x12\x11\n\tproductid\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\"\"\n\x0fPictureResponse\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\"\x1f\n\x0cSpecsRequest\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\" \n\rSpecsResponse\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\"A\n\x0b\x43\x61rtRequest\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12\x11\n\tproductid\x18\x02 \x01(\t\x12\x0e\n\x06userid\x18\x03 \x01(\t\"\x1f\n\x0c\x43\x61rtResponse\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\"2\n\x0f\x43heckoutRequest\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"#\n\x10\x43heckoutResponse\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t2\x9b\x01\n\x08Pictures\x12\x45\n\nGetPicture\x12\x19.prototype.PictureRequest\x1a\x1a.prototype.PictureResponse\"\x00\x12H\n\nAddPicture\x12\x1c.prototype.AddPictureRequest\x1a\x1a.prototype.PictureResponse\"\x00\x32\xd2\x01\n\x05Specs\x12\x43\n\x0cListProducts\x12\x17.prototype.SpecsRequest\x1a\x18.prototype.SpecsResponse\"\x00\x12\x41\n\nAddProduct\x12\x17.prototype.SpecsRequest\x1a\x18.prototype.SpecsResponse\"\x00\x12\x41\n\nGetProduct\x12\x17.prototype.SpecsRequest\x1a\x18.prototype.SpecsResponse\"\x00\x32\xcd\x01\n\x04\x43\x61rt\x12?\n\nAddProduct\x12\x16.prototype.CartRequest\x1a\x17.prototype.CartResponse\"\x00\x12\x41\n\x0c\x43heckoutCart\x12\x16.prototype.CartRequest\x1a\x17.prototype.CartResponse\"\x00\x12\x41\n\x0cListProducts\x12\x16.prototype.CartRequest\x1a\x17.prototype.CartResponse\"\x00\x32\x9c\x01\n\x08\x43heckout\x12\x44\n\x07\x41\x64\x64\x43\x61rt\x12\x1a.prototype.CheckoutRequest\x1a\x1b.prototype.CheckoutResponse\"\x00\x12J\n\rListCheckouts\x12\x1a.prototype.CheckoutRequest\x1a\x1b.prototype.CheckoutResponse\"\x00\x62\x06proto3'
)




_PICTUREREQUEST = _descriptor.Descriptor(
  name='PictureRequest',
  full_name='prototype.PictureRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='productid', full_name='prototype.PictureRequest.productid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=65,
)


_ADDPICTUREREQUEST = _descriptor.Descriptor(
  name='AddPictureRequest',
  full_name='prototype.AddPictureRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='productid', full_name='prototype.AddPictureRequest.productid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='prototype.AddPictureRequest.content', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=122,
)


_PICTURERESPONSE = _descriptor.Descriptor(
  name='PictureResponse',
  full_name='prototype.PictureResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='prototype.PictureResponse.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=158,
)


_SPECSREQUEST = _descriptor.Descriptor(
  name='SpecsRequest',
  full_name='prototype.SpecsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='prototype.SpecsRequest.content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=160,
  serialized_end=191,
)


_SPECSRESPONSE = _descriptor.Descriptor(
  name='SpecsResponse',
  full_name='prototype.SpecsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='prototype.SpecsResponse.content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=225,
)


_CARTREQUEST = _descriptor.Descriptor(
  name='CartRequest',
  full_name='prototype.CartRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='prototype.CartRequest.content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='productid', full_name='prototype.CartRequest.productid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userid', full_name='prototype.CartRequest.userid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=292,
)


_CARTRESPONSE = _descriptor.Descriptor(
  name='CartResponse',
  full_name='prototype.CartResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='prototype.CartResponse.content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=294,
  serialized_end=325,
)


_CHECKOUTREQUEST = _descriptor.Descriptor(
  name='CheckoutRequest',
  full_name='prototype.CheckoutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userid', full_name='prototype.CheckoutRequest.userid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='prototype.CheckoutRequest.content', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=327,
  serialized_end=377,
)


_CHECKOUTRESPONSE = _descriptor.Descriptor(
  name='CheckoutResponse',
  full_name='prototype.CheckoutResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='prototype.CheckoutResponse.content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=379,
  serialized_end=414,
)

DESCRIPTOR.message_types_by_name['PictureRequest'] = _PICTUREREQUEST
DESCRIPTOR.message_types_by_name['AddPictureRequest'] = _ADDPICTUREREQUEST
DESCRIPTOR.message_types_by_name['PictureResponse'] = _PICTURERESPONSE
DESCRIPTOR.message_types_by_name['SpecsRequest'] = _SPECSREQUEST
DESCRIPTOR.message_types_by_name['SpecsResponse'] = _SPECSRESPONSE
DESCRIPTOR.message_types_by_name['CartRequest'] = _CARTREQUEST
DESCRIPTOR.message_types_by_name['CartResponse'] = _CARTRESPONSE
DESCRIPTOR.message_types_by_name['CheckoutRequest'] = _CHECKOUTREQUEST
DESCRIPTOR.message_types_by_name['CheckoutResponse'] = _CHECKOUTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PictureRequest = _reflection.GeneratedProtocolMessageType('PictureRequest', (_message.Message,), {
  'DESCRIPTOR' : _PICTUREREQUEST,
  '__module__' : 'prototype_pb2'
  # @@protoc_insertion_point(class_scope:prototype.PictureRequest)
  })
_sym_db.RegisterMessage(PictureRequest)

AddPictureRequest = _reflection.GeneratedProtocolMessageType('AddPictureRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDPICTUREREQUEST,
  '__module__' : 'prototype_pb2'
  # @@protoc_insertion_point(class_scope:prototype.AddPictureRequest)
  })
_sym_db.RegisterMessage(AddPictureRequest)

PictureResponse = _reflection.GeneratedProtocolMessageType('PictureResponse', (_message.Message,), {
  'DESCRIPTOR' : _PICTURERESPONSE,
  '__module__' : 'prototype_pb2'
  # @@protoc_insertion_point(class_scope:prototype.PictureResponse)
  })
_sym_db.RegisterMessage(PictureResponse)

SpecsRequest = _reflection.GeneratedProtocolMessageType('SpecsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SPECSREQUEST,
  '__module__' : 'prototype_pb2'
  # @@protoc_insertion_point(class_scope:prototype.SpecsRequest)
  })
_sym_db.RegisterMessage(SpecsRequest)

SpecsResponse = _reflection.GeneratedProtocolMessageType('SpecsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SPECSRESPONSE,
  '__module__' : 'prototype_pb2'
  # @@protoc_insertion_point(class_scope:prototype.SpecsResponse)
  })
_sym_db.RegisterMessage(SpecsResponse)

CartRequest = _reflection.GeneratedProtocolMessageType('CartRequest', (_message.Message,), {
  'DESCRIPTOR' : _CARTREQUEST,
  '__module__' : 'prototype_pb2'
  # @@protoc_insertion_point(class_scope:prototype.CartRequest)
  })
_sym_db.RegisterMessage(CartRequest)

CartResponse = _reflection.GeneratedProtocolMessageType('CartResponse', (_message.Message,), {
  'DESCRIPTOR' : _CARTRESPONSE,
  '__module__' : 'prototype_pb2'
  # @@protoc_insertion_point(class_scope:prototype.CartResponse)
  })
_sym_db.RegisterMessage(CartResponse)

CheckoutRequest = _reflection.GeneratedProtocolMessageType('CheckoutRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKOUTREQUEST,
  '__module__' : 'prototype_pb2'
  # @@protoc_insertion_point(class_scope:prototype.CheckoutRequest)
  })
_sym_db.RegisterMessage(CheckoutRequest)

CheckoutResponse = _reflection.GeneratedProtocolMessageType('CheckoutResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHECKOUTRESPONSE,
  '__module__' : 'prototype_pb2'
  # @@protoc_insertion_point(class_scope:prototype.CheckoutResponse)
  })
_sym_db.RegisterMessage(CheckoutResponse)



_PICTURES = _descriptor.ServiceDescriptor(
  name='Pictures',
  full_name='prototype.Pictures',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=417,
  serialized_end=572,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetPicture',
    full_name='prototype.Pictures.GetPicture',
    index=0,
    containing_service=None,
    input_type=_PICTUREREQUEST,
    output_type=_PICTURERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddPicture',
    full_name='prototype.Pictures.AddPicture',
    index=1,
    containing_service=None,
    input_type=_ADDPICTUREREQUEST,
    output_type=_PICTURERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PICTURES)

DESCRIPTOR.services_by_name['Pictures'] = _PICTURES


_SPECS = _descriptor.ServiceDescriptor(
  name='Specs',
  full_name='prototype.Specs',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=575,
  serialized_end=785,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListProducts',
    full_name='prototype.Specs.ListProducts',
    index=0,
    containing_service=None,
    input_type=_SPECSREQUEST,
    output_type=_SPECSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddProduct',
    full_name='prototype.Specs.AddProduct',
    index=1,
    containing_service=None,
    input_type=_SPECSREQUEST,
    output_type=_SPECSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetProduct',
    full_name='prototype.Specs.GetProduct',
    index=2,
    containing_service=None,
    input_type=_SPECSREQUEST,
    output_type=_SPECSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SPECS)

DESCRIPTOR.services_by_name['Specs'] = _SPECS


_CART = _descriptor.ServiceDescriptor(
  name='Cart',
  full_name='prototype.Cart',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=788,
  serialized_end=993,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddProduct',
    full_name='prototype.Cart.AddProduct',
    index=0,
    containing_service=None,
    input_type=_CARTREQUEST,
    output_type=_CARTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CheckoutCart',
    full_name='prototype.Cart.CheckoutCart',
    index=1,
    containing_service=None,
    input_type=_CARTREQUEST,
    output_type=_CARTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListProducts',
    full_name='prototype.Cart.ListProducts',
    index=2,
    containing_service=None,
    input_type=_CARTREQUEST,
    output_type=_CARTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CART)

DESCRIPTOR.services_by_name['Cart'] = _CART


_CHECKOUT = _descriptor.ServiceDescriptor(
  name='Checkout',
  full_name='prototype.Checkout',
  file=DESCRIPTOR,
  index=3,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=996,
  serialized_end=1152,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddCart',
    full_name='prototype.Checkout.AddCart',
    index=0,
    containing_service=None,
    input_type=_CHECKOUTREQUEST,
    output_type=_CHECKOUTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListCheckouts',
    full_name='prototype.Checkout.ListCheckouts',
    index=1,
    containing_service=None,
    input_type=_CHECKOUTREQUEST,
    output_type=_CHECKOUTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHECKOUT)

DESCRIPTOR.services_by_name['Checkout'] = _CHECKOUT

# @@protoc_insertion_point(module_scope)