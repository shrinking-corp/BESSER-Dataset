from python_code import Ant_Attribut
from python_code import Ant_NewTask

def test_Ant_Attribut___init__():
    assert Ant_Attribut.__init__(Ant_Attribut('', '\x00', Ant_Attribut=Ant_NewTask()), '\x00\x00', '', Ant_Attribut=Ant_NewTask()) == None


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


from python_code import Ant_FormatTstamp
from python_code import Ant_Tstamp

def test_Ant_FormatTstamp___init__():
    assert Ant_FormatTstamp.__init__(Ant_FormatTstamp('', '', '', '', '', Ant_FormatTstamp=Ant_Tstamp()), '', '', '', '', '', Ant_FormatTstamp=Ant_Tstamp()) == None


from python_code import Ant_Jar

def test_Ant_Jar___init__():
    assert Ant_Jar.__init__(Ant_Jar('', '', '', '', ''), '', '', '', '', '') == None


from python_code import Ant_Javadoc

def test_Ant_Javadoc___init__():
    assert Ant_Javadoc.__init__(Ant_Javadoc('', '', '', '', '', '', '\x00', ''), '', '', '', '', '', '', '', '') == None


from python_code import Ant_Mkdir

def test_Ant_Mkdir___init__():
    assert Ant_Mkdir.__init__(Ant_Mkdir(''), '') == None


from python_code import Ant_PreDefinedTask

def test_Ant_PreDefinedTask___init__():
    assert Ant_PreDefinedTask.__init__(Ant_PreDefinedTask('', '', '\x00\x00'), '', '', '') == None


from python_code import Ant_PropertyEnv

def test_Ant_PropertyEnv___init__():
    assert Ant_PropertyEnv.__init__(Ant_PropertyEnv(''), '') == None


from python_code import Ant_PropertyFile

def test_Ant_PropertyFile___init__():
    assert Ant_PropertyFile.__init__(Ant_PropertyFile(''), '') == None


from python_code import Ant_PropertyLocation

def test_Ant_PropertyLocation___init__():
    assert Ant_PropertyLocation.__init__(Ant_PropertyLocation(''), '') == None


from python_code import Ant_PropertyName

def test_Ant_PropertyName___init__():
    assert Ant_PropertyName.__init__(Ant_PropertyName(''), '') == None


from python_code import Ant_PropertyValue

def test_Ant_PropertyValue___init__():
    assert Ant_PropertyValue.__init__(Ant_PropertyValue(''), '') == None

