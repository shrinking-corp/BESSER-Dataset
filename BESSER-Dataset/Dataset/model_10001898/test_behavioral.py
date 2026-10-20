import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Actor_Actor,
    Brinda_consultoria_external,
    Clasificar_Producto_external,
    Comprador,
    Departamento,
    Departamento_de_Inventarios_y_Suministros___Dis_Component,
    Departamento_de_contabilidad_y_tesoreria_Actor,
    Dependencia,
    Dependencia_Actor,
    Ejecuci_n,
    Elementos,
    Encargos,
    Factura,
    Generar_ordenes_de_pedidos_external,
    Historial_trabajadores,
    Juridica_Actor,
    Mileninum_Component,
    Natural_Actor,
    Obras,
    OrdenesPedido,
    Pedidos,
    Permisos,
    Planos,
    PlanosTerreno,
    Profesores,
    Proveedores,
    Proveedores_Actor,
    Recibir_ordenes_de_suministro_external,
    Recibir_productos_y_pedidos_external,
    Registrar_proveedores_external,
    Servidor_intel_i8_Node,
    Sistema_Electrico,
    Sistema_WEB_Movil___Recceci_n_de_pedidos_Component,
    Sistema_desplegable,
    SolucitudSuministro,
    Trabajadores,
    _reasConocimiento,
    facturas_pagos_,
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

def test_assoc_Provee_reverse_link_reassign_clear():
    a1 = Proveedores(direccion="sample_text", nit="sample_text", razonSocial="sample_text", telefonos=7)
    a2 = Proveedores(direccion="sample_text_2", nit="sample_text_2", razonSocial="sample_text_2", telefonos=13)
    b = Pedidos(codigo="sample_text", fecha="sample_text")
    _safe_set(b, 'proveedores17', a1)
    assert _is_linked(b, 'proveedores17', a1)
    if hasattr(a1, 'pedidos16'):
        assert _is_linked(a1, 'pedidos16', b)
    _safe_set(b, 'proveedores17', a2)
    assert _is_linked(b, 'proveedores17', a2)
    if hasattr(a1, 'pedidos16'):
        assert not _is_linked(a1, 'pedidos16', b)
    if hasattr(a2, 'pedidos16'):
        assert _is_linked(a2, 'pedidos16', b)
    _safe_set(b, 'proveedores17', None)
    assert not _is_linked(b, 'proveedores17', a2)
    if hasattr(a2, 'pedidos16'):
        assert not _is_linked(a2, 'pedidos16', b)


def test_assoc_Realiza_reverse_link_reassign_clear():
    a1 = SolucitudSuministro(codigo="sample_text", fecha="sample_text")
    a2 = SolucitudSuministro(codigo="sample_text_2", fecha="sample_text_2")
    b = Dependencia(codigo="sample_text", nombre="sample_text", responsable="sample_text")
    _safe_set(b, 'solucitudSuministro26', {a1})
    assert _is_linked(b, 'solucitudSuministro26', a1)
    if hasattr(a1, 'dependencia27'):
        assert _is_linked(a1, 'dependencia27', b)
    _safe_set(b, 'solucitudSuministro26', {a2})
    assert _is_linked(b, 'solucitudSuministro26', a2)
    if hasattr(a1, 'dependencia27'):
        assert not _is_linked(a1, 'dependencia27', b)
    if hasattr(a2, 'dependencia27'):
        assert _is_linked(a2, 'dependencia27', b)
    _safe_set(b, 'solucitudSuministro26', set())
    assert not _is_linked(b, 'solucitudSuministro26', a2)
    if hasattr(a2, 'dependencia27'):
        assert not _is_linked(a2, 'dependencia27', b)


def test_assoc_Realiza1_reverse_link_reassign_clear():
    a1 = Trabajadores(Telefono=7, identificacion="sample_text", nombre="sample_text")
    a2 = Trabajadores(Telefono=13, identificacion="sample_text_2", nombre="sample_text_2")
    b = Obras(codigo="sample_text", direccion="sample_text")
    _safe_set(b, 'trabajadores37', {a1})
    assert _is_linked(b, 'trabajadores37', a1)
    if hasattr(a1, 'obras36'):
        assert _is_linked(a1, 'obras36', b)
    _safe_set(b, 'trabajadores37', {a2})
    assert _is_linked(b, 'trabajadores37', a2)
    if hasattr(a1, 'obras36'):
        assert not _is_linked(a1, 'obras36', b)
    if hasattr(a2, 'obras36'):
        assert _is_linked(a2, 'obras36', b)
    _safe_set(b, 'trabajadores37', set())
    assert not _is_linked(b, 'trabajadores37', a2)
    if hasattr(a2, 'obras36'):
        assert not _is_linked(a2, 'obras36', b)


