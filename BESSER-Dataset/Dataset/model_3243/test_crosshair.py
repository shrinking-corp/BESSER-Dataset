from python_code import remes_ControlPath
from python_code import remes_EntryPoint
from python_code import remes_ExitPoint

def test_remes_ControlPath___init__():
    assert remes_ControlPath.__init__(remes_ControlPath('', ControlPath=remes_EntryPoint(), ControlPath27=remes_ExitPoint(), container3=remes_ExitPoint(), container=remes_EntryPoint()), '', ControlPath=remes_EntryPoint(), ControlPath27=remes_ExitPoint(), container3=remes_ExitPoint(), container=remes_EntryPoint()) == None


from python_code import ActionRoot
from python_code import LogicalRoot
from python_code import remes_Edge
from python_code import remes_EntryPoint
from python_code import remes_ExitPoint

def test_remes_Edge___init__():
    assert remes_Edge.__init__(remes_Edge('', '\x00', Edge=remes_EntryPoint(), remes_Edge=LogicalRoot(), Edge25=remes_ExitPoint(), exitEdges=remes_ExitPoint(), entryEdges=remes_EntryPoint(), remes_Edge39=ActionRoot()), '\x00\x00', '', Edge=remes_EntryPoint(), remes_Edge=LogicalRoot(), Edge25=remes_ExitPoint(), exitEdges=remes_ExitPoint(), entryEdges=remes_EntryPoint(), remes_Edge39=ActionRoot()) == None


from python_code import remes_Referable

def test_remes_Referable___init__():
    assert remes_Referable.__init__(remes_Referable(''), '') == None


from python_code import LogicalRoot
from python_code import remes_CompositeMode
from python_code import remes_SubMode

def test_remes_SubMode___init__():
    assert remes_SubMode.__init__(remes_SubMode('', False, remes_SubMode=LogicalRoot(), subModes=remes_CompositeMode(), SubMode=remes_CompositeMode()), '', False, remes_SubMode=LogicalRoot(), subModes=remes_CompositeMode(), SubMode=remes_CompositeMode()) == None

