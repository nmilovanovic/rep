using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Windows.Forms;
using k8s;
using Newtonsoft.Json.Linq;

namespace k8sForms
{
   public partial class Form1 : Form
   {
      public Form1()
      {
         InitializeComponent();
      }

      private IJEnumerable<JToken> je;
      private int selectedIndex = -1;
      private Kubernetes client;

      private void button1_Click(object sender, EventArgs e)
      {
         var config = new KubernetesClientConfiguration { Host = tbEndpoint.Text };
         client = new Kubernetes(config);
         dataGridView1.Rows.Clear();
         dataGridView1.Columns.Clear();
         dataGridView1.Refresh();
         var list = client.ListNamespacedCustomObject("elfak.rs", "v1", "default", "resourcereplicas");
         JObject jo = JObject.Parse(list.ToString());
         dataGridView1.Columns.Add("image", "image");
         dataGridView1.Columns.Add("mode", "mode");
         dataGridView1.Columns.Add("name", "name");
         dataGridView1.Columns.Add("replicas", "replicas");
         je = jo["items"].AsJEnumerable();
         foreach (var item in je)
         {
            dataGridView1.Rows.Add(item["spec"]["image"], item["spec"]["mode"], item["spec"]["name"], item["spec"]["replicas"]);
         }
      }

      private void button2_Click(object sender, EventArgs e)
      {
         if (dataGridView1.SelectedRows.Count == 0)
         {
            MessageBox.Show("Please select a custom resource.");
            return;
         }
         int ind = dataGridView1.SelectedRows[0].Index;
         selectedIndex = ind;
         tbImage.Text = dataGridView1.Rows[ind].Cells[0].Value.ToString();
         tbName.Text = dataGridView1.Rows[ind].Cells[2].Value.ToString();
         tbMode.Text = dataGridView1.Rows[ind].Cells[1].Value.ToString();
         tbReplicas.Text = dataGridView1.Rows[ind].Cells[3].Value.ToString();
      }

      private bool validateString(string mode, string target)
      {
         string[] splits = target.Split('#');
         if (mode == "day")
         {
            foreach (var str in splits)
            {
               bool match = Regex.Match(str, "^[0-2][0-9]:[0-6][0-9]:[0-6][0-9]-[0-2][0-9]:[0-6][0-9]:[0-6][0-9]-[0-9]+$").Success;
               if (!match)
               {
                  return false;
               }
            }
            return true;
         }
         else if (mode == "week")
         {
            foreach (var str in splits)
            {
               bool match = Regex.Match(str, @"^\d-\d-\d+$").Success;
               if (!match)
               {
                  return false;
               }
            }
            return true;
         }
         else if (mode == "month")
         {
            foreach (var str in splits)
            {
               bool match = Regex.Match(str, "^[0-3]?[0-9]-[0-3]?[0-9]-[0-9]+$").Success;
               if (!match)
               {
                  return false;
               }
            }
            return true;
         }
         return false;
      }

      private void button3_Click(object sender, EventArgs e)
      {
         bool valdiated = validateString(tbMode.Text, tbReplicas.Text);
         if (!valdiated)
         {
            MessageBox.Show("Input for the replicas parameter is invalid.");
         }
         JObject job = (JObject)je[selectedIndex];
         job["spec"]["image"] = tbImage.Text;
         job["spec"]["name"] = tbName.Text;
         job["spec"]["mode"] = tbMode.Text;
         job["spec"]["replicas"] = tbReplicas.Text;
         client.ReplaceNamespacedCustomObject(job, "elfak.rs", "v1", "default", "resourcereplicas", job["metadata"]["name"].ToString());
         MessageBox.Show("Changes commited!");

      }

      private void tbMode_SelectedIndexChanged(object sender, EventArgs e)
      {
         if (tbMode.Text == "auto")
         {
            tbReplicas.Enabled = false;
         }
         else
         {
            tbReplicas.Enabled = true;
         }
      }

      private void tbReplicas_MouseDoubleClick(object sender, MouseEventArgs e)
      {
         FormSpans fs = new FormSpans();
         DialogResult dr = DialogResult.Cancel;
         bool validated = false;
         string str = String.Empty;
         do
         {
            dr = fs.ShowDialog();
            if (dr != DialogResult.OK)
            {
               return;
            }
            str = fs.getString().Trim('#');
            validated = validateString(tbMode.Text, str);
            if (!validated)
            {
               MessageBox.Show("Input is invalid.");
            }
         } while (!validated);
         tbReplicas.Text = str;
      }
   }
}
