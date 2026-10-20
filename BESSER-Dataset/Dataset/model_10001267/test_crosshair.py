from python_code import dutycalls_contoller_Dealer_Control

def test_dutycalls_contoller_Dealer_Control___init__():
    assert dutycalls_contoller_Dealer_Control.__init__(dutycalls_contoller_Dealer_Control(0, 0), 0, 0) == None


from python_code import dutycalls_model_BestHand

def test_dutycalls_model_BestHand___init__():
    assert dutycalls_model_BestHand.__init__(dutycalls_model_BestHand(0), 0) == None


from python_code import dutycalls_model_User_S

def test_dutycalls_model_User_S___init__():
    assert dutycalls_model_User_S.__init__(dutycalls_model_User_S(0), 0) == None


from python_code import dutycalls_view_Instructions
from python_code import dutycalls_view_PokerTable

def test_dutycalls_view_Instructions___init__():
    assert dutycalls_view_Instructions.__init__(dutycalls_view_Instructions(dutycalls_view_PokerTable()), dutycalls_view_PokerTable()) == None

