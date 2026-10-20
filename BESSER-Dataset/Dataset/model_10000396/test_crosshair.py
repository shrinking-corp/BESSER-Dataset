from python_code import BankAccount

def test_BankAccount___init__():
    assert BankAccount.__init__(BankAccount('\x00', 0.0), '', 0.0) == None


from python_code import ClassC

def test_ClassC___init__():
    assert ClassC.__init__(ClassC(0.0, 0, '', ''), 0.0, 0, '', '') == None


from python_code import MeshGeometry3D
from python_code import Point3D

def test_MeshGeometry3D___init__():
    assert MeshGeometry3D.__init__(MeshGeometry3D(Point3D(0, 0, 0), 0, '', ''), Point3D(0, 0, 0), 0, '\x00', '') == None


from python_code import Point3D

def test_Point3D___init__():
    assert Point3D.__init__(Point3D(0, 0, 0), 0, 0, 0) == None

