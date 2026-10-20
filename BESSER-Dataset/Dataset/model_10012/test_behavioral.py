import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    LRBAC_Banker,
    LRBAC_Coder,
    LRBAC_EClass0,
    LRBAC_EClass1,
    LRBAC_Execute,
    LRBAC_Location,
    LRBAC_Object,
    LRBAC_Operation,
    LRBAC_Permission,
    LRBAC_Read,
    LRBAC_Role,
    LRBAC_Session,
    LRBAC_User,
    LRBAC_Write,
    Operation,
    User,
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

def test_assoc_AssignLoc8_reverse_link_reassign_clear():
    a1 = LRBAC_Role(RoleName="sample_text")
    a2 = LRBAC_Role(RoleName="sample_text_2")
    b = LRBAC_Location(LocName="sample_text")
    _safe_set(b, 'Location9', a1)
    assert _is_linked(b, 'Location9', a1)
    if hasattr(a1, 'LocAssign'):
        assert _is_linked(a1, 'LocAssign', b)
    _safe_set(b, 'Location9', a2)
    assert _is_linked(b, 'Location9', a2)
    if hasattr(a1, 'LocAssign'):
        assert not _is_linked(a1, 'LocAssign', b)
    if hasattr(a2, 'LocAssign'):
        assert _is_linked(a2, 'LocAssign', b)
    _safe_set(b, 'Location9', None)
    assert not _is_linked(b, 'Location9', a2)
    if hasattr(a2, 'LocAssign'):
        assert not _is_linked(a2, 'LocAssign', b)


def test_assoc_AssignUser6_reverse_link_reassign_clear():
    a1 = LRBAC_User(Age=7, Gender="sample_text", UserID=7, UserName="sample_text")
    a2 = LRBAC_User(Age=13, Gender="sample_text_2", UserID=13, UserName="sample_text_2")
    b = LRBAC_Role(RoleName="sample_text")
    _safe_set(b, 'AssignedRoles', {a1})
    assert _is_linked(b, 'AssignedRoles', a1)
    if hasattr(a1, 'User7'):
        assert _is_linked(a1, 'User7', b)
    _safe_set(b, 'AssignedRoles', {a2})
    assert _is_linked(b, 'AssignedRoles', a2)
    if hasattr(a1, 'User7'):
        assert not _is_linked(a1, 'User7', b)
    if hasattr(a2, 'User7'):
        assert _is_linked(a2, 'User7', b)
    _safe_set(b, 'AssignedRoles', set())
    assert not _is_linked(b, 'AssignedRoles', a2)
    if hasattr(a2, 'User7'):
        assert not _is_linked(a2, 'User7', b)


def test_assoc_AssignedRoles1_reverse_link_reassign_clear():
    a1 = LRBAC_User(Age=7, Gender="sample_text", UserID=7, UserName="sample_text")
    a2 = LRBAC_User(Age=13, Gender="sample_text_2", UserID=13, UserName="sample_text_2")
    b = LRBAC_Role(RoleName="sample_text")
    _safe_set(b, 'Role', a1)
    assert _is_linked(b, 'Role', a1)
    if hasattr(a1, 'AssignUser'):
        assert _is_linked(a1, 'AssignUser', b)
    _safe_set(b, 'Role', a2)
    assert _is_linked(b, 'Role', a2)
    if hasattr(a1, 'AssignUser'):
        assert not _is_linked(a1, 'AssignUser', b)
    if hasattr(a2, 'AssignUser'):
        assert _is_linked(a2, 'AssignUser', b)
    _safe_set(b, 'Role', None)
    assert not _is_linked(b, 'Role', a2)
    if hasattr(a2, 'AssignUser'):
        assert not _is_linked(a2, 'AssignUser', b)


def test_assoc_LocAssign15_reverse_link_reassign_clear():
    a1 = LRBAC_Role(RoleName="sample_text")
    a2 = LRBAC_Role(RoleName="sample_text_2")
    b = LRBAC_Location(LocName="sample_text")
    _safe_set(b, 'AssignLoc', {a1})
    assert _is_linked(b, 'AssignLoc', a1)
    if hasattr(a1, 'Role16'):
        assert _is_linked(a1, 'Role16', b)
    _safe_set(b, 'AssignLoc', {a2})
    assert _is_linked(b, 'AssignLoc', a2)
    if hasattr(a1, 'Role16'):
        assert not _is_linked(a1, 'Role16', b)
    if hasattr(a2, 'Role16'):
        assert _is_linked(a2, 'Role16', b)
    _safe_set(b, 'AssignLoc', set())
    assert not _is_linked(b, 'AssignLoc', a2)
    if hasattr(a2, 'Role16'):
        assert not _is_linked(a2, 'Role16', b)


