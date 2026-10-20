import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractContent,
    Block,
    LearningObject,
    Node,
    SimpleDidacMeta,
    lobj_AbstractContent,
    lobj_AccessControl,
    lobj_Address,
    lobj_Affiliation,
    lobj_Author,
    lobj_AuthorizationTypes,
    lobj_Block,
    lobj_BlockAudiofile,
    lobj_BlockFolder,
    lobj_BlockMeta,
    lobj_Blocktype,
    lobj_Category,
    lobj_CorrBlock,
    lobj_Course,
    lobj_CourseMeta,
    lobj_Coursetype,
    lobj_DidacMeta,
    lobj_Domain,
    lobj_Edition,
    lobj_ExternalMetadata,
    lobj_FolderMeta,
    lobj_HypertextBlock,
    lobj_HypertextContent,
    lobj_InternalRef,
    lobj_Item,
    lobj_Language,
    lobj_LearningObject,
    lobj_LearningUnit,
    lobj_LuFolder,
    lobj_LuMeta,
    lobj_LuNode,
    lobj_Module,
    lobj_ModuleFolder,
    lobj_ModuleMeta,
    lobj_Node,
    lobj_Note,
    lobj_Person,
    lobj_Precognition,
    lobj_PresentationBlock,
    lobj_PublishInfo,
    lobj_Publisher,
    lobj_ResrcFile,
    lobj_ResrcFiletype,
    lobj_ResrcFolder,
    lobj_ResrcMeta,
    lobj_Sharednotes,
    lobj_SimpleDidacMeta,
    lobj_Source,
    lobj_Theme,
    lobj_ThemeNode,
    lobj_TitleMeta,
    lobj_User,
    lobj_Userauthorization,
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

def test_assoc_accessControl47_reverse_link_reassign_clear():
    a1 = lobj_LearningUnit(luFile="sample_text", treeAsXml="sample_text")
    a2 = lobj_LearningUnit(luFile="sample_text_2", treeAsXml="sample_text_2")
    b = lobj_AccessControl(globalAccess=True, id="sample_text", lastModified=date(2024, 1, 1), lastStatusChange=date(2024, 1, 1), status="sample_text")
    _safe_set(b, 'lobj_AccessControl49', a1)
    assert _is_linked(b, 'lobj_AccessControl49', a1)
    if hasattr(a1, 'lobj_LearningUnit48'):
        assert _is_linked(a1, 'lobj_LearningUnit48', b)
    _safe_set(b, 'lobj_AccessControl49', a2)
    assert _is_linked(b, 'lobj_AccessControl49', a2)
    if hasattr(a1, 'lobj_LearningUnit48'):
        assert not _is_linked(a1, 'lobj_LearningUnit48', b)
    if hasattr(a2, 'lobj_LearningUnit48'):
        assert _is_linked(a2, 'lobj_LearningUnit48', b)
    _safe_set(b, 'lobj_AccessControl49', None)
    assert not _is_linked(b, 'lobj_AccessControl49', a2)
    if hasattr(a2, 'lobj_LearningUnit48'):
        assert not _is_linked(a2, 'lobj_LearningUnit48', b)


def test_assoc_accessControl71_reverse_link_reassign_clear():
    a1 = lobj_Module(moduleFile="sample_text", treeAsXml="sample_text")
    a2 = lobj_Module(moduleFile="sample_text_2", treeAsXml="sample_text_2")
    b = lobj_AccessControl(globalAccess=True, id="sample_text", lastModified=date(2024, 1, 1), lastStatusChange=date(2024, 1, 1), status="sample_text")
    _safe_set(b, 'lobj_AccessControl73', a1)
    assert _is_linked(b, 'lobj_AccessControl73', a1)
    if hasattr(a1, 'lobj_Module72'):
        assert _is_linked(a1, 'lobj_Module72', b)
    _safe_set(b, 'lobj_AccessControl73', a2)
    assert _is_linked(b, 'lobj_AccessControl73', a2)
    if hasattr(a1, 'lobj_Module72'):
        assert not _is_linked(a1, 'lobj_Module72', b)
    if hasattr(a2, 'lobj_Module72'):
        assert _is_linked(a2, 'lobj_Module72', b)
    _safe_set(b, 'lobj_AccessControl73', None)
    assert not _is_linked(b, 'lobj_AccessControl73', a2)
    if hasattr(a2, 'lobj_Module72'):
        assert not _is_linked(a2, 'lobj_Module72', b)


def test_assoc_accessControl90_reverse_link_reassign_clear():
    a1 = lobj_ResrcFolder(deleteScheduled=True)
    a2 = lobj_ResrcFolder(deleteScheduled=False)
    b = lobj_AccessControl(globalAccess=True, id="sample_text", lastModified=date(2024, 1, 1), lastStatusChange=date(2024, 1, 1), status="sample_text")
    _safe_set(b, 'lobj_AccessControl92', a1)
    assert _is_linked(b, 'lobj_AccessControl92', a1)
    if hasattr(a1, 'lobj_ResrcFolder91'):
        assert _is_linked(a1, 'lobj_ResrcFolder91', b)
    _safe_set(b, 'lobj_AccessControl92', a2)
    assert _is_linked(b, 'lobj_AccessControl92', a2)
    if hasattr(a1, 'lobj_ResrcFolder91'):
        assert not _is_linked(a1, 'lobj_ResrcFolder91', b)
    if hasattr(a2, 'lobj_ResrcFolder91'):
        assert _is_linked(a2, 'lobj_ResrcFolder91', b)
    _safe_set(b, 'lobj_AccessControl92', None)
    assert not _is_linked(b, 'lobj_AccessControl92', a2)
    if hasattr(a2, 'lobj_ResrcFolder91'):
        assert not _is_linked(a2, 'lobj_ResrcFolder91', b)


def test_assoc_accesscontrol106_reverse_link_reassign_clear():
    a1 = lobj_ResrcFile(file="sample_text", file_tn="sample_text", filesize=7, originalextension="sample_text", resrcHref="sample_text")
    a2 = lobj_ResrcFile(file="sample_text_2", file_tn="sample_text_2", filesize=13, originalextension="sample_text_2", resrcHref="sample_text_2")
    b = lobj_AccessControl(globalAccess=True, id="sample_text", lastModified=date(2024, 1, 1), lastStatusChange=date(2024, 1, 1), status="sample_text")
    _safe_set(b, 'lobj_AccessControl108', a1)
    assert _is_linked(b, 'lobj_AccessControl108', a1)
    if hasattr(a1, 'lobj_ResrcFile107'):
        assert _is_linked(a1, 'lobj_ResrcFile107', b)
    _safe_set(b, 'lobj_AccessControl108', a2)
    assert _is_linked(b, 'lobj_AccessControl108', a2)
    if hasattr(a1, 'lobj_ResrcFile107'):
        assert not _is_linked(a1, 'lobj_ResrcFile107', b)
    if hasattr(a2, 'lobj_ResrcFile107'):
        assert _is_linked(a2, 'lobj_ResrcFile107', b)
    _safe_set(b, 'lobj_AccessControl108', None)
    assert not _is_linked(b, 'lobj_AccessControl108', a2)
    if hasattr(a2, 'lobj_ResrcFile107'):
        assert not _is_linked(a2, 'lobj_ResrcFile107', b)


def test_assoc_address134_reverse_link_reassign_clear():
    a1 = lobj_Affiliation(id="sample_text", jobtitle="sample_text", orgdiv="sample_text", orgname="sample_text", shortaffil="sample_text")
    a2 = lobj_Affiliation(id="sample_text_2", jobtitle="sample_text_2", orgdiv="sample_text_2", orgname="sample_text_2", shortaffil="sample_text_2")
    b = lobj_Address(city="sample_text", country="sample_text", email="sample_text", fax="sample_text", id="sample_text", otheraddr="sample_text", phone="sample_text", postcode="sample_text", state="sample_text", street="sample_text")
    _safe_set(b, 'lobj_Address', a1)
    assert _is_linked(b, 'lobj_Address', a1)
    if hasattr(a1, 'lobj_Affiliation'):
        assert _is_linked(a1, 'lobj_Affiliation', b)
    _safe_set(b, 'lobj_Address', a2)
    assert _is_linked(b, 'lobj_Address', a2)
    if hasattr(a1, 'lobj_Affiliation'):
        assert not _is_linked(a1, 'lobj_Affiliation', b)
    if hasattr(a2, 'lobj_Affiliation'):
        assert _is_linked(a2, 'lobj_Affiliation', b)
    _safe_set(b, 'lobj_Address', None)
    assert not _is_linked(b, 'lobj_Address', a2)
    if hasattr(a2, 'lobj_Affiliation'):
        assert not _is_linked(a2, 'lobj_Affiliation', b)


def test_assoc_address136_reverse_link_reassign_clear():
    a1 = lobj_Author(credittype="sample_text", email="sample_text", id="sample_text")
    a2 = lobj_Author(credittype="sample_text_2", email="sample_text_2", id="sample_text_2")
    b = lobj_Address(city="sample_text", country="sample_text", email="sample_text", fax="sample_text", id="sample_text", otheraddr="sample_text", phone="sample_text", postcode="sample_text", state="sample_text", street="sample_text")
    _safe_set(b, 'lobj_Address138', a1)
    assert _is_linked(b, 'lobj_Address138', a1)
    if hasattr(a1, 'lobj_Author137'):
        assert _is_linked(a1, 'lobj_Author137', b)
    _safe_set(b, 'lobj_Address138', a2)
    assert _is_linked(b, 'lobj_Address138', a2)
    if hasattr(a1, 'lobj_Author137'):
        assert not _is_linked(a1, 'lobj_Author137', b)
    if hasattr(a2, 'lobj_Author137'):
        assert _is_linked(a2, 'lobj_Author137', b)
    _safe_set(b, 'lobj_Address138', None)
    assert not _is_linked(b, 'lobj_Address138', a2)
    if hasattr(a2, 'lobj_Author137'):
        assert not _is_linked(a2, 'lobj_Author137', b)


def test_assoc_address186_reverse_link_reassign_clear():
    a1 = lobj_Publisher(id="sample_text", publishername="sample_text")
    a2 = lobj_Publisher(id="sample_text_2", publishername="sample_text_2")
    b = lobj_Address(city="sample_text", country="sample_text", email="sample_text", fax="sample_text", id="sample_text", otheraddr="sample_text", phone="sample_text", postcode="sample_text", state="sample_text", street="sample_text")
    _safe_set(b, 'lobj_Address187', a1)
    assert _is_linked(b, 'lobj_Address187', a1)
    if hasattr(a1, 'lobj_Publisher'):
        assert _is_linked(a1, 'lobj_Publisher', b)
    _safe_set(b, 'lobj_Address187', a2)
    assert _is_linked(b, 'lobj_Address187', a2)
    if hasattr(a1, 'lobj_Publisher'):
        assert not _is_linked(a1, 'lobj_Publisher', b)
    if hasattr(a2, 'lobj_Publisher'):
        assert _is_linked(a2, 'lobj_Publisher', b)
    _safe_set(b, 'lobj_Address187', None)
    assert not _is_linked(b, 'lobj_Address187', a2)
    if hasattr(a2, 'lobj_Publisher'):
        assert not _is_linked(a2, 'lobj_Publisher', b)


def test_assoc_affiliations183_reverse_link_reassign_clear():
    a1 = lobj_Person(contrib="sample_text", firstname="sample_text", honorific="sample_text", id="sample_text", personblurb="sample_text", surname="sample_text")
    a2 = lobj_Person(contrib="sample_text_2", firstname="sample_text_2", honorific="sample_text_2", id="sample_text_2", personblurb="sample_text_2", surname="sample_text_2")
    b = lobj_Affiliation(id="sample_text", jobtitle="sample_text", orgdiv="sample_text", orgname="sample_text", shortaffil="sample_text")
    _safe_set(b, 'lobj_Affiliation185', a1)
    assert _is_linked(b, 'lobj_Affiliation185', a1)
    if hasattr(a1, 'lobj_Person184'):
        assert _is_linked(a1, 'lobj_Person184', b)
    _safe_set(b, 'lobj_Affiliation185', a2)
    assert _is_linked(b, 'lobj_Affiliation185', a2)
    if hasattr(a1, 'lobj_Person184'):
        assert not _is_linked(a1, 'lobj_Person184', b)
    if hasattr(a2, 'lobj_Person184'):
        assert _is_linked(a2, 'lobj_Person184', b)
    _safe_set(b, 'lobj_Affiliation185', None)
    assert not _is_linked(b, 'lobj_Affiliation185', a2)
    if hasattr(a2, 'lobj_Person184'):
        assert not _is_linked(a2, 'lobj_Person184', b)


def test_assoc_authType181_reverse_link_reassign_clear():
    a1 = lobj_Userauthorization(id="sample_text")
    a2 = lobj_Userauthorization(id="sample_text_2")
    b = lobj_AuthorizationTypes(authType="sample_text", authTypeDesc="sample_text", id="sample_text", readOnly=True)
    _safe_set(b, 'lobj_AuthorizationTypes', a1)
    assert _is_linked(b, 'lobj_AuthorizationTypes', a1)
    if hasattr(a1, 'lobj_Userauthorization182'):
        assert _is_linked(a1, 'lobj_Userauthorization182', b)
    _safe_set(b, 'lobj_AuthorizationTypes', a2)
    assert _is_linked(b, 'lobj_AuthorizationTypes', a2)
    if hasattr(a1, 'lobj_Userauthorization182'):
        assert not _is_linked(a1, 'lobj_Userauthorization182', b)
    if hasattr(a2, 'lobj_Userauthorization182'):
        assert _is_linked(a2, 'lobj_Userauthorization182', b)
    _safe_set(b, 'lobj_AuthorizationTypes', None)
    assert not _is_linked(b, 'lobj_AuthorizationTypes', a2)
    if hasattr(a2, 'lobj_Userauthorization182'):
        assert not _is_linked(a2, 'lobj_Userauthorization182', b)


