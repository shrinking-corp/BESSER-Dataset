from python_code import cst_CSTNode

def test_cst_CSTNode___init__():
    assert cst_CSTNode.__init__(cst_CSTNode(0, 0), 0, 0) == None


from python_code import cst_Comment

def test_cst_Comment___init__():
    assert cst_Comment.__init__(cst_Comment(''), '') == None


from python_code import cst_Macro

def test_cst_Macro___init__():
    assert cst_Macro.__init__(cst_Macro('', cst_Macro=set()), '', cst_Macro=set()) == None


from python_code import cst_Module
from python_code import cst_ModuleElement

def test_cst_ModuleElement___init__():
    assert cst_ModuleElement.__init__(cst_ModuleElement('', '\x00', cst_ModuleElement=cst_Module()), '\x00\x00', '', cst_ModuleElement=cst_Module()) == None


from python_code import cst_Module
from python_code import cst_ModuleExtendsValue

def test_cst_ModuleExtendsValue___init__():
    assert cst_ModuleExtendsValue.__init__(cst_ModuleExtendsValue('', cst_ModuleExtendsValue=cst_Module()), '', cst_ModuleExtendsValue=cst_Module()) == None


from python_code import cst_Module
from python_code import cst_ModuleImportsValue

def test_cst_ModuleImportsValue___init__():
    assert cst_ModuleImportsValue.__init__(cst_ModuleImportsValue('', cst_ModuleImportsValue=cst_Module()), '', cst_ModuleImportsValue=cst_Module()) == None


from python_code import cst_Template
from python_code import cst_TemplateOverridesValue

def test_cst_TemplateOverridesValue___init__():
    assert cst_TemplateOverridesValue.__init__(cst_TemplateOverridesValue('', cst_TemplateOverridesValue=cst_Template()), '', cst_TemplateOverridesValue=cst_Template()) == None


from python_code import cst_TextExpression

def test_cst_TextExpression___init__():
    assert cst_TextExpression.__init__(cst_TextExpression(''), '') == None