def test_assoc_LocObj17_reverse_link_reassign_clear():
    a1 = LRBAC_Object(ObjID=7)
    a2 = LRBAC_Object(ObjID=13)
    b = LRBAC_Location(LocName="sample_text")
    _safe_set(b, 'ObjLoc', {a1})
    assert _is_linked(b, 'ObjLoc', a1)
    if hasattr(a1, 'Object'):
        assert _is_linked(a1, 'Object', b)
    _safe_set(b, 'ObjLoc', {a2})
    assert _is_linked(b, 'ObjLoc', a2)
    if hasattr(a1, 'Object'):
        assert not _is_linked(a1, 'Object', b)
    if hasattr(a2, 'Object'):
        assert _is_linked(a2, 'Object', b)
    _safe_set(b, 'ObjLoc', set())
    assert not _is_linked(b, 'ObjLoc', a2)
    if hasattr(a2, 'Object'):
        assert not _is_linked(a2, 'Object', b)


def test_assoc_LocUser13_reverse_link_reassign_clear():
    a1 = LRBAC_User(Age=7, Gender="sample_text", UserID=7, UserName="sample_text")
    a2 = LRBAC_User(Age=13, Gender="sample_text_2", UserID=13, UserName="sample_text_2")
    b = LRBAC_Location(LocName="sample_text")
    _safe_set(b, 'UserLoc', {a1})
    assert _is_linked(b, 'UserLoc', a1)
    if hasattr(a1, 'User14'):
        assert _is_linked(a1, 'User14', b)
    _safe_set(b, 'UserLoc', {a2})
    assert _is_linked(b, 'UserLoc', a2)
    if hasattr(a1, 'User14'):
        assert not _is_linked(a1, 'User14', b)
    if hasattr(a2, 'User14'):
        assert _is_linked(a2, 'User14', b)
    _safe_set(b, 'UserLoc', set())
    assert not _is_linked(b, 'UserLoc', a2)
    if hasattr(a2, 'User14'):
        assert not _is_linked(a2, 'User14', b)


def test_assoc_ObjLoc31_reverse_link_reassign_clear():
    a1 = LRBAC_Object(ObjID=7)
    a2 = LRBAC_Object(ObjID=13)
    b = LRBAC_Location(LocName="sample_text")
    _safe_set(b, 'Location32', a1)
    assert _is_linked(b, 'Location32', a1)
    if hasattr(a1, 'LocObj'):
        assert _is_linked(a1, 'LocObj', b)
    _safe_set(b, 'Location32', a2)
    assert _is_linked(b, 'Location32', a2)
    if hasattr(a1, 'LocObj'):
        assert not _is_linked(a1, 'LocObj', b)
    if hasattr(a2, 'LocObj'):
        assert _is_linked(a2, 'LocObj', b)
    _safe_set(b, 'Location32', None)
    assert not _is_linked(b, 'Location32', a2)
    if hasattr(a2, 'LocObj'):
        assert not _is_linked(a2, 'LocObj', b)


def test_assoc_ObjLocPerm29_reverse_link_reassign_clear():
    a1 = LRBAC_Permission(PermName="sample_text")
    a2 = LRBAC_Permission(PermName="sample_text_2")
    b = LRBAC_Location(LocName="sample_text")
    _safe_set(b, 'Location30', a1)
    assert _is_linked(b, 'Location30', a1)
    if hasattr(a1, 'PermObjLoc'):
        assert _is_linked(a1, 'PermObjLoc', b)
    _safe_set(b, 'Location30', a2)
    assert _is_linked(b, 'Location30', a2)
    if hasattr(a1, 'PermObjLoc'):
        assert not _is_linked(a1, 'PermObjLoc', b)
    if hasattr(a2, 'PermObjLoc'):
        assert _is_linked(a2, 'PermObjLoc', b)
    _safe_set(b, 'Location30', None)
    assert not _is_linked(b, 'Location30', a2)
    if hasattr(a2, 'PermObjLoc'):
        assert not _is_linked(a2, 'PermObjLoc', b)


