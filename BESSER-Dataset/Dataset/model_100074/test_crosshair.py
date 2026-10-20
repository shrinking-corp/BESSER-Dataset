from python_code import AntScripts_Attribute

def test_AntScripts_Attribute___init__():
    assert AntScripts_Attribute.__init__(AntScripts_Attribute(''), '') == None


from python_code import AntScripts_CommentableElement

def test_AntScripts_CommentableElement___init__():
    assert AntScripts_CommentableElement.__init__(AntScripts_CommentableElement(''), '') == None


from python_code import AntScripts_DescribableElement

def test_AntScripts_DescribableElement___init__():
    assert AntScripts_DescribableElement.__init__(AntScripts_DescribableElement(''), '') == None


from python_code import AntScripts_NamedElement

def test_AntScripts_NamedElement___init__():
    assert AntScripts_NamedElement.__init__(AntScripts_NamedElement(''), '') == None


from python_code import AntScripts_Property

def test_AntScripts_Property___init__():
    assert AntScripts_Property.__init__(AntScripts_Property('\x00', '', '', '', '', '', '', '', '', '', '\x00'), '', '', '', '', '', '', '', '', '', '', '') == None


from python_code import AntScripts_Target

def test_AntScripts_Target___init__():
    assert AntScripts_Target.__init__(AntScripts_Target('', '', AntScripts_Target=set(), AntScripts_Target8=set()), '', '', AntScripts_Target=set(), AntScripts_Target8=set()) == None

