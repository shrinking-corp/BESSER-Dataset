from python_code import paplj_Bool

def test_paplj_Bool___init__():
    assert paplj_Bool.__init__(paplj_Bool(True), False) == None


from python_code import paplj_Expr
from python_code import paplj_Member
from python_code import paplj_MemberRef

def test_paplj_MemberRef___init__():
    assert paplj_MemberRef.__init__(paplj_MemberRef(False, paplj_MemberRef=paplj_Expr(), paplj_MemberRef95=paplj_Member(), paplj_MemberRef98=set()), False, paplj_MemberRef=paplj_Expr(), paplj_MemberRef95=paplj_Member(), paplj_MemberRef98=set()) == None


from python_code import paplj_Num

def test_paplj_Num___init__():
    assert paplj_Num.__init__(paplj_Num(0), 0) == None


from python_code import paplj_Expr
from python_code import paplj_Program

def test_paplj_Program___init__():
    assert paplj_Program.__init__(paplj_Program('', paplj_Program=set(), paplj_Program2=set(), paplj_Program4=paplj_Expr()), '', paplj_Program=set(), paplj_Program2=set(), paplj_Program4=paplj_Expr()) == None

