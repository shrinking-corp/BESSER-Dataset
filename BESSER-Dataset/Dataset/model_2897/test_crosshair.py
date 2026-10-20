from python_code import moba_MobaBluetoothModule

def test_moba_MobaBluetoothModule___init__():
    assert moba_MobaBluetoothModule.__init__(moba_MobaBluetoothModule(''), '') == None


from python_code import moba_MobaEnum
from python_code import moba_MobaEnumLiteral

def test_moba_MobaEnumLiteral___init__():
    assert moba_MobaEnumLiteral.__init__(moba_MobaEnumLiteral('', '', 0, True, False, False, moba_MobaEnumLiteral=moba_MobaEnum()), '', '', 0, False, False, False, moba_MobaEnumLiteral=moba_MobaEnum()) == None


from python_code import moba_MobaFeature

def test_moba_MobaFeature___init__():
    assert moba_MobaFeature.__init__(moba_MobaFeature(''), '') == None


from python_code import moba_MobaGenerator
from python_code import moba_MobaGeneratorMixinFeature

def test_moba_MobaGenerator___init__():
    assert moba_MobaGenerator.__init__(moba_MobaGenerator('\x00\x00', False, moba_MobaGenerator21=moba_MobaGeneratorMixinFeature(), moba_MobaGenerator=set()), '', True, moba_MobaGenerator21=moba_MobaGeneratorMixinFeature(), moba_MobaGenerator=set()) == None


from python_code import moba_MobaGeneratorIDFeature

def test_moba_MobaGeneratorIDFeature___init__():
    assert moba_MobaGeneratorIDFeature.__init__(moba_MobaGeneratorIDFeature('', '\x00'), '\x00\x00', '') == None


from python_code import moba_MobaGeofenceTrigger

def test_moba_MobaGeofenceTrigger___init__():
    assert moba_MobaGeofenceTrigger.__init__(moba_MobaGeofenceTrigger(''), '') == None


from python_code import moba_MobaModel

def test_moba_MobaModel___init__():
    assert moba_MobaModel.__init__(moba_MobaModel('', moba_MobaModel=set()), '', moba_MobaModel=set()) == None


from python_code import moba_MobaMuliplicity
from python_code import moba_MobaMultiplicityAble

def test_moba_MobaMuliplicity___init__():
    assert moba_MobaMuliplicity.__init__(moba_MobaMuliplicity('', '\x00', moba_MobaMuliplicity=moba_MobaMultiplicityAble()), '\x00\x00', '', moba_MobaMuliplicity=moba_MobaMultiplicityAble()) == None


from python_code import moba_MobaNFCModule

def test_moba_MobaNFCModule___init__():
    assert moba_MobaNFCModule.__init__(moba_MobaNFCModule(''), '') == None


from python_code import moba_index_MobaIndex

def test_moba_index_MobaIndex___init__():
    assert moba_index_MobaIndex.__init__(moba_index_MobaIndex('', '', '', '', moba_index_MobaIndex=set()), '', '', '', '', moba_index_MobaIndex=set()) == None


from python_code import index_moba_MobaApplication
from python_code import moba_index_MobaIndexEntry

def test_moba_index_MobaIndexEntry___init__():
    assert moba_index_MobaIndexEntry.__init__(moba_index_MobaIndexEntry('', '', '', '', '', '', moba_index_MobaIndexEntry=index_moba_MobaApplication()), '', '', '', '', '\x00', '', moba_index_MobaIndexEntry=index_moba_MobaApplication()) == None

