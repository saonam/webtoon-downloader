using System;
using System.IO;
using System.Text;
using System.Windows.Forms;
using System.Diagnostics;
using System.Threading.Tasks;
using System.Drawing;
using System.Net;
using System.Collections.Generic;
using System.Linq;

namespace ComicDownloader
{
    public partial class form_main : Form
    {
        public static form_main form_instance;
        public string errorString { get; set; } = "There are  no error so far";

        public supporting.UC_search_result[] elements = new supporting.UC_search_result[5];

        public form_main()
        {
            InitializeComponent();
            form_instance = this;
            open_file_dialog.Filter = "Image files (*.jpg, *.jpeg, *.jpe, *.jfif, *.png, *.bmp) | *.jpg; *.jpeg; *.jpe; *.jfif; *.png; *.bmp";

            bun_dropdown_source.AddItem("funbe");
            //bun_dropdown_source.AddItem("Naver Webtoon");
            //bun_dropdown_source.AddItem("Naver Best Challenge");
            //bun_dropdown_source.AddItem("Daum webtoon");
            //bun_dropdown_source.AddItem("Kakao webtoon");
            bun_dropdown_source.selectedIndex = 0;
        }

        private void Bun_fat_btn_close_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void Bun_flat_btn_show_error_Click(object sender, EventArgs e)
        {
            MessageBox.Show(errorString);
        }

        private void Bun_flat_btn_view_Click(object sender, EventArgs e)
        {
            open_file_dialog.ShowDialog();

            string tmpHTMLPath = Path.GetTempPath() + "toon_view_" + Guid.NewGuid() + "_.html";
            string ImagePath = open_file_dialog.FileName;

            using (FileStream fs = new FileStream(tmpHTMLPath, FileMode.Append))
            {
                using (StreamWriter w = new StreamWriter(fs, Encoding.UTF8))
                {
                    w.WriteLine(@"<!DOCTYPE html>");
                    w.WriteLine(@"<html>");
                    w.WriteLine(@"<head> <title> Comic View </title> </head>");
                    w.WriteLine(@"<body>");
                    w.WriteLine(@"<body style=""background-color:#000000;"">");
                    w.WriteLine(@"<div align=""center"">");
                    w.WriteLine(@"<img src=""{0}"" style='height: auto; width: 45%; margin: auto'/>", ImagePath);
                    w.WriteLine(@"</div>");
                    w.WriteLine(@"</body>");
                    w.WriteLine(@"</html>");
                }
            }

            Process.Start(tmpHTMLPath);
        }

        private void Form_main_Load(object sender, EventArgs e)
        {
            //get a list of path of all the files in the comic directory
            //display a list of them in a flow layout panel
        }

