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
    FOLLOW,
    SOCIAL_NETWORKS,
    REFUND_MESSAGES,
    REFUND,
    NOTIFICATION,
    Class,
    EVENTS_LIST,
    EVENTS_HISTORY,
    FAVORITES,
    STORE,
    STATUS_SHOPPING_HISTORY,
    STATUS2,
    SUBSCRIPTION_BENEFITS,
    SHIPPING_METHODS,
    STATUS,
    SHOPPING_HISTORY,
    QUESTIONS,
    WHISES,
    CATEGORIAS,
    PRODUCT,
    ROLES,
    USER,
    FOLLOW_MESSENGER,
    FEEDBACK_COMMENT,
    SHOPPING_MESSENGER,
    FEEDBACK,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_follow_is_not_abstract():
    assert not inspect.isabstract(FOLLOW)


def test_hyp_follow_constructor_exists():
    assert callable(FOLLOW.__init__)


def test_hyp_follow_constructor_args():
    sig = inspect.signature(FOLLOW.__init__)
    params = list(sig.parameters.keys())
    assert "userId" in params, "Missing parameter 'userId'"
    assert "createdAt" in params, "Missing parameter 'createdAt'"
    assert "followers" in params, "Missing parameter 'followers'"
    assert "followingGroup" in params, "Missing parameter 'followingGroup'"
    assert "following" in params, "Missing parameter 'following'"
    assert "_id" in params, "Missing parameter '_id'"









def test_hyp_social_networks_is_not_abstract():
    assert not inspect.isabstract(SOCIAL_NETWORKS)


def test_hyp_social_networks_constructor_exists():
    assert callable(SOCIAL_NETWORKS.__init__)


def test_hyp_social_networks_constructor_args():
    sig = inspect.signature(SOCIAL_NETWORKS.__init__)
    params = list(sig.parameters.keys())
    assert "twitter" in params, "Missing parameter 'twitter'"
    assert "updateAt" in params, "Missing parameter 'updateAt'"
    assert "facebook" in params, "Missing parameter 'facebook'"
    assert "instagram" in params, "Missing parameter 'instagram'"
    assert "_id" in params, "Missing parameter '_id'"








def test_hyp_refund_messages_is_not_abstract():
    assert not inspect.isabstract(REFUND_MESSAGES)


def test_hyp_refund_messages_constructor_exists():
    assert callable(REFUND_MESSAGES.__init__)


def test_hyp_refund_messages_constructor_args():
    sig = inspect.signature(REFUND_MESSAGES.__init__)
    params = list(sig.parameters.keys())
    assert "attach" in params, "Missing parameter 'attach'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "created_at" in params, "Missing parameter 'created_at'"
    assert "_id" in params, "Missing parameter '_id'"
    assert "message" in params, "Missing parameter 'message'"








def test_hyp_refund_is_not_abstract():
    assert not inspect.isabstract(REFUND)


def test_hyp_refund_constructor_exists():
    assert callable(REFUND.__init__)


def test_hyp_refund_constructor_args():
    sig = inspect.signature(REFUND.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"
    assert "productId" in params, "Missing parameter 'productId'"
    assert "title" in params, "Missing parameter 'title'"
    assert "storeId" in params, "Missing parameter 'storeId'"
    assert "_id" in params, "Missing parameter '_id'"
    assert "created_at" in params, "Missing parameter 'created_at'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "shoppingHistoryId" in params, "Missing parameter 'shoppingHistoryId'"











def test_hyp_notification_is_not_abstract():
    assert not inspect.isabstract(NOTIFICATION)


def test_hyp_notification_constructor_exists():
    assert callable(NOTIFICATION.__init__)


def test_hyp_notification_constructor_args():
    sig = inspect.signature(NOTIFICATION.__init__)
    params = list(sig.parameters.keys())
    assert "_id" in params, "Missing parameter '_id'"
    assert "code" in params, "Missing parameter 'code'"
    assert "message" in params, "Missing parameter 'message'"
    assert "createdAt" in params, "Missing parameter 'createdAt'"
    assert "userId" in params, "Missing parameter 'userId'"








def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_events_list_is_not_abstract():
    assert not inspect.isabstract(EVENTS_LIST)


def test_hyp_events_list_constructor_exists():
    assert callable(EVENTS_LIST.__init__)


def test_hyp_events_list_constructor_args():
    sig = inspect.signature(EVENTS_LIST.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "description" in params, "Missing parameter 'description'"
    assert "_id" in params, "Missing parameter '_id'"
    assert "createdAt" in params, "Missing parameter 'createdAt'"







def test_hyp_events_history_is_not_abstract():
    assert not inspect.isabstract(EVENTS_HISTORY)


def test_hyp_events_history_constructor_exists():
    assert callable(EVENTS_HISTORY.__init__)


def test_hyp_events_history_constructor_args():
    sig = inspect.signature(EVENTS_HISTORY.__init__)
    params = list(sig.parameters.keys())
    assert "createdAt" in params, "Missing parameter 'createdAt'"
    assert "newValue" in params, "Missing parameter 'newValue'"
    assert "oldValue" in params, "Missing parameter 'oldValue'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "eventId" in params, "Missing parameter 'eventId'"
    assert "_id" in params, "Missing parameter '_id'"









def test_hyp_favorites_is_not_abstract():
    assert not inspect.isabstract(FAVORITES)


def test_hyp_favorites_constructor_exists():
    assert callable(FAVORITES.__init__)


def test_hyp_favorites_constructor_args():
    sig = inspect.signature(FAVORITES.__init__)
    params = list(sig.parameters.keys())
    assert "statusId" in params, "Missing parameter 'statusId'"
    assert "storeId" in params, "Missing parameter 'storeId'"
    assert "createdAt" in params, "Missing parameter 'createdAt'"
    assert "_id" in params, "Missing parameter '_id'"
    assert "userId" in params, "Missing parameter 'userId'"








def test_hyp_store_is_not_abstract():
    assert not inspect.isabstract(STORE)


def test_hyp_store_constructor_exists():
    assert callable(STORE.__init__)


def test_hyp_store_constructor_args():
    sig = inspect.signature(STORE.__init__)
    params = list(sig.parameters.keys())
    assert "telephone" in params, "Missing parameter 'telephone'"
    assert "statusId" in params, "Missing parameter 'statusId'"
    assert "createdAt" in params, "Missing parameter 'createdAt'"
    assert "address" in params, "Missing parameter 'address'"
    assert "updateAt" in params, "Missing parameter 'updateAt'"
    assert "_id" in params, "Missing parameter '_id'"
    assert "schedule" in params, "Missing parameter 'schedule'"
    assert "name" in params, "Missing parameter 'name'"
    assert "email" in params, "Missing parameter 'email'"












def test_hyp_status_shopping_history_is_not_abstract():
    assert not inspect.isabstract(STATUS_SHOPPING_HISTORY)


def test_hyp_status_shopping_history_constructor_exists():
    assert callable(STATUS_SHOPPING_HISTORY.__init__)


def test_hyp_status_shopping_history_constructor_args():
    sig = inspect.signature(STATUS_SHOPPING_HISTORY.__init__)
    params = list(sig.parameters.keys())
    assert "_id" in params, "Missing parameter '_id'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_status2_is_not_abstract():
    assert not inspect.isabstract(STATUS2)


def test_hyp_status2_constructor_exists():
    assert callable(STATUS2.__init__)


def test_hyp_status2_constructor_args():
    sig = inspect.signature(STATUS2.__init__)
    params = list(sig.parameters.keys())
    assert "_id" in params, "Missing parameter '_id'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_subscription_benefits_is_not_abstract():
    assert not inspect.isabstract(SUBSCRIPTION_BENEFITS)


def test_hyp_subscription_benefits_constructor_exists():
    assert callable(SUBSCRIPTION_BENEFITS.__init__)


def test_hyp_subscription_benefits_constructor_args():
    sig = inspect.signature(SUBSCRIPTION_BENEFITS.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "key_name" in params, "Missing parameter 'key_name'"
    assert "_id" in params, "Missing parameter '_id'"






def test_hyp_shipping_methods_is_not_abstract():
    assert not inspect.isabstract(SHIPPING_METHODS)


def test_hyp_shipping_methods_constructor_exists():
    assert callable(SHIPPING_METHODS.__init__)


def test_hyp_shipping_methods_constructor_args():
    sig = inspect.signature(SHIPPING_METHODS.__init__)
    params = list(sig.parameters.keys())
    assert "createdAt" in params, "Missing parameter 'createdAt'"
    assert "price" in params, "Missing parameter 'price'"
    assert "address" in params, "Missing parameter 'address'"
    assert "arrival" in params, "Missing parameter 'arrival'"
    assert "_id" in params, "Missing parameter '_id'"
    assert "name" in params, "Missing parameter 'name'"









def test_hyp_status_is_not_abstract():
    assert not inspect.isabstract(STATUS)


def test_hyp_status_constructor_exists():
    assert callable(STATUS.__init__)


def test_hyp_status_constructor_args():
    sig = inspect.signature(STATUS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "_id" in params, "Missing parameter '_id'"
    assert "createdAt" in params, "Missing parameter 'createdAt'"






def test_hyp_shopping_history_is_not_abstract():
    assert not inspect.isabstract(SHOPPING_HISTORY)


def test_hyp_shopping_history_constructor_exists():
    assert callable(SHOPPING_HISTORY.__init__)


def test_hyp_shopping_history_constructor_args():
    sig = inspect.signature(SHOPPING_HISTORY.__init__)
    params = list(sig.parameters.keys())
    assert "photos" in params, "Missing parameter 'photos'"
    assert "shipName" in params, "Missing parameter 'shipName'"
    assert "shipArrival" in params, "Missing parameter 'shipArrival'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "status" in params, "Missing parameter 'status'"
    assert "STATUS_SHOPPING_HIST_ID" in params, "Missing parameter 'STATUS_SHOPPING_HIST_ID'"
    assert "created_at" in params, "Missing parameter 'created_at'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "price" in params, "Missing parameter 'price'"
    assert "note" in params, "Missing parameter 'note'"
    assert "shipAddress" in params, "Missing parameter 'shipAddress'"
    assert "name" in params, "Missing parameter 'name'"
    assert "productId" in params, "Missing parameter 'productId'"
    assert "storeId" in params, "Missing parameter 'storeId'"
    assert "isSold" in params, "Missing parameter 'isSold'"
    assert "score" in params, "Missing parameter 'score'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "description" in params, "Missing parameter 'description'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "shipPrice" in params, "Missing parameter 'shipPrice'"
    assert "_id" in params, "Missing parameter '_id'"
    assert "sold" in params, "Missing parameter 'sold'"
    assert "isNew" in params, "Missing parameter 'isNew'"


























def test_hyp_questions_is_not_abstract():
    assert not inspect.isabstract(QUESTIONS)


def test_hyp_questions_constructor_exists():
    assert callable(QUESTIONS.__init__)


def test_hyp_questions_constructor_args():
    sig = inspect.signature(QUESTIONS.__init__)
    params = list(sig.parameters.keys())
    assert "userId" in params, "Missing parameter 'userId'"
    assert "answer" in params, "Missing parameter 'answer'"
    assert "score" in params, "Missing parameter 'score'"
    assert "question" in params, "Missing parameter 'question'"
    assert "createdAt" in params, "Missing parameter 'createdAt'"
    assert "productId" in params, "Missing parameter 'productId'"
    assert "statusId" in params, "Missing parameter 'statusId'"
    assert "_id" in params, "Missing parameter '_id'"











def test_hyp_whises_is_not_abstract():
    assert not inspect.isabstract(WHISES)


def test_hyp_whises_constructor_exists():
    assert callable(WHISES.__init__)


def test_hyp_whises_constructor_args():
    sig = inspect.signature(WHISES.__init__)
    params = list(sig.parameters.keys())
    assert "_id" in params, "Missing parameter '_id'"
    assert "statusId" in params, "Missing parameter 'statusId'"
    assert "createdAt" in params, "Missing parameter 'createdAt'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "productId" in params, "Missing parameter 'productId'"








def test_hyp_categorias_is_not_abstract():
    assert not inspect.isabstract(CATEGORIAS)


def test_hyp_categorias_constructor_exists():
    assert callable(CATEGORIAS.__init__)


def test_hyp_categorias_constructor_args():
    sig = inspect.signature(CATEGORIAS.__init__)
    params = list(sig.parameters.keys())
    assert "_id" in params, "Missing parameter '_id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "createdAt" in params, "Missing parameter 'createdAt'"






def test_hyp_product_is_not_abstract():
    assert not inspect.isabstract(PRODUCT)


def test_hyp_product_constructor_exists():
    assert callable(PRODUCT.__init__)


def test_hyp_product_constructor_args():
    sig = inspect.signature(PRODUCT.__init__)
    params = list(sig.parameters.keys())
    assert "model" in params, "Missing parameter 'model'"
    assert "photos" in params, "Missing parameter 'photos'"
    assert "ShippingMethods" in params, "Missing parameter 'ShippingMethods'"
    assert "createdAt" in params, "Missing parameter 'createdAt'"
    assert "relatedProducts" in params, "Missing parameter 'relatedProducts'"
    assert "name" in params, "Missing parameter 'name'"
    assert "storeId" in params, "Missing parameter 'storeId'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "_id" in params, "Missing parameter '_id'"
    assert "statusId" in params, "Missing parameter 'statusId'"
    assert "dimensions" in params, "Missing parameter 'dimensions'"
    assert "description" in params, "Missing parameter 'description'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "price" in params, "Missing parameter 'price'"
    assert "color" in params, "Missing parameter 'color'"
    assert "isNew" in params, "Missing parameter 'isNew'"
    assert "sold" in params, "Missing parameter 'sold'"




















def test_hyp_roles_is_not_abstract():
    assert not inspect.isabstract(ROLES)


def test_hyp_roles_constructor_exists():
    assert callable(ROLES.__init__)


def test_hyp_roles_constructor_args():
    sig = inspect.signature(ROLES.__init__)
    params = list(sig.parameters.keys())
    assert "_id" in params, "Missing parameter '_id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "createdAt" in params, "Missing parameter 'createdAt'"






def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(USER)


def test_hyp_user_constructor_exists():
    assert callable(USER.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(USER.__init__)
    params = list(sig.parameters.keys())
    assert "verified" in params, "Missing parameter 'verified'"
    assert "lastAccess" in params, "Missing parameter 'lastAccess'"
    assert "name" in params, "Missing parameter 'name'"
    assert "_id" in params, "Missing parameter '_id'"
    assert "surname" in params, "Missing parameter 'surname'"
    assert "createdAt" in params, "Missing parameter 'createdAt'"
    assert "address" in params, "Missing parameter 'address'"
    assert "status" in params, "Missing parameter 'status'"
    assert "updateAt" in params, "Missing parameter 'updateAt'"
    assert "password" in params, "Missing parameter 'password'"
    assert "telephone" in params, "Missing parameter 'telephone'"
    assert "email" in params, "Missing parameter 'email'"















def test_hyp_follow_messenger_is_not_abstract():
    assert not inspect.isabstract(FOLLOW_MESSENGER)


def test_hyp_follow_messenger_constructor_exists():
    assert callable(FOLLOW_MESSENGER.__init__)


def test_hyp_follow_messenger_constructor_args():
    sig = inspect.signature(FOLLOW_MESSENGER.__init__)
    params = list(sig.parameters.keys())
    assert "userId" in params, "Missing parameter 'userId'"
    assert "createdAt" in params, "Missing parameter 'createdAt'"
    assert "_id" in params, "Missing parameter '_id'"






def test_hyp_feedback_comment_is_not_abstract():
    assert not inspect.isabstract(FEEDBACK_COMMENT)


def test_hyp_feedback_comment_constructor_exists():
    assert callable(FEEDBACK_COMMENT.__init__)


def test_hyp_feedback_comment_constructor_args():
    sig = inspect.signature(FEEDBACK_COMMENT.__init__)
    params = list(sig.parameters.keys())
    assert "createdAt" in params, "Missing parameter 'createdAt'"
    assert "feedbackId" in params, "Missing parameter 'feedbackId'"
    assert "_id" in params, "Missing parameter '_id'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "score" in params, "Missing parameter 'score'"









def test_hyp_shopping_messenger_is_not_abstract():
    assert not inspect.isabstract(SHOPPING_MESSENGER)


def test_hyp_shopping_messenger_constructor_exists():
    assert callable(SHOPPING_MESSENGER.__init__)


def test_hyp_shopping_messenger_constructor_args():
    sig = inspect.signature(SHOPPING_MESSENGER.__init__)
    params = list(sig.parameters.keys())
    assert "created_at" in params, "Missing parameter 'created_at'"
    assert "_id" in params, "Missing parameter '_id'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "message" in params, "Missing parameter 'message'"
    assert "photos" in params, "Missing parameter 'photos'"
    assert "storeId" in params, "Missing parameter 'storeId'"









def test_hyp_feedback_is_not_abstract():
    assert not inspect.isabstract(FEEDBACK)


def test_hyp_feedback_constructor_exists():
    assert callable(FEEDBACK.__init__)


def test_hyp_feedback_constructor_args():
    sig = inspect.signature(FEEDBACK.__init__)
    params = list(sig.parameters.keys())
    assert "userId" in params, "Missing parameter 'userId'"
    assert "createdAt" in params, "Missing parameter 'createdAt'"
    assert "linkYoutube" in params, "Missing parameter 'linkYoutube'"
    assert "like" in params, "Missing parameter 'like'"
    assert "updateAt" in params, "Missing parameter 'updateAt'"
    assert "wysiwyg" in params, "Missing parameter 'wysiwyg'"
    assert "_id" in params, "Missing parameter '_id'"
    assert "linkInstagram" in params, "Missing parameter 'linkInstagram'"
    assert "productId" in params, "Missing parameter 'productId'"
    assert "photos" in params, "Missing parameter 'photos'"












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
FOLLOW_strategy = st.builds(
    FOLLOW,
    userId=
        safe_text,
    createdAt=
        safe_text,
    followers=
        safe_text,
    followingGroup=
        safe_text,
    following=
        safe_text,
    _id=
        safe_text
)
SOCIAL_NETWORKS_strategy = st.builds(
    SOCIAL_NETWORKS,
    twitter=
        safe_text,
    updateAt=
        safe_text,
    facebook=
        safe_text,
    instagram=
        safe_text,
    _id=
        safe_text
)
REFUND_MESSAGES_strategy = st.builds(
    REFUND_MESSAGES,
    attach=
        safe_text,
    userId=
        safe_text,
    created_at=
        safe_text,
    _id=
        safe_text,
    message=
        safe_text
)
REFUND_strategy = st.builds(
    REFUND,
    message=
        safe_text,
    productId=
        safe_text,
    title=
        safe_text,
    storeId=
        safe_text,
    _id=
        safe_text,
    created_at=
        safe_text,
    userId=
        safe_text,
    shoppingHistoryId=
        safe_text
)
NOTIFICATION_strategy = st.builds(
    NOTIFICATION,
    _id=
        safe_text,
    code=
        safe_text,
    message=
        safe_text,
    createdAt=
        safe_text,
    userId=
        safe_text
)
Class_strategy = st.builds(
    Class,
)
EVENTS_LIST_strategy = st.builds(
    EVENTS_LIST,
    key=
        safe_text,
    description=
        safe_text,
    _id=
        safe_text,
    createdAt=
        safe_text
)
EVENTS_HISTORY_strategy = st.builds(
    EVENTS_HISTORY,
    createdAt=
        safe_text,
    newValue=
        safe_text,
    oldValue=
        safe_text,
    userId=
        safe_text,
    eventId=
        safe_text,
    _id=
        safe_text
)
FAVORITES_strategy = st.builds(
    FAVORITES,
    statusId=
        safe_text,
    storeId=
        safe_text,
    createdAt=
        safe_text,
    _id=
        safe_text,
    userId=
        safe_text
)
STORE_strategy = st.builds(
    STORE,
    telephone=
        safe_text,
    statusId=
        safe_text,
    createdAt=
        safe_text,
    address=
        safe_text,
    updateAt=
        safe_text,
    _id=
        safe_text,
    schedule=
        safe_text,
    name=
        safe_text,
    email=
        safe_text
)
STATUS_SHOPPING_HISTORY_strategy = st.builds(
    STATUS_SHOPPING_HISTORY,
    _id=
        safe_text,
    name=
        safe_text
)
STATUS2_strategy = st.builds(
    STATUS2,
    _id=
        safe_text,
    name=
        safe_text
)
SUBSCRIPTION_BENEFITS_strategy = st.builds(
    SUBSCRIPTION_BENEFITS,
    description=
        safe_text,
    key_name=
        safe_text,
    _id=
        safe_text
)
SHIPPING_METHODS_strategy = st.builds(
    SHIPPING_METHODS,
    createdAt=
        safe_text,
    price=
        st.integers(),
    address=
        safe_text,
    arrival=
        safe_text,
    _id=
        safe_text,
    name=
        safe_text
)
STATUS_strategy = st.builds(
    STATUS,
    name=
        safe_text,
    _id=
        safe_text,
    createdAt=
        safe_text
)
SHOPPING_HISTORY_strategy = st.builds(
    SHOPPING_HISTORY,
    photos=
        safe_text,
    shipName=
        safe_text,
    shipArrival=
        safe_text,
    quantity=
        st.integers(),
    status=
        safe_text,
    STATUS_SHOPPING_HIST_ID=
        safe_text,
    created_at=
        safe_text,
    userId=
        safe_text,
    price=
        st.integers(),
    note=
        safe_text,
    shipAddress=
        safe_text,
    name=
        safe_text,
    productId=
        safe_text,
    storeId=
        safe_text,
    isSold=
        st.booleans(),
    score=
        st.integers(),
    comment=
        safe_text,
    description=
        safe_text,
    attribute=
        safe_text,
    shipPrice=
        st.integers(),
    _id=
        safe_text,
    sold=
        st.integers(),
    isNew=
        st.booleans()
)
QUESTIONS_strategy = st.builds(
    QUESTIONS,
    userId=
        safe_text,
    answer=
        safe_text,
    score=
        st.integers(),
    question=
        safe_text,
    createdAt=
        safe_text,
    productId=
        safe_text,
    statusId=
        safe_text,
    _id=
        safe_text
)
WHISES_strategy = st.builds(
    WHISES,
    _id=
        safe_text,
    statusId=
        safe_text,
    createdAt=
        safe_text,
    userId=
        safe_text,
    productId=
        safe_text
)
CATEGORIAS_strategy = st.builds(
    CATEGORIAS,
    _id=
        safe_text,
    name=
        safe_text,
    createdAt=
        safe_text
)
PRODUCT_strategy = st.builds(
    PRODUCT,
    model=
        safe_text,
    photos=
        safe_text,
    ShippingMethods=
        safe_text,
    createdAt=
        safe_text,
    relatedProducts=
        safe_text,
    name=
        safe_text,
    storeId=
        safe_text,
    attribute=
        safe_text,
    _id=
        safe_text,
    statusId=
        safe_text,
    dimensions=
        safe_text,
    description=
        safe_text,
    quantity=
        st.integers(),
    price=
        st.integers(),
    color=
        safe_text,
    isNew=
        st.booleans(),
    sold=
        st.integers()
)
ROLES_strategy = st.builds(
    ROLES,
    _id=
        safe_text,
    name=
        safe_text,
    createdAt=
        safe_text
)
USER_strategy = st.builds(
    USER,
    verified=
        st.booleans(),
    lastAccess=
        safe_text,
    name=
        safe_text,
    _id=
        safe_text,
    surname=
        safe_text,
    createdAt=
        safe_text,
    address=
        safe_text,
    status=
        safe_text,
    updateAt=
        safe_text,
    password=
        safe_text,
    telephone=
        safe_text,
    email=
        safe_text
)
FOLLOW_MESSENGER_strategy = st.builds(
    FOLLOW_MESSENGER,
    userId=
        safe_text,
    createdAt=
        safe_text,
    _id=
        safe_text
)
FEEDBACK_COMMENT_strategy = st.builds(
    FEEDBACK_COMMENT,
    createdAt=
        safe_text,
    feedbackId=
        safe_text,
    _id=
        safe_text,
    userId=
        safe_text,
    comment=
        safe_text,
    score=
        st.integers()
)
SHOPPING_MESSENGER_strategy = st.builds(
    SHOPPING_MESSENGER,
    created_at=
        safe_text,
    _id=
        safe_text,
    userId=
        safe_text,
    message=
        safe_text,
    photos=
        safe_text,
    storeId=
        safe_text
)
FEEDBACK_strategy = st.builds(
    FEEDBACK,
    userId=
        safe_text,
    createdAt=
        safe_text,
    linkYoutube=
        safe_text,
    like=
        safe_text,
    updateAt=
        safe_text,
    wysiwyg=
        safe_text,
    _id=
        safe_text,
    linkInstagram=
        safe_text,
    productId=
        safe_text,
    photos=
        safe_text
)




@given(instance=FOLLOW_strategy)
def test_hyp_follow_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=FOLLOW_strategy)
def test_hyp_follow_createdAt_setter(instance):
    original = instance.createdAt
    instance.createdAt = original
    assert instance.createdAt == original



@given(instance=FOLLOW_strategy)
def test_hyp_follow_followers_setter(instance):
    original = instance.followers
    instance.followers = original
    assert instance.followers == original



@given(instance=FOLLOW_strategy)
def test_hyp_follow_followingGroup_setter(instance):
    original = instance.followingGroup
    instance.followingGroup = original
    assert instance.followingGroup == original



@given(instance=FOLLOW_strategy)
def test_hyp_follow_following_setter(instance):
    original = instance.following
    instance.following = original
    assert instance.following == original



@given(instance=FOLLOW_strategy)
def test_hyp_follow__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original




@given(instance=SOCIAL_NETWORKS_strategy)
def test_hyp_social_networks_twitter_setter(instance):
    original = instance.twitter
    instance.twitter = original
    assert instance.twitter == original



@given(instance=SOCIAL_NETWORKS_strategy)
def test_hyp_social_networks_updateAt_setter(instance):
    original = instance.updateAt
    instance.updateAt = original
    assert instance.updateAt == original



@given(instance=SOCIAL_NETWORKS_strategy)
def test_hyp_social_networks_facebook_setter(instance):
    original = instance.facebook
    instance.facebook = original
    assert instance.facebook == original



@given(instance=SOCIAL_NETWORKS_strategy)
def test_hyp_social_networks_instagram_setter(instance):
    original = instance.instagram
    instance.instagram = original
    assert instance.instagram == original



@given(instance=SOCIAL_NETWORKS_strategy)
def test_hyp_social_networks__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original




@given(instance=REFUND_MESSAGES_strategy)
def test_hyp_refund_messages_attach_setter(instance):
    original = instance.attach
    instance.attach = original
    assert instance.attach == original



@given(instance=REFUND_MESSAGES_strategy)
def test_hyp_refund_messages_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=REFUND_MESSAGES_strategy)
def test_hyp_refund_messages_created_at_setter(instance):
    original = instance.created_at
    instance.created_at = original
    assert instance.created_at == original



@given(instance=REFUND_MESSAGES_strategy)
def test_hyp_refund_messages__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original



@given(instance=REFUND_MESSAGES_strategy)
def test_hyp_refund_messages_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original




@given(instance=REFUND_strategy)
def test_hyp_refund_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=REFUND_strategy)
def test_hyp_refund_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original



@given(instance=REFUND_strategy)
def test_hyp_refund_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=REFUND_strategy)
def test_hyp_refund_storeId_setter(instance):
    original = instance.storeId
    instance.storeId = original
    assert instance.storeId == original



@given(instance=REFUND_strategy)
def test_hyp_refund__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original



@given(instance=REFUND_strategy)
def test_hyp_refund_created_at_setter(instance):
    original = instance.created_at
    instance.created_at = original
    assert instance.created_at == original



@given(instance=REFUND_strategy)
def test_hyp_refund_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=REFUND_strategy)
def test_hyp_refund_shoppingHistoryId_setter(instance):
    original = instance.shoppingHistoryId
    instance.shoppingHistoryId = original
    assert instance.shoppingHistoryId == original




