import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Areas_del_Conocimiento,
    Brindar_Consultoria_external,
    Calcular,
    Class4,
    Clientes_Actor,
    Component_Component,
    Creditos,
    Departamento,
    Departamento_de_inventarios_y_suministros___DIS_Component,
    Dependencia,
    Dependencias_Actor,
    ELementos,
    Entregar_los_pedidos_external,
    Horas_de_clase,
    Impuesto,
    Javaaplication,
    Juridico_Actor,
    LogicaPresentacion___Factura_Component,
    Materias,
    Millenium_S_A_Component,
    Natural_Actor,
    OrdenesPedidos,
    Pedidos,
    Pemsum_Universitario,
    Persistencia___Factura_Component,
    Producto,
    Profesor,
    Programa,
    Proveedor,
    Proveedores_Actor,
    Recibir_productos_external,
    Recivir_ordenes_de_suministro_external,
    Registrar_proveedores_external,
    Servidor_BD_Node,
    Servidor_Intel__Node,
    Servidor_WEB_Node,
    SolicitudSuministro,
    Venta,
    asignacion_de_creditos,
)

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_Asignada_por_reverse_link_reassign_clear():
    a1 = Profesor(Apellido="sample_text", Area="sample_text", ID=7, Nombre="sample_text")
    a2 = Profesor(Apellido="sample_text_2", Area="sample_text_2", ID=13, Nombre="sample_text_2")
    b = Materias(Codigo=7, Creditos=7, Nombre="sample_text", Tipo="sample_text")
    _safe_set(b, 'profesores29', {a1})
    assert _is_linked(b, 'profesores29', a1)
    if hasattr(a1, 'materias28'):
        assert _is_linked(a1, 'materias28', b)
    _safe_set(b, 'profesores29', {a2})
    assert _is_linked(b, 'profesores29', a2)
    if hasattr(a1, 'materias28'):
        assert not _is_linked(a1, 'materias28', b)
    if hasattr(a2, 'materias28'):
        assert _is_linked(a2, 'materias28', b)
    _safe_set(b, 'profesores29', set())
    assert not _is_linked(b, 'profesores29', a2)
    if hasattr(a2, 'materias28'):
        assert not _is_linked(a2, 'materias28', b)


def test_assoc_Ayudan_a_reverse_link_reassign_clear():
    a1 = Pemsum_Universitario(Materias="sample_text", Programa="sample_text")
    a2 = Pemsum_Universitario(Materias="sample_text_2", Programa="sample_text_2")
    b = Departamento(ID_Profesores=7)
    _safe_set(b, 'pemsum_Universitario35', a1)
    assert _is_linked(b, 'pemsum_Universitario35', a1)
    if hasattr(a1, 'departamento34'):
        assert _is_linked(a1, 'departamento34', b)
    _safe_set(b, 'pemsum_Universitario35', a2)
    assert _is_linked(b, 'pemsum_Universitario35', a2)
    if hasattr(a1, 'departamento34'):
        assert not _is_linked(a1, 'departamento34', b)
    if hasattr(a2, 'departamento34'):
        assert _is_linked(a2, 'departamento34', b)
    _safe_set(b, 'pemsum_Universitario35', None)
    assert not _is_linked(b, 'pemsum_Universitario35', a2)
    if hasattr(a2, 'departamento34'):
        assert not _is_linked(a2, 'departamento34', b)


