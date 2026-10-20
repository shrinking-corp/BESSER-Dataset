from python_code import eaglemodel_Approved
from python_code import eaglemodel_Errors

def test_eaglemodel_Approved___init__():
    assert eaglemodel_Approved.__init__(eaglemodel_Approved('', eaglemodel_Approved=eaglemodel_Errors()), '', eaglemodel_Approved=eaglemodel_Errors()) == None


from python_code import eaglemodel_Bus
from python_code import eaglemodel_Busses

def test_eaglemodel_Bus___init__():
    assert eaglemodel_Bus.__init__(eaglemodel_Bus('', eaglemodel_Bus=eaglemodel_Busses(), eaglemodel_Bus185=set()), '', eaglemodel_Bus=eaglemodel_Busses(), eaglemodel_Bus185=set()) == None


from python_code import eaglemodel_Class
from python_code import eaglemodel_Classes

def test_eaglemodel_Class___init__():
    assert eaglemodel_Class.__init__(eaglemodel_Class(0, '', 0.0, 0.0, eaglemodel_Class=eaglemodel_Classes(), eaglemodel_Class51=set()), 0, '', 0.0, 0.0, eaglemodel_Class=eaglemodel_Classes(), eaglemodel_Class51=set()) == None


from python_code import eaglemodel_Connect
from python_code import eaglemodel_Connects

def test_eaglemodel_Connect___init__():
    assert eaglemodel_Connect.__init__(eaglemodel_Connect('\x00\x00', '', '', '', eaglemodel_Connect=eaglemodel_Connects()), '', '', '', '', eaglemodel_Connect=eaglemodel_Connects()) == None


from python_code import eaglemodel_Connects
from python_code import eaglemodel_Device
from python_code import eaglemodel_Devices
from python_code import eaglemodel_Technologies

def test_eaglemodel_Device___init__():
    assert eaglemodel_Device.__init__(eaglemodel_Device('', '\x00', eaglemodel_Device=eaglemodel_Devices(), eaglemodel_Device143=eaglemodel_Connects(), eaglemodel_Device145=eaglemodel_Technologies()), '\x00\x00', '', eaglemodel_Device=eaglemodel_Devices(), eaglemodel_Device143=eaglemodel_Connects(), eaglemodel_Device145=eaglemodel_Technologies()) == None


from python_code import eaglemodel_Compatibility
from python_code import eaglemodel_Drawing
from python_code import eaglemodel_Eagle

def test_eaglemodel_Eagle___init__():
    assert eaglemodel_Eagle.__init__(eaglemodel_Eagle('', eaglemodel_Eagle2=eaglemodel_Drawing(), eaglemodel_Eagle=eaglemodel_Compatibility()), '', eaglemodel_Eagle2=eaglemodel_Drawing(), eaglemodel_Eagle=eaglemodel_Compatibility()) == None


from python_code import eaglemodel_Gate
from python_code import eaglemodel_Gates

def test_eaglemodel_Gate___init__():
    assert eaglemodel_Gate.__init__(eaglemodel_Gate('', '', 0.0, 0.0, '', 0, eaglemodel_Gate=eaglemodel_Gates()), '', '', 0.0, 0.0, '', 0, eaglemodel_Gate=eaglemodel_Gates()) == None


from python_code import eaglemodel_Drawing
from python_code import eaglemodel_Grid

def test_eaglemodel_Grid___init__():
    assert eaglemodel_Grid.__init__(eaglemodel_Grid(0.0, '', '', '', 0, True, 0.0, '', '', eaglemodel_Grid=eaglemodel_Drawing()), 0.0, '', '', '', 0, False, 0.0, '\x00', '', eaglemodel_Grid=eaglemodel_Drawing()) == None


from python_code import eaglemodel_Instance
from python_code import eaglemodel_Instances

def test_eaglemodel_Instance___init__():
    assert eaglemodel_Instance.__init__(eaglemodel_Instance('', '', 0.0, 0.0, False, 0, eaglemodel_Instance=eaglemodel_Instances(), eaglemodel_Instance180=set()), '', '', 0.0, 0.0, False, 0, eaglemodel_Instance=eaglemodel_Instances(), eaglemodel_Instance180=set()) == None


from python_code import eaglemodel_Junction
from python_code import eaglemodel_Segment

def test_eaglemodel_Junction___init__():
    assert eaglemodel_Junction.__init__(eaglemodel_Junction(0.0, 0.0, eaglemodel_Junction=eaglemodel_Segment()), 0.0, 0.0, eaglemodel_Junction=eaglemodel_Segment()) == None


from python_code import eaglemodel_Label
from python_code import eaglemodel_Segment

def test_eaglemodel_Label___init__():
    assert eaglemodel_Label.__init__(eaglemodel_Label(0.0, 0.0, 0.0, 0, '', 0, 0, True, eaglemodel_Label=eaglemodel_Segment()), 0.0, 0.0, 0.0, 0, '', 0, 0, False, eaglemodel_Label=eaglemodel_Segment()) == None


from python_code import eaglemodel_Layer
from python_code import eaglemodel_Layers

def test_eaglemodel_Layer___init__():
    assert eaglemodel_Layer.__init__(eaglemodel_Layer(0, '', 0, 0, False, False, eaglemodel_Layer=eaglemodel_Layers()), 0, '', 0, 0, False, False, eaglemodel_Layer=eaglemodel_Layers()) == None


from python_code import eaglemodel_Net
from python_code import eaglemodel_Nets

def test_eaglemodel_Net___init__():
    assert eaglemodel_Net.__init__(eaglemodel_Net('\x00\x00', 0, eaglemodel_Net=eaglemodel_Nets(), eaglemodel_Net189=set()), '', 0, eaglemodel_Net=eaglemodel_Nets(), eaglemodel_Net189=set()) == None


from python_code import eaglemodel_Compatibility
from python_code import eaglemodel_Note

def test_eaglemodel_Note___init__():
    assert eaglemodel_Note.__init__(eaglemodel_Note('', '', '\x00\x00', eaglemodel_Note=eaglemodel_Compatibility()), '', '', '', eaglemodel_Note=eaglemodel_Compatibility()) == None


from python_code import eaglemodel_Part
from python_code import eaglemodel_Parts

def test_eaglemodel_Part___init__():
    assert eaglemodel_Part.__init__(eaglemodel_Part('', '', '', '', '', '', '', 0.0, 0.0, False, 0, 0, eaglemodel_Part=eaglemodel_Parts(), eaglemodel_Part55=set(), eaglemodel_Part58=set()), '', '', '', '', '', '\x00', '', 0.0, 0.0, True, 0, 0, eaglemodel_Part=eaglemodel_Parts(), eaglemodel_Part55=set(), eaglemodel_Part58=set()) == None


from python_code import eaglemodel_Pinref
from python_code import eaglemodel_Segment

def test_eaglemodel_Pinref___init__():
    assert eaglemodel_Pinref.__init__(eaglemodel_Pinref('', '', '\x00\x00', eaglemodel_Pinref=eaglemodel_Segment()), '', '', '', eaglemodel_Pinref=eaglemodel_Segment()) == None

