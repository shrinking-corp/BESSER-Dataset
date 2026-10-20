from python_code import publication2014_Counted

def test_publication2014_Counted___init__():
    assert publication2014_Counted.__init__(publication2014_Counted(0), 0) == None


from python_code import publication2014_Labelled

def test_publication2014_Labelled___init__():
    assert publication2014_Labelled.__init__(publication2014_Labelled(''), '') == None


from python_code import publication2014_Named

def test_publication2014_Named___init__():
    assert publication2014_Named.__init__(publication2014_Named(''), '') == None


from python_code import publication2014_Paper
from python_code import publication2014_Paragraph
from python_code import publication2014_Write

def test_publication2014_Paragraph___init__():
    assert publication2014_Paragraph.__init__(publication2014_Paragraph('\x00', publication2014_Paragraph31=set(), publication2014_Paragraph40=publication2014_Write(), publication2014_Paragraph=publication2014_Paper()), '', publication2014_Paragraph31=set(), publication2014_Paragraph40=publication2014_Write(), publication2014_Paragraph=publication2014_Paper()) == None

