using System;
using System.IO;
using System.Data;
using System.Linq;
using System.Text;
using System.Regex;
using System.Drawing;
using System.Diagnostics;
using System.Windows.Forms;
using System.ComponentModel;
using System.Threading.Tasks;
using System.Collections.Generic;

namespace ComicDownloader.ComicUserControl.supporting
{
    public partial class UC_search_result : UserControl
    {
        public string ComicURL = "";
        Regex CMDRegex = new Regex(@"\w:\\.*>.*");

        public UC_search_result()
        {
            InitializeComponent();
        }

        public void Download()
        {
            #region Run search command
            ProcessStartInfo episodeSearchProcessStartInfo = new ProcessStartInfo();
            episodeSearchProcessStartInfo.CreateNoWindow = true;
            episodeSearchProcessStartInfo.UseShellExecute = false;
            episodeSearchProcessStartInfo.RedirectStandardInput = true;
            episodeSearchProcessStartInfo.RedirectStandardOutput = true;
            episodeSearchProcessStartInfo.FileName = Environment.ExpandEnvironmentVariables("%SystemRoot%") + @"\System32\cmd.exe";

            Process episodeSearchProcess = new Process();
            episodeSearchProcess.StartInfo = episodeSearchProcessStartInfo;

            episodeSearchProcess.Start();
            StreamReader episodeSearchProcessStreamReader = episodeSearchProcess.StandardOutput;
            StreamWriter episodeSearchProcessStreamWriter = episodeSearchProcess.StandardInput;

            episodeSearchProcessStreamWriter.WriteLine(@"support_files\get_eps.exe -u ""{0}"" -s 3", ComicURL);
            episodeSearchProcessStreamWriter.WriteLine(@"exit");
            #endregion

            #region Prepare parsing search output
            string episodeSearchProcessOutputLine = "";
            string episodeSearchProcessOutputFinal = "";
            StringReader episodeSearchStringReader = new StringReader(episodeSearchProcessStreamReader.ReadToEnd());
            byte episodeSearchLineIndex = 0;

            episodeSearchProcessStreamReader.Close();
            episodeSearchProcessStreamWriter.Close();
            episodeSearchProcess.Close();

            #endregion

            #region parse each line in search Process output
            while (true)
            {
                episodeSearchProcessOutputLine = episodeSearchStringReader.ReadLine();

                if (episodeSearchProcessOutputLine != null)
                {
                    if (episodeSearchLineIndex > 2)
                    {
                        if (!CMDRegex.IsMatch(episodeSearchProcessOutputLine))
                        {
                            episodeSearchProcessOutputFinal = episodeSearchProcessOutputFinal + episodeSearchProcessOutputLine + "\n";
                        }
                    }
                }
                else
                {
                    break;
                }
                episodeSearchLineIndex++;
            }
            episodeSearchProcessOutputFinal = episodeSearchProcessOutputFinal.Trim();

            List<string> URLList = episodeSearchProcessOutputFinal.Split('\n').ToList();
            #endregion

            #region Check for errors
            if (URLList.Count < 1)
            {
                MessageBox.Show("The comic has no episodes");
                return;
            }
            #endregion

            form_comic_range_input inputForm = new form_comic_range_input(ComicURL, URLList);
            
            for (int i = 0; i < URLList.Count; i++)
            {
                Invoke(new Action(() =>
                {
                    inputForm.rich_textbox_url_list.Text += "\n" + (i + 1).ToString() + ": " + URLList[i];
                    inputForm.lab_num_results.Text = URLList.Count.ToString() + " Results";
                }));
            }

            inputForm.ShowDialog();
        }

        private void Bun_falt_btn_download_Click(object sender, EventArgs e)
        {
            Task.Factory.StartNew(() => Download());
        }
    }
}