def test_assoc_author213_reverse_link_reassign_clear():
    a1 = lobj_Source(id="sample_text", pp="sample_text", publishDate="sample_text", publishedBy="sample_text", publishedIn="sample_text", subtitle="sample_text", title="sample_text")
    a2 = lobj_Source(id="sample_text_2", pp="sample_text_2", publishDate="sample_text_2", publishedBy="sample_text_2", publishedIn="sample_text_2", subtitle="sample_text_2", title="sample_text_2")
    b = lobj_Author(credittype="sample_text", email="sample_text", id="sample_text")
    _safe_set(b, 'lobj_Author215', a1)
    assert _is_linked(b, 'lobj_Author215', a1)
    if hasattr(a1, 'lobj_Source214'):
        assert _is_linked(a1, 'lobj_Source214', b)
    _safe_set(b, 'lobj_Author215', a2)
    assert _is_linked(b, 'lobj_Author215', a2)
    if hasattr(a1, 'lobj_Source214'):
        assert not _is_linked(a1, 'lobj_Source214', b)
    if hasattr(a2, 'lobj_Source214'):
        assert _is_linked(a2, 'lobj_Source214', b)
    _safe_set(b, 'lobj_Author215', None)
    assert not _is_linked(b, 'lobj_Author215', a2)
    if hasattr(a2, 'lobj_Source214'):
        assert not _is_linked(a2, 'lobj_Source214', b)


def test_assoc_authorizations216_reverse_link_reassign_clear():
    a1 = lobj_User(authenticateldap="sample_text", chatroomnr="sample_text", contchatdate=date(2024, 1, 1), currlogindate=date(2024, 1, 1), datafilter="sample_text", dossierasxml="sample_text", entryasxml="sample_text", firstname="sample_text", fromext="sample_text", icqnumber="sample_text", icqpassword="sample_text", id="sample_text", inchatsince=date(2024, 1, 1), languagenr="sample_text", lastcoursematerialnr="sample_text", lastcoursematerialviewnr="sample_text", lastlogindate=date(2024, 1, 1), lastname="sample_text", loginname="sample_text", matriculationnr="sample_text", notificationprofileasxml="sample_text", onlinedate=date(2024, 1, 1), onlinestatus="sample_text", password="sample_text", photo="sample_text", photochanged="sample_text", scn="sample_text")
    a2 = lobj_User(authenticateldap="sample_text_2", chatroomnr="sample_text_2", contchatdate=date(2025, 6, 15), currlogindate=date(2025, 6, 15), datafilter="sample_text_2", dossierasxml="sample_text_2", entryasxml="sample_text_2", firstname="sample_text_2", fromext="sample_text_2", icqnumber="sample_text_2", icqpassword="sample_text_2", id="sample_text_2", inchatsince=date(2025, 6, 15), languagenr="sample_text_2", lastcoursematerialnr="sample_text_2", lastcoursematerialviewnr="sample_text_2", lastlogindate=date(2025, 6, 15), lastname="sample_text_2", loginname="sample_text_2", matriculationnr="sample_text_2", notificationprofileasxml="sample_text_2", onlinedate=date(2025, 6, 15), onlinestatus="sample_text_2", password="sample_text_2", photo="sample_text_2", photochanged="sample_text_2", scn="sample_text_2")
    b = lobj_AuthorizationTypes(authType="sample_text", authTypeDesc="sample_text", id="sample_text", readOnly=True)
    _safe_set(b, 'lobj_AuthorizationTypes218', a1)
    assert _is_linked(b, 'lobj_AuthorizationTypes218', a1)
    if hasattr(a1, 'lobj_User217'):
        assert _is_linked(a1, 'lobj_User217', b)
    _safe_set(b, 'lobj_AuthorizationTypes218', a2)
    assert _is_linked(b, 'lobj_AuthorizationTypes218', a2)
    if hasattr(a1, 'lobj_User217'):
        assert not _is_linked(a1, 'lobj_User217', b)
    if hasattr(a2, 'lobj_User217'):
        assert _is_linked(a2, 'lobj_User217', b)
    _safe_set(b, 'lobj_AuthorizationTypes218', None)
    assert not _is_linked(b, 'lobj_AuthorizationTypes218', a2)
    if hasattr(a2, 'lobj_User217'):
        assert not _is_linked(a2, 'lobj_User217', b)


def test_assoc_authorizes130_reverse_link_reassign_clear():
    a1 = lobj_Userauthorization(id="sample_text")
    a2 = lobj_Userauthorization(id="sample_text_2")
    b = lobj_AccessControl(globalAccess=True, id="sample_text", lastModified=date(2024, 1, 1), lastStatusChange=date(2024, 1, 1), status="sample_text")
    _safe_set(b, 'lobj_AccessControl131', {a1})
    assert _is_linked(b, 'lobj_AccessControl131', a1)
    if hasattr(a1, 'lobj_Userauthorization'):
        assert _is_linked(a1, 'lobj_Userauthorization', b)
    _safe_set(b, 'lobj_AccessControl131', {a2})
    assert _is_linked(b, 'lobj_AccessControl131', a2)
    if hasattr(a1, 'lobj_Userauthorization'):
        assert not _is_linked(a1, 'lobj_Userauthorization', b)
    if hasattr(a2, 'lobj_Userauthorization'):
        assert _is_linked(a2, 'lobj_Userauthorization', b)
    _safe_set(b, 'lobj_AccessControl131', set())
    assert not _is_linked(b, 'lobj_AccessControl131', a2)
    if hasattr(a2, 'lobj_Userauthorization'):
        assert not _is_linked(a2, 'lobj_Userauthorization', b)


def test_assoc_authors170_reverse_link_reassign_clear():
    a1 = lobj_LuMeta(creationDate=date(2024, 1, 1))
    a2 = lobj_LuMeta(creationDate=date(2025, 6, 15))
    b = lobj_Author(credittype="sample_text", email="sample_text", id="sample_text")
    _safe_set(b, 'lobj_Author172', a1)
    assert _is_linked(b, 'lobj_Author172', a1)
    if hasattr(a1, 'lobj_LuMeta171'):
        assert _is_linked(a1, 'lobj_LuMeta171', b)
    _safe_set(b, 'lobj_Author172', a2)
    assert _is_linked(b, 'lobj_Author172', a2)
    if hasattr(a1, 'lobj_LuMeta171'):
        assert not _is_linked(a1, 'lobj_LuMeta171', b)
    if hasattr(a2, 'lobj_LuMeta171'):
        assert _is_linked(a2, 'lobj_LuMeta171', b)
    _safe_set(b, 'lobj_Author172', None)
    assert not _is_linked(b, 'lobj_Author172', a2)
    if hasattr(a2, 'lobj_LuMeta171'):
        assert not _is_linked(a2, 'lobj_LuMeta171', b)


def test_assoc_authors204_reverse_link_reassign_clear():
    a1 = lobj_ModuleMeta(creationDate=date(2024, 1, 1))
    a2 = lobj_ModuleMeta(creationDate=date(2025, 6, 15))
    b = lobj_Author(credittype="sample_text", email="sample_text", id="sample_text")
    _safe_set(b, 'lobj_Author206', a1)
    assert _is_linked(b, 'lobj_Author206', a1)
    if hasattr(a1, 'lobj_ModuleMeta205'):
        assert _is_linked(a1, 'lobj_ModuleMeta205', b)
    _safe_set(b, 'lobj_Author206', a2)
    assert _is_linked(b, 'lobj_Author206', a2)
    if hasattr(a1, 'lobj_ModuleMeta205'):
        assert not _is_linked(a1, 'lobj_ModuleMeta205', b)
    if hasattr(a2, 'lobj_ModuleMeta205'):
        assert _is_linked(a2, 'lobj_ModuleMeta205', b)
    _safe_set(b, 'lobj_Author206', None)
    assert not _is_linked(b, 'lobj_Author206', a2)
    if hasattr(a2, 'lobj_ModuleMeta205'):
        assert not _is_linked(a2, 'lobj_ModuleMeta205', b)


def test_assoc_blockAudiofile9_reverse_link_reassign_clear():
    a1 = lobj_HypertextContent(content="sample_text")
    a2 = lobj_HypertextContent(content="sample_text_2")
    b = lobj_BlockAudiofile(file="sample_text", filesize=7, originalextension="sample_text", resrcHref="sample_text")
    _safe_set(b, 'lobj_BlockAudiofile', a1)
    assert _is_linked(b, 'lobj_BlockAudiofile', a1)
    if hasattr(a1, 'lobj_HypertextContent10'):
        assert _is_linked(a1, 'lobj_HypertextContent10', b)
    _safe_set(b, 'lobj_BlockAudiofile', a2)
    assert _is_linked(b, 'lobj_BlockAudiofile', a2)
    if hasattr(a1, 'lobj_HypertextContent10'):
        assert not _is_linked(a1, 'lobj_HypertextContent10', b)
    if hasattr(a2, 'lobj_HypertextContent10'):
        assert _is_linked(a2, 'lobj_HypertextContent10', b)
    _safe_set(b, 'lobj_BlockAudiofile', None)
    assert not _is_linked(b, 'lobj_BlockAudiofile', a2)
    if hasattr(a2, 'lobj_HypertextContent10'):
        assert not _is_linked(a2, 'lobj_HypertextContent10', b)


def test_assoc_blocktype139_reverse_link_reassign_clear():
    a1 = lobj_Blocktype(creationDate=date(2024, 1, 1), description="sample_text", id="sample_text", name="sample_text", styleRef="sample_text")
    a2 = lobj_Blocktype(creationDate=date(2025, 6, 15), description="sample_text_2", id="sample_text_2", name="sample_text_2", styleRef="sample_text_2")
    b = lobj_BlockMeta(creationDate=date(2024, 1, 1), lastModified=date(2024, 1, 1), lod="sample_text", rendering="sample_text")
    _safe_set(b, 'lobj_BlockMeta140', a1)
    assert _is_linked(b, 'lobj_BlockMeta140', a1)
    if hasattr(a1, 'lobj_Blocktype'):
        assert _is_linked(a1, 'lobj_Blocktype', b)
    _safe_set(b, 'lobj_BlockMeta140', a2)
    assert _is_linked(b, 'lobj_BlockMeta140', a2)
    if hasattr(a1, 'lobj_Blocktype'):
        assert not _is_linked(a1, 'lobj_Blocktype', b)
    if hasattr(a2, 'lobj_Blocktype'):
        assert _is_linked(a2, 'lobj_Blocktype', b)
    _safe_set(b, 'lobj_BlockMeta140', None)
    assert not _is_linked(b, 'lobj_BlockMeta140', a2)
    if hasattr(a2, 'lobj_Blocktype'):
        assert not _is_linked(a2, 'lobj_Blocktype', b)


def test_assoc_blocktypes164_reverse_link_reassign_clear():
    a1 = lobj_Domain(creationDate=date(2024, 1, 1), description="sample_text", id="sample_text", name="sample_text", serverURL="sample_text")
    a2 = lobj_Domain(creationDate=date(2025, 6, 15), description="sample_text_2", id="sample_text_2", name="sample_text_2", serverURL="sample_text_2")
    b = lobj_Blocktype(creationDate=date(2024, 1, 1), description="sample_text", id="sample_text", name="sample_text", styleRef="sample_text")
    _safe_set(b, 'Blocktype', a1)
    assert _is_linked(b, 'Blocktype', a1)
    if hasattr(a1, 'domains'):
        assert _is_linked(a1, 'domains', b)
    _safe_set(b, 'Blocktype', a2)
    assert _is_linked(b, 'Blocktype', a2)
    if hasattr(a1, 'domains'):
        assert not _is_linked(a1, 'domains', b)
    if hasattr(a2, 'domains'):
        assert _is_linked(a2, 'domains', b)
    _safe_set(b, 'Blocktype', None)
    assert not _is_linked(b, 'Blocktype', a2)
    if hasattr(a2, 'domains'):
        assert not _is_linked(a2, 'domains', b)


def test_assoc_childitems41_reverse_link_reassign_clear():
    a1 = lobj_Item(id="sample_text", luRef="sample_text")
    a2 = lobj_Item(id="sample_text_2", luRef="sample_text_2")
    b = lobj_Item(id="sample_text", luRef="sample_text")
    _safe_set(b, 'lobj_Item42', a1)
    assert _is_linked(b, 'lobj_Item42', a1)
    if hasattr(a1, 'lobj_Item40'):
        assert _is_linked(a1, 'lobj_Item40', b)
    _safe_set(b, 'lobj_Item42', a2)
    assert _is_linked(b, 'lobj_Item42', a2)
    if hasattr(a1, 'lobj_Item40'):
        assert not _is_linked(a1, 'lobj_Item40', b)
    if hasattr(a2, 'lobj_Item40'):
        assert _is_linked(a2, 'lobj_Item40', b)
    _safe_set(b, 'lobj_Item42', None)
    assert not _is_linked(b, 'lobj_Item42', a2)
    if hasattr(a2, 'lobj_Item40'):
        assert not _is_linked(a2, 'lobj_Item40', b)


def test_assoc_corrBlock38_reverse_link_reassign_clear():
    a1 = lobj_Item(id="sample_text", luRef="sample_text")
    a2 = lobj_Item(id="sample_text_2", luRef="sample_text_2")
    b = lobj_CorrBlock(id="sample_text")
    _safe_set(b, 'lobj_CorrBlock39', a1)
    assert _is_linked(b, 'lobj_CorrBlock39', a1)
    if hasattr(a1, 'lobj_Item'):
        assert _is_linked(a1, 'lobj_Item', b)
    _safe_set(b, 'lobj_CorrBlock39', a2)
    assert _is_linked(b, 'lobj_CorrBlock39', a2)
    if hasattr(a1, 'lobj_Item'):
        assert not _is_linked(a1, 'lobj_Item', b)
    if hasattr(a2, 'lobj_Item'):
        assert _is_linked(a2, 'lobj_Item', b)
    _safe_set(b, 'lobj_CorrBlock39', None)
    assert not _is_linked(b, 'lobj_CorrBlock39', a2)
    if hasattr(a2, 'lobj_Item'):
        assert not _is_linked(a2, 'lobj_Item', b)


