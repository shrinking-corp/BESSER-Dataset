from python_code import libraryModel_ecore_Author
from python_code import libraryModel_ecore_Book
from python_code import libraryModel_ecore_LibraryModel

def test_libraryModel_ecore_LibraryModel___init__():
    assert libraryModel_ecore_LibraryModel.__init__(libraryModel_ecore_LibraryModel(LibraryModel=libraryModel_ecore_Book(), LibraryModel5=libraryModel_ecore_Author(), library=set(), library8=set()), LibraryModel=libraryModel_ecore_Book(), LibraryModel5=libraryModel_ecore_Author(), library=set(), library8=set()) == None

def test_libraryModel_ecore_LibraryModel_printLibrary():
    assert libraryModel_ecore_LibraryModel.printLibrary(libraryModel_ecore_LibraryModel(LibraryModel=libraryModel_ecore_Book(), LibraryModel5=libraryModel_ecore_Author(), library=set(), library8=set())) == None


from python_code import libraryModel_ecore_NamedElement

def test_libraryModel_ecore_NamedElement___init__():
    assert libraryModel_ecore_NamedElement.__init__(libraryModel_ecore_NamedElement(''), '') == None


from python_code import libraryModel_ecore_Book
from python_code import libraryModel_ecore_Picture

def test_libraryModel_ecore_Picture___init__():
    assert libraryModel_ecore_Picture.__init__(libraryModel_ecore_Picture('', Picture=libraryModel_ecore_Book(), pictures=libraryModel_ecore_Book()), '', Picture=libraryModel_ecore_Book(), pictures=libraryModel_ecore_Book()) == None

