from python_code import library_Book

def test_library_Book___init__():
    assert library_Book.__init__(library_Book(0), 0) == None


from python_code import library_LibraryShelf

def test_library_LibraryShelf___init__():
    assert library_LibraryShelf.__init__(library_LibraryShelf('', library_LibraryShelf=set()), '', library_LibraryShelf=set()) == None


from python_code import library_MultimediaItem

def test_library_MultimediaItem___init__():
    assert library_MultimediaItem.__init__(library_MultimediaItem(0.0), 0.0) == None

