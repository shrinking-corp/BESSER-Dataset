from python_code import mtl_Comment
from python_code import mtl_CommentBody

def test_mtl_CommentBody___init__():
    assert mtl_CommentBody.__init__(mtl_CommentBody(0, 0, '\x00\x00', mtl_CommentBody=mtl_Comment()), 0, 0, '', mtl_CommentBody=mtl_Comment()) == None


from python_code import mtl_Documentation
from python_code import mtl_DocumentedElement

def test_mtl_DocumentedElement___init__():
    assert mtl_DocumentedElement.__init__(mtl_DocumentedElement(True, DocumentedElement=mtl_Documentation(), documentedElement=mtl_Documentation()), False, DocumentedElement=mtl_Documentation(), documentedElement=mtl_Documentation()) == None


from python_code import OCLExpression
from python_code import mtl_FileBlock

def test_mtl_FileBlock___init__():
    assert mtl_FileBlock.__init__(mtl_FileBlock('', mtl_FileBlock=OCLExpression(), mtl_FileBlock89=OCLExpression(), mtl_FileBlock92=OCLExpression()), '\x00', mtl_FileBlock=OCLExpression(), mtl_FileBlock89=OCLExpression(), mtl_FileBlock92=OCLExpression()) == None


from python_code import mtl_ModuleDocumentation

def test_mtl_ModuleDocumentation___init__():
    assert mtl_ModuleDocumentation.__init__(mtl_ModuleDocumentation('', '', '\x00\x00'), '', '', '') == None