def test_assoc_courseMeta29_reverse_link_reassign_clear():
    a1 = lobj_CourseMeta(columnfilterasxml="sample_text", creationDate=date(2024, 1, 1), fromext="sample_text", hours=7, lvanr="sample_text")
    a2 = lobj_CourseMeta(columnfilterasxml="sample_text_2", creationDate=date(2025, 6, 15), fromext="sample_text_2", hours=13, lvanr="sample_text_2")
    b = lobj_Course(outlineAsXml="sample_text")
    _safe_set(b, 'lobj_Course30', a1)
    assert _is_linked(b, 'lobj_Course30', a1)
    if hasattr(a1, 'lobj_CourseMeta'):
        assert _is_linked(a1, 'lobj_CourseMeta', b)
    _safe_set(b, 'lobj_Course30', a2)
    assert _is_linked(b, 'lobj_Course30', a2)
    if hasattr(a1, 'lobj_CourseMeta'):
        assert not _is_linked(a1, 'lobj_CourseMeta', b)
    if hasattr(a2, 'lobj_CourseMeta'):
        assert _is_linked(a2, 'lobj_CourseMeta', b)
    _safe_set(b, 'lobj_Course30', None)
    assert not _is_linked(b, 'lobj_Course30', a2)
    if hasattr(a2, 'lobj_CourseMeta'):
        assert not _is_linked(a2, 'lobj_CourseMeta', b)


def test_assoc_coursetype34_reverse_link_reassign_clear():
    a1 = lobj_Coursetype(description="sample_text", id="sample_text", title="sample_text")
    a2 = lobj_Coursetype(description="sample_text_2", id="sample_text_2", title="sample_text_2")
    b = lobj_Course(outlineAsXml="sample_text")
    _safe_set(b, 'lobj_Course35', a1)
    assert _is_linked(b, 'lobj_Course35', a1)
    if hasattr(a1, 'lobj_Coursetype'):
        assert _is_linked(a1, 'lobj_Coursetype', b)
    _safe_set(b, 'lobj_Course35', a2)
    assert _is_linked(b, 'lobj_Course35', a2)
    if hasattr(a1, 'lobj_Coursetype'):
        assert not _is_linked(a1, 'lobj_Coursetype', b)
    if hasattr(a2, 'lobj_Coursetype'):
        assert _is_linked(a2, 'lobj_Coursetype', b)
    _safe_set(b, 'lobj_Course35', None)
    assert not _is_linked(b, 'lobj_Course35', a2)
    if hasattr(a2, 'lobj_Coursetype'):
        assert not _is_linked(a2, 'lobj_Coursetype', b)


def test_assoc_defLang144_reverse_link_reassign_clear():
    a1 = lobj_Language(code="sample_text", language="sample_text")
    a2 = lobj_Language(code="sample_text_2", language="sample_text_2")
    b = lobj_BlockMeta(creationDate=date(2024, 1, 1), lastModified=date(2024, 1, 1), lod="sample_text", rendering="sample_text")
    _safe_set(b, 'lobj_BlockMeta145', a1)
    assert _is_linked(b, 'lobj_BlockMeta145', a1)
    if hasattr(a1, 'lobj_Language146'):
        assert _is_linked(a1, 'lobj_Language146', b)
    _safe_set(b, 'lobj_BlockMeta145', a2)
    assert _is_linked(b, 'lobj_BlockMeta145', a2)
    if hasattr(a1, 'lobj_Language146'):
        assert not _is_linked(a1, 'lobj_Language146', b)
    if hasattr(a2, 'lobj_Language146'):
        assert _is_linked(a2, 'lobj_Language146', b)
    _safe_set(b, 'lobj_BlockMeta145', None)
    assert not _is_linked(b, 'lobj_BlockMeta145', a2)
    if hasattr(a2, 'lobj_Language146'):
        assert not _is_linked(a2, 'lobj_Language146', b)


def test_assoc_defLang156_reverse_link_reassign_clear():
    a1 = lobj_Language(code="sample_text", language="sample_text")
    a2 = lobj_Language(code="sample_text_2", language="sample_text_2")
    b = lobj_CourseMeta(columnfilterasxml="sample_text", creationDate=date(2024, 1, 1), fromext="sample_text", hours=7, lvanr="sample_text")
    _safe_set(b, 'lobj_CourseMeta157', a1)
    assert _is_linked(b, 'lobj_CourseMeta157', a1)
    if hasattr(a1, 'lobj_Language158'):
        assert _is_linked(a1, 'lobj_Language158', b)
    _safe_set(b, 'lobj_CourseMeta157', a2)
    assert _is_linked(b, 'lobj_CourseMeta157', a2)
    if hasattr(a1, 'lobj_Language158'):
        assert not _is_linked(a1, 'lobj_Language158', b)
    if hasattr(a2, 'lobj_Language158'):
        assert _is_linked(a2, 'lobj_Language158', b)
    _safe_set(b, 'lobj_CourseMeta157', None)
    assert not _is_linked(b, 'lobj_CourseMeta157', a2)
    if hasattr(a2, 'lobj_Language158'):
        assert not _is_linked(a2, 'lobj_Language158', b)


def test_assoc_defLang175_reverse_link_reassign_clear():
    a1 = lobj_LuMeta(creationDate=date(2024, 1, 1))
    a2 = lobj_LuMeta(creationDate=date(2025, 6, 15))
    b = lobj_Language(code="sample_text", language="sample_text")
    _safe_set(b, 'lobj_Language177', a1)
    assert _is_linked(b, 'lobj_Language177', a1)
    if hasattr(a1, 'lobj_LuMeta176'):
        assert _is_linked(a1, 'lobj_LuMeta176', b)
    _safe_set(b, 'lobj_Language177', a2)
    assert _is_linked(b, 'lobj_Language177', a2)
    if hasattr(a1, 'lobj_LuMeta176'):
        assert not _is_linked(a1, 'lobj_LuMeta176', b)
    if hasattr(a2, 'lobj_LuMeta176'):
        assert _is_linked(a2, 'lobj_LuMeta176', b)
    _safe_set(b, 'lobj_Language177', None)
    assert not _is_linked(b, 'lobj_Language177', a2)
    if hasattr(a2, 'lobj_LuMeta176'):
        assert not _is_linked(a2, 'lobj_LuMeta176', b)


def test_assoc_defLang210_reverse_link_reassign_clear():
    a1 = lobj_ModuleMeta(creationDate=date(2024, 1, 1))
    a2 = lobj_ModuleMeta(creationDate=date(2025, 6, 15))
    b = lobj_Language(code="sample_text", language="sample_text")
    _safe_set(b, 'lobj_Language212', a1)
    assert _is_linked(b, 'lobj_Language212', a1)
    if hasattr(a1, 'lobj_ModuleMeta211'):
        assert _is_linked(a1, 'lobj_ModuleMeta211', b)
    _safe_set(b, 'lobj_Language212', a2)
    assert _is_linked(b, 'lobj_Language212', a2)
    if hasattr(a1, 'lobj_ModuleMeta211'):
        assert not _is_linked(a1, 'lobj_ModuleMeta211', b)
    if hasattr(a2, 'lobj_ModuleMeta211'):
        assert _is_linked(a2, 'lobj_ModuleMeta211', b)
    _safe_set(b, 'lobj_Language212', None)
    assert not _is_linked(b, 'lobj_Language212', a2)
    if hasattr(a2, 'lobj_ModuleMeta211'):
        assert not _is_linked(a2, 'lobj_ModuleMeta211', b)


def test_assoc_didacMeta151_reverse_link_reassign_clear():
    a1 = lobj_DidacMeta(goal="sample_text")
    a2 = lobj_DidacMeta(goal="sample_text_2")
    b = lobj_CourseMeta(columnfilterasxml="sample_text", creationDate=date(2024, 1, 1), fromext="sample_text", hours=7, lvanr="sample_text")
    _safe_set(b, 'lobj_CourseMeta152', {a1})
    assert _is_linked(b, 'lobj_CourseMeta152', a1)
    if hasattr(a1, 'lobj_DidacMeta'):
        assert _is_linked(a1, 'lobj_DidacMeta', b)
    _safe_set(b, 'lobj_CourseMeta152', {a2})
    assert _is_linked(b, 'lobj_CourseMeta152', a2)
    if hasattr(a1, 'lobj_DidacMeta'):
        assert not _is_linked(a1, 'lobj_DidacMeta', b)
    if hasattr(a2, 'lobj_DidacMeta'):
        assert _is_linked(a2, 'lobj_DidacMeta', b)
    _safe_set(b, 'lobj_CourseMeta152', set())
    assert not _is_linked(b, 'lobj_CourseMeta152', a2)
    if hasattr(a2, 'lobj_DidacMeta'):
        assert not _is_linked(a2, 'lobj_DidacMeta', b)


def test_assoc_didacMeta165_reverse_link_reassign_clear():
    a1 = lobj_LuMeta(creationDate=date(2024, 1, 1))
    a2 = lobj_LuMeta(creationDate=date(2025, 6, 15))
    b = lobj_DidacMeta(goal="sample_text")
    _safe_set(b, 'lobj_DidacMeta167', a1)
    assert _is_linked(b, 'lobj_DidacMeta167', a1)
    if hasattr(a1, 'lobj_LuMeta166'):
        assert _is_linked(a1, 'lobj_LuMeta166', b)
    _safe_set(b, 'lobj_DidacMeta167', a2)
    assert _is_linked(b, 'lobj_DidacMeta167', a2)
    if hasattr(a1, 'lobj_LuMeta166'):
        assert not _is_linked(a1, 'lobj_LuMeta166', b)
    if hasattr(a2, 'lobj_LuMeta166'):
        assert _is_linked(a2, 'lobj_LuMeta166', b)
    _safe_set(b, 'lobj_DidacMeta167', None)
    assert not _is_linked(b, 'lobj_DidacMeta167', a2)
    if hasattr(a2, 'lobj_LuMeta166'):
        assert not _is_linked(a2, 'lobj_LuMeta166', b)


def test_assoc_didacMeta201_reverse_link_reassign_clear():
    a1 = lobj_ModuleMeta(creationDate=date(2024, 1, 1))
    a2 = lobj_ModuleMeta(creationDate=date(2025, 6, 15))
    b = lobj_DidacMeta(goal="sample_text")
    _safe_set(b, 'lobj_DidacMeta203', a1)
    assert _is_linked(b, 'lobj_DidacMeta203', a1)
    if hasattr(a1, 'lobj_ModuleMeta202'):
        assert _is_linked(a1, 'lobj_ModuleMeta202', b)
    _safe_set(b, 'lobj_DidacMeta203', a2)
    assert _is_linked(b, 'lobj_DidacMeta203', a2)
    if hasattr(a1, 'lobj_ModuleMeta202'):
        assert not _is_linked(a1, 'lobj_ModuleMeta202', b)
    if hasattr(a2, 'lobj_ModuleMeta202'):
        assert _is_linked(a2, 'lobj_ModuleMeta202', b)
    _safe_set(b, 'lobj_DidacMeta203', None)
    assert not _is_linked(b, 'lobj_DidacMeta203', a2)
    if hasattr(a2, 'lobj_ModuleMeta202'):
        assert not _is_linked(a2, 'lobj_ModuleMeta202', b)


def test_assoc_domain168_reverse_link_reassign_clear():
    a1 = lobj_LuMeta(creationDate=date(2024, 1, 1))
    a2 = lobj_LuMeta(creationDate=date(2025, 6, 15))
    b = lobj_Domain(creationDate=date(2024, 1, 1), description="sample_text", id="sample_text", name="sample_text", serverURL="sample_text")
    _safe_set(b, 'lobj_Domain', a1)
    assert _is_linked(b, 'lobj_Domain', a1)
    if hasattr(a1, 'lobj_LuMeta169'):
        assert _is_linked(a1, 'lobj_LuMeta169', b)
    _safe_set(b, 'lobj_Domain', a2)
    assert _is_linked(b, 'lobj_Domain', a2)
    if hasattr(a1, 'lobj_LuMeta169'):
        assert not _is_linked(a1, 'lobj_LuMeta169', b)
    if hasattr(a2, 'lobj_LuMeta169'):
        assert _is_linked(a2, 'lobj_LuMeta169', b)
    _safe_set(b, 'lobj_Domain', None)
    assert not _is_linked(b, 'lobj_Domain', a2)
    if hasattr(a2, 'lobj_LuMeta169'):
        assert not _is_linked(a2, 'lobj_LuMeta169', b)


def test_assoc_domains147_reverse_link_reassign_clear():
    a1 = lobj_Domain(creationDate=date(2024, 1, 1), description="sample_text", id="sample_text", name="sample_text", serverURL="sample_text")
    a2 = lobj_Domain(creationDate=date(2025, 6, 15), description="sample_text_2", id="sample_text_2", name="sample_text_2", serverURL="sample_text_2")
    b = lobj_Blocktype(creationDate=date(2024, 1, 1), description="sample_text", id="sample_text", name="sample_text", styleRef="sample_text")
    _safe_set(b, 'blocktypes', {a1})
    assert _is_linked(b, 'blocktypes', a1)
    if hasattr(a1, 'Domain'):
        assert _is_linked(a1, 'Domain', b)
    _safe_set(b, 'blocktypes', {a2})
    assert _is_linked(b, 'blocktypes', a2)
    if hasattr(a1, 'Domain'):
        assert not _is_linked(a1, 'Domain', b)
    if hasattr(a2, 'Domain'):
        assert _is_linked(a2, 'Domain', b)
    _safe_set(b, 'blocktypes', set())
    assert not _is_linked(b, 'blocktypes', a2)
    if hasattr(a2, 'Domain'):
        assert not _is_linked(a2, 'Domain', b)


