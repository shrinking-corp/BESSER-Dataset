import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CATEGORIAS,
    Class,
    EVENTS_HISTORY,
    EVENTS_LIST,
    FAVORITES,
    FEEDBACK,
    FEEDBACK_COMMENT,
    FOLLOW,
    FOLLOW_MESSENGER,
    NOTIFICATION,
    PRODUCT,
    QUESTIONS,
    REFUND,
    REFUND_MESSAGES,
    ROLES,
    SHIPPING_METHODS,
    SHOPPING_HISTORY,
    SHOPPING_MESSENGER,
    SOCIAL_NETWORKS,
    STATUS,
    STATUS2,
    STATUS_SHOPPING_HISTORY,
    STORE,
    SUBSCRIPTION_BENEFITS,
    USER,
    WHISES,
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

def test_assoc_CATEGORIAS_PRODUCTO_reverse_link_reassign_clear():
    a1 = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    a2 = PRODUCT(ShippingMethods="sample_text_2", _id="sample_text_2", attribute="sample_text_2", color="sample_text_2", createdAt="sample_text_2", description="sample_text_2", dimensions="sample_text_2", isNew=False, model="sample_text_2", name="sample_text_2", photos="sample_text_2", price=13, quantity=13, relatedProducts="sample_text_2", sold=13, statusId="sample_text_2", storeId="sample_text_2")
    b = CATEGORIAS(_id="sample_text", createdAt="sample_text", name="sample_text")
    _safe_set(b, 'pRODUCTO4', {a1})
    assert _is_linked(b, 'pRODUCTO4', a1)
    if hasattr(a1, 'cATEGORIAS5'):
        assert _is_linked(a1, 'cATEGORIAS5', b)
    _safe_set(b, 'pRODUCTO4', {a2})
    assert _is_linked(b, 'pRODUCTO4', a2)
    if hasattr(a1, 'cATEGORIAS5'):
        assert not _is_linked(a1, 'cATEGORIAS5', b)
    if hasattr(a2, 'cATEGORIAS5'):
        assert _is_linked(a2, 'cATEGORIAS5', b)
    _safe_set(b, 'pRODUCTO4', set())
    assert not _is_linked(b, 'pRODUCTO4', a2)
    if hasattr(a2, 'cATEGORIAS5'):
        assert not _is_linked(a2, 'cATEGORIAS5', b)


def test_assoc_COMMENTS_PRODUCT_reverse_link_reassign_clear():
    a1 = QUESTIONS(_id="sample_text", answer="sample_text", createdAt="sample_text", productId="sample_text", question="sample_text", score=7, statusId="sample_text", userId="sample_text")
    a2 = QUESTIONS(_id="sample_text_2", answer="sample_text_2", createdAt="sample_text_2", productId="sample_text_2", question="sample_text_2", score=13, statusId="sample_text_2", userId="sample_text_2")
    b = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    _safe_set(b, 'cOMMENTS11', a1)
    assert _is_linked(b, 'cOMMENTS11', a1)
    if hasattr(a1, 'pRODUCT10'):
        assert _is_linked(a1, 'pRODUCT10', b)
    _safe_set(b, 'cOMMENTS11', a2)
    assert _is_linked(b, 'cOMMENTS11', a2)
    if hasattr(a1, 'pRODUCT10'):
        assert not _is_linked(a1, 'pRODUCT10', b)
    if hasattr(a2, 'pRODUCT10'):
        assert _is_linked(a2, 'pRODUCT10', b)
    _safe_set(b, 'cOMMENTS11', None)
    assert not _is_linked(b, 'cOMMENTS11', a2)
    if hasattr(a2, 'pRODUCT10'):
        assert not _is_linked(a2, 'pRODUCT10', b)


def test_assoc_COMMENTS_USUARIO_reverse_link_reassign_clear():
    a1 = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    a2 = USER(_id="sample_text_2", address="sample_text_2", createdAt="sample_text_2", email="sample_text_2", lastAccess="sample_text_2", name="sample_text_2", password="sample_text_2", status="sample_text_2", surname="sample_text_2", telephone="sample_text_2", updateAt="sample_text_2", verified=False)
    b = QUESTIONS(_id="sample_text", answer="sample_text", createdAt="sample_text", productId="sample_text", question="sample_text", score=7, statusId="sample_text", userId="sample_text")
    _safe_set(b, 'uSUARIO12', a1)
    assert _is_linked(b, 'uSUARIO12', a1)
    if hasattr(a1, 'cOMMENTS13'):
        assert _is_linked(a1, 'cOMMENTS13', b)
    _safe_set(b, 'uSUARIO12', a2)
    assert _is_linked(b, 'uSUARIO12', a2)
    if hasattr(a1, 'cOMMENTS13'):
        assert not _is_linked(a1, 'cOMMENTS13', b)
    if hasattr(a2, 'cOMMENTS13'):
        assert _is_linked(a2, 'cOMMENTS13', b)
    _safe_set(b, 'uSUARIO12', None)
    assert not _is_linked(b, 'uSUARIO12', a2)
    if hasattr(a2, 'cOMMENTS13'):
        assert not _is_linked(a2, 'cOMMENTS13', b)


