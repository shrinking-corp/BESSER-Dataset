from python_code import doc_book_Book

def test_doc_book_Book___init__():
    assert doc_book_Book.__init__(doc_book_Book('', '', '', '', doc_book_Book=set(), doc_book_Book11=set()), '', '', '\x00', '', doc_book_Book=set(), doc_book_Book11=set()) == None


from python_code import doc_book_BookContainer

def test_doc_book_BookContainer___init__():
    assert doc_book_BookContainer.__init__(doc_book_BookContainer('', doc_book_BookContainer=set(), doc_book_BookContainer15=set()), '', doc_book_BookContainer=set(), doc_book_BookContainer15=set()) == None


from python_code import doc_book_BookSection

def test_doc_book_BookSection___init__():
    assert doc_book_BookSection.__init__(doc_book_BookSection('\x00\x00', 0, '', ''), '', 0, '', '') == None


from python_code import doc_builder_BookBuilder

def test_doc_builder_BookBuilder___init__():
    assert doc_builder_BookBuilder.__init__(doc_builder_BookBuilder('', '', '\x00', '', doc_builder_BookBuilder=set(), doc_builder_BookBuilder22=set(), doc_builder_BookBuilder19=set()), '', '', '', '', doc_builder_BookBuilder=set(), doc_builder_BookBuilder22=set(), doc_builder_BookBuilder19=set()) == None


from python_code import doc_builder_PropertyEntry

def test_doc_builder_PropertyEntry___init__():
    assert doc_builder_PropertyEntry.__init__(doc_builder_PropertyEntry('', '\x00'), '\x00\x00', '') == None


from python_code import doc_fragment_Author

def test_doc_fragment_Author___init__():
    assert doc_fragment_Author.__init__(doc_fragment_Author('', '', '\x00\x00'), '', '', '') == None


from python_code import doc_fragment_Container

def test_doc_fragment_Container___init__():
    assert doc_fragment_Container.__init__(doc_fragment_Container('', doc_fragment_Container=set(), doc_fragment_Container6=set()), '', doc_fragment_Container=set(), doc_fragment_Container6=set()) == None


from python_code import doc_fragment_Copyright

def test_doc_fragment_Copyright___init__():
    assert doc_fragment_Copyright.__init__(doc_fragment_Copyright(0, doc_fragment_Copyright=set()), 0, doc_fragment_Copyright=set()) == None


from python_code import doc_book_BookContainer
from python_code import doc_fragment_Container
from python_code import doc_fragment_PlainTextContent

def test_doc_fragment_PlainTextContent___init__():
    assert doc_fragment_PlainTextContent.__init__(doc_fragment_PlainTextContent('', Content=doc_fragment_Container('', doc_fragment_Container=set(), doc_fragment_Container6=set()), Content13=doc_book_BookContainer('', doc_book_BookContainer=set(), doc_book_BookContainer15=set())), '', Content=doc_fragment_Container('', doc_fragment_Container=set(), doc_fragment_Container6=set()), Content13=doc_book_BookContainer('', doc_book_BookContainer=set(), doc_book_BookContainer15=set())) == None


from python_code import doc_fragment_Section

def test_doc_fragment_Section___init__():
    assert doc_fragment_Section.__init__(doc_fragment_Section(''), '') == None


from python_code import doc_map_ExcludePatternRule

def test_doc_map_ExcludePatternRule___init__():
    assert doc_map_ExcludePatternRule.__init__(doc_map_ExcludePatternRule()) == None

def test_doc_map_ExcludePatternRule_checkRule():
    assert doc_map_ExcludePatternRule.checkRule(doc_map_ExcludePatternRule(), '') == None


from python_code import ResourceFactory
from python_code import doc_map_ExtensionMappingEntry

def test_doc_map_ExtensionMappingEntry___init__():
    assert doc_map_ExtensionMappingEntry.__init__(doc_map_ExtensionMappingEntry('', doc_map_ExtensionMappingEntry=ResourceFactory()), '', doc_map_ExtensionMappingEntry=ResourceFactory()) == None


from python_code import doc_map_Feature

def test_doc_map_Feature___init__():
    assert doc_map_Feature.__init__(doc_map_Feature('\x00\x00', False, doc_map_Feature=set()), '', True, doc_map_Feature=set()) == None


from python_code import doc_map_File

def test_doc_map_File___init__():
    assert doc_map_File.__init__(doc_map_File(''), '') == None


from python_code import doc_map_IncludePatternRule

def test_doc_map_IncludePatternRule___init__():
    assert doc_map_IncludePatternRule.__init__(doc_map_IncludePatternRule()) == None

def test_doc_map_IncludePatternRule_checkRule():
    assert doc_map_IncludePatternRule.checkRule(doc_map_IncludePatternRule(), '') == None


from python_code import doc_map_Map

def test_doc_map_Map___init__():
    assert doc_map_Map.__init__(doc_map_Map(doc_map_Map=set()), doc_map_Map=set()) == None

def test_doc_map_Map_visit():
    assert doc_map_Map.visit(doc_map_Map(doc_map_Map=set()), 0) == None


from python_code import doc_map_MapContainer

def test_doc_map_MapContainer___init__():
    assert doc_map_MapContainer.__init__(doc_map_MapContainer('', doc_map_MapContainer=set()), '', doc_map_MapContainer=set()) == None


from python_code import doc_map_MapElement

def test_doc_map_MapElement___init__():
    assert doc_map_MapElement.__init__(doc_map_MapElement()) == None

def test_doc_map_MapElement_visit():
    assert doc_map_MapElement.visit(doc_map_MapElement(), '') == None


from python_code import doc_map_MapSection

def test_doc_map_MapSection___init__():
    assert doc_map_MapSection.__init__(doc_map_MapSection('', '\x00'), '\x00\x00', '') == None


from python_code import doc_map_NameRule

def test_doc_map_NameRule___init__():
    assert doc_map_NameRule.__init__(doc_map_NameRule()) == None

def test_doc_map_NameRule_checkRule():
    assert doc_map_NameRule.checkRule(doc_map_NameRule(), '') == None


from python_code import doc_map_Feature
from python_code import doc_map_PatternRule

def test_doc_map_PatternRule___init__():
    assert doc_map_PatternRule.__init__(doc_map_PatternRule('', NameRule=doc_map_Feature('', True, doc_map_Feature=set())), '', NameRule=doc_map_Feature('', False, doc_map_Feature=set())) == None


from python_code import doc_map_ResourceFactory

def test_doc_map_ResourceFactory___init__():
    assert doc_map_ResourceFactory.__init__(doc_map_ResourceFactory(''), '') == None