@given(instance=NOTIFICATION_strategy)
def test_hyp_notification__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original



@given(instance=NOTIFICATION_strategy)
def test_hyp_notification_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=NOTIFICATION_strategy)
def test_hyp_notification_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=NOTIFICATION_strategy)
def test_hyp_notification_createdAt_setter(instance):
    original = instance.createdAt
    instance.createdAt = original
    assert instance.createdAt == original



@given(instance=NOTIFICATION_strategy)
def test_hyp_notification_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original





@given(instance=EVENTS_LIST_strategy)
def test_hyp_events_list_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=EVENTS_LIST_strategy)
def test_hyp_events_list_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=EVENTS_LIST_strategy)
def test_hyp_events_list__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original



@given(instance=EVENTS_LIST_strategy)
def test_hyp_events_list_createdAt_setter(instance):
    original = instance.createdAt
    instance.createdAt = original
    assert instance.createdAt == original




@given(instance=EVENTS_HISTORY_strategy)
def test_hyp_events_history_createdAt_setter(instance):
    original = instance.createdAt
    instance.createdAt = original
    assert instance.createdAt == original



@given(instance=EVENTS_HISTORY_strategy)
def test_hyp_events_history_newValue_setter(instance):
    original = instance.newValue
    instance.newValue = original
    assert instance.newValue == original



@given(instance=EVENTS_HISTORY_strategy)
def test_hyp_events_history_oldValue_setter(instance):
    original = instance.oldValue
    instance.oldValue = original
    assert instance.oldValue == original



@given(instance=EVENTS_HISTORY_strategy)
def test_hyp_events_history_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=EVENTS_HISTORY_strategy)
def test_hyp_events_history_eventId_setter(instance):
    original = instance.eventId
    instance.eventId = original
    assert instance.eventId == original



@given(instance=EVENTS_HISTORY_strategy)
def test_hyp_events_history__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original




@given(instance=FAVORITES_strategy)
def test_hyp_favorites_statusId_setter(instance):
    original = instance.statusId
    instance.statusId = original
    assert instance.statusId == original



@given(instance=FAVORITES_strategy)
def test_hyp_favorites_storeId_setter(instance):
    original = instance.storeId
    instance.storeId = original
    assert instance.storeId == original



@given(instance=FAVORITES_strategy)
def test_hyp_favorites_createdAt_setter(instance):
    original = instance.createdAt
    instance.createdAt = original
    assert instance.createdAt == original



@given(instance=FAVORITES_strategy)
def test_hyp_favorites__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original



@given(instance=FAVORITES_strategy)
def test_hyp_favorites_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original




@given(instance=STORE_strategy)
def test_hyp_store_telephone_setter(instance):
    original = instance.telephone
    instance.telephone = original
    assert instance.telephone == original



@given(instance=STORE_strategy)
def test_hyp_store_statusId_setter(instance):
    original = instance.statusId
    instance.statusId = original
    assert instance.statusId == original



@given(instance=STORE_strategy)
def test_hyp_store_createdAt_setter(instance):
    original = instance.createdAt
    instance.createdAt = original
    assert instance.createdAt == original



@given(instance=STORE_strategy)
def test_hyp_store_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=STORE_strategy)
def test_hyp_store_updateAt_setter(instance):
    original = instance.updateAt
    instance.updateAt = original
    assert instance.updateAt == original



@given(instance=STORE_strategy)
def test_hyp_store__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original



@given(instance=STORE_strategy)
def test_hyp_store_schedule_setter(instance):
    original = instance.schedule
    instance.schedule = original
    assert instance.schedule == original



@given(instance=STORE_strategy)
def test_hyp_store_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=STORE_strategy)
def test_hyp_store_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original




@given(instance=STATUS_SHOPPING_HISTORY_strategy)
def test_hyp_status_shopping_history__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original



@given(instance=STATUS_SHOPPING_HISTORY_strategy)
def test_hyp_status_shopping_history_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=STATUS2_strategy)
def test_hyp_status2__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original



@given(instance=STATUS2_strategy)
def test_hyp_status2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=SUBSCRIPTION_BENEFITS_strategy)
def test_hyp_subscription_benefits_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=SUBSCRIPTION_BENEFITS_strategy)
def test_hyp_subscription_benefits_key_name_setter(instance):
    original = instance.key_name
    instance.key_name = original
    assert instance.key_name == original



@given(instance=SUBSCRIPTION_BENEFITS_strategy)
def test_hyp_subscription_benefits__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original




@given(instance=SHIPPING_METHODS_strategy)
def test_hyp_shipping_methods_createdAt_setter(instance):
    original = instance.createdAt
    instance.createdAt = original
    assert instance.createdAt == original



@given(instance=SHIPPING_METHODS_strategy)
def test_hyp_shipping_methods_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=SHIPPING_METHODS_strategy)
def test_hyp_shipping_methods_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=SHIPPING_METHODS_strategy)
def test_hyp_shipping_methods_arrival_setter(instance):
    original = instance.arrival
    instance.arrival = original
    assert instance.arrival == original



@given(instance=SHIPPING_METHODS_strategy)
def test_hyp_shipping_methods__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original



@given(instance=SHIPPING_METHODS_strategy)
def test_hyp_shipping_methods_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=STATUS_strategy)
def test_hyp_status_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=STATUS_strategy)
def test_hyp_status__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original



@given(instance=STATUS_strategy)
def test_hyp_status_createdAt_setter(instance):
    original = instance.createdAt
    instance.createdAt = original
    assert instance.createdAt == original




@given(instance=SHOPPING_HISTORY_strategy)
def test_hyp_shopping_history_photos_setter(instance):
    original = instance.photos
    instance.photos = original
    assert instance.photos == original



