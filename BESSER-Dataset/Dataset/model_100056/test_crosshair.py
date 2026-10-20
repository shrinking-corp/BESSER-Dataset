from python_code import revision_Counted

def test_revision_Counted___init__():
    assert revision_Counted.__init__(revision_Counted(0), 0) == None


from python_code import revision_Labelled

def test_revision_Labelled___init__():
    assert revision_Labelled.__init__(revision_Labelled(''), '') == None


from python_code import revision_Named

def test_revision_Named___init__():
    assert revision_Named.__init__(revision_Named(''), '') == None


from python_code import revision_Paper
from python_code import revision_Paragraph
from python_code import revision_Write

def test_revision_Paragraph___init__():
    assert revision_Paragraph.__init__(revision_Paragraph('\x00', revision_Paragraph=revision_Paper(), revision_Paragraph31=set(), revision_Paragraph40=revision_Write()), '', revision_Paragraph=revision_Paper(), revision_Paragraph31=set(), revision_Paragraph40=revision_Write()) == None

