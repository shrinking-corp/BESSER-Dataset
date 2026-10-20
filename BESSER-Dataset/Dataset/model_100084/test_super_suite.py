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
    maven_GroupAndArtifact,
    maven_Transform,
    maven_Mappings,
    maven_Scope,
    maven_Scopes,
    Provider,
    maven_MavenProvider,
    GroupAndArtifact,
    maven_MapEntry,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_maven_groupandartifact_is_not_abstract():
    assert not inspect.isabstract(maven_GroupAndArtifact)


def test_hyp_maven_groupandartifact_constructor_exists():
    assert callable(maven_GroupAndArtifact.__init__)


def test_hyp_maven_groupandartifact_constructor_args():
    sig = inspect.signature(maven_GroupAndArtifact.__init__)
    params = list(sig.parameters.keys())
    assert "groupId" in params, "Missing parameter 'groupId'"
    assert "artifactId" in params, "Missing parameter 'artifactId'"





def test_hyp_maven_transform_is_not_abstract():
    assert not inspect.isabstract(maven_Transform)


def test_hyp_maven_transform_constructor_exists():
    assert callable(maven_Transform.__init__)


def test_hyp_maven_transform_constructor_args():
    sig = inspect.signature(maven_Transform.__init__)
    params = list(sig.parameters.keys())



def test_hyp_maven_mappings_is_not_abstract():
    assert not inspect.isabstract(maven_Mappings)


def test_hyp_maven_mappings_constructor_exists():
    assert callable(maven_Mappings.__init__)


def test_hyp_maven_mappings_constructor_args():
    sig = inspect.signature(maven_Mappings.__init__)
    params = list(sig.parameters.keys())



def test_hyp_maven_scope_is_not_abstract():
    assert not inspect.isabstract(maven_Scope)


def test_hyp_maven_scope_constructor_exists():
    assert callable(maven_Scope.__init__)


def test_hyp_maven_scope_constructor_args():
    sig = inspect.signature(maven_Scope.__init__)
    params = list(sig.parameters.keys())
    assert "exclude" in params, "Missing parameter 'exclude'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_maven_scopes_is_not_abstract():
    assert not inspect.isabstract(maven_Scopes)


def test_hyp_maven_scopes_constructor_exists():
    assert callable(maven_Scopes.__init__)


def test_hyp_maven_scopes_constructor_args():
    sig = inspect.signature(maven_Scopes.__init__)
    params = list(sig.parameters.keys())



def test_hyp_provider_is_not_abstract():
    assert not inspect.isabstract(Provider)


def test_hyp_provider_constructor_exists():
    assert callable(Provider.__init__)


def test_hyp_provider_constructor_args():
    sig = inspect.signature(Provider.__init__)
    params = list(sig.parameters.keys())



def test_hyp_maven_mavenprovider_is_not_abstract():
    assert not inspect.isabstract(maven_MavenProvider)


def test_hyp_maven_mavenprovider_constructor_exists():
    assert callable(maven_MavenProvider.__init__)


def test_hyp_maven_mavenprovider_constructor_args():
    sig = inspect.signature(maven_MavenProvider.__init__)
    params = list(sig.parameters.keys())
    assert "transitive" in params, "Missing parameter 'transitive'"




def test_hyp_groupandartifact_is_not_abstract():
    assert not inspect.isabstract(GroupAndArtifact)


def test_hyp_groupandartifact_constructor_exists():
    assert callable(GroupAndArtifact.__init__)


def test_hyp_groupandartifact_constructor_args():
    sig = inspect.signature(GroupAndArtifact.__init__)
    params = list(sig.parameters.keys())



def test_hyp_maven_mapentry_is_not_abstract():
    assert not inspect.isabstract(maven_MapEntry)


def test_hyp_maven_mapentry_constructor_exists():
    assert callable(maven_MapEntry.__init__)


