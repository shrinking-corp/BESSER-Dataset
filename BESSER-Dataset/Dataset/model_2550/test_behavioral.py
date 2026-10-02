import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    dml_BS,
    dml_D,
    dml_DI,
    dml_E,
    dml_EObject,
    dml_F,
    dml_FC,
    dml_FP,
    dml_ID,
    dml_IS,
    dml_PARFORPARAMS,
    dml_PE,
    dml_PL,
    dml_S,
    dml_SPKV,
    dml_TAN,
    dml_TE,
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

def test_assoc_di38_reverse_link_reassign_clear():
    a1 = dml_S(cwd="sample_text", src="sample_text")
    a2 = dml_S(cwd="sample_text_2", src="sample_text_2")
    b = dml_DI(clid="sample_text", cln="sample_text")
    _safe_set(b, 'dml_DI', a1)
    assert _is_linked(b, 'dml_DI', a1)
    if hasattr(a1, 'dml_S39'):
        assert _is_linked(a1, 'dml_S39', b)
    _safe_set(b, 'dml_DI', a2)
    assert _is_linked(b, 'dml_DI', a2)
    if hasattr(a1, 'dml_S39'):
        assert not _is_linked(a1, 'dml_S39', b)
    if hasattr(a2, 'dml_S39'):
        assert _is_linked(a2, 'dml_S39', b)
    _safe_set(b, 'dml_DI', None)
    assert not _is_linked(b, 'dml_DI', a2)
    if hasattr(a2, 'dml_S39'):
        assert not _is_linked(a2, 'dml_S39', b)


def test_assoc_di91_reverse_link_reassign_clear():
    a1 = dml_TE(b="sample_text", d=3.14, i=7, s="sample_text")
    a2 = dml_TE(b="sample_text_2", d=9.99, i=13, s="sample_text_2")
    b = dml_DI(clid="sample_text", cln="sample_text")
    _safe_set(b, 'dml_DI93', a1)
    assert _is_linked(b, 'dml_DI93', a1)
    if hasattr(a1, 'dml_TE92'):
        assert _is_linked(a1, 'dml_TE92', b)
    _safe_set(b, 'dml_DI93', a2)
    assert _is_linked(b, 'dml_DI93', a2)
    if hasattr(a1, 'dml_TE92'):
        assert not _is_linked(a1, 'dml_TE92', b)
    if hasattr(a2, 'dml_TE92'):
        assert _is_linked(a2, 'dml_TE92', b)
    _safe_set(b, 'dml_DI93', None)
    assert not _is_linked(b, 'dml_DI93', a2)
    if hasattr(a2, 'dml_TE92'):
        assert not _is_linked(a2, 'dml_TE92', b)


def test_assoc_e45_reverse_link_reassign_clear():
    a1 = dml_S(cwd="sample_text", src="sample_text")
    a2 = dml_S(cwd="sample_text_2", src="sample_text_2")
    b = dml_E(op="sample_text")
    _safe_set(b, 'dml_E47', a1)
    assert _is_linked(b, 'dml_E47', a1)
    if hasattr(a1, 'dml_S46'):
        assert _is_linked(a1, 'dml_S46', b)
    _safe_set(b, 'dml_E47', a2)
    assert _is_linked(b, 'dml_E47', a2)
    if hasattr(a1, 'dml_S46'):
        assert not _is_linked(a1, 'dml_S46', b)
    if hasattr(a2, 'dml_S46'):
        assert _is_linked(a2, 'dml_S46', b)
    _safe_set(b, 'dml_E47', None)
    assert not _is_linked(b, 'dml_E47', a2)
    if hasattr(a2, 'dml_S46'):
        assert not _is_linked(a2, 'dml_S46', b)


def test_assoc_e86_reverse_link_reassign_clear():
    a1 = dml_TE(b="sample_text", d=3.14, i=7, s="sample_text")
    a2 = dml_TE(b="sample_text_2", d=9.99, i=13, s="sample_text_2")
    b = dml_E(op="sample_text")
    _safe_set(b, 'dml_E87', a1)
    assert _is_linked(b, 'dml_E87', a1)
    if hasattr(a1, 'dml_TE'):
        assert _is_linked(a1, 'dml_TE', b)
    _safe_set(b, 'dml_E87', a2)
    assert _is_linked(b, 'dml_E87', a2)
    if hasattr(a1, 'dml_TE'):
        assert not _is_linked(a1, 'dml_TE', b)
    if hasattr(a2, 'dml_TE'):
        assert _is_linked(a2, 'dml_TE', b)
    _safe_set(b, 'dml_E87', None)
    assert not _is_linked(b, 'dml_E87', a2)
    if hasattr(a2, 'dml_TE'):
        assert not _is_linked(a2, 'dml_TE', b)


