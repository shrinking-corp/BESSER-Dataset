from python_code import megal_MegalAnnotation
from python_code import megal_MegalElement
from python_code import megal_Selection

def test_megal_MegalAnnotation___init__():
    assert megal_MegalAnnotation.__init__(megal_MegalAnnotation('', megal_MegalAnnotation=megal_Selection(), megal_MegalAnnotation2=megal_MegalElement()), '', megal_MegalAnnotation=megal_Selection(), megal_MegalAnnotation2=megal_MegalElement()) == None


from python_code import megal_MegalNamed

def test_megal_MegalNamed___init__():
    assert megal_MegalNamed.__init__(megal_MegalNamed(''), '') == None


from python_code import megal_MegalEntityType
from python_code import megal_QueryParam
from python_code import megal_QueryReference

def test_megal_QueryParam___init__():
    assert megal_QueryParam.__init__(megal_QueryParam('', megal_QueryParam=megal_MegalEntityType(), megal_QueryParam68=megal_QueryReference()), '', megal_QueryParam=megal_MegalEntityType(), megal_QueryParam68=megal_QueryReference()) == None


from python_code import megal_QueryPos

def test_megal_QueryPos___init__():
    assert megal_QueryPos.__init__(megal_QueryPos(0), 0) == None


from python_code import megal_QueryString

def test_megal_QueryString___init__():
    assert megal_QueryString.__init__(megal_QueryString(''), '') == None

