from python_code import pascal_atrib
from python_code import pascal_expression
from python_code import pascal_statement

def test_pascal_atrib___init__():
    assert pascal_atrib.__init__(pascal_atrib('', pascal_atrib=pascal_statement(), pascal_atrib12=pascal_expression()), '', pascal_atrib=pascal_statement(), pascal_atrib12=pascal_expression()) == None


from python_code import pascal_Pascal
from python_code import pascal_program

def test_pascal_program___init__():
    assert pascal_program.__init__(pascal_program('', pascal_program=pascal_Pascal()), '', pascal_program=pascal_Pascal()) == None


from python_code import pascal_rel_expression

def test_pascal_rel_expression___init__():
    assert pascal_rel_expression.__init__(pascal_rel_expression('', '', '', '', ''), '', '', '', '', '') == None


from python_code import pascal_var_decl

def test_pascal_var_decl___init__():
    assert pascal_var_decl.__init__(pascal_var_decl('', '', '\x00\x00'), '', '', '') == None


from python_code import pascal_var_list

def test_pascal_var_list___init__():
    assert pascal_var_list.__init__(pascal_var_list('', '', '\x00\x00'), '', '', '') == None

