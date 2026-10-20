from python_code import family_Family
from python_code import family_Pet

def test_family_Pet___init__():
    assert family_Pet.__init__(family_Pet('', family_Pet=family_Family()), '', family_Pet=family_Family()) == None

