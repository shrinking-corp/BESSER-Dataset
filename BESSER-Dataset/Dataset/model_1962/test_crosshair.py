from python_code import sourceanalysator_Article
from python_code import sourceanalysator_Library
from python_code import sourceanalysator_Source

def test_sourceanalysator_Article___init__():
    assert sourceanalysator_Article.__init__(sourceanalysator_Article('\x00\x00', '', Article=sourceanalysator_Source(), sourceanalysator_Article=sourceanalysator_Library(), article=set()), '', '', Article=sourceanalysator_Source(), sourceanalysator_Article=sourceanalysator_Library(), article=set()) == None


from python_code import sourceanalysator_GeneralSource
from python_code import sourceanalysator_Library
from python_code import sourceanalysator_Source

def test_sourceanalysator_GeneralSource___init__():
    assert sourceanalysator_GeneralSource.__init__(sourceanalysator_GeneralSource('', '', False, generalSource=set(), GeneralSource=sourceanalysator_Source(), sourceanalysator_GeneralSource=sourceanalysator_Library()), '', '', True, generalSource=set(), GeneralSource=sourceanalysator_Source(), sourceanalysator_GeneralSource=sourceanalysator_Library()) == None


from python_code import sourceanalysator_Hyperlink
from python_code import sourceanalysator_Library
from python_code import sourceanalysator_Source

def test_sourceanalysator_Hyperlink___init__():
    assert sourceanalysator_Hyperlink.__init__(sourceanalysator_Hyperlink('', sourceanalysator_Hyperlink=sourceanalysator_Library(), Hyperlink=sourceanalysator_Source(), hyperlink=set()), '', sourceanalysator_Hyperlink=sourceanalysator_Library(), Hyperlink=sourceanalysator_Source(), hyperlink=set()) == None

