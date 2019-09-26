namespace ComicDownloader.supporting
{
    partial class UC_search_result
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

        #region Component Designer generated code

        /// <summary> 
        /// Required method for Designer support - do not modify 
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(UC_search_result));
            this.bun_falt_btn_download = new Bunifu.Framework.UI.BunifuFlatButton();
            this.lab_total_eps = new System.Windows.Forms.Label();
            this.rich_textbox_description = new System.Windows.Forms.RichTextBox();
            this.lab_day = new System.Windows.Forms.Label();
            this.lab_author = new System.Windows.Forms.Label();
            this.lab_last_update = new System.Windows.Forms.Label();
            this.pict_box_main = new System.Windows.Forms.PictureBox();
            this.lab_main = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.pict_box_main)).BeginInit();
            this.SuspendLayout();
            // 
            // bun_falt_btn_download
            // 
            this.bun_falt_btn_download.Activecolor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_falt_btn_download.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_falt_btn_download.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.bun_falt_btn_download.BorderRadius = 0;
            this.bun_falt_btn_download.ButtonText = "";
            this.bun_falt_btn_download.Cursor = System.Windows.Forms.Cursors.Hand;
            this.bun_falt_btn_download.DisabledColor = System.Drawing.Color.Gray;
            this.bun_falt_btn_download.Iconcolor = System.Drawing.Color.Transparent;
            this.bun_falt_btn_download.Iconimage = ((System.Drawing.Image)(resources.GetObject("bun_falt_btn_download.Iconimage")));
            this.bun_falt_btn_download.Iconimage_right = null;
            this.bun_falt_btn_download.Iconimage_right_Selected = null;
            this.bun_falt_btn_download.Iconimage_Selected = null;
            this.bun_falt_btn_download.IconMarginLeft = 0;
            this.bun_falt_btn_download.IconMarginRight = 0;
            this.bun_falt_btn_download.IconRightVisible = true;
            this.bun_falt_btn_download.IconRightZoom = 0D;
            this.bun_falt_btn_download.IconVisible = true;
            this.bun_falt_btn_download.IconZoom = 100D;
            this.bun_falt_btn_download.IsTab = true;
            this.bun_falt_btn_download.Location = new System.Drawing.Point(987, 97);
            this.bun_falt_btn_download.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.bun_falt_btn_download.Name = "bun_falt_btn_download";
            this.bun_falt_btn_download.Normalcolor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_falt_btn_download.OnHovercolor = System.Drawing.Color.FromArgb(((int)(((byte)(36)))), ((int)(((byte)(129)))), ((int)(((byte)(77)))));
            this.bun_falt_btn_download.OnHoverTextColor = System.Drawing.Color.White;
            this.bun_falt_btn_download.selected = false;
            this.bun_falt_btn_download.Size = new System.Drawing.Size(50, 50);
            this.bun_falt_btn_download.TabIndex = 18;
            this.bun_falt_btn_download.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.bun_falt_btn_download.Textcolor = System.Drawing.Color.White;
            this.bun_falt_btn_download.TextFont = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bun_falt_btn_download.Click += new System.EventHandler(this.Bun_falt_btn_download_Click);
            // 
            // lab_total_eps
            // 
            this.lab_total_eps.AutoSize = true;
            this.lab_total_eps.Location = new System.Drawing.Point(180, 121);
            this.lab_total_eps.Name = "lab_total_eps";
            this.lab_total_eps.Size = new System.Drawing.Size(134, 15);
            this.lab_total_eps.TabIndex = 17;
            this.lab_total_eps.Text = "total episodes: 420";
            // 
            // rich_textbox_description
            // 
            this.rich_textbox_description.BackColor = System.Drawing.SystemColors.ControlLight;
            this.rich_textbox_description.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.rich_textbox_description.Font = new System.Drawing.Font("Gulim", 10F);
            this.rich_textbox_description.Location = new System.Drawing.Point(420, 45);
            this.rich_textbox_description.Name = "rich_textbox_description";
            this.rich_textbox_description.ReadOnly = true;
            this.rich_textbox_description.ScrollBars = System.Windows.Forms.RichTextBoxScrollBars.Vertical;
            this.rich_textbox_description.Size = new System.Drawing.Size(539, 95);
            this.rich_textbox_description.TabIndex = 16;
            this.rich_textbox_description.Text = "";
            // 
            // lab_day
            // 
            this.lab_day.AutoSize = true;
            this.lab_day.Location = new System.Drawing.Point(180, 70);
            this.lab_day.Name = "lab_day";
            this.lab_day.Size = new System.Drawing.Size(161, 15);
            this.lab_day.TabIndex = 15;
            this.lab_day.Text = "day of update: Monday";
            // 
            // lab_author
            // 
            this.lab_author.AutoSize = true;
            this.lab_author.Location = new System.Drawing.Point(180, 44);
            this.lab_author.Name = "lab_author";
            this.lab_author.Size = new System.Drawing.Size(133, 15);
            this.lab_author.TabIndex = 14;
            this.lab_author.Text = "Author: XXXX/YYYY";
            // 
            // lab_last_update
            // 
            this.lab_last_update.AutoSize = true;
            this.lab_last_update.Location = new System.Drawing.Point(180, 102);
            this.lab_last_update.Name = "lab_last_update";
            this.lab_last_update.Size = new System.Drawing.Size(176, 15);
            this.lab_last_update.TabIndex = 13;
            this.lab_last_update.Text = "Last Update: 2019-05-27";
            // 
            // pict_box_main
            // 
            this.pict_box_main.Location = new System.Drawing.Point(10, 10);
            this.pict_box_main.Name = "pict_box_main";
            this.pict_box_main.Size = new System.Drawing.Size(160, 130);
            this.pict_box_main.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pict_box_main.TabIndex = 12;
            this.pict_box_main.TabStop = false;
            // 
            // lab_main
            // 
            this.lab_main.AutoSize = true;
            this.lab_main.Font = new System.Drawing.Font("Gulim", 18F);
            this.lab_main.Location = new System.Drawing.Point(180, 5);
            this.lab_main.Name = "lab_main";
            this.lab_main.Size = new System.Drawing.Size(70, 30);
            this.lab_main.TabIndex = 11;
            this.lab_main.Text = "Title";
            // 
            // UC_search_result
            // 
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Inherit;
            this.BackColor = System.Drawing.SystemColors.ControlLight;
            this.Controls.Add(this.bun_falt_btn_download);
            this.Controls.Add(this.lab_total_eps);
            this.Controls.Add(this.rich_textbox_description);
            this.Controls.Add(this.lab_day);
            this.Controls.Add(this.lab_author);
            this.Controls.Add(this.lab_last_update);
            this.Controls.Add(this.pict_box_main);
            this.Controls.Add(this.lab_main);
            this.Name = "UC_search_result";
            this.Size = new System.Drawing.Size(1040, 150);
            ((System.ComponentModel.ISupportInitialize)(this.pict_box_main)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private Bunifu.Framework.UI.BunifuFlatButton bun_falt_btn_download;
        public System.Windows.Forms.Label lab_total_eps;
        public System.Windows.Forms.RichTextBox rich_textbox_description;
        public System.Windows.Forms.Label lab_day;
        public System.Windows.Forms.Label lab_author;
        public System.Windows.Forms.Label lab_last_update;
        public System.Windows.Forms.PictureBox pict_box_main;
        public System.Windows.Forms.Label lab_main;
    }
}