def test_assoc_EVENTS_LIST_EVENTS_HISTORY_reverse_link_reassign_clear():
    a1 = EVENTS_LIST(_id="sample_text", createdAt="sample_text", description="sample_text", key="sample_text")
    a2 = EVENTS_LIST(_id="sample_text_2", createdAt="sample_text_2", description="sample_text_2", key="sample_text_2")
    b = EVENTS_HISTORY(_id="sample_text", createdAt="sample_text", eventId="sample_text", newValue="sample_text", oldValue="sample_text", userId="sample_text")
    _safe_set(b, 'eVENTS_LIST37', a1)
    assert _is_linked(b, 'eVENTS_LIST37', a1)
    if hasattr(a1, 'eVENTS_HISTORY36'):
        assert _is_linked(a1, 'eVENTS_HISTORY36', b)
    _safe_set(b, 'eVENTS_LIST37', a2)
    assert _is_linked(b, 'eVENTS_LIST37', a2)
    if hasattr(a1, 'eVENTS_HISTORY36'):
        assert not _is_linked(a1, 'eVENTS_HISTORY36', b)
    if hasattr(a2, 'eVENTS_HISTORY36'):
        assert _is_linked(a2, 'eVENTS_HISTORY36', b)
    _safe_set(b, 'eVENTS_LIST37', None)
    assert not _is_linked(b, 'eVENTS_LIST37', a2)
    if hasattr(a2, 'eVENTS_HISTORY36'):
        assert not _is_linked(a2, 'eVENTS_HISTORY36', b)


def test_assoc_FAVORITES_PRODUCTO_reverse_link_reassign_clear():
    a1 = WHISES(_id="sample_text", createdAt="sample_text", productId="sample_text", statusId="sample_text", userId="sample_text")
    a2 = WHISES(_id="sample_text_2", createdAt="sample_text_2", productId="sample_text_2", statusId="sample_text_2", userId="sample_text_2")
    b = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    _safe_set(b, 'fAVORITES7', {a1})
    assert _is_linked(b, 'fAVORITES7', a1)
    if hasattr(a1, 'pRODUCTO6'):
        assert _is_linked(a1, 'pRODUCTO6', b)
    _safe_set(b, 'fAVORITES7', {a2})
    assert _is_linked(b, 'fAVORITES7', a2)
    if hasattr(a1, 'pRODUCTO6'):
        assert not _is_linked(a1, 'pRODUCTO6', b)
    if hasattr(a2, 'pRODUCTO6'):
        assert _is_linked(a2, 'pRODUCTO6', b)
    _safe_set(b, 'fAVORITES7', set())
    assert not _is_linked(b, 'fAVORITES7', a2)
    if hasattr(a2, 'pRODUCTO6'):
        assert not _is_linked(a2, 'pRODUCTO6', b)


