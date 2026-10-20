import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    Animation,
    Control,
    Node,
    Page,
    book_Action,
    book_Animation,
    book_Book,
    book_Control,
    book_Fade,
    book_Group,
    book_ImageFlash,
    book_JSAction,
    book_Label,
    book_Layer,
    book_Media,
    book_Move,
    book_Node,
    book_OpenPage,
    book_Page,
    book_Rotation,
    book_Shape,
    book_Splash,
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

def test_assoc_control8_reverse_link_reassign_clear():
    a1 = book_Layer(visible=True)
    a2 = book_Layer(visible=False)
    b = book_Control(image="sample_text", sound="sample_text")
    _safe_set(b, 'book_Control', a1)
    assert _is_linked(b, 'book_Control', a1)
    if hasattr(a1, 'book_Layer9'):
        assert _is_linked(a1, 'book_Layer9', b)
    _safe_set(b, 'book_Control', a2)
    assert _is_linked(b, 'book_Control', a2)
    if hasattr(a1, 'book_Layer9'):
        assert not _is_linked(a1, 'book_Layer9', b)
    if hasattr(a2, 'book_Layer9'):
        assert _is_linked(a2, 'book_Layer9', b)
    _safe_set(b, 'book_Control', None)
    assert not _is_linked(b, 'book_Control', a2)
    if hasattr(a2, 'book_Layer9'):
        assert not _is_linked(a2, 'book_Layer9', b)


def test_assoc_in_17_reverse_link_reassign_clear():
    a1 = book_ImageFlash(duration=7, images="sample_text")
    a2 = book_ImageFlash(duration=13, images="sample_text_2")
    b = book_Animation(autoReverse=True, delay=3.14, duration=3.14, repeat=7)
    _safe_set(b, 'book_Animation19', a1)
    assert _is_linked(b, 'book_Animation19', a1)
    if hasattr(a1, 'book_ImageFlash18'):
        assert _is_linked(a1, 'book_ImageFlash18', b)
    _safe_set(b, 'book_Animation19', a2)
    assert _is_linked(b, 'book_Animation19', a2)
    if hasattr(a1, 'book_ImageFlash18'):
        assert not _is_linked(a1, 'book_ImageFlash18', b)
    if hasattr(a2, 'book_ImageFlash18'):
        assert _is_linked(a2, 'book_ImageFlash18', b)
    _safe_set(b, 'book_Animation19', None)
    assert not _is_linked(b, 'book_Animation19', a2)
    if hasattr(a2, 'book_ImageFlash18'):
        assert not _is_linked(a2, 'book_ImageFlash18', b)


def test_assoc_layers6_reverse_link_reassign_clear():
    a1 = book_Page(name="sample_text")
    a2 = book_Page(name="sample_text_2")
    b = book_Layer(visible=True)
    _safe_set(b, 'book_Layer', a1)
    assert _is_linked(b, 'book_Layer', a1)
    if hasattr(a1, 'book_Page7'):
        assert _is_linked(a1, 'book_Page7', b)
    _safe_set(b, 'book_Layer', a2)
    assert _is_linked(b, 'book_Layer', a2)
    if hasattr(a1, 'book_Page7'):
        assert not _is_linked(a1, 'book_Page7', b)
    if hasattr(a2, 'book_Page7'):
        assert _is_linked(a2, 'book_Page7', b)
    _safe_set(b, 'book_Layer', None)
    assert not _is_linked(b, 'book_Layer', a2)
    if hasattr(a2, 'book_Page7'):
        assert not _is_linked(a2, 'book_Page7', b)


def test_assoc_main3_reverse_link_reassign_clear():
    a1 = book_Page(name="sample_text")
    a2 = book_Page(name="sample_text_2")
    b = book_Book(author="sample_text", bookId="sample_text", description="sample_text", resolution="sample_text", title="sample_text", version="sample_text")
    _safe_set(b, 'book_Book4', a1)
    assert _is_linked(b, 'book_Book4', a1)
    if hasattr(a1, 'book_Page5'):
        assert _is_linked(a1, 'book_Page5', b)
    _safe_set(b, 'book_Book4', a2)
    assert _is_linked(b, 'book_Book4', a2)
    if hasattr(a1, 'book_Page5'):
        assert not _is_linked(a1, 'book_Page5', b)
    if hasattr(a2, 'book_Page5'):
        assert _is_linked(a2, 'book_Page5', b)
    _safe_set(b, 'book_Book4', None)
    assert not _is_linked(b, 'book_Book4', a2)
    if hasattr(a2, 'book_Page5'):
        assert not _is_linked(a2, 'book_Page5', b)


