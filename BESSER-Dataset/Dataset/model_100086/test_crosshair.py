from python_code import MavenMaven_AntPropertyEnv
from python_code import MavenMaven_Project

def test_MavenMaven_AntPropertyEnv___init__():
    assert MavenMaven_AntPropertyEnv.__init__(MavenMaven_AntPropertyEnv('', AntProperty=MavenMaven_Project()), '', AntProperty=MavenMaven_Project()) == None


from python_code import MavenMaven_AntPropertyFile
from python_code import MavenMaven_Project

def test_MavenMaven_AntPropertyFile___init__():
    assert MavenMaven_AntPropertyFile.__init__(MavenMaven_AntPropertyFile('', AntProperty=MavenMaven_Project()), '', AntProperty=MavenMaven_Project()) == None


from python_code import MavenMaven_AntPropertyLocation

def test_MavenMaven_AntPropertyLocation___init__():
    assert MavenMaven_AntPropertyLocation.__init__(MavenMaven_AntPropertyLocation(''), '') == None


from python_code import MavenMaven_AntPropertyName
from python_code import MavenMaven_Project

def test_MavenMaven_AntPropertyName___init__():
    assert MavenMaven_AntPropertyName.__init__(MavenMaven_AntPropertyName('', AntProperty=MavenMaven_Project()), '', AntProperty=MavenMaven_Project()) == None


from python_code import MavenMaven_AntPropertyValue

def test_MavenMaven_AntPropertyValue___init__():
    assert MavenMaven_AntPropertyValue.__init__(MavenMaven_AntPropertyValue(''), '') == None


from python_code import ContentsGoal
from python_code import MavenMaven_AbstractGoal
from python_code import MavenMaven_AntTaskDef
from python_code import MavenMaven_JellyForEach

def test_MavenMaven_AntTaskDef___init__():
    assert MavenMaven_AntTaskDef.__init__(MavenMaven_AntTaskDef('', '', ContentsGoal=MavenMaven_JellyForEach('', '', '', MavenMaven_JellyForEach=ContentsGoal()), ContentsGoal16=MavenMaven_AbstractGoal()), '', '', ContentsGoal=MavenMaven_JellyForEach('', '', '', MavenMaven_JellyForEach=ContentsGoal()), ContentsGoal16=MavenMaven_AbstractGoal()) == None


from python_code import MavenMaven_Attribut

def test_MavenMaven_Attribut___init__():
    assert MavenMaven_Attribut.__init__(MavenMaven_Attribut('', '\x00'), '\x00\x00', '') == None


from python_code import MavenMaven_ClassPath

def test_MavenMaven_ClassPath___init__():
    assert MavenMaven_ClassPath.__init__(MavenMaven_ClassPath('', MavenMaven_ClassPath=set(), MavenMaven_ClassPath44=set()), '', MavenMaven_ClassPath=set(), MavenMaven_ClassPath44=set()) == None


from python_code import FileSet
from python_code import FilterSet
from python_code import Mapper
from python_code import MavenMaven_Copy

def test_MavenMaven_Copy___init__():
    assert MavenMaven_Copy.__init__(MavenMaven_Copy('', '', '', '', '', '', '\x00', '', MavenMaven_Copy=FileSet(), MavenMaven_Copy60=FilterSet(), MavenMaven_Copy62=Mapper()), '', '', '', '', '', '', '', '', MavenMaven_Copy=FileSet(), MavenMaven_Copy60=FilterSet(), MavenMaven_Copy62=Mapper()) == None


from python_code import MavenMaven_Delete

def test_MavenMaven_Delete___init__():
    assert MavenMaven_Delete.__init__(MavenMaven_Delete('\x00', '', '', '', '', '', '', '', '', '', '\x00'), '', '', '', '', '', '', '', '', '', '', '') == None


from python_code import MavenMaven_Echo

def test_MavenMaven_Echo___init__():
    assert MavenMaven_Echo.__init__(MavenMaven_Echo('', '', '\x00\x00'), '', '', '') == None


from python_code import MavenMaven_Exec

def test_MavenMaven_Exec___init__():
    assert MavenMaven_Exec.__init__(MavenMaven_Exec('', '\x00'), '\x00\x00', '') == None


from python_code import MavenMaven_FileList

def test_MavenMaven_FileList___init__():
    assert MavenMaven_FileList.__init__(MavenMaven_FileList('', '\x00'), '\x00\x00', '') == None


from python_code import MavenMaven_FileSet

def test_MavenMaven_FileSet___init__():
    assert MavenMaven_FileSet.__init__(MavenMaven_FileSet('', MavenMaven_FileSet=set(), MavenMaven_FileSet29=set(), MavenMaven_FileSet31=set()), '', MavenMaven_FileSet=set(), MavenMaven_FileSet29=set(), MavenMaven_FileSet31=set()) == None