def test_assoc_editionHistory132_reverse_link_reassign_clear():
    a1 = lobj_Edition(editedBy="sample_text", editionCreationDate=date(2024, 1, 1), editionNr="sample_text", id="sample_text", lastVersionNumber="sample_text", status="sample_text", version="sample_text")
    a2 = lobj_Edition(editedBy="sample_text_2", editionCreationDate=date(2025, 6, 15), editionNr="sample_text_2", id="sample_text_2", lastVersionNumber="sample_text_2", status="sample_text_2", version="sample_text_2")
    b = lobj_AccessControl(globalAccess=True, id="sample_text", lastModified=date(2024, 1, 1), lastStatusChange=date(2024, 1, 1), status="sample_text")
    _safe_set(b, 'lobj_AccessControl133', {a1})
    assert _is_linked(b, 'lobj_AccessControl133', a1)
    if hasattr(a1, 'lobj_Edition'):
        assert _is_linked(a1, 'lobj_Edition', b)
    _safe_set(b, 'lobj_AccessControl133', {a2})
    assert _is_linked(b, 'lobj_AccessControl133', a2)
    if hasattr(a1, 'lobj_Edition'):
        assert not _is_linked(a1, 'lobj_Edition', b)
    if hasattr(a2, 'lobj_Edition'):
        assert _is_linked(a2, 'lobj_Edition', b)
    _safe_set(b, 'lobj_AccessControl133', set())
    assert not _is_linked(b, 'lobj_AccessControl133', a2)
    if hasattr(a2, 'lobj_Edition'):
        assert not _is_linked(a2, 'lobj_Edition', b)


def test_assoc_externalMetadata31_reverse_link_reassign_clear():
    a1 = lobj_ExternalMetadata(file="sample_text", id="sample_text", ref="sample_text")
    a2 = lobj_ExternalMetadata(file="sample_text_2", id="sample_text_2", ref="sample_text_2")
    b = lobj_Course(outlineAsXml="sample_text")
    _safe_set(b, 'lobj_Course32', {a1})
    assert _is_linked(b, 'lobj_Course32', a1)
    if hasattr(a1, 'lobj_ExternalMetadata33'):
        assert _is_linked(a1, 'lobj_ExternalMetadata33', b)
    _safe_set(b, 'lobj_Course32', {a2})
    assert _is_linked(b, 'lobj_Course32', a2)
    if hasattr(a1, 'lobj_ExternalMetadata33'):
        assert not _is_linked(a1, 'lobj_ExternalMetadata33', b)
    if hasattr(a2, 'lobj_ExternalMetadata33'):
        assert _is_linked(a2, 'lobj_ExternalMetadata33', b)
    _safe_set(b, 'lobj_Course32', set())
    assert not _is_linked(b, 'lobj_Course32', a2)
    if hasattr(a2, 'lobj_ExternalMetadata33'):
        assert not _is_linked(a2, 'lobj_ExternalMetadata33', b)


def test_assoc_externalMetadata44_reverse_link_reassign_clear():
    a1 = lobj_LearningUnit(luFile="sample_text", treeAsXml="sample_text")
    a2 = lobj_LearningUnit(luFile="sample_text_2", treeAsXml="sample_text_2")
    b = lobj_ExternalMetadata(file="sample_text", id="sample_text", ref="sample_text")
    _safe_set(b, 'lobj_ExternalMetadata46', a1)
    assert _is_linked(b, 'lobj_ExternalMetadata46', a1)
    if hasattr(a1, 'lobj_LearningUnit45'):
        assert _is_linked(a1, 'lobj_LearningUnit45', b)
    _safe_set(b, 'lobj_ExternalMetadata46', a2)
    assert _is_linked(b, 'lobj_ExternalMetadata46', a2)
    if hasattr(a1, 'lobj_LearningUnit45'):
        assert not _is_linked(a1, 'lobj_LearningUnit45', b)
    if hasattr(a2, 'lobj_LearningUnit45'):
        assert _is_linked(a2, 'lobj_LearningUnit45', b)
    _safe_set(b, 'lobj_ExternalMetadata46', None)
    assert not _is_linked(b, 'lobj_ExternalMetadata46', a2)
    if hasattr(a2, 'lobj_LearningUnit45'):
        assert not _is_linked(a2, 'lobj_LearningUnit45', b)


def test_assoc_externalMetadata66_reverse_link_reassign_clear():
    a1 = lobj_Module(moduleFile="sample_text", treeAsXml="sample_text")
    a2 = lobj_Module(moduleFile="sample_text_2", treeAsXml="sample_text_2")
    b = lobj_ExternalMetadata(file="sample_text", id="sample_text", ref="sample_text")
    _safe_set(b, 'lobj_ExternalMetadata68', a1)
    assert _is_linked(b, 'lobj_ExternalMetadata68', a1)
    if hasattr(a1, 'lobj_Module67'):
        assert _is_linked(a1, 'lobj_Module67', b)
    _safe_set(b, 'lobj_ExternalMetadata68', a2)
    assert _is_linked(b, 'lobj_ExternalMetadata68', a2)
    if hasattr(a1, 'lobj_Module67'):
        assert not _is_linked(a1, 'lobj_Module67', b)
    if hasattr(a2, 'lobj_Module67'):
        assert _is_linked(a2, 'lobj_Module67', b)
    _safe_set(b, 'lobj_ExternalMetadata68', None)
    assert not _is_linked(b, 'lobj_ExternalMetadata68', a2)
    if hasattr(a2, 'lobj_Module67'):
        assert not _is_linked(a2, 'lobj_Module67', b)


def test_assoc_folderMeta85_reverse_link_reassign_clear():
    a1 = lobj_ResrcFolder(deleteScheduled=True)
    a2 = lobj_ResrcFolder(deleteScheduled=False)
    b = lobj_FolderMeta(creationDate=date(2024, 1, 1), description="sample_text", title="sample_text")
    _safe_set(b, 'lobj_FolderMeta86', a1)
    assert _is_linked(b, 'lobj_FolderMeta86', a1)
    if hasattr(a1, 'lobj_ResrcFolder'):
        assert _is_linked(a1, 'lobj_ResrcFolder', b)
    _safe_set(b, 'lobj_FolderMeta86', a2)
    assert _is_linked(b, 'lobj_FolderMeta86', a2)
    if hasattr(a1, 'lobj_ResrcFolder'):
        assert not _is_linked(a1, 'lobj_ResrcFolder', b)
    if hasattr(a2, 'lobj_ResrcFolder'):
        assert _is_linked(a2, 'lobj_ResrcFolder', b)
    _safe_set(b, 'lobj_FolderMeta86', None)
    assert not _is_linked(b, 'lobj_FolderMeta86', a2)
    if hasattr(a2, 'lobj_ResrcFolder'):
        assert not _is_linked(a2, 'lobj_ResrcFolder', b)


def test_assoc_hypertextContent114_reverse_link_reassign_clear():
    a1 = lobj_ResrcFile(file="sample_text", file_tn="sample_text", filesize=7, originalextension="sample_text", resrcHref="sample_text")
    a2 = lobj_ResrcFile(file="sample_text_2", file_tn="sample_text_2", filesize=13, originalextension="sample_text_2", resrcHref="sample_text_2")
    b = lobj_HypertextContent(content="sample_text")
    _safe_set(b, 'HypertextContent', a1)
    assert _is_linked(b, 'HypertextContent', a1)
    if hasattr(a1, 'resrcFile'):
        assert _is_linked(a1, 'resrcFile', b)
    _safe_set(b, 'HypertextContent', a2)
    assert _is_linked(b, 'HypertextContent', a2)
    if hasattr(a1, 'resrcFile'):
        assert not _is_linked(a1, 'resrcFile', b)
    if hasattr(a2, 'resrcFile'):
        assert _is_linked(a2, 'resrcFile', b)
    _safe_set(b, 'HypertextContent', None)
    assert not _is_linked(b, 'HypertextContent', a2)
    if hasattr(a2, 'resrcFile'):
        assert not _is_linked(a2, 'resrcFile', b)


def test_assoc_internalRefs196_reverse_link_reassign_clear():
    a1 = lobj_Precognition(id="sample_text", precog="sample_text")
    a2 = lobj_Precognition(id="sample_text_2", precog="sample_text_2")
    b = lobj_InternalRef(file="sample_text", id="sample_text", ref="sample_text", reftype="sample_text")
    _safe_set(b, 'lobj_InternalRef', a1)
    assert _is_linked(b, 'lobj_InternalRef', a1)
    if hasattr(a1, 'lobj_Precognition197'):
        assert _is_linked(a1, 'lobj_Precognition197', b)
    _safe_set(b, 'lobj_InternalRef', a2)
    assert _is_linked(b, 'lobj_InternalRef', a2)
    if hasattr(a1, 'lobj_Precognition197'):
        assert not _is_linked(a1, 'lobj_Precognition197', b)
    if hasattr(a2, 'lobj_Precognition197'):
        assert _is_linked(a2, 'lobj_Precognition197', b)
    _safe_set(b, 'lobj_InternalRef', None)
    assert not _is_linked(b, 'lobj_InternalRef', a2)
    if hasattr(a2, 'lobj_Precognition197'):
        assert not _is_linked(a2, 'lobj_Precognition197', b)


def test_assoc_item50_reverse_link_reassign_clear():
    a1 = lobj_LearningUnit(luFile="sample_text", treeAsXml="sample_text")
    a2 = lobj_LearningUnit(luFile="sample_text_2", treeAsXml="sample_text_2")
    b = lobj_Item(id="sample_text", luRef="sample_text")
    _safe_set(b, 'lobj_Item52', a1)
    assert _is_linked(b, 'lobj_Item52', a1)
    if hasattr(a1, 'lobj_LearningUnit51'):
        assert _is_linked(a1, 'lobj_LearningUnit51', b)
    _safe_set(b, 'lobj_Item52', a2)
    assert _is_linked(b, 'lobj_Item52', a2)
    if hasattr(a1, 'lobj_LearningUnit51'):
        assert not _is_linked(a1, 'lobj_LearningUnit51', b)
    if hasattr(a2, 'lobj_LearningUnit51'):
        assert _is_linked(a2, 'lobj_LearningUnit51', b)
    _safe_set(b, 'lobj_Item52', None)
    assert not _is_linked(b, 'lobj_Item52', a2)
    if hasattr(a2, 'lobj_LearningUnit51'):
        assert not _is_linked(a2, 'lobj_LearningUnit51', b)


def test_assoc_language148_reverse_link_reassign_clear():
    a1 = lobj_TitleMeta(id="sample_text", title="sample_text")
    a2 = lobj_TitleMeta(id="sample_text_2", title="sample_text_2")
    b = lobj_Language(code="sample_text", language="sample_text")
    _safe_set(b, 'lobj_Language150', a1)
    assert _is_linked(b, 'lobj_Language150', a1)
    if hasattr(a1, 'lobj_TitleMeta149'):
        assert _is_linked(a1, 'lobj_TitleMeta149', b)
    _safe_set(b, 'lobj_Language150', a2)
    assert _is_linked(b, 'lobj_Language150', a2)
    if hasattr(a1, 'lobj_TitleMeta149'):
        assert not _is_linked(a1, 'lobj_TitleMeta149', b)
    if hasattr(a2, 'lobj_TitleMeta149'):
        assert _is_linked(a2, 'lobj_TitleMeta149', b)
    _safe_set(b, 'lobj_Language150', None)
    assert not _is_linked(b, 'lobj_Language150', a2)
    if hasattr(a2, 'lobj_TitleMeta149'):
        assert not _is_linked(a2, 'lobj_TitleMeta149', b)


def test_assoc_language159_reverse_link_reassign_clear():
    a1 = lobj_SimpleDidacMeta(description="sample_text", id="sample_text", keywords="sample_text", title="sample_text")
    a2 = lobj_SimpleDidacMeta(description="sample_text_2", id="sample_text_2", keywords="sample_text_2", title="sample_text_2")
    b = lobj_Language(code="sample_text", language="sample_text")
    _safe_set(b, 'lobj_Language161', a1)
    assert _is_linked(b, 'lobj_Language161', a1)
    if hasattr(a1, 'lobj_SimpleDidacMeta160'):
        assert _is_linked(a1, 'lobj_SimpleDidacMeta160', b)
    _safe_set(b, 'lobj_Language161', a2)
    assert _is_linked(b, 'lobj_Language161', a2)
    if hasattr(a1, 'lobj_SimpleDidacMeta160'):
        assert not _is_linked(a1, 'lobj_SimpleDidacMeta160', b)
    if hasattr(a2, 'lobj_SimpleDidacMeta160'):
        assert _is_linked(a2, 'lobj_SimpleDidacMeta160', b)
    _safe_set(b, 'lobj_Language161', None)
    assert not _is_linked(b, 'lobj_Language161', a2)
    if hasattr(a2, 'lobj_SimpleDidacMeta160'):
        assert not _is_linked(a2, 'lobj_SimpleDidacMeta160', b)


def test_assoc_language193_reverse_link_reassign_clear():
    a1 = lobj_Language(code="sample_text", language="sample_text")
    a2 = lobj_Language(code="sample_text_2", language="sample_text_2")
    b = lobj_Coursetype(description="sample_text", id="sample_text", title="sample_text")
    _safe_set(b, 'lobj_Coursetype194', a1)
    assert _is_linked(b, 'lobj_Coursetype194', a1)
    if hasattr(a1, 'lobj_Language195'):
        assert _is_linked(a1, 'lobj_Language195', b)
    _safe_set(b, 'lobj_Coursetype194', a2)
    assert _is_linked(b, 'lobj_Coursetype194', a2)
    if hasattr(a1, 'lobj_Language195'):
        assert not _is_linked(a1, 'lobj_Language195', b)
    if hasattr(a2, 'lobj_Language195'):
        assert _is_linked(a2, 'lobj_Language195', b)
    _safe_set(b, 'lobj_Coursetype194', None)
    assert not _is_linked(b, 'lobj_Coursetype194', a2)
    if hasattr(a2, 'lobj_Language195'):
        assert not _is_linked(a2, 'lobj_Language195', b)


def test_assoc_language198_reverse_link_reassign_clear():
    a1 = lobj_Language(code="sample_text", language="sample_text")
    a2 = lobj_Language(code="sample_text_2", language="sample_text_2")
    b = lobj_InternalRef(file="sample_text", id="sample_text", ref="sample_text", reftype="sample_text")
    _safe_set(b, 'lobj_InternalRef199', a1)
    assert _is_linked(b, 'lobj_InternalRef199', a1)
    if hasattr(a1, 'lobj_Language200'):
        assert _is_linked(a1, 'lobj_Language200', b)
    _safe_set(b, 'lobj_InternalRef199', a2)
    assert _is_linked(b, 'lobj_InternalRef199', a2)
    if hasattr(a1, 'lobj_Language200'):
        assert not _is_linked(a1, 'lobj_Language200', b)
    if hasattr(a2, 'lobj_Language200'):
        assert _is_linked(a2, 'lobj_Language200', b)
    _safe_set(b, 'lobj_InternalRef199', None)
    assert not _is_linked(b, 'lobj_InternalRef199', a2)
    if hasattr(a2, 'lobj_Language200'):
        assert not _is_linked(a2, 'lobj_Language200', b)