        public void Search()//A function that search and display comic series
        {
            Invoke((Action)(() => { rich_textbox_status.Text = "Searching..."; }));

            #region clear list
            foreach (supporting.UC_search_result element in elements)
            {
                Invoke((Action)(() => { flow_layout_panel_main.Controls.Remove(element); }));
            }

            Array.Clear(elements, 0, elements.Length); //clear array elements
            #endregion

            try
            {
                #region Run search command
                ProcessStartInfo searchProcessStartInfo = new ProcessStartInfo();
                searchProcessStartInfo.Arguments = "-q \"" + bun_mat_textbox_search.Text + "\" -s 3";
                searchProcessStartInfo.CreateNoWindow = true;
                searchProcessStartInfo.UseShellExecute = false;
                searchProcessStartInfo.RedirectStandardOutput = true;
                searchProcessStartInfo.FileName = @"support_files\search.exe";

                Process SearchProcess = new Process();
                SearchProcess.StartInfo = searchProcessStartInfo;
                SearchProcess.Start();

                StreamReader searchProcessStreamReader = SearchProcess.StandardOutput;
                #endregion

                #region parsing search output
                List<string> URLList = searchProcessStreamReader.ReadToEnd().Trim().Split('\n').ToList();

                int SearchExitCode = SearchProcess.ExitCode;

                searchProcessStreamReader.Close();
                SearchProcess.Close();
                #endregion

                #region Check for errors
                if (URLList.Count < 1)  // if the result is empty
                {
                    Invoke((Action)(() => { rich_textbox_status.Text = "No search results"; }));
                    return;
                }
                #endregion

                #region fill elements loop (parse episode)
                elements = new supporting.UC_search_result[URLList.Count];
                Parallel.For(0, URLList.Count, new ParallelOptions { MaxDegreeOfParallelism = 3 }, i =>
                {
                    #region parse episode
                    ProcessStartInfo episodeStartInfo = new ProcessStartInfo();
                    episodeStartInfo.Arguments = "-u " + URLList[i] + " -s 3";
                    episodeStartInfo.CreateNoWindow = true;
                    episodeStartInfo.UseShellExecute = false;
                    episodeStartInfo.RedirectStandardOutput = true;
                    episodeStartInfo.FileName = @"support_files\parse_comic.exe";

                    Process episodeProcess = new Process();
                    episodeProcess.StartInfo = episodeStartInfo;
                    episodeProcess.Start();

                    StreamReader episodeProcessStreamReader = episodeProcess.StandardOutput;

                    #endregion

                    #region parsing episode output
                    List<string> episodeParsedData = episodeProcessStreamReader.ReadToEnd().Trim().Split('\n').ToList();

                    int ParseExitCode = episodeProcess.ExitCode;

                    episodeProcessStreamReader.Close();
                    episodeProcess.Close();
                    #endregion

                    #region Check for errors
                    if (episodeParsedData.Count < 1)
                    {
                        Invoke((Action)(() => { rich_textbox_status.Text = "No search results"; }));
                        return;
                    }
                    #endregion

                    #region Actual filling
                    try
                    {
                        elements[i] = new supporting.UC_search_result();
                        elements[i].ComicURL = URLList[i];
                        elements[i].lab_day.Text = "day of update: No information";
                        elements[i].lab_main.Text = episodeParsedData[0];
                        elements[i].rich_textbox_description.Text = episodeParsedData[1];
                        elements[i].lab_author.Text = "Author: " + episodeParsedData[2];
                        elements[i].lab_last_update.Text = "Last update: " + episodeParsedData[3];
                        if (int.TryParse(episodeParsedData[4], out int totalEpisode))
                        {
                            elements[i].lab_total_eps.Text = "Total episodes: " + totalEpisode.ToString();
                        }
                        else
                        {
                            elements[i].lab_total_eps.Text = "Total episodes: No information";
                        }

                        Stream ThumbnailImageStream = WebRequest.Create(episodeParsedData[5]).GetResponse().GetResponseStream();

                        elements[i].pict_box_main.Image = Bitmap.FromStream(ThumbnailImageStream);

                        Invoke((Action)(() => { flow_layout_panel_main.Controls.Add(elements[i]); }));
                    }
                    catch (System.ArgumentOutOfRangeException err)
                    {
                        Invoke((Action)(() => { rich_textbox_status.Text = "No search results"; }));
                        return;
                    }
                    #endregion

                    Invoke((Action)(() => { rich_textbox_status.Text = ""; }));
                });
                #endregion
            }
            catch (Exception err)
            {
                Invoke((Action)(() => { rich_textbox_status.Text = "An Error has occurred"; }));

                foreach (supporting.UC_search_result element in elements)
                {
                    Invoke((Action)(() => { flow_layout_panel_main.Controls.Remove(element); }));
                }
                Array.Clear(elements, 0, elements.Length);

                errorString = err.ToString();
            }
        }

        private void Bun_flat_btn_search_Click(object sender, EventArgs e)
        {
            Task.Factory.StartNew(() => Search());
        }

        private void Bun_mat_textbox_search_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                Bun_flat_btn_search_Click(this, new EventArgs());

                //This is required to not play the 'Ding!' sound when Enter key is pressed
                e.Handled = true;
                e.SuppressKeyPress = true;
            }
        }

        private void Bun_flat_btn_minimize_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;
        }
    }
}
