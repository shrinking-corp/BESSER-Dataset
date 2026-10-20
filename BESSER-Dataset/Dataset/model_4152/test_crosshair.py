from python_code import greetings_Greeting
from python_code import greetings_GreetingsModel

def test_greetings_Greeting___init__():
    assert greetings_Greeting.__init__(greetings_Greeting('', greetings_Greeting=greetings_GreetingsModel()), '', greetings_Greeting=greetings_GreetingsModel()) == None

