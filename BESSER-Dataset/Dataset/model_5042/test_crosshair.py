from python_code import model_CEFACTCode

def test_model_CEFACTCode___init__():
    assert model_CEFACTCode.__init__(model_CEFACTCode('', '', '', '', ''), '', '', '', '', '') == None


from python_code import model_Dunning

def test_model_Dunning___init__():
    assert model_Dunning.__init__(model_Dunning(''), '') == None


from python_code import model_IDescribableEntity

def test_model_IDescribableEntity___init__():
    assert model_IDescribableEntity.__init__(model_IDescribableEntity(''), '') == None


import datetime as _ch_datetime
from python_code import model_IEntity

def test_model_IEntity___init__():
    assert model_IEntity.__init__(model_IEntity('\x00\x00', _ch_datetime.date(1, 1, 1), '', _ch_datetime.date(1, 1, 1), '', '', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1)), '', _ch_datetime.date(1, 1, 1), '\x00', _ch_datetime.date(1, 1, 1), '', '', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1)) == None

def test_model_IEntity_isSameAs():
    assert model_IEntity.isSameAs(model_IEntity('', _ch_datetime.date(1, 1, 2), '', _ch_datetime.date(1, 1, 3), '', '', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1))) == None


from python_code import model_TextCategory
from python_code import model_TextModule

def test_model_TextModule___init__():
    assert model_TextModule.__init__(model_TextModule('', model_TextModule=model_TextCategory()), '', model_TextModule=model_TextCategory()) == None


from python_code import model_Tenant
from python_code import model_User

def test_model_User___init__():
    assert model_User.__init__(model_User('\x00\x00', '', model_User68=set(), model_User=model_Tenant()), '', '', model_User68=set(), model_User=model_Tenant()) == None


from python_code import model_UserProperty

def test_model_UserProperty___init__():
    assert model_UserProperty.__init__(model_UserProperty('\x00\x00', '', '', ''), '', '', '', '') == None


import datetime as _ch_datetime
from python_code import model_Voucher
from python_code import model_VoucherCategory

def test_model_Voucher___init__():
    assert model_Voucher.__init__(model_Voucher('', '', '', '', _ch_datetime.date(1, 1, 2), '', '', '', model_Voucher=model_VoucherCategory(), model_Voucher40=set()), '', '', '', '', _ch_datetime.date(1, 1, 1), '', '', '\x00', model_Voucher=model_VoucherCategory(), model_Voucher40=set()) == None


from python_code import model_WebShop

def test_model_WebShop___init__():
    assert model_WebShop.__init__(model_WebShop('\x00\x00', '', model_WebShop=set()), '', '', model_WebShop=set()) == None

