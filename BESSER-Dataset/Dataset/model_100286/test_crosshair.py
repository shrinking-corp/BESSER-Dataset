from python_code import pETRI_PetriNet

def test_pETRI_PetriNet___init__():
    assert pETRI_PetriNet.__init__(pETRI_PetriNet('', pETRI_PetriNet=set()), '', pETRI_PetriNet=set()) == None


from python_code import pETRI_Place

def test_pETRI_Place___init__():
    assert pETRI_Place.__init__(pETRI_Place(0), 0) == None