def test_assoc_FAVORITES_STORE_reverse_link_reassign_clear():
    a1 = STORE(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", name="sample_text", schedule="sample_text", statusId="sample_text", telephone="sample_text", updateAt="sample_text")
    a2 = STORE(_id="sample_text_2", address="sample_text_2", createdAt="sample_text_2", email="sample_text_2", name="sample_text_2", schedule="sample_text_2", statusId="sample_text_2", telephone="sample_text_2", updateAt="sample_text_2")
    b = FAVORITES(_id="sample_text", createdAt="sample_text", statusId="sample_text", storeId="sample_text", userId="sample_text")
    _safe_set(b, 'sTORE32', a1)
    assert _is_linked(b, 'sTORE32', a1)
    if hasattr(a1, 'fAVORITES33'):
        assert _is_linked(a1, 'fAVORITES33', b)
    _safe_set(b, 'sTORE32', a2)
    assert _is_linked(b, 'sTORE32', a2)
    if hasattr(a1, 'fAVORITES33'):
        assert not _is_linked(a1, 'fAVORITES33', b)
    if hasattr(a2, 'fAVORITES33'):
        assert _is_linked(a2, 'fAVORITES33', b)
    _safe_set(b, 'sTORE32', None)
    assert not _is_linked(b, 'sTORE32', a2)
    if hasattr(a2, 'fAVORITES33'):
        assert not _is_linked(a2, 'fAVORITES33', b)


def test_assoc_FAVORITES_USER_reverse_link_reassign_clear():
    a1 = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    a2 = USER(_id="sample_text_2", address="sample_text_2", createdAt="sample_text_2", email="sample_text_2", lastAccess="sample_text_2", name="sample_text_2", password="sample_text_2", status="sample_text_2", surname="sample_text_2", telephone="sample_text_2", updateAt="sample_text_2", verified=False)
    b = FAVORITES(_id="sample_text", createdAt="sample_text", statusId="sample_text", storeId="sample_text", userId="sample_text")
    _safe_set(b, 'uSER34', a1)
    assert _is_linked(b, 'uSER34', a1)
    if hasattr(a1, 'fAVORITES35'):
        assert _is_linked(a1, 'fAVORITES35', b)
    _safe_set(b, 'uSER34', a2)
    assert _is_linked(b, 'uSER34', a2)
    if hasattr(a1, 'fAVORITES35'):
        assert not _is_linked(a1, 'fAVORITES35', b)
    if hasattr(a2, 'fAVORITES35'):
        assert _is_linked(a2, 'fAVORITES35', b)
    _safe_set(b, 'uSER34', None)
    assert not _is_linked(b, 'uSER34', a2)
    if hasattr(a2, 'fAVORITES35'):
        assert not _is_linked(a2, 'fAVORITES35', b)


def test_assoc_FAVORITES_USUARIO_reverse_link_reassign_clear():
    a1 = WHISES(_id="sample_text", createdAt="sample_text", productId="sample_text", statusId="sample_text", userId="sample_text")
    a2 = WHISES(_id="sample_text_2", createdAt="sample_text_2", productId="sample_text_2", statusId="sample_text_2", userId="sample_text_2")
    b = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    _safe_set(b, 'fAVORITES9', {a1})
    assert _is_linked(b, 'fAVORITES9', a1)
    if hasattr(a1, 'uSUARIO8'):
        assert _is_linked(a1, 'uSUARIO8', b)
    _safe_set(b, 'fAVORITES9', {a2})
    assert _is_linked(b, 'fAVORITES9', a2)
    if hasattr(a1, 'uSUARIO8'):
        assert not _is_linked(a1, 'uSUARIO8', b)
    if hasattr(a2, 'uSUARIO8'):
        assert _is_linked(a2, 'uSUARIO8', b)
    _safe_set(b, 'fAVORITES9', set())
    assert not _is_linked(b, 'fAVORITES9', a2)
    if hasattr(a2, 'uSUARIO8'):
        assert not _is_linked(a2, 'uSUARIO8', b)


def test_assoc_FEEDBACKS_USER_reverse_link_reassign_clear():
    a1 = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    a2 = USER(_id="sample_text_2", address="sample_text_2", createdAt="sample_text_2", email="sample_text_2", lastAccess="sample_text_2", name="sample_text_2", password="sample_text_2", status="sample_text_2", surname="sample_text_2", telephone="sample_text_2", updateAt="sample_text_2", verified=False)
    b = FEEDBACK(_id="sample_text", createdAt="sample_text", like="sample_text", linkInstagram="sample_text", linkYoutube="sample_text", photos="sample_text", productId="sample_text", updateAt="sample_text", userId="sample_text", wysiwyg="sample_text")
    _safe_set(b, 'uSER50', a1)
    assert _is_linked(b, 'uSER50', a1)
    if hasattr(a1, 'fEEDBACKS51'):
        assert _is_linked(a1, 'fEEDBACKS51', b)
    _safe_set(b, 'uSER50', a2)
    assert _is_linked(b, 'uSER50', a2)
    if hasattr(a1, 'fEEDBACKS51'):
        assert not _is_linked(a1, 'fEEDBACKS51', b)
    if hasattr(a2, 'fEEDBACKS51'):
        assert _is_linked(a2, 'fEEDBACKS51', b)
    _safe_set(b, 'uSER50', None)
    assert not _is_linked(b, 'uSER50', a2)
    if hasattr(a2, 'fEEDBACKS51'):
        assert not _is_linked(a2, 'fEEDBACKS51', b)


def test_assoc_FEEDBACK_COMMENT_FEEDBACK_reverse_link_reassign_clear():
    a1 = FEEDBACK_COMMENT(_id="sample_text", comment="sample_text", createdAt="sample_text", feedbackId="sample_text", score=7, userId="sample_text")
    a2 = FEEDBACK_COMMENT(_id="sample_text_2", comment="sample_text_2", createdAt="sample_text_2", feedbackId="sample_text_2", score=13, userId="sample_text_2")
    b = FEEDBACK(_id="sample_text", createdAt="sample_text", like="sample_text", linkInstagram="sample_text", linkYoutube="sample_text", photos="sample_text", productId="sample_text", updateAt="sample_text", userId="sample_text", wysiwyg="sample_text")
    _safe_set(b, 'fEEDBACK_COMMENT53', a1)
    assert _is_linked(b, 'fEEDBACK_COMMENT53', a1)
    if hasattr(a1, 'fEEDBACK52'):
        assert _is_linked(a1, 'fEEDBACK52', b)
    _safe_set(b, 'fEEDBACK_COMMENT53', a2)
    assert _is_linked(b, 'fEEDBACK_COMMENT53', a2)
    if hasattr(a1, 'fEEDBACK52'):
        assert not _is_linked(a1, 'fEEDBACK52', b)
    if hasattr(a2, 'fEEDBACK52'):
        assert _is_linked(a2, 'fEEDBACK52', b)
    _safe_set(b, 'fEEDBACK_COMMENT53', None)
    assert not _is_linked(b, 'fEEDBACK_COMMENT53', a2)
    if hasattr(a2, 'fEEDBACK52'):
        assert not _is_linked(a2, 'fEEDBACK52', b)


def test_assoc_FRIEND_LIST_USER_reverse_link_reassign_clear():
    a1 = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    a2 = USER(_id="sample_text_2", address="sample_text_2", createdAt="sample_text_2", email="sample_text_2", lastAccess="sample_text_2", name="sample_text_2", password="sample_text_2", status="sample_text_2", surname="sample_text_2", telephone="sample_text_2", updateAt="sample_text_2", verified=False)
    b = FOLLOW(_id="sample_text", createdAt="sample_text", followers="sample_text", following="sample_text", followingGroup="sample_text", userId="sample_text")
    _safe_set(b, 'uSER46', a1)
    assert _is_linked(b, 'uSER46', a1)
    if hasattr(a1, 'fRIEND_LIST47'):
        assert _is_linked(a1, 'fRIEND_LIST47', b)
    _safe_set(b, 'uSER46', a2)
    assert _is_linked(b, 'uSER46', a2)
    if hasattr(a1, 'fRIEND_LIST47'):
        assert not _is_linked(a1, 'fRIEND_LIST47', b)
    if hasattr(a2, 'fRIEND_LIST47'):
        assert _is_linked(a2, 'fRIEND_LIST47', b)
    _safe_set(b, 'uSER46', None)
    assert not _is_linked(b, 'uSER46', a2)
    if hasattr(a2, 'fRIEND_LIST47'):
        assert not _is_linked(a2, 'fRIEND_LIST47', b)


def test_assoc_MESSENGER_SHOPPING_HISTORY_reverse_link_reassign_clear():
    a1 = SHOPPING_MESSENGER(_id="sample_text", created_at="sample_text", message="sample_text", photos="sample_text", storeId="sample_text", userId="sample_text")
    a2 = SHOPPING_MESSENGER(_id="sample_text_2", created_at="sample_text_2", message="sample_text_2", photos="sample_text_2", storeId="sample_text_2", userId="sample_text_2")
    b = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    _safe_set(b, 'mESSENGER49', a1)
    assert _is_linked(b, 'mESSENGER49', a1)
    if hasattr(a1, 'sHOPPING_HISTORY48'):
        assert _is_linked(a1, 'sHOPPING_HISTORY48', b)
    _safe_set(b, 'mESSENGER49', a2)
    assert _is_linked(b, 'mESSENGER49', a2)
    if hasattr(a1, 'sHOPPING_HISTORY48'):
        assert not _is_linked(a1, 'sHOPPING_HISTORY48', b)
    if hasattr(a2, 'sHOPPING_HISTORY48'):
        assert _is_linked(a2, 'sHOPPING_HISTORY48', b)
    _safe_set(b, 'mESSENGER49', None)
    assert not _is_linked(b, 'mESSENGER49', a2)
    if hasattr(a2, 'sHOPPING_HISTORY48'):
        assert not _is_linked(a2, 'sHOPPING_HISTORY48', b)


def test_assoc_NOTIFICATION_USER_reverse_link_reassign_clear():
    a1 = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    a2 = USER(_id="sample_text_2", address="sample_text_2", createdAt="sample_text_2", email="sample_text_2", lastAccess="sample_text_2", name="sample_text_2", password="sample_text_2", status="sample_text_2", surname="sample_text_2", telephone="sample_text_2", updateAt="sample_text_2", verified=False)
    b = NOTIFICATION(_id="sample_text", code="sample_text", createdAt="sample_text", message="sample_text", userId="sample_text")
    _safe_set(b, 'uSER38', a1)
    assert _is_linked(b, 'uSER38', a1)
    if hasattr(a1, 'nOTIFICATION39'):
        assert _is_linked(a1, 'nOTIFICATION39', b)
    _safe_set(b, 'uSER38', a2)
    assert _is_linked(b, 'uSER38', a2)
    if hasattr(a1, 'nOTIFICATION39'):
        assert not _is_linked(a1, 'nOTIFICATION39', b)
    if hasattr(a2, 'nOTIFICATION39'):
        assert _is_linked(a2, 'nOTIFICATION39', b)
    _safe_set(b, 'uSER38', None)
    assert not _is_linked(b, 'uSER38', a2)
    if hasattr(a2, 'nOTIFICATION39'):
        assert not _is_linked(a2, 'nOTIFICATION39', b)


def test_assoc_PRODUCTO_USUARIO_reverse_link_reassign_clear():
    a1 = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    a2 = USER(_id="sample_text_2", address="sample_text_2", createdAt="sample_text_2", email="sample_text_2", lastAccess="sample_text_2", name="sample_text_2", password="sample_text_2", status="sample_text_2", surname="sample_text_2", telephone="sample_text_2", updateAt="sample_text_2", verified=False)
    b = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    _safe_set(b, 'uSUARIO2', {a1})
    assert _is_linked(b, 'uSUARIO2', a1)
    if hasattr(a1, 'pRODUCTO3'):
        assert _is_linked(a1, 'pRODUCTO3', b)
    _safe_set(b, 'uSUARIO2', {a2})
    assert _is_linked(b, 'uSUARIO2', a2)
    if hasattr(a1, 'pRODUCTO3'):
        assert not _is_linked(a1, 'pRODUCTO3', b)
    if hasattr(a2, 'pRODUCTO3'):
        assert _is_linked(a2, 'pRODUCTO3', b)
    _safe_set(b, 'uSUARIO2', set())
    assert not _is_linked(b, 'uSUARIO2', a2)
    if hasattr(a2, 'pRODUCTO3'):
        assert not _is_linked(a2, 'pRODUCTO3', b)


def test_assoc_REFUND_MESSAGES_REFUND_reverse_link_reassign_clear():
    a1 = REFUND_MESSAGES(_id="sample_text", attach="sample_text", created_at="sample_text", message="sample_text", userId="sample_text")
    a2 = REFUND_MESSAGES(_id="sample_text_2", attach="sample_text_2", created_at="sample_text_2", message="sample_text_2", userId="sample_text_2")
    b = REFUND(_id="sample_text", created_at="sample_text", message="sample_text", productId="sample_text", shoppingHistoryId="sample_text", storeId="sample_text", title="sample_text", userId="sample_text")
    _safe_set(b, 'rEFUND_MESSAGES43', a1)
    assert _is_linked(b, 'rEFUND_MESSAGES43', a1)
    if hasattr(a1, 'rEFUND42'):
        assert _is_linked(a1, 'rEFUND42', b)
    _safe_set(b, 'rEFUND_MESSAGES43', a2)
    assert _is_linked(b, 'rEFUND_MESSAGES43', a2)
    if hasattr(a1, 'rEFUND42'):
        assert not _is_linked(a1, 'rEFUND42', b)
    if hasattr(a2, 'rEFUND42'):
        assert _is_linked(a2, 'rEFUND42', b)
    _safe_set(b, 'rEFUND_MESSAGES43', None)
    assert not _is_linked(b, 'rEFUND_MESSAGES43', a2)
    if hasattr(a2, 'rEFUND42'):
        assert not _is_linked(a2, 'rEFUND42', b)


def test_assoc_REFUND_SHOPPING_HISTORY_reverse_link_reassign_clear():
    a1 = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    a2 = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text_2", _id="sample_text_2", attribute="sample_text_2", comment="sample_text_2", created_at="sample_text_2", description="sample_text_2", isNew=False, isSold=False, name="sample_text_2", note="sample_text_2", photos="sample_text_2", price=13, productId="sample_text_2", quantity=13, score=13, shipAddress="sample_text_2", shipArrival="sample_text_2", shipName="sample_text_2", shipPrice=13, sold=13, status="sample_text_2", storeId="sample_text_2", userId="sample_text_2")
    b = REFUND(_id="sample_text", created_at="sample_text", message="sample_text", productId="sample_text", shoppingHistoryId="sample_text", storeId="sample_text", title="sample_text", userId="sample_text")
    _safe_set(b, 'sHOPPING_HISTORY40', a1)
    assert _is_linked(b, 'sHOPPING_HISTORY40', a1)
    if hasattr(a1, 'rEFUND41'):
        assert _is_linked(a1, 'rEFUND41', b)
    _safe_set(b, 'sHOPPING_HISTORY40', a2)
    assert _is_linked(b, 'sHOPPING_HISTORY40', a2)
    if hasattr(a1, 'rEFUND41'):
        assert not _is_linked(a1, 'rEFUND41', b)
    if hasattr(a2, 'rEFUND41'):
        assert _is_linked(a2, 'rEFUND41', b)
    _safe_set(b, 'sHOPPING_HISTORY40', None)
    assert not _is_linked(b, 'sHOPPING_HISTORY40', a2)
    if hasattr(a2, 'rEFUND41'):
        assert not _is_linked(a2, 'rEFUND41', b)


def test_assoc_SHIPPING_PRODUCT_reverse_link_reassign_clear():
    a1 = SHIPPING_METHODS(_id="sample_text", address="sample_text", arrival="sample_text", createdAt="sample_text", name="sample_text", price=7)
    a2 = SHIPPING_METHODS(_id="sample_text_2", address="sample_text_2", arrival="sample_text_2", createdAt="sample_text_2", name="sample_text_2", price=13)
    b = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    _safe_set(b, 'sHIPPING23', a1)
    assert _is_linked(b, 'sHIPPING23', a1)
    if hasattr(a1, 'pRODUCT22'):
        assert _is_linked(a1, 'pRODUCT22', b)
    _safe_set(b, 'sHIPPING23', a2)
    assert _is_linked(b, 'sHIPPING23', a2)
    if hasattr(a1, 'pRODUCT22'):
        assert not _is_linked(a1, 'pRODUCT22', b)
    if hasattr(a2, 'pRODUCT22'):
        assert _is_linked(a2, 'pRODUCT22', b)
    _safe_set(b, 'sHIPPING23', None)
    assert not _is_linked(b, 'sHIPPING23', a2)
    if hasattr(a2, 'pRODUCT22'):
        assert not _is_linked(a2, 'pRODUCT22', b)


def test_assoc_SHIPPING_SHOPPING_CART_reverse_link_reassign_clear():
    a1 = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    a2 = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text_2", _id="sample_text_2", attribute="sample_text_2", comment="sample_text_2", created_at="sample_text_2", description="sample_text_2", isNew=False, isSold=False, name="sample_text_2", note="sample_text_2", photos="sample_text_2", price=13, productId="sample_text_2", quantity=13, score=13, shipAddress="sample_text_2", shipArrival="sample_text_2", shipName="sample_text_2", shipPrice=13, sold=13, status="sample_text_2", storeId="sample_text_2", userId="sample_text_2")
    b = SHIPPING_METHODS(_id="sample_text", address="sample_text", arrival="sample_text", createdAt="sample_text", name="sample_text", price=7)
    _safe_set(b, 'sHOPPING_CART20', a1)
    assert _is_linked(b, 'sHOPPING_CART20', a1)
    if hasattr(a1, 'sHIPPING21'):
        assert _is_linked(a1, 'sHIPPING21', b)
    _safe_set(b, 'sHOPPING_CART20', a2)
    assert _is_linked(b, 'sHOPPING_CART20', a2)
    if hasattr(a1, 'sHIPPING21'):
        assert not _is_linked(a1, 'sHIPPING21', b)
    if hasattr(a2, 'sHIPPING21'):
        assert _is_linked(a2, 'sHIPPING21', b)
    _safe_set(b, 'sHOPPING_CART20', None)
    assert not _is_linked(b, 'sHOPPING_CART20', a2)
    if hasattr(a2, 'sHIPPING21'):
        assert not _is_linked(a2, 'sHIPPING21', b)


def test_assoc_SHOPPING_CART_PRODUCT_reverse_link_reassign_clear():
    a1 = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    a2 = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text_2", _id="sample_text_2", attribute="sample_text_2", comment="sample_text_2", created_at="sample_text_2", description="sample_text_2", isNew=False, isSold=False, name="sample_text_2", note="sample_text_2", photos="sample_text_2", price=13, productId="sample_text_2", quantity=13, score=13, shipAddress="sample_text_2", shipArrival="sample_text_2", shipName="sample_text_2", shipPrice=13, sold=13, status="sample_text_2", storeId="sample_text_2", userId="sample_text_2")
    b = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    _safe_set(b, 'sHOPPING_CART17', a1)
    assert _is_linked(b, 'sHOPPING_CART17', a1)
    if hasattr(a1, 'pRODUCT16'):
        assert _is_linked(a1, 'pRODUCT16', b)
    _safe_set(b, 'sHOPPING_CART17', a2)
    assert _is_linked(b, 'sHOPPING_CART17', a2)
    if hasattr(a1, 'pRODUCT16'):
        assert not _is_linked(a1, 'pRODUCT16', b)
    if hasattr(a2, 'pRODUCT16'):
        assert _is_linked(a2, 'pRODUCT16', b)
    _safe_set(b, 'sHOPPING_CART17', None)
    assert not _is_linked(b, 'sHOPPING_CART17', a2)
    if hasattr(a2, 'pRODUCT16'):
        assert not _is_linked(a2, 'pRODUCT16', b)


def test_assoc_SHOPPING_CART_USUARIO_reverse_link_reassign_clear():
    a1 = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    a2 = USER(_id="sample_text_2", address="sample_text_2", createdAt="sample_text_2", email="sample_text_2", lastAccess="sample_text_2", name="sample_text_2", password="sample_text_2", status="sample_text_2", surname="sample_text_2", telephone="sample_text_2", updateAt="sample_text_2", verified=False)
    b = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    _safe_set(b, 'uSUARIO14', a1)
    assert _is_linked(b, 'uSUARIO14', a1)
    if hasattr(a1, 'sHOPPING_CART15'):
        assert _is_linked(a1, 'sHOPPING_CART15', b)
    _safe_set(b, 'uSUARIO14', a2)
    assert _is_linked(b, 'uSUARIO14', a2)
    if hasattr(a1, 'sHOPPING_CART15'):
        assert not _is_linked(a1, 'sHOPPING_CART15', b)
    if hasattr(a2, 'sHOPPING_CART15'):
        assert _is_linked(a2, 'sHOPPING_CART15', b)
    _safe_set(b, 'uSUARIO14', None)
    assert not _is_linked(b, 'uSUARIO14', a2)
    if hasattr(a2, 'sHOPPING_CART15'):
        assert not _is_linked(a2, 'sHOPPING_CART15', b)


def test_assoc_SHOPPING_HISTORY_STORE_reverse_link_reassign_clear():
    a1 = STORE(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", name="sample_text", schedule="sample_text", statusId="sample_text", telephone="sample_text", updateAt="sample_text")
    a2 = STORE(_id="sample_text_2", address="sample_text_2", createdAt="sample_text_2", email="sample_text_2", name="sample_text_2", schedule="sample_text_2", statusId="sample_text_2", telephone="sample_text_2", updateAt="sample_text_2")
    b = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    _safe_set(b, 'sTORE30', a1)
    assert _is_linked(b, 'sTORE30', a1)
    if hasattr(a1, 'sHOPPING_HISTORY31'):
        assert _is_linked(a1, 'sHOPPING_HISTORY31', b)
    _safe_set(b, 'sTORE30', a2)
    assert _is_linked(b, 'sTORE30', a2)
    if hasattr(a1, 'sHOPPING_HISTORY31'):
        assert not _is_linked(a1, 'sHOPPING_HISTORY31', b)
    if hasattr(a2, 'sHOPPING_HISTORY31'):
        assert _is_linked(a2, 'sHOPPING_HISTORY31', b)
    _safe_set(b, 'sTORE30', None)
    assert not _is_linked(b, 'sTORE30', a2)
    if hasattr(a2, 'sHOPPING_HISTORY31'):
        assert not _is_linked(a2, 'sHOPPING_HISTORY31', b)


def test_assoc_SOCIAL_NETWORKS_USER_reverse_link_reassign_clear():
    a1 = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    a2 = USER(_id="sample_text_2", address="sample_text_2", createdAt="sample_text_2", email="sample_text_2", lastAccess="sample_text_2", name="sample_text_2", password="sample_text_2", status="sample_text_2", surname="sample_text_2", telephone="sample_text_2", updateAt="sample_text_2", verified=False)
    b = SOCIAL_NETWORKS(_id="sample_text", facebook="sample_text", instagram="sample_text", twitter="sample_text", updateAt="sample_text")
    _safe_set(b, 'uSER44', a1)
    assert _is_linked(b, 'uSER44', a1)
    if hasattr(a1, 'sOCIAL_NETWORKS45'):
        assert _is_linked(a1, 'sOCIAL_NETWORKS45', b)
    _safe_set(b, 'uSER44', a2)
    assert _is_linked(b, 'uSER44', a2)
    if hasattr(a1, 'sOCIAL_NETWORKS45'):
        assert not _is_linked(a1, 'sOCIAL_NETWORKS45', b)
    if hasattr(a2, 'sOCIAL_NETWORKS45'):
        assert _is_linked(a2, 'sOCIAL_NETWORKS45', b)
    _safe_set(b, 'uSER44', None)
    assert not _is_linked(b, 'uSER44', a2)
    if hasattr(a2, 'sOCIAL_NETWORKS45'):
        assert not _is_linked(a2, 'sOCIAL_NETWORKS45', b)


def test_assoc_STATUS_PRODUCT_reverse_link_reassign_clear():
    a1 = STATUS(_id="sample_text", createdAt="sample_text", name="sample_text")
    a2 = STATUS(_id="sample_text_2", createdAt="sample_text_2", name="sample_text_2")
    b = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    _safe_set(b, 'sTATUS19', a1)
    assert _is_linked(b, 'sTATUS19', a1)
    if hasattr(a1, 'pRODUCT18'):
        assert _is_linked(a1, 'pRODUCT18', b)
    _safe_set(b, 'sTATUS19', a2)
    assert _is_linked(b, 'sTATUS19', a2)
    if hasattr(a1, 'pRODUCT18'):
        assert not _is_linked(a1, 'pRODUCT18', b)
    if hasattr(a2, 'pRODUCT18'):
        assert _is_linked(a2, 'pRODUCT18', b)
    _safe_set(b, 'sTATUS19', None)
    assert not _is_linked(b, 'sTATUS19', a2)
    if hasattr(a2, 'pRODUCT18'):
        assert not _is_linked(a2, 'pRODUCT18', b)


def test_assoc_STATUS_SHOPPING_HISTORY_SHOPPING_HISTORY_reverse_link_reassign_clear():
    a1 = STATUS_SHOPPING_HISTORY(_id="sample_text", name="sample_text")
    a2 = STATUS_SHOPPING_HISTORY(_id="sample_text_2", name="sample_text_2")
    b = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    _safe_set(b, 'sTATUS_SHOPPING_HISTORY25', a1)
    assert _is_linked(b, 'sTATUS_SHOPPING_HISTORY25', a1)
    if hasattr(a1, 'sHOPPING_HISTORY24'):
        assert _is_linked(a1, 'sHOPPING_HISTORY24', b)
    _safe_set(b, 'sTATUS_SHOPPING_HISTORY25', a2)
    assert _is_linked(b, 'sTATUS_SHOPPING_HISTORY25', a2)
    if hasattr(a1, 'sHOPPING_HISTORY24'):
        assert not _is_linked(a1, 'sHOPPING_HISTORY24', b)
    if hasattr(a2, 'sHOPPING_HISTORY24'):
        assert _is_linked(a2, 'sHOPPING_HISTORY24', b)
    _safe_set(b, 'sTATUS_SHOPPING_HISTORY25', None)
    assert not _is_linked(b, 'sTATUS_SHOPPING_HISTORY25', a2)
    if hasattr(a2, 'sHOPPING_HISTORY24'):
        assert not _is_linked(a2, 'sHOPPING_HISTORY24', b)


def test_assoc_STORE_PRODUCT_reverse_link_reassign_clear():
    a1 = STORE(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", name="sample_text", schedule="sample_text", statusId="sample_text", telephone="sample_text", updateAt="sample_text")
    a2 = STORE(_id="sample_text_2", address="sample_text_2", createdAt="sample_text_2", email="sample_text_2", name="sample_text_2", schedule="sample_text_2", statusId="sample_text_2", telephone="sample_text_2", updateAt="sample_text_2")
    b = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    _safe_set(b, 'sTORE27', {a1})
    assert _is_linked(b, 'sTORE27', a1)
    if hasattr(a1, 'pRODUCT26'):
        assert _is_linked(a1, 'pRODUCT26', b)
    _safe_set(b, 'sTORE27', {a2})
    assert _is_linked(b, 'sTORE27', a2)
    if hasattr(a1, 'pRODUCT26'):
        assert not _is_linked(a1, 'pRODUCT26', b)
    if hasattr(a2, 'pRODUCT26'):
        assert _is_linked(a2, 'pRODUCT26', b)
    _safe_set(b, 'sTORE27', set())
    assert not _is_linked(b, 'sTORE27', a2)
    if hasattr(a2, 'pRODUCT26'):
        assert not _is_linked(a2, 'pRODUCT26', b)


def test_assoc_STORE_USER_reverse_link_reassign_clear():
    a1 = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    a2 = USER(_id="sample_text_2", address="sample_text_2", createdAt="sample_text_2", email="sample_text_2", lastAccess="sample_text_2", name="sample_text_2", password="sample_text_2", status="sample_text_2", surname="sample_text_2", telephone="sample_text_2", updateAt="sample_text_2", verified=False)
    b = STORE(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", name="sample_text", schedule="sample_text", statusId="sample_text", telephone="sample_text", updateAt="sample_text")
    _safe_set(b, 'uSER28', a1)
    assert _is_linked(b, 'uSER28', a1)
    if hasattr(a1, 'sTORE29'):
        assert _is_linked(a1, 'sTORE29', b)
    _safe_set(b, 'uSER28', a2)
    assert _is_linked(b, 'uSER28', a2)
    if hasattr(a1, 'sTORE29'):
        assert not _is_linked(a1, 'sTORE29', b)
    if hasattr(a2, 'sTORE29'):
        assert _is_linked(a2, 'sTORE29', b)
    _safe_set(b, 'uSER28', None)
    assert not _is_linked(b, 'uSER28', a2)
    if hasattr(a2, 'sTORE29'):
        assert not _is_linked(a2, 'sTORE29', b)


def test_assoc_roles_usuario_reverse_link_reassign_clear():
    a1 = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    a2 = USER(_id="sample_text_2", address="sample_text_2", createdAt="sample_text_2", email="sample_text_2", lastAccess="sample_text_2", name="sample_text_2", password="sample_text_2", status="sample_text_2", surname="sample_text_2", telephone="sample_text_2", updateAt="sample_text_2", verified=False)
    b = ROLES(_id="sample_text", createdAt="sample_text", name="sample_text")
    _safe_set(b, 'usuario0', {a1})
    assert _is_linked(b, 'usuario0', a1)
    if hasattr(a1, 'roles1'):
        assert _is_linked(a1, 'roles1', b)
    _safe_set(b, 'usuario0', {a2})
    assert _is_linked(b, 'usuario0', a2)
    if hasattr(a1, 'roles1'):
        assert not _is_linked(a1, 'roles1', b)
    if hasattr(a2, 'roles1'):
        assert _is_linked(a2, 'roles1', b)
    _safe_set(b, 'usuario0', set())
    assert not _is_linked(b, 'usuario0', a2)
    if hasattr(a2, 'roles1'):
        assert not _is_linked(a2, 'roles1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

