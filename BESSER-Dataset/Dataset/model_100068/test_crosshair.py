from python_code import Ant_Attribut

def test_Ant_Attribut___init__():
    assert Ant_Attribut.__init__(Ant_Attribut('', '\x00'), '\x00\x00', '') == None


from python_code import Ant_ClassPath

def test_Ant_ClassPath___init__():
    assert Ant_ClassPath.__init__(Ant_ClassPath('', Ant_ClassPath=set(), Ant_ClassPath31=set()), '', Ant_ClassPath=set(), Ant_ClassPath31=set()) == None


from python_code import Ant_Copy
from python_code import FileSet
from python_code import FilterSet
from python_code import Mapper

def test_Ant_Copy___init__():
    assert Ant_Copy.__init__(Ant_Copy('', '', '', '', '', '', '\x00', '', Ant_Copy=FileSet(), Ant_Copy49=FilterSet(), Ant_Copy51=Mapper()), '', '', '', '', '', '', '', '', Ant_Copy=FileSet(), Ant_Copy49=FilterSet(), Ant_Copy51=Mapper()) == None


from python_code import Ant_Delete

def test_Ant_Delete___init__():
    assert Ant_Delete.__init__(Ant_Delete('\x00', '', '', '', '', '', '', '', '', '', '\x00'), '', '', '', '', '', '', '', '', '', '', '') == None


from python_code import Ant_Echo

def test_Ant_Echo___init__():
    assert Ant_Echo.__init__(Ant_Echo('', '', '\x00\x00'), '', '', '') == None


from python_code import Ant_Exec

def test_Ant_Exec___init__():
    assert Ant_Exec.__init__(Ant_Exec('', '\x00'), '\x00\x00', '') == None


from python_code import Ant_FileList

def test_Ant_FileList___init__():
    assert Ant_FileList.__init__(Ant_FileList('', '\x00'), '\x00\x00', '') == None


from python_code import Ant_FileSet

def test_Ant_FileSet___init__():
    assert Ant_FileSet.__init__(Ant_FileSet('', Ant_FileSet=set(), Ant_FileSet16=set(), Ant_FileSet18=set()), '', Ant_FileSet=set(), Ant_FileSet16=set(), Ant_FileSet18=set()) == None


from python_code import Ant_Filter

def test_Ant_Filter___init__():
    assert Ant_Filter.__init__(Ant_Filter('', '\x00'), '\x00\x00', '') == None


from python_code import Ant_FilterSet

def test_Ant_FilterSet___init__():
    assert Ant_FilterSet.__init__(Ant_FilterSet('', '', Ant_FilterSet=set(), Ant_FilterSet21=set()), '', '', Ant_FilterSet=set(), Ant_FilterSet21=set()) == None


from python_code import Ant_FiltersFile

def test_Ant_FiltersFile___init__():
    assert Ant_FiltersFile.__init__(Ant_FiltersFile(''), '') == None


from python_code import Ant_FormatTstamp

def test_Ant_FormatTstamp___init__():
    assert Ant_FormatTstamp.__init__(Ant_FormatTstamp('', '', '', '', ''), '', '', '', '', '') == None


from python_code import Ant_InExcludes

def test_Ant_InExcludes___init__():
    assert Ant_InExcludes.__init__(Ant_InExcludes('', '', '\x00\x00'), '', '', '') == None


from python_code import Ant_Jar

def test_Ant_Jar___init__():
    assert Ant_Jar.__init__(Ant_Jar('', '', '', '', ''), '', '', '', '', '') == None


from python_code import Ant_Java
from python_code import ClassPath

def test_Ant_Java___init__():
    assert Ant_Java.__init__(Ant_Java('', '', '\x00\x00', Ant_Java=ClassPath()), '', '', '', Ant_Java=ClassPath()) == None


from python_code import Ant_Javac
from python_code import ClassPath

def test_Ant_Javac___init__():
    assert Ant_Javac.__init__(Ant_Javac('', '', '', '', '', '', Ant_Javac=set(), Ant_Javac44=ClassPath()), '', '', '', '', '', '', Ant_Javac=set(), Ant_Javac44=ClassPath()) == None


from python_code import Ant_Javadoc

def test_Ant_Javadoc___init__():
    assert Ant_Javadoc.__init__(Ant_Javadoc('', '', '', '', '', '', '\x00', ''), '', '', '', '', '', '', '', '') == None


