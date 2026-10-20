import datetime as _ch_datetime
from python_code import PhysicalCard
from python_code import restapp_model_Card

def test_restapp_model_Card___init__():
    assert restapp_model_Card.__init__(restapp_model_Card(0, _ch_datetime.date(1, 1, 1), 0.0, 0, 0.0, 0.0, 0.0, restapp_model_Card=PhysicalCard()), 0, _ch_datetime.date(1, 1, 2), 0.0, 0, 0.0, 0.0, 0.0, restapp_model_Card=PhysicalCard()) == None


from python_code import restapp_model_Category

def test_restapp_model_Category___init__():
    assert restapp_model_Category.__init__(restapp_model_Category(0, '\x00', '', 0), 0, '', '', 0) == None


import datetime as _ch_datetime
from python_code import restapp_model_Employee

def test_restapp_model_Employee___init__():
    assert restapp_model_Employee.__init__(restapp_model_Employee('', '', '', '', False, _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), 0.0, 0.0, 0, 0, '', '', ''), '', '', '', '', False, _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), 0.0, 0.0, 0, 0, '', '', '') == None


from python_code import restapp_model_PhysicalCard

def test_restapp_model_PhysicalCard___init__():
    assert restapp_model_PhysicalCard.__init__(restapp_model_PhysicalCard(0, 0, 0), 0, 0, 0) == None


import datetime as _ch_datetime
from python_code import restapp_model_Price

def test_restapp_model_Price___init__():
    assert restapp_model_Price.__init__(restapp_model_Price(0, 0.0, _ch_datetime.date(1, 1, 1), restapp_model_Price=set()), 0, 0.0, _ch_datetime.date(1, 1, 1), restapp_model_Price=set()) == None


from python_code import Category
from python_code import restapp_model_Product

def test_restapp_model_Product___init__():
    assert restapp_model_Product.__init__(restapp_model_Product(0, '', '', 0, 0, restapp_model_Product=Category()), 0, '', '', 0, 0, restapp_model_Product=Category()) == None


import datetime as _ch_datetime
from python_code import Card
from python_code import Product
from python_code import User
from python_code import restapp_model_ProductsCard

def test_restapp_model_ProductsCard___init__():
    assert restapp_model_ProductsCard.__init__(restapp_model_ProductsCard(0, _ch_datetime.date(1, 1, 1), restapp_model_ProductsCard=Product(), restapp_model_ProductsCard14=Card(), restapp_model_ProductsCard16=User()), 0, _ch_datetime.date(1, 1, 2), restapp_model_ProductsCard=Product(), restapp_model_ProductsCard14=Card(), restapp_model_ProductsCard16=User()) == None


from python_code import Product
from python_code import Purchase
from python_code import restapp_model_ProductsPurchase

def test_restapp_model_ProductsPurchase___init__():
    assert restapp_model_ProductsPurchase.__init__(restapp_model_ProductsPurchase(0, 0.0, 0, 0.0, restapp_model_ProductsPurchase=Purchase(), restapp_model_ProductsPurchase8=Product()), 0, 0.0, 0, 0.0, restapp_model_ProductsPurchase=Purchase(), restapp_model_ProductsPurchase8=Product()) == None


from python_code import restapp_model_Provider

def test_restapp_model_Provider___init__():
    assert restapp_model_Provider.__init__(restapp_model_Provider(0, '', '', '', '', ''), 0, '', '', '', '\x00', '') == None


import datetime as _ch_datetime
from python_code import Provider
from python_code import User
from python_code import restapp_model_Purchase

def test_restapp_model_Purchase___init__():
    assert restapp_model_Purchase.__init__(restapp_model_Purchase(0, _ch_datetime.date(1, 1, 1), 0.0, 0, 0.0, restapp_model_Purchase5=User(), restapp_model_Purchase=Provider()), 0, _ch_datetime.date(1, 1, 1), 0.0, 0, 0.0, restapp_model_Purchase5=User(), restapp_model_Purchase=Provider()) == None


from python_code import Employee
from python_code import restapp_model_User

def test_restapp_model_User___init__():
    assert restapp_model_User.__init__(restapp_model_User(0, '\x00', '', 0, restapp_model_User=Employee()), 0, '', '', 0, restapp_model_User=Employee()) == None

