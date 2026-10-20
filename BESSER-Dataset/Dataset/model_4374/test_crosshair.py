from python_code import hydraconstraints_Model

def test_hydraconstraints_Model___init__():
    assert hydraconstraints_Model.__init__(hydraconstraints_Model('', hydraconstraints_Model=set()), '', hydraconstraints_Model=set()) == None

def test_hydraconstraints_Model_featureModelExists():
    assert hydraconstraints_Model.featureModelExists(hydraconstraints_Model('', hydraconstraints_Model=set()), '\x00', '') == None


from python_code import hydraconstraints_Context
from python_code import hydraconstraints_MultipleFeature

def test_hydraconstraints_MultipleFeature___init__():
    assert hydraconstraints_MultipleFeature.__init__(hydraconstraints_MultipleFeature('', hydraconstraints_MultipleFeature=hydraconstraints_Context()), '', hydraconstraints_MultipleFeature=hydraconstraints_Context()) == None

def test_hydraconstraints_MultipleFeature_isMultipleFeature():
    assert hydraconstraints_MultipleFeature.isMultipleFeature(hydraconstraints_MultipleFeature('', hydraconstraints_MultipleFeature=hydraconstraints_Context()), 0, '\x00\x00') == None


from python_code import hydraconstraints_Number

def test_hydraconstraints_Number___init__():
    assert hydraconstraints_Number.__init__(hydraconstraints_Number(0), 0) == None


from python_code import hydraconstraints_Operand

def test_hydraconstraints_Operand___init__():
    assert hydraconstraints_Operand.__init__(hydraconstraints_Operand()) == None

def test_hydraconstraints_Operand_evaluate():
    assert hydraconstraints_Operand.evaluate(hydraconstraints_Operand(), '', '') == None


from python_code import hydraconstraints_SimpleFeature

def test_hydraconstraints_SimpleFeature___init__():
    assert hydraconstraints_SimpleFeature.__init__(hydraconstraints_SimpleFeature(''), '') == None

def test_hydraconstraints_SimpleFeature_isSimpleFeature():
    assert hydraconstraints_SimpleFeature.isSimpleFeature(hydraconstraints_SimpleFeature(''), 0, '\x00\x00') == None

