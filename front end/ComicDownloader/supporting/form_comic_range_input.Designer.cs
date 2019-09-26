namespace ComicDownloader.supporting
{
    partial class form_comic_range_input
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(form_comic_range_input));
            this.bun_flat_btn_go = new Bunifu.Framework.UI.BunifuFlatButton();
            this.lab_range = new System.Windows.Forms.Label();
            this.lab_end_range = new System.Windows.Forms.Label();
            this.lab_init_range = new System.Windows.Forms.Label();
            this.lab_num_results = new System.Windows.Forms.Label();
            this.rich_textbox_url_list = new System.Windows.Forms.RichTextBox();
            this.lab_instruction = new System.Windows.Forms.Label();
            this.lab_wave_mark = new System.Windows.Forms.Label();
            this.textbox_to = new System.Windows.Forms.TextBox();
            this.textbox_from = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // bun_flat_btn_go
            // 
            this.bun_flat_btn_go.Activecolor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_flat_btn_go.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_flat_btn_go.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.bun_flat_btn_go.BorderRadius = 0;
            this.bun_flat_btn_go.ButtonText = "";
            this.bun_flat_btn_go.Cursor = System.Windows.Forms.Cursors.Hand;
            this.bun_flat_btn_go.DisabledColor = System.Drawing.Color.Gray;
            this.bun_flat_btn_go.Iconcolor = System.Drawing.Color.Transparent;
            this.bun_flat_btn_go.Iconimage = ((System.Drawing.Image)(resources.GetObject("bun_flat_btn_go.Iconimage")));
            this.bun_flat_btn_go.Iconimage_right = null;
            this.bun_flat_btn_go.Iconimage_right_Selected = null;
            this.bun_flat_btn_go.Iconimage_Selected = null;
            this.bun_flat_btn_go.IconMarginLeft = 0;
            this.bun_flat_btn_go.IconMarginRight = 0;
            this.bun_flat_btn_go.IconRightVisible = true;
            this.bun_flat_btn_go.IconRightZoom = 0D;
            this.bun_flat_btn_go.IconVisible = true;
            this.bun_flat_btn_go.IconZoom = 80D;
            this.bun_flat_btn_go.IsTab = false;
            this.bun_flat_btn_go.Location = new System.Drawing.Point(367, 5);
            this.bun_flat_btn_go.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.bun_flat_btn_go.Name = "bun_flat_btn_go";
            this.bun_flat_btn_go.Normalcolor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_flat_btn_go.OnHovercolor = System.Drawing.Color.FromArgb(((int)(((byte)(36)))), ((int)(((byte)(129)))), ((int)(((byte)(77)))));
            this.bun_flat_btn_go.OnHoverTextColor = System.Drawing.Color.White;
            this.bun_flat_btn_go.selected = false;
            this.bun_flat_btn_go.Size = new System.Drawing.Size(40, 40);
            this.bun_flat_btn_go.TabIndex = 21;
            this.bun_flat_btn_go.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.bun_flat_btn_go.Textcolor = System.Drawing.Color.White;
            this.bun_flat_btn_go.TextFont = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bun_flat_btn_go.Click += new System.EventHandler(this.Bun_flat_btn_go_Click);
            // 
            // lab_range
            // 
            this.lab_range.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.lab_range.AutoSize = true;
            this.lab_range.Location = new System.Drawing.Point(302, 86);
            this.lab_range.Name = "lab_range";
            this.lab_range.Size = new System.Drawing.Size(93, 15);
            this.lab_range.TabIndex = 20;
            this.lab_range.Text = "[XXX - XXX]";
            this.lab_range.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lab_end_range
            // 
            this.lab_end_range.AutoSize = true;
            this.lab_end_range.Font = new System.Drawing.Font("Gulim", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
            this.lab_end_range.ForeColor = System.Drawing.Color.Crimson;
            this.lab_end_range.Location = new System.Drawing.Point(317, 30);
            this.lab_end_range.Name = "lab_end_range";
            this.lab_end_range.Size = new System.Drawing.Size(0, 17);
            this.lab_end_range.TabIndex = 19;
            // 
            // lab_init_range
            // 
            this.lab_init_range.AutoSize = true;
            this.lab_init_range.Font = new System.Drawing.Font("Gulim", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
            this.lab_init_range.Location = new System.Drawing.Point(151, 30);
            this.lab_init_range.Name = "lab_init_range";
            this.lab_init_range.Size = new System.Drawing.Size(0, 17);
            this.lab_init_range.TabIndex = 18;
            // 
            // lab_num_results
            // 
            this.lab_num_results.AutoSize = true;
            this.lab_num_results.Location = new System.Drawing.Point(6, 85);
            this.lab_num_results.Name = "lab_num_results";
            this.lab_num_results.Size = new System.Drawing.Size(88, 15);
            this.lab_num_results.TabIndex = 17;
            this.lab_num_results.Text = "XXX Results";
            // 
            // rich_textbox_url_list
            // 
            this.rich_textbox_url_list.BackColor = System.Drawing.SystemColors.ScrollBar;
            this.rich_textbox_url_list.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.rich_textbox_url_list.Cursor = System.Windows.Forms.Cursors.Arrow;
            this.rich_textbox_url_list.Location = new System.Drawing.Point(6, 102);
            this.rich_textbox_url_list.Name = "rich_textbox_url_list";
            this.rich_textbox_url_list.ReadOnly = true;
            this.rich_textbox_url_list.Size = new System.Drawing.Size(400, 300);
            this.rich_textbox_url_list.TabIndex = 16;
            this.rich_textbox_url_list.Text = "";
            this.rich_textbox_url_list.LinkClicked += new System.Windows.Forms.LinkClickedEventHandler(this.Rich_textbox_url_list_LinkClicked);
            // 
            // lab_instruction
            // 
            this.lab_instruction.AutoSize = true;
            this.lab_instruction.Location = new System.Drawing.Point(3, 5);
            this.lab_instruction.Name = "lab_instruction";
            this.lab_instruction.Size = new System.Drawing.Size(340, 15);
            this.lab_instruction.TabIndex = 15;
            this.lab_instruction.Text = "Enter a range of comic you are willing to download";
            // 
            // lab_wave_mark
            // 
            this.lab_wave_mark.AutoSize = true;
            this.lab_wave_mark.Location = new System.Drawing.Point(130, 35);
            this.lab_wave_mark.Name = "lab_wave_mark";
            this.lab_wave_mark.Size = new System.Drawing.Size(18, 15);
            this.lab_wave_mark.TabIndex = 14;
            this.lab_wave_mark.Text = "~";
            // 
            // textbox_to
            // 
            this.textbox_to.Location = new System.Drawing.Point(173, 30);
            this.textbox_to.Name = "textbox_to";
            this.textbox_to.Size = new System.Drawing.Size(100, 25);
            this.textbox_to.TabIndex = 13;
            this.textbox_to.Text = "END";
            this.textbox_to.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.textbox_to.TextChanged += new System.EventHandler(this.RangeUpdate);
            // 
            // textbox_from
            // 
            this.textbox_from.Location = new System.Drawing.Point(7, 30);
            this.textbox_from.Name = "textbox_from";
            this.textbox_from.Size = new System.Drawing.Size(100, 25);
            this.textbox_from.TabIndex = 12;
            this.textbox_from.Text = "START";
            this.textbox_from.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.textbox_from.TextChanged += new System.EventHandler(this.RangeUpdate);
            // 
            // form_comic_range_input
            // 
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Inherit;
            this.ClientSize = new System.Drawing.Size(412, 408);
            this.Controls.Add(this.bun_flat_btn_go);
            this.Controls.Add(this.lab_range);
            this.Controls.Add(this.lab_end_range);
            this.Controls.Add(this.lab_init_range);
            this.Controls.Add(this.lab_num_results);
            this.Controls.Add(this.rich_textbox_url_list);
            this.Controls.Add(this.lab_instruction);
            this.Controls.Add(this.lab_wave_mark);
            this.Controls.Add(this.textbox_to);
            this.Controls.Add(this.textbox_from);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.Name = "form_comic_range_input";
            this.ShowIcon = false;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
            this.Text = "Range Input";
            this.ResumeLayout(false);
            this.PerformLayout();
        }

        #endregion

        private Bunifu.Framework.UI.BunifuFlatButton bun_flat_btn_go;
        private System.Windows.Forms.Label lab_range;
        private System.Windows.Forms.Label lab_end_range;
        private System.Windows.Forms.Label lab_init_range;
        public System.Windows.Forms.Label lab_num_results;
        public System.Windows.Forms.RichTextBox rich_textbox_url_list;
        public System.Windows.Forms.Label lab_instruction;
        private System.Windows.Forms.Label lab_wave_mark;
        private System.Windows.Forms.TextBox textbox_to;
        private System.Windows.Forms.TextBox textbox_from;
    }
}