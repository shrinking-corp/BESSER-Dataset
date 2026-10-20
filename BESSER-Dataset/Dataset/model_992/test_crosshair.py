from python_code import DAG_Graph

def test_DAG_Graph___init__():
    assert DAG_Graph.__init__(DAG_Graph('', DAG_Graph=set()), '', DAG_Graph=set()) == None

