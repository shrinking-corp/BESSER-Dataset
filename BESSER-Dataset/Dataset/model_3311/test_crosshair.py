from python_code import grammar_ConnexionInstruction
from python_code import grammar_Embedding
from python_code import grammar_Node

def test_grammar_ConnexionInstruction___init__():
    assert grammar_ConnexionInstruction.__init__(grammar_ConnexionInstruction('', ConnexionInstruction=grammar_Embedding(), instructions=grammar_Embedding(), grammar_ConnexionInstruction=grammar_Node()), '', ConnexionInstruction=grammar_Embedding(), instructions=grammar_Embedding(), grammar_ConnexionInstruction=grammar_Node()) == None


from python_code import grammar_Embedding
from python_code import grammar_Grammar
from python_code import grammar_LHS
from python_code import grammar_RHS
from python_code import grammar_Rule

def test_grammar_Rule___init__():
    assert grammar_Rule.__init__(grammar_Rule('', 0, Rule=grammar_Grammar(), rules=grammar_Grammar(), parentRule=grammar_LHS(), parentRule4=grammar_RHS(), ParentRule=grammar_Embedding(), Rule13=grammar_Embedding(), Rule7=grammar_LHS(), Rule10=grammar_RHS()), '', 0, Rule=grammar_Grammar(), rules=grammar_Grammar(), parentRule=grammar_LHS(), parentRule4=grammar_RHS(), ParentRule=grammar_Embedding(), Rule13=grammar_Embedding(), Rule7=grammar_LHS(), Rule10=grammar_RHS()) == None

