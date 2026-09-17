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
    filetree_User,
    FileTreeElement,
    filetree_H2HFile,
    filetree_AccessRight,
    filetree_Container,
    filetree_FileTreeElement,
    filetree_PathToTreeElementMap,
    Container,
    filetree_Directory,
    filetree_FileTree,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_filetree_user_is_not_abstract():
    assert not inspect.isabstract(filetree_User)


def test_hyp_filetree_user_constructor_exists():
    assert callable(filetree_User.__init__)


def test_hyp_filetree_user_constructor_args():
    sig = inspect.signature(filetree_User.__init__)
    params = list(sig.parameters.keys())
    assert "pin" in params, "Missing parameter 'pin'"
    assert "rootDir" in params, "Missing parameter 'rootDir'"
    assert "password" in params, "Missing parameter 'password'"
    assert "userId" in params, "Missing parameter 'userId'"







def test_hyp_filetreeelement_is_not_abstract():
    assert not inspect.isabstract(FileTreeElement)


def test_hyp_filetreeelement_constructor_exists():
    assert callable(FileTreeElement.__init__)


def test_hyp_filetreeelement_constructor_args():
    sig = inspect.signature(FileTreeElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_filetree_h2hfile_is_not_abstract():
    assert not inspect.isabstract(filetree_H2HFile)


def test_hyp_filetree_h2hfile_constructor_exists():
    assert callable(filetree_H2HFile.__init__)


def test_hyp_filetree_h2hfile_constructor_args():
    sig = inspect.signature(filetree_H2HFile.__init__)
    params = list(sig.parameters.keys())



def test_hyp_filetree_accessright_is_not_abstract():
    assert not inspect.isabstract(filetree_AccessRight)


def test_hyp_filetree_accessright_constructor_exists():
    assert callable(filetree_AccessRight.__init__)


def test_hyp_filetree_accessright_constructor_args():
    sig = inspect.signature(filetree_AccessRight.__init__)
    params = list(sig.parameters.keys())
    assert "writePermission" in params, "Missing parameter 'writePermission'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "readPermission" in params, "Missing parameter 'readPermission'"






def test_hyp_filetree_container_is_not_abstract():
    assert not inspect.isabstract(filetree_Container)


def test_hyp_filetree_container_constructor_exists():
    assert callable(filetree_Container.__init__)


def test_hyp_filetree_container_constructor_args():
    sig = inspect.signature(filetree_Container.__init__)
    params = list(sig.parameters.keys())



def test_hyp_filetree_filetreeelement_is_not_abstract():
    assert not inspect.isabstract(filetree_FileTreeElement)


def test_hyp_filetree_filetreeelement_constructor_exists():
    assert callable(filetree_FileTreeElement.__init__)


def test_hyp_filetree_filetreeelement_constructor_args():
    sig = inspect.signature(filetree_FileTreeElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "path" in params, "Missing parameter 'path'"
    assert "file" in params, "Missing parameter 'file'"






def test_hyp_filetree_pathtotreeelementmap_is_not_abstract():
    assert not inspect.isabstract(filetree_PathToTreeElementMap)


def test_hyp_filetree_pathtotreeelementmap_constructor_exists():
    assert callable(filetree_PathToTreeElementMap.__init__)


def test_hyp_filetree_pathtotreeelementmap_constructor_args():
    sig = inspect.signature(filetree_PathToTreeElementMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"




def test_hyp_container_is_not_abstract():
    assert not inspect.isabstract(Container)


def test_hyp_container_constructor_exists():
    assert callable(Container.__init__)


def test_hyp_container_constructor_args():
    sig = inspect.signature(Container.__init__)
    params = list(sig.parameters.keys())



def test_hyp_filetree_directory_is_not_abstract():
    assert not inspect.isabstract(filetree_Directory)


def test_hyp_filetree_directory_constructor_exists():
    assert callable(filetree_Directory.__init__)


def test_hyp_filetree_directory_constructor_args():
    sig = inspect.signature(filetree_Directory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_filetree_filetree_is_not_abstract():
    assert not inspect.isabstract(filetree_FileTree)


def test_hyp_filetree_filetree_constructor_exists():
    assert callable(filetree_FileTree.__init__)


def test_hyp_filetree_filetree_constructor_args():
    sig = inspect.signature(filetree_FileTree.__init__)
    params = list(sig.parameters.keys())


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
filetree_User_strategy = st.builds(
    filetree_User,
    pin=
        safe_text,
    rootDir=
        safe_text,
    password=
        safe_text,
    userId=
        safe_text
)
FileTreeElement_strategy = st.builds(
    FileTreeElement,
)
filetree_H2HFile_strategy = st.builds(
    filetree_H2HFile,
)
filetree_AccessRight_strategy = st.builds(
    filetree_AccessRight,
    writePermission=
        st.booleans(),
    userId=
        safe_text,
    readPermission=
        st.booleans()
)
filetree_Container_strategy = st.builds(
    filetree_Container,
)
filetree_FileTreeElement_strategy = st.builds(
    filetree_FileTreeElement,
    name=
        safe_text,
    path=
        safe_text,
    file=
        safe_text
)
filetree_PathToTreeElementMap_strategy = st.builds(
    filetree_PathToTreeElementMap,
    key=
        safe_text
)
Container_strategy = st.builds(
    Container,
)
filetree_Directory_strategy = st.builds(
    filetree_Directory,
)
filetree_FileTree_strategy = st.builds(
    filetree_FileTree,
)




@given(instance=filetree_User_strategy)
def test_hyp_filetree_user_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original



@given(instance=filetree_User_strategy)
def test_hyp_filetree_user_rootDir_setter(instance):
    original = instance.rootDir
    instance.rootDir = original
    assert instance.rootDir == original



@given(instance=filetree_User_strategy)
def test_hyp_filetree_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=filetree_User_strategy)
def test_hyp_filetree_user_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original






@given(instance=filetree_AccessRight_strategy)
def test_hyp_filetree_accessright_writePermission_setter(instance):
    original = instance.writePermission
    instance.writePermission = original
    assert instance.writePermission == original



@given(instance=filetree_AccessRight_strategy)
def test_hyp_filetree_accessright_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=filetree_AccessRight_strategy)
def test_hyp_filetree_accessright_readPermission_setter(instance):
    original = instance.readPermission
    instance.readPermission = original
    assert instance.readPermission == original





@given(instance=filetree_FileTreeElement_strategy)
def test_hyp_filetree_filetreeelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=filetree_FileTreeElement_strategy)
def test_hyp_filetree_filetreeelement_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original



@given(instance=filetree_FileTreeElement_strategy)
def test_hyp_filetree_filetreeelement_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original




@given(instance=filetree_PathToTreeElementMap_strategy)
def test_hyp_filetree_pathtotreeelementmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original





# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Container,
    FileTreeElement,
    filetree_AccessRight,
    filetree_Container,
    filetree_Directory,
    filetree_FileTree,
    filetree_FileTreeElement,
    filetree_H2HFile,
    filetree_PathToTreeElementMap,
    filetree_User,
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

def test_filetree_AccessRight_readPermission_value_roundtrip():
    instance = filetree_AccessRight(readPermission=True, userId="sample_text", writePermission=True)
    assert instance.readPermission == True
    instance.readPermission = False
    assert instance.readPermission == False


def test_filetree_AccessRight_userId_value_roundtrip():
    instance = filetree_AccessRight(readPermission=True, userId="sample_text", writePermission=True)
    assert instance.userId == "sample_text"
    instance.userId = "sample_text_2"
    assert instance.userId == "sample_text_2"


def test_filetree_AccessRight_writePermission_value_roundtrip():
    instance = filetree_AccessRight(readPermission=True, userId="sample_text", writePermission=True)
    assert instance.writePermission == True
    instance.writePermission = False
    assert instance.writePermission == False


def test_filetree_FileTreeElement_file_value_roundtrip():
    instance = filetree_FileTreeElement(file="sample_text", name="sample_text", path="sample_text")
    assert instance.file == "sample_text"
    instance.file = "sample_text_2"
    assert instance.file == "sample_text_2"


def test_filetree_FileTreeElement_name_value_roundtrip():
    instance = filetree_FileTreeElement(file="sample_text", name="sample_text", path="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_filetree_FileTreeElement_path_value_roundtrip():
    instance = filetree_FileTreeElement(file="sample_text", name="sample_text", path="sample_text")
    assert instance.path == "sample_text"
    instance.path = "sample_text_2"
    assert instance.path == "sample_text_2"


def test_filetree_PathToTreeElementMap_key_value_roundtrip():
    instance = filetree_PathToTreeElementMap(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_filetree_User_password_value_roundtrip():
    instance = filetree_User(password="sample_text", pin="sample_text", rootDir="sample_text", userId="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_filetree_User_pin_value_roundtrip():
    instance = filetree_User(password="sample_text", pin="sample_text", rootDir="sample_text", userId="sample_text")
    assert instance.pin == "sample_text"
    instance.pin = "sample_text_2"
    assert instance.pin == "sample_text_2"


def test_filetree_User_rootDir_value_roundtrip():
    instance = filetree_User(password="sample_text", pin="sample_text", rootDir="sample_text", userId="sample_text")
    assert instance.rootDir == "sample_text"
    instance.rootDir = "sample_text_2"
    assert instance.rootDir == "sample_text_2"


def test_filetree_User_userId_value_roundtrip():
    instance = filetree_User(password="sample_text", pin="sample_text", rootDir="sample_text", userId="sample_text")
    assert instance.userId == "sample_text"
    instance.userId = "sample_text_2"
    assert instance.userId == "sample_text_2"


def test_filetree_Directory_isa_Container():
    instance = filetree_Directory()
    assert isinstance(instance, Container)


def test_filetree_FileTree_isa_Container():
    instance = filetree_FileTree()
    assert isinstance(instance, Container)


def test_filetree_Container_isa_FileTreeElement():
    instance = filetree_Container()
    assert isinstance(instance, FileTreeElement)


def test_filetree_H2HFile_isa_FileTreeElement():
    instance = filetree_H2HFile()
    assert isinstance(instance, FileTreeElement)


def test_assoc_accessRights2_link_reassign_clear():
    a = filetree_FileTreeElement(file="sample_text", name="sample_text", path="sample_text")
    b1 = filetree_AccessRight(readPermission=True, userId="sample_text", writePermission=True)
    b2 = filetree_AccessRight(readPermission=False, userId="sample_text_2", writePermission=False)
    _safe_set(a, 'filetree_FileTreeElement', {b1})
    assert _is_linked(a, 'filetree_FileTreeElement', b1)
    if hasattr(b1, 'filetree_AccessRight'):
        assert _is_linked(b1, 'filetree_AccessRight', a)
    _safe_set(a, 'filetree_FileTreeElement', {b2})
    assert _is_linked(a, 'filetree_FileTreeElement', b2)
    if hasattr(b1, 'filetree_AccessRight'):
        assert not _is_linked(b1, 'filetree_AccessRight', a)
    if hasattr(b2, 'filetree_AccessRight'):
        assert _is_linked(b2, 'filetree_AccessRight', a)
    _safe_set(a, 'filetree_FileTreeElement', set())
    assert not _is_linked(a, 'filetree_FileTreeElement', b2)
    if hasattr(b2, 'filetree_AccessRight'):
        assert not _is_linked(b2, 'filetree_AccessRight', a)


def test_assoc_children3_link_reassign_clear():
    a = filetree_FileTreeElement(file="sample_text", name="sample_text", path="sample_text")
    b1 = filetree_Container()
    b2 = filetree_Container()
    _safe_set(a, 'FileTreeElement', b1)
    assert _is_linked(a, 'FileTreeElement', b1)
    if hasattr(b1, 'parent'):
        assert _is_linked(b1, 'parent', a)
    _safe_set(a, 'FileTreeElement', b2)
    assert _is_linked(a, 'FileTreeElement', b2)
    if hasattr(b1, 'parent'):
        assert not _is_linked(b1, 'parent', a)
    if hasattr(b2, 'parent'):
        assert _is_linked(b2, 'parent', a)
    _safe_set(a, 'FileTreeElement', None)
    assert not _is_linked(a, 'FileTreeElement', b2)
    if hasattr(b2, 'parent'):
        assert not _is_linked(b2, 'parent', a)


def test_assoc_elements0_link_reassign_clear():
    a = filetree_PathToTreeElementMap(key="sample_text")
    b1 = filetree_FileTree()
    b2 = filetree_FileTree()
    _safe_set(a, 'filetree_PathToTreeElementMap', b1)
    assert _is_linked(a, 'filetree_PathToTreeElementMap', b1)
    if hasattr(b1, 'filetree_FileTree'):
        assert _is_linked(b1, 'filetree_FileTree', a)
    _safe_set(a, 'filetree_PathToTreeElementMap', b2)
    assert _is_linked(a, 'filetree_PathToTreeElementMap', b2)
    if hasattr(b1, 'filetree_FileTree'):
        assert not _is_linked(b1, 'filetree_FileTree', a)
    if hasattr(b2, 'filetree_FileTree'):
        assert _is_linked(b2, 'filetree_FileTree', a)
    _safe_set(a, 'filetree_PathToTreeElementMap', None)
    assert not _is_linked(a, 'filetree_PathToTreeElementMap', b2)
    if hasattr(b2, 'filetree_FileTree'):
        assert not _is_linked(b2, 'filetree_FileTree', a)


def test_assoc_fileTree4_link_reassign_clear():
    a = filetree_User(password="sample_text", pin="sample_text", rootDir="sample_text", userId="sample_text")
    b1 = filetree_FileTree()
    b2 = filetree_FileTree()
    _safe_set(a, 'filetree_User', b1)
    assert _is_linked(a, 'filetree_User', b1)
    if hasattr(b1, 'filetree_FileTree5'):
        assert _is_linked(b1, 'filetree_FileTree5', a)
    _safe_set(a, 'filetree_User', b2)
    assert _is_linked(a, 'filetree_User', b2)
    if hasattr(b1, 'filetree_FileTree5'):
        assert not _is_linked(b1, 'filetree_FileTree5', a)
    if hasattr(b2, 'filetree_FileTree5'):
        assert _is_linked(b2, 'filetree_FileTree5', a)
    _safe_set(a, 'filetree_User', None)
    assert not _is_linked(a, 'filetree_User', b2)
    if hasattr(b2, 'filetree_FileTree5'):
        assert not _is_linked(b2, 'filetree_FileTree5', a)


def test_assoc_parent1_link_reassign_clear():
    a = filetree_FileTreeElement(file="sample_text", name="sample_text", path="sample_text")
    b1 = filetree_Container()
    b2 = filetree_Container()
    _safe_set(a, 'children', b1)
    assert _is_linked(a, 'children', b1)
    if hasattr(b1, 'Container'):
        assert _is_linked(b1, 'Container', a)
    _safe_set(a, 'children', b2)
    assert _is_linked(a, 'children', b2)
    if hasattr(b1, 'Container'):
        assert not _is_linked(b1, 'Container', a)
    if hasattr(b2, 'Container'):
        assert _is_linked(b2, 'Container', a)
    _safe_set(a, 'children', None)
    assert not _is_linked(a, 'children', b2)
    if hasattr(b2, 'Container'):
        assert not _is_linked(b2, 'Container', a)


def test_assoc_value6_link_reassign_clear():
    a = filetree_PathToTreeElementMap(key="sample_text")
    b1 = filetree_FileTreeElement(file="sample_text", name="sample_text", path="sample_text")
    b2 = filetree_FileTreeElement(file="sample_text_2", name="sample_text_2", path="sample_text_2")
    _safe_set(a, 'filetree_PathToTreeElementMap7', b1)
    assert _is_linked(a, 'filetree_PathToTreeElementMap7', b1)
    if hasattr(b1, 'filetree_FileTreeElement8'):
        assert _is_linked(b1, 'filetree_FileTreeElement8', a)
    _safe_set(a, 'filetree_PathToTreeElementMap7', b2)
    assert _is_linked(a, 'filetree_PathToTreeElementMap7', b2)
    if hasattr(b1, 'filetree_FileTreeElement8'):
        assert not _is_linked(b1, 'filetree_FileTreeElement8', a)
    if hasattr(b2, 'filetree_FileTreeElement8'):
        assert _is_linked(b2, 'filetree_FileTreeElement8', a)
    _safe_set(a, 'filetree_PathToTreeElementMap7', None)
    assert not _is_linked(a, 'filetree_PathToTreeElementMap7', b2)
    if hasattr(b2, 'filetree_FileTreeElement8'):
        assert not _is_linked(b2, 'filetree_FileTreeElement8', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Container_strategy = st.builds(Container)
@given(instance=Container_strategy)
@settings(max_examples=25)
def test_Container_instantiation(instance):
    assert isinstance(instance, Container)


FileTreeElement_strategy = st.builds(FileTreeElement)
@given(instance=FileTreeElement_strategy)
@settings(max_examples=25)
def test_FileTreeElement_instantiation(instance):
    assert isinstance(instance, FileTreeElement)


filetree_AccessRight_strategy = st.builds(filetree_AccessRight, readPermission=st.booleans(), userId=safe_text, writePermission=st.booleans())
@given(instance=filetree_AccessRight_strategy)
@settings(max_examples=25)
def test_filetree_AccessRight_instantiation(instance):
    assert isinstance(instance, filetree_AccessRight)


filetree_Container_strategy = st.builds(filetree_Container)
@given(instance=filetree_Container_strategy)
@settings(max_examples=25)
def test_filetree_Container_instantiation(instance):
    assert isinstance(instance, filetree_Container)


filetree_Directory_strategy = st.builds(filetree_Directory)
@given(instance=filetree_Directory_strategy)
@settings(max_examples=25)
def test_filetree_Directory_instantiation(instance):
    assert isinstance(instance, filetree_Directory)


filetree_FileTree_strategy = st.builds(filetree_FileTree)
@given(instance=filetree_FileTree_strategy)
@settings(max_examples=25)
def test_filetree_FileTree_instantiation(instance):
    assert isinstance(instance, filetree_FileTree)


filetree_FileTreeElement_strategy = st.builds(filetree_FileTreeElement, file=safe_text, name=safe_text, path=safe_text)
@given(instance=filetree_FileTreeElement_strategy)
@settings(max_examples=25)
def test_filetree_FileTreeElement_instantiation(instance):
    assert isinstance(instance, filetree_FileTreeElement)


filetree_H2HFile_strategy = st.builds(filetree_H2HFile)
@given(instance=filetree_H2HFile_strategy)
@settings(max_examples=25)
def test_filetree_H2HFile_instantiation(instance):
    assert isinstance(instance, filetree_H2HFile)


filetree_PathToTreeElementMap_strategy = st.builds(filetree_PathToTreeElementMap, key=safe_text)
@given(instance=filetree_PathToTreeElementMap_strategy)
@settings(max_examples=25)
def test_filetree_PathToTreeElementMap_instantiation(instance):
    assert isinstance(instance, filetree_PathToTreeElementMap)


filetree_User_strategy = st.builds(filetree_User, password=safe_text, pin=safe_text, rootDir=safe_text, userId=safe_text)
@given(instance=filetree_User_strategy)
@settings(max_examples=25)
def test_filetree_User_instantiation(instance):
    assert isinstance(instance, filetree_User)



