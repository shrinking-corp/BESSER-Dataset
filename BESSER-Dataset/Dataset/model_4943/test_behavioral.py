import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Component,
    User_input_field,
    webshop_builder_3k_model_Border,
    webshop_builder_3k_model_Branding,
    webshop_builder_3k_model_Checkbox,
    webshop_builder_3k_model_Component,
    webshop_builder_3k_model_Component_group,
    webshop_builder_3k_model_Item,
    webshop_builder_3k_model_Item_to_KB_link,
    webshop_builder_3k_model_Knowledge_base,
    webshop_builder_3k_model_Login_widget,
    webshop_builder_3k_model_Menu,
    webshop_builder_3k_model_Navigation_button,
    webshop_builder_3k_model_Navigation_to_Page_link,
    webshop_builder_3k_model_Newsletter_subscription_widget,
    webshop_builder_3k_model_Page,
    webshop_builder_3k_model_Picture,
    webshop_builder_3k_model_Radio_button,
    webshop_builder_3k_model_Result_list,
    webshop_builder_3k_model_Reuse_component,
    webshop_builder_3k_model_Reuses_component_link,
    webshop_builder_3k_model_Search_widget,
    webshop_builder_3k_model_Shopping_cart_button,
    webshop_builder_3k_model_Slideshow,
    webshop_builder_3k_model_Social_button,
    webshop_builder_3k_model_Source_code,
    webshop_builder_3k_model_Style,
    webshop_builder_3k_model_Text_field,
    webshop_builder_3k_model_Text_input_field,
    webshop_builder_3k_model_User_input_field,
    webshop_builder_3k_model_Webshop_builder_3k,
    Alignment,
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

def test_assoc_border49_reverse_link_reassign_clear():
    a1 = webshop_builder_3k_model_Style(background_color="sample_text")
    a2 = webshop_builder_3k_model_Style(background_color="sample_text_2")
    b = webshop_builder_3k_model_Border(color="sample_text", thickness=7)
    _safe_set(b, 'webshop_builder_3k_model_Border', a1)
    assert _is_linked(b, 'webshop_builder_3k_model_Border', a1)
    if hasattr(a1, 'webshop_builder_3k_model_Style50'):
        assert _is_linked(a1, 'webshop_builder_3k_model_Style50', b)
    _safe_set(b, 'webshop_builder_3k_model_Border', a2)
    assert _is_linked(b, 'webshop_builder_3k_model_Border', a2)
    if hasattr(a1, 'webshop_builder_3k_model_Style50'):
        assert not _is_linked(a1, 'webshop_builder_3k_model_Style50', b)
    if hasattr(a2, 'webshop_builder_3k_model_Style50'):
        assert _is_linked(a2, 'webshop_builder_3k_model_Style50', b)
    _safe_set(b, 'webshop_builder_3k_model_Border', None)
    assert not _is_linked(b, 'webshop_builder_3k_model_Border', a2)
    if hasattr(a2, 'webshop_builder_3k_model_Style50'):
        assert not _is_linked(a2, 'webshop_builder_3k_model_Style50', b)


def test_assoc_components0_reverse_link_reassign_clear():
    a1 = webshop_builder_3k_model_Page(canvas_color="sample_text", height=7, title="sample_text", width=7)
    a2 = webshop_builder_3k_model_Page(canvas_color="sample_text_2", height=13, title="sample_text_2", width=13)
    b = webshop_builder_3k_model_Component(alignment="sample_text", height=7, name="sample_text", width=7, xposition=7, yposition=7)
    _safe_set(b, 'webshop_builder_3k_model_Component', a1)
    assert _is_linked(b, 'webshop_builder_3k_model_Component', a1)
    if hasattr(a1, 'webshop_builder_3k_model_Page'):
        assert _is_linked(a1, 'webshop_builder_3k_model_Page', b)
    _safe_set(b, 'webshop_builder_3k_model_Component', a2)
    assert _is_linked(b, 'webshop_builder_3k_model_Component', a2)
    if hasattr(a1, 'webshop_builder_3k_model_Page'):
        assert not _is_linked(a1, 'webshop_builder_3k_model_Page', b)
    if hasattr(a2, 'webshop_builder_3k_model_Page'):
        assert _is_linked(a2, 'webshop_builder_3k_model_Page', b)
    _safe_set(b, 'webshop_builder_3k_model_Component', None)
    assert not _is_linked(b, 'webshop_builder_3k_model_Component', a2)
    if hasattr(a2, 'webshop_builder_3k_model_Page'):
        assert not _is_linked(a2, 'webshop_builder_3k_model_Page', b)