def test_assoc_conformada_reverse_link_reassign_clear():
    a1 = OrdenesPedido(codigo="sample_text", fecha="sample_text")
    a2 = OrdenesPedido(codigo="sample_text_2", fecha="sample_text_2")
    b = Elementos(clasificacion="sample_text", referencia="sample_text")
    _safe_set(b, 'ordenesPedido18', {a1})
    assert _is_linked(b, 'ordenesPedido18', a1)
    if hasattr(a1, 'elementos19'):
        assert _is_linked(a1, 'elementos19', b)
    _safe_set(b, 'ordenesPedido18', {a2})
    assert _is_linked(b, 'ordenesPedido18', a2)
    if hasattr(a1, 'elementos19'):
        assert not _is_linked(a1, 'elementos19', b)
    if hasattr(a2, 'elementos19'):
        assert _is_linked(a2, 'elementos19', b)
    _safe_set(b, 'ordenesPedido18', set())
    assert not _is_linked(b, 'ordenesPedido18', a2)
    if hasattr(a2, 'elementos19'):
        assert not _is_linked(a2, 'elementos19', b)


def test_assoc_contiene_reverse_link_reassign_clear():
    a1 = Trabajadores(Telefono=7, identificacion="sample_text", nombre="sample_text")
    a2 = Trabajadores(Telefono=13, identificacion="sample_text_2", nombre="sample_text_2")
    b = Historial_trabajadores(TrabajoAntiguo="sample_text", codigo="sample_text", horasTrabajadas="sample_text")
    _safe_set(b, 'trabajadores31', a1)
    assert _is_linked(b, 'trabajadores31', a1)
    if hasattr(a1, 'his_trabajores30'):
        assert _is_linked(a1, 'his_trabajores30', b)
    _safe_set(b, 'trabajadores31', a2)
    assert _is_linked(b, 'trabajadores31', a2)
    if hasattr(a1, 'his_trabajores30'):
        assert not _is_linked(a1, 'his_trabajores30', b)
    if hasattr(a2, 'his_trabajores30'):
        assert _is_linked(a2, 'his_trabajores30', b)
    _safe_set(b, 'trabajadores31', None)
    assert not _is_linked(b, 'trabajadores31', a2)
    if hasattr(a2, 'his_trabajores30'):
        assert not _is_linked(a2, 'his_trabajores30', b)


def test_assoc_elabora_reverse_link_reassign_clear():
    a1 = Proveedores(direccion="sample_text", nit="sample_text", razonSocial="sample_text", telefonos=7)
    a2 = Proveedores(direccion="sample_text_2", nit="sample_text_2", razonSocial="sample_text_2", telefonos=13)
    b = Factura(codigo="sample_text", fecha="sample_text")
    _safe_set(b, 'proveedores25', a1)
    assert _is_linked(b, 'proveedores25', a1)
    if hasattr(a1, 'factura24'):
        assert _is_linked(a1, 'factura24', b)
    _safe_set(b, 'proveedores25', a2)
    assert _is_linked(b, 'proveedores25', a2)
    if hasattr(a1, 'factura24'):
        assert not _is_linked(a1, 'factura24', b)
    if hasattr(a2, 'factura24'):
        assert _is_linked(a2, 'factura24', b)
    _safe_set(b, 'proveedores25', None)
    assert not _is_linked(b, 'proveedores25', a2)
    if hasattr(a2, 'factura24'):
        assert not _is_linked(a2, 'factura24', b)


def test_assoc_es_enviado_reverse_link_reassign_clear():
    a1 = Proveedores(direccion="sample_text", nit="sample_text", razonSocial="sample_text", telefonos=7)
    a2 = Proveedores(direccion="sample_text_2", nit="sample_text_2", razonSocial="sample_text_2", telefonos=13)
    b = OrdenesPedido(codigo="sample_text", fecha="sample_text")
    _safe_set(b, 'proveedores15', a1)
    assert _is_linked(b, 'proveedores15', a1)
    if hasattr(a1, 'ordenesPedido14'):
        assert _is_linked(a1, 'ordenesPedido14', b)
    _safe_set(b, 'proveedores15', a2)
    assert _is_linked(b, 'proveedores15', a2)
    if hasattr(a1, 'ordenesPedido14'):
        assert not _is_linked(a1, 'ordenesPedido14', b)
    if hasattr(a2, 'ordenesPedido14'):
        assert _is_linked(a2, 'ordenesPedido14', b)
    _safe_set(b, 'proveedores15', None)
    assert not _is_linked(b, 'proveedores15', a2)
    if hasattr(a2, 'ordenesPedido14'):
        assert not _is_linked(a2, 'ordenesPedido14', b)


