from python_code import ptnetLoLA_ArcToPlaceExt

def test_ptnetLoLA_ArcToPlaceExt___init__():
    assert ptnetLoLA_ArcToPlaceExt.__init__(ptnetLoLA_ArcToPlaceExt(0.0), 0.0) == None


from python_code import ptnetLoLA_ArcToTransitionExt

def test_ptnetLoLA_ArcToTransitionExt___init__():
    assert ptnetLoLA_ArcToTransitionExt.__init__(ptnetLoLA_ArcToTransitionExt(0.0), 0.0) == None


from python_code import ptnetLoLA_Place
from python_code import ptnetLoLA_PlaceReference
from python_code import ptnetLoLA_PtNet

def test_ptnetLoLA_Place___init__():
    assert ptnetLoLA_Place.__init__(ptnetLoLA_Place(0, 0, ptnetLoLA_Place=ptnetLoLA_PtNet(), ptnetLoLA_Place20=ptnetLoLA_PlaceReference()), 0, 0, ptnetLoLA_Place=ptnetLoLA_PtNet(), ptnetLoLA_Place20=ptnetLoLA_PlaceReference()) == None


from python_code import ptnetLoLA_PlaceExt

def test_ptnetLoLA_PlaceExt___init__():
    assert ptnetLoLA_PlaceExt.__init__(ptnetLoLA_PlaceExt(0.0, False), 0.0, False) == None


from python_code import ptnetLoLA_Marking
from python_code import ptnetLoLA_RefMarkedPlace

def test_ptnetLoLA_RefMarkedPlace___init__():
    assert ptnetLoLA_RefMarkedPlace.__init__(ptnetLoLA_RefMarkedPlace(0, ptnetLoLA_RefMarkedPlace=ptnetLoLA_Marking()), 0, ptnetLoLA_RefMarkedPlace=ptnetLoLA_Marking()) == None


from python_code import ptnetLoLA_TransitionExt

def test_ptnetLoLA_TransitionExt___init__():
    assert ptnetLoLA_TransitionExt.__init__(ptnetLoLA_TransitionExt(0.0, 0, 0.0, 0), 0.0, 0, 0.0, 0) == None