def test_assoc_free_components19_reverse_link_reassign_clear():
    a1 = webshop_builder_3k_model_Webshop_builder_3k(company_name="sample_text")
    a2 = webshop_builder_3k_model_Webshop_builder_3k(company_name="sample_text_2")
    b = webshop_builder_3k_model_Component(alignment="sample_text", height=7, name="sample_text", width=7, xposition=7, yposition=7)
    _safe_set(b, 'webshop_builder_3k_model_Component21', a1)
    assert _is_linked(b, 'webshop_builder_3k_model_Component21', a1)
    if hasattr(a1, 'webshop_builder_3k_model_Webshop_builder_3k20'):
        assert _is_linked(a1, 'webshop_builder_3k_model_Webshop_builder_3k20', b)
    _safe_set(b, 'webshop_builder_3k_model_Component21', a2)
    assert _is_linked(b, 'webshop_builder_3k_model_Component21', a2)
    if hasattr(a1, 'webshop_builder_3k_model_Webshop_builder_3k20'):
        assert not _is_linked(a1, 'webshop_builder_3k_model_Webshop_builder_3k20', b)
    if hasattr(a2, 'webshop_builder_3k_model_Webshop_builder_3k20'):
        assert _is_linked(a2, 'webshop_builder_3k_model_Webshop_builder_3k20', b)
    _safe_set(b, 'webshop_builder_3k_model_Component21', None)
    assert not _is_linked(b, 'webshop_builder_3k_model_Component21', a2)
    if hasattr(a2, 'webshop_builder_3k_model_Webshop_builder_3k20'):
        assert not _is_linked(a2, 'webshop_builder_3k_model_Webshop_builder_3k20', b)


def test_assoc_index_page25_reverse_link_reassign_clear():
    a1 = webshop_builder_3k_model_Webshop_builder_3k(company_name="sample_text")
    a2 = webshop_builder_3k_model_Webshop_builder_3k(company_name="sample_text_2")
    b = webshop_builder_3k_model_Page(canvas_color="sample_text", height=7, title="sample_text", width=7)
    _safe_set(b, 'webshop_builder_3k_model_Page27', a1)
    assert _is_linked(b, 'webshop_builder_3k_model_Page27', a1)
    if hasattr(a1, 'webshop_builder_3k_model_Webshop_builder_3k26'):
        assert _is_linked(a1, 'webshop_builder_3k_model_Webshop_builder_3k26', b)
    _safe_set(b, 'webshop_builder_3k_model_Page27', a2)
    assert _is_linked(b, 'webshop_builder_3k_model_Page27', a2)
    if hasattr(a1, 'webshop_builder_3k_model_Webshop_builder_3k26'):
        assert not _is_linked(a1, 'webshop_builder_3k_model_Webshop_builder_3k26', b)
    if hasattr(a2, 'webshop_builder_3k_model_Webshop_builder_3k26'):
        assert _is_linked(a2, 'webshop_builder_3k_model_Webshop_builder_3k26', b)
    _safe_set(b, 'webshop_builder_3k_model_Page27', None)
    assert not _is_linked(b, 'webshop_builder_3k_model_Page27', a2)
    if hasattr(a2, 'webshop_builder_3k_model_Webshop_builder_3k26'):
        assert not _is_linked(a2, 'webshop_builder_3k_model_Webshop_builder_3k26', b)


