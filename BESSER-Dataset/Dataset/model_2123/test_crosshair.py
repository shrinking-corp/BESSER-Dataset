from python_code import List_SubTestPackage_SubTest
from python_code import SubTestPackage_List_Element

def test_List_SubTestPackage_SubTest___init__():
    assert List_SubTestPackage_SubTest.__init__(List_SubTestPackage_SubTest(0, subTestPointer=SubTestPackage_List_Element()), 0, subTestPointer=SubTestPackage_List_Element()) == None


from python_code import List_TestPackage_Test
from python_code import TestPackage_List_Element

def test_List_TestPackage_Test___init__():
    assert List_TestPackage_Test.__init__(List_TestPackage_Test(0, List_TestPackage_Test18=TestPackage_List_Element(), List_TestPackage_Test=TestPackage_List_Element()), 0, List_TestPackage_Test18=TestPackage_List_Element(), List_TestPackage_Test=TestPackage_List_Element()) == None