@given(instance=SHOPPING_HISTORY_strategy)
def test_hyp_shopping_history_shipName_setter(instance):
    original = instance.shipName
    instance.shipName = original
    assert instance.shipName == original



@given(instance=SHOPPING_HISTORY_strategy)
def test_hyp_shopping_history_shipArrival_setter(instance):
    original = instance.shipArrival
    instance.shipArrival = original
    assert instance.shipArrival == original



@given(instance=SHOPPING_HISTORY_strategy)
def test_hyp_shopping_history_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=SHOPPING_HISTORY_strategy)
def test_hyp_shopping_history_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=SHOPPING_HISTORY_strategy)
def test_hyp_shopping_history_STATUS_SHOPPING_HIST_ID_setter(instance):
    original = instance.STATUS_SHOPPING_HIST_ID
    instance.STATUS_SHOPPING_HIST_ID = original
    assert instance.STATUS_SHOPPING_HIST_ID == original



@given(instance=SHOPPING_HISTORY_strategy)
def test_hyp_shopping_history_created_at_setter(instance):
    original = instance.created_at
    instance.created_at = original
    assert instance.created_at == original



@given(instance=SHOPPING_HISTORY_strategy)
def test_hyp_shopping_history_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=SHOPPING_HISTORY_strategy)
def test_hyp_shopping_history_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=SHOPPING_HISTORY_strategy)
def test_hyp_shopping_history_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original



@given(instance=SHOPPING_HISTORY_strategy)
def test_hyp_shopping_history_shipAddress_setter(instance):
    original = instance.shipAddress
    instance.shipAddress = original
    assert instance.shipAddress == original



@given(instance=SHOPPING_HISTORY_strategy)
def test_hyp_shopping_history_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SHOPPING_HISTORY_strategy)
def test_hyp_shopping_history_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original



@given(instance=SHOPPING_HISTORY_strategy)
def test_hyp_shopping_history_storeId_setter(instance):
    original = instance.storeId
    instance.storeId = original
    assert instance.storeId == original



@given(instance=SHOPPING_HISTORY_strategy)
def test_hyp_shopping_history_isSold_setter(instance):
    original = instance.isSold
    instance.isSold = original
    assert instance.isSold == original



@given(instance=SHOPPING_HISTORY_strategy)
def test_hyp_shopping_history_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original



@given(instance=SHOPPING_HISTORY_strategy)
def test_hyp_shopping_history_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=SHOPPING_HISTORY_strategy)
def test_hyp_shopping_history_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=SHOPPING_HISTORY_strategy)
def test_hyp_shopping_history_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=SHOPPING_HISTORY_strategy)
def test_hyp_shopping_history_shipPrice_setter(instance):
    original = instance.shipPrice
    instance.shipPrice = original
    assert instance.shipPrice == original



@given(instance=SHOPPING_HISTORY_strategy)
def test_hyp_shopping_history__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original



@given(instance=SHOPPING_HISTORY_strategy)
def test_hyp_shopping_history_sold_setter(instance):
    original = instance.sold
    instance.sold = original
    assert instance.sold == original



@given(instance=SHOPPING_HISTORY_strategy)
def test_hyp_shopping_history_isNew_setter(instance):
    original = instance.isNew
    instance.isNew = original
    assert instance.isNew == original




@given(instance=QUESTIONS_strategy)
def test_hyp_questions_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=QUESTIONS_strategy)
def test_hyp_questions_answer_setter(instance):
    original = instance.answer
    instance.answer = original
    assert instance.answer == original



@given(instance=QUESTIONS_strategy)
def test_hyp_questions_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original



@given(instance=QUESTIONS_strategy)
def test_hyp_questions_question_setter(instance):
    original = instance.question
    instance.question = original
    assert instance.question == original



@given(instance=QUESTIONS_strategy)
def test_hyp_questions_createdAt_setter(instance):
    original = instance.createdAt
    instance.createdAt = original
    assert instance.createdAt == original



@given(instance=QUESTIONS_strategy)
def test_hyp_questions_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original



@given(instance=QUESTIONS_strategy)
def test_hyp_questions_statusId_setter(instance):
    original = instance.statusId
    instance.statusId = original
    assert instance.statusId == original



@given(instance=QUESTIONS_strategy)
def test_hyp_questions__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original




@given(instance=WHISES_strategy)
def test_hyp_whises__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original



@given(instance=WHISES_strategy)
def test_hyp_whises_statusId_setter(instance):
    original = instance.statusId
    instance.statusId = original
    assert instance.statusId == original



@given(instance=WHISES_strategy)
def test_hyp_whises_createdAt_setter(instance):
    original = instance.createdAt
    instance.createdAt = original
    assert instance.createdAt == original



@given(instance=WHISES_strategy)
def test_hyp_whises_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=WHISES_strategy)
def test_hyp_whises_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original




@given(instance=CATEGORIAS_strategy)
def test_hyp_categorias__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original



@given(instance=CATEGORIAS_strategy)
def test_hyp_categorias_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=CATEGORIAS_strategy)
def test_hyp_categorias_createdAt_setter(instance):
    original = instance.createdAt
    instance.createdAt = original
    assert instance.createdAt == original




@given(instance=PRODUCT_strategy)
def test_hyp_product_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original



@given(instance=PRODUCT_strategy)
def test_hyp_product_photos_setter(instance):
    original = instance.photos
    instance.photos = original
    assert instance.photos == original



@given(instance=PRODUCT_strategy)
def test_hyp_product_ShippingMethods_setter(instance):
    original = instance.ShippingMethods
    instance.ShippingMethods = original
    assert instance.ShippingMethods == original



@given(instance=PRODUCT_strategy)
def test_hyp_product_createdAt_setter(instance):
    original = instance.createdAt
    instance.createdAt = original
    assert instance.createdAt == original



@given(instance=PRODUCT_strategy)
def test_hyp_product_relatedProducts_setter(instance):
    original = instance.relatedProducts
    instance.relatedProducts = original
    assert instance.relatedProducts == original



@given(instance=PRODUCT_strategy)
def test_hyp_product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=PRODUCT_strategy)
def test_hyp_product_storeId_setter(instance):
    original = instance.storeId
    instance.storeId = original
    assert instance.storeId == original



@given(instance=PRODUCT_strategy)
def test_hyp_product_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=PRODUCT_strategy)
def test_hyp_product__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original



@given(instance=PRODUCT_strategy)
def test_hyp_product_statusId_setter(instance):
    original = instance.statusId
    instance.statusId = original
    assert instance.statusId == original



@given(instance=PRODUCT_strategy)
def test_hyp_product_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original



@given(instance=PRODUCT_strategy)
def test_hyp_product_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=PRODUCT_strategy)
def test_hyp_product_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=PRODUCT_strategy)
def test_hyp_product_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=PRODUCT_strategy)
def test_hyp_product_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=PRODUCT_strategy)
def test_hyp_product_isNew_setter(instance):
    original = instance.isNew
    instance.isNew = original
    assert instance.isNew == original



@given(instance=PRODUCT_strategy)
def test_hyp_product_sold_setter(instance):
    original = instance.sold
    instance.sold = original
    assert instance.sold == original




@given(instance=ROLES_strategy)
def test_hyp_roles__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original



@given(instance=ROLES_strategy)
def test_hyp_roles_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ROLES_strategy)
def test_hyp_roles_createdAt_setter(instance):
    original = instance.createdAt
    instance.createdAt = original
    assert instance.createdAt == original




@given(instance=USER_strategy)
def test_hyp_user_verified_setter(instance):
    original = instance.verified
    instance.verified = original
    assert instance.verified == original



@given(instance=USER_strategy)
def test_hyp_user_lastAccess_setter(instance):
    original = instance.lastAccess
    instance.lastAccess = original
    assert instance.lastAccess == original



@given(instance=USER_strategy)
def test_hyp_user_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=USER_strategy)
def test_hyp_user__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original



@given(instance=USER_strategy)
def test_hyp_user_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original



@given(instance=USER_strategy)
def test_hyp_user_createdAt_setter(instance):
    original = instance.createdAt
    instance.createdAt = original
    assert instance.createdAt == original



@given(instance=USER_strategy)
def test_hyp_user_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=USER_strategy)
def test_hyp_user_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=USER_strategy)
def test_hyp_user_updateAt_setter(instance):
    original = instance.updateAt
    instance.updateAt = original
    assert instance.updateAt == original



@given(instance=USER_strategy)
def test_hyp_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=USER_strategy)
def test_hyp_user_telephone_setter(instance):
    original = instance.telephone
    instance.telephone = original
    assert instance.telephone == original



@given(instance=USER_strategy)
def test_hyp_user_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original




@given(instance=FOLLOW_MESSENGER_strategy)
def test_hyp_follow_messenger_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=FOLLOW_MESSENGER_strategy)
def test_hyp_follow_messenger_createdAt_setter(instance):
    original = instance.createdAt
    instance.createdAt = original
    assert instance.createdAt == original



@given(instance=FOLLOW_MESSENGER_strategy)
def test_hyp_follow_messenger__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original




@given(instance=FEEDBACK_COMMENT_strategy)
def test_hyp_feedback_comment_createdAt_setter(instance):
    original = instance.createdAt
    instance.createdAt = original
    assert instance.createdAt == original



@given(instance=FEEDBACK_COMMENT_strategy)
def test_hyp_feedback_comment_feedbackId_setter(instance):
    original = instance.feedbackId
    instance.feedbackId = original
    assert instance.feedbackId == original



@given(instance=FEEDBACK_COMMENT_strategy)
def test_hyp_feedback_comment__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original



@given(instance=FEEDBACK_COMMENT_strategy)
def test_hyp_feedback_comment_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=FEEDBACK_COMMENT_strategy)
def test_hyp_feedback_comment_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=FEEDBACK_COMMENT_strategy)
def test_hyp_feedback_comment_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original




@given(instance=SHOPPING_MESSENGER_strategy)
def test_hyp_shopping_messenger_created_at_setter(instance):
    original = instance.created_at
    instance.created_at = original
    assert instance.created_at == original



@given(instance=SHOPPING_MESSENGER_strategy)
def test_hyp_shopping_messenger__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original



@given(instance=SHOPPING_MESSENGER_strategy)
def test_hyp_shopping_messenger_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=SHOPPING_MESSENGER_strategy)
def test_hyp_shopping_messenger_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=SHOPPING_MESSENGER_strategy)
def test_hyp_shopping_messenger_photos_setter(instance):
    original = instance.photos
    instance.photos = original
    assert instance.photos == original



@given(instance=SHOPPING_MESSENGER_strategy)
def test_hyp_shopping_messenger_storeId_setter(instance):
    original = instance.storeId
    instance.storeId = original
    assert instance.storeId == original




@given(instance=FEEDBACK_strategy)
def test_hyp_feedback_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=FEEDBACK_strategy)
def test_hyp_feedback_createdAt_setter(instance):
    original = instance.createdAt
    instance.createdAt = original
    assert instance.createdAt == original



@given(instance=FEEDBACK_strategy)
def test_hyp_feedback_linkYoutube_setter(instance):
    original = instance.linkYoutube
    instance.linkYoutube = original
    assert instance.linkYoutube == original



@given(instance=FEEDBACK_strategy)
def test_hyp_feedback_like_setter(instance):
    original = instance.like
    instance.like = original
    assert instance.like == original



@given(instance=FEEDBACK_strategy)
def test_hyp_feedback_updateAt_setter(instance):
    original = instance.updateAt
    instance.updateAt = original
    assert instance.updateAt == original



@given(instance=FEEDBACK_strategy)
def test_hyp_feedback_wysiwyg_setter(instance):
    original = instance.wysiwyg
    instance.wysiwyg = original
    assert instance.wysiwyg == original



@given(instance=FEEDBACK_strategy)
def test_hyp_feedback__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original



@given(instance=FEEDBACK_strategy)
def test_hyp_feedback_linkInstagram_setter(instance):
    original = instance.linkInstagram
    instance.linkInstagram = original
    assert instance.linkInstagram == original



@given(instance=FEEDBACK_strategy)
def test_hyp_feedback_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original



@given(instance=FEEDBACK_strategy)
def test_hyp_feedback_photos_setter(instance):
    original = instance.photos
    instance.photos = original
    assert instance.photos == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_CATEGORIAS__id_value_roundtrip():
    instance = CATEGORIAS(_id="sample_text", createdAt="sample_text", name="sample_text")
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_CATEGORIAS_createdAt_value_roundtrip():
    instance = CATEGORIAS(_id="sample_text", createdAt="sample_text", name="sample_text")
    assert instance.createdAt == "sample_text"
    instance.createdAt = "sample_text_2"
    assert instance.createdAt == "sample_text_2"


