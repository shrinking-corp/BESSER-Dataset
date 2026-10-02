from python_code import traceability_Category

def test_traceability_Category___init__():
    assert traceability_Category.__init__(traceability_Category('', traceability_Category=set()), '', traceability_Category=set()) == None

from python_code import traceability_DiffCategory

def test_traceability_DiffCategory___init__():
    assert traceability_DiffCategory.__init__(traceability_DiffCategory('', 0, False, traceability_DiffCategory=set()), '', 0, True, traceability_DiffCategory=set()) == None

from python_code import traceability_EObject
from python_code import traceability_TraceDiffs
from python_code import traceability_Traces

def test_traceability_Traces___init__():
    assert traceability_Traces.__init__(traceability_Traces('', '', datetime.date(1, 1, 1), '', '', '', '', traceability_Traces=traceability_EObject(), traceability_Traces19=traceability_EObject(), traceability_Traces22=set(), traceability_Traces32=traceability_TraceDiffs()), '', '', datetime.date(1, 1, 1), '', '', '', '', traceability_Traces=traceability_EObject(), traceability_Traces19=traceability_EObject(), traceability_Traces22=set(), traceability_Traces32=traceability_TraceDiffs()) == None
