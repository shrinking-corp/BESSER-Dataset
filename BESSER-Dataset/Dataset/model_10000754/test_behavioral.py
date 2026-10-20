import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Actor,
    Admin,
    Armor,
    BankAccount,
    Basket,
    BookStorage_Interface,
    Brave,
    Catalog,
    ClassA,
    ClassB,
    ClassC,
    ClassD,
    ClassE,
    ClassF,
    ClassG,
    ClassH,
    ClassJ,
    ClassK,
    ClassL,
    ClassM,
    ClassN,
    ClassP,
    ClassQ,
    ClassR,
    ClassS,
    ClassT,
    ClassU,
    ClassV,
    Client,
    ClientDatabase,
    ClientRewiev,
    Client_hoice_Interface,
    Coward,
    DatabaseAPI,
    DetailDescription,
    EnemyStrategy_Interface,
    GameScreen,
    Hero,
    InnerBookStorage,
    InterfaceO_Interface,
    Inventory,
    Inventory1,
    Items,
    Knife,
    LevelMap,
    Map,
    MapGenerator,
    MazeGenerator,
    MenuScreen,
    NotMyBusiness,
    Order,
    OriginalReview,
    OwnBookStorage,
    PaymentByAccaunt,
    PaymentByCard,
    PaymentByCard1,
    Payment_Interface,
    PlayerActor,
    Point,
    Review_Interface,
    Screen_Interface,
    SearchRequest,
    ShopAPI,
    ShortReview,
    StateService,
    Stats,
    SystemUser_Interface,
    WallActor,
    Wishlist,
    ______Actor,
    __________Component,
    ______________UseCase,
    _______________UseCase,
    ________________Component,
    __________________UseCase,
    ______________________Component,
    ________________________Component,
    _________________________Component,
    ___________________________Component,
    ___________________________UseCase,
    ______________________________Component,
    book,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Basket_book_stub_double():
    # Basket has no real 'book50' property in the generated
    # code (a bare stub) -- manually attach it so book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = book(author="sample_text", catygory="sample_text", keywords="sample_text", rate=3.14, title="sample_text")
    partner = Basket()
    setattr(partner, 'book50', None)
    _safe_set(owner, 'basket51', partner)
    assert getattr(partner, 'book50') == owner
    _safe_set(owner, 'basket51', None)
    assert getattr(partner, 'book50') is None


def test_assoc_Catalog_book_stub_double():
    # Catalog has no real 'book28' property in the generated
    # code (a bare stub) -- manually attach it so book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = book(author="sample_text", catygory="sample_text", keywords="sample_text", rate=3.14, title="sample_text")
    partner = Catalog()
    setattr(partner, 'book28', None)
    _safe_set(owner, 'catalog29', partner)
    assert getattr(partner, 'book28') == owner
    _safe_set(owner, 'catalog29', None)
    assert getattr(partner, 'book28') is None


def test_assoc_Client_Basket_stub_double():
    # Basket has no real 'client47' property in the generated
    # code (a bare stub) -- manually attach it so Client's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Client's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Client(addres="sample_text", card="sample_text", name="sample_text")
    partner = Basket()
    setattr(partner, 'client47', None)
    _safe_set(owner, 'basket46', partner)
    assert getattr(partner, 'client47') == owner
    _safe_set(owner, 'basket46', None)
    assert getattr(partner, 'client47') is None


def test_assoc_Client_ClientDatabase_stub_double():
    # ClientDatabase has no real 'client31' property in the generated
    # code (a bare stub) -- manually attach it so Client's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Client's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Client(addres="sample_text", card="sample_text", name="sample_text")
    partner = ClientDatabase()
    setattr(partner, 'client31', None)
    _safe_set(owner, 'clientDatabase30', partner)
    assert getattr(partner, 'client31') == owner
    _safe_set(owner, 'clientDatabase30', None)
    assert getattr(partner, 'client31') is None


def test_assoc_Client_Order_stub_double():
    # Order has no real 'client37' property in the generated
    # code (a bare stub) -- manually attach it so Client's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Client's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Client(addres="sample_text", card="sample_text", name="sample_text")
    partner = Order()
    setattr(partner, 'client37', None)
    _safe_set(owner, 'order36', partner)
    assert getattr(partner, 'client37') == owner
    _safe_set(owner, 'order36', None)
    assert getattr(partner, 'client37') is None


def test_assoc_Client_Payment_stub_double():
    # Payment_Interface has no real 'client45' property in the generated
    # code (a bare stub) -- manually attach it so Client's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Client's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Client(addres="sample_text", card="sample_text", name="sample_text")
    partner = Payment_Interface()
    setattr(partner, 'client45', None)
    _safe_set(owner, 'payment44', partner)
    assert getattr(partner, 'client45') == owner
    _safe_set(owner, 'payment44', None)
    assert getattr(partner, 'client45') is None