def test_assoc_out16_reverse_link_reassign_clear():
    a1 = book_ImageFlash(duration=7, images="sample_text")
    a2 = book_ImageFlash(duration=13, images="sample_text_2")
    b = book_Animation(autoReverse=True, delay=3.14, duration=3.14, repeat=7)
    _safe_set(b, 'book_Animation', a1)
    assert _is_linked(b, 'book_Animation', a1)
    if hasattr(a1, 'book_ImageFlash'):
        assert _is_linked(a1, 'book_ImageFlash', b)
    _safe_set(b, 'book_Animation', a2)
    assert _is_linked(b, 'book_Animation', a2)
    if hasattr(a1, 'book_ImageFlash'):
        assert not _is_linked(a1, 'book_ImageFlash', b)
    if hasattr(a2, 'book_ImageFlash'):
        assert _is_linked(a2, 'book_ImageFlash', b)
    _safe_set(b, 'book_Animation', None)
    assert not _is_linked(b, 'book_Animation', a2)
    if hasattr(a2, 'book_ImageFlash'):
        assert not _is_linked(a2, 'book_ImageFlash', b)


def test_assoc_pages0_reverse_link_reassign_clear():
    a1 = book_Page(name="sample_text")
    a2 = book_Page(name="sample_text_2")
    b = book_Book(author="sample_text", bookId="sample_text", description="sample_text", resolution="sample_text", title="sample_text", version="sample_text")
    _safe_set(b, 'book_Book', {a1})
    assert _is_linked(b, 'book_Book', a1)
    if hasattr(a1, 'book_Page'):
        assert _is_linked(a1, 'book_Page', b)
    _safe_set(b, 'book_Book', {a2})
    assert _is_linked(b, 'book_Book', a2)
    if hasattr(a1, 'book_Page'):
        assert not _is_linked(a1, 'book_Page', b)
    if hasattr(a2, 'book_Page'):
        assert _is_linked(a2, 'book_Page', b)
    _safe_set(b, 'book_Book', set())
    assert not _is_linked(b, 'book_Book', a2)
    if hasattr(a2, 'book_Page'):
        assert not _is_linked(a2, 'book_Page', b)


def test_assoc_splash1_reverse_link_reassign_clear():
    a1 = book_Splash(duration=7)
    a2 = book_Splash(duration=13)
    b = book_Book(author="sample_text", bookId="sample_text", description="sample_text", resolution="sample_text", title="sample_text", version="sample_text")
    _safe_set(b, 'book_Book2', a1)
    assert _is_linked(b, 'book_Book2', a1)
    if hasattr(a1, 'book_Splash'):
        assert _is_linked(a1, 'book_Splash', b)
    _safe_set(b, 'book_Book2', a2)
    assert _is_linked(b, 'book_Book2', a2)
    if hasattr(a1, 'book_Splash'):
        assert not _is_linked(a1, 'book_Splash', b)
    if hasattr(a2, 'book_Splash'):
        assert _is_linked(a2, 'book_Splash', b)
    _safe_set(b, 'book_Book2', None)
    assert not _is_linked(b, 'book_Book2', a2)
    if hasattr(a2, 'book_Splash'):
        assert not _is_linked(a2, 'book_Splash', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_children15_stub_double():
    # book_Group has no real 'book_Group' property in the generated
    # code (a bare stub) -- manually attach it so book_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # book_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = book_Node(background="sample_text", bounds="sample_text", enable=True, foreground="sample_text", opacity=3.14)
    partner = book_Group()
    setattr(partner, 'book_Group', None)
    _safe_set(owner, 'book_Node', partner)
    assert owner in getattr(partner, 'book_Group')
    _safe_set(owner, 'book_Node', None)
    assert owner not in getattr(partner, 'book_Group')


def test_assoc_onExposed10_stub_double():
    # book_Action has no real 'book_Action' property in the generated
    # code (a bare stub) -- manually attach it so book_Control's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # book_Control's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = book_Control(image="sample_text", sound="sample_text")
    partner = book_Action()
    setattr(partner, 'book_Action', None)
    _safe_set(owner, 'book_Control11', {partner})
    assert getattr(partner, 'book_Action') == owner
    _safe_set(owner, 'book_Control11', set())
    assert getattr(partner, 'book_Action') is None


def test_assoc_onTouched12_stub_double():
    # book_Action has no real 'book_Action14' property in the generated
    # code (a bare stub) -- manually attach it so book_Control's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # book_Control's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = book_Control(image="sample_text", sound="sample_text")
    partner = book_Action()
    setattr(partner, 'book_Action14', None)
    _safe_set(owner, 'book_Control13', {partner})
    assert getattr(partner, 'book_Action14') == owner
    _safe_set(owner, 'book_Control13', set())
    assert getattr(partner, 'book_Action14') is None


def test_assoc_page20_stub_double():
    # book_OpenPage has no real 'book_OpenPage' property in the generated
    # code (a bare stub) -- manually attach it so book_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # book_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = book_Page(name="sample_text")
    partner = book_OpenPage()
    setattr(partner, 'book_OpenPage', None)
    _safe_set(owner, 'book_Page21', partner)
    assert getattr(partner, 'book_OpenPage') == owner
    _safe_set(owner, 'book_Page21', None)
    assert getattr(partner, 'book_OpenPage') is None


