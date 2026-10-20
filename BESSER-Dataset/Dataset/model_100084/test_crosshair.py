from python_code import maven_MapEntry
from python_code import maven_Mappings

def test_maven_MapEntry___init__():
    assert maven_MapEntry.__init__(maven_MapEntry('', maven_MapEntry=set(), maven_MapEntry2=maven_Mappings()), '', maven_MapEntry=set(), maven_MapEntry2=maven_Mappings()) == None


from python_code import maven_Mappings
from python_code import maven_MavenProvider
from python_code import maven_Scopes

def test_maven_MavenProvider___init__():
    assert maven_MavenProvider.__init__(maven_MavenProvider(True, maven_MavenProvider=maven_Mappings(), maven_MavenProvider8=maven_Scopes()), False, maven_MavenProvider=maven_Mappings(), maven_MavenProvider8=maven_Scopes()) == None

def test_maven_MavenProvider_getComponentName():
    assert maven_MavenProvider.getComponentName(maven_MavenProvider(False, maven_MavenProvider=maven_Mappings(), maven_MavenProvider8=maven_Scopes()), 0, '\x00\x00') == None

def test_maven_MavenProvider_getMapEntry():
    assert maven_MavenProvider.getMapEntry(maven_MavenProvider(False, maven_MavenProvider=maven_Mappings(), maven_MavenProvider8=maven_Scopes()), 0) == None


from python_code import maven_Scope
from python_code import maven_Scopes

def test_maven_Scope___init__():
    assert maven_Scope.__init__(maven_Scope('', False, maven_Scope=maven_Scopes()), '', False, maven_Scope=maven_Scopes()) == None

