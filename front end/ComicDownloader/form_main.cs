using System;
using System.IO;
using System.Net;
using System.Text;
using System.Linq;
using System.Regex;
using System.Drawing;
using System.Net.Sockets;
using System.Diagnostics;
using System.Windows.Forms;
using System.Threading.Tasks;
using System.Collections.Generic;

namespace ComicDownloader
{
    public partial class form_main : Form
    {
        public string source = "-1";
        public bool searching = false;
        public string errorString { get; set; } = "There are no error so far";

        public supporting.UC_search_result[] elements = new supporting.UC_search_result[5];

        public form_main()
        {
            InitializeComponent();
            open_file_dialog_open.Filter = "Image files (*.jpg, *.jpeg, *.jpe, *.jfif, *.png, *.bmp) | *.jpg; *.jpeg; *.jpe; *.jfif; *.png; *.bmp";
            folder_browser_dialog.SelectedPath = Directory.GetCurrentDirectory();
            open_file_dialog_open.InitialDirectory = Directory.GetCurrentDirectory();

            bun_dropdown_source.AddItem("funbe");
            //bun_dropdown_source.AddItem("Naver Webtoon");
            //bun_dropdown_source.AddItem("Naver Best Challenge");
            //bun_dropdown_source.AddItem("Daum webtoon");
            //bun_dropdown_source.AddItem("Kakao webtoon");
            bun_dropdown_source.selectedIndex = 0;
        }

        private void Form_main_Load(object sender, EventArgs e)
        {
            
        }

        public void Search()
        {
            
            searching = true;
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
                searchProcessStartInfo.Arguments = "-q \"" + bun_mat_textbox_search.Text + "\" -s " + source;
                searchProcessStartInfo.CreateNoWindow = true;
                searchProcessStartInfo.UseShellExecute = false;
                searchProcessStartInfo.RedirectStandardOutput = true;
                searchProcessStartInfo.FileName = @"support_files\search.exe";
                
                Process SearchProcess = new Process();
                SearchProcess.StartInfo = searchProcessStartInfo;
                SearchProcess.Start();
                
                StreamReader searchProcessStreamReader = SearchProcess.StandardOutput;

                List<string> SearchResult = searchProcessStreamReader.ReadToEnd().Trim().Split('\n').ToList();

                int SearchExitCode = SearchProcess.ExitCode;

                searchProcessStreamReader.Close();
                SearchProcess.Close();
                #endregion

                #region Check for errors
                switch (SearchExitCode)
                {
                    case -1:
                        Invoke((Action)(() => { rich_textbox_status.Text = "No search results"; }));
                        return;
                    case -2:
                        Invoke((Action)(() => { rich_textbox_status.Text = "ERR_SOURCE_NOT_RECOGNIZED"; }));
                        return;
                    case -3:
                        Invoke((Action)(() => { rich_textbox_status.Text = "ERR_OPTION_NOT_RECOGNIZED"; }));
                        return;
                    case -4:
                        Invoke((Action)(() => { rich_textbox_status.Text = "Too many spaces!!"; }));
                        return;
                    default:
                        break;
                }
                #endregion

                #region fill elements loop (parse episode)
                elements = new supporting.UC_search_result[SearchResult.Count];
                Parallel.For(0, SearchResult.Count, new ParallelOptions { MaxDegreeOfParallelism = 3 }, i =>
                {
                    try
                    {
                        elements[i] = new supporting.UC_search_result(SearchResult.GetRange(1, SearchResult.Count - 7), this);
                        elements[i].ComicURL = SearchResult[0];
                        elements[i].lab_day.Text = "day of update: No information";
                        elements[i].lab_main.Text = SearchResult[SearchResult.Count - 6];
                        elements[i].rich_textbox_description.Text = SearchResult[SearchResult.Count - 5];
                        elements[i].lab_author.Text = "Author: " + SearchResult[SearchResult.Count - 4];
                        elements[i].lab_last_update.Text = "Last update: " + SearchResult[SearchResult.Count - 3];
                        if (int.TryParse(SearchResult[SearchResult.Count - 2], out int totalEpisode))
                        {
                            elements[i].lab_total_eps.Text = "Total episodes: " + totalEpisode.ToString();
                        }
                        else
                        {
                            elements[i].lab_total_eps.Text = "Total episodes: No information";
                        }

                        Stream ThumbnailImageStream = WebRequest.Create(SearchResult[SearchResult.Count - 1]).GetResponse().GetResponseStream();

                        elements[i].pict_box_main.Image = Bitmap.FromStream(ThumbnailImageStream);

                        Invoke((Action)(() => { flow_layout_panel_main.Controls.Add(elements[i]); }));
                    }
                    catch (System.ArgumentOutOfRangeException)
                    {
                        Invoke((Action)(() => { rich_textbox_status.Text = "No search results"; }));
                        return;
                    }

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

            searching = false;
        }

        private void Bun_flat_btn_search_Click(object sender, EventArgs e)
        {
            if (searching)
            {
                Invoke((Action)(() => { rich_textbox_status.Text = "You can't search while the program is already searching"; }));
            }
            else
            {
                if (Regex.Matches(bun_mat_textbox_search.Text.Trim(), " ").Count <= 1)
                {
                    Bun_dropdown_source_onItemSelected(this, new EventArgs());
                    Task.Factory.StartNew(() => Search());
                }
                else
                {
                    MessageBox.Show("There are too many spaces in the query.\nOnly the first two word will be searched.");
                }
            }
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

        private void Bun_dropdown_source_onItemSelected(object sender, EventArgs e)
        {
            switch (bun_dropdown_source.selectedIndex)
            {
                case 0: //funbe
                    source = "3";
                    break;

                case 1: //naver webtoon
                    source = "0";
                    break;

                case 2: //naver bast challenge
                    source = "1";
                    break;

                case 3: //daum webtoon
                    source = "2";
                    break;
            }
        }

        public void Btn_revert_color(object sender, EventArgs e)
        {
            ((Button)sender).BackColor = Color.FromArgb(35, 35, 35);
        }

        #region btn_view
        private void Btn_view_Click(object sender, EventArgs e)
        {
            if (open_file_dialog_open.ShowDialog() == DialogResult.OK)
            {
                string tmpHTMLPath = Path.GetTempPath() + "toon_view_" + Guid.NewGuid() + "_.html";

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
                        w.WriteLine(@"<img src=""{0}"" style='height: auto; width: 45%; margin: auto'/>", open_file_dialog_open.FileName);
                        w.WriteLine(@"</div>");
                        w.WriteLine(@"</body>");
                        w.WriteLine(@"</html>");
                    }
                }

                Process.Start(tmpHTMLPath);
            }
        }

        private void Btn_view_MouseEnter(object sender, EventArgs e)
        {
            ((Button)sender).BackColor = Color.Gray;
        }
        #endregion

        #region btn_save_location
        private void Btn_save_location_Click(object sender, EventArgs e)
        {
            DialogResult result = folder_browser_dialog.ShowDialog();
        }

        private void Btn_save_location_MouseEnter(object sender, EventArgs e)
        {
            ((Button)sender).BackColor = SystemColors.HotTrack;
        }
        #endregion

        #region btn_show_err
        private void Btn_show_err_Click(object sender, EventArgs e)
        {
            MessageBox.Show(errorString);
        }

        private void Btn_show_err_MouseEnter(object sender, EventArgs e)
        {
            ((Button)sender).BackColor = Color.Gray;
        }
        #endregion

        #region btn_minimize
        private void Btn_minimize_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;
        }

