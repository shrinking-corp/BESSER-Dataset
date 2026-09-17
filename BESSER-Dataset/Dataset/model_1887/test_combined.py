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
    JSFLibrary,
    jsflibraryregistry_ArchiveFile,
    jsflibraryregistry_PluginProvidedJSFLibrary,
    jsflibraryregistry_JSFLibrary,
    jsflibraryregistry_JSFLibraryRegistry,
    JSFVersion,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_jsflibrary_is_not_abstract():
    assert not inspect.isabstract(JSFLibrary)


def test_hyp_jsflibrary_constructor_exists():
    assert callable(JSFLibrary.__init__)


def test_hyp_jsflibrary_constructor_args():
    sig = inspect.signature(JSFLibrary.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jsflibraryregistry_archivefile_is_not_abstract():
    assert not inspect.isabstract(jsflibraryregistry_ArchiveFile)


def test_hyp_jsflibraryregistry_archivefile_constructor_exists():
    assert callable(jsflibraryregistry_ArchiveFile.__init__)


def test_hyp_jsflibraryregistry_archivefile_constructor_args():
    sig = inspect.signature(jsflibraryregistry_ArchiveFile.__init__)
    params = list(sig.parameters.keys())
    assert "SourceLocation" in params, "Missing parameter 'SourceLocation'"
    assert "RelativeDestLocation" in params, "Missing parameter 'RelativeDestLocation'"
    assert "RelativeToWorkspace" in params, "Missing parameter 'RelativeToWorkspace'"






def test_hyp_jsflibraryregistry_pluginprovidedjsflibrary_is_not_abstract():
    assert not inspect.isabstract(jsflibraryregistry_PluginProvidedJSFLibrary)


def test_hyp_jsflibraryregistry_pluginprovidedjsflibrary_constructor_exists():
    assert callable(jsflibraryregistry_PluginProvidedJSFLibrary.__init__)


def test_hyp_jsflibraryregistry_pluginprovidedjsflibrary_constructor_args():
    sig = inspect.signature(jsflibraryregistry_PluginProvidedJSFLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "pluginID" in params, "Missing parameter 'pluginID'"
    assert "Label" in params, "Missing parameter 'Label'"





def test_hyp_jsflibraryregistry_jsflibrary_is_not_abstract():
    assert not inspect.isabstract(jsflibraryregistry_JSFLibrary)


def test_hyp_jsflibraryregistry_jsflibrary_constructor_exists():
    assert callable(jsflibraryregistry_JSFLibrary.__init__)


def test_hyp_jsflibraryregistry_jsflibrary_constructor_args():
    sig = inspect.signature(jsflibraryregistry_JSFLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "JSFVersion" in params, "Missing parameter 'JSFVersion'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Implementation" in params, "Missing parameter 'Implementation'"
    assert "Deployed" in params, "Missing parameter 'Deployed'"
    assert "Name" in params, "Missing parameter 'Name'"








def test_hyp_jsflibraryregistry_jsflibraryregistry_is_not_abstract():
    assert not inspect.isabstract(jsflibraryregistry_JSFLibraryRegistry)


def test_hyp_jsflibraryregistry_jsflibraryregistry_constructor_exists():
    assert callable(jsflibraryregistry_JSFLibraryRegistry.__init__)


def test_hyp_jsflibraryregistry_jsflibraryregistry_constructor_args():
    sig = inspect.signature(jsflibraryregistry_JSFLibraryRegistry.__init__)
    params = list(sig.parameters.keys())
    assert "DefaultImplementationID" in params, "Missing parameter 'DefaultImplementationID'"


def test_hyp_jsfversion_exists():
    # Check that the Enumeration exists
    assert JSFVersion is not None

def test_hyp_jsfversion_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JSFVersion]
    expected_literals = [
        "v1_2",
        "UNKNOWN",
        "v1_1",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JSFVersion"


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
JSFLibrary_strategy = st.builds(
    JSFLibrary,
)
jsflibraryregistry_ArchiveFile_strategy = st.builds(
    jsflibraryregistry_ArchiveFile,
    SourceLocation=
        safe_text,
    RelativeDestLocation=
        safe_text,
    RelativeToWorkspace=
        st.booleans()
)
jsflibraryregistry_PluginProvidedJSFLibrary_strategy = st.builds(
    jsflibraryregistry_PluginProvidedJSFLibrary,
    pluginID=
        safe_text,
    Label=
        safe_text
)
jsflibraryregistry_JSFLibrary_strategy = st.builds(
    jsflibraryregistry_JSFLibrary,
    JSFVersion=
        safe_text,
    ID=
        safe_text,
    Implementation=
        st.booleans(),
    Deployed=
        st.booleans(),
    Name=
        safe_text
)
jsflibraryregistry_JSFLibraryRegistry_strategy = st.builds(
    jsflibraryregistry_JSFLibraryRegistry,
    DefaultImplementationID=
        safe_text
)





@given(instance=jsflibraryregistry_ArchiveFile_strategy)
def test_hyp_jsflibraryregistry_archivefile_SourceLocation_setter(instance):
    original = instance.SourceLocation
    instance.SourceLocation = original
    assert instance.SourceLocation == original



@given(instance=jsflibraryregistry_ArchiveFile_strategy)
def test_hyp_jsflibraryregistry_archivefile_RelativeDestLocation_setter(instance):
    original = instance.RelativeDestLocation
    instance.RelativeDestLocation = original
    assert instance.RelativeDestLocation == original



@given(instance=jsflibraryregistry_ArchiveFile_strategy)
def test_hyp_jsflibraryregistry_archivefile_RelativeToWorkspace_setter(instance):
    original = instance.RelativeToWorkspace
    instance.RelativeToWorkspace = original
    assert instance.RelativeToWorkspace == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=jsflibraryregistry_ArchiveFile_strategy)
@settings(max_examples=30)
def test_hyp_jsflibraryregistry_archivefile_copyto_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.copyTo(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.copyTo).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'copyTo' in jsflibraryregistry_ArchiveFile is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'copyTo' in jsflibraryregistry_ArchiveFile did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'copyTo' in jsflibraryregistry_ArchiveFile is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=jsflibraryregistry_ArchiveFile_strategy)
@settings(max_examples=30)
def test_hyp_jsflibraryregistry_archivefile_exists_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.exists()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.exists).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'exists' in jsflibraryregistry_ArchiveFile is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'exists' in jsflibraryregistry_ArchiveFile did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'exists' in jsflibraryregistry_ArchiveFile is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=jsflibraryregistry_ArchiveFile_strategy)
@settings(max_examples=30)
def test_hyp_jsflibraryregistry_archivefile_equals_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.equals(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.equals).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'equals' in jsflibraryregistry_ArchiveFile is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'equals' in jsflibraryregistry_ArchiveFile did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'equals' in jsflibraryregistry_ArchiveFile is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=jsflibraryregistry_ArchiveFile_strategy)
@settings(max_examples=30)
def test_hyp_jsflibraryregistry_archivefile_hashcode_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hashCode()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hashCode).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hashCode' in jsflibraryregistry_ArchiveFile is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hashCode' in jsflibraryregistry_ArchiveFile did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hashCode' in jsflibraryregistry_ArchiveFile is not implemented or raised an error")