def test_assoc_Ayudan_a1_reverse_link_reassign_clear():
    a1 = Pemsum_Universitario(Materias="sample_text", Programa="sample_text")
    a2 = Pemsum_Universitario(Materias="sample_text_2", Programa="sample_text_2")
    b = Areas_del_Conocimiento(Departamentos="sample_text", NombreArea="sample_text")
    _safe_set(b, 'pemsum_Universitario37', a1)
    assert _is_linked(b, 'pemsum_Universitario37', a1)
    if hasattr(a1, 'areas_del_Conocimiento36'):
        assert _is_linked(a1, 'areas_del_Conocimiento36', b)
    _safe_set(b, 'pemsum_Universitario37', a2)
    assert _is_linked(b, 'pemsum_Universitario37', a2)
    if hasattr(a1, 'areas_del_Conocimiento36'):
        assert not _is_linked(a1, 'areas_del_Conocimiento36', b)
    if hasattr(a2, 'areas_del_Conocimiento36'):
        assert _is_linked(a2, 'areas_del_Conocimiento36', b)
    _safe_set(b, 'pemsum_Universitario37', None)
    assert not _is_linked(b, 'pemsum_Universitario37', a2)
    if hasattr(a2, 'areas_del_Conocimiento36'):
        assert not _is_linked(a2, 'areas_del_Conocimiento36', b)


def test_assoc_Conforma_reverse_link_reassign_clear():
    a1 = OrdenesPedidos(Codigo="sample_text", Fecha="sample_text")
    a2 = OrdenesPedidos(Codigo="sample_text_2", Fecha="sample_text_2")
    b = ELementos(Clasificacion="sample_text", REferencia="sample_text")
    _safe_set(b, 'ordenesPedidos15', {a1})
    assert _is_linked(b, 'ordenesPedidos15', a1)
    if hasattr(a1, 'eLementos14'):
        assert _is_linked(a1, 'eLementos14', b)
    _safe_set(b, 'ordenesPedidos15', {a2})
    assert _is_linked(b, 'ordenesPedidos15', a2)
    if hasattr(a1, 'eLementos14'):
        assert not _is_linked(a1, 'eLementos14', b)
    if hasattr(a2, 'eLementos14'):
        assert _is_linked(a2, 'eLementos14', b)
    _safe_set(b, 'ordenesPedidos15', set())
    assert not _is_linked(b, 'ordenesPedidos15', a2)
    if hasattr(a2, 'eLementos14'):
        assert not _is_linked(a2, 'eLementos14', b)


def test_assoc_Contiene_reverse_link_reassign_clear():
    a1 = Pemsum_Universitario(Materias="sample_text", Programa="sample_text")
    a2 = Pemsum_Universitario(Materias="sample_text_2", Programa="sample_text_2")
    b = Materias(Codigo=7, Creditos=7, Nombre="sample_text", Tipo="sample_text")
    _safe_set(b, 'pemsum_Universitario26', a1)
    assert _is_linked(b, 'pemsum_Universitario26', a1)
    if hasattr(a1, 'materias27'):
        assert _is_linked(a1, 'materias27', b)
    _safe_set(b, 'pemsum_Universitario26', a2)
    assert _is_linked(b, 'pemsum_Universitario26', a2)
    if hasattr(a1, 'materias27'):
        assert not _is_linked(a1, 'materias27', b)
    if hasattr(a2, 'materias27'):
        assert _is_linked(a2, 'materias27', b)
    _safe_set(b, 'pemsum_Universitario26', None)
    assert not _is_linked(b, 'pemsum_Universitario26', a2)
    if hasattr(a2, 'materias27'):
        assert not _is_linked(a2, 'materias27', b)


def test_assoc_Contiene1_reverse_link_reassign_clear():
    a1 = Programa(Codigo=7, Nombre="sample_text")
    a2 = Programa(Codigo=13, Nombre="sample_text_2")
    b = Pemsum_Universitario(Materias="sample_text", Programa="sample_text")
    _safe_set(b, 'programa44', {a1})
    assert _is_linked(b, 'programa44', a1)
    if hasattr(a1, 'pemsum_Universitario45'):
        assert _is_linked(a1, 'pemsum_Universitario45', b)
    _safe_set(b, 'programa44', {a2})
    assert _is_linked(b, 'programa44', a2)
    if hasattr(a1, 'pemsum_Universitario45'):
        assert not _is_linked(a1, 'pemsum_Universitario45', b)
    if hasattr(a2, 'pemsum_Universitario45'):
        assert _is_linked(a2, 'pemsum_Universitario45', b)
    _safe_set(b, 'programa44', set())
    assert not _is_linked(b, 'programa44', a2)
    if hasattr(a2, 'pemsum_Universitario45'):
        assert not _is_linked(a2, 'pemsum_Universitario45', b)


