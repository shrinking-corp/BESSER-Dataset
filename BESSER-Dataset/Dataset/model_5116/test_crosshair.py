from python_code import benchmark_NamedElement

def test_benchmark_NamedElement___init__():
    assert benchmark_NamedElement.__init__(benchmark_NamedElement('', benchmark_NamedElement=set()), '', benchmark_NamedElement=set()) == None


from python_code import benchmark_TestCase
from python_code import benchmark_TimeResult
from python_code import benchmark_Variant

def test_benchmark_TimeResult___init__():
    assert benchmark_TimeResult.__init__(benchmark_TimeResult('\x00\x00', '', benchmark_TimeResult=benchmark_TestCase(), results=benchmark_Variant(), benchmark_TimeResult12=set(), TimeResult=benchmark_Variant()), '', '', benchmark_TimeResult=benchmark_TestCase(), results=benchmark_Variant(), benchmark_TimeResult12=set(), TimeResult=benchmark_Variant()) == None