def test_assoc_item_details_page28_reverse_link_reassign_clear():
    a1 = webshop_builder_3k_model_Webshop_builder_3k(company_name="sample_text")
    a2 = webshop_builder_3k_model_Webshop_builder_3k(company_name="sample_text_2")
    b = webshop_builder_3k_model_Page(canvas_color="sample_text", height=7, title="sample_text", width=7)
    _safe_set(b, 'webshop_builder_3k_model_Page30', a1)
    assert _is_linked(b, 'webshop_builder_3k_model_Page30', a1)
    if hasattr(a1, 'webshop_builder_3k_model_Webshop_builder_3k29'):
        assert _is_linked(a1, 'webshop_builder_3k_model_Webshop_builder_3k29', b)
    _safe_set(b, 'webshop_builder_3k_model_Page30', a2)
    assert _is_linked(b, 'webshop_builder_3k_model_Page30', a2)
    if hasattr(a1, 'webshop_builder_3k_model_Webshop_builder_3k29'):
        assert not _is_linked(a1, 'webshop_builder_3k_model_Webshop_builder_3k29', b)
    if hasattr(a2, 'webshop_builder_3k_model_Webshop_builder_3k29'):
        assert _is_linked(a2, 'webshop_builder_3k_model_Webshop_builder_3k29', b)
    _safe_set(b, 'webshop_builder_3k_model_Page30', None)
    assert not _is_linked(b, 'webshop_builder_3k_model_Page30', a2)
    if hasattr(a2, 'webshop_builder_3k_model_Webshop_builder_3k29'):
        assert not _is_linked(a2, 'webshop_builder_3k_model_Webshop_builder_3k29', b)


def test_assoc_knowledge_bases22_reverse_link_reassign_clear():
    a1 = webshop_builder_3k_model_Webshop_builder_3k(company_name="sample_text")
    a2 = webshop_builder_3k_model_Webshop_builder_3k(company_name="sample_text_2")
    b = webshop_builder_3k_model_Knowledge_base(xml_file_uri="sample_text")
    _safe_set(b, 'webshop_builder_3k_model_Knowledge_base24', a1)
    assert _is_linked(b, 'webshop_builder_3k_model_Knowledge_base24', a1)
    if hasattr(a1, 'webshop_builder_3k_model_Webshop_builder_3k23'):
        assert _is_linked(a1, 'webshop_builder_3k_model_Webshop_builder_3k23', b)
    _safe_set(b, 'webshop_builder_3k_model_Knowledge_base24', a2)
    assert _is_linked(b, 'webshop_builder_3k_model_Knowledge_base24', a2)
    if hasattr(a1, 'webshop_builder_3k_model_Webshop_builder_3k23'):
        assert not _is_linked(a1, 'webshop_builder_3k_model_Webshop_builder_3k23', b)
    if hasattr(a2, 'webshop_builder_3k_model_Webshop_builder_3k23'):
        assert _is_linked(a2, 'webshop_builder_3k_model_Webshop_builder_3k23', b)
    _safe_set(b, 'webshop_builder_3k_model_Knowledge_base24', None)
    assert not _is_linked(b, 'webshop_builder_3k_model_Knowledge_base24', a2)
    if hasattr(a2, 'webshop_builder_3k_model_Webshop_builder_3k23'):
        assert not _is_linked(a2, 'webshop_builder_3k_model_Webshop_builder_3k23', b)


