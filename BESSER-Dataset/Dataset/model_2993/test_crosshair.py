from python_code import model_Administrator

def test_model_Administrator___init__():
    assert model_Administrator.__init__(model_Administrator()) == None

def test_model_Administrator_blockUser():
    assert model_Administrator.blockUser(model_Administrator()) == None

def test_model_Administrator_deleteContent():
    assert model_Administrator.deleteContent(model_Administrator()) == None


from python_code import model_AutoConfirmedUser

def test_model_AutoConfirmedUser___init__():
    assert model_AutoConfirmedUser.__init__(model_AutoConfirmedUser()) == None

def test_model_AutoConfirmedUser_moveArticle():
    assert model_AutoConfirmedUser.moveArticle(model_AutoConfirmedUser()) == None

def test_model_AutoConfirmedUser_moveMedia():
    assert model_AutoConfirmedUser.moveMedia(model_AutoConfirmedUser()) == None

def test_model_AutoConfirmedUser_createArticle():
    assert model_AutoConfirmedUser.createArticle(model_AutoConfirmedUser()) == None

def test_model_AutoConfirmedUser_uploadMedia():
    assert model_AutoConfirmedUser.uploadMedia(model_AutoConfirmedUser()) == None


from python_code import model_Internal

def test_model_Internal___init__():
    assert model_Internal.__init__(model_Internal('', '\x00'), '\x00\x00', '') == None


from python_code import model_Node

def test_model_Node___init__():
    assert model_Node.__init__(model_Node('', '\x00'), '\x00\x00', '') == None

def test_model_Node_getURI():
    assert model_Node.getURI(model_Node('', '')) == None

def test_model_Node_renderHTML():
    assert model_Node.renderHTML(model_Node('', '')) == None

def test_model_Node_getTypePrefix():
    assert model_Node.getTypePrefix(model_Node('', '')) == None

def test_model_Node_render():
    assert model_Node.render(model_Node('', '')) == None


from python_code import model_SysOp

def test_model_SysOp___init__():
    assert model_SysOp.__init__(model_SysOp()) == None

def test_model_SysOp_removeAdmin():
    assert model_SysOp.removeAdmin(model_SysOp()) == None

def test_model_SysOp_makeAdmin():
    assert model_SysOp.makeAdmin(model_SysOp()) == None

def test_model_SysOp_blockAdmin():
    assert model_SysOp.blockAdmin(model_SysOp()) == None


from python_code import model_UnregisteredUser

def test_model_UnregisteredUser___init__():
    assert model_UnregisteredUser.__init__(model_UnregisteredUser()) == None

def test_model_UnregisteredUser_changeMode():
    assert model_UnregisteredUser.changeMode(model_UnregisteredUser()) == None

