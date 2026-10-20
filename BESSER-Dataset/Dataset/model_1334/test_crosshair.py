from python_code import minioclcs_AccVarCS
from python_code import minioclcs_ExpCS
from python_code import minioclcs_IterateExpCS
from python_code import minioclcs_PathNameCS

def test_minioclcs_AccVarCS___init__():
    assert minioclcs_AccVarCS.__init__(minioclcs_AccVarCS('', minioclcs_AccVarCS=minioclcs_IterateExpCS(), minioclcs_AccVarCS57=minioclcs_PathNameCS(), minioclcs_AccVarCS60=minioclcs_ExpCS()), '', minioclcs_AccVarCS=minioclcs_IterateExpCS(), minioclcs_AccVarCS57=minioclcs_PathNameCS(), minioclcs_AccVarCS60=minioclcs_ExpCS()) == None


from python_code import minioclcs_BooleanExpCS

def test_minioclcs_BooleanExpCS___init__():
    assert minioclcs_BooleanExpCS.__init__(minioclcs_BooleanExpCS(True), False) == None


from python_code import minioclcs_CollectionLiteralExpCS

def test_minioclcs_CollectionLiteralExpCS___init__():
    assert minioclcs_CollectionLiteralExpCS.__init__(minioclcs_CollectionLiteralExpCS('', minioclcs_CollectionLiteralExpCS=set()), '', minioclcs_CollectionLiteralExpCS=set()) == None


from python_code import minioclcs_ImportCS
from python_code import minioclcs_RootCS

def test_minioclcs_ImportCS___init__():
    assert minioclcs_ImportCS.__init__(minioclcs_ImportCS('', '\x00', minioclcs_ImportCS=minioclcs_RootCS()), '\x00\x00', '', minioclcs_ImportCS=minioclcs_RootCS()) == None


from python_code import minioclcs_IntLiteralExpCS

def test_minioclcs_IntLiteralExpCS___init__():
    assert minioclcs_IntLiteralExpCS.__init__(minioclcs_IntLiteralExpCS(0), 0) == None


from python_code import minioclcs_IteratorVarCS
from python_code import minioclcs_LoopExpCS
from python_code import minioclcs_PathNameCS

def test_minioclcs_IteratorVarCS___init__():
    assert minioclcs_IteratorVarCS.__init__(minioclcs_IteratorVarCS('', minioclcs_IteratorVarCS=minioclcs_LoopExpCS(), minioclcs_IteratorVarCS53=minioclcs_PathNameCS()), '', minioclcs_IteratorVarCS=minioclcs_LoopExpCS(), minioclcs_IteratorVarCS53=minioclcs_PathNameCS()) == None


from python_code import minioclcs_ExpCS
from python_code import minioclcs_LetExpCS
from python_code import minioclcs_LetVarCS
from python_code import minioclcs_PathNameCS

def test_minioclcs_LetVarCS___init__():
    assert minioclcs_LetVarCS.__init__(minioclcs_LetVarCS('', minioclcs_LetVarCS=minioclcs_LetExpCS(), minioclcs_LetVarCS81=minioclcs_PathNameCS(), minioclcs_LetVarCS84=minioclcs_ExpCS()), '', minioclcs_LetVarCS=minioclcs_LetExpCS(), minioclcs_LetVarCS81=minioclcs_PathNameCS(), minioclcs_LetVarCS84=minioclcs_ExpCS()) == None