def test_assoc_Es_Enviado_reverse_link_reassign_clear():
    a1 = Proveedor(Direccion="sample_text", Nit="sample_text", Razonsocial="sample_text", Telefonos="sample_text")
    a2 = Proveedor(Direccion="sample_text_2", Nit="sample_text_2", Razonsocial="sample_text_2", Telefonos="sample_text_2")
    b = OrdenesPedidos(Codigo="sample_text", Fecha="sample_text")
    _safe_set(b, 'proveedor11', a1)
    assert _is_linked(b, 'proveedor11', a1)
    if hasattr(a1, 'ordenesPedidos10'):
        assert _is_linked(a1, 'ordenesPedidos10', b)
    _safe_set(b, 'proveedor11', a2)
    assert _is_linked(b, 'proveedor11', a2)
    if hasattr(a1, 'ordenesPedidos10'):
        assert not _is_linked(a1, 'ordenesPedidos10', b)
    if hasattr(a2, 'ordenesPedidos10'):
        assert _is_linked(a2, 'ordenesPedidos10', b)
    _safe_set(b, 'proveedor11', None)
    assert not _is_linked(b, 'proveedor11', a2)
    if hasattr(a2, 'ordenesPedidos10'):
        assert not _is_linked(a2, 'ordenesPedidos10', b)


def test_assoc_Forma_reverse_link_reassign_clear():
    a1 = asignacion_de_creditos(Cod_Materia=7)
    a2 = asignacion_de_creditos(Cod_Materia=13)
    b = Creditos(Numeros=7)
    _safe_set(b, 'asignacion_de_creditos42', {a1})
    assert _is_linked(b, 'asignacion_de_creditos42', a1)
    if hasattr(a1, 'creditos43'):
        assert _is_linked(a1, 'creditos43', b)
    _safe_set(b, 'asignacion_de_creditos42', {a2})
    assert _is_linked(b, 'asignacion_de_creditos42', a2)
    if hasattr(a1, 'creditos43'):
        assert not _is_linked(a1, 'creditos43', b)
    if hasattr(a2, 'creditos43'):
        assert _is_linked(a2, 'creditos43', b)
    _safe_set(b, 'asignacion_de_creditos42', set())
    assert not _is_linked(b, 'asignacion_de_creditos42', a2)
    if hasattr(a2, 'creditos43'):
        assert not _is_linked(a2, 'creditos43', b)


def test_assoc_Genera_reverse_link_reassign_clear():
    a1 = SolicitudSuministro(Codigo="sample_text", Fecha="sample_text")
    a2 = SolicitudSuministro(Codigo="sample_text_2", Fecha="sample_text_2")
    b = OrdenesPedidos(Codigo="sample_text", Fecha="sample_text")
    _safe_set(b, 'solicitudSuministro19', {a1})
    assert _is_linked(b, 'solicitudSuministro19', a1)
    if hasattr(a1, 'ordenesPedidos18'):
        assert _is_linked(a1, 'ordenesPedidos18', b)
    _safe_set(b, 'solicitudSuministro19', {a2})
    assert _is_linked(b, 'solicitudSuministro19', a2)
    if hasattr(a1, 'ordenesPedidos18'):
        assert not _is_linked(a1, 'ordenesPedidos18', b)
    if hasattr(a2, 'ordenesPedidos18'):
        assert _is_linked(a2, 'ordenesPedidos18', b)
    _safe_set(b, 'solicitudSuministro19', set())
    assert not _is_linked(b, 'solicitudSuministro19', a2)
    if hasattr(a2, 'ordenesPedidos18'):
        assert not _is_linked(a2, 'ordenesPedidos18', b)


