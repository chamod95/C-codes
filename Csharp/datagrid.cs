using System;  
using System.Data;  
using System.Windows.Forms;  
using System.Data.SqlClient;  
  
namespace SearchRecord  
{  
    public partial class frmSearch : Form  
    {  
        //Connection String  
        string cs = "Data Source=.;Initial Catalog=Sample;Integrated Security=true;";  
        SqlConnection con;  
        SqlDataAdapter adapt;  
        DataTable dt;  
        public frmSearch()  
        {  
            InitializeComponent();  
        }  
        //frmSearch Load Event  
        private void frmSearch_Load(object sender, EventArgs e)  
        {  
            con = new SqlConnection(cs);  
            con.Open();  
            adapt = new SqlDataAdapter("select * from tbl_Employee",con);  
            dt = new DataTable();  
            adapt.Fill(dt);  
            dataGridView1.DataSource = dt;  
            con.Close();  
        }  
        //txt_SearchName TextChanged Event  
        private void txt_SearchName_TextChanged(object sender, EventArgs e)  
        {  
            con = new SqlConnection(cs);  
            con.Open();  
            adapt = new SqlDataAdapter("select * from tbl_Employee where FirstName like '"+txt_SearchName.Text+"%'", con);  
            dt = new DataTable();  
            adapt.Fill(dt);  
            dataGridView1.DataSource = dt;  
            con.Close();  
        }  
    }  
}  