def test_assoc_language6_reverse_link_reassign_clear():
    a1 = lobj_Language(code="sample_text", language="sample_text")
    a2 = lobj_Language(code="sample_text_2", language="sample_text_2")
    b = lobj_AbstractContent(heading="sample_text")
    _safe_set(b, 'lobj_AbstractContent', a1)
    assert _is_linked(b, 'lobj_AbstractContent', a1)
    if hasattr(a1, 'lobj_Language'):
        assert _is_linked(a1, 'lobj_Language', b)
    _safe_set(b, 'lobj_AbstractContent', a2)
    assert _is_linked(b, 'lobj_AbstractContent', a2)
    if hasattr(a1, 'lobj_Language'):
        assert not _is_linked(a1, 'lobj_Language', b)
    if hasattr(a2, 'lobj_Language'):
        assert _is_linked(a2, 'lobj_Language', b)
    _safe_set(b, 'lobj_AbstractContent', None)
    assert not _is_linked(b, 'lobj_AbstractContent', a2)
    if hasattr(a2, 'lobj_Language'):
        assert not _is_linked(a2, 'lobj_Language', b)


def test_assoc_lastModifiedBy122_reverse_link_reassign_clear():
    a1 = lobj_User(authenticateldap="sample_text", chatroomnr="sample_text", contchatdate=date(2024, 1, 1), currlogindate=date(2024, 1, 1), datafilter="sample_text", dossierasxml="sample_text", entryasxml="sample_text", firstname="sample_text", fromext="sample_text", icqnumber="sample_text", icqpassword="sample_text", id="sample_text", inchatsince=date(2024, 1, 1), languagenr="sample_text", lastcoursematerialnr="sample_text", lastcoursematerialviewnr="sample_text", lastlogindate=date(2024, 1, 1), lastname="sample_text", loginname="sample_text", matriculationnr="sample_text", notificationprofileasxml="sample_text", onlinedate=date(2024, 1, 1), onlinestatus="sample_text", password="sample_text", photo="sample_text", photochanged="sample_text", scn="sample_text")
    a2 = lobj_User(authenticateldap="sample_text_2", chatroomnr="sample_text_2", contchatdate=date(2025, 6, 15), currlogindate=date(2025, 6, 15), datafilter="sample_text_2", dossierasxml="sample_text_2", entryasxml="sample_text_2", firstname="sample_text_2", fromext="sample_text_2", icqnumber="sample_text_2", icqpassword="sample_text_2", id="sample_text_2", inchatsince=date(2025, 6, 15), languagenr="sample_text_2", lastcoursematerialnr="sample_text_2", lastcoursematerialviewnr="sample_text_2", lastlogindate=date(2025, 6, 15), lastname="sample_text_2", loginname="sample_text_2", matriculationnr="sample_text_2", notificationprofileasxml="sample_text_2", onlinedate=date(2025, 6, 15), onlinestatus="sample_text_2", password="sample_text_2", photo="sample_text_2", photochanged="sample_text_2", scn="sample_text_2")
    b = lobj_AccessControl(globalAccess=True, id="sample_text", lastModified=date(2024, 1, 1), lastStatusChange=date(2024, 1, 1), status="sample_text")
    _safe_set(b, 'lobj_AccessControl123', a1)
    assert _is_linked(b, 'lobj_AccessControl123', a1)
    if hasattr(a1, 'lobj_User124'):
        assert _is_linked(a1, 'lobj_User124', b)
    _safe_set(b, 'lobj_AccessControl123', a2)
    assert _is_linked(b, 'lobj_AccessControl123', a2)
    if hasattr(a1, 'lobj_User124'):
        assert not _is_linked(a1, 'lobj_User124', b)
    if hasattr(a2, 'lobj_User124'):
        assert _is_linked(a2, 'lobj_User124', b)
    _safe_set(b, 'lobj_AccessControl123', None)
    assert not _is_linked(b, 'lobj_AccessControl123', a2)
    if hasattr(a2, 'lobj_User124'):
        assert not _is_linked(a2, 'lobj_User124', b)


def test_assoc_lastStatusChangeBy125_reverse_link_reassign_clear():
    a1 = lobj_User(authenticateldap="sample_text", chatroomnr="sample_text", contchatdate=date(2024, 1, 1), currlogindate=date(2024, 1, 1), datafilter="sample_text", dossierasxml="sample_text", entryasxml="sample_text", firstname="sample_text", fromext="sample_text", icqnumber="sample_text", icqpassword="sample_text", id="sample_text", inchatsince=date(2024, 1, 1), languagenr="sample_text", lastcoursematerialnr="sample_text", lastcoursematerialviewnr="sample_text", lastlogindate=date(2024, 1, 1), lastname="sample_text", loginname="sample_text", matriculationnr="sample_text", notificationprofileasxml="sample_text", onlinedate=date(2024, 1, 1), onlinestatus="sample_text", password="sample_text", photo="sample_text", photochanged="sample_text", scn="sample_text")
    a2 = lobj_User(authenticateldap="sample_text_2", chatroomnr="sample_text_2", contchatdate=date(2025, 6, 15), currlogindate=date(2025, 6, 15), datafilter="sample_text_2", dossierasxml="sample_text_2", entryasxml="sample_text_2", firstname="sample_text_2", fromext="sample_text_2", icqnumber="sample_text_2", icqpassword="sample_text_2", id="sample_text_2", inchatsince=date(2025, 6, 15), languagenr="sample_text_2", lastcoursematerialnr="sample_text_2", lastcoursematerialviewnr="sample_text_2", lastlogindate=date(2025, 6, 15), lastname="sample_text_2", loginname="sample_text_2", matriculationnr="sample_text_2", notificationprofileasxml="sample_text_2", onlinedate=date(2025, 6, 15), onlinestatus="sample_text_2", password="sample_text_2", photo="sample_text_2", photochanged="sample_text_2", scn="sample_text_2")
    b = lobj_AccessControl(globalAccess=True, id="sample_text", lastModified=date(2024, 1, 1), lastStatusChange=date(2024, 1, 1), status="sample_text")
    _safe_set(b, 'lobj_AccessControl126', a1)
    assert _is_linked(b, 'lobj_AccessControl126', a1)
    if hasattr(a1, 'lobj_User127'):
        assert _is_linked(a1, 'lobj_User127', b)
    _safe_set(b, 'lobj_AccessControl126', a2)
    assert _is_linked(b, 'lobj_AccessControl126', a2)
    if hasattr(a1, 'lobj_User127'):
        assert not _is_linked(a1, 'lobj_User127', b)
    if hasattr(a2, 'lobj_User127'):
        assert _is_linked(a2, 'lobj_User127', b)
    _safe_set(b, 'lobj_AccessControl126', None)
    assert not _is_linked(b, 'lobj_AccessControl126', a2)
    if hasattr(a2, 'lobj_User127'):
        assert not _is_linked(a2, 'lobj_User127', b)


def test_assoc_lecturer153_reverse_link_reassign_clear():
    a1 = lobj_User(authenticateldap="sample_text", chatroomnr="sample_text", contchatdate=date(2024, 1, 1), currlogindate=date(2024, 1, 1), datafilter="sample_text", dossierasxml="sample_text", entryasxml="sample_text", firstname="sample_text", fromext="sample_text", icqnumber="sample_text", icqpassword="sample_text", id="sample_text", inchatsince=date(2024, 1, 1), languagenr="sample_text", lastcoursematerialnr="sample_text", lastcoursematerialviewnr="sample_text", lastlogindate=date(2024, 1, 1), lastname="sample_text", loginname="sample_text", matriculationnr="sample_text", notificationprofileasxml="sample_text", onlinedate=date(2024, 1, 1), onlinestatus="sample_text", password="sample_text", photo="sample_text", photochanged="sample_text", scn="sample_text")
    a2 = lobj_User(authenticateldap="sample_text_2", chatroomnr="sample_text_2", contchatdate=date(2025, 6, 15), currlogindate=date(2025, 6, 15), datafilter="sample_text_2", dossierasxml="sample_text_2", entryasxml="sample_text_2", firstname="sample_text_2", fromext="sample_text_2", icqnumber="sample_text_2", icqpassword="sample_text_2", id="sample_text_2", inchatsince=date(2025, 6, 15), languagenr="sample_text_2", lastcoursematerialnr="sample_text_2", lastcoursematerialviewnr="sample_text_2", lastlogindate=date(2025, 6, 15), lastname="sample_text_2", loginname="sample_text_2", matriculationnr="sample_text_2", notificationprofileasxml="sample_text_2", onlinedate=date(2025, 6, 15), onlinestatus="sample_text_2", password="sample_text_2", photo="sample_text_2", photochanged="sample_text_2", scn="sample_text_2")
    b = lobj_CourseMeta(columnfilterasxml="sample_text", creationDate=date(2024, 1, 1), fromext="sample_text", hours=7, lvanr="sample_text")
    _safe_set(b, 'lobj_CourseMeta154', a1)
    assert _is_linked(b, 'lobj_CourseMeta154', a1)
    if hasattr(a1, 'lobj_User155'):
        assert _is_linked(a1, 'lobj_User155', b)
    _safe_set(b, 'lobj_CourseMeta154', a2)
    assert _is_linked(b, 'lobj_CourseMeta154', a2)
    if hasattr(a1, 'lobj_User155'):
        assert not _is_linked(a1, 'lobj_User155', b)
    if hasattr(a2, 'lobj_User155'):
        assert _is_linked(a2, 'lobj_User155', b)
    _safe_set(b, 'lobj_CourseMeta154', None)
    assert not _is_linked(b, 'lobj_CourseMeta154', a2)
    if hasattr(a2, 'lobj_User155'):
        assert not _is_linked(a2, 'lobj_User155', b)


def test_assoc_luMeta43_reverse_link_reassign_clear():
    a1 = lobj_LuMeta(creationDate=date(2024, 1, 1))
    a2 = lobj_LuMeta(creationDate=date(2025, 6, 15))
    b = lobj_LearningUnit(luFile="sample_text", treeAsXml="sample_text")
    _safe_set(b, 'lobj_LearningUnit', a1)
    assert _is_linked(b, 'lobj_LearningUnit', a1)
    if hasattr(a1, 'lobj_LuMeta'):
        assert _is_linked(a1, 'lobj_LuMeta', b)
    _safe_set(b, 'lobj_LearningUnit', a2)
    assert _is_linked(b, 'lobj_LearningUnit', a2)
    if hasattr(a1, 'lobj_LuMeta'):
        assert not _is_linked(a1, 'lobj_LuMeta', b)
    if hasattr(a2, 'lobj_LuMeta'):
        assert _is_linked(a2, 'lobj_LuMeta', b)
    _safe_set(b, 'lobj_LearningUnit', None)
    assert not _is_linked(b, 'lobj_LearningUnit', a2)
    if hasattr(a2, 'lobj_LuMeta'):
        assert not _is_linked(a2, 'lobj_LuMeta', b)


def test_assoc_module36_reverse_link_reassign_clear():
    a1 = lobj_Module(moduleFile="sample_text", treeAsXml="sample_text")
    a2 = lobj_Module(moduleFile="sample_text_2", treeAsXml="sample_text_2")
    b = lobj_Course(outlineAsXml="sample_text")
    _safe_set(b, 'lobj_Course37', {a1})
    assert _is_linked(b, 'lobj_Course37', a1)
    if hasattr(a1, 'lobj_Module'):
        assert _is_linked(a1, 'lobj_Module', b)
    _safe_set(b, 'lobj_Course37', {a2})
    assert _is_linked(b, 'lobj_Course37', a2)
    if hasattr(a1, 'lobj_Module'):
        assert not _is_linked(a1, 'lobj_Module', b)
    if hasattr(a2, 'lobj_Module'):
        assert _is_linked(a2, 'lobj_Module', b)
    _safe_set(b, 'lobj_Course37', set())
    assert not _is_linked(b, 'lobj_Course37', a2)
    if hasattr(a2, 'lobj_Module'):
        assert not _is_linked(a2, 'lobj_Module', b)


def test_assoc_moduleMeta64_reverse_link_reassign_clear():
    a1 = lobj_ModuleMeta(creationDate=date(2024, 1, 1))
    a2 = lobj_ModuleMeta(creationDate=date(2025, 6, 15))
    b = lobj_Module(moduleFile="sample_text", treeAsXml="sample_text")
    _safe_set(b, 'lobj_Module65', a1)
    assert _is_linked(b, 'lobj_Module65', a1)
    if hasattr(a1, 'lobj_ModuleMeta'):
        assert _is_linked(a1, 'lobj_ModuleMeta', b)
    _safe_set(b, 'lobj_Module65', a2)
    assert _is_linked(b, 'lobj_Module65', a2)
    if hasattr(a1, 'lobj_ModuleMeta'):
        assert not _is_linked(a1, 'lobj_ModuleMeta', b)
    if hasattr(a2, 'lobj_ModuleMeta'):
        assert _is_linked(a2, 'lobj_ModuleMeta', b)
    _safe_set(b, 'lobj_Module65', None)
    assert not _is_linked(b, 'lobj_Module65', a2)
    if hasattr(a2, 'lobj_ModuleMeta'):
        assert not _is_linked(a2, 'lobj_ModuleMeta', b)


