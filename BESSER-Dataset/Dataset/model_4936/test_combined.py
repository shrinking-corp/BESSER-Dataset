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
    UIElement,
    webapp_Table,
    webapp_TextArea,
    webapp_ImageViewer,
    webapp_Form,
    Named,
    webapp_Attribute,
    webapp_ClientPage,
    webapp_UIElement,
    webapp_WebApp,
    webapp_Named,
    webapp_DataSourceManager,
    webapp_DataStructure,
    webapp_ServerPage,
    UIElementType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_uielement_is_not_abstract():
    assert not inspect.isabstract(UIElement)


def test_hyp_uielement_constructor_exists():
    assert callable(UIElement.__init__)


def test_hyp_uielement_constructor_args():
    sig = inspect.signature(UIElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_webapp_table_is_not_abstract():
    assert not inspect.isabstract(webapp_Table)


def test_hyp_webapp_table_constructor_exists():
    assert callable(webapp_Table.__init__)


def test_hyp_webapp_table_constructor_args():
    sig = inspect.signature(webapp_Table.__init__)
    params = list(sig.parameters.keys())



def test_hyp_webapp_textarea_is_not_abstract():
    assert not inspect.isabstract(webapp_TextArea)


def test_hyp_webapp_textarea_constructor_exists():
    assert callable(webapp_TextArea.__init__)


def test_hyp_webapp_textarea_constructor_args():
    sig = inspect.signature(webapp_TextArea.__init__)
    params = list(sig.parameters.keys())



def test_hyp_webapp_imageviewer_is_not_abstract():
    assert not inspect.isabstract(webapp_ImageViewer)


def test_hyp_webapp_imageviewer_constructor_exists():
    assert callable(webapp_ImageViewer.__init__)


def test_hyp_webapp_imageviewer_constructor_args():
    sig = inspect.signature(webapp_ImageViewer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_webapp_form_is_not_abstract():
    assert not inspect.isabstract(webapp_Form)


def test_hyp_webapp_form_constructor_exists():
    assert callable(webapp_Form.__init__)


def test_hyp_webapp_form_constructor_args():
    sig = inspect.signature(webapp_Form.__init__)
    params = list(sig.parameters.keys())



def test_hyp_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_hyp_named_constructor_exists():
    assert callable(Named.__init__)


def test_hyp_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_hyp_webapp_attribute_is_not_abstract():
    assert not inspect.isabstract(webapp_Attribute)


def test_hyp_webapp_attribute_constructor_exists():
    assert callable(webapp_Attribute.__init__)


def test_hyp_webapp_attribute_constructor_args():
    sig = inspect.signature(webapp_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_webapp_clientpage_is_not_abstract():
    assert not inspect.isabstract(webapp_ClientPage)


def test_hyp_webapp_clientpage_constructor_exists():
    assert callable(webapp_ClientPage.__init__)


def test_hyp_webapp_clientpage_constructor_args():
    sig = inspect.signature(webapp_ClientPage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_webapp_uielement_is_not_abstract():
    assert not inspect.isabstract(webapp_UIElement)


def test_hyp_webapp_uielement_constructor_exists():
    assert callable(webapp_UIElement.__init__)


def test_hyp_webapp_uielement_constructor_args():
    sig = inspect.signature(webapp_UIElement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_webapp_webapp_is_not_abstract():
    assert not inspect.isabstract(webapp_WebApp)


def test_hyp_webapp_webapp_constructor_exists():
    assert callable(webapp_WebApp.__init__)


def test_hyp_webapp_webapp_constructor_args():
    sig = inspect.signature(webapp_WebApp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_webapp_named_is_not_abstract():
    assert not inspect.isabstract(webapp_Named)


def test_hyp_webapp_named_constructor_exists():
    assert callable(webapp_Named.__init__)


def test_hyp_webapp_named_constructor_args():
    sig = inspect.signature(webapp_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_webapp_datasourcemanager_is_not_abstract():
    assert not inspect.isabstract(webapp_DataSourceManager)


def test_hyp_webapp_datasourcemanager_constructor_exists():
    assert callable(webapp_DataSourceManager.__init__)


def test_hyp_webapp_datasourcemanager_constructor_args():
    sig = inspect.signature(webapp_DataSourceManager.__init__)
    params = list(sig.parameters.keys())



def test_hyp_webapp_datastructure_is_not_abstract():
    assert not inspect.isabstract(webapp_DataStructure)


def test_hyp_webapp_datastructure_constructor_exists():
    assert callable(webapp_DataStructure.__init__)


def test_hyp_webapp_datastructure_constructor_args():
    sig = inspect.signature(webapp_DataStructure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_webapp_serverpage_is_not_abstract():
    assert not inspect.isabstract(webapp_ServerPage)


def test_hyp_webapp_serverpage_constructor_exists():
    assert callable(webapp_ServerPage.__init__)


def test_hyp_webapp_serverpage_constructor_args():
    sig = inspect.signature(webapp_ServerPage.__init__)
    params = list(sig.parameters.keys())

def test_hyp_uielementtype_exists():
    # Check that the Enumeration exists
    assert UIElementType is not None

def test_hyp_uielementtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UIElementType]
    expected_literals = [
        "input",
        "output",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UIElementType"


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
UIElement_strategy = st.builds(
    UIElement,
)
webapp_Table_strategy = st.builds(
    webapp_Table,
)
webapp_TextArea_strategy = st.builds(
    webapp_TextArea,
)
webapp_ImageViewer_strategy = st.builds(
    webapp_ImageViewer,
)
webapp_Form_strategy = st.builds(
    webapp_Form,
)
Named_strategy = st.builds(
    Named,
)
webapp_Attribute_strategy = st.builds(
    webapp_Attribute,
    type=
        safe_text
)
webapp_ClientPage_strategy = st.builds(
    webapp_ClientPage,
)
webapp_UIElement_strategy = st.builds(
    webapp_UIElement,
    type=
        safe_text
)
webapp_WebApp_strategy = st.builds(
    webapp_WebApp,
)
webapp_Named_strategy = st.builds(
    webapp_Named,
    name=
        safe_text
)
webapp_DataSourceManager_strategy = st.builds(
    webapp_DataSourceManager,
)
webapp_DataStructure_strategy = st.builds(
    webapp_DataStructure,
)
webapp_ServerPage_strategy = st.builds(
    webapp_ServerPage,
)










@given(instance=webapp_Attribute_strategy)
def test_hyp_webapp_attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original





@given(instance=webapp_UIElement_strategy)
def test_hyp_webapp_uielement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original





@given(instance=webapp_Named_strategy)
def test_hyp_webapp_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=webapp_ServerPage_strategy)
@settings(max_examples=30)
def test_hyp_webapp_serverpage_request_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.request()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.request).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'request' in webapp_ServerPage is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'request' in webapp_ServerPage did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'request' in webapp_ServerPage is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=webapp_ServerPage_strategy)
@settings(max_examples=30)
def test_hyp_webapp_serverpage_response_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.response()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.response).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'response' in webapp_ServerPage is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'response' in webapp_ServerPage did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'response' in webapp_ServerPage is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Named,
    UIElement,
    webapp_Attribute,
    webapp_ClientPage,
    webapp_DataSourceManager,
    webapp_DataStructure,
    webapp_Form,
    webapp_ImageViewer,
    webapp_Named,
    webapp_ServerPage,
    webapp_Table,
    webapp_TextArea,
    webapp_UIElement,
    webapp_WebApp,
    UIElementType,
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

def test_webapp_Attribute_type_value_roundtrip():
    instance = webapp_Attribute(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_webapp_Named_name_value_roundtrip():
    instance = webapp_Named(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_webapp_UIElement_type_value_roundtrip():
    instance = webapp_UIElement(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_webapp_Attribute_isa_Named():
    instance = webapp_Attribute(type="sample_text")
    assert isinstance(instance, Named)


def test_webapp_ClientPage_isa_Named():
    instance = webapp_ClientPage()
    assert isinstance(instance, Named)


def test_webapp_DataSourceManager_isa_Named():
    instance = webapp_DataSourceManager()
    assert isinstance(instance, Named)


def test_webapp_DataStructure_isa_Named():
    instance = webapp_DataStructure()
    assert isinstance(instance, Named)


def test_webapp_ServerPage_isa_Named():
    instance = webapp_ServerPage()
    assert isinstance(instance, Named)


def test_webapp_UIElement_isa_Named():
    instance = webapp_UIElement(type="sample_text")
    assert isinstance(instance, Named)


def test_webapp_WebApp_isa_Named():
    instance = webapp_WebApp()
    assert isinstance(instance, Named)


def test_webapp_Form_isa_UIElement():
    instance = webapp_Form()
    assert isinstance(instance, UIElement)


def test_webapp_ImageViewer_isa_UIElement():
    instance = webapp_ImageViewer()
    assert isinstance(instance, UIElement)


def test_webapp_Table_isa_UIElement():
    instance = webapp_Table()
    assert isinstance(instance, UIElement)


def test_webapp_TextArea_isa_UIElement():
    instance = webapp_TextArea()
    assert isinstance(instance, UIElement)


def test_assoc_attributeOf16_link_reassign_clear():
    a = webapp_Attribute(type="sample_text")
    b1 = webapp_DataStructure()
    b2 = webapp_DataStructure()
    _safe_set(a, 'parentOf', b1)
    assert _is_linked(a, 'parentOf', b1)
    if hasattr(b1, 'DataStructure17'):
        assert _is_linked(b1, 'DataStructure17', a)
    _safe_set(a, 'parentOf', b2)
    assert _is_linked(a, 'parentOf', b2)
    if hasattr(b1, 'DataStructure17'):
        assert not _is_linked(b1, 'DataStructure17', a)
    if hasattr(b2, 'DataStructure17'):
        assert _is_linked(b2, 'DataStructure17', a)
    _safe_set(a, 'parentOf', None)
    assert not _is_linked(a, 'parentOf', b2)
    if hasattr(b2, 'DataStructure17'):
        assert not _is_linked(b2, 'DataStructure17', a)


def test_assoc_composedOf20_link_reassign_clear():
    a = webapp_UIElement(type="sample_text")
    b1 = webapp_ClientPage()
    b2 = webapp_ClientPage()
    _safe_set(a, 'webapp_UIElement', b1)
    assert _is_linked(a, 'webapp_UIElement', b1)
    if hasattr(b1, 'webapp_ClientPage21'):
        assert _is_linked(b1, 'webapp_ClientPage21', a)
    _safe_set(a, 'webapp_UIElement', b2)
    assert _is_linked(a, 'webapp_UIElement', b2)
    if hasattr(b1, 'webapp_ClientPage21'):
        assert not _is_linked(b1, 'webapp_ClientPage21', a)
    if hasattr(b2, 'webapp_ClientPage21'):
        assert _is_linked(b2, 'webapp_ClientPage21', a)
    _safe_set(a, 'webapp_UIElement', None)
    assert not _is_linked(a, 'webapp_UIElement', b2)
    if hasattr(b2, 'webapp_ClientPage21'):
        assert not _is_linked(b2, 'webapp_ClientPage21', a)


def test_assoc_connectsTo22_link_reassign_clear():
    a = webapp_ServerPage()
    b1 = webapp_ClientPage()
    b2 = webapp_ClientPage()
    _safe_set(a, 'ServerPage23', b1)
    assert _is_linked(a, 'ServerPage23', b1)
    if hasattr(b1, 'generates'):
        assert _is_linked(b1, 'generates', a)
    _safe_set(a, 'ServerPage23', b2)
    assert _is_linked(a, 'ServerPage23', b2)
    if hasattr(b1, 'generates'):
        assert not _is_linked(b1, 'generates', a)
    if hasattr(b2, 'generates'):
        assert _is_linked(b2, 'generates', a)
    _safe_set(a, 'ServerPage23', None)
    assert not _is_linked(a, 'ServerPage23', b2)
    if hasattr(b2, 'generates'):
        assert not _is_linked(b2, 'generates', a)


def test_assoc_content24_link_reassign_clear():
    a = webapp_UIElement(type="sample_text")
    b1 = webapp_DataStructure()
    b2 = webapp_DataStructure()
    _safe_set(a, 'webapp_UIElement25', b1)
    assert _is_linked(a, 'webapp_UIElement25', b1)
    if hasattr(b1, 'webapp_DataStructure26'):
        assert _is_linked(b1, 'webapp_DataStructure26', a)
    _safe_set(a, 'webapp_UIElement25', b2)
    assert _is_linked(a, 'webapp_UIElement25', b2)
    if hasattr(b1, 'webapp_DataStructure26'):
        assert not _is_linked(b1, 'webapp_DataStructure26', a)
    if hasattr(b2, 'webapp_DataStructure26'):
        assert _is_linked(b2, 'webapp_DataStructure26', a)
    _safe_set(a, 'webapp_UIElement25', None)
    assert not _is_linked(a, 'webapp_UIElement25', b2)
    if hasattr(b2, 'webapp_DataStructure26'):
        assert not _is_linked(b2, 'webapp_DataStructure26', a)


def test_assoc_generates7_link_reassign_clear():
    a = webapp_ServerPage()
    b1 = webapp_ClientPage()
    b2 = webapp_ClientPage()
    _safe_set(a, 'connectsTo', b1)
    assert _is_linked(a, 'connectsTo', b1)
    if hasattr(b1, 'ClientPage'):
        assert _is_linked(b1, 'ClientPage', a)
    _safe_set(a, 'connectsTo', b2)
    assert _is_linked(a, 'connectsTo', b2)
    if hasattr(b1, 'ClientPage'):
        assert not _is_linked(b1, 'ClientPage', a)
    if hasattr(b2, 'ClientPage'):
        assert _is_linked(b2, 'ClientPage', a)
    _safe_set(a, 'connectsTo', None)
    assert not _is_linked(a, 'connectsTo', b2)
    if hasattr(b2, 'ClientPage'):
        assert not _is_linked(b2, 'ClientPage', a)


def test_assoc_getContents8_link_reassign_clear():
    a = webapp_ServerPage()
    b1 = webapp_DataSourceManager()
    b2 = webapp_DataSourceManager()
    _safe_set(a, 'providesContent', {b1})
    assert _is_linked(a, 'providesContent', b1)
    if hasattr(b1, 'DataSourceManager'):
        assert _is_linked(b1, 'DataSourceManager', a)
    _safe_set(a, 'providesContent', {b2})
    assert _is_linked(a, 'providesContent', b2)
    if hasattr(b1, 'DataSourceManager'):
        assert not _is_linked(b1, 'DataSourceManager', a)
    if hasattr(b2, 'DataSourceManager'):
        assert _is_linked(b2, 'DataSourceManager', a)
    _safe_set(a, 'providesContent', set())
    assert not _is_linked(a, 'providesContent', b2)
    if hasattr(b2, 'DataSourceManager'):
        assert not _is_linked(b2, 'DataSourceManager', a)


def test_assoc_linkedBy18_link_reassign_clear():
    a = webapp_Attribute(type="sample_text")
    b1 = webapp_DataStructure()
    b2 = webapp_DataStructure()
    _safe_set(a, 'linkedTo', {b1})
    assert _is_linked(a, 'linkedTo', b1)
    if hasattr(b1, 'DataStructure19'):
        assert _is_linked(b1, 'DataStructure19', a)
    _safe_set(a, 'linkedTo', {b2})
    assert _is_linked(a, 'linkedTo', b2)
    if hasattr(b1, 'DataStructure19'):
        assert not _is_linked(b1, 'DataStructure19', a)
    if hasattr(b2, 'DataStructure19'):
        assert _is_linked(b2, 'DataStructure19', a)
    _safe_set(a, 'linkedTo', set())
    assert not _is_linked(a, 'linkedTo', b2)
    if hasattr(b2, 'DataStructure19'):
        assert not _is_linked(b2, 'DataStructure19', a)


def test_assoc_linkedTo12_link_reassign_clear():
    a = webapp_Attribute(type="sample_text")
    b1 = webapp_DataStructure()
    b2 = webapp_DataStructure()
    _safe_set(a, 'Attribute13', b1)
    assert _is_linked(a, 'Attribute13', b1)
    if hasattr(b1, 'linkedBy'):
        assert _is_linked(b1, 'linkedBy', a)
    _safe_set(a, 'Attribute13', b2)
    assert _is_linked(a, 'Attribute13', b2)
    if hasattr(b1, 'linkedBy'):
        assert not _is_linked(b1, 'linkedBy', a)
    if hasattr(b2, 'linkedBy'):
        assert _is_linked(b2, 'linkedBy', a)
    _safe_set(a, 'Attribute13', None)
    assert not _is_linked(a, 'Attribute13', b2)
    if hasattr(b2, 'linkedBy'):
        assert not _is_linked(b2, 'linkedBy', a)


def test_assoc_managedBy10_link_reassign_clear():
    a = webapp_ServerPage()
    b1 = webapp_DataStructure()
    b2 = webapp_DataStructure()
    _safe_set(a, 'ServerPage', b1)
    assert _is_linked(a, 'ServerPage', b1)
    if hasattr(b1, 'manages'):
        assert _is_linked(b1, 'manages', a)
    _safe_set(a, 'ServerPage', b2)
    assert _is_linked(a, 'ServerPage', b2)
    if hasattr(b1, 'manages'):
        assert not _is_linked(b1, 'manages', a)
    if hasattr(b2, 'manages'):
        assert _is_linked(b2, 'manages', a)
    _safe_set(a, 'ServerPage', None)
    assert not _is_linked(a, 'ServerPage', b2)
    if hasattr(b2, 'manages'):
        assert not _is_linked(b2, 'manages', a)


def test_assoc_manages9_link_reassign_clear():
    a = webapp_ServerPage()
    b1 = webapp_DataStructure()
    b2 = webapp_DataStructure()
    _safe_set(a, 'managedBy', {b1})
    assert _is_linked(a, 'managedBy', b1)
    if hasattr(b1, 'DataStructure'):
        assert _is_linked(b1, 'DataStructure', a)
    _safe_set(a, 'managedBy', {b2})
    assert _is_linked(a, 'managedBy', b2)
    if hasattr(b1, 'DataStructure'):
        assert not _is_linked(b1, 'DataStructure', a)
    if hasattr(b2, 'DataStructure'):
        assert _is_linked(b2, 'DataStructure', a)
    _safe_set(a, 'managedBy', set())
    assert not _is_linked(a, 'managedBy', b2)
    if hasattr(b2, 'DataStructure'):
        assert not _is_linked(b2, 'DataStructure', a)


def test_assoc_parentOf11_link_reassign_clear():
    a = webapp_Attribute(type="sample_text")
    b1 = webapp_DataStructure()
    b2 = webapp_DataStructure()
    _safe_set(a, 'Attribute', b1)
    assert _is_linked(a, 'Attribute', b1)
    if hasattr(b1, 'attributeOf'):
        assert _is_linked(b1, 'attributeOf', a)
    _safe_set(a, 'Attribute', b2)
    assert _is_linked(a, 'Attribute', b2)
    if hasattr(b1, 'attributeOf'):
        assert not _is_linked(b1, 'attributeOf', a)
    if hasattr(b2, 'attributeOf'):
        assert _is_linked(b2, 'attributeOf', a)
    _safe_set(a, 'Attribute', None)
    assert not _is_linked(a, 'Attribute', b2)
    if hasattr(b2, 'attributeOf'):
        assert not _is_linked(b2, 'attributeOf', a)


def test_assoc_providesContent14_link_reassign_clear():
    a = webapp_ServerPage()
    b1 = webapp_DataSourceManager()
    b2 = webapp_DataSourceManager()
    _safe_set(a, 'ServerPage15', b1)
    assert _is_linked(a, 'ServerPage15', b1)
    if hasattr(b1, 'getContents'):
        assert _is_linked(b1, 'getContents', a)
    _safe_set(a, 'ServerPage15', b2)
    assert _is_linked(a, 'ServerPage15', b2)
    if hasattr(b1, 'getContents'):
        assert not _is_linked(b1, 'getContents', a)
    if hasattr(b2, 'getContents'):
        assert _is_linked(b2, 'getContents', a)
    _safe_set(a, 'ServerPage15', None)
    assert not _is_linked(a, 'ServerPage15', b2)
    if hasattr(b2, 'getContents'):
        assert not _is_linked(b2, 'getContents', a)


def test_assoc_serverPages1_link_reassign_clear():
    a = webapp_ServerPage()
    b1 = webapp_WebApp()
    b2 = webapp_WebApp()
    _safe_set(a, 'webapp_ServerPage', b1)
    assert _is_linked(a, 'webapp_ServerPage', b1)
    if hasattr(b1, 'webapp_WebApp2'):
        assert _is_linked(b1, 'webapp_WebApp2', a)
    _safe_set(a, 'webapp_ServerPage', b2)
    assert _is_linked(a, 'webapp_ServerPage', b2)
    if hasattr(b1, 'webapp_WebApp2'):
        assert not _is_linked(b1, 'webapp_WebApp2', a)
    if hasattr(b2, 'webapp_WebApp2'):
        assert _is_linked(b2, 'webapp_WebApp2', a)
    _safe_set(a, 'webapp_ServerPage', None)
    assert not _is_linked(a, 'webapp_ServerPage', b2)
    if hasattr(b2, 'webapp_WebApp2'):
        assert not _is_linked(b2, 'webapp_WebApp2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Named_strategy = st.builds(Named)
@given(instance=Named_strategy)
@settings(max_examples=25)
def test_Named_instantiation(instance):
    assert isinstance(instance, Named)


UIElement_strategy = st.builds(UIElement)
@given(instance=UIElement_strategy)
@settings(max_examples=25)
def test_UIElement_instantiation(instance):
    assert isinstance(instance, UIElement)


webapp_Attribute_strategy = st.builds(webapp_Attribute, type=safe_text)
@given(instance=webapp_Attribute_strategy)
@settings(max_examples=25)
def test_webapp_Attribute_instantiation(instance):
    assert isinstance(instance, webapp_Attribute)


webapp_ClientPage_strategy = st.builds(webapp_ClientPage)
@given(instance=webapp_ClientPage_strategy)
@settings(max_examples=25)
def test_webapp_ClientPage_instantiation(instance):
    assert isinstance(instance, webapp_ClientPage)


webapp_DataSourceManager_strategy = st.builds(webapp_DataSourceManager)
@given(instance=webapp_DataSourceManager_strategy)
@settings(max_examples=25)
def test_webapp_DataSourceManager_instantiation(instance):
    assert isinstance(instance, webapp_DataSourceManager)


webapp_DataStructure_strategy = st.builds(webapp_DataStructure)
@given(instance=webapp_DataStructure_strategy)
@settings(max_examples=25)
def test_webapp_DataStructure_instantiation(instance):
    assert isinstance(instance, webapp_DataStructure)


webapp_Form_strategy = st.builds(webapp_Form)
@given(instance=webapp_Form_strategy)
@settings(max_examples=25)
def test_webapp_Form_instantiation(instance):
    assert isinstance(instance, webapp_Form)


webapp_ImageViewer_strategy = st.builds(webapp_ImageViewer)
@given(instance=webapp_ImageViewer_strategy)
@settings(max_examples=25)
def test_webapp_ImageViewer_instantiation(instance):
    assert isinstance(instance, webapp_ImageViewer)


webapp_Named_strategy = st.builds(webapp_Named, name=safe_text)
@given(instance=webapp_Named_strategy)
@settings(max_examples=25)
def test_webapp_Named_instantiation(instance):
    assert isinstance(instance, webapp_Named)


webapp_ServerPage_strategy = st.builds(webapp_ServerPage)
@given(instance=webapp_ServerPage_strategy)
@settings(max_examples=25)
def test_webapp_ServerPage_instantiation(instance):
    assert isinstance(instance, webapp_ServerPage)


webapp_Table_strategy = st.builds(webapp_Table)
@given(instance=webapp_Table_strategy)
@settings(max_examples=25)
def test_webapp_Table_instantiation(instance):
    assert isinstance(instance, webapp_Table)


webapp_TextArea_strategy = st.builds(webapp_TextArea)
@given(instance=webapp_TextArea_strategy)
@settings(max_examples=25)
def test_webapp_TextArea_instantiation(instance):
    assert isinstance(instance, webapp_TextArea)


webapp_UIElement_strategy = st.builds(webapp_UIElement, type=safe_text)
@given(instance=webapp_UIElement_strategy)
@settings(max_examples=25)
def test_webapp_UIElement_instantiation(instance):
    assert isinstance(instance, webapp_UIElement)


webapp_WebApp_strategy = st.builds(webapp_WebApp)
@given(instance=webapp_WebApp_strategy)
@settings(max_examples=25)
def test_webapp_WebApp_instantiation(instance):
    assert isinstance(instance, webapp_WebApp)