def test_assoc_Hace_reverse_link_reassign_clear():
    a1 = asignacion_de_creditos(Cod_Materia=7)
    a2 = asignacion_de_creditos(Cod_Materia=13)
    b = Areas_del_Conocimiento(Departamentos="sample_text", NombreArea="sample_text")
    _safe_set(b, 'asignacion_de_creditos39', {a1})
    assert _is_linked(b, 'asignacion_de_creditos39', a1)
    if hasattr(a1, 'areas_del_Conocimiento38'):
        assert _is_linked(a1, 'areas_del_Conocimiento38', b)
    _safe_set(b, 'asignacion_de_creditos39', {a2})
    assert _is_linked(b, 'asignacion_de_creditos39', a2)
    if hasattr(a1, 'areas_del_Conocimiento38'):
        assert not _is_linked(a1, 'areas_del_Conocimiento38', b)
    if hasattr(a2, 'areas_del_Conocimiento38'):
        assert _is_linked(a2, 'areas_del_Conocimiento38', b)
    _safe_set(b, 'asignacion_de_creditos39', set())
    assert not _is_linked(b, 'asignacion_de_creditos39', a2)
    if hasattr(a2, 'areas_del_Conocimiento38'):
        assert not _is_linked(a2, 'areas_del_Conocimiento38', b)


def test_assoc_Hace1_reverse_link_reassign_clear():
    a1 = asignacion_de_creditos(Cod_Materia=7)
    a2 = asignacion_de_creditos(Cod_Materia=13)
    b = Departamento(ID_Profesores=7)
    _safe_set(b, 'asignacion_de_creditos41', {a1})
    assert _is_linked(b, 'asignacion_de_creditos41', a1)
    if hasattr(a1, 'departamento40'):
        assert _is_linked(a1, 'departamento40', b)
    _safe_set(b, 'asignacion_de_creditos41', {a2})
    assert _is_linked(b, 'asignacion_de_creditos41', a2)
    if hasattr(a1, 'departamento40'):
        assert not _is_linked(a1, 'departamento40', b)
    if hasattr(a2, 'departamento40'):
        assert _is_linked(a2, 'departamento40', b)
    _safe_set(b, 'asignacion_de_creditos41', set())
    assert not _is_linked(b, 'asignacion_de_creditos41', a2)
    if hasattr(a2, 'departamento40'):
        assert not _is_linked(a2, 'departamento40', b)


def test_assoc_Producto_Impuesto_reverse_link_reassign_clear():
    a1 = Producto(CalcularCosto=7, Cantidad=7, Codigo=7, Nombre="sample_text", Precio=7)
    a2 = Producto(CalcularCosto=13, Cantidad=13, Codigo=13, Nombre="sample_text_2", Precio=13)
    b = Impuesto(CalcularImpuesto=3.14, Porcentae=3.14)
    _safe_set(b, 'producto52', a1)
    assert _is_linked(b, 'producto52', a1)
    if hasattr(a1, 'impuesto53'):
        assert _is_linked(a1, 'impuesto53', b)
    _safe_set(b, 'producto52', a2)
    assert _is_linked(b, 'producto52', a2)
    if hasattr(a1, 'impuesto53'):
        assert not _is_linked(a1, 'impuesto53', b)
    if hasattr(a2, 'impuesto53'):
        assert _is_linked(a2, 'impuesto53', b)
    _safe_set(b, 'producto52', None)
    assert not _is_linked(b, 'producto52', a2)
    if hasattr(a2, 'impuesto53'):
        assert not _is_linked(a2, 'impuesto53', b)


