from python_code import model_Game
from python_code import model_Player

def test_model_Player___init__():
    assert model_Player.__init__(model_Player(0, game4=model_Game(), m_hand11=set()), 0, game4=model_Game(), m_hand11=set()) == None


from python_code import rules_BasicHitStrategy

def test_rules_BasicHitStrategy___init__():
    assert rules_BasicHitStrategy.__init__(rules_BasicHitStrategy(0), 0) == None

