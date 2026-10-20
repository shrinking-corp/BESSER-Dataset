from python_code import smc_BlockSMC
from python_code import smc_Invocation
from python_code import smc_Smc

def test_smc_BlockSMC___init__():
    assert smc_BlockSMC.__init__(smc_BlockSMC('', '\x00', smc_BlockSMC42=smc_Invocation(), smc_BlockSMC=smc_Smc()), '\x00\x00', '', smc_BlockSMC42=smc_Invocation(), smc_BlockSMC=smc_Smc()) == None


from python_code import smc_BooleanLiteral

def test_smc_BooleanLiteral___init__():
    assert smc_BooleanLiteral.__init__(smc_BooleanLiteral(True), False) == None


from python_code import smc_Client

def test_smc_Client___init__():
    assert smc_Client.__init__(smc_Client(''), '') == None


from python_code import smc_Comparison
from python_code import smc_Expression

def test_smc_Comparison___init__():
    assert smc_Comparison.__init__(smc_Comparison('', smc_Comparison=smc_Expression(), smc_Comparison114=smc_Expression()), '', smc_Comparison=smc_Expression(), smc_Comparison114=smc_Expression()) == None


from python_code import smc_Database
from python_code import smc_Expression

def test_smc_Database___init__():
    assert smc_Database.__init__(smc_Database('', smc_Database=smc_Expression()), '', smc_Database=smc_Expression()) == None


from python_code import smc_DateLiteral

def test_smc_DateLiteral___init__():
    assert smc_DateLiteral.__init__(smc_DateLiteral(''), '') == None


from python_code import smc_DoubleLiteral

def test_smc_DoubleLiteral___init__():
    assert smc_DoubleLiteral.__init__(smc_DoubleLiteral(0.0), 0.0) == None


from python_code import smc_Equality
from python_code import smc_Expression

def test_smc_Equality___init__():
    assert smc_Equality.__init__(smc_Equality('', smc_Equality=smc_Expression(), smc_Equality109=smc_Expression()), '', smc_Equality=smc_Expression(), smc_Equality109=smc_Expression()) == None


from python_code import smc_IntLiteral

def test_smc_IntLiteral___init__():
    assert smc_IntLiteral.__init__(smc_IntLiteral(0), 0) == None


from python_code import smc_Expression
from python_code import smc_MulOrDiv

def test_smc_MulOrDiv___init__():
    assert smc_MulOrDiv.__init__(smc_MulOrDiv('', smc_MulOrDiv=smc_Expression(), smc_MulOrDiv124=smc_Expression()), '', smc_MulOrDiv=smc_Expression(), smc_MulOrDiv124=smc_Expression()) == None


from python_code import smc_CreateTable
from python_code import smc_ParamDecl

def test_smc_ParamDecl___init__():
    assert smc_ParamDecl.__init__(smc_ParamDecl('\x00\x00', '', '', '', smc_ParamDecl=smc_CreateTable()), '', '', '', '', smc_ParamDecl=smc_CreateTable()) == None


from python_code import smc_Expression
from python_code import smc_PlusOrMinus

def test_smc_PlusOrMinus___init__():
    assert smc_PlusOrMinus.__init__(smc_PlusOrMinus('', smc_PlusOrMinus=smc_Expression(), smc_PlusOrMinus119=smc_Expression()), '', smc_PlusOrMinus=smc_Expression(), smc_PlusOrMinus119=smc_Expression()) == None


from python_code import smc_StringLiteral

def test_smc_StringLiteral___init__():
    assert smc_StringLiteral.__init__(smc_StringLiteral(''), '') == None


from python_code import smc_TimeLiteral

def test_smc_TimeLiteral___init__():
    assert smc_TimeLiteral.__init__(smc_TimeLiteral(''), '') == None

