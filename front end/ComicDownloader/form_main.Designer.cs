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
            this.bun_elipse = new Bunifu.Framework.UI.BunifuElipse(this.components);
            this.pan_drag = new System.Windows.Forms.Panel();
            this.btn_minimize = new System.Windows.Forms.Button();
            this.btn_close = new System.Windows.Forms.Button();
            this.btn_show_err = new System.Windows.Forms.Button();
            this.btn_save_location = new System.Windows.Forms.Button();
            this.btn_view = new System.Windows.Forms.Button();
            this.bun_checkbox = new Bunifu.Framework.UI.BunifuCheckbox();
            this.lab_main = new System.Windows.Forms.Label();
            this.bun_drag_control_main = new Bunifu.Framework.UI.BunifuDragControl(this.components);
            this.open_file_dialog_open = new System.Windows.Forms.OpenFileDialog();
            this.bun_dropdown_source = new Bunifu.Framework.UI.BunifuDropdown();
            this.bun_mat_textbox_search = new Bunifu.Framework.UI.BunifuMaterialTextbox();
            this.rich_textbox_status = new System.Windows.Forms.RichTextBox();
            this.bun_flat_btn_search = new Bunifu.Framework.UI.BunifuFlatButton();
            this.flow_layout_panel_main = new System.Windows.Forms.FlowLayoutPanel();
            this.bun_drag_control_sub = new Bunifu.Framework.UI.BunifuDragControl(this.components);
            this.folder_browser_dialog = new System.Windows.Forms.FolderBrowserDialog();
            this.tool_tip = new System.Windows.Forms.ToolTip(this.components);
            this.pan_drag.SuspendLayout();
            this.SuspendLayout();
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
            this.pan_drag.Controls.Add(this.btn_minimize);
            this.pan_drag.Controls.Add(this.btn_close);
            this.pan_drag.Controls.Add(this.btn_show_err);
            this.pan_drag.Controls.Add(this.btn_save_location);
            this.pan_drag.Controls.Add(this.btn_view);
            this.pan_drag.Controls.Add(this.bun_checkbox);
            this.pan_drag.Controls.Add(this.lab_main);
            this.pan_drag.ForeColor = System.Drawing.SystemColors.Control;
            this.pan_drag.Location = new System.Drawing.Point(0, 0);
            this.pan_drag.Name = "pan_drag";
            this.pan_drag.Size = new System.Drawing.Size(1050, 40);
            this.pan_drag.TabIndex = 15;
            // 
            // btn_minimize
            // 
            this.btn_minimize.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("btn_minimize.BackgroundImage")));
            this.btn_minimize.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.btn_minimize.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btn_minimize.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(35)))), ((int)(((byte)(35)))), ((int)(((byte)(35)))));
            this.btn_minimize.Location = new System.Drawing.Point(970, 0);
            this.btn_minimize.Name = "btn_minimize";
            this.btn_minimize.Size = new System.Drawing.Size(40, 41);
            this.btn_minimize.TabIndex = 19;
            this.tool_tip.SetToolTip(this.btn_minimize, "minimize window");
            this.btn_minimize.UseVisualStyleBackColor = true;
            this.btn_minimize.Click += new System.EventHandler(this.Btn_minimize_Click);
            this.btn_minimize.MouseEnter += new System.EventHandler(this.Btn_minimize_MouseEnter);
            this.btn_minimize.MouseLeave += new System.EventHandler(this.Btn_revert_color);
            // 
            // btn_close
            // 
            this.btn_close.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("btn_close.BackgroundImage")));
            this.btn_close.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.btn_close.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btn_close.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(35)))), ((int)(((byte)(35)))), ((int)(((byte)(35)))));
            this.btn_close.Location = new System.Drawing.Point(1010, 0);
            this.btn_close.Name = "btn_close";
            this.btn_close.Size = new System.Drawing.Size(40, 41);
            this.btn_close.TabIndex = 18;
            this.tool_tip.SetToolTip(this.btn_close, "Close program");
            this.btn_close.UseVisualStyleBackColor = true;
            this.btn_close.Click += new System.EventHandler(this.Btn_close_Click);
            this.btn_close.MouseEnter += new System.EventHandler(this.Btn_close_MouseEnter);
            this.btn_close.MouseLeave += new System.EventHandler(this.Btn_revert_color);
            // 
            // btn_show_err
            // 
            this.btn_show_err.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("btn_show_err.BackgroundImage")));
            this.btn_show_err.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.btn_show_err.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btn_show_err.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(35)))), ((int)(((byte)(35)))), ((int)(((byte)(35)))));
            this.btn_show_err.Location = new System.Drawing.Point(931, 0);
            this.btn_show_err.Name = "btn_show_err";
            this.btn_show_err.Size = new System.Drawing.Size(40, 41);
            this.btn_show_err.TabIndex = 17;
            this.tool_tip.SetToolTip(this.btn_show_err, "See error");
            this.btn_show_err.UseVisualStyleBackColor = true;
            this.btn_show_err.Click += new System.EventHandler(this.Btn_show_err_Click);
            this.btn_show_err.MouseEnter += new System.EventHandler(this.Btn_show_err_MouseEnter);
            this.btn_show_err.MouseLeave += new System.EventHandler(this.Btn_revert_color);
            // 
            // btn_save_location
            // 
            this.btn_save_location.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("btn_save_location.BackgroundImage")));
            this.btn_save_location.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.btn_save_location.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btn_save_location.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(35)))), ((int)(((byte)(35)))), ((int)(((byte)(35)))));
            this.btn_save_location.Location = new System.Drawing.Point(363, 0);
            this.btn_save_location.Name = "btn_save_location";
            this.btn_save_location.Size = new System.Drawing.Size(40, 41);
            this.btn_save_location.TabIndex = 16;
            this.tool_tip.SetToolTip(this.btn_save_location, "Set custom save ocation");
            this.btn_save_location.UseVisualStyleBackColor = true;
            this.btn_save_location.Click += new System.EventHandler(this.Btn_save_location_Click);
            this.btn_save_location.MouseEnter += new System.EventHandler(this.Btn_save_location_MouseEnter);
            this.btn_save_location.MouseLeave += new System.EventHandler(this.Btn_revert_color);
            // 
            // btn_view
            // 
            this.btn_view.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("btn_view.BackgroundImage")));
            this.btn_view.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.btn_view.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btn_view.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(35)))), ((int)(((byte)(35)))), ((int)(((byte)(35)))));
            this.btn_view.Location = new System.Drawing.Point(892, 0);
            this.btn_view.Name = "btn_view";
            this.btn_view.Size = new System.Drawing.Size(40, 41);
            this.btn_view.TabIndex = 15;
            this.tool_tip.SetToolTip(this.btn_view, "View comic on browser");
            this.btn_view.UseVisualStyleBackColor = true;
            this.btn_view.Click += new System.EventHandler(this.Btn_view_Click);
            this.btn_view.MouseEnter += new System.EventHandler(this.Btn_view_MouseEnter);
            this.btn_view.MouseLeave += new System.EventHandler(this.Btn_revert_color);
            // 
            // bun_checkbox
            // 
            this.bun_checkbox.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(51)))), ((int)(((byte)(205)))), ((int)(((byte)(117)))));
            this.bun_checkbox.ChechedOffColor = System.Drawing.Color.FromArgb(((int)(((byte)(132)))), ((int)(((byte)(135)))), ((int)(((byte)(140)))));
            this.bun_checkbox.Checked = true;
            this.bun_checkbox.CheckedOnColor = System.Drawing.Color.FromArgb(((int)(((byte)(51)))), ((int)(((byte)(205)))), ((int)(((byte)(117)))));
            this.bun_checkbox.ForeColor = System.Drawing.Color.White;
            this.bun_checkbox.Location = new System.Drawing.Point(412, 11);
            this.bun_checkbox.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.bun_checkbox.Name = "bun_checkbox";
            this.bun_checkbox.Size = new System.Drawing.Size(20, 20);
            this.bun_checkbox.TabIndex = 14;
            // 
            // lab_main
            // 
            this.lab_main.Font = new System.Drawing.Font("Lucida Sans", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lab_main.Location = new System.Drawing.Point(0, 0);
            this.lab_main.Name = "lab_main";
            this.lab_main.Size = new System.Drawing.Size(363, 40);
            this.lab_main.TabIndex = 12;
            this.lab_main.Text = "Comic Downloader v2.2";
            this.lab_main.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // bun_drag_control_main
            // 
            this.bun_drag_control_main.Fixed = true;
            this.bun_drag_control_main.Horizontal = true;
            this.bun_drag_control_main.TargetControl = this.pan_drag;
            this.bun_drag_control_main.Vertical = true;
            // 
            // open_file_dialog_open
            // 
            this.open_file_dialog_open.FileName = "openFileDialog1";
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
            this.bun_dropdown_source.onItemSelected += new System.EventHandler(this.Bun_dropdown_source_onItemSelected);
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
        public Bunifu.Framework.UI.BunifuElipse bun_elipse;
        private System.Windows.Forms.Panel pan_drag;
        public Bunifu.Framework.UI.BunifuDragControl bun_drag_control_main;
        private System.Windows.Forms.OpenFileDialog open_file_dialog_open;
        private Bunifu.Framework.UI.BunifuDropdown bun_dropdown_source;
        public Bunifu.Framework.UI.BunifuMaterialTextbox bun_mat_textbox_search;
        public System.Windows.Forms.RichTextBox rich_textbox_status;
        private Bunifu.Framework.UI.BunifuFlatButton bun_flat_btn_search;
        public System.Windows.Forms.FlowLayoutPanel flow_layout_panel_main;
        private System.Windows.Forms.Label lab_main;
        public Bunifu.Framework.UI.BunifuDragControl bun_drag_control_sub;
        public System.Windows.Forms.FolderBrowserDialog folder_browser_dialog;
        private Bunifu.Framework.UI.BunifuCheckbox bun_checkbox;
        private System.Windows.Forms.ToolTip tool_tip;
        private System.Windows.Forms.Button btn_view;
        private System.Windows.Forms.Button btn_save_location;
        private System.Windows.Forms.Button btn_show_err;
        private System.Windows.Forms.Button btn_close;
        private System.Windows.Forms.Button btn_minimize;
    }
}

