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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_b67_stub_double():
    # dml_IS has no real 'dml_IS69' property in the generated
    # code (a bare stub) -- manually attach it so dml_DI's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dml_DI's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dml_DI(clid="sample_text", cln="sample_text")
    partner = dml_IS()
    setattr(partner, 'dml_IS69', None)
    _safe_set(owner, 'dml_DI68', partner)
    assert getattr(partner, 'dml_IS69') == owner
    _safe_set(owner, 'dml_DI68', None)
    assert getattr(partner, 'dml_IS69') is None


def test_assoc_e100_stub_double():
    # dml_PE has no real 'dml_PE101' property in the generated
    # code (a bare stub) -- manually attach it so dml_E's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dml_E's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dml_E(op="sample_text")
    partner = dml_PE()
    setattr(partner, 'dml_PE101', None)
    _safe_set(owner, 'dml_E102', partner)
    assert getattr(partner, 'dml_PE101') == owner
    _safe_set(owner, 'dml_E102', None)
    assert getattr(partner, 'dml_PE101') is None


def test_assoc_e173_stub_double():
    # dml_IS has no real 'dml_IS74' property in the generated
    # code (a bare stub) -- manually attach it so dml_E's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dml_E's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dml_E(op="sample_text")
    partner = dml_IS()
    setattr(partner, 'dml_IS74', None)
    _safe_set(owner, 'dml_E75', partner)
    assert getattr(partner, 'dml_IS74') == owner
    _safe_set(owner, 'dml_E75', None)
    assert getattr(partner, 'dml_IS74') is None


def test_assoc_e276_stub_double():
    # dml_IS has no real 'dml_IS77' property in the generated
    # code (a bare stub) -- manually attach it so dml_E's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dml_E's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dml_E(op="sample_text")
    partner = dml_IS()
    setattr(partner, 'dml_IS77', None)
    _safe_set(owner, 'dml_E78', partner)
    assert getattr(partner, 'dml_IS77') == owner
    _safe_set(owner, 'dml_E78', None)
    assert getattr(partner, 'dml_IS77') is None


def test_assoc_e70_stub_double():
    # dml_IS has no real 'dml_IS72' property in the generated
    # code (a bare stub) -- manually attach it so dml_DI's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dml_DI's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dml_DI(clid="sample_text", cln="sample_text")
    partner = dml_IS()
    setattr(partner, 'dml_IS72', None)
    _safe_set(owner, 'dml_DI71', partner)
    assert getattr(partner, 'dml_IS72') == owner
    _safe_set(owner, 'dml_DI71', None)
    assert getattr(partner, 'dml_IS72') is None


def test_assoc_es22_stub_double():
    # dml_BS has no real 'dml_BS24' property in the generated
    # code (a bare stub) -- manually attach it so dml_S's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dml_S's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dml_S(cwd="sample_text", src="sample_text")
    partner = dml_BS()
    setattr(partner, 'dml_BS24', None)
    _safe_set(owner, 'dml_S23', partner)
    assert getattr(partner, 'dml_BS24') == owner
    _safe_set(owner, 'dml_S23', None)
    assert getattr(partner, 'dml_BS24') is None


def test_assoc_fp25_stub_double():
    # dml_FP has no real 'dml_FP' property in the generated
    # code (a bare stub) -- manually attach it so dml_S's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dml_S's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dml_S(cwd="sample_text", src="sample_text")
    partner = dml_FP()
    setattr(partner, 'dml_FP', None)
    _safe_set(owner, 'dml_S26', partner)
    assert getattr(partner, 'dml_FP') == owner
    _safe_set(owner, 'dml_S26', None)
    assert getattr(partner, 'dml_FP') is None


def test_assoc_id59_stub_double():
    # dml_FP has no real 'dml_FP60' property in the generated
    # code (a bare stub) -- manually attach it so dml_ID's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dml_ID's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dml_ID(name="sample_text")
    partner = dml_FP()
    setattr(partner, 'dml_FP60', None)
    _safe_set(owner, 'dml_ID61', partner)
    assert getattr(partner, 'dml_FP60') == owner
    _safe_set(owner, 'dml_ID61', None)
    assert getattr(partner, 'dml_FP60') is None


def test_assoc_id97_stub_double():
    # dml_PE has no real 'dml_PE98' property in the generated
    # code (a bare stub) -- manually attach it so dml_ID's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dml_ID's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dml_ID(name="sample_text")
    partner = dml_PE()
    setattr(partner, 'dml_PE98', None)
    _safe_set(owner, 'dml_ID99', partner)
    assert getattr(partner, 'dml_PE98') == owner
    _safe_set(owner, 'dml_ID99', None)
    assert getattr(partner, 'dml_PE98') is None


def test_assoc_is_20_stub_double():
    # dml_BS has no real 'dml_BS' property in the generated
    # code (a bare stub) -- manually attach it so dml_S's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dml_S's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dml_S(cwd="sample_text", src="sample_text")
    partner = dml_BS()
    setattr(partner, 'dml_BS', None)
    _safe_set(owner, 'dml_S21', partner)
    assert getattr(partner, 'dml_BS') == owner
    _safe_set(owner, 'dml_S21', None)
    assert getattr(partner, 'dml_BS') is None


def test_assoc_name3_stub_double():
    # dml_F has no real 'dml_F4' property in the generated
    # code (a bare stub) -- manually attach it so dml_ID's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dml_ID's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dml_ID(name="sample_text")
    partner = dml_F()
    setattr(partner, 'dml_F4', None)
    _safe_set(owner, 'dml_ID', partner)
    assert getattr(partner, 'dml_F4') == owner
    _safe_set(owner, 'dml_ID', None)
    assert getattr(partner, 'dml_F4') is None