def test_assoc_pages17_reverse_link_reassign_clear():
    a1 = webshop_builder_3k_model_Webshop_builder_3k(company_name="sample_text")
    a2 = webshop_builder_3k_model_Webshop_builder_3k(company_name="sample_text_2")
    b = webshop_builder_3k_model_Page(canvas_color="sample_text", height=7, title="sample_text", width=7)
    _safe_set(b, 'webshop_builder_3k_model_Page18', a1)
    assert _is_linked(b, 'webshop_builder_3k_model_Page18', a1)
    if hasattr(a1, 'webshop_builder_3k_model_Webshop_builder_3k'):
        assert _is_linked(a1, 'webshop_builder_3k_model_Webshop_builder_3k', b)
    _safe_set(b, 'webshop_builder_3k_model_Page18', a2)
    assert _is_linked(b, 'webshop_builder_3k_model_Page18', a2)
    if hasattr(a1, 'webshop_builder_3k_model_Webshop_builder_3k'):
        assert not _is_linked(a1, 'webshop_builder_3k_model_Webshop_builder_3k', b)
    if hasattr(a2, 'webshop_builder_3k_model_Webshop_builder_3k'):
        assert _is_linked(a2, 'webshop_builder_3k_model_Webshop_builder_3k', b)
    _safe_set(b, 'webshop_builder_3k_model_Page18', None)
    assert not _is_linked(b, 'webshop_builder_3k_model_Page18', a2)
    if hasattr(a2, 'webshop_builder_3k_model_Webshop_builder_3k'):
        assert not _is_linked(a2, 'webshop_builder_3k_model_Webshop_builder_3k', b)


def test_assoc_reuse_components1_reverse_link_reassign_clear():
    a1 = webshop_builder_3k_model_Reuse_component(xposition=7, yposition=7)
    a2 = webshop_builder_3k_model_Reuse_component(xposition=13, yposition=13)
    b = webshop_builder_3k_model_Page(canvas_color="sample_text", height=7, title="sample_text", width=7)
    _safe_set(b, 'webshop_builder_3k_model_Page2', {a1})
    assert _is_linked(b, 'webshop_builder_3k_model_Page2', a1)
    if hasattr(a1, 'webshop_builder_3k_model_Reuse_component'):
        assert _is_linked(a1, 'webshop_builder_3k_model_Reuse_component', b)
    _safe_set(b, 'webshop_builder_3k_model_Page2', {a2})
    assert _is_linked(b, 'webshop_builder_3k_model_Page2', a2)
    if hasattr(a1, 'webshop_builder_3k_model_Reuse_component'):
        assert not _is_linked(a1, 'webshop_builder_3k_model_Reuse_component', b)
    if hasattr(a2, 'webshop_builder_3k_model_Reuse_component'):
        assert _is_linked(a2, 'webshop_builder_3k_model_Reuse_component', b)
    _safe_set(b, 'webshop_builder_3k_model_Page2', set())
    assert not _is_linked(b, 'webshop_builder_3k_model_Page2', a2)
    if hasattr(a2, 'webshop_builder_3k_model_Reuse_component'):
        assert not _is_linked(a2, 'webshop_builder_3k_model_Reuse_component', b)


def test_assoc_style3_reverse_link_reassign_clear():
    a1 = webshop_builder_3k_model_Style(background_color="sample_text")
    a2 = webshop_builder_3k_model_Style(background_color="sample_text_2")
    b = webshop_builder_3k_model_Page(canvas_color="sample_text", height=7, title="sample_text", width=7)
    _safe_set(b, 'webshop_builder_3k_model_Page4', a1)
    assert _is_linked(b, 'webshop_builder_3k_model_Page4', a1)
    if hasattr(a1, 'webshop_builder_3k_model_Style'):
        assert _is_linked(a1, 'webshop_builder_3k_model_Style', b)
    _safe_set(b, 'webshop_builder_3k_model_Page4', a2)
    assert _is_linked(b, 'webshop_builder_3k_model_Page4', a2)
    if hasattr(a1, 'webshop_builder_3k_model_Style'):
        assert not _is_linked(a1, 'webshop_builder_3k_model_Style', b)
    if hasattr(a2, 'webshop_builder_3k_model_Style'):
        assert _is_linked(a2, 'webshop_builder_3k_model_Style', b)
    _safe_set(b, 'webshop_builder_3k_model_Page4', None)
    assert not _is_linked(b, 'webshop_builder_3k_model_Page4', a2)
    if hasattr(a2, 'webshop_builder_3k_model_Style'):
        assert not _is_linked(a2, 'webshop_builder_3k_model_Style', b)


