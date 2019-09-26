using System;
using System.Diagnostics;
using System.Windows.Forms;
using System.Threading.Tasks;
using System.Collections.Generic;

namespace ComicDownloader.supporting
{
    public partial class form_comic_range_input : Form
    {
        string ComicURL;
        List<string> URLList;
        form_main main_form;

        public int from = -1;
        public int to = -1;

        public bool aAllowed = false;
        public bool bAllowed = false;

        public form_comic_range_input(string ParentComicURL, List<string> ParentURLList, form_main Parentmain_form)
        {
            InitializeComponent();
            ComicURL = ParentComicURL;
            URLList = ParentURLList;
            main_form = Parentmain_form;
            RangeUpdate(this, new EventArgs());
        }

        private void RangeUpdate(object sender, EventArgs e)
        {
            if (textbox_from.Text == "START" || textbox_from.Text == "END")
            {
                if (textbox_from.Text == "START")
                {
                    from = 1;
                    aAllowed = true;
                }
                else
                {
                    from = URLList.Count;
                    aAllowed = true;
                }
            }
            else
            {
                if (int.TryParse(textbox_from.Text, out from)) aAllowed = true;
                else aAllowed = false;
            }

            if (textbox_to.Text == "START" || textbox_to.Text == "END")
            {
                if (textbox_to.Text == "START")
                {
                    to = 1;
                    bAllowed = true;
                    
                }
                else
                {
                    to = URLList.Count;
                    bAllowed = true;
                }
            }
            else
            {
                if (int.TryParse(textbox_to.Text, out to)) bAllowed = true;
                else bAllowed = false;
            }

            if (aAllowed && bAllowed)
            {
                if ((to >= from) && (to <= URLList.Count) && (from > 0))
                {
                    aAllowed = true;
                    bAllowed = true;
                }
                else
                {
                    aAllowed = false;
                    bAllowed = false;
                }
            }
            
            if (aAllowed)
            {
                lab_init_range.Text = "";
            }
            else
            {
                lab_init_range.Text = "!";
                from = -1;
            }

            if (bAllowed)
            {
                lab_end_range.Text = "";
            }
            else
            {
                lab_end_range.Text = "!";
                to = -1;
            }

            lab_range.Text = "[" + from + " ~ " + to + "]";
        }

        public void Download()
        {
            if (main_form.folder_browser_dialog.SelectedPath.EndsWith(@"\"))
            {
                main_form.folder_browser_dialog.SelectedPath = main_form.folder_browser_dialog.SelectedPath.Remove(main_form.folder_browser_dialog.SelectedPath.Length - 1);
            }

            #region Run search command
            ProcessStartInfo episodeDownloadProcessStartInfo = new ProcessStartInfo();
            episodeDownloadProcessStartInfo.WorkingDirectory = @"support_files\";
            episodeDownloadProcessStartInfo.Arguments = string.Format(@"-u {0} -s {1} -l ""{2}""", ComicURL, main_form.source, main_form.folder_browser_dialog.SelectedPath);
            episodeDownloadProcessStartInfo.CreateNoWindow = false;
            episodeDownloadProcessStartInfo.UseShellExecute = false;
            episodeDownloadProcessStartInfo.FileName = @"support_files\download.exe";

            Process episodeDownloadProcess = new Process();
            episodeDownloadProcess.StartInfo = episodeDownloadProcessStartInfo;

            episodeDownloadProcess.Start();
            episodeDownloadProcess.WaitForExit();
            int DownloadExitCode = episodeDownloadProcess.ExitCode;
            #endregion

            #region Check for errors
            //error handling
            #endregion

            this.Close();
        }

        private void Rich_textbox_url_list_LinkClicked(object sender, LinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start(e.LinkText);
        }

        private void Bun_flat_btn_go_Click(object sender, EventArgs e)
        {
            if (aAllowed && bAllowed)
            {
                Task.Factory.StartNew(() => Download());
                this.Close();
            }
            else
            {
                MessageBox.Show("Invalid range");
            }
        }
    }
}