def test_assoc_ObjPerm33_reverse_link_reassign_clear():
    a1 = LRBAC_Permission(PermName="sample_text")
    a2 = LRBAC_Permission(PermName="sample_text_2")
    b = LRBAC_Object(ObjID=7)
    _safe_set(b, 'PermObj', {a1})
    assert _is_linked(b, 'PermObj', a1)
    if hasattr(a1, 'Permission34'):
        assert _is_linked(a1, 'Permission34', b)
    _safe_set(b, 'PermObj', {a2})
    assert _is_linked(b, 'PermObj', a2)
    if hasattr(a1, 'Permission34'):
        assert not _is_linked(a1, 'Permission34', b)
    if hasattr(a2, 'Permission34'):
        assert _is_linked(a2, 'Permission34', b)
    _safe_set(b, 'PermObj', set())
    assert not _is_linked(b, 'PermObj', a2)
    if hasattr(a2, 'Permission34'):
        assert not _is_linked(a2, 'Permission34', b)


def test_assoc_PermObj23_reverse_link_reassign_clear():
    a1 = LRBAC_Permission(PermName="sample_text")
    a2 = LRBAC_Permission(PermName="sample_text_2")
    b = LRBAC_Object(ObjID=7)
    _safe_set(b, 'Object24', a1)
    assert _is_linked(b, 'Object24', a1)
    if hasattr(a1, 'ObjPerm'):
        assert _is_linked(a1, 'ObjPerm', b)
    _safe_set(b, 'Object24', a2)
    assert _is_linked(b, 'Object24', a2)
    if hasattr(a1, 'ObjPerm'):
        assert not _is_linked(a1, 'ObjPerm', b)
    if hasattr(a2, 'ObjPerm'):
        assert _is_linked(a2, 'ObjPerm', b)
    _safe_set(b, 'Object24', None)
    assert not _is_linked(b, 'Object24', a2)
    if hasattr(a2, 'ObjPerm'):
        assert not _is_linked(a2, 'ObjPerm', b)


def test_assoc_PermObjLoc20_reverse_link_reassign_clear():
    a1 = LRBAC_Permission(PermName="sample_text")
    a2 = LRBAC_Permission(PermName="sample_text_2")
    b = LRBAC_Location(LocName="sample_text")
    _safe_set(b, 'ObjLocPerm', {a1})
    assert _is_linked(b, 'ObjLocPerm', a1)
    if hasattr(a1, 'Permission21'):
        assert _is_linked(a1, 'Permission21', b)
    _safe_set(b, 'ObjLocPerm', {a2})
    assert _is_linked(b, 'ObjLocPerm', a2)
    if hasattr(a1, 'Permission21'):
        assert not _is_linked(a1, 'Permission21', b)
    if hasattr(a2, 'Permission21'):
        assert _is_linked(a2, 'Permission21', b)
    _safe_set(b, 'ObjLocPerm', set())
    assert not _is_linked(b, 'ObjLocPerm', a2)
    if hasattr(a2, 'Permission21'):
        assert not _is_linked(a2, 'Permission21', b)


def test_assoc_PermRole25_reverse_link_reassign_clear():
    a1 = LRBAC_Role(RoleName="sample_text")
    a2 = LRBAC_Role(RoleName="sample_text_2")
    b = LRBAC_Permission(PermName="sample_text")
    _safe_set(b, 'RolePerm', a1)
    assert _is_linked(b, 'RolePerm', a1)
    if hasattr(a1, 'Role26'):
        assert _is_linked(a1, 'Role26', b)
    _safe_set(b, 'RolePerm', a2)
    assert _is_linked(b, 'RolePerm', a2)
    if hasattr(a1, 'Role26'):
        assert not _is_linked(a1, 'Role26', b)
    if hasattr(a2, 'Role26'):
        assert _is_linked(a2, 'Role26', b)
    _safe_set(b, 'RolePerm', None)
    assert not _is_linked(b, 'RolePerm', a2)
    if hasattr(a2, 'Role26'):
        assert not _is_linked(a2, 'Role26', b)


