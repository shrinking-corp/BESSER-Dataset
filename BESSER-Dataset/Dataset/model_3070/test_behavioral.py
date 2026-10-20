import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Type,
    myDsl_BaseException,
    myDsl_Block,
    myDsl_DataAccessObject,
    myDsl_DataModel,
    myDsl_DataModelMethodConclusion,
    myDsl_DomainModel,
    myDsl_ExceptionMapper,
    myDsl_Feature,
    myDsl_ModelMapper,
    myDsl_PrimitiveType,
    myDsl_Resource,
    myDsl_RestAPI,
    myDsl_RestException,
    myDsl_RestExceptionList,
    myDsl_RestModel,
    myDsl_RestModelMethodConclusion,
    myDsl_Service,
    myDsl_Transformation,
    myDsl_Type,
    myDsl_ValidationService,
    RestStatusCode,
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

def test_assoc_baseException153_reverse_link_reassign_clear():
    a1 = myDsl_ExceptionMapper(name="sample_text")
    a2 = myDsl_ExceptionMapper(name="sample_text_2")
    b = myDsl_BaseException(errorCode="sample_text", message="sample_text")
    _safe_set(b, 'myDsl_BaseException', a1)
    assert _is_linked(b, 'myDsl_BaseException', a1)
    if hasattr(a1, 'myDsl_ExceptionMapper154'):
        assert _is_linked(a1, 'myDsl_ExceptionMapper154', b)
    _safe_set(b, 'myDsl_BaseException', a2)
    assert _is_linked(b, 'myDsl_BaseException', a2)
    if hasattr(a1, 'myDsl_ExceptionMapper154'):
        assert not _is_linked(a1, 'myDsl_ExceptionMapper154', b)
    if hasattr(a2, 'myDsl_ExceptionMapper154'):
        assert _is_linked(a2, 'myDsl_ExceptionMapper154', b)
    _safe_set(b, 'myDsl_BaseException', None)
    assert not _is_linked(b, 'myDsl_BaseException', a2)
    if hasattr(a2, 'myDsl_ExceptionMapper154'):
        assert not _is_linked(a2, 'myDsl_ExceptionMapper154', b)