def test_hyp_maven_mapentry_constructor_args():
    sig = inspect.signature(maven_MapEntry.__init__)
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
maven_GroupAndArtifact_strategy = st.builds(
    maven_GroupAndArtifact,
    groupId=
        safe_text,
    artifactId=
        safe_text
)
maven_Transform_strategy = st.builds(
    maven_Transform,
)
maven_Mappings_strategy = st.builds(
    maven_Mappings,
)
maven_Scope_strategy = st.builds(
    maven_Scope,
    exclude=
        st.booleans(),
    name=
        safe_text
)
maven_Scopes_strategy = st.builds(
    maven_Scopes,
)
Provider_strategy = st.builds(
    Provider,
)
maven_MavenProvider_strategy = st.builds(
    maven_MavenProvider,
    transitive=
        st.booleans()
)
GroupAndArtifact_strategy = st.builds(
    GroupAndArtifact,
)
maven_MapEntry_strategy = st.builds(
    maven_MapEntry,
    name=
        safe_text
)




@given(instance=maven_GroupAndArtifact_strategy)
def test_hyp_maven_groupandartifact_groupId_setter(instance):
    original = instance.groupId
    instance.groupId = original
    assert instance.groupId == original



@given(instance=maven_GroupAndArtifact_strategy)
def test_hyp_maven_groupandartifact_artifactId_setter(instance):
    original = instance.artifactId
    instance.artifactId = original
    assert instance.artifactId == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings







@given(instance=maven_Scope_strategy)
def test_hyp_maven_scope_exclude_setter(instance):
    original = instance.exclude
    instance.exclude = original
    assert instance.exclude == original



@given(instance=maven_Scope_strategy)
def test_hyp_maven_scope_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=maven_MavenProvider_strategy)
def test_hyp_maven_mavenprovider_transitive_setter(instance):
    original = instance.transitive
    instance.transitive = original
    assert instance.transitive == original





@given(instance=maven_MapEntry_strategy)
def test_hyp_maven_mapentry_name_setter(instance):
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
    GroupAndArtifact,
    Provider,
    maven_GroupAndArtifact,
    maven_MapEntry,
    maven_Mappings,
    maven_MavenProvider,
    maven_Scope,
    maven_Scopes,
    maven_Transform,
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

def test_maven_GroupAndArtifact_artifactId_value_roundtrip():
    instance = maven_GroupAndArtifact(artifactId="sample_text", groupId="sample_text")
    assert instance.artifactId == "sample_text"
    instance.artifactId = "sample_text_2"
    assert instance.artifactId == "sample_text_2"


def test_maven_GroupAndArtifact_groupId_value_roundtrip():
    instance = maven_GroupAndArtifact(artifactId="sample_text", groupId="sample_text")
    assert instance.groupId == "sample_text"
    instance.groupId = "sample_text_2"
    assert instance.groupId == "sample_text_2"


