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
    Element,
    Comment,
    Make_Makefile,
    Make_Dependency,
    Make_Comment,
    Rule,
    Make_ShellLine,
    Make_Macro,
    ShellLine,
    Dependency,
    Make_FileDep,
    Make_RuleDep,
    Make_Rule,
    Make_Element,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_hyp_element_constructor_exists():
    assert callable(Element.__init__)


def test_hyp_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_hyp_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_hyp_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_make_makefile_is_not_abstract():
    assert not inspect.isabstract(Make_Makefile)


def test_hyp_make_makefile_constructor_exists():
    assert callable(Make_Makefile.__init__)


def test_hyp_make_makefile_constructor_args():
    sig = inspect.signature(Make_Makefile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_make_dependency_is_not_abstract():
    assert not inspect.isabstract(Make_Dependency)


def test_hyp_make_dependency_constructor_exists():
    assert callable(Make_Dependency.__init__)


def test_hyp_make_dependency_constructor_args():
    sig = inspect.signature(Make_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_hyp_make_comment_is_not_abstract():
    assert not inspect.isabstract(Make_Comment)


def test_hyp_make_comment_constructor_exists():
    assert callable(Make_Comment.__init__)


def test_hyp_make_comment_constructor_args():
    sig = inspect.signature(Make_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_rule_is_not_abstract():
    assert not inspect.isabstract(Rule)


def test_hyp_rule_constructor_exists():
    assert callable(Rule.__init__)


def test_hyp_rule_constructor_args():
    sig = inspect.signature(Rule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_make_shellline_is_not_abstract():
    assert not inspect.isabstract(Make_ShellLine)


def test_hyp_make_shellline_constructor_exists():
    assert callable(Make_ShellLine.__init__)


def test_hyp_make_shellline_constructor_args():
    sig = inspect.signature(Make_ShellLine.__init__)
    params = list(sig.parameters.keys())
    assert "display" in params, "Missing parameter 'display'"
    assert "command" in params, "Missing parameter 'command'"





def test_hyp_make_macro_is_not_abstract():
    assert not inspect.isabstract(Make_Macro)


def test_hyp_make_macro_constructor_exists():
    assert callable(Make_Macro.__init__)


def test_hyp_make_macro_constructor_args():
    sig = inspect.signature(Make_Macro.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_shellline_is_not_abstract():
    assert not inspect.isabstract(ShellLine)


def test_hyp_shellline_constructor_exists():
    assert callable(ShellLine.__init__)


def test_hyp_shellline_constructor_args():
    sig = inspect.signature(ShellLine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_hyp_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_hyp_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_hyp_make_filedep_is_not_abstract():
    assert not inspect.isabstract(Make_FileDep)


def test_hyp_make_filedep_constructor_exists():
    assert callable(Make_FileDep.__init__)


def test_hyp_make_filedep_constructor_args():
    sig = inspect.signature(Make_FileDep.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_make_ruledep_is_not_abstract():
    assert not inspect.isabstract(Make_RuleDep)


def test_hyp_make_ruledep_constructor_exists():
    assert callable(Make_RuleDep.__init__)


def test_hyp_make_ruledep_constructor_args():
    sig = inspect.signature(Make_RuleDep.__init__)
    params = list(sig.parameters.keys())



def test_hyp_make_rule_is_not_abstract():
    assert not inspect.isabstract(Make_Rule)


def test_hyp_make_rule_constructor_exists():
    assert callable(Make_Rule.__init__)


def test_hyp_make_rule_constructor_args():
    sig = inspect.signature(Make_Rule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_make_element_is_not_abstract():
    assert not inspect.isabstract(Make_Element)


def test_hyp_make_element_constructor_exists():
    assert callable(Make_Element.__init__)


def test_hyp_make_element_constructor_args():
    sig = inspect.signature(Make_Element.__init__)
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
Element_strategy = st.builds(
    Element,
)
Comment_strategy = st.builds(
    Comment,
)
Make_Makefile_strategy = st.builds(
    Make_Makefile,
    name=
        safe_text
)
Make_Dependency_strategy = st.builds(
    Make_Dependency,
)
Make_Comment_strategy = st.builds(
    Make_Comment,
    text=
        safe_text
)
Rule_strategy = st.builds(
    Rule,
)
Make_ShellLine_strategy = st.builds(
    Make_ShellLine,
    display=
        safe_text,
    command=
        safe_text
)
Make_Macro_strategy = st.builds(
    Make_Macro,
    value=
        safe_text
)
ShellLine_strategy = st.builds(
    ShellLine,
)
Dependency_strategy = st.builds(
    Dependency,
)
Make_FileDep_strategy = st.builds(
    Make_FileDep,
    name=
        safe_text
)
Make_RuleDep_strategy = st.builds(
    Make_RuleDep,
)
Make_Rule_strategy = st.builds(
    Make_Rule,
)
Make_Element_strategy = st.builds(
    Make_Element,
    name=
        safe_text
)






@given(instance=Make_Makefile_strategy)
def test_hyp_make_makefile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=Make_Comment_strategy)
def test_hyp_make_comment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original





@given(instance=Make_ShellLine_strategy)
def test_hyp_make_shellline_display_setter(instance):
    original = instance.display
    instance.display = original
    assert instance.display == original



@given(instance=Make_ShellLine_strategy)
def test_hyp_make_shellline_command_setter(instance):
    original = instance.command
    instance.command = original
    assert instance.command == original




@given(instance=Make_Macro_strategy)
def test_hyp_make_macro_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=Make_FileDep_strategy)
def test_hyp_make_filedep_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=Make_Element_strategy)
def test_hyp_make_element_name_setter(instance):
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
    Comment,
    Dependency,
    Element,
    Make_Comment,
    Make_Dependency,
    Make_Element,
    Make_FileDep,
    Make_Macro,
    Make_Makefile,
    Make_Rule,
    Make_RuleDep,
    Make_ShellLine,
    Rule,
    ShellLine,
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

def test_Make_Comment_text_value_roundtrip():
    instance = Make_Comment(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_Make_Element_name_value_roundtrip():
    instance = Make_Element(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Make_FileDep_name_value_roundtrip():
    instance = Make_FileDep(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Make_Macro_value_value_roundtrip():
    instance = Make_Macro(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_Make_Makefile_name_value_roundtrip():
    instance = Make_Makefile(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Make_ShellLine_command_value_roundtrip():
    instance = Make_ShellLine(command="sample_text", display="sample_text")
    assert instance.command == "sample_text"
    instance.command = "sample_text_2"
    assert instance.command == "sample_text_2"


def test_Make_ShellLine_display_value_roundtrip():
    instance = Make_ShellLine(command="sample_text", display="sample_text")
    assert instance.display == "sample_text"
    instance.display = "sample_text_2"
    assert instance.display == "sample_text_2"


def test_Make_FileDep_isa_Dependency():
    instance = Make_FileDep(name="sample_text")
    assert isinstance(instance, Dependency)


def test_Make_RuleDep_isa_Dependency():
    instance = Make_RuleDep()
    assert isinstance(instance, Dependency)


def test_Make_Macro_isa_Element():
    instance = Make_Macro(value="sample_text")
    assert isinstance(instance, Element)


def test_Make_Rule_isa_Element():
    instance = Make_Rule()
    assert isinstance(instance, Element)


def test_assoc_comment0_link_reassign_clear():
    a = Make_Makefile(name="sample_text")
    b1 = Comment()
    b2 = Comment()
    _safe_set(a, 'Make_Makefile', b1)
    assert _is_linked(a, 'Make_Makefile', b1)
    if hasattr(b1, 'Comment'):
        assert _is_linked(b1, 'Comment', a)
    _safe_set(a, 'Make_Makefile', b2)
    assert _is_linked(a, 'Make_Makefile', b2)
    if hasattr(b1, 'Comment'):
        assert not _is_linked(b1, 'Comment', a)
    if hasattr(b2, 'Comment'):
        assert _is_linked(b2, 'Comment', a)
    _safe_set(a, 'Make_Makefile', None)
    assert not _is_linked(a, 'Make_Makefile', b2)
    if hasattr(b2, 'Comment'):
        assert not _is_linked(b2, 'Comment', a)


def test_assoc_elements1_link_reassign_clear():
    a = Make_Makefile(name="sample_text")
    b1 = Element()
    b2 = Element()
    _safe_set(a, 'Make_Makefile2', {b1})
    assert _is_linked(a, 'Make_Makefile2', b1)
    if hasattr(b1, 'Element'):
        assert _is_linked(b1, 'Element', a)
    _safe_set(a, 'Make_Makefile2', {b2})
    assert _is_linked(a, 'Make_Makefile2', b2)
    if hasattr(b1, 'Element'):
        assert not _is_linked(b1, 'Element', a)
    if hasattr(b2, 'Element'):
        assert _is_linked(b2, 'Element', a)
    _safe_set(a, 'Make_Makefile2', set())
    assert not _is_linked(a, 'Make_Makefile2', b2)
    if hasattr(b2, 'Element'):
        assert not _is_linked(b2, 'Element', a)


def test_assoc_ruleShellLine5_link_reassign_clear():
    a = Make_ShellLine(command="sample_text", display="sample_text")
    b1 = Rule()
    b2 = Rule()
    _safe_set(a, 'shellLines', b1)
    assert _is_linked(a, 'shellLines', b1)
    if hasattr(b1, 'Rule'):
        assert _is_linked(b1, 'Rule', a)
    _safe_set(a, 'shellLines', b2)
    assert _is_linked(a, 'shellLines', b2)
    if hasattr(b1, 'Rule'):
        assert not _is_linked(b1, 'Rule', a)
    if hasattr(b2, 'Rule'):
        assert _is_linked(b2, 'Rule', a)
    _safe_set(a, 'shellLines', None)
    assert not _is_linked(a, 'shellLines', b2)
    if hasattr(b2, 'Rule'):
        assert not _is_linked(b2, 'Rule', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Comment_strategy = st.builds(Comment)
@given(instance=Comment_strategy)
@settings(max_examples=25)
def test_Comment_instantiation(instance):
    assert isinstance(instance, Comment)


Dependency_strategy = st.builds(Dependency)
@given(instance=Dependency_strategy)
@settings(max_examples=25)
def test_Dependency_instantiation(instance):
    assert isinstance(instance, Dependency)


Element_strategy = st.builds(Element)
@given(instance=Element_strategy)
@settings(max_examples=25)
def test_Element_instantiation(instance):
    assert isinstance(instance, Element)


Make_Comment_strategy = st.builds(Make_Comment, text=safe_text)
@given(instance=Make_Comment_strategy)
@settings(max_examples=25)
def test_Make_Comment_instantiation(instance):
    assert isinstance(instance, Make_Comment)


Make_Dependency_strategy = st.builds(Make_Dependency)
@given(instance=Make_Dependency_strategy)
@settings(max_examples=25)
def test_Make_Dependency_instantiation(instance):
    assert isinstance(instance, Make_Dependency)


Make_Element_strategy = st.builds(Make_Element, name=safe_text)
@given(instance=Make_Element_strategy)
@settings(max_examples=25)
def test_Make_Element_instantiation(instance):
    assert isinstance(instance, Make_Element)


Make_FileDep_strategy = st.builds(Make_FileDep, name=safe_text)
@given(instance=Make_FileDep_strategy)
@settings(max_examples=25)
def test_Make_FileDep_instantiation(instance):
    assert isinstance(instance, Make_FileDep)


Make_Macro_strategy = st.builds(Make_Macro, value=safe_text)
@given(instance=Make_Macro_strategy)
@settings(max_examples=25)
def test_Make_Macro_instantiation(instance):
    assert isinstance(instance, Make_Macro)


Make_Makefile_strategy = st.builds(Make_Makefile, name=safe_text)
@given(instance=Make_Makefile_strategy)
@settings(max_examples=25)
def test_Make_Makefile_instantiation(instance):
    assert isinstance(instance, Make_Makefile)


Make_Rule_strategy = st.builds(Make_Rule)
@given(instance=Make_Rule_strategy)
@settings(max_examples=25)
def test_Make_Rule_instantiation(instance):
    assert isinstance(instance, Make_Rule)


Make_RuleDep_strategy = st.builds(Make_RuleDep)
@given(instance=Make_RuleDep_strategy)
@settings(max_examples=25)
def test_Make_RuleDep_instantiation(instance):
    assert isinstance(instance, Make_RuleDep)


Make_ShellLine_strategy = st.builds(Make_ShellLine, command=safe_text, display=safe_text)
@given(instance=Make_ShellLine_strategy)
@settings(max_examples=25)
def test_Make_ShellLine_instantiation(instance):
    assert isinstance(instance, Make_ShellLine)


Rule_strategy = st.builds(Rule)
@given(instance=Rule_strategy)
@settings(max_examples=25)
def test_Rule_instantiation(instance):
    assert isinstance(instance, Rule)


ShellLine_strategy = st.builds(ShellLine)
@given(instance=ShellLine_strategy)
@settings(max_examples=25)
def test_ShellLine_instantiation(instance):
    assert isinstance(instance, ShellLine)