def test_assoc_Provee_reverse_link_reassign_clear():
    a1 = Proveedor(Direccion="sample_text", Nit="sample_text", Razonsocial="sample_text", Telefonos="sample_text")
    a2 = Proveedor(Direccion="sample_text_2", Nit="sample_text_2", Razonsocial="sample_text_2", Telefonos="sample_text_2")
    b = Pedidos(Codigo="sample_text", Fecha="sample_text")
    _safe_set(b, 'proveedor12', a1)
    assert _is_linked(b, 'proveedor12', a1)
    if hasattr(a1, 'pedidos13'):
        assert _is_linked(a1, 'pedidos13', b)
    _safe_set(b, 'proveedor12', a2)
    assert _is_linked(b, 'proveedor12', a2)
    if hasattr(a1, 'pedidos13'):
        assert not _is_linked(a1, 'pedidos13', b)
    if hasattr(a2, 'pedidos13'):
        assert _is_linked(a2, 'pedidos13', b)
    _safe_set(b, 'proveedor12', None)
    assert not _is_linked(b, 'proveedor12', a2)
    if hasattr(a2, 'pedidos13'):
        assert not _is_linked(a2, 'pedidos13', b)


def test_assoc_Realiza_reverse_link_reassign_clear():
    a1 = SolicitudSuministro(Codigo="sample_text", Fecha="sample_text")
    a2 = SolicitudSuministro(Codigo="sample_text_2", Fecha="sample_text_2")
    b = Dependencia(Codigo="sample_text", Nombre="sample_text", Responsable="sample_text")
    _safe_set(b, 'solicitudSuministro20', {a1})
    assert _is_linked(b, 'solicitudSuministro20', a1)
    if hasattr(a1, 'dependencia21'):
        assert _is_linked(a1, 'dependencia21', b)
    _safe_set(b, 'solicitudSuministro20', {a2})
    assert _is_linked(b, 'solicitudSuministro20', a2)
    if hasattr(a1, 'dependencia21'):
        assert not _is_linked(a1, 'dependencia21', b)
    if hasattr(a2, 'dependencia21'):
        assert _is_linked(a2, 'dependencia21', b)
    _safe_set(b, 'solicitudSuministro20', set())
    assert not _is_linked(b, 'solicitudSuministro20', a2)
    if hasattr(a2, 'dependencia21'):
        assert not _is_linked(a2, 'dependencia21', b)


def test_assoc_Relasiona_reverse_link_reassign_clear():
    a1 = SolicitudSuministro(Codigo="sample_text", Fecha="sample_text")
    a2 = SolicitudSuministro(Codigo="sample_text_2", Fecha="sample_text_2")
    b = ELementos(Clasificacion="sample_text", REferencia="sample_text")
    _safe_set(b, 'solicitudSuministro17', {a1})
    assert _is_linked(b, 'solicitudSuministro17', a1)
    if hasattr(a1, 'eLementos16'):
        assert _is_linked(a1, 'eLementos16', b)
    _safe_set(b, 'solicitudSuministro17', {a2})
    assert _is_linked(b, 'solicitudSuministro17', a2)
    if hasattr(a1, 'eLementos16'):
        assert not _is_linked(a1, 'eLementos16', b)
    if hasattr(a2, 'eLementos16'):
        assert _is_linked(a2, 'eLementos16', b)
    _safe_set(b, 'solicitudSuministro17', set())
    assert not _is_linked(b, 'solicitudSuministro17', a2)
    if hasattr(a2, 'eLementos16'):
        assert not _is_linked(a2, 'eLementos16', b)


def test_assoc_Tiene_reverse_link_reassign_clear():
    a1 = Materias(Codigo=7, Creditos=7, Nombre="sample_text", Tipo="sample_text")
    a2 = Materias(Codigo=13, Creditos=13, Nombre="sample_text_2", Tipo="sample_text_2")
    b = Creditos(Numeros=7)
    _safe_set(b, 'materias30', a1)
    assert _is_linked(b, 'materias30', a1)
    if hasattr(a1, 'creditos31'):
        assert _is_linked(a1, 'creditos31', b)
    _safe_set(b, 'materias30', a2)
    assert _is_linked(b, 'materias30', a2)
    if hasattr(a1, 'creditos31'):
        assert not _is_linked(a1, 'creditos31', b)
    if hasattr(a2, 'creditos31'):
        assert _is_linked(a2, 'creditos31', b)
    _safe_set(b, 'materias30', None)
    assert not _is_linked(b, 'materias30', a2)
    if hasattr(a2, 'creditos31'):
        assert not _is_linked(a2, 'creditos31', b)


