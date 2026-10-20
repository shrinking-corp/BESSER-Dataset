from python_code import Distribucion

def test_Distribucion___init__():
    assert Distribucion.__init__(Distribucion(0, '', 0, '', ''), 0, '', 0, '', '') == None


from python_code import Elementos

def test_Elementos___init__():
    assert Elementos.__init__(Elementos('', '', factura29=set(), ordenesPedidos19=set(), solicitudSuministro21=set()), '', '', factura29=set(), ordenesPedidos19=set(), solicitudSuministro21=set()) == None


from python_code import EmpresasFiliales

def test_EmpresasFiliales___init__():
    assert EmpresasFiliales.__init__(EmpresasFiliales(0, '\x00', trabajador33=set()), 0, '', trabajador33=set()) == None


from python_code import Fabricacion

def test_Fabricacion___init__():
    assert Fabricacion.__init__(Fabricacion(0, '', 0, '', ''), 0, '', 0, '', '') == None


from python_code import Informe

def test_Informe___init__():
    assert Informe.__init__(Informe(0, '', '', 0, '', 0, trabajador31=set()), 0, '', '', 0, '', 0, trabajador31=set()) == None


from python_code import Proveedor

def test_Proveedor___init__():
    assert Proveedor.__init__(Proveedor('', '', '\x00', '', factura26=set(), ordenesPedidos14=set(), pedidos16=set()), '', '', '', '', factura26=set(), ordenesPedidos14=set(), pedidos16=set()) == None


from python_code import VentaCalzado

def test_VentaCalzado___init__():
    assert VentaCalzado.__init__(VentaCalzado(0, '', 0, '', ''), 0, '', 0, '', '') == None

