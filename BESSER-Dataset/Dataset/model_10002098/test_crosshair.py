from python_code import Browsing_Website
from python_code import User__Pengunjung__Actor

def test_Browsing_Website___init__():
    assert Browsing_Website.__init__(Browsing_Website(User__Pengunjung__Actor()), User__Pengunjung__Actor()) == None


from python_code import Admin_Actor
from python_code import Login_Website

def test_Login_Website___init__():
    assert Login_Website.__init__(Login_Website(Admin_Actor()), Admin_Actor()) == None


from python_code import Fitur_Pencarian_berdsarkan_penyakit_UseCase
from python_code import Forum_diskusi_UseCase
from python_code import Menu_Halaman_Website

def test_Menu_Halaman_Website___init__():
    assert Menu_Halaman_Website.__init__(Menu_Halaman_Website(Forum_diskusi_UseCase(), Fitur_Pencarian_berdsarkan_penyakit_UseCase()), Forum_diskusi_UseCase(), Fitur_Pencarian_berdsarkan_penyakit_UseCase()) == None


from python_code import Asal_daerah_tumbuhan_herbal_UseCase
from python_code import Cara_pengolahannya_UseCase
from python_code import Dosisnya_UseCase
from python_code import Gambar_tumbuhan_herbalnya_UseCase
from python_code import Jenis_tumbuhan_herbal_UseCase
from python_code import Kelas_Ordo_tumbuhan_herbal_UseCase
from python_code import Khasiatnya_apa_UseCase
from python_code import Nama_Tumbuh_Tumbuhan_Herbal
from python_code import Nama_latinnya_UseCase
from python_code import Obat__Produk_jadi__UseCase

def test_Nama_Tumbuh_Tumbuhan_Herbal___init__():
    assert Nama_Tumbuh_Tumbuhan_Herbal.__init__(Nama_Tumbuh_Tumbuhan_Herbal(Nama_latinnya_UseCase(), Jenis_tumbuhan_herbal_UseCase(), Asal_daerah_tumbuhan_herbal_UseCase(), Kelas_Ordo_tumbuhan_herbal_UseCase(), Khasiatnya_apa_UseCase(), Dosisnya_UseCase(), Cara_pengolahannya_UseCase(), Gambar_tumbuhan_herbalnya_UseCase(), Obat__Produk_jadi__UseCase()), Nama_latinnya_UseCase(), Jenis_tumbuhan_herbal_UseCase(), Asal_daerah_tumbuhan_herbal_UseCase(), Kelas_Ordo_tumbuhan_herbal_UseCase(), Khasiatnya_apa_UseCase(), Dosisnya_UseCase(), Cara_pengolahannya_UseCase(), Gambar_tumbuhan_herbalnya_UseCase(), Obat__Produk_jadi__UseCase()) == None


from python_code import Kelola_data_website_UseCase
from python_code import Menambah_membuat_data_website_UseCase
from python_code import Mengedit_data_website_UseCase
from python_code import Menghapus_data_website_UseCase
from python_code import Pengelola_Website

def test_Pengelola_Website___init__():
    assert Pengelola_Website.__init__(Pengelola_Website(Kelola_data_website_UseCase(), Menambah_membuat_data_website_UseCase(), Menghapus_data_website_UseCase(), Mengedit_data_website_UseCase()), Kelola_data_website_UseCase(), Menambah_membuat_data_website_UseCase(), Menghapus_data_website_UseCase(), Mengedit_data_website_UseCase()) == None

