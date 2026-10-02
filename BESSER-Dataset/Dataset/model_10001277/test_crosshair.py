from python_code import Answers

def test_Answers___init__():
    assert Answers.__init__(Answers(datetime.date(1, 1, 1), 0.0, '\x00'), datetime.date(1, 1, 1), 0.0, '') == None

from python_code import Choices

def test_Choices___init__():
    assert Choices.__init__(Choices(datetime.date(1, 1, 2)), datetime.date(1, 1, 1)) == None

from python_code import MCRightAnswer

def test_MCRightAnswer___init__():
    assert MCRightAnswer.__init__(MCRightAnswer(0, 0.0), 0, 0.0) == None

from python_code import NumericAnswers

def test_NumericAnswers___init__():
    assert NumericAnswers.__init__(NumericAnswers('', '\x00'), '\x00\x00', '') == None
