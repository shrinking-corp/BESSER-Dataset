from python_code import Activity

def test_Activity___init__():
    assert Activity.__init__(Activity(0, '', '', 0, 0, '', '\x00', False), 0, '', '', 0, 0, '', '', False) == None


from python_code import Attachment

def test_Attachment___init__():
    assert Attachment.__init__(Attachment(0, '', '', '', '', '', '\x00', ''), 0, '', '', '', '', '', '', '') == None


from python_code import Comment

def test_Comment___init__():
    assert Comment.__init__(Comment(0, '', '', '', ''), 0, '', '', '', '') == None


from python_code import RoomService
from python_code import Room_Interface

def test_RoomService___init__():
    assert RoomService.__init__(RoomService('\x00\x00', '', '', '', room11=Room_Interface()), '', '', '', '', room11=Room_Interface()) == None

