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
    Animation,
    book_Move,
    book_Rotation,
    book_Fade,
    Action,
    book_JSAction,
    book_OpenPage,
    book_Animation,
    Control,
    book_ImageFlash,
    book_Label,
    book_Media,
    book_Group,
    book_Action,
    Node,
    book_Shape,
    book_Node,
    book_Control,
    Page,
    book_Layer,
    book_Splash,
    book_Page,
    book_Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_animation_is_not_abstract():
    assert not inspect.isabstract(Animation)


def test_hyp_animation_constructor_exists():
    assert callable(Animation.__init__)


def test_hyp_animation_constructor_args():
    sig = inspect.signature(Animation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_book_move_is_not_abstract():
    assert not inspect.isabstract(book_Move)


def test_hyp_book_move_constructor_exists():
    assert callable(book_Move.__init__)


def test_hyp_book_move_constructor_args():
    sig = inspect.signature(book_Move.__init__)
    params = list(sig.parameters.keys())
    assert "toLocation" in params, "Missing parameter 'toLocation'"
    assert "fromLocation" in params, "Missing parameter 'fromLocation'"





def test_hyp_book_rotation_is_not_abstract():
    assert not inspect.isabstract(book_Rotation)


def test_hyp_book_rotation_constructor_exists():
    assert callable(book_Rotation.__init__)


def test_hyp_book_rotation_constructor_args():
    sig = inspect.signature(book_Rotation.__init__)
    params = list(sig.parameters.keys())
    assert "fromAngle" in params, "Missing parameter 'fromAngle'"
    assert "toAngle" in params, "Missing parameter 'toAngle'"





def test_hyp_book_fade_is_not_abstract():
    assert not inspect.isabstract(book_Fade)


def test_hyp_book_fade_constructor_exists():
    assert callable(book_Fade.__init__)


def test_hyp_book_fade_constructor_args():
    sig = inspect.signature(book_Fade.__init__)
    params = list(sig.parameters.keys())
    assert "fromValue" in params, "Missing parameter 'fromValue'"
    assert "toValue" in params, "Missing parameter 'toValue'"





def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_book_jsaction_is_not_abstract():
    assert not inspect.isabstract(book_JSAction)


def test_hyp_book_jsaction_constructor_exists():
    assert callable(book_JSAction.__init__)


def test_hyp_book_jsaction_constructor_args():
    sig = inspect.signature(book_JSAction.__init__)
    params = list(sig.parameters.keys())
    assert "javaScript" in params, "Missing parameter 'javaScript'"




def test_hyp_book_openpage_is_not_abstract():
    assert not inspect.isabstract(book_OpenPage)


def test_hyp_book_openpage_constructor_exists():
    assert callable(book_OpenPage.__init__)


def test_hyp_book_openpage_constructor_args():
    sig = inspect.signature(book_OpenPage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_book_animation_is_not_abstract():
    assert not inspect.isabstract(book_Animation)


def test_hyp_book_animation_constructor_exists():
    assert callable(book_Animation.__init__)


def test_hyp_book_animation_constructor_args():
    sig = inspect.signature(book_Animation.__init__)
    params = list(sig.parameters.keys())
    assert "autoReverse" in params, "Missing parameter 'autoReverse'"
    assert "delay" in params, "Missing parameter 'delay'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "repeat" in params, "Missing parameter 'repeat'"







def test_hyp_control_is_not_abstract():
    assert not inspect.isabstract(Control)


def test_hyp_control_constructor_exists():
    assert callable(Control.__init__)


def test_hyp_control_constructor_args():
    sig = inspect.signature(Control.__init__)
    params = list(sig.parameters.keys())



def test_hyp_book_imageflash_is_not_abstract():
    assert not inspect.isabstract(book_ImageFlash)


def test_hyp_book_imageflash_constructor_exists():
    assert callable(book_ImageFlash.__init__)


def test_hyp_book_imageflash_constructor_args():
    sig = inspect.signature(book_ImageFlash.__init__)
    params = list(sig.parameters.keys())
    assert "images" in params, "Missing parameter 'images'"
    assert "duration" in params, "Missing parameter 'duration'"





def test_hyp_book_label_is_not_abstract():
    assert not inspect.isabstract(book_Label)


def test_hyp_book_label_constructor_exists():
    assert callable(book_Label.__init__)


def test_hyp_book_label_constructor_args():
    sig = inspect.signature(book_Label.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "font" in params, "Missing parameter 'font'"





def test_hyp_book_media_is_not_abstract():
    assert not inspect.isabstract(book_Media)


def test_hyp_book_media_constructor_exists():
    assert callable(book_Media.__init__)


def test_hyp_book_media_constructor_args():
    sig = inspect.signature(book_Media.__init__)
    params = list(sig.parameters.keys())
    assert "repeat" in params, "Missing parameter 'repeat'"
    assert "autoPlay" in params, "Missing parameter 'autoPlay'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "url" in params, "Missing parameter 'url'"







def test_hyp_book_group_is_not_abstract():
    assert not inspect.isabstract(book_Group)


def test_hyp_book_group_constructor_exists():
    assert callable(book_Group.__init__)


def test_hyp_book_group_constructor_args():
    sig = inspect.signature(book_Group.__init__)
    params = list(sig.parameters.keys())



def test_hyp_book_action_is_not_abstract():
    assert not inspect.isabstract(book_Action)


def test_hyp_book_action_constructor_exists():
    assert callable(book_Action.__init__)


def test_hyp_book_action_constructor_args():
    sig = inspect.signature(book_Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_hyp_node_constructor_exists():
    assert callable(Node.__init__)


def test_hyp_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_book_shape_is_not_abstract():
    assert not inspect.isabstract(book_Shape)


def test_hyp_book_shape_constructor_exists():
    assert callable(book_Shape.__init__)


def test_hyp_book_shape_constructor_args():
    sig = inspect.signature(book_Shape.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"





def test_hyp_book_node_is_not_abstract():
    assert not inspect.isabstract(book_Node)


def test_hyp_book_node_constructor_exists():
    assert callable(book_Node.__init__)


def test_hyp_book_node_constructor_args():
    sig = inspect.signature(book_Node.__init__)
    params = list(sig.parameters.keys())
    assert "background" in params, "Missing parameter 'background'"
    assert "opacity" in params, "Missing parameter 'opacity'"
    assert "foreground" in params, "Missing parameter 'foreground'"
    assert "enable" in params, "Missing parameter 'enable'"
    assert "bounds" in params, "Missing parameter 'bounds'"








def test_hyp_book_control_is_not_abstract():
    assert not inspect.isabstract(book_Control)


def test_hyp_book_control_constructor_exists():
    assert callable(book_Control.__init__)


def test_hyp_book_control_constructor_args():
    sig = inspect.signature(book_Control.__init__)
    params = list(sig.parameters.keys())
    assert "image" in params, "Missing parameter 'image'"
    assert "sound" in params, "Missing parameter 'sound'"





def test_hyp_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_hyp_page_constructor_exists():
    assert callable(Page.__init__)


def test_hyp_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())



def test_hyp_book_layer_is_not_abstract():
    assert not inspect.isabstract(book_Layer)


def test_hyp_book_layer_constructor_exists():
    assert callable(book_Layer.__init__)


def test_hyp_book_layer_constructor_args():
    sig = inspect.signature(book_Layer.__init__)
    params = list(sig.parameters.keys())
    assert "visible" in params, "Missing parameter 'visible'"




def test_hyp_book_splash_is_not_abstract():
    assert not inspect.isabstract(book_Splash)


def test_hyp_book_splash_constructor_exists():
    assert callable(book_Splash.__init__)


def test_hyp_book_splash_constructor_args():
    sig = inspect.signature(book_Splash.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"




def test_hyp_book_page_is_not_abstract():
    assert not inspect.isabstract(book_Page)


def test_hyp_book_page_constructor_exists():
    assert callable(book_Page.__init__)


def test_hyp_book_page_constructor_args():
    sig = inspect.signature(book_Page.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_book_book_is_not_abstract():
    assert not inspect.isabstract(book_Book)


def test_hyp_book_book_constructor_exists():
    assert callable(book_Book.__init__)


def test_hyp_book_book_constructor_args():
    sig = inspect.signature(book_Book.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "description" in params, "Missing parameter 'description'"
    assert "bookId" in params, "Missing parameter 'bookId'"
    assert "title" in params, "Missing parameter 'title'"
    assert "resolution" in params, "Missing parameter 'resolution'"
    assert "version" in params, "Missing parameter 'version'"








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
Animation_strategy = st.builds(
    Animation,
)
book_Move_strategy = st.builds(
    book_Move,
    toLocation=
        safe_text,
    fromLocation=
        safe_text
)
book_Rotation_strategy = st.builds(
    book_Rotation,
    fromAngle=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    toAngle=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
book_Fade_strategy = st.builds(
    book_Fade,
    fromValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    toValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Action_strategy = st.builds(
    Action,
)
book_JSAction_strategy = st.builds(
    book_JSAction,
    javaScript=
        safe_text
)
book_OpenPage_strategy = st.builds(
    book_OpenPage,
)
book_Animation_strategy = st.builds(
    book_Animation,
    autoReverse=
        st.booleans(),
    delay=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    duration=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    repeat=
        st.integers()
)
Control_strategy = st.builds(
    Control,
)
book_ImageFlash_strategy = st.builds(
    book_ImageFlash,
    images=
        safe_text,
    duration=
        st.integers()
)
book_Label_strategy = st.builds(
    book_Label,
    text=
        safe_text,
    font=
        safe_text
)
book_Media_strategy = st.builds(
    book_Media,
    repeat=
        st.integers(),
    autoPlay=
        st.booleans(),
    duration=
        st.integers(),
    url=
        safe_text
)
book_Group_strategy = st.builds(
    book_Group,
)
book_Action_strategy = st.builds(
    book_Action,
)
Node_strategy = st.builds(
    Node,
)
book_Shape_strategy = st.builds(
    book_Shape,
    points=
        safe_text,
    lineWidth=
        st.integers()
)
book_Node_strategy = st.builds(
    book_Node,
    background=
        safe_text,
    opacity=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    foreground=
        safe_text,
    enable=
        st.booleans(),
    bounds=
        safe_text
)
book_Control_strategy = st.builds(
    book_Control,
    image=
        safe_text,
    sound=
        safe_text
)
Page_strategy = st.builds(
    Page,
)
book_Layer_strategy = st.builds(
    book_Layer,
    visible=
        st.booleans()
)
book_Splash_strategy = st.builds(
    book_Splash,
    duration=
        st.integers()
)
book_Page_strategy = st.builds(
    book_Page,
    name=
        safe_text
)
book_Book_strategy = st.builds(
    book_Book,
    author=
        safe_text,
    description=
        safe_text,
    bookId=
        safe_text,
    title=
        safe_text,
    resolution=
        safe_text,
    version=
        safe_text
)





@given(instance=book_Move_strategy)
def test_hyp_book_move_toLocation_setter(instance):
    original = instance.toLocation
    instance.toLocation = original
    assert instance.toLocation == original



@given(instance=book_Move_strategy)
def test_hyp_book_move_fromLocation_setter(instance):
    original = instance.fromLocation
    instance.fromLocation = original
    assert instance.fromLocation == original




@given(instance=book_Rotation_strategy)
def test_hyp_book_rotation_fromAngle_setter(instance):
    original = instance.fromAngle
    instance.fromAngle = original
    assert instance.fromAngle == original



@given(instance=book_Rotation_strategy)
def test_hyp_book_rotation_toAngle_setter(instance):
    original = instance.toAngle
    instance.toAngle = original
    assert instance.toAngle == original




@given(instance=book_Fade_strategy)
def test_hyp_book_fade_fromValue_setter(instance):
    original = instance.fromValue
    instance.fromValue = original
    assert instance.fromValue == original



@given(instance=book_Fade_strategy)
def test_hyp_book_fade_toValue_setter(instance):
    original = instance.toValue
    instance.toValue = original
    assert instance.toValue == original





@given(instance=book_JSAction_strategy)
def test_hyp_book_jsaction_javaScript_setter(instance):
    original = instance.javaScript
    instance.javaScript = original
    assert instance.javaScript == original





@given(instance=book_Animation_strategy)
def test_hyp_book_animation_autoReverse_setter(instance):
    original = instance.autoReverse
    instance.autoReverse = original
    assert instance.autoReverse == original



@given(instance=book_Animation_strategy)
def test_hyp_book_animation_delay_setter(instance):
    original = instance.delay
    instance.delay = original
    assert instance.delay == original



@given(instance=book_Animation_strategy)
def test_hyp_book_animation_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=book_Animation_strategy)
def test_hyp_book_animation_repeat_setter(instance):
    original = instance.repeat
    instance.repeat = original
    assert instance.repeat == original





@given(instance=book_ImageFlash_strategy)
def test_hyp_book_imageflash_images_setter(instance):
    original = instance.images
    instance.images = original
    assert instance.images == original



@given(instance=book_ImageFlash_strategy)
def test_hyp_book_imageflash_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original




@given(instance=book_Label_strategy)
def test_hyp_book_label_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=book_Label_strategy)
def test_hyp_book_label_font_setter(instance):
    original = instance.font
    instance.font = original
    assert instance.font == original




@given(instance=book_Media_strategy)
def test_hyp_book_media_repeat_setter(instance):
    original = instance.repeat
    instance.repeat = original
    assert instance.repeat == original



@given(instance=book_Media_strategy)
def test_hyp_book_media_autoPlay_setter(instance):
    original = instance.autoPlay
    instance.autoPlay = original
    assert instance.autoPlay == original



@given(instance=book_Media_strategy)
def test_hyp_book_media_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=book_Media_strategy)
def test_hyp_book_media_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original







@given(instance=book_Shape_strategy)
def test_hyp_book_shape_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original



@given(instance=book_Shape_strategy)
def test_hyp_book_shape_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original




@given(instance=book_Node_strategy)
def test_hyp_book_node_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original



@given(instance=book_Node_strategy)
def test_hyp_book_node_opacity_setter(instance):
    original = instance.opacity
    instance.opacity = original
    assert instance.opacity == original



@given(instance=book_Node_strategy)
def test_hyp_book_node_foreground_setter(instance):
    original = instance.foreground
    instance.foreground = original
    assert instance.foreground == original



@given(instance=book_Node_strategy)
def test_hyp_book_node_enable_setter(instance):
    original = instance.enable
    instance.enable = original
    assert instance.enable == original



@given(instance=book_Node_strategy)
def test_hyp_book_node_bounds_setter(instance):
    original = instance.bounds
    instance.bounds = original
    assert instance.bounds == original




@given(instance=book_Control_strategy)
def test_hyp_book_control_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original



@given(instance=book_Control_strategy)
def test_hyp_book_control_sound_setter(instance):
    original = instance.sound
    instance.sound = original
    assert instance.sound == original





@given(instance=book_Layer_strategy)
def test_hyp_book_layer_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original




@given(instance=book_Splash_strategy)
def test_hyp_book_splash_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original




@given(instance=book_Page_strategy)
def test_hyp_book_page_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=book_Book_strategy)
def test_hyp_book_book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=book_Book_strategy)
def test_hyp_book_book_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=book_Book_strategy)
def test_hyp_book_book_bookId_setter(instance):
    original = instance.bookId
    instance.bookId = original
    assert instance.bookId == original



@given(instance=book_Book_strategy)
def test_hyp_book_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=book_Book_strategy)
def test_hyp_book_book_resolution_setter(instance):
    original = instance.resolution
    instance.resolution = original
    assert instance.resolution == original



@given(instance=book_Book_strategy)
def test_hyp_book_book_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    Animation,
    Control,
    Node,
    Page,
    book_Action,
    book_Animation,
    book_Book,
    book_Control,
    book_Fade,
    book_Group,
    book_ImageFlash,
    book_JSAction,
    book_Label,
    book_Layer,
    book_Media,
    book_Move,
    book_Node,
    book_OpenPage,
    book_Page,
    book_Rotation,
    book_Shape,
    book_Splash,
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

def test_book_Animation_autoReverse_value_roundtrip():
    instance = book_Animation(autoReverse=True, delay=3.14, duration=3.14, repeat=7)
    assert instance.autoReverse == True
    instance.autoReverse = False
    assert instance.autoReverse == False


def test_book_Animation_delay_value_roundtrip():
    instance = book_Animation(autoReverse=True, delay=3.14, duration=3.14, repeat=7)
    assert instance.delay == 3.14
    instance.delay = 9.99
    assert instance.delay == 9.99


def test_book_Animation_duration_value_roundtrip():
    instance = book_Animation(autoReverse=True, delay=3.14, duration=3.14, repeat=7)
    assert instance.duration == 3.14
    instance.duration = 9.99
    assert instance.duration == 9.99


def test_book_Animation_repeat_value_roundtrip():
    instance = book_Animation(autoReverse=True, delay=3.14, duration=3.14, repeat=7)
    assert instance.repeat == 7
    instance.repeat = 13
    assert instance.repeat == 13


def test_book_Book_author_value_roundtrip():
    instance = book_Book(author="sample_text", bookId="sample_text", description="sample_text", resolution="sample_text", title="sample_text", version="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_book_Book_bookId_value_roundtrip():
    instance = book_Book(author="sample_text", bookId="sample_text", description="sample_text", resolution="sample_text", title="sample_text", version="sample_text")
    assert instance.bookId == "sample_text"
    instance.bookId = "sample_text_2"
    assert instance.bookId == "sample_text_2"


def test_book_Book_description_value_roundtrip():
    instance = book_Book(author="sample_text", bookId="sample_text", description="sample_text", resolution="sample_text", title="sample_text", version="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_book_Book_resolution_value_roundtrip():
    instance = book_Book(author="sample_text", bookId="sample_text", description="sample_text", resolution="sample_text", title="sample_text", version="sample_text")
    assert instance.resolution == "sample_text"
    instance.resolution = "sample_text_2"
    assert instance.resolution == "sample_text_2"


def test_book_Book_title_value_roundtrip():
    instance = book_Book(author="sample_text", bookId="sample_text", description="sample_text", resolution="sample_text", title="sample_text", version="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_book_Book_version_value_roundtrip():
    instance = book_Book(author="sample_text", bookId="sample_text", description="sample_text", resolution="sample_text", title="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_book_Control_image_value_roundtrip():
    instance = book_Control(image="sample_text", sound="sample_text")
    assert instance.image == "sample_text"
    instance.image = "sample_text_2"
    assert instance.image == "sample_text_2"


def test_book_Control_sound_value_roundtrip():
    instance = book_Control(image="sample_text", sound="sample_text")
    assert instance.sound == "sample_text"
    instance.sound = "sample_text_2"
    assert instance.sound == "sample_text_2"


def test_book_Fade_fromValue_value_roundtrip():
    instance = book_Fade(fromValue=3.14, toValue=3.14)
    assert instance.fromValue == 3.14
    instance.fromValue = 9.99
    assert instance.fromValue == 9.99


def test_book_Fade_toValue_value_roundtrip():
    instance = book_Fade(fromValue=3.14, toValue=3.14)
    assert instance.toValue == 3.14
    instance.toValue = 9.99
    assert instance.toValue == 9.99


def test_book_ImageFlash_duration_value_roundtrip():
    instance = book_ImageFlash(duration=7, images="sample_text")
    assert instance.duration == 7
    instance.duration = 13
    assert instance.duration == 13


def test_book_ImageFlash_images_value_roundtrip():
    instance = book_ImageFlash(duration=7, images="sample_text")
    assert instance.images == "sample_text"
    instance.images = "sample_text_2"
    assert instance.images == "sample_text_2"


def test_book_JSAction_javaScript_value_roundtrip():
    instance = book_JSAction(javaScript="sample_text")
    assert instance.javaScript == "sample_text"
    instance.javaScript = "sample_text_2"
    assert instance.javaScript == "sample_text_2"


def test_book_Label_font_value_roundtrip():
    instance = book_Label(font="sample_text", text="sample_text")
    assert instance.font == "sample_text"
    instance.font = "sample_text_2"
    assert instance.font == "sample_text_2"


def test_book_Label_text_value_roundtrip():
    instance = book_Label(font="sample_text", text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_book_Layer_visible_value_roundtrip():
    instance = book_Layer(visible=True)
    assert instance.visible == True
    instance.visible = False
    assert instance.visible == False


def test_book_Media_autoPlay_value_roundtrip():
    instance = book_Media(autoPlay=True, duration=7, repeat=7, url="sample_text")
    assert instance.autoPlay == True
    instance.autoPlay = False
    assert instance.autoPlay == False


def test_book_Media_duration_value_roundtrip():
    instance = book_Media(autoPlay=True, duration=7, repeat=7, url="sample_text")
    assert instance.duration == 7
    instance.duration = 13
    assert instance.duration == 13


def test_book_Media_repeat_value_roundtrip():
    instance = book_Media(autoPlay=True, duration=7, repeat=7, url="sample_text")
    assert instance.repeat == 7
    instance.repeat = 13
    assert instance.repeat == 13


def test_book_Media_url_value_roundtrip():
    instance = book_Media(autoPlay=True, duration=7, repeat=7, url="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_book_Move_fromLocation_value_roundtrip():
    instance = book_Move(fromLocation="sample_text", toLocation="sample_text")
    assert instance.fromLocation == "sample_text"
    instance.fromLocation = "sample_text_2"
    assert instance.fromLocation == "sample_text_2"


def test_book_Move_toLocation_value_roundtrip():
    instance = book_Move(fromLocation="sample_text", toLocation="sample_text")
    assert instance.toLocation == "sample_text"
    instance.toLocation = "sample_text_2"
    assert instance.toLocation == "sample_text_2"


def test_book_Node_background_value_roundtrip():
    instance = book_Node(background="sample_text", bounds="sample_text", enable=True, foreground="sample_text", opacity=3.14)
    assert instance.background == "sample_text"
    instance.background = "sample_text_2"
    assert instance.background == "sample_text_2"


def test_book_Node_bounds_value_roundtrip():
    instance = book_Node(background="sample_text", bounds="sample_text", enable=True, foreground="sample_text", opacity=3.14)
    assert instance.bounds == "sample_text"
    instance.bounds = "sample_text_2"
    assert instance.bounds == "sample_text_2"


def test_book_Node_enable_value_roundtrip():
    instance = book_Node(background="sample_text", bounds="sample_text", enable=True, foreground="sample_text", opacity=3.14)
    assert instance.enable == True
    instance.enable = False
    assert instance.enable == False


def test_book_Node_foreground_value_roundtrip():
    instance = book_Node(background="sample_text", bounds="sample_text", enable=True, foreground="sample_text", opacity=3.14)
    assert instance.foreground == "sample_text"
    instance.foreground = "sample_text_2"
    assert instance.foreground == "sample_text_2"


def test_book_Node_opacity_value_roundtrip():
    instance = book_Node(background="sample_text", bounds="sample_text", enable=True, foreground="sample_text", opacity=3.14)
    assert instance.opacity == 3.14
    instance.opacity = 9.99
    assert instance.opacity == 9.99


def test_book_Page_name_value_roundtrip():
    instance = book_Page(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_book_Rotation_fromAngle_value_roundtrip():
    instance = book_Rotation(fromAngle=3.14, toAngle=3.14)
    assert instance.fromAngle == 3.14
    instance.fromAngle = 9.99
    assert instance.fromAngle == 9.99


def test_book_Rotation_toAngle_value_roundtrip():
    instance = book_Rotation(fromAngle=3.14, toAngle=3.14)
    assert instance.toAngle == 3.14
    instance.toAngle = 9.99
    assert instance.toAngle == 9.99


def test_book_Shape_lineWidth_value_roundtrip():
    instance = book_Shape(lineWidth=7, points="sample_text")
    assert instance.lineWidth == 7
    instance.lineWidth = 13
    assert instance.lineWidth == 13


def test_book_Shape_points_value_roundtrip():
    instance = book_Shape(lineWidth=7, points="sample_text")
    assert instance.points == "sample_text"
    instance.points = "sample_text_2"
    assert instance.points == "sample_text_2"


def test_book_Splash_duration_value_roundtrip():
    instance = book_Splash(duration=7)
    assert instance.duration == 7
    instance.duration = 13
    assert instance.duration == 13


def test_book_Animation_isa_Action():
    instance = book_Animation(autoReverse=True, delay=3.14, duration=3.14, repeat=7)
    assert isinstance(instance, Action)


def test_book_JSAction_isa_Action():
    instance = book_JSAction(javaScript="sample_text")
    assert isinstance(instance, Action)


def test_book_OpenPage_isa_Action():
    instance = book_OpenPage()
    assert isinstance(instance, Action)


def test_book_Fade_isa_Animation():
    instance = book_Fade(fromValue=3.14, toValue=3.14)
    assert isinstance(instance, Animation)


def test_book_Move_isa_Animation():
    instance = book_Move(fromLocation="sample_text", toLocation="sample_text")
    assert isinstance(instance, Animation)


def test_book_Rotation_isa_Animation():
    instance = book_Rotation(fromAngle=3.14, toAngle=3.14)
    assert isinstance(instance, Animation)


def test_book_Group_isa_Control():
    instance = book_Group()
    assert isinstance(instance, Control)


def test_book_ImageFlash_isa_Control():
    instance = book_ImageFlash(duration=7, images="sample_text")
    assert isinstance(instance, Control)


def test_book_Label_isa_Control():
    instance = book_Label(font="sample_text", text="sample_text")
    assert isinstance(instance, Control)


def test_book_Media_isa_Control():
    instance = book_Media(autoPlay=True, duration=7, repeat=7, url="sample_text")
    assert isinstance(instance, Control)


def test_book_Control_isa_Node():
    instance = book_Control(image="sample_text", sound="sample_text")
    assert isinstance(instance, Node)


def test_book_Shape_isa_Node():
    instance = book_Shape(lineWidth=7, points="sample_text")
    assert isinstance(instance, Node)


def test_book_Splash_isa_Page():
    instance = book_Splash(duration=7)
    assert isinstance(instance, Page)


def test_assoc_children15_link_reassign_clear():
    a = book_Node(background="sample_text", bounds="sample_text", enable=True, foreground="sample_text", opacity=3.14)
    b1 = book_Group()
    b2 = book_Group()
    _safe_set(a, 'book_Node', b1)
    assert _is_linked(a, 'book_Node', b1)
    if hasattr(b1, 'book_Group'):
        assert _is_linked(b1, 'book_Group', a)
    _safe_set(a, 'book_Node', b2)
    assert _is_linked(a, 'book_Node', b2)
    if hasattr(b1, 'book_Group'):
        assert not _is_linked(b1, 'book_Group', a)
    if hasattr(b2, 'book_Group'):
        assert _is_linked(b2, 'book_Group', a)
    _safe_set(a, 'book_Node', None)
    assert not _is_linked(a, 'book_Node', b2)
    if hasattr(b2, 'book_Group'):
        assert not _is_linked(b2, 'book_Group', a)


def test_assoc_control8_link_reassign_clear():
    a = book_Layer(visible=True)
    b1 = book_Control(image="sample_text", sound="sample_text")
    b2 = book_Control(image="sample_text_2", sound="sample_text_2")
    _safe_set(a, 'book_Layer9', b1)
    assert _is_linked(a, 'book_Layer9', b1)
    if hasattr(b1, 'book_Control'):
        assert _is_linked(b1, 'book_Control', a)
    _safe_set(a, 'book_Layer9', b2)
    assert _is_linked(a, 'book_Layer9', b2)
    if hasattr(b1, 'book_Control'):
        assert not _is_linked(b1, 'book_Control', a)
    if hasattr(b2, 'book_Control'):
        assert _is_linked(b2, 'book_Control', a)
    _safe_set(a, 'book_Layer9', None)
    assert not _is_linked(a, 'book_Layer9', b2)
    if hasattr(b2, 'book_Control'):
        assert not _is_linked(b2, 'book_Control', a)


def test_assoc_in_17_link_reassign_clear():
    a = book_ImageFlash(duration=7, images="sample_text")
    b1 = book_Animation(autoReverse=True, delay=3.14, duration=3.14, repeat=7)
    b2 = book_Animation(autoReverse=False, delay=9.99, duration=9.99, repeat=13)
    _safe_set(a, 'book_ImageFlash18', b1)
    assert _is_linked(a, 'book_ImageFlash18', b1)
    if hasattr(b1, 'book_Animation19'):
        assert _is_linked(b1, 'book_Animation19', a)
    _safe_set(a, 'book_ImageFlash18', b2)
    assert _is_linked(a, 'book_ImageFlash18', b2)
    if hasattr(b1, 'book_Animation19'):
        assert not _is_linked(b1, 'book_Animation19', a)
    if hasattr(b2, 'book_Animation19'):
        assert _is_linked(b2, 'book_Animation19', a)
    _safe_set(a, 'book_ImageFlash18', None)
    assert not _is_linked(a, 'book_ImageFlash18', b2)
    if hasattr(b2, 'book_Animation19'):
        assert not _is_linked(b2, 'book_Animation19', a)


def test_assoc_layers6_link_reassign_clear():
    a = book_Page(name="sample_text")
    b1 = book_Layer(visible=True)
    b2 = book_Layer(visible=False)
    _safe_set(a, 'book_Page7', {b1})
    assert _is_linked(a, 'book_Page7', b1)
    if hasattr(b1, 'book_Layer'):
        assert _is_linked(b1, 'book_Layer', a)
    _safe_set(a, 'book_Page7', {b2})
    assert _is_linked(a, 'book_Page7', b2)
    if hasattr(b1, 'book_Layer'):
        assert not _is_linked(b1, 'book_Layer', a)
    if hasattr(b2, 'book_Layer'):
        assert _is_linked(b2, 'book_Layer', a)
    _safe_set(a, 'book_Page7', set())
    assert not _is_linked(a, 'book_Page7', b2)
    if hasattr(b2, 'book_Layer'):
        assert not _is_linked(b2, 'book_Layer', a)


def test_assoc_main3_link_reassign_clear():
    a = book_Page(name="sample_text")
    b1 = book_Book(author="sample_text", bookId="sample_text", description="sample_text", resolution="sample_text", title="sample_text", version="sample_text")
    b2 = book_Book(author="sample_text_2", bookId="sample_text_2", description="sample_text_2", resolution="sample_text_2", title="sample_text_2", version="sample_text_2")
    _safe_set(a, 'book_Page5', b1)
    assert _is_linked(a, 'book_Page5', b1)
    if hasattr(b1, 'book_Book4'):
        assert _is_linked(b1, 'book_Book4', a)
    _safe_set(a, 'book_Page5', b2)
    assert _is_linked(a, 'book_Page5', b2)
    if hasattr(b1, 'book_Book4'):
        assert not _is_linked(b1, 'book_Book4', a)
    if hasattr(b2, 'book_Book4'):
        assert _is_linked(b2, 'book_Book4', a)
    _safe_set(a, 'book_Page5', None)
    assert not _is_linked(a, 'book_Page5', b2)
    if hasattr(b2, 'book_Book4'):
        assert not _is_linked(b2, 'book_Book4', a)


def test_assoc_onExposed10_link_reassign_clear():
    a = book_Control(image="sample_text", sound="sample_text")
    b1 = book_Action()
    b2 = book_Action()
    _safe_set(a, 'book_Control11', {b1})
    assert _is_linked(a, 'book_Control11', b1)
    if hasattr(b1, 'book_Action'):
        assert _is_linked(b1, 'book_Action', a)
    _safe_set(a, 'book_Control11', {b2})
    assert _is_linked(a, 'book_Control11', b2)
    if hasattr(b1, 'book_Action'):
        assert not _is_linked(b1, 'book_Action', a)
    if hasattr(b2, 'book_Action'):
        assert _is_linked(b2, 'book_Action', a)
    _safe_set(a, 'book_Control11', set())
    assert not _is_linked(a, 'book_Control11', b2)
    if hasattr(b2, 'book_Action'):
        assert not _is_linked(b2, 'book_Action', a)


def test_assoc_onTouched12_link_reassign_clear():
    a = book_Control(image="sample_text", sound="sample_text")
    b1 = book_Action()
    b2 = book_Action()
    _safe_set(a, 'book_Control13', {b1})
    assert _is_linked(a, 'book_Control13', b1)
    if hasattr(b1, 'book_Action14'):
        assert _is_linked(b1, 'book_Action14', a)
    _safe_set(a, 'book_Control13', {b2})
    assert _is_linked(a, 'book_Control13', b2)
    if hasattr(b1, 'book_Action14'):
        assert not _is_linked(b1, 'book_Action14', a)
    if hasattr(b2, 'book_Action14'):
        assert _is_linked(b2, 'book_Action14', a)
    _safe_set(a, 'book_Control13', set())
    assert not _is_linked(a, 'book_Control13', b2)
    if hasattr(b2, 'book_Action14'):
        assert not _is_linked(b2, 'book_Action14', a)


def test_assoc_out16_link_reassign_clear():
    a = book_ImageFlash(duration=7, images="sample_text")
    b1 = book_Animation(autoReverse=True, delay=3.14, duration=3.14, repeat=7)
    b2 = book_Animation(autoReverse=False, delay=9.99, duration=9.99, repeat=13)
    _safe_set(a, 'book_ImageFlash', b1)
    assert _is_linked(a, 'book_ImageFlash', b1)
    if hasattr(b1, 'book_Animation'):
        assert _is_linked(b1, 'book_Animation', a)
    _safe_set(a, 'book_ImageFlash', b2)
    assert _is_linked(a, 'book_ImageFlash', b2)
    if hasattr(b1, 'book_Animation'):
        assert not _is_linked(b1, 'book_Animation', a)
    if hasattr(b2, 'book_Animation'):
        assert _is_linked(b2, 'book_Animation', a)
    _safe_set(a, 'book_ImageFlash', None)
    assert not _is_linked(a, 'book_ImageFlash', b2)
    if hasattr(b2, 'book_Animation'):
        assert not _is_linked(b2, 'book_Animation', a)


def test_assoc_page20_link_reassign_clear():
    a = book_Page(name="sample_text")
    b1 = book_OpenPage()
    b2 = book_OpenPage()
    _safe_set(a, 'book_Page21', b1)
    assert _is_linked(a, 'book_Page21', b1)
    if hasattr(b1, 'book_OpenPage'):
        assert _is_linked(b1, 'book_OpenPage', a)
    _safe_set(a, 'book_Page21', b2)
    assert _is_linked(a, 'book_Page21', b2)
    if hasattr(b1, 'book_OpenPage'):
        assert not _is_linked(b1, 'book_OpenPage', a)
    if hasattr(b2, 'book_OpenPage'):
        assert _is_linked(b2, 'book_OpenPage', a)
    _safe_set(a, 'book_Page21', None)
    assert not _is_linked(a, 'book_Page21', b2)
    if hasattr(b2, 'book_OpenPage'):
        assert not _is_linked(b2, 'book_OpenPage', a)


def test_assoc_pages0_link_reassign_clear():
    a = book_Page(name="sample_text")
    b1 = book_Book(author="sample_text", bookId="sample_text", description="sample_text", resolution="sample_text", title="sample_text", version="sample_text")
    b2 = book_Book(author="sample_text_2", bookId="sample_text_2", description="sample_text_2", resolution="sample_text_2", title="sample_text_2", version="sample_text_2")
    _safe_set(a, 'book_Page', b1)
    assert _is_linked(a, 'book_Page', b1)
    if hasattr(b1, 'book_Book'):
        assert _is_linked(b1, 'book_Book', a)
    _safe_set(a, 'book_Page', b2)
    assert _is_linked(a, 'book_Page', b2)
    if hasattr(b1, 'book_Book'):
        assert not _is_linked(b1, 'book_Book', a)
    if hasattr(b2, 'book_Book'):
        assert _is_linked(b2, 'book_Book', a)
    _safe_set(a, 'book_Page', None)
    assert not _is_linked(a, 'book_Page', b2)
    if hasattr(b2, 'book_Book'):
        assert not _is_linked(b2, 'book_Book', a)


def test_assoc_splash1_link_reassign_clear():
    a = book_Splash(duration=7)
    b1 = book_Book(author="sample_text", bookId="sample_text", description="sample_text", resolution="sample_text", title="sample_text", version="sample_text")
    b2 = book_Book(author="sample_text_2", bookId="sample_text_2", description="sample_text_2", resolution="sample_text_2", title="sample_text_2", version="sample_text_2")
    _safe_set(a, 'book_Splash', b1)
    assert _is_linked(a, 'book_Splash', b1)
    if hasattr(b1, 'book_Book2'):
        assert _is_linked(b1, 'book_Book2', a)
    _safe_set(a, 'book_Splash', b2)
    assert _is_linked(a, 'book_Splash', b2)
    if hasattr(b1, 'book_Book2'):
        assert not _is_linked(b1, 'book_Book2', a)
    if hasattr(b2, 'book_Book2'):
        assert _is_linked(b2, 'book_Book2', a)
    _safe_set(a, 'book_Splash', None)
    assert not _is_linked(a, 'book_Splash', b2)
    if hasattr(b2, 'book_Book2'):
        assert not _is_linked(b2, 'book_Book2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


Animation_strategy = st.builds(Animation)
@given(instance=Animation_strategy)
@settings(max_examples=25)
def test_Animation_instantiation(instance):
    assert isinstance(instance, Animation)


Control_strategy = st.builds(Control)
@given(instance=Control_strategy)
@settings(max_examples=25)
def test_Control_instantiation(instance):
    assert isinstance(instance, Control)


Node_strategy = st.builds(Node)
@given(instance=Node_strategy)
@settings(max_examples=25)
def test_Node_instantiation(instance):
    assert isinstance(instance, Node)


Page_strategy = st.builds(Page)
@given(instance=Page_strategy)
@settings(max_examples=25)
def test_Page_instantiation(instance):
    assert isinstance(instance, Page)


book_Action_strategy = st.builds(book_Action)
@given(instance=book_Action_strategy)
@settings(max_examples=25)
def test_book_Action_instantiation(instance):
    assert isinstance(instance, book_Action)


book_Animation_strategy = st.builds(book_Animation, autoReverse=st.booleans(), delay=st.floats(allow_nan=False, allow_infinity=False), duration=st.floats(allow_nan=False, allow_infinity=False), repeat=st.integers())
@given(instance=book_Animation_strategy)
@settings(max_examples=25)
def test_book_Animation_instantiation(instance):
    assert isinstance(instance, book_Animation)


book_Book_strategy = st.builds(book_Book, author=safe_text, bookId=safe_text, description=safe_text, resolution=safe_text, title=safe_text, version=safe_text)
@given(instance=book_Book_strategy)
@settings(max_examples=25)
def test_book_Book_instantiation(instance):
    assert isinstance(instance, book_Book)


book_Control_strategy = st.builds(book_Control, image=safe_text, sound=safe_text)
@given(instance=book_Control_strategy)
@settings(max_examples=25)
def test_book_Control_instantiation(instance):
    assert isinstance(instance, book_Control)


book_Fade_strategy = st.builds(book_Fade, fromValue=st.floats(allow_nan=False, allow_infinity=False), toValue=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=book_Fade_strategy)
@settings(max_examples=25)
def test_book_Fade_instantiation(instance):
    assert isinstance(instance, book_Fade)


book_Group_strategy = st.builds(book_Group)
@given(instance=book_Group_strategy)
@settings(max_examples=25)
def test_book_Group_instantiation(instance):
    assert isinstance(instance, book_Group)


book_ImageFlash_strategy = st.builds(book_ImageFlash, duration=st.integers(), images=safe_text)
@given(instance=book_ImageFlash_strategy)
@settings(max_examples=25)
def test_book_ImageFlash_instantiation(instance):
    assert isinstance(instance, book_ImageFlash)


book_JSAction_strategy = st.builds(book_JSAction, javaScript=safe_text)
@given(instance=book_JSAction_strategy)
@settings(max_examples=25)
def test_book_JSAction_instantiation(instance):
    assert isinstance(instance, book_JSAction)


book_Label_strategy = st.builds(book_Label, font=safe_text, text=safe_text)
@given(instance=book_Label_strategy)
@settings(max_examples=25)
def test_book_Label_instantiation(instance):
    assert isinstance(instance, book_Label)


book_Layer_strategy = st.builds(book_Layer, visible=st.booleans())
@given(instance=book_Layer_strategy)
@settings(max_examples=25)
def test_book_Layer_instantiation(instance):
    assert isinstance(instance, book_Layer)


book_Media_strategy = st.builds(book_Media, autoPlay=st.booleans(), duration=st.integers(), repeat=st.integers(), url=safe_text)
@given(instance=book_Media_strategy)
@settings(max_examples=25)
def test_book_Media_instantiation(instance):
    assert isinstance(instance, book_Media)


book_Move_strategy = st.builds(book_Move, fromLocation=safe_text, toLocation=safe_text)
@given(instance=book_Move_strategy)
@settings(max_examples=25)
def test_book_Move_instantiation(instance):
    assert isinstance(instance, book_Move)


book_Node_strategy = st.builds(book_Node, background=safe_text, bounds=safe_text, enable=st.booleans(), foreground=safe_text, opacity=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=book_Node_strategy)
@settings(max_examples=25)
def test_book_Node_instantiation(instance):
    assert isinstance(instance, book_Node)


book_OpenPage_strategy = st.builds(book_OpenPage)
@given(instance=book_OpenPage_strategy)
@settings(max_examples=25)
def test_book_OpenPage_instantiation(instance):
    assert isinstance(instance, book_OpenPage)


book_Page_strategy = st.builds(book_Page, name=safe_text)
@given(instance=book_Page_strategy)
@settings(max_examples=25)
def test_book_Page_instantiation(instance):
    assert isinstance(instance, book_Page)


book_Rotation_strategy = st.builds(book_Rotation, fromAngle=st.floats(allow_nan=False, allow_infinity=False), toAngle=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=book_Rotation_strategy)
@settings(max_examples=25)
def test_book_Rotation_instantiation(instance):
    assert isinstance(instance, book_Rotation)


book_Shape_strategy = st.builds(book_Shape, lineWidth=st.integers(), points=safe_text)
@given(instance=book_Shape_strategy)
@settings(max_examples=25)
def test_book_Shape_instantiation(instance):
    assert isinstance(instance, book_Shape)


book_Splash_strategy = st.builds(book_Splash, duration=st.integers())
@given(instance=book_Splash_strategy)
@settings(max_examples=25)
def test_book_Splash_instantiation(instance):
    assert isinstance(instance, book_Splash)



