from python_code import tortugaDSL_COLOREABLE
from python_code import tortugaDSL_COLOR_SPEC

def test_tortugaDSL_COLOREABLE___init__():
    assert tortugaDSL_COLOREABLE.__init__(tortugaDSL_COLOREABLE('', tortugaDSL_COLOREABLE=tortugaDSL_COLOR_SPEC()), '', tortugaDSL_COLOREABLE=tortugaDSL_COLOR_SPEC()) == None


from python_code import tortugaDSL_DRAW_STRING

def test_tortugaDSL_DRAW_STRING___init__():
    assert tortugaDSL_DRAW_STRING.__init__(tortugaDSL_DRAW_STRING(''), '') == None


from python_code import tortugaDSL_REFERENCIABLE
from python_code import tortugaDSL_VARIABLE_REF

def test_tortugaDSL_REFERENCIABLE___init__():
    assert tortugaDSL_REFERENCIABLE.__init__(tortugaDSL_REFERENCIABLE('', tortugaDSL_REFERENCIABLE=tortugaDSL_VARIABLE_REF()), '', tortugaDSL_REFERENCIABLE=tortugaDSL_VARIABLE_REF()) == None


from python_code import tortugaDSL_PROCEDURE_CALL
from python_code import tortugaDSL_TO

def test_tortugaDSL_TO___init__():
    assert tortugaDSL_TO.__init__(tortugaDSL_TO('', tortugaDSL_TO=set(), tortugaDSL_TO37=tortugaDSL_PROCEDURE_CALL()), '', tortugaDSL_TO=set(), tortugaDSL_TO37=tortugaDSL_PROCEDURE_CALL()) == None


from python_code import tortugaDSL_VALUE

def test_tortugaDSL_VALUE___init__():
    assert tortugaDSL_VALUE.__init__(tortugaDSL_VALUE(0.0), 0.0) == None