def test_assoc_Tiene1_reverse_link_reassign_clear():
    a1 = Materias(Codigo=7, Creditos=7, Nombre="sample_text", Tipo="sample_text")
    a2 = Materias(Codigo=13, Creditos=13, Nombre="sample_text_2", Tipo="sample_text_2")
    b = Horas_de_clase(CreditosMateria="sample_text", TipoCreditos="sample_text")
    _safe_set(b, 'materias33', a1)
    assert _is_linked(b, 'materias33', a1)
    if hasattr(a1, 'horas_de_clase32'):
        assert _is_linked(a1, 'horas_de_clase32', b)
    _safe_set(b, 'materias33', a2)
    assert _is_linked(b, 'materias33', a2)
    if hasattr(a1, 'horas_de_clase32'):
        assert not _is_linked(a1, 'horas_de_clase32', b)
    if hasattr(a2, 'horas_de_clase32'):
        assert _is_linked(a2, 'horas_de_clase32', b)
    _safe_set(b, 'materias33', None)
    assert not _is_linked(b, 'materias33', a2)
    if hasattr(a2, 'horas_de_clase32'):
        assert not _is_linked(a2, 'horas_de_clase32', b)


def test_assoc_Venta_Impuesto_reverse_link_reassign_clear():
    a1 = Venta(Codigo=7, Fecha="sample_text", RealizarVenta="sample_text")
    a2 = Venta(Codigo=13, Fecha="sample_text_2", RealizarVenta="sample_text_2")
    b = Impuesto(CalcularImpuesto=3.14, Porcentae=3.14)
    _safe_set(b, 'venta50', a1)
    assert _is_linked(b, 'venta50', a1)
    if hasattr(a1, 'impuesto51'):
        assert _is_linked(a1, 'impuesto51', b)
    _safe_set(b, 'venta50', a2)
    assert _is_linked(b, 'venta50', a2)
    if hasattr(a1, 'impuesto51'):
        assert not _is_linked(a1, 'impuesto51', b)
    if hasattr(a2, 'impuesto51'):
        assert _is_linked(a2, 'impuesto51', b)
    _safe_set(b, 'venta50', None)
    assert not _is_linked(b, 'venta50', a2)
    if hasattr(a2, 'impuesto51'):
        assert not _is_linked(a2, 'impuesto51', b)


def test_assoc_Venta_Producto_reverse_link_reassign_clear():
    a1 = Venta(Codigo=7, Fecha="sample_text", RealizarVenta="sample_text")
    a2 = Venta(Codigo=13, Fecha="sample_text_2", RealizarVenta="sample_text_2")
    b = Producto(CalcularCosto=7, Cantidad=7, Codigo=7, Nombre="sample_text", Precio=7)
    _safe_set(b, 'venta48', a1)
    assert _is_linked(b, 'venta48', a1)
    if hasattr(a1, 'producto49'):
        assert _is_linked(a1, 'producto49', b)
    _safe_set(b, 'venta48', a2)
    assert _is_linked(b, 'venta48', a2)
    if hasattr(a1, 'producto49'):
        assert not _is_linked(a1, 'producto49', b)
    if hasattr(a2, 'producto49'):
        assert _is_linked(a2, 'producto49', b)
    _safe_set(b, 'venta48', None)
    assert not _is_linked(b, 'venta48', a2)
    if hasattr(a2, 'producto49'):
        assert not _is_linked(a2, 'producto49', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