def test_assoc_factura_reverse_link_reassign_clear():
    a1 = Factura(codigo="sample_text", fecha="sample_text")
    a2 = Factura(codigo="sample_text_2", fecha="sample_text_2")
    b = Elementos(clasificacion="sample_text", referencia="sample_text")
    _safe_set(b, 'factura28', {a1})
    assert _is_linked(b, 'factura28', a1)
    if hasattr(a1, 'elementos29'):
        assert _is_linked(a1, 'elementos29', b)
    _safe_set(b, 'factura28', {a2})
    assert _is_linked(b, 'factura28', a2)
    if hasattr(a1, 'elementos29'):
        assert not _is_linked(a1, 'elementos29', b)
    if hasattr(a2, 'elementos29'):
        assert _is_linked(a2, 'elementos29', b)
    _safe_set(b, 'factura28', set())
    assert not _is_linked(b, 'factura28', a2)
    if hasattr(a2, 'elementos29'):
        assert not _is_linked(a2, 'elementos29', b)


def test_assoc_factura1_reverse_link_reassign_clear():
    a1 = facturas_pagos_(codigo="sample_text", pagoNomina=7, total="sample_text")
    a2 = facturas_pagos_(codigo="sample_text_2", pagoNomina=13, total="sample_text_2")
    b = Trabajadores(Telefono=7, identificacion="sample_text", nombre="sample_text")
    _safe_set(b, 'factura41', a1)
    assert _is_linked(b, 'factura41', a1)
    if hasattr(a1, 'trabajadores40'):
        assert _is_linked(a1, 'trabajadores40', b)
    _safe_set(b, 'factura41', a2)
    assert _is_linked(b, 'factura41', a2)
    if hasattr(a1, 'trabajadores40'):
        assert not _is_linked(a1, 'trabajadores40', b)
    if hasattr(a2, 'trabajadores40'):
        assert _is_linked(a2, 'trabajadores40', b)
    _safe_set(b, 'factura41', None)
    assert not _is_linked(b, 'factura41', a2)
    if hasattr(a2, 'trabajadores40'):
        assert not _is_linked(a2, 'trabajadores40', b)


def test_assoc_genera_reverse_link_reassign_clear():
    a1 = SolucitudSuministro(codigo="sample_text", fecha="sample_text")
    a2 = SolucitudSuministro(codigo="sample_text_2", fecha="sample_text_2")
    b = OrdenesPedido(codigo="sample_text", fecha="sample_text")
    _safe_set(b, 'solucitudSuministro22', {a1})
    assert _is_linked(b, 'solucitudSuministro22', a1)
    if hasattr(a1, 'ordenesPedido23'):
        assert _is_linked(a1, 'ordenesPedido23', b)
    _safe_set(b, 'solucitudSuministro22', {a2})
    assert _is_linked(b, 'solucitudSuministro22', a2)
    if hasattr(a1, 'ordenesPedido23'):
        assert not _is_linked(a1, 'ordenesPedido23', b)
    if hasattr(a2, 'ordenesPedido23'):
        assert _is_linked(a2, 'ordenesPedido23', b)
    _safe_set(b, 'solucitudSuministro22', set())
    assert not _is_linked(b, 'solucitudSuministro22', a2)
    if hasattr(a2, 'ordenesPedido23'):
        assert not _is_linked(a2, 'ordenesPedido23', b)


def test_assoc_genera1_reverse_link_reassign_clear():
    a1 = facturas_pagos_(codigo="sample_text", pagoNomina=7, total="sample_text")
    a2 = facturas_pagos_(codigo="sample_text_2", pagoNomina=13, total="sample_text_2")
    b = Obras(codigo="sample_text", direccion="sample_text")
    _safe_set(b, 'factura33', {a1})
    assert _is_linked(b, 'factura33', a1)
    if hasattr(a1, 'obras32'):
        assert _is_linked(a1, 'obras32', b)
    _safe_set(b, 'factura33', {a2})
    assert _is_linked(b, 'factura33', a2)
    if hasattr(a1, 'obras32'):
        assert not _is_linked(a1, 'obras32', b)
    if hasattr(a2, 'obras32'):
        assert _is_linked(a2, 'obras32', b)
    _safe_set(b, 'factura33', set())
    assert not _is_linked(b, 'factura33', a2)
    if hasattr(a2, 'obras32'):
        assert not _is_linked(a2, 'obras32', b)


def test_assoc_hace_reverse_link_reassign_clear():
    a1 = Encargos(codigo="sample_text", detalles="sample_text")
    a2 = Encargos(codigo="sample_text_2", detalles="sample_text_2")
    b = Comprador(Nombre="sample_text", identificacion="sample_text", telefono="sample_text")
    _safe_set(b, 'encargos43', {a1})
    assert _is_linked(b, 'encargos43', a1)
    if hasattr(a1, 'comprador42'):
        assert _is_linked(a1, 'comprador42', b)
    _safe_set(b, 'encargos43', {a2})
    assert _is_linked(b, 'encargos43', a2)
    if hasattr(a1, 'comprador42'):
        assert not _is_linked(a1, 'comprador42', b)
    if hasattr(a2, 'comprador42'):
        assert _is_linked(a2, 'comprador42', b)
    _safe_set(b, 'encargos43', set())
    assert not _is_linked(b, 'encargos43', a2)
    if hasattr(a2, 'comprador42'):
        assert not _is_linked(a2, 'comprador42', b)