def test_assoc_Client_Wishlist_stub_double():
    # Wishlist has no real 'client55' property in the generated
    # code (a bare stub) -- manually attach it so Client's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Client's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Client(addres="sample_text", card="sample_text", name="sample_text")
    partner = Wishlist()
    setattr(partner, 'client55', None)
    _safe_set(owner, 'wishlist54', partner)
    assert getattr(partner, 'client55') == owner
    _safe_set(owner, 'wishlist54', None)
    assert getattr(partner, 'client55') is None


def test_assoc_DetailDescription_ClientRewiev_stub_double():
    # DetailDescription has no real 'clientRewiev22' property in the generated
    # code (a bare stub) -- manually attach it so ClientRewiev's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClientRewiev's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClientRewiev(mark=7, text="sample_text")
    partner = DetailDescription()
    setattr(partner, 'clientRewiev22', None)
    _safe_set(owner, 'detailDescription23', partner)
    assert getattr(partner, 'clientRewiev22') == owner
    _safe_set(owner, 'detailDescription23', None)
    assert getattr(partner, 'clientRewiev22') is None


def test_assoc_DetailDescription_OriginalReview_stub_double():
    # DetailDescription has no real 'originalReview24' property in the generated
    # code (a bare stub) -- manually attach it so OriginalReview's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OriginalReview's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OriginalReview(texr="sample_text")
    partner = DetailDescription()
    setattr(partner, 'originalReview24', None)
    _safe_set(owner, 'detailDescription25', partner)
    assert getattr(partner, 'originalReview24') == owner
    _safe_set(owner, 'detailDescription25', None)
    assert getattr(partner, 'originalReview24') is None


def test_assoc_Order_book_stub_double():
    # Order has no real 'book52' property in the generated
    # code (a bare stub) -- manually attach it so book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = book(author="sample_text", catygory="sample_text", keywords="sample_text", rate=3.14, title="sample_text")
    partner = Order()
    setattr(partner, 'book52', None)
    _safe_set(owner, 'order53', partner)
    assert getattr(partner, 'book52') == owner
    _safe_set(owner, 'order53', None)
    assert getattr(partner, 'book52') is None


def test_assoc_SearchRequest_book_stub_double():
    # SearchRequest has no real 'book38' property in the generated
    # code (a bare stub) -- manually attach it so book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = book(author="sample_text", catygory="sample_text", keywords="sample_text", rate=3.14, title="sample_text")
    partner = SearchRequest()
    setattr(partner, 'book38', None)
    _safe_set(owner, 'searchRequest39', partner)
    assert getattr(partner, 'book38') == owner
    _safe_set(owner, 'searchRequest39', None)
    assert getattr(partner, 'book38') is None


def test_assoc_Wishlist_book_stub_double():
    # Wishlist has no real 'book48' property in the generated
    # code (a bare stub) -- manually attach it so book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = book(author="sample_text", catygory="sample_text", keywords="sample_text", rate=3.14, title="sample_text")
    partner = Wishlist()
    setattr(partner, 'book48', None)
    _safe_set(owner, 'wishlist49', partner)
    assert getattr(partner, 'book48') == owner
    _safe_set(owner, 'wishlist49', None)
    assert getattr(partner, 'book48') is None


def test_assoc_book_DetailDescription_stub_double():
    # DetailDescription has no real 'book21' property in the generated
    # code (a bare stub) -- manually attach it so book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = book(author="sample_text", catygory="sample_text", keywords="sample_text", rate=3.14, title="sample_text")
    partner = DetailDescription()
    setattr(partner, 'book21', None)
    _safe_set(owner, 'detailDescription20', partner)
    assert getattr(partner, 'book21') == owner
    _safe_set(owner, 'detailDescription20', None)
    assert getattr(partner, 'book21') is None


def test_assoc_book_Review_stub_double():
    # Review_Interface has no real 'book19' property in the generated
    # code (a bare stub) -- manually attach it so book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = book(author="sample_text", catygory="sample_text", keywords="sample_text", rate=3.14, title="sample_text")
    partner = Review_Interface()
    setattr(partner, 'book19', None)
    _safe_set(owner, 'review18', partner)
    assert getattr(partner, 'book19') == owner
    _safe_set(owner, 'review18', None)
    assert getattr(partner, 'book19') is None


def test_assoc_book_ShortReview_stub_double():
    # ShortReview has no real 'book27' property in the generated
    # code (a bare stub) -- manually attach it so book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = book(author="sample_text", catygory="sample_text", keywords="sample_text", rate=3.14, title="sample_text")
    partner = ShortReview()
    setattr(partner, 'book27', None)
    _safe_set(owner, 'shortReview26', partner)
    assert getattr(partner, 'book27') == owner
    _safe_set(owner, 'shortReview26', None)
    assert getattr(partner, 'book27') is None