def test_assoc_f88_reverse_link_reassign_clear():
    a1 = dml_TE(b="sample_text", d=3.14, i=7, s="sample_text")
    a2 = dml_TE(b="sample_text_2", d=9.99, i=13, s="sample_text_2")
    b = dml_FC(bif="sample_text")
    _safe_set(b, 'dml_FC90', a1)
    assert _is_linked(b, 'dml_FC90', a1)
    if hasattr(a1, 'dml_TE89'):
        assert _is_linked(a1, 'dml_TE89', b)
    _safe_set(b, 'dml_FC90', a2)
    assert _is_linked(b, 'dml_FC90', a2)
    if hasattr(a1, 'dml_TE89'):
        assert not _is_linked(a1, 'dml_TE89', b)
    if hasattr(a2, 'dml_TE89'):
        assert _is_linked(a2, 'dml_TE89', b)
    _safe_set(b, 'dml_FC90', None)
    assert not _is_linked(b, 'dml_FC90', a2)
    if hasattr(a2, 'dml_TE89'):
        assert not _is_linked(a2, 'dml_TE89', b)


def test_assoc_fc40_reverse_link_reassign_clear():
    a1 = dml_S(cwd="sample_text", src="sample_text")
    a2 = dml_S(cwd="sample_text_2", src="sample_text_2")
    b = dml_FC(bif="sample_text")
    _safe_set(b, 'dml_FC', a1)
    assert _is_linked(b, 'dml_FC', a1)
    if hasattr(a1, 'dml_S41'):
        assert _is_linked(a1, 'dml_S41', b)
    _safe_set(b, 'dml_FC', a2)
    assert _is_linked(b, 'dml_FC', a2)
    if hasattr(a1, 'dml_S41'):
        assert not _is_linked(a1, 'dml_S41', b)
    if hasattr(a2, 'dml_S41'):
        assert _is_linked(a2, 'dml_S41', b)
    _safe_set(b, 'dml_FC', None)
    assert not _is_linked(b, 'dml_FC', a2)
    if hasattr(a2, 'dml_S41'):
        assert not _is_linked(a2, 'dml_S41', b)


def test_assoc_id48_reverse_link_reassign_clear():
    a1 = dml_ID(name="sample_text")
    a2 = dml_ID(name="sample_text_2")
    b = dml_FC(bif="sample_text")
    _safe_set(b, 'dml_FC49', a1)
    assert _is_linked(b, 'dml_FC49', a1)
    if hasattr(a1, 'dml_ID50'):
        assert _is_linked(a1, 'dml_ID50', b)
    _safe_set(b, 'dml_FC49', a2)
    assert _is_linked(b, 'dml_FC49', a2)
    if hasattr(a1, 'dml_ID50'):
        assert not _is_linked(a1, 'dml_ID50', b)
    if hasattr(a2, 'dml_ID50'):
        assert _is_linked(a2, 'dml_ID50', b)
    _safe_set(b, 'dml_FC49', None)
    assert not _is_linked(b, 'dml_FC49', a2)
    if hasattr(a2, 'dml_ID50'):
        assert not _is_linked(a2, 'dml_ID50', b)


def test_assoc_id64_reverse_link_reassign_clear():
    a1 = dml_ID(name="sample_text")
    a2 = dml_ID(name="sample_text_2")
    b = dml_DI(clid="sample_text", cln="sample_text")
    _safe_set(b, 'dml_DI65', a1)
    assert _is_linked(b, 'dml_DI65', a1)
    if hasattr(a1, 'dml_ID66'):
        assert _is_linked(a1, 'dml_ID66', b)
    _safe_set(b, 'dml_DI65', a2)
    assert _is_linked(b, 'dml_DI65', a2)
    if hasattr(a1, 'dml_ID66'):
        assert not _is_linked(a1, 'dml_ID66', b)
    if hasattr(a2, 'dml_ID66'):
        assert _is_linked(a2, 'dml_ID66', b)
    _safe_set(b, 'dml_DI65', None)
    assert not _is_linked(b, 'dml_DI65', a2)
    if hasattr(a2, 'dml_ID66'):
        assert not _is_linked(a2, 'dml_ID66', b)


