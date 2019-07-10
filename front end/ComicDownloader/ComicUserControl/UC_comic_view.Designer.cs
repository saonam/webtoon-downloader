namespace ComicDownloader.ComicUserControl
{
    partial class UC_comic_view
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
            this.bun_flat_btn_view = new Bunifu.Framework.UI.BunifuFlatButton();
            this.open_file_dialog = new System.Windows.Forms.OpenFileDialog();
            this.SuspendLayout();
            // 
            // bun_flat_btn_view
            // 
            this.bun_flat_btn_view.Activecolor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_flat_btn_view.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_flat_btn_view.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.bun_flat_btn_view.BorderRadius = 0;
            this.bun_flat_btn_view.ButtonText = "View";
            this.bun_flat_btn_view.Cursor = System.Windows.Forms.Cursors.Hand;
            this.bun_flat_btn_view.DisabledColor = System.Drawing.Color.Gray;
            this.bun_flat_btn_view.Iconcolor = System.Drawing.Color.Transparent;
            this.bun_flat_btn_view.Iconimage = null;
            this.bun_flat_btn_view.Iconimage_right = null;
            this.bun_flat_btn_view.Iconimage_right_Selected = null;
            this.bun_flat_btn_view.Iconimage_Selected = null;
            this.bun_flat_btn_view.IconMarginLeft = 0;
            this.bun_flat_btn_view.IconMarginRight = 0;
            this.bun_flat_btn_view.IconRightVisible = true;
            this.bun_flat_btn_view.IconRightZoom = 0D;
            this.bun_flat_btn_view.IconVisible = true;
            this.bun_flat_btn_view.IconZoom = 90D;
            this.bun_flat_btn_view.IsTab = false;
            this.bun_flat_btn_view.Location = new System.Drawing.Point(4, 3);
            this.bun_flat_btn_view.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.bun_flat_btn_view.Name = "bun_flat_btn_view";
            this.bun_flat_btn_view.Normalcolor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_flat_btn_view.OnHovercolor = System.Drawing.Color.FromArgb(((int)(((byte)(36)))), ((int)(((byte)(129)))), ((int)(((byte)(77)))));
            this.bun_flat_btn_view.OnHoverTextColor = System.Drawing.Color.White;
            this.bun_flat_btn_view.selected = false;
            this.bun_flat_btn_view.Size = new System.Drawing.Size(321, 55);
            this.bun_flat_btn_view.TabIndex = 1;
            this.bun_flat_btn_view.Text = "View";
            this.bun_flat_btn_view.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.bun_flat_btn_view.Textcolor = System.Drawing.Color.White;
            this.bun_flat_btn_view.TextFont = new System.Drawing.Font("Microsoft Sans Serif", 12F);
            this.bun_flat_btn_view.Click += new System.EventHandler(this.Bun_flat_btn_view_Click);
            // 
            // open_file_dialog
            // 
            this.open_file_dialog.FileName = "open_file_dialog";
            this.open_file_dialog.Filter = "PNG Image|*.png, *.jpg, *.bmp";
            this.open_file_dialog.ShowHelp = true;
            this.open_file_dialog.ShowReadOnly = true;
            // 
            // UC_comic_view
            // 
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Inherit;
            this.Controls.Add(this.bun_flat_btn_view);
            this.Name = "UC_comic_view";
            this.Size = new System.Drawing.Size(1050, 715);
            this.Load += new System.EventHandler(this.UC_comic_view_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private Bunifu.Framework.UI.BunifuFlatButton bun_flat_btn_view;
        public System.Windows.Forms.OpenFileDialog open_file_dialog;
    }
}
