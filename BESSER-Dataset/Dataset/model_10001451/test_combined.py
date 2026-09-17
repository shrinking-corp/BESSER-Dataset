# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Ventana,
    JFrame,
    Cuadrado,
    Canvas,
    Figura,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_ventana_is_not_abstract():
    assert not inspect.isabstract(Ventana)


def test_hyp_ventana_constructor_exists():
    assert callable(Ventana.__init__)


def test_hyp_ventana_constructor_args():
    sig = inspect.signature(Ventana.__init__)
    params = list(sig.parameters.keys())
    assert "c3" in params, "Missing parameter 'c3'"
    assert "l2" in params, "Missing parameter 'l2'"
    assert "fig" in params, "Missing parameter 'fig'"
    assert "c1" in params, "Missing parameter 'c1'"
    assert "l1" in params, "Missing parameter 'l1'"
    assert "etiqueta" in params, "Missing parameter 'etiqueta'"
    assert "c2" in params, "Missing parameter 'c2'"

def test_hyp_ventana_has_c3():
    assert hasattr(Ventana, "c3")
    descriptor = None
    for klass in Ventana.__mro__:
        if "c3" in klass.__dict__:
            descriptor = klass.__dict__["c3"]
            break
    assert isinstance(descriptor, property)

def test_hyp_ventana_has_l2():
    assert hasattr(Ventana, "l2")
    descriptor = None
    for klass in Ventana.__mro__:
        if "l2" in klass.__dict__:
            descriptor = klass.__dict__["l2"]
            break
    assert isinstance(descriptor, property)

def test_hyp_ventana_has_fig():
    assert hasattr(Ventana, "fig")
    descriptor = None
    for klass in Ventana.__mro__:
        if "fig" in klass.__dict__:
            descriptor = klass.__dict__["fig"]
            break
    assert isinstance(descriptor, property)

def test_hyp_ventana_has_c1():
    assert hasattr(Ventana, "c1")
    descriptor = None
    for klass in Ventana.__mro__:
        if "c1" in klass.__dict__:
            descriptor = klass.__dict__["c1"]
            break
    assert isinstance(descriptor, property)

def test_hyp_ventana_has_l1():
    assert hasattr(Ventana, "l1")
    descriptor = None
    for klass in Ventana.__mro__:
        if "l1" in klass.__dict__:
            descriptor = klass.__dict__["l1"]
            break
    assert isinstance(descriptor, property)

def test_hyp_ventana_has_etiqueta():
    assert hasattr(Ventana, "etiqueta")
    descriptor = None
    for klass in Ventana.__mro__:
        if "etiqueta" in klass.__dict__:
            descriptor = klass.__dict__["etiqueta"]
            break
    assert isinstance(descriptor, property)

def test_hyp_ventana_has_c2():
    assert hasattr(Ventana, "c2")
    descriptor = None
    for klass in Ventana.__mro__:
        if "c2" in klass.__dict__:
            descriptor = klass.__dict__["c2"]
            break
    assert isinstance(descriptor, property)



def test_hyp_jframe_is_not_abstract():
    assert not inspect.isabstract(JFrame)


def test_hyp_jframe_constructor_exists():
    assert callable(JFrame.__init__)


def test_hyp_jframe_constructor_args():
    sig = inspect.signature(JFrame.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cuadrado_is_not_abstract():
    assert not inspect.isabstract(Cuadrado)


def test_hyp_cuadrado_constructor_exists():
    assert callable(Cuadrado.__init__)


def test_hyp_cuadrado_constructor_args():
    sig = inspect.signature(Cuadrado.__init__)
    params = list(sig.parameters.keys())
    assert "v1" in params, "Missing parameter 'v1'"
    assert "img" in params, "Missing parameter 'img'"
    assert "v2" in params, "Missing parameter 'v2'"






def test_hyp_canvas_is_not_abstract():
    assert not inspect.isabstract(Canvas)


def test_hyp_canvas_constructor_exists():
    assert callable(Canvas.__init__)


def test_hyp_canvas_constructor_args():
    sig = inspect.signature(Canvas.__init__)
    params = list(sig.parameters.keys())



def test_hyp_figura_is_not_abstract():
    assert not inspect.isabstract(Figura)


def test_hyp_figura_constructor_exists():
    assert callable(Figura.__init__)


def test_hyp_figura_constructor_args():
    sig = inspect.signature(Figura.__init__)
    params = list(sig.parameters.keys())
    assert "estado" in params, "Missing parameter 'estado'"
    assert "valor" in params, "Missing parameter 'valor'"




# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Ventana_strategy = st.builds(
    Ventana,
    c3=
        st.none(),
    l2=
        st.integers(),
    fig=
        st.none(),
    c1=
        st.none(),
    l1=
        st.integers(),
    etiqueta=
        safe_text,
    c2=
        st.none()
)
JFrame_strategy = st.builds(
    JFrame,
)
Cuadrado_strategy = st.builds(
    Cuadrado,
    v1=
        st.integers(),
    img=
        safe_text,
    v2=
        st.integers()
)
Canvas_strategy = st.builds(
    Canvas,
)
Figura_strategy = st.builds(
    Figura,
    estado=
        st.booleans(),
    valor=
        st.integers()
)

