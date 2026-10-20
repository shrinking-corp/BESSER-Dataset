from python_code import publication2014a_Counted

def test_publication2014a_Counted___init__():
    assert publication2014a_Counted.__init__(publication2014a_Counted(0), 0) == None


from python_code import publication2014a_Labelled

def test_publication2014a_Labelled___init__():
    assert publication2014a_Labelled.__init__(publication2014a_Labelled(''), '') == None


from python_code import publication2014a_Named

def test_publication2014a_Named___init__():
    assert publication2014a_Named.__init__(publication2014a_Named(''), '') == None


from python_code import publication2014a_Paper
from python_code import publication2014a_Paragraph
from python_code import publication2014a_Write

def test_publication2014a_Paragraph___init__():
    assert publication2014a_Paragraph.__init__(publication2014a_Paragraph('\x00', publication2014a_Paragraph25=set(), publication2014a_Paragraph32=publication2014a_Write(), publication2014a_Paragraph=publication2014a_Paper()), '', publication2014a_Paragraph25=set(), publication2014a_Paragraph32=publication2014a_Write(), publication2014a_Paragraph=publication2014a_Paper()) == None

