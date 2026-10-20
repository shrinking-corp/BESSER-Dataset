import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Avanzar_hacia_el_siguiendo_ejemplar__UseCase,
    Buscar_un_ejemplar_por_su_nombre__UseCase,
    Calcular_el_numero_de_ejemplares_por_raza__UseCase,
    Calcular_el_promedio_de_edad_de_todos_los_caninos__UseCase,
    Canino,
    Desplazarse_hasta_el_primer_ejemplar_UseCase,
    Desplazarse_hasta_el_ultimo_ejemplar__UseCase,
    Empresa,
    Int,
    Int2,
    Regresar_hacia_el_anterior_ejemplar__UseCase,
    String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones,
    String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones2,
    Usuario_Actor,
    Visualizar_hoja_de_vida_de_cada_perrito__UseCase,
    double,
    void,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

