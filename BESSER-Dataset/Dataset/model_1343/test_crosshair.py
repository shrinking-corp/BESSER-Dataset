from python_code import oclinEcoreCST_AnnotationCS
from python_code import oclinEcoreCST_ModelElementCS

def test_oclinEcoreCST_AnnotationCS___init__():
    assert oclinEcoreCST_AnnotationCS.__init__(oclinEcoreCST_AnnotationCS('\x00\x00', '', oclinEcoreCST_AnnotationCS=set(), oclinEcoreCST_AnnotationCS27=oclinEcoreCST_ModelElementCS()), '', '', oclinEcoreCST_AnnotationCS=set(), oclinEcoreCST_AnnotationCS27=oclinEcoreCST_ModelElementCS()) == None


from python_code import oclinEcoreCST_ClassifierCS
from python_code import oclinEcoreCST_ClassifierCSRef
from python_code import oclinEcoreCST_PackageCS

def test_oclinEcoreCST_ClassifierCS___init__():
    assert oclinEcoreCST_ClassifierCS.__init__(oclinEcoreCST_ClassifierCS('', '', oclinEcoreCST_ClassifierCS=set(), oclinEcoreCST_ClassifierCS11=set(), oclinEcoreCST_ClassifierCS13=oclinEcoreCST_ClassifierCSRef(), oclinEcoreCST_ClassifierCS40=oclinEcoreCST_PackageCS()), '', '', oclinEcoreCST_ClassifierCS=set(), oclinEcoreCST_ClassifierCS11=set(), oclinEcoreCST_ClassifierCS13=oclinEcoreCST_ClassifierCSRef(), oclinEcoreCST_ClassifierCS40=oclinEcoreCST_PackageCS()) == None


from python_code import oclinEcoreCST_EnumCS
from python_code import oclinEcoreCST_EnumLiteralCS

def test_oclinEcoreCST_EnumLiteralCS___init__():
    assert oclinEcoreCST_EnumLiteralCS.__init__(oclinEcoreCST_EnumLiteralCS(0, oclinEcoreCST_EnumLiteralCS=oclinEcoreCST_EnumCS()), 0, oclinEcoreCST_EnumLiteralCS=oclinEcoreCST_EnumCS()) == None


from python_code import oclinEcoreCST_DocumentCS
from python_code import oclinEcoreCST_ImportCS

def test_oclinEcoreCST_ImportCS___init__():
    assert oclinEcoreCST_ImportCS.__init__(oclinEcoreCST_ImportCS('', oclinEcoreCST_ImportCS=oclinEcoreCST_DocumentCS()), '', oclinEcoreCST_ImportCS=oclinEcoreCST_DocumentCS()) == None


from python_code import oclinEcoreCST_NamedElementCS

def test_oclinEcoreCST_NamedElementCS___init__():
    assert oclinEcoreCST_NamedElementCS.__init__(oclinEcoreCST_NamedElementCS(''), '') == None


from python_code import oclinEcoreCST_ReferenceCS
from python_code import oclinEcoreCST_ReferenceCSRef
from python_code import oclinEcoreCST_ReferenceRef

def test_oclinEcoreCST_ReferenceCS___init__():
    assert oclinEcoreCST_ReferenceCS.__init__(oclinEcoreCST_ReferenceCS(False, oclinEcoreCST_ReferenceCS=oclinEcoreCST_ReferenceRef(), oclinEcoreCST_ReferenceCS46=set(), oclinEcoreCST_ReferenceCS48=oclinEcoreCST_ReferenceCSRef()), False, oclinEcoreCST_ReferenceCS=oclinEcoreCST_ReferenceRef(), oclinEcoreCST_ReferenceCS46=set(), oclinEcoreCST_ReferenceCS48=oclinEcoreCST_ReferenceCSRef()) == None


from python_code import oclinEcoreCST_ClassifierRef
from python_code import oclinEcoreCST_TypedElementCS

def test_oclinEcoreCST_TypedElementCS___init__():
    assert oclinEcoreCST_TypedElementCS.__init__(oclinEcoreCST_TypedElementCS(0, '\x00', '', 0, oclinEcoreCST_TypedElementCS=oclinEcoreCST_ClassifierRef()), 0, '', '', 0, oclinEcoreCST_TypedElementCS=oclinEcoreCST_ClassifierRef()) == None

