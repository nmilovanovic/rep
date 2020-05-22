using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace k8sForms
{
   public partial class FormSpans : Form
   {
      public FormSpans()
      {
         InitializeComponent();
      }

      private void button1_Click(object sender, EventArgs e)
      {
         flowLayoutPanel1.Controls.Add(new UserControl1());
      }

      private void button2_Click(object sender, EventArgs e)
      {
         this.DialogResult = DialogResult.OK;
      }

      public string getString()
      {
         StringBuilder sb = new StringBuilder();
         foreach(Control c in flowLayoutPanel1.Controls)
         {
            UserControl1 uc1 = (UserControl1)c;
            sb.Append(uc1.textBox1.Text);
            sb.Append("-");
            sb.Append(uc1.textBox2.Text);
            sb.Append("-");
            sb.Append(uc1.textBox3.Text);
            sb.Append("#");
         }
         return sb.ToString();
      }
   }
}
