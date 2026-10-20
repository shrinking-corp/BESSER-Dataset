from python_code import Graphql_Enum
from python_code import Graphql_EnumValue

def test_Graphql_EnumValue___init__():
    assert Graphql_EnumValue.__init__(Graphql_EnumValue('', '\x00', Graphql_EnumValue=Graphql_Enum()), '\x00\x00', '', Graphql_EnumValue=Graphql_Enum()) == None


from python_code import Graphql_Schema

def test_Graphql_Schema___init__():
    assert Graphql_Schema.__init__(Graphql_Schema('', Graphql_Schema=set()), '', Graphql_Schema=set()) == None