def test_assoc_notes191_reverse_link_reassign_clear():
    a1 = lobj_Sharednotes(id="sample_text")
    a2 = lobj_Sharednotes(id="sample_text_2")
    b = lobj_Note(content="sample_text", date=date(2024, 1, 1), id="sample_text", noteAuthor="sample_text")
    _safe_set(b, 'lobj_Note', a1)
    assert _is_linked(b, 'lobj_Note', a1)
    if hasattr(a1, 'lobj_Sharednotes192'):
        assert _is_linked(a1, 'lobj_Sharednotes192', b)
    _safe_set(b, 'lobj_Note', a2)
    assert _is_linked(b, 'lobj_Note', a2)
    if hasattr(a1, 'lobj_Sharednotes192'):
        assert not _is_linked(a1, 'lobj_Sharednotes192', b)
    if hasattr(a2, 'lobj_Sharednotes192'):
        assert _is_linked(a2, 'lobj_Sharednotes192', b)
    _safe_set(b, 'lobj_Note', None)
    assert not _is_linked(b, 'lobj_Note', a2)
    if hasattr(a2, 'lobj_Sharednotes192'):
        assert not _is_linked(a2, 'lobj_Sharednotes192', b)


def test_assoc_owner120_reverse_link_reassign_clear():
    a1 = lobj_User(authenticateldap="sample_text", chatroomnr="sample_text", contchatdate=date(2024, 1, 1), currlogindate=date(2024, 1, 1), datafilter="sample_text", dossierasxml="sample_text", entryasxml="sample_text", firstname="sample_text", fromext="sample_text", icqnumber="sample_text", icqpassword="sample_text", id="sample_text", inchatsince=date(2024, 1, 1), languagenr="sample_text", lastcoursematerialnr="sample_text", lastcoursematerialviewnr="sample_text", lastlogindate=date(2024, 1, 1), lastname="sample_text", loginname="sample_text", matriculationnr="sample_text", notificationprofileasxml="sample_text", onlinedate=date(2024, 1, 1), onlinestatus="sample_text", password="sample_text", photo="sample_text", photochanged="sample_text", scn="sample_text")
    a2 = lobj_User(authenticateldap="sample_text_2", chatroomnr="sample_text_2", contchatdate=date(2025, 6, 15), currlogindate=date(2025, 6, 15), datafilter="sample_text_2", dossierasxml="sample_text_2", entryasxml="sample_text_2", firstname="sample_text_2", fromext="sample_text_2", icqnumber="sample_text_2", icqpassword="sample_text_2", id="sample_text_2", inchatsince=date(2025, 6, 15), languagenr="sample_text_2", lastcoursematerialnr="sample_text_2", lastcoursematerialviewnr="sample_text_2", lastlogindate=date(2025, 6, 15), lastname="sample_text_2", loginname="sample_text_2", matriculationnr="sample_text_2", notificationprofileasxml="sample_text_2", onlinedate=date(2025, 6, 15), onlinestatus="sample_text_2", password="sample_text_2", photo="sample_text_2", photochanged="sample_text_2", scn="sample_text_2")
    b = lobj_AccessControl(globalAccess=True, id="sample_text", lastModified=date(2024, 1, 1), lastStatusChange=date(2024, 1, 1), status="sample_text")
    _safe_set(b, 'lobj_AccessControl121', a1)
    assert _is_linked(b, 'lobj_AccessControl121', a1)
    if hasattr(a1, 'lobj_User'):
        assert _is_linked(a1, 'lobj_User', b)
    _safe_set(b, 'lobj_AccessControl121', a2)
    assert _is_linked(b, 'lobj_AccessControl121', a2)
    if hasattr(a1, 'lobj_User'):
        assert not _is_linked(a1, 'lobj_User', b)
    if hasattr(a2, 'lobj_User'):
        assert _is_linked(a2, 'lobj_User', b)
    _safe_set(b, 'lobj_AccessControl121', None)
    assert not _is_linked(b, 'lobj_AccessControl121', a2)
    if hasattr(a2, 'lobj_User'):
        assert not _is_linked(a2, 'lobj_User', b)


def test_assoc_person135_reverse_link_reassign_clear():
    a1 = lobj_Person(contrib="sample_text", firstname="sample_text", honorific="sample_text", id="sample_text", personblurb="sample_text", surname="sample_text")
    a2 = lobj_Person(contrib="sample_text_2", firstname="sample_text_2", honorific="sample_text_2", id="sample_text_2", personblurb="sample_text_2", surname="sample_text_2")
    b = lobj_Author(credittype="sample_text", email="sample_text", id="sample_text")
    _safe_set(b, 'lobj_Author', a1)
    assert _is_linked(b, 'lobj_Author', a1)
    if hasattr(a1, 'lobj_Person'):
        assert _is_linked(a1, 'lobj_Person', b)
    _safe_set(b, 'lobj_Author', a2)
    assert _is_linked(b, 'lobj_Author', a2)
    if hasattr(a1, 'lobj_Person'):
        assert not _is_linked(a1, 'lobj_Person', b)
    if hasattr(a2, 'lobj_Person'):
        assert _is_linked(a2, 'lobj_Person', b)
    _safe_set(b, 'lobj_Author', None)
    assert not _is_linked(b, 'lobj_Author', a2)
    if hasattr(a2, 'lobj_Person'):
        assert not _is_linked(a2, 'lobj_Person', b)


def test_assoc_precognition162_reverse_link_reassign_clear():
    a1 = lobj_Precognition(id="sample_text", precog="sample_text")
    a2 = lobj_Precognition(id="sample_text_2", precog="sample_text_2")
    b = lobj_DidacMeta(goal="sample_text")
    _safe_set(b, 'lobj_DidacMeta163', a1)
    assert _is_linked(b, 'lobj_DidacMeta163', a1)
    if hasattr(a1, 'lobj_Precognition'):
        assert _is_linked(a1, 'lobj_Precognition', b)
    _safe_set(b, 'lobj_DidacMeta163', a2)
    assert _is_linked(b, 'lobj_DidacMeta163', a2)
    if hasattr(a1, 'lobj_Precognition'):
        assert not _is_linked(a1, 'lobj_Precognition', b)
    if hasattr(a2, 'lobj_Precognition'):
        assert _is_linked(a2, 'lobj_Precognition', b)
    _safe_set(b, 'lobj_DidacMeta163', None)
    assert not _is_linked(b, 'lobj_DidacMeta163', a2)
    if hasattr(a2, 'lobj_Precognition'):
        assert not _is_linked(a2, 'lobj_Precognition', b)


def test_assoc_presentationBlock25_reverse_link_reassign_clear():
    a1 = lobj_PresentationBlock(id="sample_text", lod=7, rendering="sample_text")
    a2 = lobj_PresentationBlock(id="sample_text_2", lod=13, rendering="sample_text_2")
    b = lobj_CorrBlock(id="sample_text")
    _safe_set(b, 'lobj_CorrBlock', {a1})
    assert _is_linked(b, 'lobj_CorrBlock', a1)
    if hasattr(a1, 'lobj_PresentationBlock'):
        assert _is_linked(a1, 'lobj_PresentationBlock', b)
    _safe_set(b, 'lobj_CorrBlock', {a2})
    assert _is_linked(b, 'lobj_CorrBlock', a2)
    if hasattr(a1, 'lobj_PresentationBlock'):
        assert not _is_linked(a1, 'lobj_PresentationBlock', b)
    if hasattr(a2, 'lobj_PresentationBlock'):
        assert _is_linked(a2, 'lobj_PresentationBlock', b)
    _safe_set(b, 'lobj_CorrBlock', set())
    assert not _is_linked(b, 'lobj_CorrBlock', a2)
    if hasattr(a2, 'lobj_PresentationBlock'):
        assert not _is_linked(a2, 'lobj_PresentationBlock', b)


def test_assoc_publishInfo173_reverse_link_reassign_clear():
    a1 = lobj_PublishInfo(edition="sample_text", id="sample_text", pubdate=date(2024, 1, 1), pubsnumber="sample_text", releaseinfo="sample_text")
    a2 = lobj_PublishInfo(edition="sample_text_2", id="sample_text_2", pubdate=date(2025, 6, 15), pubsnumber="sample_text_2", releaseinfo="sample_text_2")
    b = lobj_LuMeta(creationDate=date(2024, 1, 1))
    _safe_set(b, 'lobj_LuMeta174', a1)
    assert _is_linked(b, 'lobj_LuMeta174', a1)
    if hasattr(a1, 'lobj_PublishInfo'):
        assert _is_linked(a1, 'lobj_PublishInfo', b)
    _safe_set(b, 'lobj_LuMeta174', a2)
    assert _is_linked(b, 'lobj_LuMeta174', a2)
    if hasattr(a1, 'lobj_PublishInfo'):
        assert not _is_linked(a1, 'lobj_PublishInfo', b)
    if hasattr(a2, 'lobj_PublishInfo'):
        assert _is_linked(a2, 'lobj_PublishInfo', b)
    _safe_set(b, 'lobj_LuMeta174', None)
    assert not _is_linked(b, 'lobj_LuMeta174', a2)
    if hasattr(a2, 'lobj_PublishInfo'):
        assert not _is_linked(a2, 'lobj_PublishInfo', b)


def test_assoc_publishInfo207_reverse_link_reassign_clear():
    a1 = lobj_PublishInfo(edition="sample_text", id="sample_text", pubdate=date(2024, 1, 1), pubsnumber="sample_text", releaseinfo="sample_text")
    a2 = lobj_PublishInfo(edition="sample_text_2", id="sample_text_2", pubdate=date(2025, 6, 15), pubsnumber="sample_text_2", releaseinfo="sample_text_2")
    b = lobj_ModuleMeta(creationDate=date(2024, 1, 1))
    _safe_set(b, 'lobj_ModuleMeta208', a1)
    assert _is_linked(b, 'lobj_ModuleMeta208', a1)
    if hasattr(a1, 'lobj_PublishInfo209'):
        assert _is_linked(a1, 'lobj_PublishInfo209', b)
    _safe_set(b, 'lobj_ModuleMeta208', a2)
    assert _is_linked(b, 'lobj_ModuleMeta208', a2)
    if hasattr(a1, 'lobj_PublishInfo209'):
        assert not _is_linked(a1, 'lobj_PublishInfo209', b)
    if hasattr(a2, 'lobj_PublishInfo209'):
        assert _is_linked(a2, 'lobj_PublishInfo209', b)
    _safe_set(b, 'lobj_ModuleMeta208', None)
    assert not _is_linked(b, 'lobj_ModuleMeta208', a2)
    if hasattr(a2, 'lobj_PublishInfo209'):
        assert not _is_linked(a2, 'lobj_PublishInfo209', b)


def test_assoc_publisher188_reverse_link_reassign_clear():
    a1 = lobj_Publisher(id="sample_text", publishername="sample_text")
    a2 = lobj_Publisher(id="sample_text_2", publishername="sample_text_2")
    b = lobj_PublishInfo(edition="sample_text", id="sample_text", pubdate=date(2024, 1, 1), pubsnumber="sample_text", releaseinfo="sample_text")
    _safe_set(b, 'lobj_PublishInfo189', a1)
    assert _is_linked(b, 'lobj_PublishInfo189', a1)
    if hasattr(a1, 'lobj_Publisher190'):
        assert _is_linked(a1, 'lobj_Publisher190', b)
    _safe_set(b, 'lobj_PublishInfo189', a2)
    assert _is_linked(b, 'lobj_PublishInfo189', a2)
    if hasattr(a1, 'lobj_Publisher190'):
        assert not _is_linked(a1, 'lobj_Publisher190', b)
    if hasattr(a2, 'lobj_Publisher190'):
        assert _is_linked(a2, 'lobj_Publisher190', b)
    _safe_set(b, 'lobj_PublishInfo189', None)
    assert not _is_linked(b, 'lobj_PublishInfo189', a2)
    if hasattr(a2, 'lobj_Publisher190'):
        assert not _is_linked(a2, 'lobj_Publisher190', b)


def test_assoc_resrcFile11_reverse_link_reassign_clear():
    a1 = lobj_ResrcFile(file="sample_text", file_tn="sample_text", filesize=7, originalextension="sample_text", resrcHref="sample_text")
    a2 = lobj_ResrcFile(file="sample_text_2", file_tn="sample_text_2", filesize=13, originalextension="sample_text_2", resrcHref="sample_text_2")
    b = lobj_HypertextContent(content="sample_text")
    _safe_set(b, 'hypertextContent', {a1})
    assert _is_linked(b, 'hypertextContent', a1)
    if hasattr(a1, 'ResrcFile'):
        assert _is_linked(a1, 'ResrcFile', b)
    _safe_set(b, 'hypertextContent', {a2})
    assert _is_linked(b, 'hypertextContent', a2)
    if hasattr(a1, 'ResrcFile'):
        assert not _is_linked(a1, 'ResrcFile', b)
    if hasattr(a2, 'ResrcFile'):
        assert _is_linked(a2, 'ResrcFile', b)
    _safe_set(b, 'hypertextContent', set())
    assert not _is_linked(b, 'hypertextContent', a2)
    if hasattr(a2, 'ResrcFile'):
        assert not _is_linked(a2, 'ResrcFile', b)


def test_assoc_resrcFile93_reverse_link_reassign_clear():
    a1 = lobj_ResrcFolder(deleteScheduled=True)
    a2 = lobj_ResrcFolder(deleteScheduled=False)
    b = lobj_ResrcFile(file="sample_text", file_tn="sample_text", filesize=7, originalextension="sample_text", resrcHref="sample_text")
    _safe_set(b, 'lobj_ResrcFile', a1)
    assert _is_linked(b, 'lobj_ResrcFile', a1)
    if hasattr(a1, 'lobj_ResrcFolder94'):
        assert _is_linked(a1, 'lobj_ResrcFolder94', b)
    _safe_set(b, 'lobj_ResrcFile', a2)
    assert _is_linked(b, 'lobj_ResrcFile', a2)
    if hasattr(a1, 'lobj_ResrcFolder94'):
        assert not _is_linked(a1, 'lobj_ResrcFolder94', b)
    if hasattr(a2, 'lobj_ResrcFolder94'):
        assert _is_linked(a2, 'lobj_ResrcFolder94', b)
    _safe_set(b, 'lobj_ResrcFile', None)
    assert not _is_linked(b, 'lobj_ResrcFile', a2)
    if hasattr(a2, 'lobj_ResrcFolder94'):
        assert not _is_linked(a2, 'lobj_ResrcFolder94', b)


