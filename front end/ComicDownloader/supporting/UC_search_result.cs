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

namespace ComicDownloader.supporting
{
    public partial class UC_search_result : UserControl
    {
        public string ComicURL = "";
        Regex CMDRegex = new Regex(@"\w:\\.*>.*");
        List<string> URLList;

        public UC_search_result(List<string> ParentURLList)
        {
            InitializeComponent();
            URLList = ParentURLList;
        }

        public void Download()
        {
            form_comic_range_input inputForm = new form_comic_range_input(ComicURL, URLList);

            for (int i = 0; i < URLList.Count; i++)
            { // I put this outside the inputForm initializing code so it will run after everything is complete.
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