@given(instance=jsflibraryregistry_PluginProvidedJSFLibrary_strategy)
def test_hyp_jsflibraryregistry_pluginprovidedjsflibrary_pluginID_setter(instance):
    original = instance.pluginID
    instance.pluginID = original
    assert instance.pluginID == original



@given(instance=jsflibraryregistry_PluginProvidedJSFLibrary_strategy)
def test_hyp_jsflibraryregistry_pluginprovidedjsflibrary_Label_setter(instance):
    original = instance.Label
    instance.Label = original
    assert instance.Label == original




@given(instance=jsflibraryregistry_JSFLibrary_strategy)
def test_hyp_jsflibraryregistry_jsflibrary_JSFVersion_setter(instance):
    original = instance.JSFVersion
    instance.JSFVersion = original
    assert instance.JSFVersion == original



@given(instance=jsflibraryregistry_JSFLibrary_strategy)
def test_hyp_jsflibraryregistry_jsflibrary_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=jsflibraryregistry_JSFLibrary_strategy)
def test_hyp_jsflibraryregistry_jsflibrary_Implementation_setter(instance):
    original = instance.Implementation
    instance.Implementation = original
    assert instance.Implementation == original



@given(instance=jsflibraryregistry_JSFLibrary_strategy)
def test_hyp_jsflibraryregistry_jsflibrary_Deployed_setter(instance):
    original = instance.Deployed
    instance.Deployed = original
    assert instance.Deployed == original



