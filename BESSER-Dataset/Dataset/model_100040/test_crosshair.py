from python_code import qsar_DescriptorType
from python_code import qsar_DescriptorlistType

def test_qsar_DescriptorType___init__():
    assert qsar_DescriptorType.__init__(qsar_DescriptorType('', '', '', qsar_DescriptorType=qsar_DescriptorlistType(), qsar_DescriptorType5=set()), '', '', '', qsar_DescriptorType=qsar_DescriptorlistType(), qsar_DescriptorType5=set()) == None


from python_code import qsar_DescriptorproviderType
from python_code import qsar_QsarType

def test_qsar_DescriptorproviderType___init__():
    assert qsar_DescriptorproviderType.__init__(qsar_DescriptorproviderType('', '', '', '', '', qsar_DescriptorproviderType=qsar_QsarType()), '', '', '', '', '', qsar_DescriptorproviderType=qsar_QsarType()) == None


from python_code import qsar_DescriptorresultType
from python_code import qsar_DescriptorresultlistsType

def test_qsar_DescriptorresultType___init__():
    assert qsar_DescriptorresultType.__init__(qsar_DescriptorresultType('\x00\x00', '', qsar_DescriptorresultType=qsar_DescriptorresultlistsType(), qsar_DescriptorresultType3=set()), '', '', qsar_DescriptorresultType=qsar_DescriptorresultlistsType(), qsar_DescriptorresultType3=set()) == None


from python_code import qsar_DocumentRoot

def test_qsar_DocumentRoot___init__():
    assert qsar_DocumentRoot.__init__(qsar_DocumentRoot('', qsar_DocumentRoot=set(), qsar_DocumentRoot8=set(), qsar_DocumentRoot11=set()), '', qsar_DocumentRoot=set(), qsar_DocumentRoot8=set(), qsar_DocumentRoot11=set()) == None


from python_code import qsar_MetadataType
from python_code import qsar_QsarType

def test_qsar_MetadataType___init__():
    assert qsar_MetadataType.__init__(qsar_MetadataType('', '', '', '', '', qsar_MetadataType30=qsar_QsarType(), qsar_MetadataType=set()), '', '', '', '\x00', '', qsar_MetadataType30=qsar_QsarType(), qsar_MetadataType=set()) == None


from python_code import qsar_PreprocessingStepType
from python_code import qsar_PreprocessingType

def test_qsar_PreprocessingStepType___init__():
    assert qsar_PreprocessingStepType.__init__(qsar_PreprocessingStepType('', '', '', '', '', qsar_PreprocessingStepType=qsar_PreprocessingType()), '', '', '', '', '', qsar_PreprocessingStepType=qsar_PreprocessingType()) == None


from python_code import qsar_ResourceType
from python_code import qsar_StructurelistType

def test_qsar_ResourceType___init__():
    assert qsar_ResourceType.__init__(qsar_ResourceType('', '', '', '', '', '', '', '', '', '', qsar_ResourceType=set(), qsar_ResourceType39=qsar_StructurelistType()), '\x00', '', '', '', '', '', '', '', '', '', qsar_ResourceType=set(), qsar_ResourceType39=qsar_StructurelistType()) == None


from python_code import qsar_ResponseType
from python_code import qsar_ResponsesListType

def test_qsar_ResponseType___init__():
    assert qsar_ResponseType.__init__(qsar_ResponseType('\x00\x00', '', '', '', qsar_ResponseType=qsar_ResponsesListType()), '', '', '', '', qsar_ResponseType=qsar_ResponsesListType()) == None


from python_code import qsar_QsarType
from python_code import qsar_ResponseunitType

def test_qsar_ResponseunitType___init__():
    assert qsar_ResponseunitType.__init__(qsar_ResponseunitType('', '', '', '', '', qsar_ResponseunitType=qsar_QsarType()), '', '', '', '', '', qsar_ResponseunitType=qsar_QsarType()) == None

