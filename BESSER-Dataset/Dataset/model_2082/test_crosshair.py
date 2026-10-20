from python_code import Skeleton
from python_code import rsgf_bundle_Bundle

def test_rsgf_bundle_Bundle___init__():
    assert rsgf_bundle_Bundle.__init__(rsgf_bundle_Bundle('', rsgf_bundle_Bundle=Skeleton(), rsgf_bundle_Bundle14=set()), '', rsgf_bundle_Bundle=Skeleton(), rsgf_bundle_Bundle14=set()) == None


from python_code import Middleware
from python_code import rsgf_bundle_Process

def test_rsgf_bundle_Process___init__():
    assert rsgf_bundle_Process.__init__(rsgf_bundle_Process('', rsgf_bundle_Process=set(), rsgf_bundle_Process17=Middleware()), '', rsgf_bundle_Process=set(), rsgf_bundle_Process17=Middleware()) == None


from python_code import VM
from python_code import rsgf_mw_Middleware

def test_rsgf_mw_Middleware___init__():
    assert rsgf_mw_Middleware.__init__(rsgf_mw_Middleware(rsgf_mw_Middleware21=VM(), rsgf_mw_Middleware=set()), rsgf_mw_Middleware21=VM(), rsgf_mw_Middleware=set()) == None

def test_rsgf_mw_Middleware_send():
    assert rsgf_mw_Middleware.send(rsgf_mw_Middleware(rsgf_mw_Middleware21=VM(), rsgf_mw_Middleware=set())) == None

def test_rsgf_mw_Middleware_bind():
    assert rsgf_mw_Middleware.bind(rsgf_mw_Middleware(rsgf_mw_Middleware21=VM(), rsgf_mw_Middleware=set())) == None

def test_rsgf_mw_Middleware_establish():
    assert rsgf_mw_Middleware.establish(rsgf_mw_Middleware(rsgf_mw_Middleware21=VM(), rsgf_mw_Middleware=set())) == None


from python_code import Tree
from python_code import rsgf_skeleton_Skeleton

def test_rsgf_skeleton_Skeleton___init__():
    assert rsgf_skeleton_Skeleton.__init__(rsgf_skeleton_Skeleton('', rsgf_skeleton_Skeleton10=set(), rsgf_skeleton_Skeleton=Tree()), '', rsgf_skeleton_Skeleton10=set(), rsgf_skeleton_Skeleton=Tree()) == None


from python_code import Middleware
from python_code import rsgf_bundle_Process
from python_code import rsgf_tree_BasicNode

def test_rsgf_tree_BasicNode___init__():
    assert rsgf_tree_BasicNode.__init__(rsgf_tree_BasicNode('\x00\x00', Node=rsgf_bundle_Process('', rsgf_bundle_Process=set(), rsgf_bundle_Process17=Middleware())), '', Node=rsgf_bundle_Process('', rsgf_bundle_Process=set(), rsgf_bundle_Process17=Middleware())) == None


from python_code import rsgf_tree_Node

def test_rsgf_tree_Node___init__():
    assert rsgf_tree_Node.__init__(rsgf_tree_Node(''), '') == None


from python_code import Root
from python_code import rsgf_tree_Tree

def test_rsgf_tree_Tree___init__():
    assert rsgf_tree_Tree.__init__(rsgf_tree_Tree('', rsgf_tree_Tree=Root(), rsgf_tree_Tree2=set(), rsgf_tree_Tree4=set()), '', rsgf_tree_Tree=Root(), rsgf_tree_Tree2=set(), rsgf_tree_Tree4=set()) == None


from python_code import rsgf_vm_VM

def test_rsgf_vm_VM___init__():
    assert rsgf_vm_VM.__init__(rsgf_vm_VM('', '\x00'), '\x00\x00', '') == None