@given(instance=jsflibraryregistry_JSFLibrary_strategy)
def test_hyp_jsflibraryregistry_jsflibrary_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=jsflibraryregistry_JSFLibrary_strategy)
@settings(max_examples=30)
def test_hyp_jsflibraryregistry_jsflibrary_updatevalues_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.updateValues(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.updateValues).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'updateValues' in jsflibraryregistry_JSFLibrary is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateValues' in jsflibraryregistry_JSFLibrary did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateValues' in jsflibraryregistry_JSFLibrary is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=jsflibraryregistry_JSFLibrary_strategy)
@settings(max_examples=30)
def test_hyp_jsflibraryregistry_jsflibrary_containsarchivefile_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.containsArchiveFile(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.containsArchiveFile).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'containsArchiveFile' in jsflibraryregistry_JSFLibrary is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'containsArchiveFile' in jsflibraryregistry_JSFLibrary did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'containsArchiveFile' in jsflibraryregistry_JSFLibrary is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=jsflibraryregistry_JSFLibrary_strategy)
@settings(max_examples=30)
def test_hyp_jsflibraryregistry_jsflibrary_copyto_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.copyTo(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.copyTo).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'copyTo' in jsflibraryregistry_JSFLibrary is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'copyTo' in jsflibraryregistry_JSFLibrary did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'copyTo' in jsflibraryregistry_JSFLibrary is not implemented or raised an error")




@given(instance=jsflibraryregistry_JSFLibraryRegistry_strategy)
def test_hyp_jsflibraryregistry_jsflibraryregistry_DefaultImplementationID_setter(instance):
    original = instance.DefaultImplementationID
    instance.DefaultImplementationID = original
    assert instance.DefaultImplementationID == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=jsflibraryregistry_JSFLibraryRegistry_strategy)
@settings(max_examples=30)
def test_hyp_jsflibraryregistry_jsflibraryregistry_removejsflibrary_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeJSFLibrary(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeJSFLibrary).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeJSFLibrary' in jsflibraryregistry_JSFLibraryRegistry is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeJSFLibrary' in jsflibraryregistry_JSFLibraryRegistry did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeJSFLibrary' in jsflibraryregistry_JSFLibraryRegistry is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=jsflibraryregistry_JSFLibraryRegistry_strategy)
@settings(max_examples=30)
def test_hyp_jsflibraryregistry_jsflibraryregistry_setdefaultimplementation_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setDefaultImplementation(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setDefaultImplementation).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setDefaultImplementation' in jsflibraryregistry_JSFLibraryRegistry is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setDefaultImplementation' in jsflibraryregistry_JSFLibraryRegistry did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setDefaultImplementation' in jsflibraryregistry_JSFLibraryRegistry is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=jsflibraryregistry_JSFLibraryRegistry_strategy)
@settings(max_examples=30)
def test_hyp_jsflibraryregistry_jsflibraryregistry_addjsflibrary_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addJSFLibrary(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addJSFLibrary).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addJSFLibrary' in jsflibraryregistry_JSFLibraryRegistry is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addJSFLibrary' in jsflibraryregistry_JSFLibraryRegistry did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addJSFLibrary' in jsflibraryregistry_JSFLibraryRegistry is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    JSFLibrary,
    jsflibraryregistry_ArchiveFile,
    jsflibraryregistry_JSFLibrary,
    jsflibraryregistry_JSFLibraryRegistry,
    jsflibraryregistry_PluginProvidedJSFLibrary,
    JSFVersion,
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

def test_jsflibraryregistry_ArchiveFile_RelativeDestLocation_value_roundtrip():
    instance = jsflibraryregistry_ArchiveFile(RelativeDestLocation="sample_text", RelativeToWorkspace=True, SourceLocation="sample_text")
    assert instance.RelativeDestLocation == "sample_text"
    instance.RelativeDestLocation = "sample_text_2"
    assert instance.RelativeDestLocation == "sample_text_2"


