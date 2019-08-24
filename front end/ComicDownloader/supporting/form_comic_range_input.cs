using System;
using System.IO;
using System.Data;
using System.Linq;
using System.Text;
using System.Regex;
using System.Threading;
using System.Drawing;
using System.Diagnostics;
using System.Windows.Forms;
using System.ComponentModel;
using System.Threading.Tasks;
using System.Collections.Generic;

namespace ComicDownloader.supporting
{
    public partial class form_comic_range_input : Form
    {
        string ComicURL;
        List<string> URLList;

        public int from = -1;
        public int to = -1;

        public bool aAllowed = false;
        public bool bAllowed = false;

        int exitCode;

        public form_comic_range_input(string ParentComicURL, List<string> ParentURLList)
        {
            InitializeComponent();
            ComicURL = ParentComicURL;
            URLList = ParentURLList;
            RangeUpdate(this, new EventArgs());
            folder_browser_dialog.SelectedPath = System.Environment.CurrentDirectory;
            textbox_where.Text = System.Environment.CurrentDirectory;
        }

        private void RangeUpdate(object sender, EventArgs e)
        {
            if (textbox_from.Text == "START")
            {
                from = 1;
                aAllowed = true;
            }
            else
            {
                if (int.TryParse(textbox_from.Text, out from)) aAllowed = true;
                else aAllowed = false;
            }

            if (textbox_to.Text == "END")
            {
                to = URLList.Count;
                bAllowed = true;
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

        public void DownloadLoop()
        {
            #region Run search command
            ProcessStartInfo episodeDownloadProcessStartInfo = new ProcessStartInfo();
            episodeDownloadProcessStartInfo.WorkingDirectory = @".\support_files\";
            episodeDownloadProcessStartInfo.Arguments = "-u " + ComicURL + " -e " + (from-1).ToString() + "-" + (to-1).ToString() + @" -l ..\ -s 3";
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
            //error
            #endregion

            this.Close();
        }

        private void Rich_textbox_url_list_LinkClicked(object sender, LinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start(e.LinkText);
        }

        private void Bun_flat_btn_go_Click(object sender, EventArgs e)
        {
            Task.Factory.StartNew(() => DownloadLoop());
            MessageBox.Show("Start downloading...\nYou may close the GUI");
            this.Visible = false;
        }

        private void Bun_flat_btn_choose_Click(object sender, EventArgs e)
        {
            Thread threadGetFile = new Thread(new ThreadStart(() =>
            {
                if (folder_browser_dialog.ShowDialog() == DialogResult.Cancel)
                {
                    return;
                }

                Invoke((Action)(() => { textbox_where.Text = folder_browser_dialog.SelectedPath; }));
            }));

            threadGetFile.SetApartmentState(ApartmentState.STA);
            threadGetFile.Start();
        }
    }
}