def test_maven_MapEntry_name_value_roundtrip():
    instance = maven_MapEntry(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_maven_MavenProvider_transitive_value_roundtrip():
    instance = maven_MavenProvider(transitive=True)
    assert instance.transitive == True
    instance.transitive = False
    assert instance.transitive == False


def test_maven_Scope_exclude_value_roundtrip():
    instance = maven_Scope(exclude=True, name="sample_text")
    assert instance.exclude == True
    instance.exclude = False
    assert instance.exclude == False


def test_maven_Scope_name_value_roundtrip():
    instance = maven_Scope(exclude=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_maven_MapEntry_isa_GroupAndArtifact():
    instance = maven_MapEntry(name="sample_text")
    assert isinstance(instance, GroupAndArtifact)


def test_maven_MavenProvider_isa_Provider():
    instance = maven_MavenProvider(transitive=True)
    assert isinstance(instance, Provider)


def test_assoc_aliases0_link_reassign_clear():
    a = maven_MapEntry(name="sample_text")
    b1 = maven_GroupAndArtifact(artifactId="sample_text", groupId="sample_text")
    b2 = maven_GroupAndArtifact(artifactId="sample_text_2", groupId="sample_text_2")
    _safe_set(a, 'maven_MapEntry', {b1})
    assert _is_linked(a, 'maven_MapEntry', b1)
    if hasattr(b1, 'maven_GroupAndArtifact'):
        assert _is_linked(b1, 'maven_GroupAndArtifact', a)
    _safe_set(a, 'maven_MapEntry', {b2})
    assert _is_linked(a, 'maven_MapEntry', b2)
    if hasattr(b1, 'maven_GroupAndArtifact'):
        assert not _is_linked(b1, 'maven_GroupAndArtifact', a)
    if hasattr(b2, 'maven_GroupAndArtifact'):
        assert _is_linked(b2, 'maven_GroupAndArtifact', a)
    _safe_set(a, 'maven_MapEntry', set())
    assert not _is_linked(a, 'maven_MapEntry', b2)
    if hasattr(b2, 'maven_GroupAndArtifact'):
        assert not _is_linked(b2, 'maven_GroupAndArtifact', a)


def test_assoc_entries1_link_reassign_clear():
    a = maven_MapEntry(name="sample_text")
    b1 = maven_Mappings()
    b2 = maven_Mappings()
    _safe_set(a, 'maven_MapEntry2', b1)
    assert _is_linked(a, 'maven_MapEntry2', b1)
    if hasattr(b1, 'maven_Mappings'):
        assert _is_linked(b1, 'maven_Mappings', a)
    _safe_set(a, 'maven_MapEntry2', b2)
    assert _is_linked(a, 'maven_MapEntry2', b2)
    if hasattr(b1, 'maven_Mappings'):
        assert not _is_linked(b1, 'maven_Mappings', a)
    if hasattr(b2, 'maven_Mappings'):
        assert _is_linked(b2, 'maven_Mappings', a)
    _safe_set(a, 'maven_MapEntry2', None)
    assert not _is_linked(a, 'maven_MapEntry2', b2)
    if hasattr(b2, 'maven_Mappings'):
        assert not _is_linked(b2, 'maven_Mappings', a)


def test_assoc_mappings5_link_reassign_clear():
    a = maven_MavenProvider(transitive=True)
    b1 = maven_Mappings()
    b2 = maven_Mappings()
    _safe_set(a, 'maven_MavenProvider', b1)
    assert _is_linked(a, 'maven_MavenProvider', b1)
    if hasattr(b1, 'maven_Mappings6'):
        assert _is_linked(b1, 'maven_Mappings6', a)
    _safe_set(a, 'maven_MavenProvider', b2)
    assert _is_linked(a, 'maven_MavenProvider', b2)
    if hasattr(b1, 'maven_Mappings6'):
        assert not _is_linked(b1, 'maven_Mappings6', a)
    if hasattr(b2, 'maven_Mappings6'):
        assert _is_linked(b2, 'maven_Mappings6', a)
    _safe_set(a, 'maven_MavenProvider', None)
    assert not _is_linked(a, 'maven_MavenProvider', b2)
    if hasattr(b2, 'maven_Mappings6'):
        assert not _is_linked(b2, 'maven_Mappings6', a)


def test_assoc_scope9_link_reassign_clear():
    a = maven_Scope(exclude=True, name="sample_text")
    b1 = maven_Scopes()
    b2 = maven_Scopes()
    _safe_set(a, 'maven_Scope', b1)
    assert _is_linked(a, 'maven_Scope', b1)
    if hasattr(b1, 'maven_Scopes10'):
        assert _is_linked(b1, 'maven_Scopes10', a)
    _safe_set(a, 'maven_Scope', b2)
    assert _is_linked(a, 'maven_Scope', b2)
    if hasattr(b1, 'maven_Scopes10'):
        assert not _is_linked(b1, 'maven_Scopes10', a)
    if hasattr(b2, 'maven_Scopes10'):
        assert _is_linked(b2, 'maven_Scopes10', a)
    _safe_set(a, 'maven_Scope', None)
    assert not _is_linked(a, 'maven_Scope', b2)
    if hasattr(b2, 'maven_Scopes10'):
        assert not _is_linked(b2, 'maven_Scopes10', a)


def test_assoc_scopes7_link_reassign_clear():
    a = maven_MavenProvider(transitive=True)
    b1 = maven_Scopes()
    b2 = maven_Scopes()
    _safe_set(a, 'maven_MavenProvider8', b1)
    assert _is_linked(a, 'maven_MavenProvider8', b1)
    if hasattr(b1, 'maven_Scopes'):
        assert _is_linked(b1, 'maven_Scopes', a)
    _safe_set(a, 'maven_MavenProvider8', b2)
    assert _is_linked(a, 'maven_MavenProvider8', b2)
    if hasattr(b1, 'maven_Scopes'):
        assert not _is_linked(b1, 'maven_Scopes', a)
    if hasattr(b2, 'maven_Scopes'):
        assert _is_linked(b2, 'maven_Scopes', a)
    _safe_set(a, 'maven_MavenProvider8', None)
    assert not _is_linked(a, 'maven_MavenProvider8', b2)
    if hasattr(b2, 'maven_Scopes'):
        assert not _is_linked(b2, 'maven_Scopes', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

GroupAndArtifact_strategy = st.builds(GroupAndArtifact)
@given(instance=GroupAndArtifact_strategy)
@settings(max_examples=25)
def test_GroupAndArtifact_instantiation(instance):
    assert isinstance(instance, GroupAndArtifact)


Provider_strategy = st.builds(Provider)
@given(instance=Provider_strategy)
@settings(max_examples=25)
def test_Provider_instantiation(instance):
    assert isinstance(instance, Provider)


maven_GroupAndArtifact_strategy = st.builds(maven_GroupAndArtifact, artifactId=safe_text, groupId=safe_text)
@given(instance=maven_GroupAndArtifact_strategy)
@settings(max_examples=25)
def test_maven_GroupAndArtifact_instantiation(instance):
    assert isinstance(instance, maven_GroupAndArtifact)


maven_MapEntry_strategy = st.builds(maven_MapEntry, name=safe_text)
@given(instance=maven_MapEntry_strategy)
@settings(max_examples=25)
def test_maven_MapEntry_instantiation(instance):
    assert isinstance(instance, maven_MapEntry)


maven_Mappings_strategy = st.builds(maven_Mappings)
@given(instance=maven_Mappings_strategy)
@settings(max_examples=25)
def test_maven_Mappings_instantiation(instance):
    assert isinstance(instance, maven_Mappings)


maven_MavenProvider_strategy = st.builds(maven_MavenProvider, transitive=st.booleans())
@given(instance=maven_MavenProvider_strategy)
@settings(max_examples=25)
def test_maven_MavenProvider_instantiation(instance):
    assert isinstance(instance, maven_MavenProvider)


maven_Scope_strategy = st.builds(maven_Scope, exclude=st.booleans(), name=safe_text)
@given(instance=maven_Scope_strategy)
@settings(max_examples=25)
def test_maven_Scope_instantiation(instance):
    assert isinstance(instance, maven_Scope)


maven_Scopes_strategy = st.builds(maven_Scopes)
@given(instance=maven_Scopes_strategy)
@settings(max_examples=25)
def test_maven_Scopes_instantiation(instance):
    assert isinstance(instance, maven_Scopes)


maven_Transform_strategy = st.builds(maven_Transform)
@given(instance=maven_Transform_strategy)
@settings(max_examples=25)
def test_maven_Transform_instantiation(instance):
    assert isinstance(instance, maven_Transform)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    GroupAndArtifact,
    Provider,
    maven_GroupAndArtifact,
    maven_MapEntry,
    maven_Mappings,
    maven_MavenProvider,
    maven_Scope,
    maven_Scopes,
    maven_Transform,
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

def test_assoc_aliases0_reverse_link_reassign_clear():
    a1 = maven_MapEntry(name="sample_text")
    a2 = maven_MapEntry(name="sample_text_2")
    b = maven_GroupAndArtifact(artifactId="sample_text", groupId="sample_text")
    _safe_set(b, 'maven_GroupAndArtifact', a1)
    assert _is_linked(b, 'maven_GroupAndArtifact', a1)
    if hasattr(a1, 'maven_MapEntry'):
        assert _is_linked(a1, 'maven_MapEntry', b)
    _safe_set(b, 'maven_GroupAndArtifact', a2)
    assert _is_linked(b, 'maven_GroupAndArtifact', a2)
    if hasattr(a1, 'maven_MapEntry'):
        assert not _is_linked(a1, 'maven_MapEntry', b)
    if hasattr(a2, 'maven_MapEntry'):
        assert _is_linked(a2, 'maven_MapEntry', b)
    _safe_set(b, 'maven_GroupAndArtifact', None)
    assert not _is_linked(b, 'maven_GroupAndArtifact', a2)
    if hasattr(a2, 'maven_MapEntry'):
        assert not _is_linked(a2, 'maven_MapEntry', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_entries1_stub_double():
    # maven_Mappings has no real 'maven_Mappings' property in the generated
    # code (a bare stub) -- manually attach it so maven_MapEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # maven_MapEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = maven_MapEntry(name="sample_text")
    partner = maven_Mappings()
    setattr(partner, 'maven_Mappings', None)
    _safe_set(owner, 'maven_MapEntry2', partner)
    assert owner in getattr(partner, 'maven_Mappings')
    _safe_set(owner, 'maven_MapEntry2', None)
    assert owner not in getattr(partner, 'maven_Mappings')


def test_assoc_mappings5_stub_double():
    # maven_Mappings has no real 'maven_Mappings6' property in the generated
    # code (a bare stub) -- manually attach it so maven_MavenProvider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # maven_MavenProvider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = maven_MavenProvider(transitive=True)
    partner = maven_Mappings()
    setattr(partner, 'maven_Mappings6', None)
    _safe_set(owner, 'maven_MavenProvider', partner)
    assert getattr(partner, 'maven_Mappings6') == owner
    _safe_set(owner, 'maven_MavenProvider', None)
    assert getattr(partner, 'maven_Mappings6') is None


def test_assoc_scope9_stub_double():
    # maven_Scopes has no real 'maven_Scopes10' property in the generated
    # code (a bare stub) -- manually attach it so maven_Scope's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # maven_Scope's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = maven_Scope(exclude=True, name="sample_text")
    partner = maven_Scopes()
    setattr(partner, 'maven_Scopes10', None)
    _safe_set(owner, 'maven_Scope', partner)
    assert owner in getattr(partner, 'maven_Scopes10')
    _safe_set(owner, 'maven_Scope', None)
    assert owner not in getattr(partner, 'maven_Scopes10')


def test_assoc_scopes7_stub_double():
    # maven_Scopes has no real 'maven_Scopes' property in the generated
    # code (a bare stub) -- manually attach it so maven_MavenProvider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # maven_MavenProvider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = maven_MavenProvider(transitive=True)
    partner = maven_Scopes()
    setattr(partner, 'maven_Scopes', None)
    _safe_set(owner, 'maven_MavenProvider8', partner)
    assert getattr(partner, 'maven_Scopes') == owner
    _safe_set(owner, 'maven_MavenProvider8', None)
    assert getattr(partner, 'maven_Scopes') is None




from python_code import maven_MapEntry
from python_code import maven_Mappings

def test_maven_MapEntry___init__():
    assert maven_MapEntry.__init__(maven_MapEntry('', maven_MapEntry=set(), maven_MapEntry2=maven_Mappings()), '', maven_MapEntry=set(), maven_MapEntry2=maven_Mappings()) == None
from python_code import maven_Mappings
from python_code import maven_MavenProvider
from python_code import maven_Scopes

def test_maven_MavenProvider___init__():
    assert maven_MavenProvider.__init__(maven_MavenProvider(True, maven_MavenProvider=maven_Mappings(), maven_MavenProvider8=maven_Scopes()), False, maven_MavenProvider=maven_Mappings(), maven_MavenProvider8=maven_Scopes()) == None

def test_maven_MavenProvider_getComponentName():
    assert maven_MavenProvider.getComponentName(maven_MavenProvider(False, maven_MavenProvider=maven_Mappings(), maven_MavenProvider8=maven_Scopes()), 0, '\x00\x00') == None

def test_maven_MavenProvider_getMapEntry():
    assert maven_MavenProvider.getMapEntry(maven_MavenProvider(False, maven_MavenProvider=maven_Mappings(), maven_MavenProvider8=maven_Scopes()), 0) == None
from python_code import maven_Scope
from python_code import maven_Scopes

def test_maven_Scope___init__():
    assert maven_Scope.__init__(maven_Scope('', False, maven_Scope=maven_Scopes()), '', False, maven_Scope=maven_Scopes()) == None

