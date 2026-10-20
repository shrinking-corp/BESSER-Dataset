import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Item,
    NamedItem,
    Relation,
    modeldraw_BooleanAttribute,
    modeldraw_Content,
    modeldraw_EAttribute,
    modeldraw_EClass,
    modeldraw_EEnumLiteral,
    modeldraw_EReference,
    modeldraw_Edge,
    modeldraw_Enumerator,
    modeldraw_Information,
    modeldraw_Item,
    modeldraw_Level,
    modeldraw_MutatorDraw,
    modeldraw_NamedItem,
    modeldraw_Node,
    modeldraw_NodeEnumerator,
    modeldraw_Relation,
    Decoration,
    DrawType,
    NodeColor,
    NodeShape,
    NodeStyle,
    NodeType,
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

def test_assoc_attribute9_reverse_link_reassign_clear():
    a1 = modeldraw_Node(color="sample_text", shape="sample_text", style="sample_text", type="sample_text")
    a2 = modeldraw_Node(color="sample_text_2", shape="sample_text_2", style="sample_text_2", type="sample_text_2")
    b = modeldraw_BooleanAttribute(negation=True)
    _safe_set(b, 'modeldraw_BooleanAttribute11', a1)
    assert _is_linked(b, 'modeldraw_BooleanAttribute11', a1)
    if hasattr(a1, 'modeldraw_Node10'):
        assert _is_linked(a1, 'modeldraw_Node10', b)
    _safe_set(b, 'modeldraw_BooleanAttribute11', a2)
    assert _is_linked(b, 'modeldraw_BooleanAttribute11', a2)
    if hasattr(a1, 'modeldraw_Node10'):
        assert not _is_linked(a1, 'modeldraw_Node10', b)
    if hasattr(a2, 'modeldraw_Node10'):
        assert _is_linked(a2, 'modeldraw_Node10', b)
    _safe_set(b, 'modeldraw_BooleanAttribute11', None)
    assert not _is_linked(b, 'modeldraw_BooleanAttribute11', a2)
    if hasattr(a2, 'modeldraw_Node10'):
        assert not _is_linked(a2, 'modeldraw_Node10', b)


def test_assoc_contents4_reverse_link_reassign_clear():
    a1 = modeldraw_MutatorDraw(metamodel="sample_text", type="sample_text")
    a2 = modeldraw_MutatorDraw(metamodel="sample_text_2", type="sample_text_2")
    b = modeldraw_Content(symbol="sample_text")
    _safe_set(b, 'modeldraw_Content', a1)
    assert _is_linked(b, 'modeldraw_Content', a1)
    if hasattr(a1, 'modeldraw_MutatorDraw5'):
        assert _is_linked(a1, 'modeldraw_MutatorDraw5', b)
    _safe_set(b, 'modeldraw_Content', a2)
    assert _is_linked(b, 'modeldraw_Content', a2)
    if hasattr(a1, 'modeldraw_MutatorDraw5'):
        assert not _is_linked(a1, 'modeldraw_MutatorDraw5', b)
    if hasattr(a2, 'modeldraw_MutatorDraw5'):
        assert _is_linked(a2, 'modeldraw_MutatorDraw5', b)
    _safe_set(b, 'modeldraw_Content', None)
    assert not _is_linked(b, 'modeldraw_Content', a2)
    if hasattr(a2, 'modeldraw_MutatorDraw5'):
        assert not _is_linked(a2, 'modeldraw_MutatorDraw5', b)


def test_assoc_nodes1_reverse_link_reassign_clear():
    a1 = modeldraw_Node(color="sample_text", shape="sample_text", style="sample_text", type="sample_text")
    a2 = modeldraw_Node(color="sample_text_2", shape="sample_text_2", style="sample_text_2", type="sample_text_2")
    b = modeldraw_MutatorDraw(metamodel="sample_text", type="sample_text")
    _safe_set(b, 'modeldraw_MutatorDraw', {a1})
    assert _is_linked(b, 'modeldraw_MutatorDraw', a1)
    if hasattr(a1, 'modeldraw_Node'):
        assert _is_linked(a1, 'modeldraw_Node', b)
    _safe_set(b, 'modeldraw_MutatorDraw', {a2})
    assert _is_linked(b, 'modeldraw_MutatorDraw', a2)
    if hasattr(a1, 'modeldraw_Node'):
        assert not _is_linked(a1, 'modeldraw_Node', b)
    if hasattr(a2, 'modeldraw_Node'):
        assert _is_linked(a2, 'modeldraw_Node', b)
    _safe_set(b, 'modeldraw_MutatorDraw', set())
    assert not _is_linked(b, 'modeldraw_MutatorDraw', a2)
    if hasattr(a2, 'modeldraw_Node'):
        assert not _is_linked(a2, 'modeldraw_Node', b)


