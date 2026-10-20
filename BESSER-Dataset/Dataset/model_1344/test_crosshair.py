from python_code import myAtl_BinaryOperatorCS
from python_code import myAtl_InfixExpCS

def test_myAtl_BinaryOperatorCS___init__():
    assert myAtl_BinaryOperatorCS.__init__(myAtl_BinaryOperatorCS('', myAtl_BinaryOperatorCS=myAtl_InfixExpCS()), '', myAtl_BinaryOperatorCS=myAtl_InfixExpCS()) == None


from python_code import myAtl_BindingStat
from python_code import myAtl_ExpCS

def test_myAtl_BindingStat___init__():
    assert myAtl_BindingStat.__init__(myAtl_BindingStat('', myAtl_BindingStat69=myAtl_ExpCS(), myAtl_BindingStat=myAtl_ExpCS()), '', myAtl_BindingStat69=myAtl_ExpCS(), myAtl_BindingStat=myAtl_ExpCS()) == None


from python_code import myAtl_BooleanLiteralExpCS

def test_myAtl_BooleanLiteralExpCS___init__():
    assert myAtl_BooleanLiteralExpCS.__init__(myAtl_BooleanLiteralExpCS(''), '') == None


from python_code import myAtl_ExpCS
from python_code import myAtl_LetExpCS
from python_code import myAtl_LetVariableCS
from python_code import myAtl_TypeExpCS

def test_myAtl_LetVariableCS___init__():
    assert myAtl_LetVariableCS.__init__(myAtl_LetVariableCS('', myAtl_LetVariableCS=myAtl_LetExpCS(), myAtl_LetVariableCS131=myAtl_TypeExpCS(), myAtl_LetVariableCS134=myAtl_ExpCS()), '', myAtl_LetVariableCS=myAtl_LetExpCS(), myAtl_LetVariableCS131=myAtl_TypeExpCS(), myAtl_LetVariableCS134=myAtl_ExpCS()) == None


from python_code import myAtl_ExpCS
from python_code import myAtl_NavigatingArgExpCS
from python_code import myAtl_NavigatingBarArgCS
from python_code import myAtl_TypeExpCS

def test_myAtl_NavigatingBarArgCS___init__():
    assert myAtl_NavigatingBarArgCS.__init__(myAtl_NavigatingBarArgCS('', myAtl_NavigatingBarArgCS=myAtl_NavigatingArgExpCS(), myAtl_NavigatingBarArgCS97=myAtl_TypeExpCS(), myAtl_NavigatingBarArgCS100=myAtl_ExpCS()), '', myAtl_NavigatingBarArgCS=myAtl_NavigatingArgExpCS(), myAtl_NavigatingBarArgCS97=myAtl_TypeExpCS(), myAtl_NavigatingBarArgCS100=myAtl_ExpCS()) == None


from python_code import myAtl_ExpCS
from python_code import myAtl_NavigatingArgExpCS
from python_code import myAtl_NavigatingCommaArgCS
from python_code import myAtl_TypeExpCS

def test_myAtl_NavigatingCommaArgCS___init__():
    assert myAtl_NavigatingCommaArgCS.__init__(myAtl_NavigatingCommaArgCS('', myAtl_NavigatingCommaArgCS=myAtl_NavigatingArgExpCS(), myAtl_NavigatingCommaArgCS105=myAtl_TypeExpCS(), myAtl_NavigatingCommaArgCS108=myAtl_ExpCS()), '', myAtl_NavigatingCommaArgCS=myAtl_NavigatingArgExpCS(), myAtl_NavigatingCommaArgCS105=myAtl_TypeExpCS(), myAtl_NavigatingCommaArgCS108=myAtl_ExpCS()) == None


from python_code import myAtl_ExpCS
from python_code import myAtl_NavigatingArgExpCS
from python_code import myAtl_NavigatingSemiArgCS
from python_code import myAtl_TypeExpCS

def test_myAtl_NavigatingSemiArgCS___init__():
    assert myAtl_NavigatingSemiArgCS.__init__(myAtl_NavigatingSemiArgCS('', myAtl_NavigatingSemiArgCS=myAtl_NavigatingArgExpCS(), myAtl_NavigatingSemiArgCS113=myAtl_TypeExpCS(), myAtl_NavigatingSemiArgCS116=myAtl_ExpCS()), '', myAtl_NavigatingSemiArgCS=myAtl_NavigatingArgExpCS(), myAtl_NavigatingSemiArgCS113=myAtl_TypeExpCS(), myAtl_NavigatingSemiArgCS116=myAtl_ExpCS()) == None


from python_code import myAtl_NumberLiteralExpCS

def test_myAtl_NumberLiteralExpCS___init__():
    assert myAtl_NumberLiteralExpCS.__init__(myAtl_NumberLiteralExpCS(''), '') == None


from python_code import myAtl_StringExpCs

def test_myAtl_StringExpCs___init__():
    assert myAtl_StringExpCs.__init__(myAtl_StringExpCs(''), '') == None


from python_code import myAtl_StringLiteralExpCS

def test_myAtl_StringLiteralExpCS___init__():
    assert myAtl_StringLiteralExpCS.__init__(myAtl_StringLiteralExpCS(''), '') == None


from python_code import myAtl_ExpCS
from python_code import myAtl_TupleLiteralExpCS
from python_code import myAtl_TupleLiteralPartCS
from python_code import myAtl_TypeExpCS

def test_myAtl_TupleLiteralPartCS___init__():
    assert myAtl_TupleLiteralPartCS.__init__(myAtl_TupleLiteralPartCS('', myAtl_TupleLiteralPartCS=myAtl_TupleLiteralExpCS(), myAtl_TupleLiteralPartCS81=myAtl_TypeExpCS(), myAtl_TupleLiteralPartCS84=myAtl_ExpCS()), '', myAtl_TupleLiteralPartCS=myAtl_TupleLiteralExpCS(), myAtl_TupleLiteralPartCS81=myAtl_TypeExpCS(), myAtl_TupleLiteralPartCS84=myAtl_ExpCS()) == None


from python_code import myAtl_TupleTypeCS

def test_myAtl_TupleTypeCS___init__():
    assert myAtl_TupleTypeCS.__init__(myAtl_TupleTypeCS('\x00', myAtl_TupleTypeCS=set()), '', myAtl_TupleTypeCS=set()) == None


from python_code import myAtl_TypeLiteralCS
from python_code import myAtl_TypeLiteralExpCS

def test_myAtl_TypeLiteralCS___init__():
    assert myAtl_TypeLiteralCS.__init__(myAtl_TypeLiteralCS('', myAtl_TypeLiteralCS=myAtl_TypeLiteralExpCS()), '', myAtl_TypeLiteralCS=myAtl_TypeLiteralExpCS()) == None


from python_code import myAtl_TypeNameExpCS

def test_myAtl_TypeNameExpCS___init__():
    assert myAtl_TypeNameExpCS.__init__(myAtl_TypeNameExpCS('', '\x00'), '\x00\x00', '') == None


from python_code import myAtl_PrefixExpCS
from python_code import myAtl_UnaryOperatorCS

def test_myAtl_UnaryOperatorCS___init__():
    assert myAtl_UnaryOperatorCS.__init__(myAtl_UnaryOperatorCS('', myAtl_UnaryOperatorCS=myAtl_PrefixExpCS()), '', myAtl_UnaryOperatorCS=myAtl_PrefixExpCS()) == None

