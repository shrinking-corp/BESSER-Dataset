from python_code import UseCases_BooleanExpression

def test_UseCases_BooleanExpression___init__():
    assert UseCases_BooleanExpression.__init__(UseCases_BooleanExpression(''), '') == None


from python_code import UseCases_LocationReference

def test_UseCases_LocationReference___init__():
    assert UseCases_LocationReference.__init__(UseCases_LocationReference(''), '') == None


from python_code import Extend
from python_code import Include
from python_code import UseCases_Instance
from python_code import UseCases_UseCase

def test_UseCases_UseCase___init__():
    assert UseCases_UseCase.__init__(UseCases_UseCase('', addition=Include(), base=Include(), extension=Extend(), base7=Extend(), useCase=set(), Classifier=UseCases_Instance()), '', addition=Include(), base=Include(), extension=Extend(), base7=Extend(), useCase=set(), Classifier=UseCases_Instance()) == None

