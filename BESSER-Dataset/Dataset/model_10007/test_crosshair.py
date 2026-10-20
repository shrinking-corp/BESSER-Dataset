from python_code import fruit_Apple
from python_code import fruit_Stem

def test_fruit_Apple___init__():
    assert fruit_Apple.__init__(fruit_Apple('', fruit_Apple=fruit_Stem()), '', fruit_Apple=fruit_Stem()) == None

def test_fruit_Apple_label():
    assert fruit_Apple.label(fruit_Apple('', fruit_Apple=fruit_Stem()), 0) == None

def test_fruit_Apple_preferredLabel():
    assert fruit_Apple.preferredLabel(fruit_Apple('', fruit_Apple=fruit_Stem()), 0) == None

def test_fruit_Apple_newApple():
    assert fruit_Apple.newApple(fruit_Apple('', fruit_Apple=fruit_Stem())) == None