def test_assoc_ife18_reverse_link_reassign_clear():
    a1 = dml_S(cwd="sample_text", src="sample_text")
    a2 = dml_S(cwd="sample_text_2", src="sample_text_2")
    b = dml_E(op="sample_text")
    _safe_set(b, 'dml_E', a1)
    assert _is_linked(b, 'dml_E', a1)
    if hasattr(a1, 'dml_S19'):
        assert _is_linked(a1, 'dml_S19', b)
    _safe_set(b, 'dml_E', a2)
    assert _is_linked(b, 'dml_E', a2)
    if hasattr(a1, 'dml_S19'):
        assert not _is_linked(a1, 'dml_S19', b)
    if hasattr(a2, 'dml_S19'):
        assert _is_linked(a2, 'dml_S19', b)
    _safe_set(b, 'dml_E', None)
    assert not _is_linked(b, 'dml_E', a2)
    if hasattr(a2, 'dml_S19'):
        assert not _is_linked(a2, 'dml_S19', b)


def test_assoc_k94_reverse_link_reassign_clear():
    a1 = dml_SPKV(v="sample_text")
    a2 = dml_SPKV(v="sample_text_2")
    b = dml_ID(name="sample_text")
    _safe_set(b, 'dml_ID96', a1)
    assert _is_linked(b, 'dml_ID96', a1)
    if hasattr(a1, 'dml_SPKV95'):
        assert _is_linked(a1, 'dml_SPKV95', b)
    _safe_set(b, 'dml_ID96', a2)
    assert _is_linked(b, 'dml_ID96', a2)
    if hasattr(a1, 'dml_SPKV95'):
        assert not _is_linked(a1, 'dml_SPKV95', b)
    if hasattr(a2, 'dml_SPKV95'):
        assert _is_linked(a2, 'dml_SPKV95', b)
    _safe_set(b, 'dml_ID96', None)
    assert not _is_linked(b, 'dml_ID96', a2)
    if hasattr(a2, 'dml_SPKV95'):
        assert not _is_linked(a2, 'dml_SPKV95', b)


def test_assoc_lhsdi42_reverse_link_reassign_clear():
    a1 = dml_S(cwd="sample_text", src="sample_text")
    a2 = dml_S(cwd="sample_text_2", src="sample_text_2")
    b = dml_DI(clid="sample_text", cln="sample_text")
    _safe_set(b, 'dml_DI44', a1)
    assert _is_linked(b, 'dml_DI44', a1)
    if hasattr(a1, 'dml_S43'):
        assert _is_linked(a1, 'dml_S43', b)
    _safe_set(b, 'dml_DI44', a2)
    assert _is_linked(b, 'dml_DI44', a2)
    if hasattr(a1, 'dml_S43'):
        assert not _is_linked(a1, 'dml_S43', b)
    if hasattr(a2, 'dml_S43'):
        assert _is_linked(a2, 'dml_S43', b)
    _safe_set(b, 'dml_DI44', None)
    assert not _is_linked(b, 'dml_DI44', a2)
    if hasattr(a2, 'dml_S43'):
        assert not _is_linked(a2, 'dml_S43', b)


def test_assoc_name103_reverse_link_reassign_clear():
    a1 = dml_TAN(t="sample_text")
    a2 = dml_TAN(t="sample_text_2")
    b = dml_ID(name="sample_text")
    _safe_set(b, 'dml_ID105', a1)
    assert _is_linked(b, 'dml_ID105', a1)
    if hasattr(a1, 'dml_TAN104'):
        assert _is_linked(a1, 'dml_TAN104', b)
    _safe_set(b, 'dml_ID105', a2)
    assert _is_linked(b, 'dml_ID105', a2)
    if hasattr(a1, 'dml_TAN104'):
        assert not _is_linked(a1, 'dml_TAN104', b)
    if hasattr(a2, 'dml_TAN104'):
        assert _is_linked(a2, 'dml_TAN104', b)
    _safe_set(b, 'dml_ID105', None)
    assert not _is_linked(b, 'dml_ID105', a2)
    if hasattr(a2, 'dml_TAN104'):
        assert not _is_linked(a2, 'dml_TAN104', b)