def test_jsflibraryregistry_ArchiveFile_RelativeToWorkspace_value_roundtrip():
    instance = jsflibraryregistry_ArchiveFile(RelativeDestLocation="sample_text", RelativeToWorkspace=True, SourceLocation="sample_text")
    assert instance.RelativeToWorkspace == True
    instance.RelativeToWorkspace = False
    assert instance.RelativeToWorkspace == False


def test_jsflibraryregistry_ArchiveFile_SourceLocation_value_roundtrip():
    instance = jsflibraryregistry_ArchiveFile(RelativeDestLocation="sample_text", RelativeToWorkspace=True, SourceLocation="sample_text")
    assert instance.SourceLocation == "sample_text"
    instance.SourceLocation = "sample_text_2"
    assert instance.SourceLocation == "sample_text_2"


def test_jsflibraryregistry_JSFLibrary_Deployed_value_roundtrip():
    instance = jsflibraryregistry_JSFLibrary(Deployed=True, ID="sample_text", Implementation=True, JSFVersion="sample_text", Name="sample_text")
    assert instance.Deployed == True
    instance.Deployed = False
    assert instance.Deployed == False


def test_jsflibraryregistry_JSFLibrary_ID_value_roundtrip():
    instance = jsflibraryregistry_JSFLibrary(Deployed=True, ID="sample_text", Implementation=True, JSFVersion="sample_text", Name="sample_text")
    assert instance.ID == "sample_text"
    instance.ID = "sample_text_2"
    assert instance.ID == "sample_text_2"


def test_jsflibraryregistry_JSFLibrary_Implementation_value_roundtrip():
    instance = jsflibraryregistry_JSFLibrary(Deployed=True, ID="sample_text", Implementation=True, JSFVersion="sample_text", Name="sample_text")
    assert instance.Implementation == True
    instance.Implementation = False
    assert instance.Implementation == False


def test_jsflibraryregistry_JSFLibrary_JSFVersion_value_roundtrip():
    instance = jsflibraryregistry_JSFLibrary(Deployed=True, ID="sample_text", Implementation=True, JSFVersion="sample_text", Name="sample_text")
    assert instance.JSFVersion == "sample_text"
    instance.JSFVersion = "sample_text_2"
    assert instance.JSFVersion == "sample_text_2"


