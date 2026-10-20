from python_code import Skeleton
from python_code import ws_bundle_Bundle

def test_ws_bundle_Bundle___init__():
    assert ws_bundle_Bundle.__init__(ws_bundle_Bundle('', ws_bundle_Bundle=Skeleton(), ws_bundle_Bundle23=set()), '', ws_bundle_Bundle=Skeleton(), ws_bundle_Bundle23=set()) == None


from python_code import Middleware
from python_code import ws_bundle_Process

def test_ws_bundle_Process___init__():
    assert ws_bundle_Process.__init__(ws_bundle_Process('\x00\x00', ws_bundle_Process=set(), ws_bundle_Process27=Middleware()), '', ws_bundle_Process=set(), ws_bundle_Process27=Middleware()) == None

def test_ws_bundle_Process_receive():
    assert ws_bundle_Process.receive(ws_bundle_Process('', ws_bundle_Process=set(), ws_bundle_Process27=Middleware())) == None


from python_code import VM
from python_code import ws_middleware_Middleware

def test_ws_middleware_Middleware___init__():
    assert ws_middleware_Middleware.__init__(ws_middleware_Middleware(ws_middleware_Middleware=VM(), ws_middleware_Middleware2=set()), ws_middleware_Middleware=VM(), ws_middleware_Middleware2=set()) == None

def test_ws_middleware_Middleware_send():
    assert ws_middleware_Middleware.send(ws_middleware_Middleware(ws_middleware_Middleware=VM(), ws_middleware_Middleware2=set())) == None

def test_ws_middleware_Middleware_bind():
    assert ws_middleware_Middleware.bind(ws_middleware_Middleware(ws_middleware_Middleware=VM(), ws_middleware_Middleware2=set())) == None

def test_ws_middleware_Middleware_establish():
    assert ws_middleware_Middleware.establish(ws_middleware_Middleware(ws_middleware_Middleware=VM(), ws_middleware_Middleware2=set())) == None


from python_code import ws_middleware_Processor

def test_ws_middleware_Processor___init__():
    assert ws_middleware_Processor.__init__(ws_middleware_Processor('', '\x00'), '\x00\x00', '') == None

def test_ws_middleware_Processor_receive():
    assert ws_middleware_Processor.receive(ws_middleware_Processor('', '')) == None


from python_code import ws_middleware_Repository

def test_ws_middleware_Repository___init__():
    assert ws_middleware_Repository.__init__(ws_middleware_Repository(ws_middleware_Repository=set()), ws_middleware_Repository=set()) == None

def test_ws_middleware_Repository_lookup():
    assert ws_middleware_Repository.lookup(ws_middleware_Repository(ws_middleware_Repository=set())) == None

def test_ws_middleware_Repository_rebind():
    assert ws_middleware_Repository.rebind(ws_middleware_Repository(ws_middleware_Repository=set())) == None


from python_code import ws_middleware_Repository
from python_code import ws_middleware_ServiceImpl

def test_ws_middleware_ServiceImpl___init__():
    assert ws_middleware_ServiceImpl.__init__(ws_middleware_ServiceImpl(ServiceDescription=ws_middleware_Repository(ws_middleware_Repository=set())), ServiceDescription=ws_middleware_Repository(ws_middleware_Repository=set())) == None

def test_ws_middleware_ServiceImpl_receive():
    assert ws_middleware_ServiceImpl.receive(ws_middleware_ServiceImpl(ServiceDescription=ws_middleware_Repository(ws_middleware_Repository=set()))) == None


from python_code import ServiceImpl
from python_code import ws_middleware_Stub

def test_ws_middleware_Stub___init__():
    assert ws_middleware_Stub.__init__(ws_middleware_Stub(ws_middleware_Stub=ServiceImpl()), ws_middleware_Stub=ServiceImpl()) == None

def test_ws_middleware_Stub_receive():
    assert ws_middleware_Stub.receive(ws_middleware_Stub(ws_middleware_Stub=ServiceImpl())) == None


from python_code import ws_middleware_VM

def test_ws_middleware_VM___init__():
    assert ws_middleware_VM.__init__(ws_middleware_VM('\x00\x00', '', ws_middleware_VM=set()), '', '', ws_middleware_VM=set()) == None


from python_code import Tree
from python_code import ws_skeleton_Skeleton

def test_ws_skeleton_Skeleton___init__():
    assert ws_skeleton_Skeleton.__init__(ws_skeleton_Skeleton('', ws_skeleton_Skeleton=Tree(), ws_skeleton_Skeleton19=set()), '', ws_skeleton_Skeleton=Tree(), ws_skeleton_Skeleton19=set()) == None


from python_code import Middleware
from python_code import ws_bundle_Process
from python_code import ws_tree_BasicNode

def test_ws_tree_BasicNode___init__():
    assert ws_tree_BasicNode.__init__(ws_tree_BasicNode('', Node=ws_bundle_Process('', ws_bundle_Process=set(), ws_bundle_Process27=Middleware())), '', Node=ws_bundle_Process('', ws_bundle_Process=set(), ws_bundle_Process27=Middleware())) == None


from python_code import ws_tree_Node

def test_ws_tree_Node___init__():
    assert ws_tree_Node.__init__(ws_tree_Node(''), '') == None


from python_code import Root
from python_code import ws_tree_Tree

def test_ws_tree_Tree___init__():
    assert ws_tree_Tree.__init__(ws_tree_Tree('', ws_tree_Tree=Root(), ws_tree_Tree11=set(), ws_tree_Tree13=set()), '', ws_tree_Tree=Root(), ws_tree_Tree11=set(), ws_tree_Tree13=set()) == None

