from python_code import rcl_LogAction

def test_rcl_LogAction___init__():
    assert rcl_LogAction.__init__(rcl_LogAction(''), '') == None


from python_code import rcl_ObstacleQuery

def test_rcl_ObstacleQuery___init__():
    assert rcl_ObstacleQuery.__init__(rcl_ObstacleQuery(True), False) == None


from python_code import rcl_RclBlock
from python_code import rcl_RoverProgram

def test_rcl_RoverProgram___init__():
    assert rcl_RoverProgram.__init__(rcl_RoverProgram('\x00', rcl_RoverProgram=set(), rcl_RoverProgram2=rcl_RclBlock()), '', rcl_RoverProgram=set(), rcl_RoverProgram2=rcl_RclBlock()) == None


from python_code import rcl_SendAction

def test_rcl_SendAction___init__():
    assert rcl_SendAction.__init__(rcl_SendAction(''), '') == None


from python_code import rcl_RoverValue
from python_code import rcl_VarAssignment

def test_rcl_VarAssignment___init__():
    assert rcl_VarAssignment.__init__(rcl_VarAssignment('', rcl_VarAssignment=rcl_RoverValue()), '', rcl_VarAssignment=rcl_RoverValue()) == None


from python_code import rcl_VarRef

def test_rcl_VarRef___init__():
    assert rcl_VarRef.__init__(rcl_VarRef(''), '') == None