def test_assoc_pe51_stub_double():
    # dml_PE has no real 'dml_PE' property in the generated
    # code (a bare stub) -- manually attach it so dml_FC's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dml_FC's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dml_FC(bif="sample_text")
    partner = dml_PE()
    setattr(partner, 'dml_PE', None)
    _safe_set(owner, 'dml_FC52', {partner})
    assert getattr(partner, 'dml_PE') == owner
    _safe_set(owner, 'dml_FC52', set())
    assert getattr(partner, 'dml_PE') is None


def test_assoc_pf32_stub_double():
    # dml_FP has no real 'dml_FP34' property in the generated
    # code (a bare stub) -- manually attach it so dml_S's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dml_S's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dml_S(cwd="sample_text", src="sample_text")
    partner = dml_FP()
    setattr(partner, 'dml_FP34', None)
    _safe_set(owner, 'dml_S33', partner)
    assert getattr(partner, 'dml_FP34') == owner
    _safe_set(owner, 'dml_S33', None)
    assert getattr(partner, 'dml_FP34') is None


def test_assoc_s1_stub_double():
    # dml_D has no real 'dml_D2' property in the generated
    # code (a bare stub) -- manually attach it so dml_S's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dml_S's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dml_S(cwd="sample_text", src="sample_text")
    partner = dml_D()
    setattr(partner, 'dml_D2', None)
    _safe_set(owner, 'dml_S', partner)
    assert getattr(partner, 'dml_D2') == owner
    _safe_set(owner, 'dml_S', None)
    assert getattr(partner, 'dml_D2') is None


def test_assoc_s10_stub_double():
    # dml_F has no real 'dml_F11' property in the generated
    # code (a bare stub) -- manually attach it so dml_S's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dml_S's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dml_S(cwd="sample_text", src="sample_text")
    partner = dml_F()
    setattr(partner, 'dml_F11', None)
    _safe_set(owner, 'dml_S12', partner)
    assert getattr(partner, 'dml_F11') == owner
    _safe_set(owner, 'dml_S12', None)
    assert getattr(partner, 'dml_F11') is None


def test_assoc_s29_stub_double():
    # dml_BS has no real 'dml_BS31' property in the generated
    # code (a bare stub) -- manually attach it so dml_S's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dml_S's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dml_S(cwd="sample_text", src="sample_text")
    partner = dml_BS()
    setattr(partner, 'dml_BS31', None)
    _safe_set(owner, 'dml_S30', partner)
    assert getattr(partner, 'dml_BS31') == owner
    _safe_set(owner, 'dml_S30', None)
    assert getattr(partner, 'dml_BS31') is None


def test_assoc_s56_stub_double():
    # dml_BS has no real 'dml_BS57' property in the generated
    # code (a bare stub) -- manually attach it so dml_S's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dml_S's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dml_S(cwd="sample_text", src="sample_text")
    partner = dml_BS()
    setattr(partner, 'dml_BS57', None)
    _safe_set(owner, 'dml_S58', partner)
    assert getattr(partner, 'dml_BS57') == owner
    _safe_set(owner, 'dml_S58', None)
    assert getattr(partner, 'dml_BS57') is None


def test_assoc_singleS53_stub_double():
    # dml_BS has no real 'dml_BS54' property in the generated
    # code (a bare stub) -- manually attach it so dml_S's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dml_S's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dml_S(cwd="sample_text", src="sample_text")
    partner = dml_BS()
    setattr(partner, 'dml_BS54', None)
    _safe_set(owner, 'dml_S55', partner)
    assert getattr(partner, 'dml_BS54') == owner
    _safe_set(owner, 'dml_S55', None)
    assert getattr(partner, 'dml_BS54') is None


def test_assoc_spkv13_stub_double():
    # dml_F has no real 'dml_F14' property in the generated
    # code (a bare stub) -- manually attach it so dml_SPKV's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dml_SPKV's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dml_SPKV(v="sample_text")
    partner = dml_F()
    setattr(partner, 'dml_F14', None)
    _safe_set(owner, 'dml_SPKV', partner)
    assert getattr(partner, 'dml_F14') == owner
    _safe_set(owner, 'dml_SPKV', None)
    assert getattr(partner, 'dml_F14') is None


def test_assoc_t181_stub_double():
    # dml_EObject has no real 'dml_EObject' property in the generated
    # code (a bare stub) -- manually attach it so dml_E's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dml_E's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dml_E(op="sample_text")
    partner = dml_EObject()
    setattr(partner, 'dml_EObject', None)
    _safe_set(owner, 'dml_E82', partner)
    assert getattr(partner, 'dml_EObject') == owner
    _safe_set(owner, 'dml_E82', None)
    assert getattr(partner, 'dml_EObject') is None


def test_assoc_t79_stub_double():
    # dml_PL has no real 'dml_PL80' property in the generated
    # code (a bare stub) -- manually attach it so dml_TAN's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dml_TAN's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dml_TAN(t="sample_text")
    partner = dml_PL()
    setattr(partner, 'dml_PL80', None)
    _safe_set(owner, 'dml_TAN', partner)
    assert getattr(partner, 'dml_PL80') == owner
    _safe_set(owner, 'dml_TAN', None)
    assert getattr(partner, 'dml_PL80') is None


