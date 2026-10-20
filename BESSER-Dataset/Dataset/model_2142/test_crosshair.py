from python_code import WT_DocumentElt

def test_WT_DocumentElt___init__():
    assert WT_DocumentElt.__init__(WT_DocumentElt('', '\x00'), '\x00\x00', '') == None


from python_code import WT_WTComponents

def test_WT_WTComponents___init__():
    assert WT_WTComponents.__init__(WT_WTComponents('', WT_WTComponents=set()), '', WT_WTComponents=set()) == None

