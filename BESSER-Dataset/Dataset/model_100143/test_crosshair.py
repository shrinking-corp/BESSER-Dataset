from python_code import model_Database
from python_code import model_Site

def test_model_Database___init__():
    assert model_Database.__init__(model_Database('', model_Database=set(), model_Database2=set(), model_Database82=model_Site()), '', model_Database=set(), model_Database2=set(), model_Database82=model_Site()) == None


from python_code import model_DescribedElement

def test_model_DescribedElement___init__():
    assert model_DescribedElement.__init__(model_DescribedElement(''), '') == None


from python_code import model_FQNamedElement

def test_model_FQNamedElement___init__():
    assert model_FQNamedElement.__init__(model_FQNamedElement()) == None

def test_model_FQNamedElement_getFQName():
    assert model_FQNamedElement.getFQName(model_FQNamedElement()) == None


from python_code import model_File
from python_code import model_TaskFile

def test_model_File___init__():
    assert model_File.__init__(model_File('\x00\x00', '', model_File=set(), model_File58=model_TaskFile(), model_File61=model_TaskFile()), '', '', model_File=set(), model_File58=model_TaskFile(), model_File61=model_TaskFile()) == None


from python_code import model_FileSet
from python_code import model_Site

def test_model_FileSet___init__():
    assert model_FileSet.__init__(model_FileSet('', model_FileSet=set(), model_FileSet85=model_Site()), '', model_FileSet=set(), model_FileSet85=model_Site()) == None


from python_code import model_Mapping

def test_model_Mapping___init__():
    assert model_Mapping.__init__(model_Mapping(''), '') == None


from python_code import model_NamedElement

def test_model_NamedElement___init__():
    assert model_NamedElement.__init__(model_NamedElement(''), '') == None


from python_code import model_SCTFile

def test_model_SCTFile___init__():
    assert model_SCTFile.__init__(model_SCTFile('', model_SCTFile=set(), model_SCTFile21=set()), '', model_SCTFile=set(), model_SCTFile21=set()) == None


from python_code import model_SeparatedElement

def test_model_SeparatedElement___init__():
    assert model_SeparatedElement.__init__(model_SeparatedElement(''), '') == None


from python_code import model_Schema
from python_code import model_View

def test_model_View___init__():
    assert model_View.__init__(model_View('', model_View=model_Schema()), '', model_View=model_Schema()) == None

