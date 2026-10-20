from python_code import Commentaires

def test_Commentaires___init__():
    assert Commentaires.__init__(Commentaires(0.0, 0, '', ''), 0.0, 0, '', '') == None


from python_code import Membres

def test_Membres___init__():
    assert Membres.__init__(Membres('', '', '', '', 0, ''), '', '', '', '', 0, '') == None


from python_code import Quizz

def test_Quizz___init__():
    assert Quizz.__init__(Quizz('\x00', 0.0), '', 0.0) == None

