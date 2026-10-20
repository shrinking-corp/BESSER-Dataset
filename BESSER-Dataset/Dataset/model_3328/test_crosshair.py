from python_code import sample_Given
from python_code import sample_Sentence
from python_code import sample_Then
from python_code import sample_When

def test_sample_Sentence___init__():
    assert sample_Sentence.__init__(sample_Sentence('', sample_Sentence11=sample_Given(), sample_Sentence14=sample_Then(), sample_Sentence=sample_When()), '', sample_Sentence11=sample_Given(), sample_Sentence14=sample_Then(), sample_Sentence=sample_When()) == None


from python_code import sample_Story

def test_sample_Story___init__():
    assert sample_Story.__init__(sample_Story('', '', '', '', sample_Story=set()), '', '', '', '', sample_Story=set()) == None

