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
            this.bun_flat_btn_show_error = new Bunifu.Framework.UI.BunifuFlatButton();
            this.bun_elipse = new Bunifu.Framework.UI.BunifuElipse(this.components);
            this.pan_drag = new System.Windows.Forms.Panel();
            this.lab_main = new System.Windows.Forms.Label();
            this.bun_flat_btn_minimize = new Bunifu.Framework.UI.BunifuFlatButton();
            this.bun_flat_btn_view = new Bunifu.Framework.UI.BunifuFlatButton();
            this.bun_fat_btn_close = new Bunifu.Framework.UI.BunifuFlatButton();
            this.bun_drag_control_main = new Bunifu.Framework.UI.BunifuDragControl(this.components);
            this.open_file_dialog = new System.Windows.Forms.OpenFileDialog();
            this.bun_dropdown_source = new Bunifu.Framework.UI.BunifuDropdown();
            this.bun_mat_textbox_search = new Bunifu.Framework.UI.BunifuMaterialTextbox();
            this.rich_textbox_status = new System.Windows.Forms.RichTextBox();
            this.bun_flat_btn_search = new Bunifu.Framework.UI.BunifuFlatButton();
            this.flow_layout_panel_main = new System.Windows.Forms.FlowLayoutPanel();
            this.bun_drag_control_sub = new Bunifu.Framework.UI.BunifuDragControl(this.components);
            this.pan_drag.SuspendLayout();
            this.SuspendLayout();
            // 
            // bun_flat_btn_show_error
            // 
            this.bun_flat_btn_show_error.Activecolor = System.Drawing.Color.FromArgb(((int)(((byte)(35)))), ((int)(((byte)(35)))), ((int)(((byte)(35)))));
            this.bun_flat_btn_show_error.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(35)))), ((int)(((byte)(35)))), ((int)(((byte)(35)))));
            this.bun_flat_btn_show_error.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.bun_flat_btn_show_error.BorderRadius = 0;
            this.bun_flat_btn_show_error.ButtonText = "Show Error";
            this.bun_flat_btn_show_error.Cursor = System.Windows.Forms.Cursors.Hand;
            this.bun_flat_btn_show_error.DisabledColor = System.Drawing.Color.Gray;
            this.bun_flat_btn_show_error.ForeColor = System.Drawing.SystemColors.Control;
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
            this.bun_flat_btn_show_error.Location = new System.Drawing.Point(880, 0);
            this.bun_flat_btn_show_error.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.bun_flat_btn_show_error.Name = "bun_flat_btn_show_error";
            this.bun_flat_btn_show_error.Normalcolor = System.Drawing.Color.FromArgb(((int)(((byte)(35)))), ((int)(((byte)(35)))), ((int)(((byte)(35)))));
            this.bun_flat_btn_show_error.OnHovercolor = System.Drawing.SystemColors.ControlDark;
            this.bun_flat_btn_show_error.OnHoverTextColor = System.Drawing.Color.White;
            this.bun_flat_btn_show_error.selected = false;
            this.bun_flat_btn_show_error.Size = new System.Drawing.Size(90, 41);
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
            this.pan_drag.Controls.Add(this.lab_main);
            this.pan_drag.Controls.Add(this.bun_flat_btn_minimize);
            this.pan_drag.Controls.Add(this.bun_flat_btn_view);
            this.pan_drag.Controls.Add(this.bun_flat_btn_show_error);
            this.pan_drag.Controls.Add(this.bun_fat_btn_close);
            this.pan_drag.ForeColor = System.Drawing.SystemColors.Control;
            this.pan_drag.Location = new System.Drawing.Point(0, 0);
            this.pan_drag.Name = "pan_drag";
            this.pan_drag.Size = new System.Drawing.Size(1050, 40);
            this.pan_drag.TabIndex = 15;
            // 
            // lab_main
            // 
            this.lab_main.Font = new System.Drawing.Font("Gulim", 16F);
            this.lab_main.Location = new System.Drawing.Point(0, 0);
            this.lab_main.Name = "lab_main";
            this.lab_main.Size = new System.Drawing.Size(320, 40);
            this.lab_main.TabIndex = 12;
            this.lab_main.Text = "Comic Downloader v2.2";
            this.lab_main.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // bun_flat_btn_minimize
            // 
            this.bun_flat_btn_minimize.Activecolor = System.Drawing.SystemColors.HotTrack;
            this.bun_flat_btn_minimize.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(35)))), ((int)(((byte)(35)))), ((int)(((byte)(35)))));
            this.bun_flat_btn_minimize.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.bun_flat_btn_minimize.BorderRadius = 0;
            this.bun_flat_btn_minimize.ButtonText = "";
            this.bun_flat_btn_minimize.Cursor = System.Windows.Forms.Cursors.Hand;
            this.bun_flat_btn_minimize.DisabledColor = System.Drawing.Color.Gray;
            this.bun_flat_btn_minimize.Iconcolor = System.Drawing.Color.Transparent;
            this.bun_flat_btn_minimize.Iconimage = ((System.Drawing.Image)(resources.GetObject("bun_flat_btn_minimize.Iconimage")));
            this.bun_flat_btn_minimize.Iconimage_right = null;
            this.bun_flat_btn_minimize.Iconimage_right_Selected = null;
            this.bun_flat_btn_minimize.Iconimage_Selected = null;
            this.bun_flat_btn_minimize.IconMarginLeft = 0;
            this.bun_flat_btn_minimize.IconMarginRight = 0;
            this.bun_flat_btn_minimize.IconRightVisible = true;
            this.bun_flat_btn_minimize.IconRightZoom = 0D;
            this.bun_flat_btn_minimize.IconVisible = true;
            this.bun_flat_btn_minimize.IconZoom = 50D;
            this.bun_flat_btn_minimize.IsTab = false;
            this.bun_flat_btn_minimize.Location = new System.Drawing.Point(970, 0);
            this.bun_flat_btn_minimize.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.bun_flat_btn_minimize.Name = "bun_flat_btn_minimize";
            this.bun_flat_btn_minimize.Normalcolor = System.Drawing.Color.FromArgb(((int)(((byte)(35)))), ((int)(((byte)(35)))), ((int)(((byte)(35)))));
            this.bun_flat_btn_minimize.OnHovercolor = System.Drawing.SystemColors.HotTrack;
            this.bun_flat_btn_minimize.OnHoverTextColor = System.Drawing.Color.White;
            this.bun_flat_btn_minimize.selected = false;
            this.bun_flat_btn_minimize.Size = new System.Drawing.Size(41, 41);
            this.bun_flat_btn_minimize.TabIndex = 11;
            this.bun_flat_btn_minimize.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.bun_flat_btn_minimize.Textcolor = System.Drawing.Color.White;
            this.bun_flat_btn_minimize.TextFont = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bun_flat_btn_minimize.Click += new System.EventHandler(this.Bun_flat_btn_minimize_Click);
            // 
            // bun_flat_btn_view
            // 
            this.bun_flat_btn_view.Activecolor = System.Drawing.Color.FromArgb(((int)(((byte)(35)))), ((int)(((byte)(35)))), ((int)(((byte)(35)))));
            this.bun_flat_btn_view.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(35)))), ((int)(((byte)(35)))), ((int)(((byte)(35)))));
            this.bun_flat_btn_view.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.bun_flat_btn_view.BorderRadius = 0;
            this.bun_flat_btn_view.ButtonText = "View comic on broewser";
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
            this.bun_flat_btn_view.Location = new System.Drawing.Point(680, 0);
            this.bun_flat_btn_view.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.bun_flat_btn_view.Name = "bun_flat_btn_view";
            this.bun_flat_btn_view.Normalcolor = System.Drawing.Color.FromArgb(((int)(((byte)(35)))), ((int)(((byte)(35)))), ((int)(((byte)(35)))));
            this.bun_flat_btn_view.OnHovercolor = System.Drawing.SystemColors.ControlDarkDark;
            this.bun_flat_btn_view.OnHoverTextColor = System.Drawing.Color.White;
            this.bun_flat_btn_view.selected = false;
            this.bun_flat_btn_view.Size = new System.Drawing.Size(200, 41);
            this.bun_flat_btn_view.TabIndex = 10;
            this.bun_flat_btn_view.Text = "View comic on broewser";
            this.bun_flat_btn_view.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.bun_flat_btn_view.Textcolor = System.Drawing.Color.White;
            this.bun_flat_btn_view.TextFont = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bun_flat_btn_view.Click += new System.EventHandler(this.Bun_flat_btn_view_Click);
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
            // open_file_dialog
            // 
            this.open_file_dialog.FileName = "openFileDialog1";
            // 
            // bun_dropdown_source
            // 
            this.bun_dropdown_source.BackColor = System.Drawing.Color.Transparent;
            this.bun_dropdown_source.BorderRadius = 3;
            this.bun_dropdown_source.Font = new System.Drawing.Font("Source Code Pro", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bun_dropdown_source.ForeColor = System.Drawing.Color.White;
            this.bun_dropdown_source.Items = new string[0];
            this.bun_dropdown_source.Location = new System.Drawing.Point(-1, 84);
            this.bun_dropdown_source.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.bun_dropdown_source.Name = "bun_dropdown_source";
            this.bun_dropdown_source.NomalColor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_dropdown_source.onHoverColor = System.Drawing.Color.FromArgb(((int)(((byte)(36)))), ((int)(((byte)(129)))), ((int)(((byte)(77)))));
            this.bun_dropdown_source.selectedIndex = -1;
            this.bun_dropdown_source.Size = new System.Drawing.Size(245, 40);
            this.bun_dropdown_source.TabIndex = 16;
            // 
            // bun_mat_textbox_search
            // 
            this.bun_mat_textbox_search.BackColor = System.Drawing.SystemColors.Control;
            this.bun_mat_textbox_search.Cursor = System.Windows.Forms.Cursors.IBeam;
            this.bun_mat_textbox_search.Font = new System.Drawing.Font("Century Gothic", 19F);
            this.bun_mat_textbox_search.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.bun_mat_textbox_search.HintForeColor = System.Drawing.SystemColors.ControlDarkDark;
            this.bun_mat_textbox_search.HintText = "Search";
            this.bun_mat_textbox_search.isPassword = false;
            this.bun_mat_textbox_search.LineFocusedColor = System.Drawing.Color.FromArgb(((int)(((byte)(36)))), ((int)(((byte)(129)))), ((int)(((byte)(77)))));
            this.bun_mat_textbox_search.LineIdleColor = System.Drawing.Color.Gray;
            this.bun_mat_textbox_search.LineMouseHoverColor = System.Drawing.Color.SeaGreen;
            this.bun_mat_textbox_search.LineThickness = 6;
            this.bun_mat_textbox_search.Location = new System.Drawing.Point(0, 40);
            this.bun_mat_textbox_search.Margin = new System.Windows.Forms.Padding(8);
            this.bun_mat_textbox_search.Name = "bun_mat_textbox_search";
            this.bun_mat_textbox_search.Size = new System.Drawing.Size(1000, 45);
            this.bun_mat_textbox_search.TabIndex = 17;
            this.bun_mat_textbox_search.TextAlign = System.Windows.Forms.HorizontalAlignment.Left;
            this.bun_mat_textbox_search.KeyDown += new System.Windows.Forms.KeyEventHandler(this.Bun_mat_textbox_search_KeyDown);
            // 
            // rich_textbox_status
            // 
            this.rich_textbox_status.BackColor = System.Drawing.SystemColors.Control;
            this.rich_textbox_status.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.rich_textbox_status.Cursor = System.Windows.Forms.Cursors.Arrow;
            this.rich_textbox_status.Font = new System.Drawing.Font("Gulim", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
            this.rich_textbox_status.Location = new System.Drawing.Point(245, 95);
            this.rich_textbox_status.Name = "rich_textbox_status";
            this.rich_textbox_status.ReadOnly = true;
            this.rich_textbox_status.ScrollBars = System.Windows.Forms.RichTextBoxScrollBars.None;
            this.rich_textbox_status.ShortcutsEnabled = false;
            this.rich_textbox_status.Size = new System.Drawing.Size(805, 30);
            this.rich_textbox_status.TabIndex = 20;
            this.rich_textbox_status.Text = "";
            // 
            // bun_flat_btn_search
            // 
            this.bun_flat_btn_search.Activecolor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_flat_btn_search.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_flat_btn_search.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("bun_flat_btn_search.BackgroundImage")));
            this.bun_flat_btn_search.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.bun_flat_btn_search.BorderRadius = 0;
            this.bun_flat_btn_search.ButtonText = "";
            this.bun_flat_btn_search.Cursor = System.Windows.Forms.Cursors.Hand;
            this.bun_flat_btn_search.DisabledColor = System.Drawing.Color.Gray;
            this.bun_flat_btn_search.Iconcolor = System.Drawing.Color.Transparent;
            this.bun_flat_btn_search.Iconimage = null;
            this.bun_flat_btn_search.Iconimage_right = null;
            this.bun_flat_btn_search.Iconimage_right_Selected = null;
            this.bun_flat_btn_search.Iconimage_Selected = null;
            this.bun_flat_btn_search.IconMarginLeft = 0;
            this.bun_flat_btn_search.IconMarginRight = 0;
            this.bun_flat_btn_search.IconRightVisible = true;
            this.bun_flat_btn_search.IconRightZoom = 0D;
            this.bun_flat_btn_search.IconVisible = true;
            this.bun_flat_btn_search.IconZoom = 90D;
            this.bun_flat_btn_search.IsTab = false;
            this.bun_flat_btn_search.Location = new System.Drawing.Point(1000, 40);
            this.bun_flat_btn_search.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.bun_flat_btn_search.Name = "bun_flat_btn_search";
            this.bun_flat_btn_search.Normalcolor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_flat_btn_search.OnHovercolor = System.Drawing.Color.FromArgb(((int)(((byte)(36)))), ((int)(((byte)(129)))), ((int)(((byte)(77)))));
            this.bun_flat_btn_search.OnHoverTextColor = System.Drawing.Color.White;
            this.bun_flat_btn_search.selected = false;
            this.bun_flat_btn_search.Size = new System.Drawing.Size(51, 46);
            this.bun_flat_btn_search.TabIndex = 19;
            this.bun_flat_btn_search.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.bun_flat_btn_search.Textcolor = System.Drawing.Color.White;
            this.bun_flat_btn_search.TextFont = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bun_flat_btn_search.Click += new System.EventHandler(this.Bun_flat_btn_search_Click);
            // 
            // flow_layout_panel_main
            // 
            this.flow_layout_panel_main.AutoScroll = true;
            this.flow_layout_panel_main.Location = new System.Drawing.Point(0, 125);
            this.flow_layout_panel_main.Name = "flow_layout_panel_main";
            this.flow_layout_panel_main.Size = new System.Drawing.Size(1050, 633);
            this.flow_layout_panel_main.TabIndex = 18;
            // 
            // bun_drag_control_sub
            // 
            this.bun_drag_control_sub.Fixed = true;
            this.bun_drag_control_sub.Horizontal = true;
            this.bun_drag_control_sub.TargetControl = this.lab_main;
            this.bun_drag_control_sub.Vertical = true;
            // 
            // form_main
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(120F, 120F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Dpi;
            this.ClientSize = new System.Drawing.Size(1050, 760);
            this.Controls.Add(this.flow_layout_panel_main);
            this.Controls.Add(this.bun_dropdown_source);
            this.Controls.Add(this.bun_mat_textbox_search);
            this.Controls.Add(this.rich_textbox_status);
            this.Controls.Add(this.bun_flat_btn_search);
            this.Controls.Add(this.pan_drag);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "form_main";
            this.Load += new System.EventHandler(this.Form_main_Load);
            this.pan_drag.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion
        private Bunifu.Framework.UI.BunifuFlatButton bun_flat_btn_show_error;
        public Bunifu.Framework.UI.BunifuElipse bun_elipse;
        private System.Windows.Forms.Panel pan_drag;
        private Bunifu.Framework.UI.BunifuFlatButton bun_fat_btn_close;
        public Bunifu.Framework.UI.BunifuDragControl bun_drag_control_main;
        private Bunifu.Framework.UI.BunifuFlatButton bun_flat_btn_view;
        private System.Windows.Forms.OpenFileDialog open_file_dialog;
        private Bunifu.Framework.UI.BunifuDropdown bun_dropdown_source;
        public Bunifu.Framework.UI.BunifuMaterialTextbox bun_mat_textbox_search;
        public System.Windows.Forms.RichTextBox rich_textbox_status;
        private Bunifu.Framework.UI.BunifuFlatButton bun_flat_btn_search;
        public System.Windows.Forms.FlowLayoutPanel flow_layout_panel_main;
        private Bunifu.Framework.UI.BunifuFlatButton bun_flat_btn_minimize;
        private System.Windows.Forms.Label lab_main;
        public Bunifu.Framework.UI.BunifuDragControl bun_drag_control_sub;
    }
}

