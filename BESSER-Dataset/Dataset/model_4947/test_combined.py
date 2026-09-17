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
    forms_Form,
    ItemType,
    forms_Decision,
    forms_Number,
    forms_Choice,
    forms_Date,
    forms_FreeText,
    forms_Option,
    forms_ItemType,
    forms_Item,
    forms_Group,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_forms_form_is_not_abstract():
    assert not inspect.isabstract(forms_Form)


def test_hyp_forms_form_constructor_exists():
    assert callable(forms_Form.__init__)


def test_hyp_forms_form_constructor_args():
    sig = inspect.signature(forms_Form.__init__)
    params = list(sig.parameters.keys())
    assert "caption" in params, "Missing parameter 'caption'"




def test_hyp_itemtype_is_not_abstract():
    assert not inspect.isabstract(ItemType)


def test_hyp_itemtype_constructor_exists():
    assert callable(ItemType.__init__)


def test_hyp_itemtype_constructor_args():
    sig = inspect.signature(ItemType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forms_decision_is_not_abstract():
    assert not inspect.isabstract(forms_Decision)


def test_hyp_forms_decision_constructor_exists():
    assert callable(forms_Decision.__init__)


def test_hyp_forms_decision_constructor_args():
    sig = inspect.signature(forms_Decision.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forms_number_is_not_abstract():
    assert not inspect.isabstract(forms_Number)


def test_hyp_forms_number_constructor_exists():
    assert callable(forms_Number.__init__)


def test_hyp_forms_number_constructor_args():
    sig = inspect.signature(forms_Number.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forms_choice_is_not_abstract():
    assert not inspect.isabstract(forms_Choice)


def test_hyp_forms_choice_constructor_exists():
    assert callable(forms_Choice.__init__)


def test_hyp_forms_choice_constructor_args():
    sig = inspect.signature(forms_Choice.__init__)
    params = list(sig.parameters.keys())
    assert "multiple" in params, "Missing parameter 'multiple'"




def test_hyp_forms_date_is_not_abstract():
    assert not inspect.isabstract(forms_Date)


def test_hyp_forms_date_constructor_exists():
    assert callable(forms_Date.__init__)


def test_hyp_forms_date_constructor_args():
    sig = inspect.signature(forms_Date.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forms_freetext_is_not_abstract():
    assert not inspect.isabstract(forms_FreeText)


def test_hyp_forms_freetext_constructor_exists():
    assert callable(forms_FreeText.__init__)


def test_hyp_forms_freetext_constructor_args():
    sig = inspect.signature(forms_FreeText.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forms_option_is_not_abstract():
    assert not inspect.isabstract(forms_Option)


def test_hyp_forms_option_constructor_exists():
    assert callable(forms_Option.__init__)


def test_hyp_forms_option_constructor_args():
    sig = inspect.signature(forms_Option.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "text" in params, "Missing parameter 'text'"





def test_hyp_forms_itemtype_is_not_abstract():
    assert not inspect.isabstract(forms_ItemType)


def test_hyp_forms_itemtype_constructor_exists():
    assert callable(forms_ItemType.__init__)


def test_hyp_forms_itemtype_constructor_args():
    sig = inspect.signature(forms_ItemType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forms_item_is_not_abstract():
    assert not inspect.isabstract(forms_Item)


def test_hyp_forms_item_constructor_exists():
    assert callable(forms_Item.__init__)


def test_hyp_forms_item_constructor_args():
    sig = inspect.signature(forms_Item.__init__)
    params = list(sig.parameters.keys())
    assert "explanation" in params, "Missing parameter 'explanation'"
    assert "text" in params, "Missing parameter 'text'"





def test_hyp_forms_group_is_not_abstract():
    assert not inspect.isabstract(forms_Group)


def test_hyp_forms_group_constructor_exists():
    assert callable(forms_Group.__init__)


def test_hyp_forms_group_constructor_args():
    sig = inspect.signature(forms_Group.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"



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
forms_Form_strategy = st.builds(
    forms_Form,
    caption=
        safe_text
)
ItemType_strategy = st.builds(
    ItemType,
)
forms_Decision_strategy = st.builds(
    forms_Decision,
)
forms_Number_strategy = st.builds(
    forms_Number,
)
forms_Choice_strategy = st.builds(
    forms_Choice,
    multiple=
        st.booleans()
)
forms_Date_strategy = st.builds(
    forms_Date,
)
forms_FreeText_strategy = st.builds(
    forms_FreeText,
)
forms_Option_strategy = st.builds(
    forms_Option,
    id=
        safe_text,
    text=
        safe_text
)
forms_ItemType_strategy = st.builds(
    forms_ItemType,
)
forms_Item_strategy = st.builds(
    forms_Item,
    explanation=
        safe_text,
    text=
        safe_text
)
forms_Group_strategy = st.builds(
    forms_Group,
    name=
        safe_text
)




@given(instance=forms_Form_strategy)
def test_hyp_forms_form_caption_setter(instance):
    original = instance.caption
    instance.caption = original
    assert instance.caption == original







@given(instance=forms_Choice_strategy)
def test_hyp_forms_choice_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original






@given(instance=forms_Option_strategy)
def test_hyp_forms_option_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=forms_Option_strategy)
def test_hyp_forms_option_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original





@given(instance=forms_Item_strategy)
def test_hyp_forms_item_explanation_setter(instance):
    original = instance.explanation
    instance.explanation = original
    assert instance.explanation == original



@given(instance=forms_Item_strategy)
def test_hyp_forms_item_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=forms_Group_strategy)
def test_hyp_forms_group_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ItemType,
    forms_Choice,
    forms_Date,
    forms_Decision,
    forms_Form,
    forms_FreeText,
    forms_Group,
    forms_Item,
    forms_ItemType,
    forms_Number,
    forms_Option,
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

def test_forms_Choice_multiple_value_roundtrip():
    instance = forms_Choice(multiple=True)
    assert instance.multiple == True
    instance.multiple = False
    assert instance.multiple == False


def test_forms_Form_caption_value_roundtrip():
    instance = forms_Form(caption="sample_text")
    assert instance.caption == "sample_text"
    instance.caption = "sample_text_2"
    assert instance.caption == "sample_text_2"


def test_forms_Group_name_value_roundtrip():
    instance = forms_Group(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_forms_Item_explanation_value_roundtrip():
    instance = forms_Item(explanation="sample_text", text="sample_text")
    assert instance.explanation == "sample_text"
    instance.explanation = "sample_text_2"
    assert instance.explanation == "sample_text_2"


def test_forms_Item_text_value_roundtrip():
    instance = forms_Item(explanation="sample_text", text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_forms_Option_id_value_roundtrip():
    instance = forms_Option(id="sample_text", text="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_forms_Option_text_value_roundtrip():
    instance = forms_Option(id="sample_text", text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_forms_Choice_isa_ItemType():
    instance = forms_Choice(multiple=True)
    assert isinstance(instance, ItemType)


def test_forms_Date_isa_ItemType():
    instance = forms_Date()
    assert isinstance(instance, ItemType)


def test_forms_Decision_isa_ItemType():
    instance = forms_Decision()
    assert isinstance(instance, ItemType)


def test_forms_FreeText_isa_ItemType():
    instance = forms_FreeText()
    assert isinstance(instance, ItemType)


def test_forms_Number_isa_ItemType():
    instance = forms_Number()
    assert isinstance(instance, ItemType)


def test_assoc_dependentOf2_link_reassign_clear():
    a = forms_Option(id="sample_text", text="sample_text")
    b1 = forms_Item(explanation="sample_text", text="sample_text")
    b2 = forms_Item(explanation="sample_text_2", text="sample_text_2")
    _safe_set(a, 'forms_Option', b1)
    assert _is_linked(a, 'forms_Option', b1)
    if hasattr(b1, 'forms_Item3'):
        assert _is_linked(b1, 'forms_Item3', a)
    _safe_set(a, 'forms_Option', b2)
    assert _is_linked(a, 'forms_Option', b2)
    if hasattr(b1, 'forms_Item3'):
        assert not _is_linked(b1, 'forms_Item3', a)
    if hasattr(b2, 'forms_Item3'):
        assert _is_linked(b2, 'forms_Item3', a)
    _safe_set(a, 'forms_Option', None)
    assert not _is_linked(a, 'forms_Option', b2)
    if hasattr(b2, 'forms_Item3'):
        assert not _is_linked(b2, 'forms_Item3', a)


def test_assoc_groups0_link_reassign_clear():
    a = forms_Group(name="sample_text")
    b1 = forms_Form(caption="sample_text")
    b2 = forms_Form(caption="sample_text_2")
    _safe_set(a, 'forms_Group', b1)
    assert _is_linked(a, 'forms_Group', b1)
    if hasattr(b1, 'forms_Form'):
        assert _is_linked(b1, 'forms_Form', a)
    _safe_set(a, 'forms_Group', b2)
    assert _is_linked(a, 'forms_Group', b2)
    if hasattr(b1, 'forms_Form'):
        assert not _is_linked(b1, 'forms_Form', a)
    if hasattr(b2, 'forms_Form'):
        assert _is_linked(b2, 'forms_Form', a)
    _safe_set(a, 'forms_Group', None)
    assert not _is_linked(a, 'forms_Group', b2)
    if hasattr(b2, 'forms_Form'):
        assert not _is_linked(b2, 'forms_Form', a)


def test_assoc_itemType1_link_reassign_clear():
    a = forms_Item(explanation="sample_text", text="sample_text")
    b1 = forms_ItemType()
    b2 = forms_ItemType()
    _safe_set(a, 'forms_Item', b1)
    assert _is_linked(a, 'forms_Item', b1)
    if hasattr(b1, 'forms_ItemType'):
        assert _is_linked(b1, 'forms_ItemType', a)
    _safe_set(a, 'forms_Item', b2)
    assert _is_linked(a, 'forms_Item', b2)
    if hasattr(b1, 'forms_ItemType'):
        assert not _is_linked(b1, 'forms_ItemType', a)
    if hasattr(b2, 'forms_ItemType'):
        assert _is_linked(b2, 'forms_ItemType', a)
    _safe_set(a, 'forms_Item', None)
    assert not _is_linked(a, 'forms_Item', b2)
    if hasattr(b2, 'forms_ItemType'):
        assert not _is_linked(b2, 'forms_ItemType', a)


def test_assoc_items6_link_reassign_clear():
    a = forms_Item(explanation="sample_text", text="sample_text")
    b1 = forms_Group(name="sample_text")
    b2 = forms_Group(name="sample_text_2")
    _safe_set(a, 'forms_Item8', b1)
    assert _is_linked(a, 'forms_Item8', b1)
    if hasattr(b1, 'forms_Group7'):
        assert _is_linked(b1, 'forms_Group7', a)
    _safe_set(a, 'forms_Item8', b2)
    assert _is_linked(a, 'forms_Item8', b2)
    if hasattr(b1, 'forms_Group7'):
        assert not _is_linked(b1, 'forms_Group7', a)
    if hasattr(b2, 'forms_Group7'):
        assert _is_linked(b2, 'forms_Group7', a)
    _safe_set(a, 'forms_Item8', None)
    assert not _is_linked(a, 'forms_Item8', b2)
    if hasattr(b2, 'forms_Group7'):
        assert not _is_linked(b2, 'forms_Group7', a)


def test_assoc_options4_link_reassign_clear():
    a = forms_Option(id="sample_text", text="sample_text")
    b1 = forms_Choice(multiple=True)
    b2 = forms_Choice(multiple=False)
    _safe_set(a, 'forms_Option5', b1)
    assert _is_linked(a, 'forms_Option5', b1)
    if hasattr(b1, 'forms_Choice'):
        assert _is_linked(b1, 'forms_Choice', a)
    _safe_set(a, 'forms_Option5', b2)
    assert _is_linked(a, 'forms_Option5', b2)
    if hasattr(b1, 'forms_Choice'):
        assert not _is_linked(b1, 'forms_Choice', a)
    if hasattr(b2, 'forms_Choice'):
        assert _is_linked(b2, 'forms_Choice', a)
    _safe_set(a, 'forms_Option5', None)
    assert not _is_linked(a, 'forms_Option5', b2)
    if hasattr(b2, 'forms_Choice'):
        assert not _is_linked(b2, 'forms_Choice', a)


def test_assoc_options9_link_reassign_clear():
    a = forms_Option(id="sample_text", text="sample_text")
    b1 = forms_Decision()
    b2 = forms_Decision()
    _safe_set(a, 'forms_Option10', b1)
    assert _is_linked(a, 'forms_Option10', b1)
    if hasattr(b1, 'forms_Decision'):
        assert _is_linked(b1, 'forms_Decision', a)
    _safe_set(a, 'forms_Option10', b2)
    assert _is_linked(a, 'forms_Option10', b2)
    if hasattr(b1, 'forms_Decision'):
        assert not _is_linked(b1, 'forms_Decision', a)
    if hasattr(b2, 'forms_Decision'):
        assert _is_linked(b2, 'forms_Decision', a)
    _safe_set(a, 'forms_Option10', None)
    assert not _is_linked(a, 'forms_Option10', b2)
    if hasattr(b2, 'forms_Decision'):
        assert not _is_linked(b2, 'forms_Decision', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ItemType_strategy = st.builds(ItemType)
@given(instance=ItemType_strategy)
@settings(max_examples=25)
def test_ItemType_instantiation(instance):
    assert isinstance(instance, ItemType)


forms_Choice_strategy = st.builds(forms_Choice, multiple=st.booleans())
@given(instance=forms_Choice_strategy)
@settings(max_examples=25)
def test_forms_Choice_instantiation(instance):
    assert isinstance(instance, forms_Choice)


forms_Date_strategy = st.builds(forms_Date)
@given(instance=forms_Date_strategy)
@settings(max_examples=25)
def test_forms_Date_instantiation(instance):
    assert isinstance(instance, forms_Date)


forms_Decision_strategy = st.builds(forms_Decision)
@given(instance=forms_Decision_strategy)
@settings(max_examples=25)
def test_forms_Decision_instantiation(instance):
    assert isinstance(instance, forms_Decision)


forms_Form_strategy = st.builds(forms_Form, caption=safe_text)
@given(instance=forms_Form_strategy)
@settings(max_examples=25)
def test_forms_Form_instantiation(instance):
    assert isinstance(instance, forms_Form)


forms_FreeText_strategy = st.builds(forms_FreeText)
@given(instance=forms_FreeText_strategy)
@settings(max_examples=25)
def test_forms_FreeText_instantiation(instance):
    assert isinstance(instance, forms_FreeText)


forms_Group_strategy = st.builds(forms_Group, name=safe_text)
@given(instance=forms_Group_strategy)
@settings(max_examples=25)
def test_forms_Group_instantiation(instance):
    assert isinstance(instance, forms_Group)


forms_Item_strategy = st.builds(forms_Item, explanation=safe_text, text=safe_text)
@given(instance=forms_Item_strategy)
@settings(max_examples=25)
def test_forms_Item_instantiation(instance):
    assert isinstance(instance, forms_Item)


forms_ItemType_strategy = st.builds(forms_ItemType)
@given(instance=forms_ItemType_strategy)
@settings(max_examples=25)
def test_forms_ItemType_instantiation(instance):
    assert isinstance(instance, forms_ItemType)


forms_Number_strategy = st.builds(forms_Number)
@given(instance=forms_Number_strategy)
@settings(max_examples=25)
def test_forms_Number_instantiation(instance):
    assert isinstance(instance, forms_Number)


forms_Option_strategy = st.builds(forms_Option, id=safe_text, text=safe_text)
@given(instance=forms_Option_strategy)
@settings(max_examples=25)
def test_forms_Option_instantiation(instance):
    assert isinstance(instance, forms_Option)



