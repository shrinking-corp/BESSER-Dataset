from python_code import FeedBack

def test_FeedBack___init__():
    assert FeedBack.__init__(FeedBack('\x00\x00', '', Items10=set()), '', '', Items10=set()) == None

