using System;
using System.IO;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Diagnostics;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ComicDownloader.ComicUserControl
{
    public partial class UC_comic_view : UserControl
    {
        public UC_comic_view()
        {
            InitializeComponent();
            open_file_dialog.Filter = "Image files (*.jpg, *.jpeg, *.jpe, *.jfif, *.png, *.bmp) | *.jpg; *.jpeg; *.jpe; *.jfif; *.png; *.bmp";
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
                    w.WriteLine(@"<html>");
                    w.WriteLine(@"<head> <title> Comic View </title> </head>");
                    w.WriteLine(@"<body>");
                    w.WriteLine(@"<div align=""center"">");
                    w.WriteLine(@"<img src=""{0}"" style='height: auto; width: 45%; margin: auto'/>", ImagePath);
                    w.WriteLine(@"</div>");
                    w.WriteLine(@"</body>");
                    w.WriteLine(@"</html>");
                }
            }

            Process.Start(tmpHTMLPath);
        }

        private void UC_comic_view_Load(object sender, EventArgs e)
        {
            //get a list of path of all the files in the comic directory
            //display a list of them in a flow layout panel
        }
    }
}