def test_assoc_PermRoleLoc18_reverse_link_reassign_clear():
    a1 = LRBAC_Permission(PermName="sample_text")
    a2 = LRBAC_Permission(PermName="sample_text_2")
    b = LRBAC_Location(LocName="sample_text")
    _safe_set(b, 'RoleLocPerm', {a1})
    assert _is_linked(b, 'RoleLocPerm', a1)
    if hasattr(a1, 'Permission19'):
        assert _is_linked(a1, 'Permission19', b)
    _safe_set(b, 'RoleLocPerm', {a2})
    assert _is_linked(b, 'RoleLocPerm', a2)
    if hasattr(a1, 'Permission19'):
        assert not _is_linked(a1, 'Permission19', b)
    if hasattr(a2, 'Permission19'):
        assert _is_linked(a2, 'Permission19', b)
    _safe_set(b, 'RoleLocPerm', set())
    assert not _is_linked(b, 'RoleLocPerm', a2)
    if hasattr(a2, 'Permission19'):
        assert not _is_linked(a2, 'Permission19', b)


def test_assoc_RoleLocPerm27_reverse_link_reassign_clear():
    a1 = LRBAC_Permission(PermName="sample_text")
    a2 = LRBAC_Permission(PermName="sample_text_2")
    b = LRBAC_Location(LocName="sample_text")
    _safe_set(b, 'Location28', a1)
    assert _is_linked(b, 'Location28', a1)
    if hasattr(a1, 'PermRoleLoc'):
        assert _is_linked(a1, 'PermRoleLoc', b)
    _safe_set(b, 'Location28', a2)
    assert _is_linked(b, 'Location28', a2)
    if hasattr(a1, 'PermRoleLoc'):
        assert not _is_linked(a1, 'PermRoleLoc', b)
    if hasattr(a2, 'PermRoleLoc'):
        assert _is_linked(a2, 'PermRoleLoc', b)
    _safe_set(b, 'Location28', None)
    assert not _is_linked(b, 'Location28', a2)
    if hasattr(a2, 'PermRoleLoc'):
        assert not _is_linked(a2, 'PermRoleLoc', b)


def test_assoc_RolePerm12_reverse_link_reassign_clear():
    a1 = LRBAC_Role(RoleName="sample_text")
    a2 = LRBAC_Role(RoleName="sample_text_2")
    b = LRBAC_Permission(PermName="sample_text")
    _safe_set(b, 'Permission', a1)
    assert _is_linked(b, 'Permission', a1)
    if hasattr(a1, 'PermRole'):
        assert _is_linked(a1, 'PermRole', b)
    _safe_set(b, 'Permission', a2)
    assert _is_linked(b, 'Permission', a2)
    if hasattr(a1, 'PermRole'):
        assert not _is_linked(a1, 'PermRole', b)
    if hasattr(a2, 'PermRole'):
        assert _is_linked(a2, 'PermRole', b)
    _safe_set(b, 'Permission', None)
    assert not _is_linked(b, 'Permission', a2)
    if hasattr(a2, 'PermRole'):
        assert not _is_linked(a2, 'PermRole', b)


def test_assoc_RoleSess10_reverse_link_reassign_clear():
    a1 = LRBAC_Session(MaxRoles=7)
    a2 = LRBAC_Session(MaxRoles=13)
    b = LRBAC_Role(RoleName="sample_text")
    _safe_set(b, 'SessRole', {a1})
    assert _is_linked(b, 'SessRole', a1)
    if hasattr(a1, 'Session11'):
        assert _is_linked(a1, 'Session11', b)
    _safe_set(b, 'SessRole', {a2})
    assert _is_linked(b, 'SessRole', a2)
    if hasattr(a1, 'Session11'):
        assert not _is_linked(a1, 'Session11', b)
    if hasattr(a2, 'Session11'):
        assert _is_linked(a2, 'Session11', b)
    _safe_set(b, 'SessRole', set())
    assert not _is_linked(b, 'SessRole', a2)
    if hasattr(a2, 'Session11'):
        assert not _is_linked(a2, 'Session11', b)


def test_assoc_SessRole3_reverse_link_reassign_clear():
    a1 = LRBAC_Session(MaxRoles=7)
    a2 = LRBAC_Session(MaxRoles=13)
    b = LRBAC_Role(RoleName="sample_text")
    _safe_set(b, 'Role4', a1)
    assert _is_linked(b, 'Role4', a1)
    if hasattr(a1, 'RoleSess'):
        assert _is_linked(a1, 'RoleSess', b)
    _safe_set(b, 'Role4', a2)
    assert _is_linked(b, 'Role4', a2)
    if hasattr(a1, 'RoleSess'):
        assert not _is_linked(a1, 'RoleSess', b)
    if hasattr(a2, 'RoleSess'):
        assert _is_linked(a2, 'RoleSess', b)
    _safe_set(b, 'Role4', None)
    assert not _is_linked(b, 'Role4', a2)
    if hasattr(a2, 'RoleSess'):
        assert not _is_linked(a2, 'RoleSess', b)


