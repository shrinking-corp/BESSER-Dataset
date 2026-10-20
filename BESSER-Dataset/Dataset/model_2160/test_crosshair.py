from python_code import list_VersionedList
from python_code import list_VersionedListEdge
from python_code import list_VersionedListStartReference
from python_code import list_VersionedListVertex

def test_list_VersionedList___init__():
    assert list_VersionedList.__init__(list_VersionedList(list=set(), list2=set(), list4=set(), VersionedList22=list_VersionedListStartReference(), VersionedList=list_VersionedListVertex(), VersionedList18=list_VersionedListEdge()), list=set(), list2=set(), list4=set(), VersionedList22=list_VersionedListStartReference(), VersionedList=list_VersionedListVertex(), VersionedList18=list_VersionedListEdge()) == None

def test_list_VersionedList_getAllOccurrencesOf():
    assert list_VersionedList.getAllOccurrencesOf(list_VersionedList(list=set(), list2=set(), list4=set(), VersionedList22=list_VersionedListStartReference(), VersionedList=list_VersionedListVertex(), VersionedList18=list_VersionedListEdge()), '\x00') == None

def test_list_VersionedList_getEdge():
    assert list_VersionedList.getEdge(list_VersionedList(list=set(), list2=set(), list4=set(), VersionedList22=list_VersionedListStartReference(), VersionedList=list_VersionedListVertex(), VersionedList18=list_VersionedListEdge()), '\x00', '') == None

def test_list_VersionedList_linearize():
    assert list_VersionedList.linearize(list_VersionedList(list=set(), list2=set(), list4=set(), VersionedList22=list_VersionedListStartReference(), VersionedList=list_VersionedListVertex(), VersionedList18=list_VersionedListEdge())) == None

