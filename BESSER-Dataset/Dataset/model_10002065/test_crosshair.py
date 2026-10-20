from python_code import Person
from python_code import str

def test_Person___init__():
    assert Person.__init__(Person(str(), str()), str(), str()) == None


from python_code import Stuff
from python_code import str

def test_Stuff___init__():
    assert Stuff.__init__(Stuff(str(), str()), str(), str()) == None


from python_code import Binary_File
from python_code import Exceptions
from python_code import ILogin_Interface
from python_code import User
from python_code import str

def test_User___init__():
    assert User.__init__(User(str(), str(), str(), str(), User_ILogin_02=ILogin_Interface(), binary_File4=Binary_File(), exceptions10=Exceptions()), str(), str(), str(), str(), User_ILogin_02=ILogin_Interface(), binary_File4=Binary_File(), exceptions10=Exceptions()) == None

