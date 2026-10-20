from python_code import kbuild_Assign
from python_code import kbuild_HostProgram
from python_code import kbuild_Variable

def test_kbuild_HostProgram___init__():
    assert kbuild_HostProgram.__init__(kbuild_HostProgram('', kbuild_HostProgram=kbuild_Variable(), kbuild_HostProgram24=kbuild_Assign()), '', kbuild_HostProgram=kbuild_Variable(), kbuild_HostProgram24=kbuild_Assign()) == None


from python_code import kbuild_Ifndef

def test_kbuild_Ifndef___init__():
    assert kbuild_Ifndef.__init__(kbuild_Ifndef(''), '') == None


from python_code import kbuild_MyVariable
from python_code import kbuild_Variable

def test_kbuild_MyVariable___init__():
    assert kbuild_MyVariable.__init__(kbuild_MyVariable('', kbuild_MyVariable=kbuild_Variable()), '', kbuild_MyVariable=kbuild_Variable()) == None


from python_code import kbuild_ObjectShellChar

def test_kbuild_ObjectShellChar___init__():
    assert kbuild_ObjectShellChar.__init__(kbuild_ObjectShellChar(''), '') == None


from python_code import kbuild_ObjectSingleFile

def test_kbuild_ObjectSingleFile___init__():
    assert kbuild_ObjectSingleFile.__init__(kbuild_ObjectSingleFile(''), '') == None


from python_code import kbuild_ObjectVariable
from python_code import kbuild_Variable

def test_kbuild_ObjectVariable___init__():
    assert kbuild_ObjectVariable.__init__(kbuild_ObjectVariable('', kbuild_ObjectVariable=kbuild_Variable()), '', kbuild_ObjectVariable=kbuild_Variable()) == None


from python_code import kbuild_If
from python_code import kbuild_ObjectShellCmd
from python_code import kbuild_ShellCmd
from python_code import kbuild_ShellPart

def test_kbuild_ShellCmd___init__():
    assert kbuild_ShellCmd.__init__(kbuild_ShellCmd('', kbuild_ShellCmd15=set(), kbuild_ShellCmd=kbuild_If(), kbuild_ShellCmd20=kbuild_ShellPart(), kbuild_ShellCmd39=kbuild_ObjectShellCmd()), '', kbuild_ShellCmd15=set(), kbuild_ShellCmd=kbuild_If(), kbuild_ShellCmd20=kbuild_ShellPart(), kbuild_ShellCmd39=kbuild_ObjectShellCmd()) == None


from python_code import kbuild_ShellPart
from python_code import kbuild_VarSlashSym

def test_kbuild_VarSlashSym___init__():
    assert kbuild_VarSlashSym.__init__(kbuild_VarSlashSym('', kbuild_VarSlashSym=kbuild_ShellPart()), '', kbuild_VarSlashSym=kbuild_ShellPart()) == None