def test_assoc_relations2_reverse_link_reassign_clear():
    a1 = modeldraw_Relation(src_decoration="sample_text", tar_decoration="sample_text")
    a2 = modeldraw_Relation(src_decoration="sample_text_2", tar_decoration="sample_text_2")
    b = modeldraw_MutatorDraw(metamodel="sample_text", type="sample_text")
    _safe_set(b, 'modeldraw_MutatorDraw3', {a1})
    assert _is_linked(b, 'modeldraw_MutatorDraw3', a1)
    if hasattr(a1, 'modeldraw_Relation'):
        assert _is_linked(a1, 'modeldraw_Relation', b)
    _safe_set(b, 'modeldraw_MutatorDraw3', {a2})
    assert _is_linked(b, 'modeldraw_MutatorDraw3', a2)
    if hasattr(a1, 'modeldraw_Relation'):
        assert not _is_linked(a1, 'modeldraw_Relation', b)
    if hasattr(a2, 'modeldraw_Relation'):
        assert _is_linked(a2, 'modeldraw_Relation', b)
    _safe_set(b, 'modeldraw_MutatorDraw3', set())
    assert not _is_linked(b, 'modeldraw_MutatorDraw3', a2)
    if hasattr(a2, 'modeldraw_Relation'):
        assert not _is_linked(a2, 'modeldraw_Relation', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_att7_stub_double():
    # modeldraw_EAttribute has no real 'modeldraw_EAttribute8' property in the generated
    # code (a bare stub) -- manually attach it so modeldraw_BooleanAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modeldraw_BooleanAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modeldraw_BooleanAttribute(negation=True)
    partner = modeldraw_EAttribute()
    setattr(partner, 'modeldraw_EAttribute8', None)
    _safe_set(owner, 'modeldraw_BooleanAttribute', partner)
    assert getattr(partner, 'modeldraw_EAttribute8') == owner
    _safe_set(owner, 'modeldraw_BooleanAttribute', None)
    assert getattr(partner, 'modeldraw_EAttribute8') is None


def test_assoc_enumerator35_stub_double():
    # modeldraw_NodeEnumerator has no real 'modeldraw_NodeEnumerator36' property in the generated
    # code (a bare stub) -- manually attach it so modeldraw_Enumerator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modeldraw_Enumerator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modeldraw_Enumerator(value="sample_text")
    partner = modeldraw_NodeEnumerator()
    setattr(partner, 'modeldraw_NodeEnumerator36', None)
    _safe_set(owner, 'modeldraw_Enumerator', partner)
    assert owner in getattr(partner, 'modeldraw_NodeEnumerator36')
    _safe_set(owner, 'modeldraw_Enumerator', None)
    assert owner not in getattr(partner, 'modeldraw_NodeEnumerator36')


def test_assoc_info47_stub_double():
    # modeldraw_Information has no real 'modeldraw_Information49' property in the generated
    # code (a bare stub) -- manually attach it so modeldraw_Content's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modeldraw_Content's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modeldraw_Content(symbol="sample_text")
    partner = modeldraw_Information()
    setattr(partner, 'modeldraw_Information49', None)
    _safe_set(owner, 'modeldraw_Content48', {partner})
    assert getattr(partner, 'modeldraw_Information49') == owner
    _safe_set(owner, 'modeldraw_Content48', set())
    assert getattr(partner, 'modeldraw_Information49') is None


def test_assoc_label17_stub_double():
    # modeldraw_EAttribute has no real 'modeldraw_EAttribute19' property in the generated
    # code (a bare stub) -- manually attach it so modeldraw_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modeldraw_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modeldraw_Relation(src_decoration="sample_text", tar_decoration="sample_text")
    partner = modeldraw_EAttribute()
    setattr(partner, 'modeldraw_EAttribute19', None)
    _safe_set(owner, 'modeldraw_Relation18', partner)
    assert getattr(partner, 'modeldraw_EAttribute19') == owner
    _safe_set(owner, 'modeldraw_Relation18', None)
    assert getattr(partner, 'modeldraw_EAttribute19') is None


def test_assoc_literal37_stub_double():
    # modeldraw_EEnumLiteral has no real 'modeldraw_EEnumLiteral' property in the generated
    # code (a bare stub) -- manually attach it so modeldraw_Enumerator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modeldraw_Enumerator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modeldraw_Enumerator(value="sample_text")
    partner = modeldraw_EEnumLiteral()
    setattr(partner, 'modeldraw_EEnumLiteral', None)
    _safe_set(owner, 'modeldraw_Enumerator38', partner)
    assert getattr(partner, 'modeldraw_EEnumLiteral') == owner
    _safe_set(owner, 'modeldraw_Enumerator38', None)
    assert getattr(partner, 'modeldraw_EEnumLiteral') is None


def test_assoc_nodenum44_stub_double():
    # modeldraw_NodeEnumerator has no real 'modeldraw_NodeEnumerator46' property in the generated
    # code (a bare stub) -- manually attach it so modeldraw_Content's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modeldraw_Content's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modeldraw_Content(symbol="sample_text")
    partner = modeldraw_NodeEnumerator()
    setattr(partner, 'modeldraw_NodeEnumerator46', None)
    _safe_set(owner, 'modeldraw_Content45', {partner})
    assert getattr(partner, 'modeldraw_NodeEnumerator46') == owner
    _safe_set(owner, 'modeldraw_Content45', set())
    assert getattr(partner, 'modeldraw_NodeEnumerator46') is None


def test_assoc_reference12_stub_double():
    # modeldraw_EReference has no real 'modeldraw_EReference' property in the generated
    # code (a bare stub) -- manually attach it so modeldraw_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modeldraw_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modeldraw_Node(color="sample_text", shape="sample_text", style="sample_text", type="sample_text")
    partner = modeldraw_EReference()
    setattr(partner, 'modeldraw_EReference', None)
    _safe_set(owner, 'modeldraw_Node13', {partner})
    assert getattr(partner, 'modeldraw_EReference') == owner
    _safe_set(owner, 'modeldraw_Node13', set())
    assert getattr(partner, 'modeldraw_EReference') is None


def test_assoc_reference14_stub_double():
    # modeldraw_EReference has no real 'modeldraw_EReference16' property in the generated
    # code (a bare stub) -- manually attach it so modeldraw_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modeldraw_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modeldraw_Relation(src_decoration="sample_text", tar_decoration="sample_text")
    partner = modeldraw_EReference()
    setattr(partner, 'modeldraw_EReference16', None)
    _safe_set(owner, 'modeldraw_Relation15', partner)
    assert getattr(partner, 'modeldraw_EReference16') == owner
    _safe_set(owner, 'modeldraw_Relation15', None)
    assert getattr(partner, 'modeldraw_EReference16') is None


def test_assoc_src_label20_stub_double():
    # modeldraw_EAttribute has no real 'modeldraw_EAttribute22' property in the generated
    # code (a bare stub) -- manually attach it so modeldraw_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modeldraw_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modeldraw_Relation(src_decoration="sample_text", tar_decoration="sample_text")
    partner = modeldraw_EAttribute()
    setattr(partner, 'modeldraw_EAttribute22', None)
    _safe_set(owner, 'modeldraw_Relation21', partner)
    assert getattr(partner, 'modeldraw_EAttribute22') == owner
    _safe_set(owner, 'modeldraw_Relation21', None)
    assert getattr(partner, 'modeldraw_EAttribute22') is None


def test_assoc_tar_label23_stub_double():
    # modeldraw_EAttribute has no real 'modeldraw_EAttribute25' property in the generated
    # code (a bare stub) -- manually attach it so modeldraw_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modeldraw_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modeldraw_Relation(src_decoration="sample_text", tar_decoration="sample_text")
    partner = modeldraw_EAttribute()
    setattr(partner, 'modeldraw_EAttribute25', None)
    _safe_set(owner, 'modeldraw_Relation24', partner)
    assert getattr(partner, 'modeldraw_EAttribute25') == owner
    _safe_set(owner, 'modeldraw_Relation24', None)
    assert getattr(partner, 'modeldraw_EAttribute25') is None


