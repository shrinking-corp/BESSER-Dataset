from python_code import beans_Bean
from python_code import beans_BeanLibrary

def test_beans_BeanLibrary___init__():
    assert beans_BeanLibrary.__init__(beans_BeanLibrary('', beanLibrary=set(), BeanLibrary=beans_Bean()), '', beanLibrary=set(), BeanLibrary=beans_Bean()) == None


from python_code import beans_Bean
from python_code import beans_BeanProperty

def test_beans_BeanProperty___init__():
    assert beans_BeanProperty.__init__(beans_BeanProperty('', False, BeanProperty=beans_Bean(), properties=beans_Bean()), '', False, BeanProperty=beans_Bean(), properties=beans_Bean()) == None


from python_code import beans_NamedElement

def test_beans_NamedElement___init__():
    assert beans_NamedElement.__init__(beans_NamedElement(''), '') == None