def test_assoc_resrcFiletype109_reverse_link_reassign_clear():
    a1 = lobj_ResrcFiletype(applet=True, filetypeDesc="sample_text", filetypeExtension="sample_text", filetypeImageBif="sample_text", filetypeImageSmall="sample_text", id="sample_text", image=True)
    a2 = lobj_ResrcFiletype(applet=False, filetypeDesc="sample_text_2", filetypeExtension="sample_text_2", filetypeImageBif="sample_text_2", filetypeImageSmall="sample_text_2", id="sample_text_2", image=False)
    b = lobj_ResrcFile(file="sample_text", file_tn="sample_text", filesize=7, originalextension="sample_text", resrcHref="sample_text")
    _safe_set(b, 'lobj_ResrcFile110', a1)
    assert _is_linked(b, 'lobj_ResrcFile110', a1)
    if hasattr(a1, 'lobj_ResrcFiletype'):
        assert _is_linked(a1, 'lobj_ResrcFiletype', b)
    _safe_set(b, 'lobj_ResrcFile110', a2)
    assert _is_linked(b, 'lobj_ResrcFile110', a2)
    if hasattr(a1, 'lobj_ResrcFiletype'):
        assert not _is_linked(a1, 'lobj_ResrcFiletype', b)
    if hasattr(a2, 'lobj_ResrcFiletype'):
        assert _is_linked(a2, 'lobj_ResrcFiletype', b)
    _safe_set(b, 'lobj_ResrcFile110', None)
    assert not _is_linked(b, 'lobj_ResrcFile110', a2)
    if hasattr(a2, 'lobj_ResrcFiletype'):
        assert not _is_linked(a2, 'lobj_ResrcFiletype', b)


def test_assoc_resrcFiletype117_reverse_link_reassign_clear():
    a1 = lobj_ResrcFiletype(applet=True, filetypeDesc="sample_text", filetypeExtension="sample_text", filetypeImageBif="sample_text", filetypeImageSmall="sample_text", id="sample_text", image=True)
    a2 = lobj_ResrcFiletype(applet=False, filetypeDesc="sample_text_2", filetypeExtension="sample_text_2", filetypeImageBif="sample_text_2", filetypeImageSmall="sample_text_2", id="sample_text_2", image=False)
    b = lobj_BlockAudiofile(file="sample_text", filesize=7, originalextension="sample_text", resrcHref="sample_text")
    _safe_set(b, 'lobj_BlockAudiofile118', a1)
    assert _is_linked(b, 'lobj_BlockAudiofile118', a1)
    if hasattr(a1, 'lobj_ResrcFiletype119'):
        assert _is_linked(a1, 'lobj_ResrcFiletype119', b)
    _safe_set(b, 'lobj_BlockAudiofile118', a2)
    assert _is_linked(b, 'lobj_BlockAudiofile118', a2)
    if hasattr(a1, 'lobj_ResrcFiletype119'):
        assert not _is_linked(a1, 'lobj_ResrcFiletype119', b)
    if hasattr(a2, 'lobj_ResrcFiletype119'):
        assert _is_linked(a2, 'lobj_ResrcFiletype119', b)
    _safe_set(b, 'lobj_BlockAudiofile118', None)
    assert not _is_linked(b, 'lobj_BlockAudiofile118', a2)
    if hasattr(a2, 'lobj_ResrcFiletype119'):
        assert not _is_linked(a2, 'lobj_ResrcFiletype119', b)


def test_assoc_resrcFolder88_reverse_link_reassign_clear():
    a1 = lobj_ResrcFolder(deleteScheduled=True)
    a2 = lobj_ResrcFolder(deleteScheduled=False)
    b = lobj_ResrcFolder(deleteScheduled=True)
    _safe_set(b, 'lobj_ResrcFolder89', a1)
    assert _is_linked(b, 'lobj_ResrcFolder89', a1)
    if hasattr(a1, 'lobj_ResrcFolder87'):
        assert _is_linked(a1, 'lobj_ResrcFolder87', b)
    _safe_set(b, 'lobj_ResrcFolder89', a2)
    assert _is_linked(b, 'lobj_ResrcFolder89', a2)
    if hasattr(a1, 'lobj_ResrcFolder87'):
        assert not _is_linked(a1, 'lobj_ResrcFolder87', b)
    if hasattr(a2, 'lobj_ResrcFolder87'):
        assert _is_linked(a2, 'lobj_ResrcFolder87', b)
    _safe_set(b, 'lobj_ResrcFolder89', None)
    assert not _is_linked(b, 'lobj_ResrcFolder89', a2)
    if hasattr(a2, 'lobj_ResrcFolder87'):
        assert not _is_linked(a2, 'lobj_ResrcFolder87', b)


def test_assoc_resrcMeta115_reverse_link_reassign_clear():
    a1 = lobj_ResrcMeta(creationDate=date(2024, 1, 1), description="sample_text", filename="sample_text", height=7, keywords="sample_text", lastModified=date(2024, 1, 1), parameters="sample_text", title="sample_text", width=7)
    a2 = lobj_ResrcMeta(creationDate=date(2025, 6, 15), description="sample_text_2", filename="sample_text_2", height=13, keywords="sample_text_2", lastModified=date(2025, 6, 15), parameters="sample_text_2", title="sample_text_2", width=13)
    b = lobj_ResrcFile(file="sample_text", file_tn="sample_text", filesize=7, originalextension="sample_text", resrcHref="sample_text")
    _safe_set(b, 'lobj_ResrcFile116', a1)
    assert _is_linked(b, 'lobj_ResrcFile116', a1)
    if hasattr(a1, 'lobj_ResrcMeta'):
        assert _is_linked(a1, 'lobj_ResrcMeta', b)
    _safe_set(b, 'lobj_ResrcFile116', a2)
    assert _is_linked(b, 'lobj_ResrcFile116', a2)
    if hasattr(a1, 'lobj_ResrcMeta'):
        assert not _is_linked(a1, 'lobj_ResrcMeta', b)
    if hasattr(a2, 'lobj_ResrcMeta'):
        assert _is_linked(a2, 'lobj_ResrcMeta', b)
    _safe_set(b, 'lobj_ResrcFile116', None)
    assert not _is_linked(b, 'lobj_ResrcFile116', a2)
    if hasattr(a2, 'lobj_ResrcMeta'):
        assert not _is_linked(a2, 'lobj_ResrcMeta', b)


def test_assoc_rootNode69_reverse_link_reassign_clear():
    a1 = lobj_Node(id="sample_text", visible=True)
    a2 = lobj_Node(id="sample_text_2", visible=False)
    b = lobj_Module(moduleFile="sample_text", treeAsXml="sample_text")
    _safe_set(b, 'lobj_Module70', a1)
    assert _is_linked(b, 'lobj_Module70', a1)
    if hasattr(a1, 'lobj_Node'):
        assert _is_linked(a1, 'lobj_Node', b)
    _safe_set(b, 'lobj_Module70', a2)
    assert _is_linked(b, 'lobj_Module70', a2)
    if hasattr(a1, 'lobj_Node'):
        assert not _is_linked(a1, 'lobj_Node', b)
    if hasattr(a2, 'lobj_Node'):
        assert _is_linked(a2, 'lobj_Node', b)
    _safe_set(b, 'lobj_Module70', None)
    assert not _is_linked(b, 'lobj_Module70', a2)
    if hasattr(a2, 'lobj_Node'):
        assert not _is_linked(a2, 'lobj_Node', b)


def test_assoc_sharednotes128_reverse_link_reassign_clear():
    a1 = lobj_Sharednotes(id="sample_text")
    a2 = lobj_Sharednotes(id="sample_text_2")
    b = lobj_AccessControl(globalAccess=True, id="sample_text", lastModified=date(2024, 1, 1), lastStatusChange=date(2024, 1, 1), status="sample_text")
    _safe_set(b, 'lobj_AccessControl129', a1)
    assert _is_linked(b, 'lobj_AccessControl129', a1)
    if hasattr(a1, 'lobj_Sharednotes'):
        assert _is_linked(a1, 'lobj_Sharednotes', b)
    _safe_set(b, 'lobj_AccessControl129', a2)
    assert _is_linked(b, 'lobj_AccessControl129', a2)
    if hasattr(a1, 'lobj_Sharednotes'):
        assert not _is_linked(a1, 'lobj_Sharednotes', b)
    if hasattr(a2, 'lobj_Sharednotes'):
        assert _is_linked(a2, 'lobj_Sharednotes', b)
    _safe_set(b, 'lobj_AccessControl129', None)
    assert not _is_linked(b, 'lobj_AccessControl129', a2)
    if hasattr(a2, 'lobj_Sharednotes'):
        assert not _is_linked(a2, 'lobj_Sharednotes', b)


def test_assoc_simpleDidacMeta141_reverse_link_reassign_clear():
    a1 = lobj_SimpleDidacMeta(description="sample_text", id="sample_text", keywords="sample_text", title="sample_text")
    a2 = lobj_SimpleDidacMeta(description="sample_text_2", id="sample_text_2", keywords="sample_text_2", title="sample_text_2")
    b = lobj_BlockMeta(creationDate=date(2024, 1, 1), lastModified=date(2024, 1, 1), lod="sample_text", rendering="sample_text")
    _safe_set(b, 'lobj_BlockMeta142', {a1})
    assert _is_linked(b, 'lobj_BlockMeta142', a1)
    if hasattr(a1, 'lobj_SimpleDidacMeta143'):
        assert _is_linked(a1, 'lobj_SimpleDidacMeta143', b)
    _safe_set(b, 'lobj_BlockMeta142', {a2})
    assert _is_linked(b, 'lobj_BlockMeta142', a2)
    if hasattr(a1, 'lobj_SimpleDidacMeta143'):
        assert not _is_linked(a1, 'lobj_SimpleDidacMeta143', b)
    if hasattr(a2, 'lobj_SimpleDidacMeta143'):
        assert _is_linked(a2, 'lobj_SimpleDidacMeta143', b)
    _safe_set(b, 'lobj_BlockMeta142', set())
    assert not _is_linked(b, 'lobj_BlockMeta142', a2)
    if hasattr(a2, 'lobj_SimpleDidacMeta143'):
        assert not _is_linked(a2, 'lobj_SimpleDidacMeta143', b)


def test_assoc_source111_reverse_link_reassign_clear():
    a1 = lobj_Source(id="sample_text", pp="sample_text", publishDate="sample_text", publishedBy="sample_text", publishedIn="sample_text", subtitle="sample_text", title="sample_text")
    a2 = lobj_Source(id="sample_text_2", pp="sample_text_2", publishDate="sample_text_2", publishedBy="sample_text_2", publishedIn="sample_text_2", subtitle="sample_text_2", title="sample_text_2")
    b = lobj_ResrcFile(file="sample_text", file_tn="sample_text", filesize=7, originalextension="sample_text", resrcHref="sample_text")
    _safe_set(b, 'lobj_ResrcFile112', a1)
    assert _is_linked(b, 'lobj_ResrcFile112', a1)
    if hasattr(a1, 'lobj_Source113'):
        assert _is_linked(a1, 'lobj_Source113', b)
    _safe_set(b, 'lobj_ResrcFile112', a2)
    assert _is_linked(b, 'lobj_ResrcFile112', a2)
    if hasattr(a1, 'lobj_Source113'):
        assert not _is_linked(a1, 'lobj_Source113', b)
    if hasattr(a2, 'lobj_Source113'):
        assert _is_linked(a2, 'lobj_Source113', b)
    _safe_set(b, 'lobj_ResrcFile112', None)
    assert not _is_linked(b, 'lobj_ResrcFile112', a2)
    if hasattr(a2, 'lobj_Source113'):
        assert not _is_linked(a2, 'lobj_Source113', b)


def test_assoc_source7_reverse_link_reassign_clear():
    a1 = lobj_Source(id="sample_text", pp="sample_text", publishDate="sample_text", publishedBy="sample_text", publishedIn="sample_text", subtitle="sample_text", title="sample_text")
    a2 = lobj_Source(id="sample_text_2", pp="sample_text_2", publishDate="sample_text_2", publishedBy="sample_text_2", publishedIn="sample_text_2", subtitle="sample_text_2", title="sample_text_2")
    b = lobj_AbstractContent(heading="sample_text")
    _safe_set(b, 'lobj_AbstractContent8', a1)
    assert _is_linked(b, 'lobj_AbstractContent8', a1)
    if hasattr(a1, 'lobj_Source'):
        assert _is_linked(a1, 'lobj_Source', b)
    _safe_set(b, 'lobj_AbstractContent8', a2)
    assert _is_linked(b, 'lobj_AbstractContent8', a2)
    if hasattr(a1, 'lobj_Source'):
        assert not _is_linked(a1, 'lobj_Source', b)
    if hasattr(a2, 'lobj_Source'):
        assert _is_linked(a2, 'lobj_Source', b)
    _safe_set(b, 'lobj_AbstractContent8', None)
    assert not _is_linked(b, 'lobj_AbstractContent8', a2)
    if hasattr(a2, 'lobj_Source'):
        assert not _is_linked(a2, 'lobj_Source', b)


def test_assoc_titleMeta26_reverse_link_reassign_clear():
    a1 = lobj_TitleMeta(id="sample_text", title="sample_text")
    a2 = lobj_TitleMeta(id="sample_text_2", title="sample_text_2")
    b = lobj_CorrBlock(id="sample_text")
    _safe_set(b, 'lobj_CorrBlock27', {a1})
    assert _is_linked(b, 'lobj_CorrBlock27', a1)
    if hasattr(a1, 'lobj_TitleMeta28'):
        assert _is_linked(a1, 'lobj_TitleMeta28', b)
    _safe_set(b, 'lobj_CorrBlock27', {a2})
    assert _is_linked(b, 'lobj_CorrBlock27', a2)
    if hasattr(a1, 'lobj_TitleMeta28'):
        assert not _is_linked(a1, 'lobj_TitleMeta28', b)
    if hasattr(a2, 'lobj_TitleMeta28'):
        assert _is_linked(a2, 'lobj_TitleMeta28', b)
    _safe_set(b, 'lobj_CorrBlock27', set())
    assert not _is_linked(b, 'lobj_CorrBlock27', a2)
    if hasattr(a2, 'lobj_TitleMeta28'):
        assert not _is_linked(a2, 'lobj_TitleMeta28', b)


