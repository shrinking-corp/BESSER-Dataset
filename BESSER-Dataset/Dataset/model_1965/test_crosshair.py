from python_code import MediaPlayer_BaseObject

def test_MediaPlayer_BaseObject___init__():
    assert MediaPlayer_BaseObject.__init__(MediaPlayer_BaseObject(0, '\x00'), 0, '\x00') == None

def test_MediaPlayer_BaseObject_addPropertyChangeListener():
    assert MediaPlayer_BaseObject.addPropertyChangeListener(MediaPlayer_BaseObject(0, ''), '') == None

def test_MediaPlayer_BaseObject_removePropertyChangeListener():
    assert MediaPlayer_BaseObject.removePropertyChangeListener(MediaPlayer_BaseObject(0, ''), '') == None