from python_code import Ant_Mapper

def test_Ant_Mapper___init__():
    assert Ant_Mapper.__init__(Ant_Mapper('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import Ant_Mkdir

def test_Ant_Mkdir___init__():
    assert Ant_Mkdir.__init__(Ant_Mkdir(''), '') == None


from python_code import Ant_Path
from python_code import Path

def test_Ant_Path___init__():
    assert Ant_Path.__init__(Ant_Path('', '', Ant_Path=Path(), Ant_Path25=set(), Ant_Path27=set()), '', '', Ant_Path=Path(), Ant_Path25=set(), Ant_Path27=set()) == None


from python_code import Ant_PathElement

def test_Ant_PathElement___init__():
    assert Ant_PathElement.__init__(Ant_PathElement('', '\x00'), '\x00\x00', '') == None


from python_code import Ant_PreDefinedTask
from python_code import Ant_Target

def test_Ant_PreDefinedTask___init__():
    assert Ant_PreDefinedTask.__init__(Ant_PreDefinedTask('\x00', '', '', Task=Ant_Target('\x00', '', '', '', Ant_Target=set(), target=set())), '', '', '', Task=Ant_Target('', '', '', '', Ant_Target=set(), target=set())) == None


from python_code import Ant_Project
from python_code import Path
from python_code import Target

def test_Ant_Project___init__():
    assert Ant_Project.__init__(Ant_Project('', '', '', Ant_Project=Target(), Ant_Project2=Path(), Ant_Project4=set(), Ant_Project6=set(), Ant_Project8=set()), '', '', '\x00', Ant_Project=Target(), Ant_Project2=Path(), Ant_Project4=set(), Ant_Project6=set(), Ant_Project8=set()) == None


from python_code import Ant_Project
from python_code import Ant_PropertyEnv
from python_code import Path
from python_code import Target

def test_Ant_PropertyEnv___init__():
    assert Ant_PropertyEnv.__init__(Ant_PropertyEnv('', Property=Ant_Project('', '', '', Ant_Project=Target(), Ant_Project2=Path(), Ant_Project4=set(), Ant_Project6=set(), Ant_Project8=set())), '', Property=Ant_Project('\x00', '', '', Ant_Project=Target(), Ant_Project2=Path(), Ant_Project4=set(), Ant_Project6=set(), Ant_Project8=set())) == None


from python_code import Ant_Project
from python_code import Ant_PropertyFile
from python_code import Path
from python_code import Target

def test_Ant_PropertyFile___init__():
    assert Ant_PropertyFile.__init__(Ant_PropertyFile('', Property=Ant_Project('', '', '', Ant_Project=Target(), Ant_Project2=Path(), Ant_Project4=set(), Ant_Project6=set(), Ant_Project8=set())), '', Property=Ant_Project('\x00', '', '', Ant_Project=Target(), Ant_Project2=Path(), Ant_Project4=set(), Ant_Project6=set(), Ant_Project8=set())) == None


from python_code import Ant_PropertyLocation

def test_Ant_PropertyLocation___init__():
    assert Ant_PropertyLocation.__init__(Ant_PropertyLocation(''), '') == None


from python_code import Ant_Project
from python_code import Ant_PropertyName
from python_code import Path
from python_code import Target

def test_Ant_PropertyName___init__():
    assert Ant_PropertyName.__init__(Ant_PropertyName('', Property=Ant_Project('', '', '', Ant_Project=Target(), Ant_Project2=Path(), Ant_Project4=set(), Ant_Project6=set(), Ant_Project8=set())), '', Property=Ant_Project('\x00', '', '', Ant_Project=Target(), Ant_Project2=Path(), Ant_Project4=set(), Ant_Project6=set(), Ant_Project8=set())) == None


from python_code import Ant_PropertyValue

def test_Ant_PropertyValue___init__():
    assert Ant_PropertyValue.__init__(Ant_PropertyValue(''), '') == None


from python_code import Ant_Target

def test_Ant_Target___init__():
    assert Ant_Target.__init__(Ant_Target('', '', '', '', Ant_Target=set(), target=set()), '', '\x00', '', '', Ant_Target=set(), target=set()) == None


from python_code import Ant_TaskDef

def test_Ant_TaskDef___init__():
    assert Ant_TaskDef.__init__(Ant_TaskDef('', '\x00'), '\x00\x00', '') == None