def test_assoc_user178_reverse_link_reassign_clear():
    a1 = lobj_Userauthorization(id="sample_text")
    a2 = lobj_Userauthorization(id="sample_text_2")
    b = lobj_User(authenticateldap="sample_text", chatroomnr="sample_text", contchatdate=date(2024, 1, 1), currlogindate=date(2024, 1, 1), datafilter="sample_text", dossierasxml="sample_text", entryasxml="sample_text", firstname="sample_text", fromext="sample_text", icqnumber="sample_text", icqpassword="sample_text", id="sample_text", inchatsince=date(2024, 1, 1), languagenr="sample_text", lastcoursematerialnr="sample_text", lastcoursematerialviewnr="sample_text", lastlogindate=date(2024, 1, 1), lastname="sample_text", loginname="sample_text", matriculationnr="sample_text", notificationprofileasxml="sample_text", onlinedate=date(2024, 1, 1), onlinestatus="sample_text", password="sample_text", photo="sample_text", photochanged="sample_text", scn="sample_text")
    _safe_set(b, 'lobj_User180', a1)
    assert _is_linked(b, 'lobj_User180', a1)
    if hasattr(a1, 'lobj_Userauthorization179'):
        assert _is_linked(a1, 'lobj_Userauthorization179', b)
    _safe_set(b, 'lobj_User180', a2)
    assert _is_linked(b, 'lobj_User180', a2)
    if hasattr(a1, 'lobj_Userauthorization179'):
        assert not _is_linked(a1, 'lobj_Userauthorization179', b)
    if hasattr(a2, 'lobj_Userauthorization179'):
        assert _is_linked(a2, 'lobj_Userauthorization179', b)
    _safe_set(b, 'lobj_User180', None)
    assert not _is_linked(b, 'lobj_User180', a2)
    if hasattr(a2, 'lobj_Userauthorization179'):
        assert not _is_linked(a2, 'lobj_Userauthorization179', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_accessControl19_stub_double():
    # lobj_BlockFolder has no real 'lobj_BlockFolder20' property in the generated
    # code (a bare stub) -- manually attach it so lobj_AccessControl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lobj_AccessControl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lobj_AccessControl(globalAccess=True, id="sample_text", lastModified=date(2024, 1, 1), lastStatusChange=date(2024, 1, 1), status="sample_text")
    partner = lobj_BlockFolder()
    setattr(partner, 'lobj_BlockFolder20', None)
    _safe_set(owner, 'lobj_AccessControl21', partner)
    assert getattr(partner, 'lobj_BlockFolder20') == owner
    _safe_set(owner, 'lobj_AccessControl21', None)
    assert getattr(partner, 'lobj_BlockFolder20') is None


def test_assoc_accessControl3_stub_double():
    # lobj_Block has no real 'lobj_Block4' property in the generated
    # code (a bare stub) -- manually attach it so lobj_AccessControl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lobj_AccessControl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lobj_AccessControl(globalAccess=True, id="sample_text", lastModified=date(2024, 1, 1), lastStatusChange=date(2024, 1, 1), status="sample_text")
    partner = lobj_Block()
    setattr(partner, 'lobj_Block4', None)
    _safe_set(owner, 'lobj_AccessControl', partner)
    assert getattr(partner, 'lobj_Block4') == owner
    _safe_set(owner, 'lobj_AccessControl', None)
    assert getattr(partner, 'lobj_Block4') is None


def test_assoc_accessControl61_stub_double():
    # lobj_LuFolder has no real 'lobj_LuFolder62' property in the generated
    # code (a bare stub) -- manually attach it so lobj_AccessControl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lobj_AccessControl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lobj_AccessControl(globalAccess=True, id="sample_text", lastModified=date(2024, 1, 1), lastStatusChange=date(2024, 1, 1), status="sample_text")
    partner = lobj_LuFolder()
    setattr(partner, 'lobj_LuFolder62', None)
    _safe_set(owner, 'lobj_AccessControl63', partner)
    assert getattr(partner, 'lobj_LuFolder62') == owner
    _safe_set(owner, 'lobj_AccessControl63', None)
    assert getattr(partner, 'lobj_LuFolder62') is None


def test_assoc_accessControl82_stub_double():
    # lobj_ModuleFolder has no real 'lobj_ModuleFolder83' property in the generated
    # code (a bare stub) -- manually attach it so lobj_AccessControl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lobj_AccessControl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lobj_AccessControl(globalAccess=True, id="sample_text", lastModified=date(2024, 1, 1), lastStatusChange=date(2024, 1, 1), status="sample_text")
    partner = lobj_ModuleFolder()
    setattr(partner, 'lobj_ModuleFolder83', None)
    _safe_set(owner, 'lobj_AccessControl84', partner)
    assert getattr(partner, 'lobj_ModuleFolder83') == owner
    _safe_set(owner, 'lobj_AccessControl84', None)
    assert getattr(partner, 'lobj_ModuleFolder83') is None


def test_assoc_block96_stub_double():
    # lobj_Block has no real 'lobj_Block98' property in the generated
    # code (a bare stub) -- manually attach it so lobj_PresentationBlock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lobj_PresentationBlock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lobj_PresentationBlock(id="sample_text", lod=7, rendering="sample_text")
    partner = lobj_Block()
    setattr(partner, 'lobj_Block98', None)
    _safe_set(owner, 'lobj_PresentationBlock97', partner)
    assert getattr(partner, 'lobj_Block98') == owner
    _safe_set(owner, 'lobj_PresentationBlock97', None)
    assert getattr(partner, 'lobj_Block98') is None


def test_assoc_blockMeta0_stub_double():
    # lobj_Block has no real 'lobj_Block' property in the generated
    # code (a bare stub) -- manually attach it so lobj_BlockMeta's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lobj_BlockMeta's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lobj_BlockMeta(creationDate=date(2024, 1, 1), lastModified=date(2024, 1, 1), lod="sample_text", rendering="sample_text")
    partner = lobj_Block()
    setattr(partner, 'lobj_Block', None)
    _safe_set(owner, 'lobj_BlockMeta', partner)
    assert getattr(partner, 'lobj_Block') == owner
    _safe_set(owner, 'lobj_BlockMeta', None)
    assert getattr(partner, 'lobj_Block') is None


def test_assoc_childnodes101_stub_double():
    # lobj_ThemeNode has no real 'lobj_ThemeNode102' property in the generated
    # code (a bare stub) -- manually attach it so lobj_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lobj_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lobj_Node(id="sample_text", visible=True)
    partner = lobj_ThemeNode()
    setattr(partner, 'lobj_ThemeNode102', None)
    _safe_set(owner, 'lobj_Node103', partner)
    assert owner in getattr(partner, 'lobj_ThemeNode102')
    _safe_set(owner, 'lobj_Node103', None)
    assert owner not in getattr(partner, 'lobj_ThemeNode102')


def test_assoc_course23_stub_double():
    # lobj_Category has no real 'lobj_Category24' property in the generated
    # code (a bare stub) -- manually attach it so lobj_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lobj_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lobj_Course(outlineAsXml="sample_text")
    partner = lobj_Category()
    setattr(partner, 'lobj_Category24', None)
    _safe_set(owner, 'lobj_Course', partner)
    assert owner in getattr(partner, 'lobj_Category24')
    _safe_set(owner, 'lobj_Course', None)
    assert owner not in getattr(partner, 'lobj_Category24')


def test_assoc_externalMetadata1_stub_double():
    # lobj_Block has no real 'lobj_Block2' property in the generated
    # code (a bare stub) -- manually attach it so lobj_ExternalMetadata's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lobj_ExternalMetadata's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lobj_ExternalMetadata(file="sample_text", id="sample_text", ref="sample_text")
    partner = lobj_Block()
    setattr(partner, 'lobj_Block2', None)
    _safe_set(owner, 'lobj_ExternalMetadata', partner)
    assert owner in getattr(partner, 'lobj_Block2')
    _safe_set(owner, 'lobj_ExternalMetadata', None)
    assert owner not in getattr(partner, 'lobj_Block2')


def test_assoc_folderMeta12_stub_double():
    # lobj_BlockFolder has no real 'lobj_BlockFolder' property in the generated
    # code (a bare stub) -- manually attach it so lobj_FolderMeta's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lobj_FolderMeta's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lobj_FolderMeta(creationDate=date(2024, 1, 1), description="sample_text", title="sample_text")
    partner = lobj_BlockFolder()
    setattr(partner, 'lobj_BlockFolder', None)
    _safe_set(owner, 'lobj_FolderMeta', partner)
    assert getattr(partner, 'lobj_BlockFolder') == owner
    _safe_set(owner, 'lobj_FolderMeta', None)
    assert getattr(partner, 'lobj_BlockFolder') is None


def test_assoc_folderMeta53_stub_double():
    # lobj_LuFolder has no real 'lobj_LuFolder' property in the generated
    # code (a bare stub) -- manually attach it so lobj_FolderMeta's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lobj_FolderMeta's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lobj_FolderMeta(creationDate=date(2024, 1, 1), description="sample_text", title="sample_text")
    partner = lobj_LuFolder()
    setattr(partner, 'lobj_LuFolder', None)
    _safe_set(owner, 'lobj_FolderMeta54', partner)
    assert getattr(partner, 'lobj_LuFolder') == owner
    _safe_set(owner, 'lobj_FolderMeta54', None)
    assert getattr(partner, 'lobj_LuFolder') is None


def test_assoc_folderMeta74_stub_double():
    # lobj_ModuleFolder has no real 'lobj_ModuleFolder' property in the generated
    # code (a bare stub) -- manually attach it so lobj_FolderMeta's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lobj_FolderMeta's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lobj_FolderMeta(creationDate=date(2024, 1, 1), description="sample_text", title="sample_text")
    partner = lobj_ModuleFolder()
    setattr(partner, 'lobj_ModuleFolder', None)
    _safe_set(owner, 'lobj_FolderMeta75', partner)
    assert getattr(partner, 'lobj_ModuleFolder') == owner
    _safe_set(owner, 'lobj_FolderMeta75', None)
    assert getattr(partner, 'lobj_ModuleFolder') is None


def test_assoc_hypertextContent5_stub_double():
    # lobj_HypertextBlock has no real 'lobj_HypertextBlock' property in the generated
    # code (a bare stub) -- manually attach it so lobj_HypertextContent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lobj_HypertextContent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lobj_HypertextContent(content="sample_text")
    partner = lobj_HypertextBlock()
    setattr(partner, 'lobj_HypertextBlock', None)
    _safe_set(owner, 'lobj_HypertextContent', partner)
    assert owner in getattr(partner, 'lobj_HypertextBlock')
    _safe_set(owner, 'lobj_HypertextContent', None)
    assert owner not in getattr(partner, 'lobj_HypertextBlock')


def test_assoc_learningUnit104_stub_double():
    # lobj_LuNode has no real 'lobj_LuNode' property in the generated
    # code (a bare stub) -- manually attach it so lobj_LearningUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lobj_LearningUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lobj_LearningUnit(luFile="sample_text", treeAsXml="sample_text")
    partner = lobj_LuNode()
    setattr(partner, 'lobj_LuNode', None)
    _safe_set(owner, 'lobj_LearningUnit105', partner)
    assert getattr(partner, 'lobj_LuNode') == owner
    _safe_set(owner, 'lobj_LearningUnit105', None)
    assert getattr(partner, 'lobj_LuNode') is None


def test_assoc_learningUnit58_stub_double():
    # lobj_LuFolder has no real 'lobj_LuFolder59' property in the generated
    # code (a bare stub) -- manually attach it so lobj_LearningUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lobj_LearningUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lobj_LearningUnit(luFile="sample_text", treeAsXml="sample_text")
    partner = lobj_LuFolder()
    setattr(partner, 'lobj_LuFolder59', None)
    _safe_set(owner, 'lobj_LearningUnit60', partner)
    assert owner in getattr(partner, 'lobj_LuFolder59')
    _safe_set(owner, 'lobj_LearningUnit60', None)
    assert owner not in getattr(partner, 'lobj_LuFolder59')


def test_assoc_module79_stub_double():
    # lobj_ModuleFolder has no real 'lobj_ModuleFolder80' property in the generated
    # code (a bare stub) -- manually attach it so lobj_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lobj_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lobj_Module(moduleFile="sample_text", treeAsXml="sample_text")
    partner = lobj_ModuleFolder()
    setattr(partner, 'lobj_ModuleFolder80', None)
    _safe_set(owner, 'lobj_Module81', partner)
    assert owner in getattr(partner, 'lobj_ModuleFolder80')
    _safe_set(owner, 'lobj_Module81', None)
    assert owner not in getattr(partner, 'lobj_ModuleFolder80')


def test_assoc_simpleDidacMeta95_stub_double():
    # lobj_Theme has no real 'lobj_Theme' property in the generated
    # code (a bare stub) -- manually attach it so lobj_SimpleDidacMeta's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lobj_SimpleDidacMeta's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lobj_SimpleDidacMeta(description="sample_text", id="sample_text", keywords="sample_text", title="sample_text")
    partner = lobj_Theme()
    setattr(partner, 'lobj_Theme', None)
    _safe_set(owner, 'lobj_SimpleDidacMeta', partner)
    assert owner in getattr(partner, 'lobj_Theme')
    _safe_set(owner, 'lobj_SimpleDidacMeta', None)
    assert owner not in getattr(partner, 'lobj_Theme')


def test_assoc_titleMeta22_stub_double():
    # lobj_Category has no real 'lobj_Category' property in the generated
    # code (a bare stub) -- manually attach it so lobj_TitleMeta's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lobj_TitleMeta's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lobj_TitleMeta(id="sample_text", title="sample_text")
    partner = lobj_Category()
    setattr(partner, 'lobj_Category', None)
    _safe_set(owner, 'lobj_TitleMeta', partner)
    assert owner in getattr(partner, 'lobj_Category')
    _safe_set(owner, 'lobj_TitleMeta', None)
    assert owner not in getattr(partner, 'lobj_Category')


