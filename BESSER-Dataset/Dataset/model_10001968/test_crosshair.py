from python_code import Jurusans

def test_Jurusans___init__():
    assert Jurusans.__init__(Jurusans(0, 0, '\x00\x00'), 0, 0, '') == None


from python_code import Login

def test_Login___init__():
    assert Login.__init__(Login('', '\x00'), '\x00\x00', '') == None


from python_code import Mahasiswas

def test_Mahasiswas___init__():
    assert Mahasiswas.__init__(Mahasiswas(0), 0) == None


from python_code import Pembayarans

def test_Pembayarans___init__():
    assert Pembayarans.__init__(Pembayarans(0, '', '', '', 0, 0, 0, 0, '', 0, 0, 0), 0, '', '', '', 0, 0, 0, 0, '', 0, 0, 0) == None


from python_code import Prodis

def test_Prodis___init__():
    assert Prodis.__init__(Prodis(0, '', 0, 0, 0), 0, '', 0, 0, 0) == None


from python_code import Setting

def test_Setting___init__():
    assert Setting.__init__(Setting(0, '', '', '', '', '', '\x00', 0), 0, '', '', '', '', '', '', 0) == None


from python_code import masterBiaya

def test_masterBiaya___init__():
    assert masterBiaya.__init__(masterBiaya(0, 0, '', 0, 0, 0, 0), 0, 0, '', 0, 0, 0, 0) == None


from python_code import masterKategori

def test_masterKategori___init__():
    assert masterKategori.__init__(masterKategori(0, '\x00', 0, 0), 0, '', 0, 0) == None

