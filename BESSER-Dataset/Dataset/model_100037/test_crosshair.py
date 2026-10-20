from python_code import publication2014b_Counted

def test_publication2014b_Counted___init__():
    assert publication2014b_Counted.__init__(publication2014b_Counted(0), 0) == None


from python_code import publication2014b_Labelled

def test_publication2014b_Labelled___init__():
    assert publication2014b_Labelled.__init__(publication2014b_Labelled(''), '') == None


from python_code import publication2014b_Named

def test_publication2014b_Named___init__():
    assert publication2014b_Named.__init__(publication2014b_Named(''), '') == None


from python_code import publication2014b_Paper
from python_code import publication2014b_Paragraph
from python_code import publication2014b_Write

def test_publication2014b_Paragraph___init__():
    assert publication2014b_Paragraph.__init__(publication2014b_Paragraph('\x00', publication2014b_Paragraph=publication2014b_Paper(), publication2014b_Paragraph32=publication2014b_Write(), publication2014b_Paragraph25=set()), '', publication2014b_Paragraph=publication2014b_Paper(), publication2014b_Paragraph32=publication2014b_Write(), publication2014b_Paragraph25=set()) == None

