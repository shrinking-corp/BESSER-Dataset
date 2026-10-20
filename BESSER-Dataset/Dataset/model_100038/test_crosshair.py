from python_code import publication2014c_Counted

def test_publication2014c_Counted___init__():
    assert publication2014c_Counted.__init__(publication2014c_Counted(0), 0) == None


from python_code import publication2014c_Labelled

def test_publication2014c_Labelled___init__():
    assert publication2014c_Labelled.__init__(publication2014c_Labelled(''), '') == None


from python_code import publication2014c_Named

def test_publication2014c_Named___init__():
    assert publication2014c_Named.__init__(publication2014c_Named(''), '') == None


from python_code import publication2014c_Paper
from python_code import publication2014c_Paragraph
from python_code import publication2014c_Write

def test_publication2014c_Paragraph___init__():
    assert publication2014c_Paragraph.__init__(publication2014c_Paragraph('\x00', publication2014c_Paragraph32=publication2014c_Write(), publication2014c_Paragraph=publication2014c_Paper(), publication2014c_Paragraph25=set()), '', publication2014c_Paragraph32=publication2014c_Write(), publication2014c_Paragraph=publication2014c_Paper(), publication2014c_Paragraph25=set()) == None

