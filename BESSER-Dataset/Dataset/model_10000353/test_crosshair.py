import datetime as _ch_datetime
from python_code import Data_Pegawai

def test_Data_Pegawai___init__():
    assert Data_Pegawai.__init__(Data_Pegawai('', _ch_datetime.date(1, 1, 1), '', 0, '', ''), '', _ch_datetime.date(1, 1, 1), '', 0, '', '') == None


import datetime as _ch_datetime
from python_code import Data_Peminjaman

def test_Data_Peminjaman___init__():
    assert Data_Peminjaman.__init__(Data_Peminjaman(0, _ch_datetime.date(1, 1, 1), '', 0, '', ''), 0, _ch_datetime.date(1, 1, 1), '', 0, '', '') == None


import datetime as _ch_datetime
from python_code import Transaksi_Peminjaman

def test_Transaksi_Peminjaman___init__():
    assert Transaksi_Peminjaman.__init__(Transaksi_Peminjaman(0, '', '', 0, 0, _ch_datetime.date(1, 1, 1), ''), 0, '', '', 0, 0, _ch_datetime.date(1, 1, 1), '') == None


from python_code import account_CertificatesOfDepositAccount

def test_account_CertificatesOfDepositAccount___init__():
    assert account_CertificatesOfDepositAccount.__init__(account_CertificatesOfDepositAccount(0, 0.0), 0, 0.0) == None


from python_code import account_CheckingAccount

def test_account_CheckingAccount___init__():
    assert account_CheckingAccount.__init__(account_CheckingAccount(''), '') == None


from python_code import account_SavingsAccount

def test_account_SavingsAccount___init__():
    assert account_SavingsAccount.__init__(account_SavingsAccount(0.0), 0.0) == None

