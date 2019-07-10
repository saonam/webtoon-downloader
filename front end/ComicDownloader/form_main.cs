using System;
using System.IO;
using System.Net;
using System.Web;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Security;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Runtime.ExceptionServices;

namespace ComicDownloader
{
    public partial class form_main : Form
    {
        public static form_main form_instance;
        public form_main()
        {
            InitializeComponent();
            form_instance = this;
        }

        private void Bun_fat_btn_close_Click(object sender, EventArgs e)
        {
            if (MessageBox.Show("Are you sure you want to exit?\nAll the downloading process will be terminated.", "", MessageBoxButtons.YesNo, MessageBoxIcon.Question) == DialogResult.Yes)
            {
                Application.Exit();
            }
        }

        private void Bun_flat_btn_search_tab_Click(object sender, EventArgs e)
        {
            form_UC_comic_search.Visible = true;
            form_UC_comic_search.BringToFront();
        }

        private void Bun_flat_btn_downloading_tab_Click(object sender, EventArgs e)
        {
            form_UC_comic_downloading.Visible = true;
            form_UC_comic_downloading.BringToFront();
        }

        private void Bun_flat_btn_view_tab_Click(object sender, EventArgs e)
        {
            form_UC_comic_view.Visible = true;
            form_UC_comic_view.BringToFront();
        }

        private void Bun_flat_btn_settings_Click(object sender, EventArgs e)
        {
            form_UC_menu.Visible = true;
            form_UC_menu.BringToFront();
        }

        private void Bun_flat_btn_show_error_Click(object sender, EventArgs e)
        {
            MessageBox.Show(form_UC_comic_search.errorString);
        }
    }
}
