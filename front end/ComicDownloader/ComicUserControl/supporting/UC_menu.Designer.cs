namespace ComicDownloader.ComicUserControl.supporting
{
    partial class UC_menu
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
            this.lab_main = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // lab_main
            // 
            this.lab_main.AutoSize = true;
            this.lab_main.Font = new System.Drawing.Font("Source Code Pro Black", 25.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lab_main.Location = new System.Drawing.Point(0, 0);
            this.lab_main.Name = "lab_main";
            this.lab_main.Size = new System.Drawing.Size(127, 54);
            this.lab_main.TabIndex = 5;
            this.lab_main.Text = "menu";
            // 
            // UC_menu
            // 
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Inherit;
            this.Controls.Add(this.lab_main);
            this.Name = "UC_menu";
            this.Size = new System.Drawing.Size(1050, 715);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        public System.Windows.Forms.Label lab_main;
    }
}
