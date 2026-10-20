from python_code import dslComponent_DocumElt

def test_dslComponent_DocumElt___init__():
    assert dslComponent_DocumElt.__init__(dslComponent_DocumElt('', '\x00'), '\x00\x00', '') == None


from python_code import dslComponent_WTComponents

def test_dslComponent_WTComponents___init__():
    assert dslComponent_WTComponents.__init__(dslComponent_WTComponents('\x00\x00', '', dslComponent_WTComponents=set()), '', '', dslComponent_WTComponents=set()) == None

