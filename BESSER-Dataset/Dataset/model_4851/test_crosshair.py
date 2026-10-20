from python_code import aml_AbstractElements
from python_code import aml_Aml

def test_aml_AbstractElements___init__():
    assert aml_AbstractElements.__init__(aml_AbstractElements('', aml_AbstractElements=aml_Aml()), '', aml_AbstractElements=aml_Aml()) == None


from python_code import aml_Cable
from python_code import aml_ColorFeature

def test_aml_ColorFeature___init__():
    assert aml_ColorFeature.__init__(aml_ColorFeature('', '\x00', aml_ColorFeature=aml_Cable()), '\x00\x00', '', aml_ColorFeature=aml_Cable()) == None


from python_code import aml_Entity
from python_code import aml_Feature
from python_code import aml_PriceRule

def test_aml_Feature___init__():
    assert aml_Feature.__init__(aml_Feature('', '\x00', aml_Feature=aml_PriceRule(), aml_Feature25=aml_Entity()), '\x00\x00', '', aml_Feature=aml_PriceRule(), aml_Feature25=aml_Entity()) == None


from python_code import aml_Drive
from python_code import aml_FormFeature

def test_aml_FormFeature___init__():
    assert aml_FormFeature.__init__(aml_FormFeature('', 0, aml_FormFeature=aml_Drive()), '', 0, aml_FormFeature=aml_Drive()) == None


from python_code import aml_Cable
from python_code import aml_LengthFeature

def test_aml_LengthFeature___init__():
    assert aml_LengthFeature.__init__(aml_LengthFeature('\x00', 0.0, aml_LengthFeature=aml_Cable()), '', 0.0, aml_LengthFeature=aml_Cable()) == None


from python_code import aml_MaxFeature
from python_code import aml_MinMax

def test_aml_MaxFeature___init__():
    assert aml_MaxFeature.__init__(aml_MaxFeature('', 0, aml_MaxFeature=aml_MinMax()), '', 0, aml_MaxFeature=aml_MinMax()) == None


from python_code import aml_Cable
from python_code import aml_NetWorkFeature

def test_aml_NetWorkFeature___init__():
    assert aml_NetWorkFeature.__init__(aml_NetWorkFeature('', '\x00', aml_NetWorkFeature=aml_Cable()), '\x00\x00', '', aml_NetWorkFeature=aml_Cable()) == None


from python_code import aml_MinMax
from python_code import aml_ProductPUIDFeature

def test_aml_ProductPUIDFeature___init__():
    assert aml_ProductPUIDFeature.__init__(aml_ProductPUIDFeature('', 0, aml_ProductPUIDFeature=aml_MinMax()), '', 0, aml_ProductPUIDFeature=aml_MinMax()) == None


from python_code import aml_Drive
from python_code import aml_SizeFeature

def test_aml_SizeFeature___init__():
    assert aml_SizeFeature.__init__(aml_SizeFeature('', 0, aml_SizeFeature=aml_Drive()), '', 0, aml_SizeFeature=aml_Drive()) == None


from python_code import aml_Drive
from python_code import aml_SpeedFeature

def test_aml_SpeedFeature___init__():
    assert aml_SpeedFeature.__init__(aml_SpeedFeature('\x00', 0.0, aml_SpeedFeature=aml_Drive()), '', 0.0, aml_SpeedFeature=aml_Drive()) == None


from python_code import aml_MinMax
from python_code import aml_TargetGroupFeature

def test_aml_TargetGroupFeature___init__():
    assert aml_TargetGroupFeature.__init__(aml_TargetGroupFeature('', '\x00', aml_TargetGroupFeature=aml_MinMax()), '\x00\x00', '', aml_TargetGroupFeature=aml_MinMax()) == None


from python_code import aml_Drive
from python_code import aml_TypeFeature

def test_aml_TypeFeature___init__():
    assert aml_TypeFeature.__init__(aml_TypeFeature('', '\x00', aml_TypeFeature=aml_Drive()), '\x00\x00', '', aml_TypeFeature=aml_Drive()) == None

