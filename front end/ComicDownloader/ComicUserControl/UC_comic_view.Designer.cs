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
            this.open_file_dialog = new System.Windows.Forms.OpenFileDialog();
            this.SuspendLayout();
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
            this.Name = "UC_comic_view";
            this.Size = new System.Drawing.Size(1050, 715);
            this.Load += new System.EventHandler(this.UC_comic_view_Load);
            this.ResumeLayout(false);

        }

        #endregion
        public System.Windows.Forms.OpenFileDialog open_file_dialog;
    }
}