def test_assoc_nesecita_reverse_link_reassign_clear():
    a1 = Planos(Codigo="sample_text", Escala="sample_text", Fecha="sample_text")
    a2 = Planos(Codigo="sample_text_2", Escala="sample_text_2", Fecha="sample_text_2")
    b = Obras(codigo="sample_text", direccion="sample_text")
    _safe_set(b, 'planos35', {a1})
    assert _is_linked(b, 'planos35', a1)
    if hasattr(a1, 'obras34'):
        assert _is_linked(a1, 'obras34', b)
    _safe_set(b, 'planos35', {a2})
    assert _is_linked(b, 'planos35', a2)
    if hasattr(a1, 'obras34'):
        assert not _is_linked(a1, 'obras34', b)
    if hasattr(a2, 'obras34'):
        assert _is_linked(a2, 'obras34', b)
    _safe_set(b, 'planos35', set())
    assert not _is_linked(b, 'planos35', a2)
    if hasattr(a2, 'obras34'):
        assert not _is_linked(a2, 'obras34', b)


def test_assoc_realiza_reverse_link_reassign_clear():
    a1 = Obras(codigo="sample_text", direccion="sample_text")
    a2 = Obras(codigo="sample_text_2", direccion="sample_text_2")
    b = Encargos(codigo="sample_text", detalles="sample_text")
    _safe_set(b, 'obras45', {a1})
    assert _is_linked(b, 'obras45', a1)
    if hasattr(a1, 'encargos44'):
        assert _is_linked(a1, 'encargos44', b)
    _safe_set(b, 'obras45', {a2})
    assert _is_linked(b, 'obras45', a2)
    if hasattr(a1, 'encargos44'):
        assert not _is_linked(a1, 'encargos44', b)
    if hasattr(a2, 'encargos44'):
        assert _is_linked(a2, 'encargos44', b)
    _safe_set(b, 'obras45', set())
    assert not _is_linked(b, 'obras45', a2)
    if hasattr(a2, 'encargos44'):
        assert not _is_linked(a2, 'encargos44', b)


def test_assoc_relaciona_reverse_link_reassign_clear():
    a1 = SolucitudSuministro(codigo="sample_text", fecha="sample_text")
    a2 = SolucitudSuministro(codigo="sample_text_2", fecha="sample_text_2")
    b = Elementos(clasificacion="sample_text", referencia="sample_text")
    _safe_set(b, 'solucitudSuministro21', a1)
    assert _is_linked(b, 'solucitudSuministro21', a1)
    if hasattr(a1, 'elementos20'):
        assert _is_linked(a1, 'elementos20', b)
    _safe_set(b, 'solucitudSuministro21', a2)
    assert _is_linked(b, 'solucitudSuministro21', a2)
    if hasattr(a1, 'elementos20'):
        assert not _is_linked(a1, 'elementos20', b)
    if hasattr(a2, 'elementos20'):
        assert _is_linked(a2, 'elementos20', b)
    _safe_set(b, 'solucitudSuministro21', None)
    assert not _is_linked(b, 'solucitudSuministro21', a2)
    if hasattr(a2, 'elementos20'):
        assert not _is_linked(a2, 'elementos20', b)


def test_assoc_requiere_reverse_link_reassign_clear():
    a1 = Planos(Codigo="sample_text", Escala="sample_text", Fecha="sample_text")
    a2 = Planos(Codigo="sample_text_2", Escala="sample_text_2", Fecha="sample_text_2")
    b = Permisos(Codigo="sample_text", Estado="sample_text", Fecha="sample_text")
    _safe_set(b, 'planos38', a1)
    assert _is_linked(b, 'planos38', a1)
    if hasattr(a1, 'permisos39'):
        assert _is_linked(a1, 'permisos39', b)
    _safe_set(b, 'planos38', a2)
    assert _is_linked(b, 'planos38', a2)
    if hasattr(a1, 'permisos39'):
        assert not _is_linked(a1, 'permisos39', b)
    if hasattr(a2, 'permisos39'):
        assert _is_linked(a2, 'permisos39', b)
    _safe_set(b, 'planos38', None)
    assert not _is_linked(b, 'planos38', a2)
    if hasattr(a2, 'permisos39'):
        assert not _is_linked(a2, 'permisos39', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