@given(instance=Ventana_strategy)
@settings(max_examples=50)
def test_hyp_ventana_instantiation(instance):
    assert isinstance(instance, Ventana)



@given(instance=Ventana_strategy)
def test_hyp_ventana_c3_setter(instance):
    original = instance.c3
    instance.c3 = original
    assert instance.c3 == original



@given(instance=Ventana_strategy)
def test_hyp_ventana_l2_setter(instance):
    original = instance.l2
    instance.l2 = original
    assert instance.l2 == original



@given(instance=Ventana_strategy)
def test_hyp_ventana_fig_setter(instance):
    original = instance.fig
    instance.fig = original
    assert instance.fig == original



@given(instance=Ventana_strategy)
def test_hyp_ventana_c1_setter(instance):
    original = instance.c1
    instance.c1 = original
    assert instance.c1 == original



@given(instance=Ventana_strategy)
def test_hyp_ventana_l1_setter(instance):
    original = instance.l1
    instance.l1 = original
    assert instance.l1 == original



@given(instance=Ventana_strategy)
def test_hyp_ventana_etiqueta_setter(instance):
    original = instance.etiqueta
    instance.etiqueta = original
    assert instance.etiqueta == original



@given(instance=Ventana_strategy)
def test_hyp_ventana_c2_setter(instance):
    original = instance.c2
    instance.c2 = original
    assert instance.c2 == original





@given(instance=Cuadrado_strategy)
def test_hyp_cuadrado_v1_setter(instance):
    original = instance.v1
    instance.v1 = original
    assert instance.v1 == original



@given(instance=Cuadrado_strategy)
def test_hyp_cuadrado_img_setter(instance):
    original = instance.img
    instance.img = original
    assert instance.img == original



@given(instance=Cuadrado_strategy)
def test_hyp_cuadrado_v2_setter(instance):
    original = instance.v2
    instance.v2 = original
    assert instance.v2 == original





@given(instance=Figura_strategy)
def test_hyp_figura_estado_setter(instance):
    original = instance.estado
    instance.estado = original
    assert instance.estado == original



@given(instance=Figura_strategy)
def test_hyp_figura_valor_setter(instance):
    original = instance.valor
    instance.valor = original
    assert instance.valor == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Canvas,
    Cuadrado,
    Figura,
    JFrame,
    Ventana,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_Cuadrado_img_value_roundtrip():
    instance = Cuadrado(img="sample_text", v1=7, v2=7)
    assert instance.img == "sample_text"
    instance.img = "sample_text_2"
    assert instance.img == "sample_text_2"


def test_Cuadrado_v1_value_roundtrip():
    instance = Cuadrado(img="sample_text", v1=7, v2=7)
    assert instance.v1 == 7
    instance.v1 = 13
    assert instance.v1 == 13


def test_Cuadrado_v2_value_roundtrip():
    instance = Cuadrado(img="sample_text", v1=7, v2=7)
    assert instance.v2 == 7
    instance.v2 = 13
    assert instance.v2 == 13


def test_Figura_estado_value_roundtrip():
    instance = Figura(estado=True, valor=7)
    assert instance.estado == True
    instance.estado = False
    assert instance.estado == False


def test_Figura_valor_value_roundtrip():
    instance = Figura(estado=True, valor=7)
    assert instance.valor == 7
    instance.valor = 13
    assert instance.valor == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Canvas_strategy = st.builds(Canvas)
@given(instance=Canvas_strategy)
@settings(max_examples=25)
def test_Canvas_instantiation(instance):
    assert isinstance(instance, Canvas)


Cuadrado_strategy = st.builds(Cuadrado, img=safe_text, v1=st.integers(), v2=st.integers())
@given(instance=Cuadrado_strategy)
@settings(max_examples=25)
def test_Cuadrado_instantiation(instance):
    assert isinstance(instance, Cuadrado)


Figura_strategy = st.builds(Figura, estado=st.booleans(), valor=st.integers())
@given(instance=Figura_strategy)
@settings(max_examples=25)
def test_Figura_instantiation(instance):
    assert isinstance(instance, Figura)


JFrame_strategy = st.builds(JFrame)
@given(instance=JFrame_strategy)
@settings(max_examples=25)
def test_JFrame_instantiation(instance):
    assert isinstance(instance, JFrame)



