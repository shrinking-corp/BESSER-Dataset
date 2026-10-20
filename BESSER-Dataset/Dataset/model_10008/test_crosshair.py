from python_code import game_Action
from python_code import game_Choix
from python_code import game_Condition
from python_code import game_Description
from python_code import game_Interaction

def test_game_Choix___init__():
    assert game_Choix.__init__(game_Choix('', game_Choix93=game_Interaction(), game_Choix96=game_Interaction(), game_Choix98=game_Description(), game_Choix101=game_Condition(), game_Choix=game_Action(), game_Choix87=game_Interaction(), game_Choix104=set()), '', game_Choix93=game_Interaction(), game_Choix96=game_Interaction(), game_Choix98=game_Description(), game_Choix101=game_Condition(), game_Choix=game_Action(), game_Choix87=game_Interaction(), game_Choix104=set()) == None


from python_code import game_EntiteLieu
from python_code import game_Interaction
from python_code import game_Personne

def test_game_Personne___init__():
    assert game_Personne.__init__(game_Personne('', game_Personne20=game_Interaction(), game_Personne=game_EntiteLieu()), '', game_Personne20=game_Interaction(), game_Personne=game_EntiteLieu()) == None


from python_code import game_Condition
from python_code import game_Description
from python_code import game_Texte

def test_game_Texte___init__():
    assert game_Texte.__init__(game_Texte('', game_Texte=game_Description(), game_Texte58=game_Condition()), '', game_Texte=game_Description(), game_Texte58=game_Condition()) == None