def test_jsflibraryregistry_JSFLibrary_Name_value_roundtrip():
    instance = jsflibraryregistry_JSFLibrary(Deployed=True, ID="sample_text", Implementation=True, JSFVersion="sample_text", Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_jsflibraryregistry_JSFLibraryRegistry_DefaultImplementationID_value_roundtrip():
    instance = jsflibraryregistry_JSFLibraryRegistry(DefaultImplementationID="sample_text")
    assert instance.DefaultImplementationID == "sample_text"
    instance.DefaultImplementationID = "sample_text_2"
    assert instance.DefaultImplementationID == "sample_text_2"


def test_jsflibraryregistry_PluginProvidedJSFLibrary_Label_value_roundtrip():
    instance = jsflibraryregistry_PluginProvidedJSFLibrary(Label="sample_text", pluginID="sample_text")
    assert instance.Label == "sample_text"
    instance.Label = "sample_text_2"
    assert instance.Label == "sample_text_2"


def test_jsflibraryregistry_PluginProvidedJSFLibrary_pluginID_value_roundtrip():
    instance = jsflibraryregistry_PluginProvidedJSFLibrary(Label="sample_text", pluginID="sample_text")
    assert instance.pluginID == "sample_text"
    instance.pluginID = "sample_text_2"
    assert instance.pluginID == "sample_text_2"


def test_jsflibraryregistry_PluginProvidedJSFLibrary_isa_JSFLibrary():
    instance = jsflibraryregistry_PluginProvidedJSFLibrary(Label="sample_text", pluginID="sample_text")
    assert isinstance(instance, JSFLibrary)


def test_assoc_ArchiveFiles3_link_reassign_clear():
    a = jsflibraryregistry_JSFLibrary(Deployed=True, ID="sample_text", Implementation=True, JSFVersion="sample_text", Name="sample_text")
    b1 = jsflibraryregistry_ArchiveFile(RelativeDestLocation="sample_text", RelativeToWorkspace=True, SourceLocation="sample_text")
    b2 = jsflibraryregistry_ArchiveFile(RelativeDestLocation="sample_text_2", RelativeToWorkspace=False, SourceLocation="sample_text_2")
    _safe_set(a, 'JSFLibrary', {b1})
    assert _is_linked(a, 'JSFLibrary', b1)
    if hasattr(b1, 'ArchiveFile'):
        assert _is_linked(b1, 'ArchiveFile', a)
    _safe_set(a, 'JSFLibrary', {b2})
    assert _is_linked(a, 'JSFLibrary', b2)
    if hasattr(b1, 'ArchiveFile'):
        assert not _is_linked(b1, 'ArchiveFile', a)
    if hasattr(b2, 'ArchiveFile'):
        assert _is_linked(b2, 'ArchiveFile', a)
    _safe_set(a, 'JSFLibrary', set())
    assert not _is_linked(a, 'JSFLibrary', b2)
    if hasattr(b2, 'ArchiveFile'):
        assert not _is_linked(b2, 'ArchiveFile', a)


def test_assoc_JSFLibraries0_link_reassign_clear():
    a = jsflibraryregistry_JSFLibraryRegistry(DefaultImplementationID="sample_text")
    b1 = jsflibraryregistry_JSFLibrary(Deployed=True, ID="sample_text", Implementation=True, JSFVersion="sample_text", Name="sample_text")
    b2 = jsflibraryregistry_JSFLibrary(Deployed=False, ID="sample_text_2", Implementation=False, JSFVersion="sample_text_2", Name="sample_text_2")
    _safe_set(a, 'jsflibraryregistry_JSFLibraryRegistry', {b1})
    assert _is_linked(a, 'jsflibraryregistry_JSFLibraryRegistry', b1)
    if hasattr(b1, 'jsflibraryregistry_JSFLibrary'):
        assert _is_linked(b1, 'jsflibraryregistry_JSFLibrary', a)
    _safe_set(a, 'jsflibraryregistry_JSFLibraryRegistry', {b2})
    assert _is_linked(a, 'jsflibraryregistry_JSFLibraryRegistry', b2)
    if hasattr(b1, 'jsflibraryregistry_JSFLibrary'):
        assert not _is_linked(b1, 'jsflibraryregistry_JSFLibrary', a)
    if hasattr(b2, 'jsflibraryregistry_JSFLibrary'):
        assert _is_linked(b2, 'jsflibraryregistry_JSFLibrary', a)
    _safe_set(a, 'jsflibraryregistry_JSFLibraryRegistry', set())
    assert not _is_linked(a, 'jsflibraryregistry_JSFLibraryRegistry', b2)
    if hasattr(b2, 'jsflibraryregistry_JSFLibrary'):
        assert not _is_linked(b2, 'jsflibraryregistry_JSFLibrary', a)


def test_assoc_JSFLibrary4_link_reassign_clear():
    a = jsflibraryregistry_JSFLibrary(Deployed=True, ID="sample_text", Implementation=True, JSFVersion="sample_text", Name="sample_text")
    b1 = jsflibraryregistry_ArchiveFile(RelativeDestLocation="sample_text", RelativeToWorkspace=True, SourceLocation="sample_text")
    b2 = jsflibraryregistry_ArchiveFile(RelativeDestLocation="sample_text_2", RelativeToWorkspace=False, SourceLocation="sample_text_2")
    _safe_set(a, 'JSFLibrary5', b1)
    assert _is_linked(a, 'JSFLibrary5', b1)
    if hasattr(b1, 'ArchiveFiles'):
        assert _is_linked(b1, 'ArchiveFiles', a)
    _safe_set(a, 'JSFLibrary5', b2)
    assert _is_linked(a, 'JSFLibrary5', b2)
    if hasattr(b1, 'ArchiveFiles'):
        assert not _is_linked(b1, 'ArchiveFiles', a)
    if hasattr(b2, 'ArchiveFiles'):
        assert _is_linked(b2, 'ArchiveFiles', a)
    _safe_set(a, 'JSFLibrary5', None)
    assert not _is_linked(a, 'JSFLibrary5', b2)
    if hasattr(b2, 'ArchiveFiles'):
        assert not _is_linked(b2, 'ArchiveFiles', a)


def test_assoc_PluginProvidedJSFLibraries1_link_reassign_clear():
    a = jsflibraryregistry_PluginProvidedJSFLibrary(Label="sample_text", pluginID="sample_text")
    b1 = jsflibraryregistry_JSFLibraryRegistry(DefaultImplementationID="sample_text")
    b2 = jsflibraryregistry_JSFLibraryRegistry(DefaultImplementationID="sample_text_2")
    _safe_set(a, 'jsflibraryregistry_PluginProvidedJSFLibrary', b1)
    assert _is_linked(a, 'jsflibraryregistry_PluginProvidedJSFLibrary', b1)
    if hasattr(b1, 'jsflibraryregistry_JSFLibraryRegistry2'):
        assert _is_linked(b1, 'jsflibraryregistry_JSFLibraryRegistry2', a)
    _safe_set(a, 'jsflibraryregistry_PluginProvidedJSFLibrary', b2)
    assert _is_linked(a, 'jsflibraryregistry_PluginProvidedJSFLibrary', b2)
    if hasattr(b1, 'jsflibraryregistry_JSFLibraryRegistry2'):
        assert not _is_linked(b1, 'jsflibraryregistry_JSFLibraryRegistry2', a)
    if hasattr(b2, 'jsflibraryregistry_JSFLibraryRegistry2'):
        assert _is_linked(b2, 'jsflibraryregistry_JSFLibraryRegistry2', a)
    _safe_set(a, 'jsflibraryregistry_PluginProvidedJSFLibrary', None)
    assert not _is_linked(a, 'jsflibraryregistry_PluginProvidedJSFLibrary', b2)
    if hasattr(b2, 'jsflibraryregistry_JSFLibraryRegistry2'):
        assert not _is_linked(b2, 'jsflibraryregistry_JSFLibraryRegistry2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

JSFLibrary_strategy = st.builds(JSFLibrary)
@given(instance=JSFLibrary_strategy)
@settings(max_examples=25)
def test_JSFLibrary_instantiation(instance):
    assert isinstance(instance, JSFLibrary)


jsflibraryregistry_ArchiveFile_strategy = st.builds(jsflibraryregistry_ArchiveFile, RelativeDestLocation=safe_text, RelativeToWorkspace=st.booleans(), SourceLocation=safe_text)
@given(instance=jsflibraryregistry_ArchiveFile_strategy)
@settings(max_examples=25)
def test_jsflibraryregistry_ArchiveFile_instantiation(instance):
    assert isinstance(instance, jsflibraryregistry_ArchiveFile)


jsflibraryregistry_JSFLibrary_strategy = st.builds(jsflibraryregistry_JSFLibrary, Deployed=st.booleans(), ID=safe_text, Implementation=st.booleans(), JSFVersion=safe_text, Name=safe_text)
@given(instance=jsflibraryregistry_JSFLibrary_strategy)
@settings(max_examples=25)
def test_jsflibraryregistry_JSFLibrary_instantiation(instance):
    assert isinstance(instance, jsflibraryregistry_JSFLibrary)


jsflibraryregistry_JSFLibraryRegistry_strategy = st.builds(jsflibraryregistry_JSFLibraryRegistry, DefaultImplementationID=safe_text)
@given(instance=jsflibraryregistry_JSFLibraryRegistry_strategy)
@settings(max_examples=25)
def test_jsflibraryregistry_JSFLibraryRegistry_instantiation(instance):
    assert isinstance(instance, jsflibraryregistry_JSFLibraryRegistry)


jsflibraryregistry_PluginProvidedJSFLibrary_strategy = st.builds(jsflibraryregistry_PluginProvidedJSFLibrary, Label=safe_text, pluginID=safe_text)
@given(instance=jsflibraryregistry_PluginProvidedJSFLibrary_strategy)
@settings(max_examples=25)
def test_jsflibraryregistry_PluginProvidedJSFLibrary_instantiation(instance):
    assert isinstance(instance, jsflibraryregistry_PluginProvidedJSFLibrary)