        private void Btn_minimize_MouseEnter(object sender, EventArgs e)
        {
            ((Button)sender).BackColor = SystemColors.HotTrack;
        }
        #endregion

        #region btn_close
        private void Btn_close_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
        private void Btn_close_MouseEnter(object sender, EventArgs e)
        {
            ((Button)sender).BackColor = Color.Crimson;
        }


        #endregion
    }

    public class UDPSocket
    {
        /*
        Big thanks to: https://gist.github.com/darkguy2008
        Got code from: https://gist.github.com/darkguy2008/413a6fea3a5b4e67e5e0d96f750088a9

        UDPSocket s = new UDPSocket();
        s.Server("127.0.0.1", 3301);
        */
        private Socket _socket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);
        private const int bufSize = 8 * 1024;
        private State state = new State();
        private EndPoint epFrom = new IPEndPoint(IPAddress.Any, 0);
        private AsyncCallback recv = null;

        public class State
        {
            public byte[] buffer = new byte[bufSize];
        }

        public void Server(string address, int port)
        {
            _socket.SetSocketOption(SocketOptionLevel.IP, SocketOptionName.ReuseAddress, true);
            _socket.Bind(new IPEndPoint(IPAddress.Parse(address), port));
            Receive();
        }

        private void Receive()
        {
            _socket.BeginReceiveFrom(state.buffer, 0, bufSize, SocketFlags.None, ref epFrom, recv = (ar) =>
            {
                State so = (State)ar.AsyncState;
                int bytes = _socket.EndReceiveFrom(ar, ref epFrom);
                _socket.BeginReceiveFrom(so.buffer, 0, bufSize, SocketFlags.None, ref epFrom, recv, so);
                MessageBox.Show(Encoding.ASCII.GetString(so.buffer, 0, bytes));
            }, state);
        }
    }
}