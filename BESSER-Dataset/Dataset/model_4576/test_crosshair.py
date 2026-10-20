from python_code import sensinact_DSL_CEP_DURATION_MIN

def test_sensinact_DSL_CEP_DURATION_MIN___init__():
    assert sensinact_DSL_CEP_DURATION_MIN.__init__(sensinact_DSL_CEP_DURATION_MIN(''), '') == None


from python_code import sensinact_DSL_CEP_DURATION_SEC

def test_sensinact_DSL_CEP_DURATION_SEC___init__():
    assert sensinact_DSL_CEP_DURATION_SEC.__init__(sensinact_DSL_CEP_DURATION_SEC(''), '') == None


from python_code import sensinact_DSL_FLAG_AUTOSTART
from python_code import sensinact_DSL_SENSINACT

def test_sensinact_DSL_FLAG_AUTOSTART___init__():
    assert sensinact_DSL_FLAG_AUTOSTART.__init__(sensinact_DSL_FLAG_AUTOSTART(True, sensinact_DSL_FLAG_AUTOSTART=sensinact_DSL_SENSINACT()), False, sensinact_DSL_FLAG_AUTOSTART=sensinact_DSL_SENSINACT()) == None


from python_code import sensinact_DSL_Object_Boolean

def test_sensinact_DSL_Object_Boolean___init__():
    assert sensinact_DSL_Object_Boolean.__init__(sensinact_DSL_Object_Boolean(True), False) == None


from python_code import sensinact_DSL_Object_Number

def test_sensinact_DSL_Object_Number___init__():
    assert sensinact_DSL_Object_Number.__init__(sensinact_DSL_Object_Number(''), '') == None


from python_code import sensinact_DSL_Object_String

def test_sensinact_DSL_Object_String___init__():
    assert sensinact_DSL_Object_String.__init__(sensinact_DSL_Object_String(''), '') == None


from python_code import sensinact_DSL_Resource
from python_code import sensinact_DSL_SENSINACT

def test_sensinact_DSL_Resource___init__():
    assert sensinact_DSL_Resource.__init__(sensinact_DSL_Resource('\x00\x00', '', '', '', sensinact_DSL_Resource=sensinact_DSL_SENSINACT()), '', '', '', '', sensinact_DSL_Resource=sensinact_DSL_SENSINACT()) == None

