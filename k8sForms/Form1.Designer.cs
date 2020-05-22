namespace k8sForms
{
   partial class Form1
   {
      /// <summary>
      /// Required designer variable.
      /// </summary>
      private System.ComponentModel.IContainer components = null;

      /// <summary>
      /// Clean up any resources being used.
      /// </summary>
      /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
      protected override void Dispose(bool disposing)
      {
         if (disposing && (components != null))
         {
            components.Dispose();
         }
         base.Dispose(disposing);
      }

      #region Windows Form Designer generated code

      /// <summary>
      /// Required method for Designer support - do not modify
      /// the contents of this method with the code editor.
      /// </summary>
      private void InitializeComponent()
      {
         this.dataGridView1 = new System.Windows.Forms.DataGridView();
         this.button1 = new System.Windows.Forms.Button();
         this.tableLayoutPanel1 = new System.Windows.Forms.TableLayoutPanel();
         this.label1 = new System.Windows.Forms.Label();
         this.label2 = new System.Windows.Forms.Label();
         this.label3 = new System.Windows.Forms.Label();
         this.label4 = new System.Windows.Forms.Label();
         this.tbImage = new System.Windows.Forms.TextBox();
         this.tbName = new System.Windows.Forms.TextBox();
         this.tbReplicas = new System.Windows.Forms.TextBox();
         this.tbMode = new System.Windows.Forms.ListBox();
         this.button2 = new System.Windows.Forms.Button();
         this.button3 = new System.Windows.Forms.Button();
         this.tbEndpoint = new System.Windows.Forms.TextBox();
         ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
         this.tableLayoutPanel1.SuspendLayout();
         this.SuspendLayout();
         // 
         // dataGridView1
         // 
         this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
         this.dataGridView1.Location = new System.Drawing.Point(12, 12);
         this.dataGridView1.MultiSelect = false;
         this.dataGridView1.Name = "dataGridView1";
         this.dataGridView1.ReadOnly = true;
         this.dataGridView1.Size = new System.Drawing.Size(462, 426);
         this.dataGridView1.TabIndex = 0;
         // 
         // button1
         // 
         this.button1.Location = new System.Drawing.Point(486, 415);
         this.button1.Name = "button1";
         this.button1.Size = new System.Drawing.Size(75, 23);
         this.button1.TabIndex = 1;
         this.button1.Text = "Refresh";
         this.button1.UseVisualStyleBackColor = true;
         this.button1.Click += new System.EventHandler(this.button1_Click);
         // 
         // tableLayoutPanel1
         // 
         this.tableLayoutPanel1.ColumnCount = 2;
         this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 21.42857F));
         this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 78.57143F));
         this.tableLayoutPanel1.Controls.Add(this.label1, 0, 0);
         this.tableLayoutPanel1.Controls.Add(this.label2, 0, 1);
         this.tableLayoutPanel1.Controls.Add(this.label3, 0, 2);
         this.tableLayoutPanel1.Controls.Add(this.label4, 0, 3);
         this.tableLayoutPanel1.Controls.Add(this.tbImage, 1, 0);
         this.tableLayoutPanel1.Controls.Add(this.tbName, 1, 1);
         this.tableLayoutPanel1.Controls.Add(this.tbReplicas, 1, 3);
         this.tableLayoutPanel1.Controls.Add(this.tbMode, 1, 2);
         this.tableLayoutPanel1.Location = new System.Drawing.Point(480, 12);
         this.tableLayoutPanel1.Name = "tableLayoutPanel1";
         this.tableLayoutPanel1.RowCount = 5;
         this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 25F));
         this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 25F));
         this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 25F));
         this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 25F));
         this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 20F));
         this.tableLayoutPanel1.Size = new System.Drawing.Size(308, 242);
         this.tableLayoutPanel1.TabIndex = 2;
         // 
         // label1
         // 
         this.label1.AutoSize = true;
         this.label1.Location = new System.Drawing.Point(3, 0);
         this.label1.Name = "label1";
         this.label1.Size = new System.Drawing.Size(39, 13);
         this.label1.TabIndex = 0;
         this.label1.Text = "Image:";
         // 
         // label2
         // 
         this.label2.AutoSize = true;
         this.label2.Location = new System.Drawing.Point(3, 55);
         this.label2.Name = "label2";
         this.label2.Size = new System.Drawing.Size(38, 13);
         this.label2.TabIndex = 1;
         this.label2.Text = "Name:";
         // 
         // label3
         // 
         this.label3.AutoSize = true;
         this.label3.Location = new System.Drawing.Point(3, 110);
         this.label3.Name = "label3";
         this.label3.Size = new System.Drawing.Size(34, 13);
         this.label3.TabIndex = 2;
         this.label3.Text = "Mode";
         // 
         // label4
         // 
         this.label4.AutoSize = true;
         this.label4.Location = new System.Drawing.Point(3, 165);
         this.label4.Name = "label4";
         this.label4.Size = new System.Drawing.Size(51, 13);
         this.label4.TabIndex = 3;
         this.label4.Text = "Replicas:";
         // 
         // tbImage
         // 
         this.tbImage.Location = new System.Drawing.Point(68, 3);
         this.tbImage.Name = "tbImage";
         this.tbImage.Size = new System.Drawing.Size(236, 20);
         this.tbImage.TabIndex = 4;
         // 
         // tbName
         // 
         this.tbName.Location = new System.Drawing.Point(68, 58);
         this.tbName.Name = "tbName";
         this.tbName.Size = new System.Drawing.Size(236, 20);
         this.tbName.TabIndex = 5;
         // 
         // tbReplicas
         // 
         this.tbReplicas.Location = new System.Drawing.Point(68, 168);
         this.tbReplicas.Multiline = true;
         this.tbReplicas.Name = "tbReplicas";
         this.tbReplicas.Size = new System.Drawing.Size(236, 49);
         this.tbReplicas.TabIndex = 7;
         this.tbReplicas.MouseDoubleClick += new System.Windows.Forms.MouseEventHandler(this.tbReplicas_MouseDoubleClick);
         // 
         // tbMode
         // 
         this.tbMode.FormattingEnabled = true;
         this.tbMode.Items.AddRange(new object[] {
            "day",
            "week",
            "month",
            "auto"});
         this.tbMode.Location = new System.Drawing.Point(68, 113);
         this.tbMode.Name = "tbMode";
         this.tbMode.Size = new System.Drawing.Size(120, 43);
         this.tbMode.TabIndex = 8;
         this.tbMode.SelectedIndexChanged += new System.EventHandler(this.tbMode_SelectedIndexChanged);
         // 
         // button2
         // 
         this.button2.Location = new System.Drawing.Point(480, 260);
         this.button2.Name = "button2";
         this.button2.Size = new System.Drawing.Size(154, 23);
         this.button2.TabIndex = 3;
         this.button2.Text = "Select custom resource";
         this.button2.UseVisualStyleBackColor = true;
         this.button2.Click += new System.EventHandler(this.button2_Click);
         // 
         // button3
         // 
         this.button3.Location = new System.Drawing.Point(671, 260);
         this.button3.Name = "button3";
         this.button3.Size = new System.Drawing.Size(113, 23);
         this.button3.TabIndex = 4;
         this.button3.Text = "Commit changes";
         this.button3.UseVisualStyleBackColor = true;
         this.button3.Click += new System.EventHandler(this.button3_Click);
         // 
         // tbEndpoint
         // 
         this.tbEndpoint.Location = new System.Drawing.Point(567, 418);
         this.tbEndpoint.Name = "tbEndpoint";
         this.tbEndpoint.ScrollBars = System.Windows.Forms.ScrollBars.Horizontal;
         this.tbEndpoint.Size = new System.Drawing.Size(217, 20);
         this.tbEndpoint.TabIndex = 5;
         this.tbEndpoint.Text = "http://192.168.1.6:8001";
         // 
         // Form1
         // 
         this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
         this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
         this.ClientSize = new System.Drawing.Size(800, 450);
         this.Controls.Add(this.tbEndpoint);
         this.Controls.Add(this.button3);
         this.Controls.Add(this.button2);
         this.Controls.Add(this.tableLayoutPanel1);
         this.Controls.Add(this.button1);
         this.Controls.Add(this.dataGridView1);
         this.Name = "Form1";
         this.Text = "Form1";
         ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
         this.tableLayoutPanel1.ResumeLayout(false);
         this.tableLayoutPanel1.PerformLayout();
         this.ResumeLayout(false);
         this.PerformLayout();

      }

      #endregion

      private System.Windows.Forms.DataGridView dataGridView1;
      private System.Windows.Forms.Button button1;
      private System.Windows.Forms.TableLayoutPanel tableLayoutPanel1;
      private System.Windows.Forms.Label label1;
      private System.Windows.Forms.Label label2;
      private System.Windows.Forms.Label label3;
      private System.Windows.Forms.Label label4;
      private System.Windows.Forms.TextBox tbImage;
      private System.Windows.Forms.TextBox tbName;
      private System.Windows.Forms.TextBox tbReplicas;
      private System.Windows.Forms.Button button2;
      private System.Windows.Forms.Button button3;
      private System.Windows.Forms.ListBox tbMode;
      private System.Windows.Forms.TextBox tbEndpoint;
   }
}

