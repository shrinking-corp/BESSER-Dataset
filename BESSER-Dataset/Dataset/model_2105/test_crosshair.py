from python_code import SemanticResourceDB_SemanticDB
from python_code import SemanticResourceDB_TreeRoot

def test_SemanticResourceDB_TreeRoot___init__():
    assert SemanticResourceDB_TreeRoot.__init__(SemanticResourceDB_TreeRoot('', TreeRoot=SemanticResourceDB_SemanticDB(), roots=SemanticResourceDB_SemanticDB()), '', TreeRoot=SemanticResourceDB_SemanticDB(), roots=SemanticResourceDB_SemanticDB()) == None

