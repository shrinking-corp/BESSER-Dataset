from python_code import rqsDsl_RAnnotation

def test_rqsDsl_RAnnotation___init__():
    assert rqsDsl_RAnnotation.__init__(rqsDsl_RAnnotation(0, 0, '', 0, 0, 0, 0), 0, 0, '', 0, 0, 0, 0) == None


from python_code import rqsDsl_Model
from python_code import rqsDsl_Requirement

def test_rqsDsl_Requirement___init__():
    assert rqsDsl_Requirement.__init__(rqsDsl_Requirement('', rqsDsl_Requirement=rqsDsl_Model()), '', rqsDsl_Requirement=rqsDsl_Model()) == None


from python_code import rqsDsl_TAnnotation

def test_rqsDsl_TAnnotation___init__():
    assert rqsDsl_TAnnotation.__init__(rqsDsl_TAnnotation('', 0, 0, '', 0, 0), '', 0, 0, '', 0, 0) == None