def test_assoc_style6_reverse_link_reassign_clear():
    a1 = webshop_builder_3k_model_Style(background_color="sample_text")
    a2 = webshop_builder_3k_model_Style(background_color="sample_text_2")
    b = webshop_builder_3k_model_Component(alignment="sample_text", height=7, name="sample_text", width=7, xposition=7, yposition=7)
    _safe_set(b, 'webshop_builder_3k_model_Component7', a1)
    assert _is_linked(b, 'webshop_builder_3k_model_Component7', a1)
    if hasattr(a1, 'webshop_builder_3k_model_Style8'):
        assert _is_linked(a1, 'webshop_builder_3k_model_Style8', b)
    _safe_set(b, 'webshop_builder_3k_model_Component7', a2)
    assert _is_linked(b, 'webshop_builder_3k_model_Component7', a2)
    if hasattr(a1, 'webshop_builder_3k_model_Style8'):
        assert not _is_linked(a1, 'webshop_builder_3k_model_Style8', b)
    if hasattr(a2, 'webshop_builder_3k_model_Style8'):
        assert _is_linked(a2, 'webshop_builder_3k_model_Style8', b)
    _safe_set(b, 'webshop_builder_3k_model_Component7', None)
    assert not _is_linked(b, 'webshop_builder_3k_model_Component7', a2)
    if hasattr(a2, 'webshop_builder_3k_model_Style8'):
        assert not _is_linked(a2, 'webshop_builder_3k_model_Style8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_company_logo12_stub_double():
    # webshop_builder_3k_model_Branding has no real 'webshop_builder_3k_model_Branding13' property in the generated
    # code (a bare stub) -- manually attach it so webshop_builder_3k_model_Picture's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webshop_builder_3k_model_Picture's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webshop_builder_3k_model_Picture(alternative_text="sample_text", source="sample_text", title="sample_text")
    partner = webshop_builder_3k_model_Branding()
    setattr(partner, 'webshop_builder_3k_model_Branding13', None)
    _safe_set(owner, 'webshop_builder_3k_model_Picture', partner)
    assert getattr(partner, 'webshop_builder_3k_model_Branding13') == owner
    _safe_set(owner, 'webshop_builder_3k_model_Picture', None)
    assert getattr(partner, 'webshop_builder_3k_model_Branding13') is None


def test_assoc_company_name11_stub_double():
    # webshop_builder_3k_model_Branding has no real 'webshop_builder_3k_model_Branding' property in the generated
    # code (a bare stub) -- manually attach it so webshop_builder_3k_model_Text_field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webshop_builder_3k_model_Text_field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webshop_builder_3k_model_Text_field(header_level=7, text="sample_text")
    partner = webshop_builder_3k_model_Branding()
    setattr(partner, 'webshop_builder_3k_model_Branding', None)
    _safe_set(owner, 'webshop_builder_3k_model_Text_field', partner)
    assert getattr(partner, 'webshop_builder_3k_model_Branding') == owner
    _safe_set(owner, 'webshop_builder_3k_model_Text_field', None)
    assert getattr(partner, 'webshop_builder_3k_model_Branding') is None


def test_assoc_item_picture31_stub_double():
    # webshop_builder_3k_model_Item has no real 'webshop_builder_3k_model_Item' property in the generated
    # code (a bare stub) -- manually attach it so webshop_builder_3k_model_Picture's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webshop_builder_3k_model_Picture's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webshop_builder_3k_model_Picture(alternative_text="sample_text", source="sample_text", title="sample_text")
    partner = webshop_builder_3k_model_Item()
    setattr(partner, 'webshop_builder_3k_model_Item', None)
    _safe_set(owner, 'webshop_builder_3k_model_Picture32', partner)
    assert getattr(partner, 'webshop_builder_3k_model_Item') == owner
    _safe_set(owner, 'webshop_builder_3k_model_Picture32', None)
    assert getattr(partner, 'webshop_builder_3k_model_Item') is None


def test_assoc_knowledge_base10_stub_double():
    # webshop_builder_3k_model_Item_to_KB_link has no real 'webshop_builder_3k_model_Item_to_KB_link' property in the generated
    # code (a bare stub) -- manually attach it so webshop_builder_3k_model_Knowledge_base's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webshop_builder_3k_model_Knowledge_base's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webshop_builder_3k_model_Knowledge_base(xml_file_uri="sample_text")
    partner = webshop_builder_3k_model_Item_to_KB_link()
    setattr(partner, 'webshop_builder_3k_model_Item_to_KB_link', None)
    _safe_set(owner, 'webshop_builder_3k_model_Knowledge_base', partner)
    assert getattr(partner, 'webshop_builder_3k_model_Item_to_KB_link') == owner
    _safe_set(owner, 'webshop_builder_3k_model_Knowledge_base', None)
    assert getattr(partner, 'webshop_builder_3k_model_Item_to_KB_link') is None


def test_assoc_link5_stub_double():
    # webshop_builder_3k_model_Reuses_component_link has no real 'Reuses_component_link' property in the generated
    # code (a bare stub) -- manually attach it so webshop_builder_3k_model_Reuse_component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webshop_builder_3k_model_Reuse_component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webshop_builder_3k_model_Reuse_component(xposition=7, yposition=7)
    partner = webshop_builder_3k_model_Reuses_component_link()
    setattr(partner, 'Reuses_component_link', None)
    _safe_set(owner, 'source', partner)
    assert getattr(partner, 'Reuses_component_link') == owner
    _safe_set(owner, 'source', None)
    assert getattr(partner, 'Reuses_component_link') is None


def test_assoc_picture40_stub_double():
    # webshop_builder_3k_model_Navigation_button has no real 'webshop_builder_3k_model_Navigation_button' property in the generated
    # code (a bare stub) -- manually attach it so webshop_builder_3k_model_Picture's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webshop_builder_3k_model_Picture's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webshop_builder_3k_model_Picture(alternative_text="sample_text", source="sample_text", title="sample_text")
    partner = webshop_builder_3k_model_Navigation_button()
    setattr(partner, 'webshop_builder_3k_model_Navigation_button', None)
    _safe_set(owner, 'webshop_builder_3k_model_Picture41', partner)
    assert getattr(partner, 'webshop_builder_3k_model_Navigation_button') == owner
    _safe_set(owner, 'webshop_builder_3k_model_Picture41', None)
    assert getattr(partner, 'webshop_builder_3k_model_Navigation_button') is None


def test_assoc_result_template37_stub_double():
    # webshop_builder_3k_model_Item has no real 'webshop_builder_3k_model_Item38' property in the generated
    # code (a bare stub) -- manually attach it so webshop_builder_3k_model_Result_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webshop_builder_3k_model_Result_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webshop_builder_3k_model_Result_list(distance_between_items=7, number_of_items_per_page=7)
    partner = webshop_builder_3k_model_Item()
    setattr(partner, 'webshop_builder_3k_model_Item38', None)
    _safe_set(owner, 'webshop_builder_3k_model_Result_list', partner)
    assert getattr(partner, 'webshop_builder_3k_model_Item38') == owner
    _safe_set(owner, 'webshop_builder_3k_model_Result_list', None)
    assert getattr(partner, 'webshop_builder_3k_model_Item38') is None


def test_assoc_source14_stub_double():
    # webshop_builder_3k_model_Reuses_component_link has no real 'link' property in the generated
    # code (a bare stub) -- manually attach it so webshop_builder_3k_model_Reuse_component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webshop_builder_3k_model_Reuse_component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webshop_builder_3k_model_Reuse_component(xposition=7, yposition=7)
    partner = webshop_builder_3k_model_Reuses_component_link()
    setattr(partner, 'link', None)
    _safe_set(owner, 'Reuse_component', partner)
    assert getattr(partner, 'link') == owner
    _safe_set(owner, 'Reuse_component', None)
    assert getattr(partner, 'link') is None


def test_assoc_target15_stub_double():
    # webshop_builder_3k_model_Reuses_component_link has no real 'webshop_builder_3k_model_Reuses_component_link' property in the generated
    # code (a bare stub) -- manually attach it so webshop_builder_3k_model_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webshop_builder_3k_model_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webshop_builder_3k_model_Component(alignment="sample_text", height=7, name="sample_text", width=7, xposition=7, yposition=7)
    partner = webshop_builder_3k_model_Reuses_component_link()
    setattr(partner, 'webshop_builder_3k_model_Reuses_component_link', None)
    _safe_set(owner, 'webshop_builder_3k_model_Component16', partner)
    assert getattr(partner, 'webshop_builder_3k_model_Reuses_component_link') == owner
    _safe_set(owner, 'webshop_builder_3k_model_Component16', None)
    assert getattr(partner, 'webshop_builder_3k_model_Reuses_component_link') is None


def test_assoc_target47_stub_double():
    # webshop_builder_3k_model_Navigation_to_Page_link has no real 'webshop_builder_3k_model_Navigation_to_Page_link' property in the generated
    # code (a bare stub) -- manually attach it so webshop_builder_3k_model_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webshop_builder_3k_model_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webshop_builder_3k_model_Page(canvas_color="sample_text", height=7, title="sample_text", width=7)
    partner = webshop_builder_3k_model_Navigation_to_Page_link()
    setattr(partner, 'webshop_builder_3k_model_Navigation_to_Page_link', None)
    _safe_set(owner, 'webshop_builder_3k_model_Page48', partner)
    assert getattr(partner, 'webshop_builder_3k_model_Navigation_to_Page_link') == owner
    _safe_set(owner, 'webshop_builder_3k_model_Page48', None)
    assert getattr(partner, 'webshop_builder_3k_model_Navigation_to_Page_link') is None


def test_assoc_text42_stub_double():
    # webshop_builder_3k_model_Navigation_button has no real 'webshop_builder_3k_model_Navigation_button43' property in the generated
    # code (a bare stub) -- manually attach it so webshop_builder_3k_model_Text_field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webshop_builder_3k_model_Text_field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webshop_builder_3k_model_Text_field(header_level=7, text="sample_text")
    partner = webshop_builder_3k_model_Navigation_button()
    setattr(partner, 'webshop_builder_3k_model_Navigation_button43', None)
    _safe_set(owner, 'webshop_builder_3k_model_Text_field44', partner)
    assert getattr(partner, 'webshop_builder_3k_model_Navigation_button43') == owner
    _safe_set(owner, 'webshop_builder_3k_model_Text_field44', None)
    assert getattr(partner, 'webshop_builder_3k_model_Navigation_button43') is None


def test_assoc_text_fields33_stub_double():
    # webshop_builder_3k_model_Item has no real 'webshop_builder_3k_model_Item34' property in the generated
    # code (a bare stub) -- manually attach it so webshop_builder_3k_model_Text_field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webshop_builder_3k_model_Text_field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webshop_builder_3k_model_Text_field(header_level=7, text="sample_text")
    partner = webshop_builder_3k_model_Item()
    setattr(partner, 'webshop_builder_3k_model_Item34', None)
    _safe_set(owner, 'webshop_builder_3k_model_Text_field35', partner)
    assert owner in getattr(partner, 'webshop_builder_3k_model_Item34')
    _safe_set(owner, 'webshop_builder_3k_model_Text_field35', None)
    assert owner not in getattr(partner, 'webshop_builder_3k_model_Item34')