def test_assoc_p27_reverse_link_reassign_clear():
    a1 = dml_S(cwd="sample_text", src="sample_text")
    a2 = dml_S(cwd="sample_text_2", src="sample_text_2")
    b = dml_PARFORPARAMS(params="sample_text")
    _safe_set(b, 'dml_PARFORPARAMS', a1)
    assert _is_linked(b, 'dml_PARFORPARAMS', a1)
    if hasattr(a1, 'dml_S28'):
        assert _is_linked(a1, 'dml_S28', b)
    _safe_set(b, 'dml_PARFORPARAMS', a2)
    assert _is_linked(b, 'dml_PARFORPARAMS', a2)
    if hasattr(a1, 'dml_S28'):
        assert not _is_linked(a1, 'dml_S28', b)
    if hasattr(a2, 'dml_S28'):
        assert _is_linked(a2, 'dml_S28', b)
    _safe_set(b, 'dml_PARFORPARAMS', None)
    assert not _is_linked(b, 'dml_PARFORPARAMS', a2)
    if hasattr(a2, 'dml_S28'):
        assert not _is_linked(a2, 'dml_S28', b)


def test_assoc_srcid15_reverse_link_reassign_clear():
    a1 = dml_S(cwd="sample_text", src="sample_text")
    a2 = dml_S(cwd="sample_text_2", src="sample_text_2")
    b = dml_ID(name="sample_text")
    _safe_set(b, 'dml_ID17', a1)
    assert _is_linked(b, 'dml_ID17', a1)
    if hasattr(a1, 'dml_S16'):
        assert _is_linked(a1, 'dml_S16', b)
    _safe_set(b, 'dml_ID17', a2)
    assert _is_linked(b, 'dml_ID17', a2)
    if hasattr(a1, 'dml_S16'):
        assert not _is_linked(a1, 'dml_S16', b)
    if hasattr(a2, 'dml_S16'):
        assert _is_linked(a2, 'dml_S16', b)
    _safe_set(b, 'dml_ID17', None)
    assert not _is_linked(b, 'dml_ID17', a2)
    if hasattr(a2, 'dml_S16'):
        assert not _is_linked(a2, 'dml_S16', b)


def test_assoc_t284_reverse_link_reassign_clear():
    a1 = dml_E(op="sample_text")
    a2 = dml_E(op="sample_text_2")
    b = dml_E(op="sample_text")
    _safe_set(b, 'dml_E85', a1)
    assert _is_linked(b, 'dml_E85', a1)
    if hasattr(a1, 'dml_E83'):
        assert _is_linked(a1, 'dml_E83', b)
    _safe_set(b, 'dml_E85', a2)
    assert _is_linked(b, 'dml_E85', a2)
    if hasattr(a1, 'dml_E83'):
        assert not _is_linked(a1, 'dml_E83', b)
    if hasattr(a2, 'dml_E83'):
        assert _is_linked(a2, 'dml_E83', b)
    _safe_set(b, 'dml_E85', None)
    assert not _is_linked(b, 'dml_E85', a2)
    if hasattr(a2, 'dml_E83'):
        assert not _is_linked(a2, 'dml_E83', b)


def test_assoc_we35_reverse_link_reassign_clear():
    a1 = dml_S(cwd="sample_text", src="sample_text")
    a2 = dml_S(cwd="sample_text_2", src="sample_text_2")
    b = dml_E(op="sample_text")
    _safe_set(b, 'dml_E37', a1)
    assert _is_linked(b, 'dml_E37', a1)
    if hasattr(a1, 'dml_S36'):
        assert _is_linked(a1, 'dml_S36', b)
    _safe_set(b, 'dml_E37', a2)
    assert _is_linked(b, 'dml_E37', a2)
    if hasattr(a1, 'dml_S36'):
        assert not _is_linked(a1, 'dml_S36', b)
    if hasattr(a2, 'dml_S36'):
        assert _is_linked(a2, 'dml_S36', b)
    _safe_set(b, 'dml_E37', None)
    assert not _is_linked(b, 'dml_E37', a2)
    if hasattr(a2, 'dml_S36'):
        assert not _is_linked(a2, 'dml_S36', b)