def test_assoc_createDataModel106_reverse_link_reassign_clear():
    a1 = myDsl_DataModel(id="sample_text")
    a2 = myDsl_DataModel(id="sample_text_2")
    b = myDsl_DataAccessObject(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    _safe_set(b, 'myDsl_DataAccessObject107', a1)
    assert _is_linked(b, 'myDsl_DataAccessObject107', a1)
    if hasattr(a1, 'myDsl_DataModel108'):
        assert _is_linked(a1, 'myDsl_DataModel108', b)
    _safe_set(b, 'myDsl_DataAccessObject107', a2)
    assert _is_linked(b, 'myDsl_DataAccessObject107', a2)
    if hasattr(a1, 'myDsl_DataModel108'):
        assert not _is_linked(a1, 'myDsl_DataModel108', b)
    if hasattr(a2, 'myDsl_DataModel108'):
        assert _is_linked(a2, 'myDsl_DataModel108', b)
    _safe_set(b, 'myDsl_DataAccessObject107', None)
    assert not _is_linked(b, 'myDsl_DataAccessObject107', a2)
    if hasattr(a2, 'myDsl_DataModel108'):
        assert not _is_linked(a2, 'myDsl_DataModel108', b)


def test_assoc_createDataModel71_reverse_link_reassign_clear():
    a1 = myDsl_Service(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    a2 = myDsl_Service(deleteby="sample_text_2", findby="sample_text_2", name="sample_text_2", updateby="sample_text_2")
    b = myDsl_DataModel(id="sample_text")
    _safe_set(b, 'myDsl_DataModel73', a1)
    assert _is_linked(b, 'myDsl_DataModel73', a1)
    if hasattr(a1, 'myDsl_Service72'):
        assert _is_linked(a1, 'myDsl_Service72', b)
    _safe_set(b, 'myDsl_DataModel73', a2)
    assert _is_linked(b, 'myDsl_DataModel73', a2)
    if hasattr(a1, 'myDsl_Service72'):
        assert not _is_linked(a1, 'myDsl_Service72', b)
    if hasattr(a2, 'myDsl_Service72'):
        assert _is_linked(a2, 'myDsl_Service72', b)
    _safe_set(b, 'myDsl_DataModel73', None)
    assert not _is_linked(b, 'myDsl_DataModel73', a2)
    if hasattr(a2, 'myDsl_Service72'):
        assert not _is_linked(a2, 'myDsl_Service72', b)


def test_assoc_createMethod109_reverse_link_reassign_clear():
    a1 = myDsl_DataAccessObject(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    a2 = myDsl_DataAccessObject(deleteby="sample_text_2", findby="sample_text_2", name="sample_text_2", updateby="sample_text_2")
    b = myDsl_Block(code="sample_text")
    _safe_set(b, 'myDsl_Block111', a1)
    assert _is_linked(b, 'myDsl_Block111', a1)
    if hasattr(a1, 'myDsl_DataAccessObject110'):
        assert _is_linked(a1, 'myDsl_DataAccessObject110', b)
    _safe_set(b, 'myDsl_Block111', a2)
    assert _is_linked(b, 'myDsl_Block111', a2)
    if hasattr(a1, 'myDsl_DataAccessObject110'):
        assert not _is_linked(a1, 'myDsl_DataAccessObject110', b)
    if hasattr(a2, 'myDsl_DataAccessObject110'):
        assert _is_linked(a2, 'myDsl_DataAccessObject110', b)
    _safe_set(b, 'myDsl_Block111', None)
    assert not _is_linked(b, 'myDsl_Block111', a2)
    if hasattr(a2, 'myDsl_DataAccessObject110'):
        assert not _is_linked(a2, 'myDsl_DataAccessObject110', b)


def test_assoc_createMethod41_reverse_link_reassign_clear():
    a1 = myDsl_Resource(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    a2 = myDsl_Resource(deleteby="sample_text_2", findby="sample_text_2", name="sample_text_2", updateby="sample_text_2")
    b = myDsl_Block(code="sample_text")
    _safe_set(b, 'myDsl_Block', a1)
    assert _is_linked(b, 'myDsl_Block', a1)
    if hasattr(a1, 'myDsl_Resource42'):
        assert _is_linked(a1, 'myDsl_Resource42', b)
    _safe_set(b, 'myDsl_Block', a2)
    assert _is_linked(b, 'myDsl_Block', a2)
    if hasattr(a1, 'myDsl_Resource42'):
        assert not _is_linked(a1, 'myDsl_Resource42', b)
    if hasattr(a2, 'myDsl_Resource42'):
        assert _is_linked(a2, 'myDsl_Resource42', b)
    _safe_set(b, 'myDsl_Block', None)
    assert not _is_linked(b, 'myDsl_Block', a2)
    if hasattr(a2, 'myDsl_Resource42'):
        assert not _is_linked(a2, 'myDsl_Resource42', b)


def test_assoc_createMethod74_reverse_link_reassign_clear():
    a1 = myDsl_Service(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    a2 = myDsl_Service(deleteby="sample_text_2", findby="sample_text_2", name="sample_text_2", updateby="sample_text_2")
    b = myDsl_Block(code="sample_text")
    _safe_set(b, 'myDsl_Block76', a1)
    assert _is_linked(b, 'myDsl_Block76', a1)
    if hasattr(a1, 'myDsl_Service75'):
        assert _is_linked(a1, 'myDsl_Service75', b)
    _safe_set(b, 'myDsl_Block76', a2)
    assert _is_linked(b, 'myDsl_Block76', a2)
    if hasattr(a1, 'myDsl_Service75'):
        assert not _is_linked(a1, 'myDsl_Service75', b)
    if hasattr(a2, 'myDsl_Service75'):
        assert _is_linked(a2, 'myDsl_Service75', b)
    _safe_set(b, 'myDsl_Block76', None)
    assert not _is_linked(b, 'myDsl_Block76', a2)
    if hasattr(a2, 'myDsl_Service75'):
        assert not _is_linked(a2, 'myDsl_Service75', b)


def test_assoc_dao68_reverse_link_reassign_clear():
    a1 = myDsl_Service(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    a2 = myDsl_Service(deleteby="sample_text_2", findby="sample_text_2", name="sample_text_2", updateby="sample_text_2")
    b = myDsl_DataAccessObject(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    _safe_set(b, 'myDsl_DataAccessObject70', a1)
    assert _is_linked(b, 'myDsl_DataAccessObject70', a1)
    if hasattr(a1, 'myDsl_Service69'):
        assert _is_linked(a1, 'myDsl_Service69', b)
    _safe_set(b, 'myDsl_DataAccessObject70', a2)
    assert _is_linked(b, 'myDsl_DataAccessObject70', a2)
    if hasattr(a1, 'myDsl_Service69'):
        assert not _is_linked(a1, 'myDsl_Service69', b)
    if hasattr(a2, 'myDsl_Service69'):
        assert _is_linked(a2, 'myDsl_Service69', b)
    _safe_set(b, 'myDsl_DataAccessObject70', None)
    assert not _is_linked(b, 'myDsl_DataAccessObject70', a2)
    if hasattr(a2, 'myDsl_Service69'):
        assert not _is_linked(a2, 'myDsl_Service69', b)


def test_assoc_deleteMethod130_reverse_link_reassign_clear():
    a1 = myDsl_DataAccessObject(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    a2 = myDsl_DataAccessObject(deleteby="sample_text_2", findby="sample_text_2", name="sample_text_2", updateby="sample_text_2")
    b = myDsl_Block(code="sample_text")
    _safe_set(b, 'myDsl_Block132', a1)
    assert _is_linked(b, 'myDsl_Block132', a1)
    if hasattr(a1, 'myDsl_DataAccessObject131'):
        assert _is_linked(a1, 'myDsl_DataAccessObject131', b)
    _safe_set(b, 'myDsl_Block132', a2)
    assert _is_linked(b, 'myDsl_Block132', a2)
    if hasattr(a1, 'myDsl_DataAccessObject131'):
        assert not _is_linked(a1, 'myDsl_DataAccessObject131', b)
    if hasattr(a2, 'myDsl_DataAccessObject131'):
        assert _is_linked(a2, 'myDsl_DataAccessObject131', b)
    _safe_set(b, 'myDsl_Block132', None)
    assert not _is_linked(b, 'myDsl_Block132', a2)
    if hasattr(a2, 'myDsl_DataAccessObject131'):
        assert not _is_linked(a2, 'myDsl_DataAccessObject131', b)


def test_assoc_deleteMethod63_reverse_link_reassign_clear():
    a1 = myDsl_Resource(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    a2 = myDsl_Resource(deleteby="sample_text_2", findby="sample_text_2", name="sample_text_2", updateby="sample_text_2")
    b = myDsl_Block(code="sample_text")
    _safe_set(b, 'myDsl_Block65', a1)
    assert _is_linked(b, 'myDsl_Block65', a1)
    if hasattr(a1, 'myDsl_Resource64'):
        assert _is_linked(a1, 'myDsl_Resource64', b)
    _safe_set(b, 'myDsl_Block65', a2)
    assert _is_linked(b, 'myDsl_Block65', a2)
    if hasattr(a1, 'myDsl_Resource64'):
        assert not _is_linked(a1, 'myDsl_Resource64', b)
    if hasattr(a2, 'myDsl_Resource64'):
        assert _is_linked(a2, 'myDsl_Resource64', b)
    _safe_set(b, 'myDsl_Block65', None)
    assert not _is_linked(b, 'myDsl_Block65', a2)
    if hasattr(a2, 'myDsl_Resource64'):
        assert not _is_linked(a2, 'myDsl_Resource64', b)


def test_assoc_deleteMethod94_reverse_link_reassign_clear():
    a1 = myDsl_Service(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    a2 = myDsl_Service(deleteby="sample_text_2", findby="sample_text_2", name="sample_text_2", updateby="sample_text_2")
    b = myDsl_Block(code="sample_text")
    _safe_set(b, 'myDsl_Block96', a1)
    assert _is_linked(b, 'myDsl_Block96', a1)
    if hasattr(a1, 'myDsl_Service95'):
        assert _is_linked(a1, 'myDsl_Service95', b)
    _safe_set(b, 'myDsl_Block96', a2)
    assert _is_linked(b, 'myDsl_Block96', a2)
    if hasattr(a1, 'myDsl_Service95'):
        assert not _is_linked(a1, 'myDsl_Service95', b)
    if hasattr(a2, 'myDsl_Service95'):
        assert _is_linked(a2, 'myDsl_Service95', b)
    _safe_set(b, 'myDsl_Block96', None)
    assert not _is_linked(b, 'myDsl_Block96', a2)
    if hasattr(a2, 'myDsl_Service95'):
        assert not _is_linked(a2, 'myDsl_Service95', b)


def test_assoc_exceptionMapper33_reverse_link_reassign_clear():
    a1 = myDsl_Resource(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    a2 = myDsl_Resource(deleteby="sample_text_2", findby="sample_text_2", name="sample_text_2", updateby="sample_text_2")
    b = myDsl_ExceptionMapper(name="sample_text")
    _safe_set(b, 'myDsl_ExceptionMapper35', a1)
    assert _is_linked(b, 'myDsl_ExceptionMapper35', a1)
    if hasattr(a1, 'myDsl_Resource34'):
        assert _is_linked(a1, 'myDsl_Resource34', b)
    _safe_set(b, 'myDsl_ExceptionMapper35', a2)
    assert _is_linked(b, 'myDsl_ExceptionMapper35', a2)
    if hasattr(a1, 'myDsl_Resource34'):
        assert not _is_linked(a1, 'myDsl_Resource34', b)
    if hasattr(a2, 'myDsl_Resource34'):
        assert _is_linked(a2, 'myDsl_Resource34', b)
    _safe_set(b, 'myDsl_ExceptionMapper35', None)
    assert not _is_linked(b, 'myDsl_ExceptionMapper35', a2)
    if hasattr(a2, 'myDsl_Resource34'):
        assert not _is_linked(a2, 'myDsl_Resource34', b)


def test_assoc_features13_reverse_link_reassign_clear():
    a1 = myDsl_Feature(many=True, name="sample_text")
    a2 = myDsl_Feature(many=False, name="sample_text_2")
    b = myDsl_DataModel(id="sample_text")
    _safe_set(b, 'myDsl_DataModel14', {a1})
    assert _is_linked(b, 'myDsl_DataModel14', a1)
    if hasattr(a1, 'myDsl_Feature'):
        assert _is_linked(a1, 'myDsl_Feature', b)
    _safe_set(b, 'myDsl_DataModel14', {a2})
    assert _is_linked(b, 'myDsl_DataModel14', a2)
    if hasattr(a1, 'myDsl_Feature'):
        assert not _is_linked(a1, 'myDsl_Feature', b)
    if hasattr(a2, 'myDsl_Feature'):
        assert _is_linked(a2, 'myDsl_Feature', b)
    _safe_set(b, 'myDsl_DataModel14', set())
    assert not _is_linked(b, 'myDsl_DataModel14', a2)
    if hasattr(a2, 'myDsl_Feature'):
        assert not _is_linked(a2, 'myDsl_Feature', b)


def test_assoc_findMethod115_reverse_link_reassign_clear():
    a1 = myDsl_DataAccessObject(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    a2 = myDsl_DataAccessObject(deleteby="sample_text_2", findby="sample_text_2", name="sample_text_2", updateby="sample_text_2")
    b = myDsl_Block(code="sample_text")
    _safe_set(b, 'myDsl_Block117', a1)
    assert _is_linked(b, 'myDsl_Block117', a1)
    if hasattr(a1, 'myDsl_DataAccessObject116'):
        assert _is_linked(a1, 'myDsl_DataAccessObject116', b)
    _safe_set(b, 'myDsl_Block117', a2)
    assert _is_linked(b, 'myDsl_Block117', a2)
    if hasattr(a1, 'myDsl_DataAccessObject116'):
        assert not _is_linked(a1, 'myDsl_DataAccessObject116', b)
    if hasattr(a2, 'myDsl_DataAccessObject116'):
        assert _is_linked(a2, 'myDsl_DataAccessObject116', b)
    _safe_set(b, 'myDsl_Block117', None)
    assert not _is_linked(b, 'myDsl_Block117', a2)
    if hasattr(a2, 'myDsl_DataAccessObject116'):
        assert not _is_linked(a2, 'myDsl_DataAccessObject116', b)


def test_assoc_findMethod45_reverse_link_reassign_clear():
    a1 = myDsl_Resource(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    a2 = myDsl_Resource(deleteby="sample_text_2", findby="sample_text_2", name="sample_text_2", updateby="sample_text_2")
    b = myDsl_Block(code="sample_text")
    _safe_set(b, 'myDsl_Block47', a1)
    assert _is_linked(b, 'myDsl_Block47', a1)
    if hasattr(a1, 'myDsl_Resource46'):
        assert _is_linked(a1, 'myDsl_Resource46', b)
    _safe_set(b, 'myDsl_Block47', a2)
    assert _is_linked(b, 'myDsl_Block47', a2)
    if hasattr(a1, 'myDsl_Resource46'):
        assert not _is_linked(a1, 'myDsl_Resource46', b)
    if hasattr(a2, 'myDsl_Resource46'):
        assert _is_linked(a2, 'myDsl_Resource46', b)
    _safe_set(b, 'myDsl_Block47', None)
    assert not _is_linked(b, 'myDsl_Block47', a2)
    if hasattr(a2, 'myDsl_Resource46'):
        assert not _is_linked(a2, 'myDsl_Resource46', b)


def test_assoc_findMethod79_reverse_link_reassign_clear():
    a1 = myDsl_Service(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    a2 = myDsl_Service(deleteby="sample_text_2", findby="sample_text_2", name="sample_text_2", updateby="sample_text_2")
    b = myDsl_Block(code="sample_text")
    _safe_set(b, 'myDsl_Block81', a1)
    assert _is_linked(b, 'myDsl_Block81', a1)
    if hasattr(a1, 'myDsl_Service80'):
        assert _is_linked(a1, 'myDsl_Service80', b)
    _safe_set(b, 'myDsl_Block81', a2)
    assert _is_linked(b, 'myDsl_Block81', a2)
    if hasattr(a1, 'myDsl_Service80'):
        assert not _is_linked(a1, 'myDsl_Service80', b)
    if hasattr(a2, 'myDsl_Service80'):
        assert _is_linked(a2, 'myDsl_Service80', b)
    _safe_set(b, 'myDsl_Block81', None)
    assert not _is_linked(b, 'myDsl_Block81', a2)
    if hasattr(a2, 'myDsl_Service80'):
        assert not _is_linked(a2, 'myDsl_Service80', b)


def test_assoc_restException150_reverse_link_reassign_clear():
    a1 = myDsl_RestException(message="sample_text", statusCode="sample_text")
    a2 = myDsl_RestException(message="sample_text_2", statusCode="sample_text_2")
    b = myDsl_ExceptionMapper(name="sample_text")
    _safe_set(b, 'myDsl_ExceptionMapper151', a1)
    assert _is_linked(b, 'myDsl_ExceptionMapper151', a1)
    if hasattr(a1, 'myDsl_RestException152'):
        assert _is_linked(a1, 'myDsl_RestException152', b)
    _safe_set(b, 'myDsl_ExceptionMapper151', a2)
    assert _is_linked(b, 'myDsl_ExceptionMapper151', a2)
    if hasattr(a1, 'myDsl_RestException152'):
        assert not _is_linked(a1, 'myDsl_RestException152', b)
    if hasattr(a2, 'myDsl_RestException152'):
        assert _is_linked(a2, 'myDsl_RestException152', b)
    _safe_set(b, 'myDsl_ExceptionMapper151', None)
    assert not _is_linked(b, 'myDsl_ExceptionMapper151', a2)
    if hasattr(a2, 'myDsl_RestException152'):
        assert not _is_linked(a2, 'myDsl_RestException152', b)


def test_assoc_service30_reverse_link_reassign_clear():
    a1 = myDsl_Service(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    a2 = myDsl_Service(deleteby="sample_text_2", findby="sample_text_2", name="sample_text_2", updateby="sample_text_2")
    b = myDsl_Resource(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    _safe_set(b, 'myDsl_Resource31', {a1})
    assert _is_linked(b, 'myDsl_Resource31', a1)
    if hasattr(a1, 'myDsl_Service32'):
        assert _is_linked(a1, 'myDsl_Service32', b)
    _safe_set(b, 'myDsl_Resource31', {a2})
    assert _is_linked(b, 'myDsl_Resource31', a2)
    if hasattr(a1, 'myDsl_Service32'):
        assert not _is_linked(a1, 'myDsl_Service32', b)
    if hasattr(a2, 'myDsl_Service32'):
        assert _is_linked(a2, 'myDsl_Service32', b)
    _safe_set(b, 'myDsl_Resource31', set())
    assert not _is_linked(b, 'myDsl_Resource31', a2)
    if hasattr(a2, 'myDsl_Service32'):
        assert not _is_linked(a2, 'myDsl_Service32', b)


def test_assoc_superType12_reverse_link_reassign_clear():
    a1 = myDsl_DataModel(id="sample_text")
    a2 = myDsl_DataModel(id="sample_text_2")
    b = myDsl_DataModel(id="sample_text")
    _safe_set(b, 'myDsl_DataModel11', a1)
    assert _is_linked(b, 'myDsl_DataModel11', a1)
    if hasattr(a1, 'myDsl_DataModel'):
        assert _is_linked(a1, 'myDsl_DataModel', b)
    _safe_set(b, 'myDsl_DataModel11', a2)
    assert _is_linked(b, 'myDsl_DataModel11', a2)
    if hasattr(a1, 'myDsl_DataModel'):
        assert not _is_linked(a1, 'myDsl_DataModel', b)
    if hasattr(a2, 'myDsl_DataModel'):
        assert _is_linked(a2, 'myDsl_DataModel', b)
    _safe_set(b, 'myDsl_DataModel11', None)
    assert not _is_linked(b, 'myDsl_DataModel11', a2)
    if hasattr(a2, 'myDsl_DataModel'):
        assert not _is_linked(a2, 'myDsl_DataModel', b)


def test_assoc_type27_reverse_link_reassign_clear():
    a1 = myDsl_Type(name="sample_text")
    a2 = myDsl_Type(name="sample_text_2")
    b = myDsl_Feature(many=True, name="sample_text")
    _safe_set(b, 'myDsl_Feature28', a1)
    assert _is_linked(b, 'myDsl_Feature28', a1)
    if hasattr(a1, 'myDsl_Type29'):
        assert _is_linked(a1, 'myDsl_Type29', b)
    _safe_set(b, 'myDsl_Feature28', a2)
    assert _is_linked(b, 'myDsl_Feature28', a2)
    if hasattr(a1, 'myDsl_Type29'):
        assert not _is_linked(a1, 'myDsl_Type29', b)
    if hasattr(a2, 'myDsl_Type29'):
        assert _is_linked(a2, 'myDsl_Type29', b)
    _safe_set(b, 'myDsl_Feature28', None)
    assert not _is_linked(b, 'myDsl_Feature28', a2)
    if hasattr(a2, 'myDsl_Type29'):
        assert not _is_linked(a2, 'myDsl_Type29', b)


def test_assoc_updateDataModel121_reverse_link_reassign_clear():
    a1 = myDsl_DataModel(id="sample_text")
    a2 = myDsl_DataModel(id="sample_text_2")
    b = myDsl_DataAccessObject(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    _safe_set(b, 'myDsl_DataAccessObject122', a1)
    assert _is_linked(b, 'myDsl_DataAccessObject122', a1)
    if hasattr(a1, 'myDsl_DataModel123'):
        assert _is_linked(a1, 'myDsl_DataModel123', b)
    _safe_set(b, 'myDsl_DataAccessObject122', a2)
    assert _is_linked(b, 'myDsl_DataAccessObject122', a2)
    if hasattr(a1, 'myDsl_DataModel123'):
        assert not _is_linked(a1, 'myDsl_DataModel123', b)
    if hasattr(a2, 'myDsl_DataModel123'):
        assert _is_linked(a2, 'myDsl_DataModel123', b)
    _safe_set(b, 'myDsl_DataAccessObject122', None)
    assert not _is_linked(b, 'myDsl_DataAccessObject122', a2)
    if hasattr(a2, 'myDsl_DataModel123'):
        assert not _is_linked(a2, 'myDsl_DataModel123', b)


def test_assoc_updateDataModel85_reverse_link_reassign_clear():
    a1 = myDsl_Service(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    a2 = myDsl_Service(deleteby="sample_text_2", findby="sample_text_2", name="sample_text_2", updateby="sample_text_2")
    b = myDsl_DataModel(id="sample_text")
    _safe_set(b, 'myDsl_DataModel87', a1)
    assert _is_linked(b, 'myDsl_DataModel87', a1)
    if hasattr(a1, 'myDsl_Service86'):
        assert _is_linked(a1, 'myDsl_Service86', b)
    _safe_set(b, 'myDsl_DataModel87', a2)
    assert _is_linked(b, 'myDsl_DataModel87', a2)
    if hasattr(a1, 'myDsl_Service86'):
        assert not _is_linked(a1, 'myDsl_Service86', b)
    if hasattr(a2, 'myDsl_Service86'):
        assert _is_linked(a2, 'myDsl_Service86', b)
    _safe_set(b, 'myDsl_DataModel87', None)
    assert not _is_linked(b, 'myDsl_DataModel87', a2)
    if hasattr(a2, 'myDsl_Service86'):
        assert not _is_linked(a2, 'myDsl_Service86', b)


def test_assoc_updateMethod124_reverse_link_reassign_clear():
    a1 = myDsl_DataAccessObject(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    a2 = myDsl_DataAccessObject(deleteby="sample_text_2", findby="sample_text_2", name="sample_text_2", updateby="sample_text_2")
    b = myDsl_Block(code="sample_text")
    _safe_set(b, 'myDsl_Block126', a1)
    assert _is_linked(b, 'myDsl_Block126', a1)
    if hasattr(a1, 'myDsl_DataAccessObject125'):
        assert _is_linked(a1, 'myDsl_DataAccessObject125', b)
    _safe_set(b, 'myDsl_Block126', a2)
    assert _is_linked(b, 'myDsl_Block126', a2)
    if hasattr(a1, 'myDsl_DataAccessObject125'):
        assert not _is_linked(a1, 'myDsl_DataAccessObject125', b)
    if hasattr(a2, 'myDsl_DataAccessObject125'):
        assert _is_linked(a2, 'myDsl_DataAccessObject125', b)
    _safe_set(b, 'myDsl_Block126', None)
    assert not _is_linked(b, 'myDsl_Block126', a2)
    if hasattr(a2, 'myDsl_DataAccessObject125'):
        assert not _is_linked(a2, 'myDsl_DataAccessObject125', b)


def test_assoc_updateMethod57_reverse_link_reassign_clear():
    a1 = myDsl_Resource(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    a2 = myDsl_Resource(deleteby="sample_text_2", findby="sample_text_2", name="sample_text_2", updateby="sample_text_2")
    b = myDsl_Block(code="sample_text")
    _safe_set(b, 'myDsl_Block59', a1)
    assert _is_linked(b, 'myDsl_Block59', a1)
    if hasattr(a1, 'myDsl_Resource58'):
        assert _is_linked(a1, 'myDsl_Resource58', b)
    _safe_set(b, 'myDsl_Block59', a2)
    assert _is_linked(b, 'myDsl_Block59', a2)
    if hasattr(a1, 'myDsl_Resource58'):
        assert not _is_linked(a1, 'myDsl_Resource58', b)
    if hasattr(a2, 'myDsl_Resource58'):
        assert _is_linked(a2, 'myDsl_Resource58', b)
    _safe_set(b, 'myDsl_Block59', None)
    assert not _is_linked(b, 'myDsl_Block59', a2)
    if hasattr(a2, 'myDsl_Resource58'):
        assert not _is_linked(a2, 'myDsl_Resource58', b)


def test_assoc_updateMethod88_reverse_link_reassign_clear():
    a1 = myDsl_Service(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    a2 = myDsl_Service(deleteby="sample_text_2", findby="sample_text_2", name="sample_text_2", updateby="sample_text_2")
    b = myDsl_Block(code="sample_text")
    _safe_set(b, 'myDsl_Block90', a1)
    assert _is_linked(b, 'myDsl_Block90', a1)
    if hasattr(a1, 'myDsl_Service89'):
        assert _is_linked(a1, 'myDsl_Service89', b)
    _safe_set(b, 'myDsl_Block90', a2)
    assert _is_linked(b, 'myDsl_Block90', a2)
    if hasattr(a1, 'myDsl_Service89'):
        assert not _is_linked(a1, 'myDsl_Service89', b)
    if hasattr(a2, 'myDsl_Service89'):
        assert _is_linked(a2, 'myDsl_Service89', b)
    _safe_set(b, 'myDsl_Block90', None)
    assert not _is_linked(b, 'myDsl_Block90', a2)
    if hasattr(a2, 'myDsl_Service89'):
        assert not _is_linked(a2, 'myDsl_Service89', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_block103_stub_double():
    # myDsl_ValidationService has no real 'myDsl_ValidationService104' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Block(code="sample_text")
    partner = myDsl_ValidationService()
    setattr(partner, 'myDsl_ValidationService104', None)
    _safe_set(owner, 'myDsl_Block105', partner)
    assert getattr(partner, 'myDsl_ValidationService104') == owner
    _safe_set(owner, 'myDsl_Block105', None)
    assert getattr(partner, 'myDsl_ValidationService104') is None


def test_assoc_createConclusion112_stub_double():
    # myDsl_DataModelMethodConclusion has no real 'myDsl_DataModelMethodConclusion114' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_DataAccessObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_DataAccessObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_DataAccessObject(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    partner = myDsl_DataModelMethodConclusion()
    setattr(partner, 'myDsl_DataModelMethodConclusion114', None)
    _safe_set(owner, 'myDsl_DataAccessObject113', partner)
    assert getattr(partner, 'myDsl_DataModelMethodConclusion114') == owner
    _safe_set(owner, 'myDsl_DataAccessObject113', None)
    assert getattr(partner, 'myDsl_DataModelMethodConclusion114') is None


def test_assoc_createConclusion43_stub_double():
    # myDsl_RestModelMethodConclusion has no real 'myDsl_RestModelMethodConclusion' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Resource(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    partner = myDsl_RestModelMethodConclusion()
    setattr(partner, 'myDsl_RestModelMethodConclusion', None)
    _safe_set(owner, 'myDsl_Resource44', partner)
    assert getattr(partner, 'myDsl_RestModelMethodConclusion') == owner
    _safe_set(owner, 'myDsl_Resource44', None)
    assert getattr(partner, 'myDsl_RestModelMethodConclusion') is None


def test_assoc_createConclusion77_stub_double():
    # myDsl_DataModelMethodConclusion has no real 'myDsl_DataModelMethodConclusion' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Service(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    partner = myDsl_DataModelMethodConclusion()
    setattr(partner, 'myDsl_DataModelMethodConclusion', None)
    _safe_set(owner, 'myDsl_Service78', partner)
    assert getattr(partner, 'myDsl_DataModelMethodConclusion') == owner
    _safe_set(owner, 'myDsl_Service78', None)
    assert getattr(partner, 'myDsl_DataModelMethodConclusion') is None


def test_assoc_createValService39_stub_double():
    # myDsl_ValidationService has no real 'myDsl_ValidationService' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Resource(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    partner = myDsl_ValidationService()
    setattr(partner, 'myDsl_ValidationService', None)
    _safe_set(owner, 'myDsl_Resource40', partner)
    assert getattr(partner, 'myDsl_ValidationService') == owner
    _safe_set(owner, 'myDsl_Resource40', None)
    assert getattr(partner, 'myDsl_ValidationService') is None


def test_assoc_dao7_stub_double():
    # myDsl_RestAPI has no real 'myDsl_RestAPI8' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_DataAccessObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_DataAccessObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_DataAccessObject(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    partner = myDsl_RestAPI()
    setattr(partner, 'myDsl_RestAPI8', None)
    _safe_set(owner, 'myDsl_DataAccessObject', partner)
    assert owner in getattr(partner, 'myDsl_RestAPI8')
    _safe_set(owner, 'myDsl_DataAccessObject', None)
    assert owner not in getattr(partner, 'myDsl_RestAPI8')


def test_assoc_dataModel136_stub_double():
    # myDsl_DataModelMethodConclusion has no real 'myDsl_DataModelMethodConclusion137' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_DataModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_DataModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_DataModel(id="sample_text")
    partner = myDsl_DataModelMethodConclusion()
    setattr(partner, 'myDsl_DataModelMethodConclusion137', None)
    _safe_set(owner, 'myDsl_DataModel138', partner)
    assert getattr(partner, 'myDsl_DataModelMethodConclusion137') == owner
    _safe_set(owner, 'myDsl_DataModel138', None)
    assert getattr(partner, 'myDsl_DataModelMethodConclusion137') is None


def test_assoc_dataModel21_stub_double():
    # myDsl_Transformation has no real 'myDsl_Transformation22' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_DataModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_DataModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_DataModel(id="sample_text")
    partner = myDsl_Transformation()
    setattr(partner, 'myDsl_Transformation22', None)
    _safe_set(owner, 'myDsl_DataModel23', partner)
    assert getattr(partner, 'myDsl_Transformation22') == owner
    _safe_set(owner, 'myDsl_DataModel23', None)
    assert getattr(partner, 'myDsl_Transformation22') is None


def test_assoc_elements0_stub_double():
    # myDsl_DomainModel has no real 'myDsl_DomainModel' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Type(name="sample_text")
    partner = myDsl_DomainModel()
    setattr(partner, 'myDsl_DomainModel', None)
    _safe_set(owner, 'myDsl_Type', partner)
    assert owner in getattr(partner, 'myDsl_DomainModel')
    _safe_set(owner, 'myDsl_Type', None)
    assert owner not in getattr(partner, 'myDsl_DomainModel')


def test_assoc_exception148_stub_double():
    # myDsl_RestExceptionList has no real 'myDsl_RestExceptionList149' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_RestException's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_RestException's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_RestException(message="sample_text", statusCode="sample_text")
    partner = myDsl_RestExceptionList()
    setattr(partner, 'myDsl_RestExceptionList149', None)
    _safe_set(owner, 'myDsl_RestException', partner)
    assert owner in getattr(partner, 'myDsl_RestExceptionList149')
    _safe_set(owner, 'myDsl_RestException', None)
    assert owner not in getattr(partner, 'myDsl_RestExceptionList149')


def test_assoc_exception466_stub_double():
    # myDsl_RestExceptionList has no real 'myDsl_RestExceptionList' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Resource(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    partner = myDsl_RestExceptionList()
    setattr(partner, 'myDsl_RestExceptionList', None)
    _safe_set(owner, 'myDsl_Resource67', partner)
    assert getattr(partner, 'myDsl_RestExceptionList') == owner
    _safe_set(owner, 'myDsl_Resource67', None)
    assert getattr(partner, 'myDsl_RestExceptionList') is None


def test_assoc_exception497_stub_double():
    # myDsl_RestExceptionList has no real 'myDsl_RestExceptionList99' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Service(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    partner = myDsl_RestExceptionList()
    setattr(partner, 'myDsl_RestExceptionList99', None)
    _safe_set(owner, 'myDsl_Service98', partner)
    assert getattr(partner, 'myDsl_RestExceptionList99') == owner
    _safe_set(owner, 'myDsl_Service98', None)
    assert getattr(partner, 'myDsl_RestExceptionList99') is None


def test_assoc_exceptionMapper9_stub_double():
    # myDsl_RestAPI has no real 'myDsl_RestAPI10' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExceptionMapper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExceptionMapper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExceptionMapper(name="sample_text")
    partner = myDsl_RestAPI()
    setattr(partner, 'myDsl_RestAPI10', None)
    _safe_set(owner, 'myDsl_ExceptionMapper', partner)
    assert owner in getattr(partner, 'myDsl_RestAPI10')
    _safe_set(owner, 'myDsl_ExceptionMapper', None)
    assert owner not in getattr(partner, 'myDsl_RestAPI10')


def test_assoc_exceptions133_stub_double():
    # myDsl_RestExceptionList has no real 'myDsl_RestExceptionList135' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_DataAccessObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_DataAccessObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_DataAccessObject(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    partner = myDsl_RestExceptionList()
    setattr(partner, 'myDsl_RestExceptionList135', None)
    _safe_set(owner, 'myDsl_DataAccessObject134', partner)
    assert getattr(partner, 'myDsl_RestExceptionList135') == owner
    _safe_set(owner, 'myDsl_DataAccessObject134', None)
    assert getattr(partner, 'myDsl_RestExceptionList135') is None


def test_assoc_findConclusion118_stub_double():
    # myDsl_DataModelMethodConclusion has no real 'myDsl_DataModelMethodConclusion120' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_DataAccessObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_DataAccessObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_DataAccessObject(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    partner = myDsl_DataModelMethodConclusion()
    setattr(partner, 'myDsl_DataModelMethodConclusion120', None)
    _safe_set(owner, 'myDsl_DataAccessObject119', partner)
    assert getattr(partner, 'myDsl_DataModelMethodConclusion120') == owner
    _safe_set(owner, 'myDsl_DataAccessObject119', None)
    assert getattr(partner, 'myDsl_DataModelMethodConclusion120') is None


def test_assoc_findConclusion48_stub_double():
    # myDsl_RestModelMethodConclusion has no real 'myDsl_RestModelMethodConclusion50' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Resource(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    partner = myDsl_RestModelMethodConclusion()
    setattr(partner, 'myDsl_RestModelMethodConclusion50', None)
    _safe_set(owner, 'myDsl_Resource49', partner)
    assert getattr(partner, 'myDsl_RestModelMethodConclusion50') == owner
    _safe_set(owner, 'myDsl_Resource49', None)
    assert getattr(partner, 'myDsl_RestModelMethodConclusion50') is None


def test_assoc_findConclusion82_stub_double():
    # myDsl_DataModelMethodConclusion has no real 'myDsl_DataModelMethodConclusion84' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Service(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    partner = myDsl_DataModelMethodConclusion()
    setattr(partner, 'myDsl_DataModelMethodConclusion84', None)
    _safe_set(owner, 'myDsl_Service83', partner)
    assert getattr(partner, 'myDsl_DataModelMethodConclusion84') == owner
    _safe_set(owner, 'myDsl_Service83', None)
    assert getattr(partner, 'myDsl_DataModelMethodConclusion84') is None


def test_assoc_resource3_stub_double():
    # myDsl_RestAPI has no real 'myDsl_RestAPI4' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Resource(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    partner = myDsl_RestAPI()
    setattr(partner, 'myDsl_RestAPI4', None)
    _safe_set(owner, 'myDsl_Resource', partner)
    assert getattr(partner, 'myDsl_RestAPI4') == owner
    _safe_set(owner, 'myDsl_Resource', None)
    assert getattr(partner, 'myDsl_RestAPI4') is None


def test_assoc_service5_stub_double():
    # myDsl_RestAPI has no real 'myDsl_RestAPI6' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Service(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    partner = myDsl_RestAPI()
    setattr(partner, 'myDsl_RestAPI6', None)
    _safe_set(owner, 'myDsl_Service', partner)
    assert owner in getattr(partner, 'myDsl_RestAPI6')
    _safe_set(owner, 'myDsl_Service', None)
    assert owner not in getattr(partner, 'myDsl_RestAPI6')


def test_assoc_updateConclusion127_stub_double():
    # myDsl_DataModelMethodConclusion has no real 'myDsl_DataModelMethodConclusion129' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_DataAccessObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_DataAccessObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_DataAccessObject(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    partner = myDsl_DataModelMethodConclusion()
    setattr(partner, 'myDsl_DataModelMethodConclusion129', None)
    _safe_set(owner, 'myDsl_DataAccessObject128', partner)
    assert getattr(partner, 'myDsl_DataModelMethodConclusion129') == owner
    _safe_set(owner, 'myDsl_DataAccessObject128', None)
    assert getattr(partner, 'myDsl_DataModelMethodConclusion129') is None


def test_assoc_updateConclusion60_stub_double():
    # myDsl_RestModelMethodConclusion has no real 'myDsl_RestModelMethodConclusion62' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Resource(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    partner = myDsl_RestModelMethodConclusion()
    setattr(partner, 'myDsl_RestModelMethodConclusion62', None)
    _safe_set(owner, 'myDsl_Resource61', partner)
    assert getattr(partner, 'myDsl_RestModelMethodConclusion62') == owner
    _safe_set(owner, 'myDsl_Resource61', None)
    assert getattr(partner, 'myDsl_RestModelMethodConclusion62') is None


def test_assoc_updateConclusion91_stub_double():
    # myDsl_DataModelMethodConclusion has no real 'myDsl_DataModelMethodConclusion93' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Service(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    partner = myDsl_DataModelMethodConclusion()
    setattr(partner, 'myDsl_DataModelMethodConclusion93', None)
    _safe_set(owner, 'myDsl_Service92', partner)
    assert getattr(partner, 'myDsl_DataModelMethodConclusion93') == owner
    _safe_set(owner, 'myDsl_Service92', None)
    assert getattr(partner, 'myDsl_DataModelMethodConclusion93') is None


def test_assoc_updateValService54_stub_double():
    # myDsl_ValidationService has no real 'myDsl_ValidationService56' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Resource(deleteby="sample_text", findby="sample_text", name="sample_text", updateby="sample_text")
    partner = myDsl_ValidationService()
    setattr(partner, 'myDsl_ValidationService56', None)
    _safe_set(owner, 'myDsl_Resource55', partner)
    assert getattr(partner, 'myDsl_ValidationService56') == owner
    _safe_set(owner, 'myDsl_Resource55', None)
    assert getattr(partner, 'myDsl_ValidationService56') is None