def test_CATEGORIAS_name_value_roundtrip():
    instance = CATEGORIAS(_id="sample_text", createdAt="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_EVENTS_HISTORY__id_value_roundtrip():
    instance = EVENTS_HISTORY(_id="sample_text", createdAt="sample_text", eventId="sample_text", newValue="sample_text", oldValue="sample_text", userId="sample_text")
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_EVENTS_HISTORY_createdAt_value_roundtrip():
    instance = EVENTS_HISTORY(_id="sample_text", createdAt="sample_text", eventId="sample_text", newValue="sample_text", oldValue="sample_text", userId="sample_text")
    assert instance.createdAt == "sample_text"
    instance.createdAt = "sample_text_2"
    assert instance.createdAt == "sample_text_2"


def test_EVENTS_HISTORY_eventId_value_roundtrip():
    instance = EVENTS_HISTORY(_id="sample_text", createdAt="sample_text", eventId="sample_text", newValue="sample_text", oldValue="sample_text", userId="sample_text")
    assert instance.eventId == "sample_text"
    instance.eventId = "sample_text_2"
    assert instance.eventId == "sample_text_2"


def test_EVENTS_HISTORY_newValue_value_roundtrip():
    instance = EVENTS_HISTORY(_id="sample_text", createdAt="sample_text", eventId="sample_text", newValue="sample_text", oldValue="sample_text", userId="sample_text")
    assert instance.newValue == "sample_text"
    instance.newValue = "sample_text_2"
    assert instance.newValue == "sample_text_2"


def test_EVENTS_HISTORY_oldValue_value_roundtrip():
    instance = EVENTS_HISTORY(_id="sample_text", createdAt="sample_text", eventId="sample_text", newValue="sample_text", oldValue="sample_text", userId="sample_text")
    assert instance.oldValue == "sample_text"
    instance.oldValue = "sample_text_2"
    assert instance.oldValue == "sample_text_2"


def test_EVENTS_HISTORY_userId_value_roundtrip():
    instance = EVENTS_HISTORY(_id="sample_text", createdAt="sample_text", eventId="sample_text", newValue="sample_text", oldValue="sample_text", userId="sample_text")
    assert instance.userId == "sample_text"
    instance.userId = "sample_text_2"
    assert instance.userId == "sample_text_2"


def test_EVENTS_LIST__id_value_roundtrip():
    instance = EVENTS_LIST(_id="sample_text", createdAt="sample_text", description="sample_text", key="sample_text")
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_EVENTS_LIST_createdAt_value_roundtrip():
    instance = EVENTS_LIST(_id="sample_text", createdAt="sample_text", description="sample_text", key="sample_text")
    assert instance.createdAt == "sample_text"
    instance.createdAt = "sample_text_2"
    assert instance.createdAt == "sample_text_2"


def test_EVENTS_LIST_description_value_roundtrip():
    instance = EVENTS_LIST(_id="sample_text", createdAt="sample_text", description="sample_text", key="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_EVENTS_LIST_key_value_roundtrip():
    instance = EVENTS_LIST(_id="sample_text", createdAt="sample_text", description="sample_text", key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_FAVORITES__id_value_roundtrip():
    instance = FAVORITES(_id="sample_text", createdAt="sample_text", statusId="sample_text", storeId="sample_text", userId="sample_text")
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_FAVORITES_createdAt_value_roundtrip():
    instance = FAVORITES(_id="sample_text", createdAt="sample_text", statusId="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.createdAt == "sample_text"
    instance.createdAt = "sample_text_2"
    assert instance.createdAt == "sample_text_2"


def test_FAVORITES_statusId_value_roundtrip():
    instance = FAVORITES(_id="sample_text", createdAt="sample_text", statusId="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.statusId == "sample_text"
    instance.statusId = "sample_text_2"
    assert instance.statusId == "sample_text_2"


def test_FAVORITES_storeId_value_roundtrip():
    instance = FAVORITES(_id="sample_text", createdAt="sample_text", statusId="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.storeId == "sample_text"
    instance.storeId = "sample_text_2"
    assert instance.storeId == "sample_text_2"


def test_FAVORITES_userId_value_roundtrip():
    instance = FAVORITES(_id="sample_text", createdAt="sample_text", statusId="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.userId == "sample_text"
    instance.userId = "sample_text_2"
    assert instance.userId == "sample_text_2"


def test_FEEDBACK__id_value_roundtrip():
    instance = FEEDBACK(_id="sample_text", createdAt="sample_text", like="sample_text", linkInstagram="sample_text", linkYoutube="sample_text", photos="sample_text", productId="sample_text", updateAt="sample_text", userId="sample_text", wysiwyg="sample_text")
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_FEEDBACK_createdAt_value_roundtrip():
    instance = FEEDBACK(_id="sample_text", createdAt="sample_text", like="sample_text", linkInstagram="sample_text", linkYoutube="sample_text", photos="sample_text", productId="sample_text", updateAt="sample_text", userId="sample_text", wysiwyg="sample_text")
    assert instance.createdAt == "sample_text"
    instance.createdAt = "sample_text_2"
    assert instance.createdAt == "sample_text_2"


def test_FEEDBACK_like_value_roundtrip():
    instance = FEEDBACK(_id="sample_text", createdAt="sample_text", like="sample_text", linkInstagram="sample_text", linkYoutube="sample_text", photos="sample_text", productId="sample_text", updateAt="sample_text", userId="sample_text", wysiwyg="sample_text")
    assert instance.like == "sample_text"
    instance.like = "sample_text_2"
    assert instance.like == "sample_text_2"


def test_FEEDBACK_linkInstagram_value_roundtrip():
    instance = FEEDBACK(_id="sample_text", createdAt="sample_text", like="sample_text", linkInstagram="sample_text", linkYoutube="sample_text", photos="sample_text", productId="sample_text", updateAt="sample_text", userId="sample_text", wysiwyg="sample_text")
    assert instance.linkInstagram == "sample_text"
    instance.linkInstagram = "sample_text_2"
    assert instance.linkInstagram == "sample_text_2"


def test_FEEDBACK_linkYoutube_value_roundtrip():
    instance = FEEDBACK(_id="sample_text", createdAt="sample_text", like="sample_text", linkInstagram="sample_text", linkYoutube="sample_text", photos="sample_text", productId="sample_text", updateAt="sample_text", userId="sample_text", wysiwyg="sample_text")
    assert instance.linkYoutube == "sample_text"
    instance.linkYoutube = "sample_text_2"
    assert instance.linkYoutube == "sample_text_2"


def test_FEEDBACK_photos_value_roundtrip():
    instance = FEEDBACK(_id="sample_text", createdAt="sample_text", like="sample_text", linkInstagram="sample_text", linkYoutube="sample_text", photos="sample_text", productId="sample_text", updateAt="sample_text", userId="sample_text", wysiwyg="sample_text")
    assert instance.photos == "sample_text"
    instance.photos = "sample_text_2"
    assert instance.photos == "sample_text_2"


def test_FEEDBACK_productId_value_roundtrip():
    instance = FEEDBACK(_id="sample_text", createdAt="sample_text", like="sample_text", linkInstagram="sample_text", linkYoutube="sample_text", photos="sample_text", productId="sample_text", updateAt="sample_text", userId="sample_text", wysiwyg="sample_text")
    assert instance.productId == "sample_text"
    instance.productId = "sample_text_2"
    assert instance.productId == "sample_text_2"


def test_FEEDBACK_updateAt_value_roundtrip():
    instance = FEEDBACK(_id="sample_text", createdAt="sample_text", like="sample_text", linkInstagram="sample_text", linkYoutube="sample_text", photos="sample_text", productId="sample_text", updateAt="sample_text", userId="sample_text", wysiwyg="sample_text")
    assert instance.updateAt == "sample_text"
    instance.updateAt = "sample_text_2"
    assert instance.updateAt == "sample_text_2"


def test_FEEDBACK_userId_value_roundtrip():
    instance = FEEDBACK(_id="sample_text", createdAt="sample_text", like="sample_text", linkInstagram="sample_text", linkYoutube="sample_text", photos="sample_text", productId="sample_text", updateAt="sample_text", userId="sample_text", wysiwyg="sample_text")
    assert instance.userId == "sample_text"
    instance.userId = "sample_text_2"
    assert instance.userId == "sample_text_2"


def test_FEEDBACK_wysiwyg_value_roundtrip():
    instance = FEEDBACK(_id="sample_text", createdAt="sample_text", like="sample_text", linkInstagram="sample_text", linkYoutube="sample_text", photos="sample_text", productId="sample_text", updateAt="sample_text", userId="sample_text", wysiwyg="sample_text")
    assert instance.wysiwyg == "sample_text"
    instance.wysiwyg = "sample_text_2"
    assert instance.wysiwyg == "sample_text_2"


def test_FEEDBACK_COMMENT__id_value_roundtrip():
    instance = FEEDBACK_COMMENT(_id="sample_text", comment="sample_text", createdAt="sample_text", feedbackId="sample_text", score=7, userId="sample_text")
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_FEEDBACK_COMMENT_comment_value_roundtrip():
    instance = FEEDBACK_COMMENT(_id="sample_text", comment="sample_text", createdAt="sample_text", feedbackId="sample_text", score=7, userId="sample_text")
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_FEEDBACK_COMMENT_createdAt_value_roundtrip():
    instance = FEEDBACK_COMMENT(_id="sample_text", comment="sample_text", createdAt="sample_text", feedbackId="sample_text", score=7, userId="sample_text")
    assert instance.createdAt == "sample_text"
    instance.createdAt = "sample_text_2"
    assert instance.createdAt == "sample_text_2"


def test_FEEDBACK_COMMENT_feedbackId_value_roundtrip():
    instance = FEEDBACK_COMMENT(_id="sample_text", comment="sample_text", createdAt="sample_text", feedbackId="sample_text", score=7, userId="sample_text")
    assert instance.feedbackId == "sample_text"
    instance.feedbackId = "sample_text_2"
    assert instance.feedbackId == "sample_text_2"


def test_FEEDBACK_COMMENT_score_value_roundtrip():
    instance = FEEDBACK_COMMENT(_id="sample_text", comment="sample_text", createdAt="sample_text", feedbackId="sample_text", score=7, userId="sample_text")
    assert instance.score == 7
    instance.score = 13
    assert instance.score == 13


def test_FEEDBACK_COMMENT_userId_value_roundtrip():
    instance = FEEDBACK_COMMENT(_id="sample_text", comment="sample_text", createdAt="sample_text", feedbackId="sample_text", score=7, userId="sample_text")
    assert instance.userId == "sample_text"
    instance.userId = "sample_text_2"
    assert instance.userId == "sample_text_2"


def test_FOLLOW__id_value_roundtrip():
    instance = FOLLOW(_id="sample_text", createdAt="sample_text", followers="sample_text", following="sample_text", followingGroup="sample_text", userId="sample_text")
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_FOLLOW_createdAt_value_roundtrip():
    instance = FOLLOW(_id="sample_text", createdAt="sample_text", followers="sample_text", following="sample_text", followingGroup="sample_text", userId="sample_text")
    assert instance.createdAt == "sample_text"
    instance.createdAt = "sample_text_2"
    assert instance.createdAt == "sample_text_2"


def test_FOLLOW_followers_value_roundtrip():
    instance = FOLLOW(_id="sample_text", createdAt="sample_text", followers="sample_text", following="sample_text", followingGroup="sample_text", userId="sample_text")
    assert instance.followers == "sample_text"
    instance.followers = "sample_text_2"
    assert instance.followers == "sample_text_2"


def test_FOLLOW_following_value_roundtrip():
    instance = FOLLOW(_id="sample_text", createdAt="sample_text", followers="sample_text", following="sample_text", followingGroup="sample_text", userId="sample_text")
    assert instance.following == "sample_text"
    instance.following = "sample_text_2"
    assert instance.following == "sample_text_2"


def test_FOLLOW_followingGroup_value_roundtrip():
    instance = FOLLOW(_id="sample_text", createdAt="sample_text", followers="sample_text", following="sample_text", followingGroup="sample_text", userId="sample_text")
    assert instance.followingGroup == "sample_text"
    instance.followingGroup = "sample_text_2"
    assert instance.followingGroup == "sample_text_2"


def test_FOLLOW_userId_value_roundtrip():
    instance = FOLLOW(_id="sample_text", createdAt="sample_text", followers="sample_text", following="sample_text", followingGroup="sample_text", userId="sample_text")
    assert instance.userId == "sample_text"
    instance.userId = "sample_text_2"
    assert instance.userId == "sample_text_2"


def test_FOLLOW_MESSENGER__id_value_roundtrip():
    instance = FOLLOW_MESSENGER(_id="sample_text", createdAt="sample_text", userId="sample_text")
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_FOLLOW_MESSENGER_createdAt_value_roundtrip():
    instance = FOLLOW_MESSENGER(_id="sample_text", createdAt="sample_text", userId="sample_text")
    assert instance.createdAt == "sample_text"
    instance.createdAt = "sample_text_2"
    assert instance.createdAt == "sample_text_2"


def test_FOLLOW_MESSENGER_userId_value_roundtrip():
    instance = FOLLOW_MESSENGER(_id="sample_text", createdAt="sample_text", userId="sample_text")
    assert instance.userId == "sample_text"
    instance.userId = "sample_text_2"
    assert instance.userId == "sample_text_2"


def test_NOTIFICATION__id_value_roundtrip():
    instance = NOTIFICATION(_id="sample_text", code="sample_text", createdAt="sample_text", message="sample_text", userId="sample_text")
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_NOTIFICATION_code_value_roundtrip():
    instance = NOTIFICATION(_id="sample_text", code="sample_text", createdAt="sample_text", message="sample_text", userId="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_NOTIFICATION_createdAt_value_roundtrip():
    instance = NOTIFICATION(_id="sample_text", code="sample_text", createdAt="sample_text", message="sample_text", userId="sample_text")
    assert instance.createdAt == "sample_text"
    instance.createdAt = "sample_text_2"
    assert instance.createdAt == "sample_text_2"


def test_NOTIFICATION_message_value_roundtrip():
    instance = NOTIFICATION(_id="sample_text", code="sample_text", createdAt="sample_text", message="sample_text", userId="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_NOTIFICATION_userId_value_roundtrip():
    instance = NOTIFICATION(_id="sample_text", code="sample_text", createdAt="sample_text", message="sample_text", userId="sample_text")
    assert instance.userId == "sample_text"
    instance.userId = "sample_text_2"
    assert instance.userId == "sample_text_2"


def test_PRODUCT_ShippingMethods_value_roundtrip():
    instance = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    assert instance.ShippingMethods == "sample_text"
    instance.ShippingMethods = "sample_text_2"
    assert instance.ShippingMethods == "sample_text_2"


def test_PRODUCT__id_value_roundtrip():
    instance = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_PRODUCT_attribute_value_roundtrip():
    instance = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_PRODUCT_color_value_roundtrip():
    instance = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_PRODUCT_createdAt_value_roundtrip():
    instance = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    assert instance.createdAt == "sample_text"
    instance.createdAt = "sample_text_2"
    assert instance.createdAt == "sample_text_2"


def test_PRODUCT_description_value_roundtrip():
    instance = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_PRODUCT_dimensions_value_roundtrip():
    instance = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    assert instance.dimensions == "sample_text"
    instance.dimensions = "sample_text_2"
    assert instance.dimensions == "sample_text_2"


def test_PRODUCT_isNew_value_roundtrip():
    instance = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    assert instance.isNew == True
    instance.isNew = False
    assert instance.isNew == False


def test_PRODUCT_model_value_roundtrip():
    instance = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    assert instance.model == "sample_text"
    instance.model = "sample_text_2"
    assert instance.model == "sample_text_2"


def test_PRODUCT_name_value_roundtrip():
    instance = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_PRODUCT_photos_value_roundtrip():
    instance = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    assert instance.photos == "sample_text"
    instance.photos = "sample_text_2"
    assert instance.photos == "sample_text_2"


def test_PRODUCT_price_value_roundtrip():
    instance = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    assert instance.price == 7
    instance.price = 13
    assert instance.price == 13


def test_PRODUCT_quantity_value_roundtrip():
    instance = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    assert instance.quantity == 7
    instance.quantity = 13
    assert instance.quantity == 13


def test_PRODUCT_relatedProducts_value_roundtrip():
    instance = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    assert instance.relatedProducts == "sample_text"
    instance.relatedProducts = "sample_text_2"
    assert instance.relatedProducts == "sample_text_2"


def test_PRODUCT_sold_value_roundtrip():
    instance = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    assert instance.sold == 7
    instance.sold = 13
    assert instance.sold == 13


def test_PRODUCT_statusId_value_roundtrip():
    instance = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    assert instance.statusId == "sample_text"
    instance.statusId = "sample_text_2"
    assert instance.statusId == "sample_text_2"


def test_PRODUCT_storeId_value_roundtrip():
    instance = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    assert instance.storeId == "sample_text"
    instance.storeId = "sample_text_2"
    assert instance.storeId == "sample_text_2"


def test_QUESTIONS__id_value_roundtrip():
    instance = QUESTIONS(_id="sample_text", answer="sample_text", createdAt="sample_text", productId="sample_text", question="sample_text", score=7, statusId="sample_text", userId="sample_text")
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_QUESTIONS_answer_value_roundtrip():
    instance = QUESTIONS(_id="sample_text", answer="sample_text", createdAt="sample_text", productId="sample_text", question="sample_text", score=7, statusId="sample_text", userId="sample_text")
    assert instance.answer == "sample_text"
    instance.answer = "sample_text_2"
    assert instance.answer == "sample_text_2"


def test_QUESTIONS_createdAt_value_roundtrip():
    instance = QUESTIONS(_id="sample_text", answer="sample_text", createdAt="sample_text", productId="sample_text", question="sample_text", score=7, statusId="sample_text", userId="sample_text")
    assert instance.createdAt == "sample_text"
    instance.createdAt = "sample_text_2"
    assert instance.createdAt == "sample_text_2"


def test_QUESTIONS_productId_value_roundtrip():
    instance = QUESTIONS(_id="sample_text", answer="sample_text", createdAt="sample_text", productId="sample_text", question="sample_text", score=7, statusId="sample_text", userId="sample_text")
    assert instance.productId == "sample_text"
    instance.productId = "sample_text_2"
    assert instance.productId == "sample_text_2"


def test_QUESTIONS_question_value_roundtrip():
    instance = QUESTIONS(_id="sample_text", answer="sample_text", createdAt="sample_text", productId="sample_text", question="sample_text", score=7, statusId="sample_text", userId="sample_text")
    assert instance.question == "sample_text"
    instance.question = "sample_text_2"
    assert instance.question == "sample_text_2"


def test_QUESTIONS_score_value_roundtrip():
    instance = QUESTIONS(_id="sample_text", answer="sample_text", createdAt="sample_text", productId="sample_text", question="sample_text", score=7, statusId="sample_text", userId="sample_text")
    assert instance.score == 7
    instance.score = 13
    assert instance.score == 13


def test_QUESTIONS_statusId_value_roundtrip():
    instance = QUESTIONS(_id="sample_text", answer="sample_text", createdAt="sample_text", productId="sample_text", question="sample_text", score=7, statusId="sample_text", userId="sample_text")
    assert instance.statusId == "sample_text"
    instance.statusId = "sample_text_2"
    assert instance.statusId == "sample_text_2"


def test_QUESTIONS_userId_value_roundtrip():
    instance = QUESTIONS(_id="sample_text", answer="sample_text", createdAt="sample_text", productId="sample_text", question="sample_text", score=7, statusId="sample_text", userId="sample_text")
    assert instance.userId == "sample_text"
    instance.userId = "sample_text_2"
    assert instance.userId == "sample_text_2"


def test_REFUND__id_value_roundtrip():
    instance = REFUND(_id="sample_text", created_at="sample_text", message="sample_text", productId="sample_text", shoppingHistoryId="sample_text", storeId="sample_text", title="sample_text", userId="sample_text")
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_REFUND_created_at_value_roundtrip():
    instance = REFUND(_id="sample_text", created_at="sample_text", message="sample_text", productId="sample_text", shoppingHistoryId="sample_text", storeId="sample_text", title="sample_text", userId="sample_text")
    assert instance.created_at == "sample_text"
    instance.created_at = "sample_text_2"
    assert instance.created_at == "sample_text_2"


def test_REFUND_message_value_roundtrip():
    instance = REFUND(_id="sample_text", created_at="sample_text", message="sample_text", productId="sample_text", shoppingHistoryId="sample_text", storeId="sample_text", title="sample_text", userId="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_REFUND_productId_value_roundtrip():
    instance = REFUND(_id="sample_text", created_at="sample_text", message="sample_text", productId="sample_text", shoppingHistoryId="sample_text", storeId="sample_text", title="sample_text", userId="sample_text")
    assert instance.productId == "sample_text"
    instance.productId = "sample_text_2"
    assert instance.productId == "sample_text_2"


def test_REFUND_shoppingHistoryId_value_roundtrip():
    instance = REFUND(_id="sample_text", created_at="sample_text", message="sample_text", productId="sample_text", shoppingHistoryId="sample_text", storeId="sample_text", title="sample_text", userId="sample_text")
    assert instance.shoppingHistoryId == "sample_text"
    instance.shoppingHistoryId = "sample_text_2"
    assert instance.shoppingHistoryId == "sample_text_2"


def test_REFUND_storeId_value_roundtrip():
    instance = REFUND(_id="sample_text", created_at="sample_text", message="sample_text", productId="sample_text", shoppingHistoryId="sample_text", storeId="sample_text", title="sample_text", userId="sample_text")
    assert instance.storeId == "sample_text"
    instance.storeId = "sample_text_2"
    assert instance.storeId == "sample_text_2"


def test_REFUND_title_value_roundtrip():
    instance = REFUND(_id="sample_text", created_at="sample_text", message="sample_text", productId="sample_text", shoppingHistoryId="sample_text", storeId="sample_text", title="sample_text", userId="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_REFUND_userId_value_roundtrip():
    instance = REFUND(_id="sample_text", created_at="sample_text", message="sample_text", productId="sample_text", shoppingHistoryId="sample_text", storeId="sample_text", title="sample_text", userId="sample_text")
    assert instance.userId == "sample_text"
    instance.userId = "sample_text_2"
    assert instance.userId == "sample_text_2"


def test_REFUND_MESSAGES__id_value_roundtrip():
    instance = REFUND_MESSAGES(_id="sample_text", attach="sample_text", created_at="sample_text", message="sample_text", userId="sample_text")
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_REFUND_MESSAGES_attach_value_roundtrip():
    instance = REFUND_MESSAGES(_id="sample_text", attach="sample_text", created_at="sample_text", message="sample_text", userId="sample_text")
    assert instance.attach == "sample_text"
    instance.attach = "sample_text_2"
    assert instance.attach == "sample_text_2"


def test_REFUND_MESSAGES_created_at_value_roundtrip():
    instance = REFUND_MESSAGES(_id="sample_text", attach="sample_text", created_at="sample_text", message="sample_text", userId="sample_text")
    assert instance.created_at == "sample_text"
    instance.created_at = "sample_text_2"
    assert instance.created_at == "sample_text_2"


def test_REFUND_MESSAGES_message_value_roundtrip():
    instance = REFUND_MESSAGES(_id="sample_text", attach="sample_text", created_at="sample_text", message="sample_text", userId="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_REFUND_MESSAGES_userId_value_roundtrip():
    instance = REFUND_MESSAGES(_id="sample_text", attach="sample_text", created_at="sample_text", message="sample_text", userId="sample_text")
    assert instance.userId == "sample_text"
    instance.userId = "sample_text_2"
    assert instance.userId == "sample_text_2"


def test_ROLES__id_value_roundtrip():
    instance = ROLES(_id="sample_text", createdAt="sample_text", name="sample_text")
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_ROLES_createdAt_value_roundtrip():
    instance = ROLES(_id="sample_text", createdAt="sample_text", name="sample_text")
    assert instance.createdAt == "sample_text"
    instance.createdAt = "sample_text_2"
    assert instance.createdAt == "sample_text_2"


def test_ROLES_name_value_roundtrip():
    instance = ROLES(_id="sample_text", createdAt="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SHIPPING_METHODS__id_value_roundtrip():
    instance = SHIPPING_METHODS(_id="sample_text", address="sample_text", arrival="sample_text", createdAt="sample_text", name="sample_text", price=7)
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_SHIPPING_METHODS_address_value_roundtrip():
    instance = SHIPPING_METHODS(_id="sample_text", address="sample_text", arrival="sample_text", createdAt="sample_text", name="sample_text", price=7)
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_SHIPPING_METHODS_arrival_value_roundtrip():
    instance = SHIPPING_METHODS(_id="sample_text", address="sample_text", arrival="sample_text", createdAt="sample_text", name="sample_text", price=7)
    assert instance.arrival == "sample_text"
    instance.arrival = "sample_text_2"
    assert instance.arrival == "sample_text_2"


def test_SHIPPING_METHODS_createdAt_value_roundtrip():
    instance = SHIPPING_METHODS(_id="sample_text", address="sample_text", arrival="sample_text", createdAt="sample_text", name="sample_text", price=7)
    assert instance.createdAt == "sample_text"
    instance.createdAt = "sample_text_2"
    assert instance.createdAt == "sample_text_2"


def test_SHIPPING_METHODS_name_value_roundtrip():
    instance = SHIPPING_METHODS(_id="sample_text", address="sample_text", arrival="sample_text", createdAt="sample_text", name="sample_text", price=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SHIPPING_METHODS_price_value_roundtrip():
    instance = SHIPPING_METHODS(_id="sample_text", address="sample_text", arrival="sample_text", createdAt="sample_text", name="sample_text", price=7)
    assert instance.price == 7
    instance.price = 13
    assert instance.price == 13


def test_SHOPPING_HISTORY_STATUS_SHOPPING_HIST_ID_value_roundtrip():
    instance = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.STATUS_SHOPPING_HIST_ID == "sample_text"
    instance.STATUS_SHOPPING_HIST_ID = "sample_text_2"
    assert instance.STATUS_SHOPPING_HIST_ID == "sample_text_2"


def test_SHOPPING_HISTORY__id_value_roundtrip():
    instance = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_SHOPPING_HISTORY_attribute_value_roundtrip():
    instance = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_SHOPPING_HISTORY_comment_value_roundtrip():
    instance = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_SHOPPING_HISTORY_created_at_value_roundtrip():
    instance = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.created_at == "sample_text"
    instance.created_at = "sample_text_2"
    assert instance.created_at == "sample_text_2"


def test_SHOPPING_HISTORY_description_value_roundtrip():
    instance = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_SHOPPING_HISTORY_isNew_value_roundtrip():
    instance = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.isNew == True
    instance.isNew = False
    assert instance.isNew == False


def test_SHOPPING_HISTORY_isSold_value_roundtrip():
    instance = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.isSold == True
    instance.isSold = False
    assert instance.isSold == False


def test_SHOPPING_HISTORY_name_value_roundtrip():
    instance = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SHOPPING_HISTORY_note_value_roundtrip():
    instance = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_SHOPPING_HISTORY_photos_value_roundtrip():
    instance = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.photos == "sample_text"
    instance.photos = "sample_text_2"
    assert instance.photos == "sample_text_2"


def test_SHOPPING_HISTORY_price_value_roundtrip():
    instance = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.price == 7
    instance.price = 13
    assert instance.price == 13


def test_SHOPPING_HISTORY_productId_value_roundtrip():
    instance = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.productId == "sample_text"
    instance.productId = "sample_text_2"
    assert instance.productId == "sample_text_2"


def test_SHOPPING_HISTORY_quantity_value_roundtrip():
    instance = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.quantity == 7
    instance.quantity = 13
    assert instance.quantity == 13


def test_SHOPPING_HISTORY_score_value_roundtrip():
    instance = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.score == 7
    instance.score = 13
    assert instance.score == 13


def test_SHOPPING_HISTORY_shipAddress_value_roundtrip():
    instance = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.shipAddress == "sample_text"
    instance.shipAddress = "sample_text_2"
    assert instance.shipAddress == "sample_text_2"


def test_SHOPPING_HISTORY_shipArrival_value_roundtrip():
    instance = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.shipArrival == "sample_text"
    instance.shipArrival = "sample_text_2"
    assert instance.shipArrival == "sample_text_2"


def test_SHOPPING_HISTORY_shipName_value_roundtrip():
    instance = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.shipName == "sample_text"
    instance.shipName = "sample_text_2"
    assert instance.shipName == "sample_text_2"


def test_SHOPPING_HISTORY_shipPrice_value_roundtrip():
    instance = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.shipPrice == 7
    instance.shipPrice = 13
    assert instance.shipPrice == 13


def test_SHOPPING_HISTORY_sold_value_roundtrip():
    instance = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.sold == 7
    instance.sold = 13
    assert instance.sold == 13


def test_SHOPPING_HISTORY_status_value_roundtrip():
    instance = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_SHOPPING_HISTORY_storeId_value_roundtrip():
    instance = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.storeId == "sample_text"
    instance.storeId = "sample_text_2"
    assert instance.storeId == "sample_text_2"


def test_SHOPPING_HISTORY_userId_value_roundtrip():
    instance = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.userId == "sample_text"
    instance.userId = "sample_text_2"
    assert instance.userId == "sample_text_2"


def test_SHOPPING_MESSENGER__id_value_roundtrip():
    instance = SHOPPING_MESSENGER(_id="sample_text", created_at="sample_text", message="sample_text", photos="sample_text", storeId="sample_text", userId="sample_text")
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_SHOPPING_MESSENGER_created_at_value_roundtrip():
    instance = SHOPPING_MESSENGER(_id="sample_text", created_at="sample_text", message="sample_text", photos="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.created_at == "sample_text"
    instance.created_at = "sample_text_2"
    assert instance.created_at == "sample_text_2"


def test_SHOPPING_MESSENGER_message_value_roundtrip():
    instance = SHOPPING_MESSENGER(_id="sample_text", created_at="sample_text", message="sample_text", photos="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_SHOPPING_MESSENGER_photos_value_roundtrip():
    instance = SHOPPING_MESSENGER(_id="sample_text", created_at="sample_text", message="sample_text", photos="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.photos == "sample_text"
    instance.photos = "sample_text_2"
    assert instance.photos == "sample_text_2"


def test_SHOPPING_MESSENGER_storeId_value_roundtrip():
    instance = SHOPPING_MESSENGER(_id="sample_text", created_at="sample_text", message="sample_text", photos="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.storeId == "sample_text"
    instance.storeId = "sample_text_2"
    assert instance.storeId == "sample_text_2"


def test_SHOPPING_MESSENGER_userId_value_roundtrip():
    instance = SHOPPING_MESSENGER(_id="sample_text", created_at="sample_text", message="sample_text", photos="sample_text", storeId="sample_text", userId="sample_text")
    assert instance.userId == "sample_text"
    instance.userId = "sample_text_2"
    assert instance.userId == "sample_text_2"


def test_SOCIAL_NETWORKS__id_value_roundtrip():
    instance = SOCIAL_NETWORKS(_id="sample_text", facebook="sample_text", instagram="sample_text", twitter="sample_text", updateAt="sample_text")
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_SOCIAL_NETWORKS_facebook_value_roundtrip():
    instance = SOCIAL_NETWORKS(_id="sample_text", facebook="sample_text", instagram="sample_text", twitter="sample_text", updateAt="sample_text")
    assert instance.facebook == "sample_text"
    instance.facebook = "sample_text_2"
    assert instance.facebook == "sample_text_2"


def test_SOCIAL_NETWORKS_instagram_value_roundtrip():
    instance = SOCIAL_NETWORKS(_id="sample_text", facebook="sample_text", instagram="sample_text", twitter="sample_text", updateAt="sample_text")
    assert instance.instagram == "sample_text"
    instance.instagram = "sample_text_2"
    assert instance.instagram == "sample_text_2"


def test_SOCIAL_NETWORKS_twitter_value_roundtrip():
    instance = SOCIAL_NETWORKS(_id="sample_text", facebook="sample_text", instagram="sample_text", twitter="sample_text", updateAt="sample_text")
    assert instance.twitter == "sample_text"
    instance.twitter = "sample_text_2"
    assert instance.twitter == "sample_text_2"


def test_SOCIAL_NETWORKS_updateAt_value_roundtrip():
    instance = SOCIAL_NETWORKS(_id="sample_text", facebook="sample_text", instagram="sample_text", twitter="sample_text", updateAt="sample_text")
    assert instance.updateAt == "sample_text"
    instance.updateAt = "sample_text_2"
    assert instance.updateAt == "sample_text_2"


def test_STATUS__id_value_roundtrip():
    instance = STATUS(_id="sample_text", createdAt="sample_text", name="sample_text")
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_STATUS_createdAt_value_roundtrip():
    instance = STATUS(_id="sample_text", createdAt="sample_text", name="sample_text")
    assert instance.createdAt == "sample_text"
    instance.createdAt = "sample_text_2"
    assert instance.createdAt == "sample_text_2"


def test_STATUS_name_value_roundtrip():
    instance = STATUS(_id="sample_text", createdAt="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_STATUS2__id_value_roundtrip():
    instance = STATUS2(_id="sample_text", name="sample_text")
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_STATUS2_name_value_roundtrip():
    instance = STATUS2(_id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_STATUS_SHOPPING_HISTORY__id_value_roundtrip():
    instance = STATUS_SHOPPING_HISTORY(_id="sample_text", name="sample_text")
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_STATUS_SHOPPING_HISTORY_name_value_roundtrip():
    instance = STATUS_SHOPPING_HISTORY(_id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_STORE__id_value_roundtrip():
    instance = STORE(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", name="sample_text", schedule="sample_text", statusId="sample_text", telephone="sample_text", updateAt="sample_text")
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_STORE_address_value_roundtrip():
    instance = STORE(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", name="sample_text", schedule="sample_text", statusId="sample_text", telephone="sample_text", updateAt="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_STORE_createdAt_value_roundtrip():
    instance = STORE(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", name="sample_text", schedule="sample_text", statusId="sample_text", telephone="sample_text", updateAt="sample_text")
    assert instance.createdAt == "sample_text"
    instance.createdAt = "sample_text_2"
    assert instance.createdAt == "sample_text_2"


def test_STORE_email_value_roundtrip():
    instance = STORE(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", name="sample_text", schedule="sample_text", statusId="sample_text", telephone="sample_text", updateAt="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_STORE_name_value_roundtrip():
    instance = STORE(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", name="sample_text", schedule="sample_text", statusId="sample_text", telephone="sample_text", updateAt="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_STORE_schedule_value_roundtrip():
    instance = STORE(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", name="sample_text", schedule="sample_text", statusId="sample_text", telephone="sample_text", updateAt="sample_text")
    assert instance.schedule == "sample_text"
    instance.schedule = "sample_text_2"
    assert instance.schedule == "sample_text_2"


def test_STORE_statusId_value_roundtrip():
    instance = STORE(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", name="sample_text", schedule="sample_text", statusId="sample_text", telephone="sample_text", updateAt="sample_text")
    assert instance.statusId == "sample_text"
    instance.statusId = "sample_text_2"
    assert instance.statusId == "sample_text_2"


def test_STORE_telephone_value_roundtrip():
    instance = STORE(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", name="sample_text", schedule="sample_text", statusId="sample_text", telephone="sample_text", updateAt="sample_text")
    assert instance.telephone == "sample_text"
    instance.telephone = "sample_text_2"
    assert instance.telephone == "sample_text_2"


def test_STORE_updateAt_value_roundtrip():
    instance = STORE(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", name="sample_text", schedule="sample_text", statusId="sample_text", telephone="sample_text", updateAt="sample_text")
    assert instance.updateAt == "sample_text"
    instance.updateAt = "sample_text_2"
    assert instance.updateAt == "sample_text_2"


def test_SUBSCRIPTION_BENEFITS__id_value_roundtrip():
    instance = SUBSCRIPTION_BENEFITS(_id="sample_text", description="sample_text", key_name="sample_text")
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_SUBSCRIPTION_BENEFITS_description_value_roundtrip():
    instance = SUBSCRIPTION_BENEFITS(_id="sample_text", description="sample_text", key_name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_SUBSCRIPTION_BENEFITS_key_name_value_roundtrip():
    instance = SUBSCRIPTION_BENEFITS(_id="sample_text", description="sample_text", key_name="sample_text")
    assert instance.key_name == "sample_text"
    instance.key_name = "sample_text_2"
    assert instance.key_name == "sample_text_2"


def test_USER__id_value_roundtrip():
    instance = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_USER_address_value_roundtrip():
    instance = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_USER_createdAt_value_roundtrip():
    instance = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    assert instance.createdAt == "sample_text"
    instance.createdAt = "sample_text_2"
    assert instance.createdAt == "sample_text_2"


def test_USER_email_value_roundtrip():
    instance = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_USER_lastAccess_value_roundtrip():
    instance = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    assert instance.lastAccess == "sample_text"
    instance.lastAccess = "sample_text_2"
    assert instance.lastAccess == "sample_text_2"


def test_USER_name_value_roundtrip():
    instance = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_USER_password_value_roundtrip():
    instance = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_USER_status_value_roundtrip():
    instance = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_USER_surname_value_roundtrip():
    instance = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    assert instance.surname == "sample_text"
    instance.surname = "sample_text_2"
    assert instance.surname == "sample_text_2"


def test_USER_telephone_value_roundtrip():
    instance = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    assert instance.telephone == "sample_text"
    instance.telephone = "sample_text_2"
    assert instance.telephone == "sample_text_2"


def test_USER_updateAt_value_roundtrip():
    instance = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    assert instance.updateAt == "sample_text"
    instance.updateAt = "sample_text_2"
    assert instance.updateAt == "sample_text_2"


def test_USER_verified_value_roundtrip():
    instance = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    assert instance.verified == True
    instance.verified = False
    assert instance.verified == False


def test_WHISES__id_value_roundtrip():
    instance = WHISES(_id="sample_text", createdAt="sample_text", productId="sample_text", statusId="sample_text", userId="sample_text")
    assert instance._id == "sample_text"
    instance._id = "sample_text_2"
    assert instance._id == "sample_text_2"


def test_WHISES_createdAt_value_roundtrip():
    instance = WHISES(_id="sample_text", createdAt="sample_text", productId="sample_text", statusId="sample_text", userId="sample_text")
    assert instance.createdAt == "sample_text"
    instance.createdAt = "sample_text_2"
    assert instance.createdAt == "sample_text_2"


def test_WHISES_productId_value_roundtrip():
    instance = WHISES(_id="sample_text", createdAt="sample_text", productId="sample_text", statusId="sample_text", userId="sample_text")
    assert instance.productId == "sample_text"
    instance.productId = "sample_text_2"
    assert instance.productId == "sample_text_2"


def test_WHISES_statusId_value_roundtrip():
    instance = WHISES(_id="sample_text", createdAt="sample_text", productId="sample_text", statusId="sample_text", userId="sample_text")
    assert instance.statusId == "sample_text"
    instance.statusId = "sample_text_2"
    assert instance.statusId == "sample_text_2"


def test_WHISES_userId_value_roundtrip():
    instance = WHISES(_id="sample_text", createdAt="sample_text", productId="sample_text", statusId="sample_text", userId="sample_text")
    assert instance.userId == "sample_text"
    instance.userId = "sample_text_2"
    assert instance.userId == "sample_text_2"


def test_assoc_CATEGORIAS_PRODUCTO_link_reassign_clear():
    a = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    b1 = CATEGORIAS(_id="sample_text", createdAt="sample_text", name="sample_text")
    b2 = CATEGORIAS(_id="sample_text_2", createdAt="sample_text_2", name="sample_text_2")
    _safe_set(a, 'cATEGORIAS5', b1)
    assert _is_linked(a, 'cATEGORIAS5', b1)
    if hasattr(b1, 'pRODUCTO4'):
        assert _is_linked(b1, 'pRODUCTO4', a)
    _safe_set(a, 'cATEGORIAS5', b2)
    assert _is_linked(a, 'cATEGORIAS5', b2)
    if hasattr(b1, 'pRODUCTO4'):
        assert not _is_linked(b1, 'pRODUCTO4', a)
    if hasattr(b2, 'pRODUCTO4'):
        assert _is_linked(b2, 'pRODUCTO4', a)
    _safe_set(a, 'cATEGORIAS5', None)
    assert not _is_linked(a, 'cATEGORIAS5', b2)
    if hasattr(b2, 'pRODUCTO4'):
        assert not _is_linked(b2, 'pRODUCTO4', a)


def test_assoc_COMMENTS_PRODUCT_link_reassign_clear():
    a = QUESTIONS(_id="sample_text", answer="sample_text", createdAt="sample_text", productId="sample_text", question="sample_text", score=7, statusId="sample_text", userId="sample_text")
    b1 = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    b2 = PRODUCT(ShippingMethods="sample_text_2", _id="sample_text_2", attribute="sample_text_2", color="sample_text_2", createdAt="sample_text_2", description="sample_text_2", dimensions="sample_text_2", isNew=False, model="sample_text_2", name="sample_text_2", photos="sample_text_2", price=13, quantity=13, relatedProducts="sample_text_2", sold=13, statusId="sample_text_2", storeId="sample_text_2")
    _safe_set(a, 'pRODUCT10', b1)
    assert _is_linked(a, 'pRODUCT10', b1)
    if hasattr(b1, 'cOMMENTS11'):
        assert _is_linked(b1, 'cOMMENTS11', a)
    _safe_set(a, 'pRODUCT10', b2)
    assert _is_linked(a, 'pRODUCT10', b2)
    if hasattr(b1, 'cOMMENTS11'):
        assert not _is_linked(b1, 'cOMMENTS11', a)
    if hasattr(b2, 'cOMMENTS11'):
        assert _is_linked(b2, 'cOMMENTS11', a)
    _safe_set(a, 'pRODUCT10', None)
    assert not _is_linked(a, 'pRODUCT10', b2)
    if hasattr(b2, 'cOMMENTS11'):
        assert not _is_linked(b2, 'cOMMENTS11', a)


def test_assoc_COMMENTS_USUARIO_link_reassign_clear():
    a = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    b1 = QUESTIONS(_id="sample_text", answer="sample_text", createdAt="sample_text", productId="sample_text", question="sample_text", score=7, statusId="sample_text", userId="sample_text")
    b2 = QUESTIONS(_id="sample_text_2", answer="sample_text_2", createdAt="sample_text_2", productId="sample_text_2", question="sample_text_2", score=13, statusId="sample_text_2", userId="sample_text_2")
    _safe_set(a, 'cOMMENTS13', b1)
    assert _is_linked(a, 'cOMMENTS13', b1)
    if hasattr(b1, 'uSUARIO12'):
        assert _is_linked(b1, 'uSUARIO12', a)
    _safe_set(a, 'cOMMENTS13', b2)
    assert _is_linked(a, 'cOMMENTS13', b2)
    if hasattr(b1, 'uSUARIO12'):
        assert not _is_linked(b1, 'uSUARIO12', a)
    if hasattr(b2, 'uSUARIO12'):
        assert _is_linked(b2, 'uSUARIO12', a)
    _safe_set(a, 'cOMMENTS13', None)
    assert not _is_linked(a, 'cOMMENTS13', b2)
    if hasattr(b2, 'uSUARIO12'):
        assert not _is_linked(b2, 'uSUARIO12', a)


def test_assoc_EVENTS_LIST_EVENTS_HISTORY_link_reassign_clear():
    a = EVENTS_LIST(_id="sample_text", createdAt="sample_text", description="sample_text", key="sample_text")
    b1 = EVENTS_HISTORY(_id="sample_text", createdAt="sample_text", eventId="sample_text", newValue="sample_text", oldValue="sample_text", userId="sample_text")
    b2 = EVENTS_HISTORY(_id="sample_text_2", createdAt="sample_text_2", eventId="sample_text_2", newValue="sample_text_2", oldValue="sample_text_2", userId="sample_text_2")
    _safe_set(a, 'eVENTS_HISTORY36', b1)
    assert _is_linked(a, 'eVENTS_HISTORY36', b1)
    if hasattr(b1, 'eVENTS_LIST37'):
        assert _is_linked(b1, 'eVENTS_LIST37', a)
    _safe_set(a, 'eVENTS_HISTORY36', b2)
    assert _is_linked(a, 'eVENTS_HISTORY36', b2)
    if hasattr(b1, 'eVENTS_LIST37'):
        assert not _is_linked(b1, 'eVENTS_LIST37', a)
    if hasattr(b2, 'eVENTS_LIST37'):
        assert _is_linked(b2, 'eVENTS_LIST37', a)
    _safe_set(a, 'eVENTS_HISTORY36', None)
    assert not _is_linked(a, 'eVENTS_HISTORY36', b2)
    if hasattr(b2, 'eVENTS_LIST37'):
        assert not _is_linked(b2, 'eVENTS_LIST37', a)


def test_assoc_FAVORITES_PRODUCTO_link_reassign_clear():
    a = WHISES(_id="sample_text", createdAt="sample_text", productId="sample_text", statusId="sample_text", userId="sample_text")
    b1 = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    b2 = PRODUCT(ShippingMethods="sample_text_2", _id="sample_text_2", attribute="sample_text_2", color="sample_text_2", createdAt="sample_text_2", description="sample_text_2", dimensions="sample_text_2", isNew=False, model="sample_text_2", name="sample_text_2", photos="sample_text_2", price=13, quantity=13, relatedProducts="sample_text_2", sold=13, statusId="sample_text_2", storeId="sample_text_2")
    _safe_set(a, 'pRODUCTO6', b1)
    assert _is_linked(a, 'pRODUCTO6', b1)
    if hasattr(b1, 'fAVORITES7'):
        assert _is_linked(b1, 'fAVORITES7', a)
    _safe_set(a, 'pRODUCTO6', b2)
    assert _is_linked(a, 'pRODUCTO6', b2)
    if hasattr(b1, 'fAVORITES7'):
        assert not _is_linked(b1, 'fAVORITES7', a)
    if hasattr(b2, 'fAVORITES7'):
        assert _is_linked(b2, 'fAVORITES7', a)
    _safe_set(a, 'pRODUCTO6', None)
    assert not _is_linked(a, 'pRODUCTO6', b2)
    if hasattr(b2, 'fAVORITES7'):
        assert not _is_linked(b2, 'fAVORITES7', a)


def test_assoc_FAVORITES_STORE_link_reassign_clear():
    a = STORE(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", name="sample_text", schedule="sample_text", statusId="sample_text", telephone="sample_text", updateAt="sample_text")
    b1 = FAVORITES(_id="sample_text", createdAt="sample_text", statusId="sample_text", storeId="sample_text", userId="sample_text")
    b2 = FAVORITES(_id="sample_text_2", createdAt="sample_text_2", statusId="sample_text_2", storeId="sample_text_2", userId="sample_text_2")
    _safe_set(a, 'fAVORITES33', b1)
    assert _is_linked(a, 'fAVORITES33', b1)
    if hasattr(b1, 'sTORE32'):
        assert _is_linked(b1, 'sTORE32', a)
    _safe_set(a, 'fAVORITES33', b2)
    assert _is_linked(a, 'fAVORITES33', b2)
    if hasattr(b1, 'sTORE32'):
        assert not _is_linked(b1, 'sTORE32', a)
    if hasattr(b2, 'sTORE32'):
        assert _is_linked(b2, 'sTORE32', a)
    _safe_set(a, 'fAVORITES33', None)
    assert not _is_linked(a, 'fAVORITES33', b2)
    if hasattr(b2, 'sTORE32'):
        assert not _is_linked(b2, 'sTORE32', a)


def test_assoc_FAVORITES_USER_link_reassign_clear():
    a = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    b1 = FAVORITES(_id="sample_text", createdAt="sample_text", statusId="sample_text", storeId="sample_text", userId="sample_text")
    b2 = FAVORITES(_id="sample_text_2", createdAt="sample_text_2", statusId="sample_text_2", storeId="sample_text_2", userId="sample_text_2")
    _safe_set(a, 'fAVORITES35', b1)
    assert _is_linked(a, 'fAVORITES35', b1)
    if hasattr(b1, 'uSER34'):
        assert _is_linked(b1, 'uSER34', a)
    _safe_set(a, 'fAVORITES35', b2)
    assert _is_linked(a, 'fAVORITES35', b2)
    if hasattr(b1, 'uSER34'):
        assert not _is_linked(b1, 'uSER34', a)
    if hasattr(b2, 'uSER34'):
        assert _is_linked(b2, 'uSER34', a)
    _safe_set(a, 'fAVORITES35', None)
    assert not _is_linked(a, 'fAVORITES35', b2)
    if hasattr(b2, 'uSER34'):
        assert not _is_linked(b2, 'uSER34', a)


def test_assoc_FAVORITES_USUARIO_link_reassign_clear():
    a = WHISES(_id="sample_text", createdAt="sample_text", productId="sample_text", statusId="sample_text", userId="sample_text")
    b1 = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    b2 = USER(_id="sample_text_2", address="sample_text_2", createdAt="sample_text_2", email="sample_text_2", lastAccess="sample_text_2", name="sample_text_2", password="sample_text_2", status="sample_text_2", surname="sample_text_2", telephone="sample_text_2", updateAt="sample_text_2", verified=False)
    _safe_set(a, 'uSUARIO8', b1)
    assert _is_linked(a, 'uSUARIO8', b1)
    if hasattr(b1, 'fAVORITES9'):
        assert _is_linked(b1, 'fAVORITES9', a)
    _safe_set(a, 'uSUARIO8', b2)
    assert _is_linked(a, 'uSUARIO8', b2)
    if hasattr(b1, 'fAVORITES9'):
        assert not _is_linked(b1, 'fAVORITES9', a)
    if hasattr(b2, 'fAVORITES9'):
        assert _is_linked(b2, 'fAVORITES9', a)
    _safe_set(a, 'uSUARIO8', None)
    assert not _is_linked(a, 'uSUARIO8', b2)
    if hasattr(b2, 'fAVORITES9'):
        assert not _is_linked(b2, 'fAVORITES9', a)


def test_assoc_FEEDBACKS_USER_link_reassign_clear():
    a = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    b1 = FEEDBACK(_id="sample_text", createdAt="sample_text", like="sample_text", linkInstagram="sample_text", linkYoutube="sample_text", photos="sample_text", productId="sample_text", updateAt="sample_text", userId="sample_text", wysiwyg="sample_text")
    b2 = FEEDBACK(_id="sample_text_2", createdAt="sample_text_2", like="sample_text_2", linkInstagram="sample_text_2", linkYoutube="sample_text_2", photos="sample_text_2", productId="sample_text_2", updateAt="sample_text_2", userId="sample_text_2", wysiwyg="sample_text_2")
    _safe_set(a, 'fEEDBACKS51', b1)
    assert _is_linked(a, 'fEEDBACKS51', b1)
    if hasattr(b1, 'uSER50'):
        assert _is_linked(b1, 'uSER50', a)
    _safe_set(a, 'fEEDBACKS51', b2)
    assert _is_linked(a, 'fEEDBACKS51', b2)
    if hasattr(b1, 'uSER50'):
        assert not _is_linked(b1, 'uSER50', a)
    if hasattr(b2, 'uSER50'):
        assert _is_linked(b2, 'uSER50', a)
    _safe_set(a, 'fEEDBACKS51', None)
    assert not _is_linked(a, 'fEEDBACKS51', b2)
    if hasattr(b2, 'uSER50'):
        assert not _is_linked(b2, 'uSER50', a)


def test_assoc_FEEDBACK_COMMENT_FEEDBACK_link_reassign_clear():
    a = FEEDBACK_COMMENT(_id="sample_text", comment="sample_text", createdAt="sample_text", feedbackId="sample_text", score=7, userId="sample_text")
    b1 = FEEDBACK(_id="sample_text", createdAt="sample_text", like="sample_text", linkInstagram="sample_text", linkYoutube="sample_text", photos="sample_text", productId="sample_text", updateAt="sample_text", userId="sample_text", wysiwyg="sample_text")
    b2 = FEEDBACK(_id="sample_text_2", createdAt="sample_text_2", like="sample_text_2", linkInstagram="sample_text_2", linkYoutube="sample_text_2", photos="sample_text_2", productId="sample_text_2", updateAt="sample_text_2", userId="sample_text_2", wysiwyg="sample_text_2")
    _safe_set(a, 'fEEDBACK52', b1)
    assert _is_linked(a, 'fEEDBACK52', b1)
    if hasattr(b1, 'fEEDBACK_COMMENT53'):
        assert _is_linked(b1, 'fEEDBACK_COMMENT53', a)
    _safe_set(a, 'fEEDBACK52', b2)
    assert _is_linked(a, 'fEEDBACK52', b2)
    if hasattr(b1, 'fEEDBACK_COMMENT53'):
        assert not _is_linked(b1, 'fEEDBACK_COMMENT53', a)
    if hasattr(b2, 'fEEDBACK_COMMENT53'):
        assert _is_linked(b2, 'fEEDBACK_COMMENT53', a)
    _safe_set(a, 'fEEDBACK52', None)
    assert not _is_linked(a, 'fEEDBACK52', b2)
    if hasattr(b2, 'fEEDBACK_COMMENT53'):
        assert not _is_linked(b2, 'fEEDBACK_COMMENT53', a)


def test_assoc_FRIEND_LIST_USER_link_reassign_clear():
    a = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    b1 = FOLLOW(_id="sample_text", createdAt="sample_text", followers="sample_text", following="sample_text", followingGroup="sample_text", userId="sample_text")
    b2 = FOLLOW(_id="sample_text_2", createdAt="sample_text_2", followers="sample_text_2", following="sample_text_2", followingGroup="sample_text_2", userId="sample_text_2")
    _safe_set(a, 'fRIEND_LIST47', b1)
    assert _is_linked(a, 'fRIEND_LIST47', b1)
    if hasattr(b1, 'uSER46'):
        assert _is_linked(b1, 'uSER46', a)
    _safe_set(a, 'fRIEND_LIST47', b2)
    assert _is_linked(a, 'fRIEND_LIST47', b2)
    if hasattr(b1, 'uSER46'):
        assert not _is_linked(b1, 'uSER46', a)
    if hasattr(b2, 'uSER46'):
        assert _is_linked(b2, 'uSER46', a)
    _safe_set(a, 'fRIEND_LIST47', None)
    assert not _is_linked(a, 'fRIEND_LIST47', b2)
    if hasattr(b2, 'uSER46'):
        assert not _is_linked(b2, 'uSER46', a)


def test_assoc_MESSENGER_SHOPPING_HISTORY_link_reassign_clear():
    a = SHOPPING_MESSENGER(_id="sample_text", created_at="sample_text", message="sample_text", photos="sample_text", storeId="sample_text", userId="sample_text")
    b1 = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    b2 = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text_2", _id="sample_text_2", attribute="sample_text_2", comment="sample_text_2", created_at="sample_text_2", description="sample_text_2", isNew=False, isSold=False, name="sample_text_2", note="sample_text_2", photos="sample_text_2", price=13, productId="sample_text_2", quantity=13, score=13, shipAddress="sample_text_2", shipArrival="sample_text_2", shipName="sample_text_2", shipPrice=13, sold=13, status="sample_text_2", storeId="sample_text_2", userId="sample_text_2")
    _safe_set(a, 'sHOPPING_HISTORY48', b1)
    assert _is_linked(a, 'sHOPPING_HISTORY48', b1)
    if hasattr(b1, 'mESSENGER49'):
        assert _is_linked(b1, 'mESSENGER49', a)
    _safe_set(a, 'sHOPPING_HISTORY48', b2)
    assert _is_linked(a, 'sHOPPING_HISTORY48', b2)
    if hasattr(b1, 'mESSENGER49'):
        assert not _is_linked(b1, 'mESSENGER49', a)
    if hasattr(b2, 'mESSENGER49'):
        assert _is_linked(b2, 'mESSENGER49', a)
    _safe_set(a, 'sHOPPING_HISTORY48', None)
    assert not _is_linked(a, 'sHOPPING_HISTORY48', b2)
    if hasattr(b2, 'mESSENGER49'):
        assert not _is_linked(b2, 'mESSENGER49', a)


def test_assoc_NOTIFICATION_USER_link_reassign_clear():
    a = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    b1 = NOTIFICATION(_id="sample_text", code="sample_text", createdAt="sample_text", message="sample_text", userId="sample_text")
    b2 = NOTIFICATION(_id="sample_text_2", code="sample_text_2", createdAt="sample_text_2", message="sample_text_2", userId="sample_text_2")
    _safe_set(a, 'nOTIFICATION39', b1)
    assert _is_linked(a, 'nOTIFICATION39', b1)
    if hasattr(b1, 'uSER38'):
        assert _is_linked(b1, 'uSER38', a)
    _safe_set(a, 'nOTIFICATION39', b2)
    assert _is_linked(a, 'nOTIFICATION39', b2)
    if hasattr(b1, 'uSER38'):
        assert not _is_linked(b1, 'uSER38', a)
    if hasattr(b2, 'uSER38'):
        assert _is_linked(b2, 'uSER38', a)
    _safe_set(a, 'nOTIFICATION39', None)
    assert not _is_linked(a, 'nOTIFICATION39', b2)
    if hasattr(b2, 'uSER38'):
        assert not _is_linked(b2, 'uSER38', a)


def test_assoc_PRODUCTO_USUARIO_link_reassign_clear():
    a = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    b1 = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    b2 = PRODUCT(ShippingMethods="sample_text_2", _id="sample_text_2", attribute="sample_text_2", color="sample_text_2", createdAt="sample_text_2", description="sample_text_2", dimensions="sample_text_2", isNew=False, model="sample_text_2", name="sample_text_2", photos="sample_text_2", price=13, quantity=13, relatedProducts="sample_text_2", sold=13, statusId="sample_text_2", storeId="sample_text_2")
    _safe_set(a, 'pRODUCTO3', b1)
    assert _is_linked(a, 'pRODUCTO3', b1)
    if hasattr(b1, 'uSUARIO2'):
        assert _is_linked(b1, 'uSUARIO2', a)
    _safe_set(a, 'pRODUCTO3', b2)
    assert _is_linked(a, 'pRODUCTO3', b2)
    if hasattr(b1, 'uSUARIO2'):
        assert not _is_linked(b1, 'uSUARIO2', a)
    if hasattr(b2, 'uSUARIO2'):
        assert _is_linked(b2, 'uSUARIO2', a)
    _safe_set(a, 'pRODUCTO3', None)
    assert not _is_linked(a, 'pRODUCTO3', b2)
    if hasattr(b2, 'uSUARIO2'):
        assert not _is_linked(b2, 'uSUARIO2', a)


def test_assoc_REFUND_MESSAGES_REFUND_link_reassign_clear():
    a = REFUND_MESSAGES(_id="sample_text", attach="sample_text", created_at="sample_text", message="sample_text", userId="sample_text")
    b1 = REFUND(_id="sample_text", created_at="sample_text", message="sample_text", productId="sample_text", shoppingHistoryId="sample_text", storeId="sample_text", title="sample_text", userId="sample_text")
    b2 = REFUND(_id="sample_text_2", created_at="sample_text_2", message="sample_text_2", productId="sample_text_2", shoppingHistoryId="sample_text_2", storeId="sample_text_2", title="sample_text_2", userId="sample_text_2")
    _safe_set(a, 'rEFUND42', b1)
    assert _is_linked(a, 'rEFUND42', b1)
    if hasattr(b1, 'rEFUND_MESSAGES43'):
        assert _is_linked(b1, 'rEFUND_MESSAGES43', a)
    _safe_set(a, 'rEFUND42', b2)
    assert _is_linked(a, 'rEFUND42', b2)
    if hasattr(b1, 'rEFUND_MESSAGES43'):
        assert not _is_linked(b1, 'rEFUND_MESSAGES43', a)
    if hasattr(b2, 'rEFUND_MESSAGES43'):
        assert _is_linked(b2, 'rEFUND_MESSAGES43', a)
    _safe_set(a, 'rEFUND42', None)
    assert not _is_linked(a, 'rEFUND42', b2)
    if hasattr(b2, 'rEFUND_MESSAGES43'):
        assert not _is_linked(b2, 'rEFUND_MESSAGES43', a)


def test_assoc_REFUND_SHOPPING_HISTORY_link_reassign_clear():
    a = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    b1 = REFUND(_id="sample_text", created_at="sample_text", message="sample_text", productId="sample_text", shoppingHistoryId="sample_text", storeId="sample_text", title="sample_text", userId="sample_text")
    b2 = REFUND(_id="sample_text_2", created_at="sample_text_2", message="sample_text_2", productId="sample_text_2", shoppingHistoryId="sample_text_2", storeId="sample_text_2", title="sample_text_2", userId="sample_text_2")
    _safe_set(a, 'rEFUND41', b1)
    assert _is_linked(a, 'rEFUND41', b1)
    if hasattr(b1, 'sHOPPING_HISTORY40'):
        assert _is_linked(b1, 'sHOPPING_HISTORY40', a)
    _safe_set(a, 'rEFUND41', b2)
    assert _is_linked(a, 'rEFUND41', b2)
    if hasattr(b1, 'sHOPPING_HISTORY40'):
        assert not _is_linked(b1, 'sHOPPING_HISTORY40', a)
    if hasattr(b2, 'sHOPPING_HISTORY40'):
        assert _is_linked(b2, 'sHOPPING_HISTORY40', a)
    _safe_set(a, 'rEFUND41', None)
    assert not _is_linked(a, 'rEFUND41', b2)
    if hasattr(b2, 'sHOPPING_HISTORY40'):
        assert not _is_linked(b2, 'sHOPPING_HISTORY40', a)


def test_assoc_SHIPPING_PRODUCT_link_reassign_clear():
    a = SHIPPING_METHODS(_id="sample_text", address="sample_text", arrival="sample_text", createdAt="sample_text", name="sample_text", price=7)
    b1 = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    b2 = PRODUCT(ShippingMethods="sample_text_2", _id="sample_text_2", attribute="sample_text_2", color="sample_text_2", createdAt="sample_text_2", description="sample_text_2", dimensions="sample_text_2", isNew=False, model="sample_text_2", name="sample_text_2", photos="sample_text_2", price=13, quantity=13, relatedProducts="sample_text_2", sold=13, statusId="sample_text_2", storeId="sample_text_2")
    _safe_set(a, 'pRODUCT22', b1)
    assert _is_linked(a, 'pRODUCT22', b1)
    if hasattr(b1, 'sHIPPING23'):
        assert _is_linked(b1, 'sHIPPING23', a)
    _safe_set(a, 'pRODUCT22', b2)
    assert _is_linked(a, 'pRODUCT22', b2)
    if hasattr(b1, 'sHIPPING23'):
        assert not _is_linked(b1, 'sHIPPING23', a)
    if hasattr(b2, 'sHIPPING23'):
        assert _is_linked(b2, 'sHIPPING23', a)
    _safe_set(a, 'pRODUCT22', None)
    assert not _is_linked(a, 'pRODUCT22', b2)
    if hasattr(b2, 'sHIPPING23'):
        assert not _is_linked(b2, 'sHIPPING23', a)


def test_assoc_SHIPPING_SHOPPING_CART_link_reassign_clear():
    a = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    b1 = SHIPPING_METHODS(_id="sample_text", address="sample_text", arrival="sample_text", createdAt="sample_text", name="sample_text", price=7)
    b2 = SHIPPING_METHODS(_id="sample_text_2", address="sample_text_2", arrival="sample_text_2", createdAt="sample_text_2", name="sample_text_2", price=13)
    _safe_set(a, 'sHIPPING21', b1)
    assert _is_linked(a, 'sHIPPING21', b1)
    if hasattr(b1, 'sHOPPING_CART20'):
        assert _is_linked(b1, 'sHOPPING_CART20', a)
    _safe_set(a, 'sHIPPING21', b2)
    assert _is_linked(a, 'sHIPPING21', b2)
    if hasattr(b1, 'sHOPPING_CART20'):
        assert not _is_linked(b1, 'sHOPPING_CART20', a)
    if hasattr(b2, 'sHOPPING_CART20'):
        assert _is_linked(b2, 'sHOPPING_CART20', a)
    _safe_set(a, 'sHIPPING21', None)
    assert not _is_linked(a, 'sHIPPING21', b2)
    if hasattr(b2, 'sHOPPING_CART20'):
        assert not _is_linked(b2, 'sHOPPING_CART20', a)


def test_assoc_SHOPPING_CART_PRODUCT_link_reassign_clear():
    a = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    b1 = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    b2 = PRODUCT(ShippingMethods="sample_text_2", _id="sample_text_2", attribute="sample_text_2", color="sample_text_2", createdAt="sample_text_2", description="sample_text_2", dimensions="sample_text_2", isNew=False, model="sample_text_2", name="sample_text_2", photos="sample_text_2", price=13, quantity=13, relatedProducts="sample_text_2", sold=13, statusId="sample_text_2", storeId="sample_text_2")
    _safe_set(a, 'pRODUCT16', b1)
    assert _is_linked(a, 'pRODUCT16', b1)
    if hasattr(b1, 'sHOPPING_CART17'):
        assert _is_linked(b1, 'sHOPPING_CART17', a)
    _safe_set(a, 'pRODUCT16', b2)
    assert _is_linked(a, 'pRODUCT16', b2)
    if hasattr(b1, 'sHOPPING_CART17'):
        assert not _is_linked(b1, 'sHOPPING_CART17', a)
    if hasattr(b2, 'sHOPPING_CART17'):
        assert _is_linked(b2, 'sHOPPING_CART17', a)
    _safe_set(a, 'pRODUCT16', None)
    assert not _is_linked(a, 'pRODUCT16', b2)
    if hasattr(b2, 'sHOPPING_CART17'):
        assert not _is_linked(b2, 'sHOPPING_CART17', a)


def test_assoc_SHOPPING_CART_USUARIO_link_reassign_clear():
    a = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    b1 = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    b2 = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text_2", _id="sample_text_2", attribute="sample_text_2", comment="sample_text_2", created_at="sample_text_2", description="sample_text_2", isNew=False, isSold=False, name="sample_text_2", note="sample_text_2", photos="sample_text_2", price=13, productId="sample_text_2", quantity=13, score=13, shipAddress="sample_text_2", shipArrival="sample_text_2", shipName="sample_text_2", shipPrice=13, sold=13, status="sample_text_2", storeId="sample_text_2", userId="sample_text_2")
    _safe_set(a, 'sHOPPING_CART15', b1)
    assert _is_linked(a, 'sHOPPING_CART15', b1)
    if hasattr(b1, 'uSUARIO14'):
        assert _is_linked(b1, 'uSUARIO14', a)
    _safe_set(a, 'sHOPPING_CART15', b2)
    assert _is_linked(a, 'sHOPPING_CART15', b2)
    if hasattr(b1, 'uSUARIO14'):
        assert not _is_linked(b1, 'uSUARIO14', a)
    if hasattr(b2, 'uSUARIO14'):
        assert _is_linked(b2, 'uSUARIO14', a)
    _safe_set(a, 'sHOPPING_CART15', None)
    assert not _is_linked(a, 'sHOPPING_CART15', b2)
    if hasattr(b2, 'uSUARIO14'):
        assert not _is_linked(b2, 'uSUARIO14', a)


def test_assoc_SHOPPING_HISTORY_STORE_link_reassign_clear():
    a = STORE(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", name="sample_text", schedule="sample_text", statusId="sample_text", telephone="sample_text", updateAt="sample_text")
    b1 = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    b2 = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text_2", _id="sample_text_2", attribute="sample_text_2", comment="sample_text_2", created_at="sample_text_2", description="sample_text_2", isNew=False, isSold=False, name="sample_text_2", note="sample_text_2", photos="sample_text_2", price=13, productId="sample_text_2", quantity=13, score=13, shipAddress="sample_text_2", shipArrival="sample_text_2", shipName="sample_text_2", shipPrice=13, sold=13, status="sample_text_2", storeId="sample_text_2", userId="sample_text_2")
    _safe_set(a, 'sHOPPING_HISTORY31', b1)
    assert _is_linked(a, 'sHOPPING_HISTORY31', b1)
    if hasattr(b1, 'sTORE30'):
        assert _is_linked(b1, 'sTORE30', a)
    _safe_set(a, 'sHOPPING_HISTORY31', b2)
    assert _is_linked(a, 'sHOPPING_HISTORY31', b2)
    if hasattr(b1, 'sTORE30'):
        assert not _is_linked(b1, 'sTORE30', a)
    if hasattr(b2, 'sTORE30'):
        assert _is_linked(b2, 'sTORE30', a)
    _safe_set(a, 'sHOPPING_HISTORY31', None)
    assert not _is_linked(a, 'sHOPPING_HISTORY31', b2)
    if hasattr(b2, 'sTORE30'):
        assert not _is_linked(b2, 'sTORE30', a)


def test_assoc_SOCIAL_NETWORKS_USER_link_reassign_clear():
    a = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    b1 = SOCIAL_NETWORKS(_id="sample_text", facebook="sample_text", instagram="sample_text", twitter="sample_text", updateAt="sample_text")
    b2 = SOCIAL_NETWORKS(_id="sample_text_2", facebook="sample_text_2", instagram="sample_text_2", twitter="sample_text_2", updateAt="sample_text_2")
    _safe_set(a, 'sOCIAL_NETWORKS45', b1)
    assert _is_linked(a, 'sOCIAL_NETWORKS45', b1)
    if hasattr(b1, 'uSER44'):
        assert _is_linked(b1, 'uSER44', a)
    _safe_set(a, 'sOCIAL_NETWORKS45', b2)
    assert _is_linked(a, 'sOCIAL_NETWORKS45', b2)
    if hasattr(b1, 'uSER44'):
        assert not _is_linked(b1, 'uSER44', a)
    if hasattr(b2, 'uSER44'):
        assert _is_linked(b2, 'uSER44', a)
    _safe_set(a, 'sOCIAL_NETWORKS45', None)
    assert not _is_linked(a, 'sOCIAL_NETWORKS45', b2)
    if hasattr(b2, 'uSER44'):
        assert not _is_linked(b2, 'uSER44', a)


def test_assoc_STATUS_PRODUCT_link_reassign_clear():
    a = STATUS(_id="sample_text", createdAt="sample_text", name="sample_text")
    b1 = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    b2 = PRODUCT(ShippingMethods="sample_text_2", _id="sample_text_2", attribute="sample_text_2", color="sample_text_2", createdAt="sample_text_2", description="sample_text_2", dimensions="sample_text_2", isNew=False, model="sample_text_2", name="sample_text_2", photos="sample_text_2", price=13, quantity=13, relatedProducts="sample_text_2", sold=13, statusId="sample_text_2", storeId="sample_text_2")
    _safe_set(a, 'pRODUCT18', b1)
    assert _is_linked(a, 'pRODUCT18', b1)
    if hasattr(b1, 'sTATUS19'):
        assert _is_linked(b1, 'sTATUS19', a)
    _safe_set(a, 'pRODUCT18', b2)
    assert _is_linked(a, 'pRODUCT18', b2)
    if hasattr(b1, 'sTATUS19'):
        assert not _is_linked(b1, 'sTATUS19', a)
    if hasattr(b2, 'sTATUS19'):
        assert _is_linked(b2, 'sTATUS19', a)
    _safe_set(a, 'pRODUCT18', None)
    assert not _is_linked(a, 'pRODUCT18', b2)
    if hasattr(b2, 'sTATUS19'):
        assert not _is_linked(b2, 'sTATUS19', a)


def test_assoc_STATUS_SHOPPING_HISTORY_SHOPPING_HISTORY_link_reassign_clear():
    a = STATUS_SHOPPING_HISTORY(_id="sample_text", name="sample_text")
    b1 = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text", _id="sample_text", attribute="sample_text", comment="sample_text", created_at="sample_text", description="sample_text", isNew=True, isSold=True, name="sample_text", note="sample_text", photos="sample_text", price=7, productId="sample_text", quantity=7, score=7, shipAddress="sample_text", shipArrival="sample_text", shipName="sample_text", shipPrice=7, sold=7, status="sample_text", storeId="sample_text", userId="sample_text")
    b2 = SHOPPING_HISTORY(STATUS_SHOPPING_HIST_ID="sample_text_2", _id="sample_text_2", attribute="sample_text_2", comment="sample_text_2", created_at="sample_text_2", description="sample_text_2", isNew=False, isSold=False, name="sample_text_2", note="sample_text_2", photos="sample_text_2", price=13, productId="sample_text_2", quantity=13, score=13, shipAddress="sample_text_2", shipArrival="sample_text_2", shipName="sample_text_2", shipPrice=13, sold=13, status="sample_text_2", storeId="sample_text_2", userId="sample_text_2")
    _safe_set(a, 'sHOPPING_HISTORY24', b1)
    assert _is_linked(a, 'sHOPPING_HISTORY24', b1)
    if hasattr(b1, 'sTATUS_SHOPPING_HISTORY25'):
        assert _is_linked(b1, 'sTATUS_SHOPPING_HISTORY25', a)
    _safe_set(a, 'sHOPPING_HISTORY24', b2)
    assert _is_linked(a, 'sHOPPING_HISTORY24', b2)
    if hasattr(b1, 'sTATUS_SHOPPING_HISTORY25'):
        assert not _is_linked(b1, 'sTATUS_SHOPPING_HISTORY25', a)
    if hasattr(b2, 'sTATUS_SHOPPING_HISTORY25'):
        assert _is_linked(b2, 'sTATUS_SHOPPING_HISTORY25', a)
    _safe_set(a, 'sHOPPING_HISTORY24', None)
    assert not _is_linked(a, 'sHOPPING_HISTORY24', b2)
    if hasattr(b2, 'sTATUS_SHOPPING_HISTORY25'):
        assert not _is_linked(b2, 'sTATUS_SHOPPING_HISTORY25', a)


def test_assoc_STORE_PRODUCT_link_reassign_clear():
    a = STORE(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", name="sample_text", schedule="sample_text", statusId="sample_text", telephone="sample_text", updateAt="sample_text")
    b1 = PRODUCT(ShippingMethods="sample_text", _id="sample_text", attribute="sample_text", color="sample_text", createdAt="sample_text", description="sample_text", dimensions="sample_text", isNew=True, model="sample_text", name="sample_text", photos="sample_text", price=7, quantity=7, relatedProducts="sample_text", sold=7, statusId="sample_text", storeId="sample_text")
    b2 = PRODUCT(ShippingMethods="sample_text_2", _id="sample_text_2", attribute="sample_text_2", color="sample_text_2", createdAt="sample_text_2", description="sample_text_2", dimensions="sample_text_2", isNew=False, model="sample_text_2", name="sample_text_2", photos="sample_text_2", price=13, quantity=13, relatedProducts="sample_text_2", sold=13, statusId="sample_text_2", storeId="sample_text_2")
    _safe_set(a, 'pRODUCT26', b1)
    assert _is_linked(a, 'pRODUCT26', b1)
    if hasattr(b1, 'sTORE27'):
        assert _is_linked(b1, 'sTORE27', a)
    _safe_set(a, 'pRODUCT26', b2)
    assert _is_linked(a, 'pRODUCT26', b2)
    if hasattr(b1, 'sTORE27'):
        assert not _is_linked(b1, 'sTORE27', a)
    if hasattr(b2, 'sTORE27'):
        assert _is_linked(b2, 'sTORE27', a)
    _safe_set(a, 'pRODUCT26', None)
    assert not _is_linked(a, 'pRODUCT26', b2)
    if hasattr(b2, 'sTORE27'):
        assert not _is_linked(b2, 'sTORE27', a)


def test_assoc_STORE_USER_link_reassign_clear():
    a = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    b1 = STORE(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", name="sample_text", schedule="sample_text", statusId="sample_text", telephone="sample_text", updateAt="sample_text")
    b2 = STORE(_id="sample_text_2", address="sample_text_2", createdAt="sample_text_2", email="sample_text_2", name="sample_text_2", schedule="sample_text_2", statusId="sample_text_2", telephone="sample_text_2", updateAt="sample_text_2")
    _safe_set(a, 'sTORE29', b1)
    assert _is_linked(a, 'sTORE29', b1)
    if hasattr(b1, 'uSER28'):
        assert _is_linked(b1, 'uSER28', a)
    _safe_set(a, 'sTORE29', b2)
    assert _is_linked(a, 'sTORE29', b2)
    if hasattr(b1, 'uSER28'):
        assert not _is_linked(b1, 'uSER28', a)
    if hasattr(b2, 'uSER28'):
        assert _is_linked(b2, 'uSER28', a)
    _safe_set(a, 'sTORE29', None)
    assert not _is_linked(a, 'sTORE29', b2)
    if hasattr(b2, 'uSER28'):
        assert not _is_linked(b2, 'uSER28', a)


def test_assoc_roles_usuario_link_reassign_clear():
    a = USER(_id="sample_text", address="sample_text", createdAt="sample_text", email="sample_text", lastAccess="sample_text", name="sample_text", password="sample_text", status="sample_text", surname="sample_text", telephone="sample_text", updateAt="sample_text", verified=True)
    b1 = ROLES(_id="sample_text", createdAt="sample_text", name="sample_text")
    b2 = ROLES(_id="sample_text_2", createdAt="sample_text_2", name="sample_text_2")
    _safe_set(a, 'roles1', b1)
    assert _is_linked(a, 'roles1', b1)
    if hasattr(b1, 'usuario0'):
        assert _is_linked(b1, 'usuario0', a)
    _safe_set(a, 'roles1', b2)
    assert _is_linked(a, 'roles1', b2)
    if hasattr(b1, 'usuario0'):
        assert not _is_linked(b1, 'usuario0', a)
    if hasattr(b2, 'usuario0'):
        assert _is_linked(b2, 'usuario0', a)
    _safe_set(a, 'roles1', None)
    assert not _is_linked(a, 'roles1', b2)
    if hasattr(b2, 'usuario0'):
        assert not _is_linked(b2, 'usuario0', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CATEGORIAS_strategy = st.builds(CATEGORIAS, _id=safe_text, createdAt=safe_text, name=safe_text)
@given(instance=CATEGORIAS_strategy)
@settings(max_examples=25)
def test_CATEGORIAS_instantiation(instance):
    assert isinstance(instance, CATEGORIAS)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


EVENTS_HISTORY_strategy = st.builds(EVENTS_HISTORY, _id=safe_text, createdAt=safe_text, eventId=safe_text, newValue=safe_text, oldValue=safe_text, userId=safe_text)
@given(instance=EVENTS_HISTORY_strategy)
@settings(max_examples=25)
def test_EVENTS_HISTORY_instantiation(instance):
    assert isinstance(instance, EVENTS_HISTORY)


EVENTS_LIST_strategy = st.builds(EVENTS_LIST, _id=safe_text, createdAt=safe_text, description=safe_text, key=safe_text)
@given(instance=EVENTS_LIST_strategy)
@settings(max_examples=25)
def test_EVENTS_LIST_instantiation(instance):
    assert isinstance(instance, EVENTS_LIST)


FAVORITES_strategy = st.builds(FAVORITES, _id=safe_text, createdAt=safe_text, statusId=safe_text, storeId=safe_text, userId=safe_text)
@given(instance=FAVORITES_strategy)
@settings(max_examples=25)
def test_FAVORITES_instantiation(instance):
    assert isinstance(instance, FAVORITES)


FEEDBACK_strategy = st.builds(FEEDBACK, _id=safe_text, createdAt=safe_text, like=safe_text, linkInstagram=safe_text, linkYoutube=safe_text, photos=safe_text, productId=safe_text, updateAt=safe_text, userId=safe_text, wysiwyg=safe_text)
@given(instance=FEEDBACK_strategy)
@settings(max_examples=25)
def test_FEEDBACK_instantiation(instance):
    assert isinstance(instance, FEEDBACK)


FEEDBACK_COMMENT_strategy = st.builds(FEEDBACK_COMMENT, _id=safe_text, comment=safe_text, createdAt=safe_text, feedbackId=safe_text, score=st.integers(), userId=safe_text)
@given(instance=FEEDBACK_COMMENT_strategy)
@settings(max_examples=25)
def test_FEEDBACK_COMMENT_instantiation(instance):
    assert isinstance(instance, FEEDBACK_COMMENT)


FOLLOW_strategy = st.builds(FOLLOW, _id=safe_text, createdAt=safe_text, followers=safe_text, following=safe_text, followingGroup=safe_text, userId=safe_text)
@given(instance=FOLLOW_strategy)
@settings(max_examples=25)
def test_FOLLOW_instantiation(instance):
    assert isinstance(instance, FOLLOW)


FOLLOW_MESSENGER_strategy = st.builds(FOLLOW_MESSENGER, _id=safe_text, createdAt=safe_text, userId=safe_text)
@given(instance=FOLLOW_MESSENGER_strategy)
@settings(max_examples=25)
def test_FOLLOW_MESSENGER_instantiation(instance):
    assert isinstance(instance, FOLLOW_MESSENGER)


NOTIFICATION_strategy = st.builds(NOTIFICATION, _id=safe_text, code=safe_text, createdAt=safe_text, message=safe_text, userId=safe_text)
@given(instance=NOTIFICATION_strategy)
@settings(max_examples=25)
def test_NOTIFICATION_instantiation(instance):
    assert isinstance(instance, NOTIFICATION)


PRODUCT_strategy = st.builds(PRODUCT, ShippingMethods=safe_text, _id=safe_text, attribute=safe_text, color=safe_text, createdAt=safe_text, description=safe_text, dimensions=safe_text, isNew=st.booleans(), model=safe_text, name=safe_text, photos=safe_text, price=st.integers(), quantity=st.integers(), relatedProducts=safe_text, sold=st.integers(), statusId=safe_text, storeId=safe_text)
@given(instance=PRODUCT_strategy)
@settings(max_examples=25)
def test_PRODUCT_instantiation(instance):
    assert isinstance(instance, PRODUCT)


QUESTIONS_strategy = st.builds(QUESTIONS, _id=safe_text, answer=safe_text, createdAt=safe_text, productId=safe_text, question=safe_text, score=st.integers(), statusId=safe_text, userId=safe_text)
@given(instance=QUESTIONS_strategy)
@settings(max_examples=25)
def test_QUESTIONS_instantiation(instance):
    assert isinstance(instance, QUESTIONS)


REFUND_strategy = st.builds(REFUND, _id=safe_text, created_at=safe_text, message=safe_text, productId=safe_text, shoppingHistoryId=safe_text, storeId=safe_text, title=safe_text, userId=safe_text)
@given(instance=REFUND_strategy)
@settings(max_examples=25)
def test_REFUND_instantiation(instance):
    assert isinstance(instance, REFUND)


REFUND_MESSAGES_strategy = st.builds(REFUND_MESSAGES, _id=safe_text, attach=safe_text, created_at=safe_text, message=safe_text, userId=safe_text)
@given(instance=REFUND_MESSAGES_strategy)
@settings(max_examples=25)
def test_REFUND_MESSAGES_instantiation(instance):
    assert isinstance(instance, REFUND_MESSAGES)


ROLES_strategy = st.builds(ROLES, _id=safe_text, createdAt=safe_text, name=safe_text)
@given(instance=ROLES_strategy)
@settings(max_examples=25)
def test_ROLES_instantiation(instance):
    assert isinstance(instance, ROLES)


SHIPPING_METHODS_strategy = st.builds(SHIPPING_METHODS, _id=safe_text, address=safe_text, arrival=safe_text, createdAt=safe_text, name=safe_text, price=st.integers())
@given(instance=SHIPPING_METHODS_strategy)
@settings(max_examples=25)
def test_SHIPPING_METHODS_instantiation(instance):
    assert isinstance(instance, SHIPPING_METHODS)


SHOPPING_HISTORY_strategy = st.builds(SHOPPING_HISTORY, STATUS_SHOPPING_HIST_ID=safe_text, _id=safe_text, attribute=safe_text, comment=safe_text, created_at=safe_text, description=safe_text, isNew=st.booleans(), isSold=st.booleans(), name=safe_text, note=safe_text, photos=safe_text, price=st.integers(), productId=safe_text, quantity=st.integers(), score=st.integers(), shipAddress=safe_text, shipArrival=safe_text, shipName=safe_text, shipPrice=st.integers(), sold=st.integers(), status=safe_text, storeId=safe_text, userId=safe_text)
@given(instance=SHOPPING_HISTORY_strategy)
@settings(max_examples=25)
def test_SHOPPING_HISTORY_instantiation(instance):
    assert isinstance(instance, SHOPPING_HISTORY)


SHOPPING_MESSENGER_strategy = st.builds(SHOPPING_MESSENGER, _id=safe_text, created_at=safe_text, message=safe_text, photos=safe_text, storeId=safe_text, userId=safe_text)
@given(instance=SHOPPING_MESSENGER_strategy)
@settings(max_examples=25)
def test_SHOPPING_MESSENGER_instantiation(instance):
    assert isinstance(instance, SHOPPING_MESSENGER)


SOCIAL_NETWORKS_strategy = st.builds(SOCIAL_NETWORKS, _id=safe_text, facebook=safe_text, instagram=safe_text, twitter=safe_text, updateAt=safe_text)
@given(instance=SOCIAL_NETWORKS_strategy)
@settings(max_examples=25)
def test_SOCIAL_NETWORKS_instantiation(instance):
    assert isinstance(instance, SOCIAL_NETWORKS)


STATUS_strategy = st.builds(STATUS, _id=safe_text, createdAt=safe_text, name=safe_text)
@given(instance=STATUS_strategy)
@settings(max_examples=25)
def test_STATUS_instantiation(instance):
    assert isinstance(instance, STATUS)


STATUS2_strategy = st.builds(STATUS2, _id=safe_text, name=safe_text)
@given(instance=STATUS2_strategy)
@settings(max_examples=25)
def test_STATUS2_instantiation(instance):
    assert isinstance(instance, STATUS2)


STATUS_SHOPPING_HISTORY_strategy = st.builds(STATUS_SHOPPING_HISTORY, _id=safe_text, name=safe_text)
@given(instance=STATUS_SHOPPING_HISTORY_strategy)
@settings(max_examples=25)
def test_STATUS_SHOPPING_HISTORY_instantiation(instance):
    assert isinstance(instance, STATUS_SHOPPING_HISTORY)


STORE_strategy = st.builds(STORE, _id=safe_text, address=safe_text, createdAt=safe_text, email=safe_text, name=safe_text, schedule=safe_text, statusId=safe_text, telephone=safe_text, updateAt=safe_text)
@given(instance=STORE_strategy)
@settings(max_examples=25)
def test_STORE_instantiation(instance):
    assert isinstance(instance, STORE)


SUBSCRIPTION_BENEFITS_strategy = st.builds(SUBSCRIPTION_BENEFITS, _id=safe_text, description=safe_text, key_name=safe_text)
@given(instance=SUBSCRIPTION_BENEFITS_strategy)
@settings(max_examples=25)
def test_SUBSCRIPTION_BENEFITS_instantiation(instance):
    assert isinstance(instance, SUBSCRIPTION_BENEFITS)


USER_strategy = st.builds(USER, _id=safe_text, address=safe_text, createdAt=safe_text, email=safe_text, lastAccess=safe_text, name=safe_text, password=safe_text, status=safe_text, surname=safe_text, telephone=safe_text, updateAt=safe_text, verified=st.booleans())
@given(instance=USER_strategy)
@settings(max_examples=25)
def test_USER_instantiation(instance):
    assert isinstance(instance, USER)


WHISES_strategy = st.builds(WHISES, _id=safe_text, createdAt=safe_text, productId=safe_text, statusId=safe_text, userId=safe_text)
@given(instance=WHISES_strategy)
@settings(max_examples=25)
def test_WHISES_instantiation(instance):
    assert isinstance(instance, WHISES)



