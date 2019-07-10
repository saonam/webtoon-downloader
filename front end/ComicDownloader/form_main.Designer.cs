namespace ComicDownloader
{
    partial class form_main
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
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(form_main));
            this.bun_flat_btn_view_tab = new Bunifu.Framework.UI.BunifuFlatButton();
            this.bun_flat_btn_downloading_tab = new Bunifu.Framework.UI.BunifuFlatButton();
            this.bun_flat_btn_search_tab = new Bunifu.Framework.UI.BunifuFlatButton();
            this.bun_flat_btn_show_error = new Bunifu.Framework.UI.BunifuFlatButton();
            this.bun_elipse = new Bunifu.Framework.UI.BunifuElipse(this.components);
            this.pan_drag = new System.Windows.Forms.Panel();
            this.bun_flat_btn_settings = new Bunifu.Framework.UI.BunifuFlatButton();
            this.bun_fat_btn_close = new Bunifu.Framework.UI.BunifuFlatButton();
            this.bun_drag_control_main = new Bunifu.Framework.UI.BunifuDragControl(this.components);
            this.form_UC_comic_search = new ComicDownloader.ComicUserControl.UC_comic_search();
            this.form_UC_comic_downloading = new ComicDownloader.ComicUserControl.UC_comic_downloading();
            this.form_UC_comic_view = new ComicDownloader.ComicUserControl.UC_comic_view();
            this.form_UC_menu = new ComicDownloader.ComicUserControl.supporting.UC_menu();
            this.pan_drag.SuspendLayout();
            this.SuspendLayout();
            // 
            // bun_flat_btn_view_tab
            // 
            this.bun_flat_btn_view_tab.Activecolor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_flat_btn_view_tab.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_flat_btn_view_tab.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.bun_flat_btn_view_tab.BorderRadius = 0;
            this.bun_flat_btn_view_tab.ButtonText = "View";
            this.bun_flat_btn_view_tab.Cursor = System.Windows.Forms.Cursors.Hand;
            this.bun_flat_btn_view_tab.DisabledColor = System.Drawing.Color.Gray;
            this.bun_flat_btn_view_tab.Iconcolor = System.Drawing.Color.Transparent;
            this.bun_flat_btn_view_tab.Iconimage = null;
            this.bun_flat_btn_view_tab.Iconimage_right = null;
            this.bun_flat_btn_view_tab.Iconimage_right_Selected = null;
            this.bun_flat_btn_view_tab.Iconimage_Selected = null;
            this.bun_flat_btn_view_tab.IconMarginLeft = 0;
            this.bun_flat_btn_view_tab.IconMarginRight = 0;
            this.bun_flat_btn_view_tab.IconRightVisible = true;
            this.bun_flat_btn_view_tab.IconRightZoom = 0D;
            this.bun_flat_btn_view_tab.IconVisible = true;
            this.bun_flat_btn_view_tab.IconZoom = 90D;
            this.bun_flat_btn_view_tab.IsTab = false;
            this.bun_flat_btn_view_tab.Location = new System.Drawing.Point(640, 755);
            this.bun_flat_btn_view_tab.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.bun_flat_btn_view_tab.Name = "bun_flat_btn_view_tab";
            this.bun_flat_btn_view_tab.Normalcolor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_flat_btn_view_tab.OnHovercolor = System.Drawing.Color.FromArgb(((int)(((byte)(36)))), ((int)(((byte)(129)))), ((int)(((byte)(77)))));
            this.bun_flat_btn_view_tab.OnHoverTextColor = System.Drawing.Color.White;
            this.bun_flat_btn_view_tab.selected = false;
            this.bun_flat_btn_view_tab.Size = new System.Drawing.Size(321, 46);
            this.bun_flat_btn_view_tab.TabIndex = 12;
            this.bun_flat_btn_view_tab.Text = "View";
            this.bun_flat_btn_view_tab.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.bun_flat_btn_view_tab.Textcolor = System.Drawing.Color.White;
            this.bun_flat_btn_view_tab.TextFont = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bun_flat_btn_view_tab.Click += new System.EventHandler(this.Bun_flat_btn_view_tab_Click);
            // 
            // bun_flat_btn_downloading_tab
            // 
            this.bun_flat_btn_downloading_tab.Activecolor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_flat_btn_downloading_tab.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_flat_btn_downloading_tab.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.bun_flat_btn_downloading_tab.BorderRadius = 0;
            this.bun_flat_btn_downloading_tab.ButtonText = "Downloading";
            this.bun_flat_btn_downloading_tab.Cursor = System.Windows.Forms.Cursors.Hand;
            this.bun_flat_btn_downloading_tab.DisabledColor = System.Drawing.Color.Gray;
            this.bun_flat_btn_downloading_tab.Iconcolor = System.Drawing.Color.Transparent;
            this.bun_flat_btn_downloading_tab.Iconimage = null;
            this.bun_flat_btn_downloading_tab.Iconimage_right = null;
            this.bun_flat_btn_downloading_tab.Iconimage_right_Selected = null;
            this.bun_flat_btn_downloading_tab.Iconimage_Selected = null;
            this.bun_flat_btn_downloading_tab.IconMarginLeft = 0;
            this.bun_flat_btn_downloading_tab.IconMarginRight = 0;
            this.bun_flat_btn_downloading_tab.IconRightVisible = true;
            this.bun_flat_btn_downloading_tab.IconRightZoom = 0D;
            this.bun_flat_btn_downloading_tab.IconVisible = true;
            this.bun_flat_btn_downloading_tab.IconZoom = 90D;
            this.bun_flat_btn_downloading_tab.IsTab = false;
            this.bun_flat_btn_downloading_tab.Location = new System.Drawing.Point(320, 755);
            this.bun_flat_btn_downloading_tab.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.bun_flat_btn_downloading_tab.Name = "bun_flat_btn_downloading_tab";
            this.bun_flat_btn_downloading_tab.Normalcolor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_flat_btn_downloading_tab.OnHovercolor = System.Drawing.Color.FromArgb(((int)(((byte)(36)))), ((int)(((byte)(129)))), ((int)(((byte)(77)))));
            this.bun_flat_btn_downloading_tab.OnHoverTextColor = System.Drawing.Color.White;
            this.bun_flat_btn_downloading_tab.selected = false;
            this.bun_flat_btn_downloading_tab.Size = new System.Drawing.Size(321, 46);
            this.bun_flat_btn_downloading_tab.TabIndex = 11;
            this.bun_flat_btn_downloading_tab.Text = "Downloading";
            this.bun_flat_btn_downloading_tab.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.bun_flat_btn_downloading_tab.Textcolor = System.Drawing.Color.White;
            this.bun_flat_btn_downloading_tab.TextFont = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bun_flat_btn_downloading_tab.Click += new System.EventHandler(this.Bun_flat_btn_downloading_tab_Click);
            // 
            // bun_flat_btn_search_tab
            // 
            this.bun_flat_btn_search_tab.Activecolor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_flat_btn_search_tab.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_flat_btn_search_tab.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.bun_flat_btn_search_tab.BorderRadius = 0;
            this.bun_flat_btn_search_tab.ButtonText = "Search";
            this.bun_flat_btn_search_tab.Cursor = System.Windows.Forms.Cursors.Hand;
            this.bun_flat_btn_search_tab.DisabledColor = System.Drawing.Color.Gray;
            this.bun_flat_btn_search_tab.Iconcolor = System.Drawing.Color.Transparent;
            this.bun_flat_btn_search_tab.Iconimage = null;
            this.bun_flat_btn_search_tab.Iconimage_right = null;
            this.bun_flat_btn_search_tab.Iconimage_right_Selected = null;
            this.bun_flat_btn_search_tab.Iconimage_Selected = null;
            this.bun_flat_btn_search_tab.IconMarginLeft = 0;
            this.bun_flat_btn_search_tab.IconMarginRight = 0;
            this.bun_flat_btn_search_tab.IconRightVisible = true;
            this.bun_flat_btn_search_tab.IconRightZoom = 0D;
            this.bun_flat_btn_search_tab.IconVisible = true;
            this.bun_flat_btn_search_tab.IconZoom = 90D;
            this.bun_flat_btn_search_tab.IsTab = false;
            this.bun_flat_btn_search_tab.Location = new System.Drawing.Point(0, 755);
            this.bun_flat_btn_search_tab.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.bun_flat_btn_search_tab.Name = "bun_flat_btn_search_tab";
            this.bun_flat_btn_search_tab.Normalcolor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_flat_btn_search_tab.OnHovercolor = System.Drawing.Color.FromArgb(((int)(((byte)(36)))), ((int)(((byte)(129)))), ((int)(((byte)(77)))));
            this.bun_flat_btn_search_tab.OnHoverTextColor = System.Drawing.Color.White;
            this.bun_flat_btn_search_tab.selected = false;
            this.bun_flat_btn_search_tab.Size = new System.Drawing.Size(321, 46);
            this.bun_flat_btn_search_tab.TabIndex = 10;
            this.bun_flat_btn_search_tab.Text = "Search";
            this.bun_flat_btn_search_tab.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.bun_flat_btn_search_tab.Textcolor = System.Drawing.Color.White;
            this.bun_flat_btn_search_tab.TextFont = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bun_flat_btn_search_tab.Click += new System.EventHandler(this.Bun_flat_btn_search_tab_Click);
            // 
            // bun_flat_btn_show_error
            // 
            this.bun_flat_btn_show_error.Activecolor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_flat_btn_show_error.BackColor = System.Drawing.Color.SeaGreen;
            this.bun_flat_btn_show_error.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.bun_flat_btn_show_error.BorderRadius = 0;
            this.bun_flat_btn_show_error.ButtonText = "Show Error";
            this.bun_flat_btn_show_error.Cursor = System.Windows.Forms.Cursors.Hand;
            this.bun_flat_btn_show_error.DisabledColor = System.Drawing.Color.Gray;
            this.bun_flat_btn_show_error.Iconcolor = System.Drawing.Color.Transparent;
            this.bun_flat_btn_show_error.Iconimage = null;
            this.bun_flat_btn_show_error.Iconimage_right = null;
            this.bun_flat_btn_show_error.Iconimage_right_Selected = null;
            this.bun_flat_btn_show_error.Iconimage_Selected = null;
            this.bun_flat_btn_show_error.IconMarginLeft = 0;
            this.bun_flat_btn_show_error.IconMarginRight = 0;
            this.bun_flat_btn_show_error.IconRightVisible = true;
            this.bun_flat_btn_show_error.IconRightZoom = 0D;
            this.bun_flat_btn_show_error.IconVisible = true;
            this.bun_flat_btn_show_error.IconZoom = 90D;
            this.bun_flat_btn_show_error.IsTab = false;
            this.bun_flat_btn_show_error.Location = new System.Drawing.Point(960, 755);
            this.bun_flat_btn_show_error.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.bun_flat_btn_show_error.Name = "bun_flat_btn_show_error";
            this.bun_flat_btn_show_error.Normalcolor = System.Drawing.Color.SeaGreen;
            this.bun_flat_btn_show_error.OnHovercolor = System.Drawing.Color.FromArgb(((int)(((byte)(36)))), ((int)(((byte)(129)))), ((int)(((byte)(77)))));
            this.bun_flat_btn_show_error.OnHoverTextColor = System.Drawing.Color.White;
            this.bun_flat_btn_show_error.selected = false;
            this.bun_flat_btn_show_error.Size = new System.Drawing.Size(91, 46);
            this.bun_flat_btn_show_error.TabIndex = 9;
            this.bun_flat_btn_show_error.Text = "Show Error";
            this.bun_flat_btn_show_error.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.bun_flat_btn_show_error.Textcolor = System.Drawing.Color.White;
            this.bun_flat_btn_show_error.TextFont = new System.Drawing.Font("Microsoft Sans Serif", 9F);
            this.bun_flat_btn_show_error.Click += new System.EventHandler(this.Bun_flat_btn_show_error_Click);
            // 
            // bun_elipse
            // 
            this.bun_elipse.ElipseRadius = 15;
            this.bun_elipse.TargetControl = this;
            // 
            // pan_drag
            // 
            this.pan_drag.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.pan_drag.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(35)))), ((int)(((byte)(35)))), ((int)(((byte)(35)))));
            this.pan_drag.Controls.Add(this.bun_flat_btn_settings);
            this.pan_drag.Controls.Add(this.bun_fat_btn_close);
            this.pan_drag.Location = new System.Drawing.Point(0, 0);
            this.pan_drag.Name = "pan_drag";
            this.pan_drag.Size = new System.Drawing.Size(1050, 40);
            this.pan_drag.TabIndex = 15;
            // 
            // bun_flat_btn_settings
            // 
            this.bun_flat_btn_settings.Activecolor = System.Drawing.Color.FromArgb(((int)(((byte)(60)))), ((int)(((byte)(60)))), ((int)(((byte)(60)))));
            this.bun_flat_btn_settings.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(40)))), ((int)(((byte)(40)))), ((int)(((byte)(40)))));
            this.bun_flat_btn_settings.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("bun_flat_btn_settings.BackgroundImage")));
            this.bun_flat_btn_settings.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.bun_flat_btn_settings.BorderRadius = 0;
            this.bun_flat_btn_settings.ButtonText = "";
            this.bun_flat_btn_settings.Cursor = System.Windows.Forms.Cursors.Hand;
            this.bun_flat_btn_settings.DisabledColor = System.Drawing.Color.Gray;
            this.bun_flat_btn_settings.Iconcolor = System.Drawing.Color.Transparent;
            this.bun_flat_btn_settings.Iconimage = null;
            this.bun_flat_btn_settings.Iconimage_right = null;
            this.bun_flat_btn_settings.Iconimage_right_Selected = null;
            this.bun_flat_btn_settings.Iconimage_Selected = null;
            this.bun_flat_btn_settings.IconMarginLeft = 0;
            this.bun_flat_btn_settings.IconMarginRight = 0;
            this.bun_flat_btn_settings.IconRightVisible = true;
            this.bun_flat_btn_settings.IconRightZoom = 0D;
            this.bun_flat_btn_settings.IconVisible = true;
            this.bun_flat_btn_settings.IconZoom = 90D;
            this.bun_flat_btn_settings.IsTab = false;
            this.bun_flat_btn_settings.Location = new System.Drawing.Point(0, 0);
            this.bun_flat_btn_settings.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.bun_flat_btn_settings.Name = "bun_flat_btn_settings";
            this.bun_flat_btn_settings.Normalcolor = System.Drawing.Color.FromArgb(((int)(((byte)(40)))), ((int)(((byte)(40)))), ((int)(((byte)(40)))));
            this.bun_flat_btn_settings.OnHovercolor = System.Drawing.Color.FromArgb(((int)(((byte)(50)))), ((int)(((byte)(50)))), ((int)(((byte)(50)))));
            this.bun_flat_btn_settings.OnHoverTextColor = System.Drawing.Color.White;
            this.bun_flat_btn_settings.selected = false;
            this.bun_flat_btn_settings.Size = new System.Drawing.Size(40, 40);
            this.bun_flat_btn_settings.TabIndex = 2;
            this.bun_flat_btn_settings.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.bun_flat_btn_settings.Textcolor = System.Drawing.Color.White;
            this.bun_flat_btn_settings.TextFont = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bun_flat_btn_settings.Click += new System.EventHandler(this.Bun_flat_btn_settings_Click);
            // 
            // bun_fat_btn_close
            // 
            this.bun_fat_btn_close.Activecolor = System.Drawing.Color.FromArgb(((int)(((byte)(240)))), ((int)(((byte)(40)))), ((int)(((byte)(80)))));
            this.bun_fat_btn_close.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(35)))), ((int)(((byte)(35)))), ((int)(((byte)(35)))));
            this.bun_fat_btn_close.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.bun_fat_btn_close.BorderRadius = 0;
            this.bun_fat_btn_close.ButtonText = "";
            this.bun_fat_btn_close.Cursor = System.Windows.Forms.Cursors.Hand;
            this.bun_fat_btn_close.DisabledColor = System.Drawing.Color.Gray;
            this.bun_fat_btn_close.Iconcolor = System.Drawing.Color.Transparent;
            this.bun_fat_btn_close.Iconimage = ((System.Drawing.Image)(resources.GetObject("bun_fat_btn_close.Iconimage")));
            this.bun_fat_btn_close.Iconimage_right = null;
            this.bun_fat_btn_close.Iconimage_right_Selected = null;
            this.bun_fat_btn_close.Iconimage_Selected = null;
            this.bun_fat_btn_close.IconMarginLeft = 0;
            this.bun_fat_btn_close.IconMarginRight = 0;
            this.bun_fat_btn_close.IconRightVisible = true;
            this.bun_fat_btn_close.IconRightZoom = 0D;
            this.bun_fat_btn_close.IconVisible = true;
            this.bun_fat_btn_close.IconZoom = 50D;
            this.bun_fat_btn_close.IsTab = false;
            this.bun_fat_btn_close.Location = new System.Drawing.Point(1010, 0);
            this.bun_fat_btn_close.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.bun_fat_btn_close.Name = "bun_fat_btn_close";
            this.bun_fat_btn_close.Normalcolor = System.Drawing.Color.FromArgb(((int)(((byte)(35)))), ((int)(((byte)(35)))), ((int)(((byte)(35)))));
            this.bun_fat_btn_close.OnHovercolor = System.Drawing.Color.Crimson;
            this.bun_fat_btn_close.OnHoverTextColor = System.Drawing.Color.White;
            this.bun_fat_btn_close.selected = false;
            this.bun_fat_btn_close.Size = new System.Drawing.Size(41, 41);
            this.bun_fat_btn_close.TabIndex = 1;
            this.bun_fat_btn_close.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.bun_fat_btn_close.Textcolor = System.Drawing.Color.White;
            this.bun_fat_btn_close.TextFont = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bun_fat_btn_close.Click += new System.EventHandler(this.Bun_fat_btn_close_Click);
            // 
            // bun_drag_control_main
            // 
            this.bun_drag_control_main.Fixed = true;
            this.bun_drag_control_main.Horizontal = true;
            this.bun_drag_control_main.TargetControl = this.pan_drag;
            this.bun_drag_control_main.Vertical = true;
            // 
            // form_UC_comic_search
            // 
            this.form_UC_comic_search.errorString = "There are  no error so far";
            this.form_UC_comic_search.Location = new System.Drawing.Point(0, 40);
            this.form_UC_comic_search.Name = "form_UC_comic_search";
            this.form_UC_comic_search.Size = new System.Drawing.Size(1050, 715);
            this.form_UC_comic_search.TabIndex = 13;
            // 
            // form_UC_comic_downloading
            // 
            this.form_UC_comic_downloading.Location = new System.Drawing.Point(0, 40);
            this.form_UC_comic_downloading.Name = "form_UC_comic_downloading";
            this.form_UC_comic_downloading.Size = new System.Drawing.Size(1050, 715);
            this.form_UC_comic_downloading.TabIndex = 14;
            // 
            // form_UC_comic_view
            // 
            this.form_UC_comic_view.Location = new System.Drawing.Point(0, 40);
            this.form_UC_comic_view.Name = "form_UC_comic_view";
            this.form_UC_comic_view.Size = new System.Drawing.Size(1050, 715);
            this.form_UC_comic_view.TabIndex = 16;
            // 
            // form_UC_menu
            // 
            this.form_UC_menu.Location = new System.Drawing.Point(0, 40);
            this.form_UC_menu.Name = "form_UC_menu";
            this.form_UC_menu.Size = new System.Drawing.Size(1050, 715);
            this.form_UC_menu.TabIndex = 17;
            // 
            // form_main
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(120F, 120F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Dpi;
            this.ClientSize = new System.Drawing.Size(1050, 800);
            this.Controls.Add(this.pan_drag);
            this.Controls.Add(this.form_UC_comic_search);
            this.Controls.Add(this.bun_flat_btn_view_tab);
            this.Controls.Add(this.bun_flat_btn_downloading_tab);
            this.Controls.Add(this.bun_flat_btn_search_tab);
            this.Controls.Add(this.bun_flat_btn_show_error);
            this.Controls.Add(this.form_UC_comic_downloading);
            this.Controls.Add(this.form_UC_comic_view);
            this.Controls.Add(this.form_UC_menu);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "form_main";
            this.pan_drag.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private Bunifu.Framework.UI.BunifuFlatButton bun_flat_btn_view_tab;
        private Bunifu.Framework.UI.BunifuFlatButton bun_flat_btn_downloading_tab;
        private Bunifu.Framework.UI.BunifuFlatButton bun_flat_btn_search_tab;
        private Bunifu.Framework.UI.BunifuFlatButton bun_flat_btn_show_error;
        private ComicUserControl.UC_comic_search form_UC_comic_search;
        private ComicUserControl.UC_comic_downloading form_UC_comic_downloading;
        public Bunifu.Framework.UI.BunifuElipse bun_elipse;
        private System.Windows.Forms.Panel pan_drag;
        private Bunifu.Framework.UI.BunifuFlatButton bun_fat_btn_close;
        public Bunifu.Framework.UI.BunifuDragControl bun_drag_control_main;
        private ComicUserControl.UC_comic_view form_UC_comic_view;
        private Bunifu.Framework.UI.BunifuFlatButton bun_flat_btn_settings;
        private ComicUserControl.supporting.UC_menu form_UC_menu;
    }
}

