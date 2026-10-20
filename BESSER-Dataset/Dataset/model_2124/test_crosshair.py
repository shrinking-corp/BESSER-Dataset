from python_code import tests_TestCategoryAllProperty
from python_code import tests_TestCategoryComposition
from python_code import tests_TestCategoryCompositionArray
from python_code import tests_TestCategoryReference
from python_code import tests_TestCategoryReferenceArray

def test_tests_TestCategoryAllProperty___init__():
    assert tests_TestCategoryAllProperty.__init__(tests_TestCategoryAllProperty('', 0, 0.0, False, '', '', tests_TestCategoryAllProperty=tests_TestCategoryComposition(), tests_TestCategoryAllProperty2=tests_TestCategoryReference(), tests_TestCategoryAllProperty4=tests_TestCategoryCompositionArray(), tests_TestCategoryAllProperty7=tests_TestCategoryCompositionArray(), tests_TestCategoryAllProperty9=tests_TestCategoryReferenceArray(), tests_TestCategoryAllProperty12=tests_TestCategoryReferenceArray()), '', 0, 0.0, True, '', '', tests_TestCategoryAllProperty=tests_TestCategoryComposition(), tests_TestCategoryAllProperty2=tests_TestCategoryReference(), tests_TestCategoryAllProperty4=tests_TestCategoryCompositionArray(), tests_TestCategoryAllProperty7=tests_TestCategoryCompositionArray(), tests_TestCategoryAllProperty9=tests_TestCategoryReferenceArray(), tests_TestCategoryAllProperty12=tests_TestCategoryReferenceArray()) == None


from python_code import tests_TestCategoryExtends

def test_tests_TestCategoryExtends___init__():
    assert tests_TestCategoryExtends.__init__(tests_TestCategoryExtends(0), 0) == None


from python_code import tests_TestCategoryIntrinsicArray

def test_tests_TestCategoryIntrinsicArray___init__():
    assert tests_TestCategoryIntrinsicArray.__init__(tests_TestCategoryIntrinsicArray('', '\x00'), '\x00\x00', '') == None


from python_code import tests_TestCrossLinkedParametersWithCalculation

def test_tests_TestCrossLinkedParametersWithCalculation___init__():
    assert tests_TestCrossLinkedParametersWithCalculation.__init__(tests_TestCrossLinkedParametersWithCalculation(0.0), 0.0) == None


from python_code import tests_TestMassParameters
from python_code import tests_TestParameter

def test_tests_TestParameter___init__():
    assert tests_TestParameter.__init__(tests_TestParameter(0.0, tests_TestParameter=tests_TestMassParameters()), 0.0, tests_TestParameter=tests_TestMassParameters()) == None