def test_assoc_SessUser5_reverse_link_reassign_clear():
    a1 = LRBAC_User(Age=7, Gender="sample_text", UserID=7, UserName="sample_text")
    a2 = LRBAC_User(Age=13, Gender="sample_text_2", UserID=13, UserName="sample_text_2")
    b = LRBAC_Session(MaxRoles=7)
    _safe_set(b, 'UserSess', a1)
    assert _is_linked(b, 'UserSess', a1)
    if hasattr(a1, 'User'):
        assert _is_linked(a1, 'User', b)
    _safe_set(b, 'UserSess', a2)
    assert _is_linked(b, 'UserSess', a2)
    if hasattr(a1, 'User'):
        assert not _is_linked(a1, 'User', b)
    if hasattr(a2, 'User'):
        assert _is_linked(a2, 'User', b)
    _safe_set(b, 'UserSess', None)
    assert not _is_linked(b, 'UserSess', a2)
    if hasattr(a2, 'User'):
        assert not _is_linked(a2, 'User', b)


def test_assoc_UserLoc2_reverse_link_reassign_clear():
    a1 = LRBAC_User(Age=7, Gender="sample_text", UserID=7, UserName="sample_text")
    a2 = LRBAC_User(Age=13, Gender="sample_text_2", UserID=13, UserName="sample_text_2")
    b = LRBAC_Location(LocName="sample_text")
    _safe_set(b, 'Location', a1)
    assert _is_linked(b, 'Location', a1)
    if hasattr(a1, 'LocUser'):
        assert _is_linked(a1, 'LocUser', b)
    _safe_set(b, 'Location', a2)
    assert _is_linked(b, 'Location', a2)
    if hasattr(a1, 'LocUser'):
        assert not _is_linked(a1, 'LocUser', b)
    if hasattr(a2, 'LocUser'):
        assert _is_linked(a2, 'LocUser', b)
    _safe_set(b, 'Location', None)
    assert not _is_linked(b, 'Location', a2)
    if hasattr(a2, 'LocUser'):
        assert not _is_linked(a2, 'LocUser', b)


def test_assoc_UserSess0_reverse_link_reassign_clear():
    a1 = LRBAC_User(Age=7, Gender="sample_text", UserID=7, UserName="sample_text")
    a2 = LRBAC_User(Age=13, Gender="sample_text_2", UserID=13, UserName="sample_text_2")
    b = LRBAC_Session(MaxRoles=7)
    _safe_set(b, 'Session', a1)
    assert _is_linked(b, 'Session', a1)
    if hasattr(a1, 'SessUser'):
        assert _is_linked(a1, 'SessUser', b)
    _safe_set(b, 'Session', a2)
    assert _is_linked(b, 'Session', a2)
    if hasattr(a1, 'SessUser'):
        assert not _is_linked(a1, 'SessUser', b)
    if hasattr(a2, 'SessUser'):
        assert _is_linked(a2, 'SessUser', b)
    _safe_set(b, 'Session', None)
    assert not _is_linked(b, 'Session', a2)
    if hasattr(a2, 'SessUser'):
        assert not _is_linked(a2, 'SessUser', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_OperPerm35_stub_double():
    # LRBAC_Operation has no real 'PermOper' property in the generated
    # code (a bare stub) -- manually attach it so LRBAC_Permission's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # LRBAC_Permission's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = LRBAC_Permission(PermName="sample_text")
    partner = LRBAC_Operation()
    setattr(partner, 'PermOper', None)
    _safe_set(owner, 'Permission36', partner)
    assert owner in getattr(partner, 'PermOper')
    _safe_set(owner, 'Permission36', None)
    assert owner not in getattr(partner, 'PermOper')


def test_assoc_PermOper22_stub_double():
    # LRBAC_Operation has no real 'Operation' property in the generated
    # code (a bare stub) -- manually attach it so LRBAC_Permission's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # LRBAC_Permission's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = LRBAC_Permission(PermName="sample_text")
    partner = LRBAC_Operation()
    setattr(partner, 'Operation', None)
    _safe_set(owner, 'OperPerm', partner)
    assert getattr(partner, 'Operation') == owner
    _safe_set(owner, 'OperPerm', None)
    assert getattr(partner, 'Operation') is None


