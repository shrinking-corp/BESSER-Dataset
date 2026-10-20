from python_code import railway_RailwayElement

def test_railway_RailwayElement___init__():
    assert railway_RailwayElement.__init__(railway_RailwayElement(0), 0) == None


from python_code import railway_Segment

def test_railway_Segment___init__():
    assert railway_Segment.__init__(railway_Segment(0, railway_Segment=set(), railway_Segment2=set()), 0, railway_Segment=set(), railway_Segment2=set()) == None