from python_code import MavenMaven_Filter

def test_MavenMaven_Filter___init__():
    assert MavenMaven_Filter.__init__(MavenMaven_Filter('', '\x00'), '\x00\x00', '') == None


from python_code import MavenMaven_FilterSet

def test_MavenMaven_FilterSet___init__():
    assert MavenMaven_FilterSet.__init__(MavenMaven_FilterSet('', '', MavenMaven_FilterSet34=set(), MavenMaven_FilterSet=set()), '', '', MavenMaven_FilterSet34=set(), MavenMaven_FilterSet=set()) == None


from python_code import MavenMaven_FiltersFile

def test_MavenMaven_FiltersFile___init__():
    assert MavenMaven_FiltersFile.__init__(MavenMaven_FiltersFile(''), '') == None


from python_code import MavenMaven_Goal
from python_code import PostGoal
from python_code import PreGoal

def test_MavenMaven_Goal___init__():
    assert MavenMaven_Goal.__init__(MavenMaven_Goal('', centralGoal=PreGoal(), centralGoal25=PostGoal()), '', centralGoal=PreGoal(), centralGoal25=PostGoal()) == None


from python_code import MavenMaven_InExcludes

def test_MavenMaven_InExcludes___init__():
    assert MavenMaven_InExcludes.__init__(MavenMaven_InExcludes('', '', '\x00\x00'), '', '', '') == None


from python_code import MavenMaven_Jar

def test_MavenMaven_Jar___init__():
    assert MavenMaven_Jar.__init__(MavenMaven_Jar('', '', '', '', ''), '', '', '', '', '') == None


from python_code import ClassPath
from python_code import MavenMaven_Java

def test_MavenMaven_Java___init__():
    assert MavenMaven_Java.__init__(MavenMaven_Java('', '', '\x00\x00', MavenMaven_Java=ClassPath()), '', '', '', MavenMaven_Java=ClassPath()) == None


from python_code import ClassPath
from python_code import MavenMaven_Javac

def test_MavenMaven_Javac___init__():
    assert MavenMaven_Javac.__init__(MavenMaven_Javac('', '', '', '', '', '', MavenMaven_Javac=set(), MavenMaven_Javac55=ClassPath()), '', '', '', '', '', '', MavenMaven_Javac=set(), MavenMaven_Javac55=ClassPath()) == None


from python_code import MavenMaven_Javadoc

def test_MavenMaven_Javadoc___init__():
    assert MavenMaven_Javadoc.__init__(MavenMaven_Javadoc('', '', '', '', '', '', '\x00', ''), '', '', '', '', '', '', '', '') == None


from python_code import ContentsGoal
from python_code import MavenMaven_JellyForEach

def test_MavenMaven_JellyForEach___init__():
    assert MavenMaven_JellyForEach.__init__(MavenMaven_JellyForEach('', '', '', MavenMaven_JellyForEach=ContentsGoal()), '', '', '', MavenMaven_JellyForEach=ContentsGoal()) == None


from python_code import MavenMaven_JellySet

def test_MavenMaven_JellySet___init__():
    assert MavenMaven_JellySet.__init__(MavenMaven_JellySet('', '\x00'), '\x00\x00', '') == None


from python_code import MavenMaven_Mapper

def test_MavenMaven_Mapper___init__():
    assert MavenMaven_Mapper.__init__(MavenMaven_Mapper('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import MavenMaven_Mkdir

def test_MavenMaven_Mkdir___init__():
    assert MavenMaven_Mkdir.__init__(MavenMaven_Mkdir(''), '') == None


from python_code import MavenMaven_Path
from python_code import Path

def test_MavenMaven_Path___init__():
    assert MavenMaven_Path.__init__(MavenMaven_Path('', '', MavenMaven_Path=Path(), MavenMaven_Path38=set(), MavenMaven_Path40=set()), '', '', MavenMaven_Path=Path(), MavenMaven_Path38=set(), MavenMaven_Path40=set()) == None


from python_code import MavenMaven_PathElement

def test_MavenMaven_PathElement___init__():
    assert MavenMaven_PathElement.__init__(MavenMaven_PathElement('', '\x00'), '\x00\x00', '') == None


from python_code import MavenMaven_PreDefinedTask

def test_MavenMaven_PreDefinedTask___init__():
    assert MavenMaven_PreDefinedTask.__init__(MavenMaven_PreDefinedTask('', '', '\x00\x00'), '', '', '') == None


from python_code import MavenMaven_Xmlns

def test_MavenMaven_Xmlns___init__():
    assert MavenMaven_Xmlns.__init__(MavenMaven_Xmlns('', '\x00'), '\x00\x00', '') == None

