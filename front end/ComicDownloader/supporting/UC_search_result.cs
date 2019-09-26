using System;
using System.Windows.Forms;
using System.Threading.Tasks;
using System.Collections.Generic;

namespace ComicDownloader.supporting
{
    public partial class UC_search_result : UserControl
    {
        form_main main_form;
        public string ComicURL = "";
        List<string> URLList;

        public UC_search_result(List<string> ParentURLList, form_main Parentmain_form)
        {
            InitializeComponent();
            URLList = ParentURLList;
            main_form = Parentmain_form;
        }

        public void Download()
        {
            form_comic_range_input inputForm = new form_comic_range_input(ComicURL, URLList, main_form);

            Invoke(new Action(() =>
            {
                for (int i = 0; i < URLList.Count; i++)
                { // I put this outside the inputForm initializing code so it will run after everything is complete.
                    inputForm.rich_textbox_url_list.Text += "\n" + (i + 1).ToString() + ": " + URLList[i];
                }

                inputForm.lab_num_results.Text = URLList.Count.ToString() + " Results";
            }));

            

            inputForm.ShowDialog();
        }

        private void Bun_falt_btn_download_Click(object sender, EventArgs e)
        {
            Task.Factory.StartNew(() => Download());
        }
    }
}
