from python_code import esm_IEsmLayout

def test_esm_IEsmLayout___init__():
    assert esm_IEsmLayout.__init__(esm_IEsmLayout(''), '') == None


from python_code import esm_DRichText
from python_code import esm_DState
from python_code import esm_IEsmState
from python_code import esm_IEsmStateModel

def test_esm_IEsmState___init__():
    assert esm_IEsmState.__init__(esm_IEsmState('', esm_IEsmState=esm_IEsmStateModel(), esm_IEsmState5=esm_DState(), esm_IEsmState7=esm_DRichText()), '', esm_IEsmState=esm_IEsmStateModel(), esm_IEsmState5=esm_DState(), esm_IEsmState7=esm_DRichText()) == None

