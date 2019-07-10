namespace ComicDownloader.ComicUserControl
{
    partial class UC_comic_search
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(UC_comic_search));
            this.bun_dropdown_source = new Bunifu.Framework.UI.BunifuDropdown();
            this.bun_mat_textbox_search = new Bunifu.Framework.UI.BunifuMaterialTextbox();
            this.rich_textbox_status = new System.Windows.Forms.RichTextBox();
            this.bun_flat_btn_search = new Bunifu.Framework.UI.BunifuFlatButton();
            this.flow_layout_panel_main = new System.Windows.Forms.FlowLayoutPanel();
            this.SuspendLayout();
            // 
            // bun_dropdown_source
            // 
            this.bun_dropdown_source.BackColor = System.Drawing.Color.Transparent;
            this.bun_dropdown_source.BorderRadius = 3;
            this.bun_dropdown_source.Font = new System.Drawing.Font("Source Code Pro", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bun_dropdown_source.ForeColor = System.Drawing.Color.White;
            this.bun_dropdown_source.Items = new string[0];
            this.bun_dropdown_source.Location = new System.Drawing.Point(-1, 44);
            this.bun_dropdown_source.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.bun_dropdown_source.Name = "bun_dropdown_source";
            this.bun_dropdown_source.NomalColor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_dropdown_source.onHoverColor = System.Drawing.Color.FromArgb(((int)(((byte)(36)))), ((int)(((byte)(129)))), ((int)(((byte)(77)))));
            this.bun_dropdown_source.selectedIndex = -1;
            this.bun_dropdown_source.Size = new System.Drawing.Size(245, 40);
            this.bun_dropdown_source.TabIndex = 10;
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
            this.bun_mat_textbox_search.Location = new System.Drawing.Point(0, 0);
            this.bun_mat_textbox_search.Margin = new System.Windows.Forms.Padding(8);
            this.bun_mat_textbox_search.Name = "bun_mat_textbox_search";
            this.bun_mat_textbox_search.Size = new System.Drawing.Size(1000, 45);
            this.bun_mat_textbox_search.TabIndex = 11;
            this.bun_mat_textbox_search.TextAlign = System.Windows.Forms.HorizontalAlignment.Left;
            this.bun_mat_textbox_search.KeyDown += new System.Windows.Forms.KeyEventHandler(this.Bun_mat_textbox_search_KeyDown);
            // 
            // rich_textbox_status
            // 
            this.rich_textbox_status.BackColor = System.Drawing.SystemColors.Control;
            this.rich_textbox_status.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.rich_textbox_status.Cursor = System.Windows.Forms.Cursors.Arrow;
            this.rich_textbox_status.Font = new System.Drawing.Font("Gulim", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
            this.rich_textbox_status.Location = new System.Drawing.Point(245, 55);
            this.rich_textbox_status.Name = "rich_textbox_status";
            this.rich_textbox_status.ReadOnly = true;
            this.rich_textbox_status.ScrollBars = System.Windows.Forms.RichTextBoxScrollBars.None;
            this.rich_textbox_status.ShortcutsEnabled = false;
            this.rich_textbox_status.Size = new System.Drawing.Size(805, 30);
            this.rich_textbox_status.TabIndex = 14;
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
            this.bun_flat_btn_search.Location = new System.Drawing.Point(1000, 0);
            this.bun_flat_btn_search.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.bun_flat_btn_search.Name = "bun_flat_btn_search";
            this.bun_flat_btn_search.Normalcolor = System.Drawing.Color.FromArgb(((int)(((byte)(46)))), ((int)(((byte)(139)))), ((int)(((byte)(87)))));
            this.bun_flat_btn_search.OnHovercolor = System.Drawing.Color.FromArgb(((int)(((byte)(36)))), ((int)(((byte)(129)))), ((int)(((byte)(77)))));
            this.bun_flat_btn_search.OnHoverTextColor = System.Drawing.Color.White;
            this.bun_flat_btn_search.selected = false;
            this.bun_flat_btn_search.Size = new System.Drawing.Size(51, 46);
            this.bun_flat_btn_search.TabIndex = 13;
            this.bun_flat_btn_search.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.bun_flat_btn_search.Textcolor = System.Drawing.Color.White;
            this.bun_flat_btn_search.TextFont = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bun_flat_btn_search.Click += new System.EventHandler(this.Bun_flat_btn_search_Click);
            // 
            // flow_layout_panel_main
            // 
            this.flow_layout_panel_main.AutoScroll = true;
            this.flow_layout_panel_main.Location = new System.Drawing.Point(0, 82);
            this.flow_layout_panel_main.Name = "flow_layout_panel_main";
            this.flow_layout_panel_main.Size = new System.Drawing.Size(1050, 633);
            this.flow_layout_panel_main.TabIndex = 12;
            // 
            // UC_comic_search
            // 
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Inherit;
            this.Controls.Add(this.bun_dropdown_source);
            this.Controls.Add(this.bun_mat_textbox_search);
            this.Controls.Add(this.rich_textbox_status);
            this.Controls.Add(this.bun_flat_btn_search);
            this.Controls.Add(this.flow_layout_panel_main);
            this.Name = "UC_comic_search";
            this.Size = new System.Drawing.Size(1050, 715);
            this.ResumeLayout(false);

        }

        #endregion

        private Bunifu.Framework.UI.BunifuDropdown bun_dropdown_source;
        public System.Windows.Forms.RichTextBox rich_textbox_status;
        private Bunifu.Framework.UI.BunifuFlatButton bun_flat_btn_search;
        public System.Windows.Forms.FlowLayoutPanel flow_layout_panel_main;
        public Bunifu.Framework.UI.BunifuMaterialTextbox bun_mat_textbox_search;
    }
}
