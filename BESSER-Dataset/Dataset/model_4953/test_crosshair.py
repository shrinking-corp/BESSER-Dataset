from python_code import webApplication_Named

def test_webApplication_Named___init__():
    assert webApplication_Named.__init__(webApplication_Named(''), '') == None


from python_code import webApplication_content_Field

def test_webApplication_content_Field___init__():
    assert webApplication_content_Field.__init__(webApplication_content_Field(''), '') == None


from python_code import webApplication_content_Menu
from python_code import webApplication_content_Page

def test_webApplication_content_Menu___init__():
    assert webApplication_content_Menu.__init__(webApplication_content_Menu('', '', 0, Content=webApplication_content_Page()), '\x00', '', 0, Content=webApplication_content_Page()) == None


from python_code import webApplication_content_MultipleContent
from python_code import webApplication_content_Page

def test_webApplication_content_MultipleContent___init__():
    assert webApplication_content_MultipleContent.__init__(webApplication_content_MultipleContent(False, 0, Content=webApplication_content_Page()), False, 0, Content=webApplication_content_Page()) == None


from python_code import webApplication_data_Column

def test_webApplication_data_Column___init__():
    assert webApplication_data_Column.__init__(webApplication_data_Column('', 0, False), '\x00', 0, False) == None


from python_code import webApplication_data_Entity

def test_webApplication_data_Entity___init__():
    assert webApplication_data_Entity.__init__(webApplication_data_Entity('', webApplication_data_Entity=set(), webApplication_data_Entity9=set(), webApplication_data_Entity11=set()), '', webApplication_data_Entity=set(), webApplication_data_Entity9=set(), webApplication_data_Entity11=set()) == None

def test_webApplication_data_Entity_getPKRelated():
    assert webApplication_data_Entity.getPKRelated(webApplication_data_Entity('', webApplication_data_Entity=set(), webApplication_data_Entity9=set(), webApplication_data_Entity11=set())) == None

def test_webApplication_data_Entity_getPK():
    assert webApplication_data_Entity.getPK(webApplication_data_Entity('', webApplication_data_Entity=set(), webApplication_data_Entity9=set(), webApplication_data_Entity11=set())) == None

