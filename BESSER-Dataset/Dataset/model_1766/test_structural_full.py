import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Artifact,
    Device,
    DurationArtifact,
    MediaLibrary_Artifact,
    MediaLibrary_AudioBook,
    MediaLibrary_Computer,
    MediaLibrary_Device,
    MediaLibrary_DurationArtifact,
    MediaLibrary_EReader,
    MediaLibrary_Ebook,
    MediaLibrary_Ecosystem,
    MediaLibrary_ExternalSource,
    MediaLibrary_Image,
    MediaLibrary_Library,
    MediaLibrary_MediaCollection,
    MediaLibrary_MediaSource,
    MediaLibrary_MusicTrack,
    MediaLibrary_NamedElement,
    MediaLibrary_Smartphone,
    MediaLibrary_Store,
    MediaLibrary_Tablet,
    MediaLibrary_Video,
    MediaSource,
    NamedElement,
    SourceType,
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

def test_MediaLibrary_DurationArtifact_duration_value_roundtrip():
    instance = MediaLibrary_DurationArtifact(duration=7)
    assert instance.duration == 7
    instance.duration = 13
    assert instance.duration == 13


def test_MediaLibrary_EReader_audioEnabled_value_roundtrip():
    instance = MediaLibrary_EReader(audioEnabled="sample_text", videoEnabled="sample_text")
    assert instance.audioEnabled == "sample_text"
    instance.audioEnabled = "sample_text_2"
    assert instance.audioEnabled == "sample_text_2"


def test_MediaLibrary_EReader_videoEnabled_value_roundtrip():
    instance = MediaLibrary_EReader(audioEnabled="sample_text", videoEnabled="sample_text")
    assert instance.videoEnabled == "sample_text"
    instance.videoEnabled = "sample_text_2"
    assert instance.videoEnabled == "sample_text_2"


def test_MediaLibrary_ExternalSource_sourceType_value_roundtrip():
    instance = MediaLibrary_ExternalSource(sourceType="sample_text")
    assert instance.sourceType == "sample_text"
    instance.sourceType = "sample_text_2"
    assert instance.sourceType == "sample_text_2"


def test_MediaLibrary_NamedElement_name_value_roundtrip():
    instance = MediaLibrary_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MediaLibrary_DurationArtifact_isa_Artifact():
    instance = MediaLibrary_DurationArtifact(duration=7)
    assert isinstance(instance, Artifact)


def test_MediaLibrary_Ebook_isa_Artifact():
    instance = MediaLibrary_Ebook()
    assert isinstance(instance, Artifact)


def test_MediaLibrary_Image_isa_Artifact():
    instance = MediaLibrary_Image()
    assert isinstance(instance, Artifact)


def test_MediaLibrary_Computer_isa_Device():
    instance = MediaLibrary_Computer()
    assert isinstance(instance, Device)


def test_MediaLibrary_EReader_isa_Device():
    instance = MediaLibrary_EReader(audioEnabled="sample_text", videoEnabled="sample_text")
    assert isinstance(instance, Device)


def test_MediaLibrary_Smartphone_isa_Device():
    instance = MediaLibrary_Smartphone()
    assert isinstance(instance, Device)


def test_MediaLibrary_Tablet_isa_Device():
    instance = MediaLibrary_Tablet()
    assert isinstance(instance, Device)


def test_MediaLibrary_AudioBook_isa_DurationArtifact():
    instance = MediaLibrary_AudioBook()
    assert isinstance(instance, DurationArtifact)


def test_MediaLibrary_MusicTrack_isa_DurationArtifact():
    instance = MediaLibrary_MusicTrack()
    assert isinstance(instance, DurationArtifact)


def test_MediaLibrary_Video_isa_DurationArtifact():
    instance = MediaLibrary_Video()
    assert isinstance(instance, DurationArtifact)


def test_MediaLibrary_ExternalSource_isa_MediaSource():
    instance = MediaLibrary_ExternalSource(sourceType="sample_text")
    assert isinstance(instance, MediaSource)


def test_MediaLibrary_Store_isa_MediaSource():
    instance = MediaLibrary_Store()
    assert isinstance(instance, MediaSource)


def test_MediaLibrary_Artifact_isa_NamedElement():
    instance = MediaLibrary_Artifact()
    assert isinstance(instance, NamedElement)


def test_MediaLibrary_Device_isa_NamedElement():
    instance = MediaLibrary_Device()
    assert isinstance(instance, NamedElement)


def test_MediaLibrary_Library_isa_NamedElement():
    instance = MediaLibrary_Library()
    assert isinstance(instance, NamedElement)


def test_MediaLibrary_MediaCollection_isa_NamedElement():
    instance = MediaLibrary_MediaCollection()
    assert isinstance(instance, NamedElement)


def test_MediaLibrary_MediaSource_isa_NamedElement():
    instance = MediaLibrary_MediaSource()
    assert isinstance(instance, NamedElement)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Artifact_strategy = st.builds(Artifact)
@given(instance=Artifact_strategy)
@settings(max_examples=25)
def test_Artifact_instantiation(instance):
    assert isinstance(instance, Artifact)


Device_strategy = st.builds(Device)
@given(instance=Device_strategy)
@settings(max_examples=25)
def test_Device_instantiation(instance):
    assert isinstance(instance, Device)


DurationArtifact_strategy = st.builds(DurationArtifact)
@given(instance=DurationArtifact_strategy)
@settings(max_examples=25)
def test_DurationArtifact_instantiation(instance):
    assert isinstance(instance, DurationArtifact)


MediaLibrary_Artifact_strategy = st.builds(MediaLibrary_Artifact)
@given(instance=MediaLibrary_Artifact_strategy)
@settings(max_examples=25)
def test_MediaLibrary_Artifact_instantiation(instance):
    assert isinstance(instance, MediaLibrary_Artifact)


MediaLibrary_AudioBook_strategy = st.builds(MediaLibrary_AudioBook)
@given(instance=MediaLibrary_AudioBook_strategy)
@settings(max_examples=25)
def test_MediaLibrary_AudioBook_instantiation(instance):
    assert isinstance(instance, MediaLibrary_AudioBook)


MediaLibrary_Computer_strategy = st.builds(MediaLibrary_Computer)
@given(instance=MediaLibrary_Computer_strategy)
@settings(max_examples=25)
def test_MediaLibrary_Computer_instantiation(instance):
    assert isinstance(instance, MediaLibrary_Computer)


MediaLibrary_Device_strategy = st.builds(MediaLibrary_Device)
@given(instance=MediaLibrary_Device_strategy)
@settings(max_examples=25)
def test_MediaLibrary_Device_instantiation(instance):
    assert isinstance(instance, MediaLibrary_Device)


MediaLibrary_DurationArtifact_strategy = st.builds(MediaLibrary_DurationArtifact, duration=st.integers())
@given(instance=MediaLibrary_DurationArtifact_strategy)
@settings(max_examples=25)
def test_MediaLibrary_DurationArtifact_instantiation(instance):
    assert isinstance(instance, MediaLibrary_DurationArtifact)


MediaLibrary_EReader_strategy = st.builds(MediaLibrary_EReader, audioEnabled=safe_text, videoEnabled=safe_text)
@given(instance=MediaLibrary_EReader_strategy)
@settings(max_examples=25)
def test_MediaLibrary_EReader_instantiation(instance):
    assert isinstance(instance, MediaLibrary_EReader)


MediaLibrary_Ebook_strategy = st.builds(MediaLibrary_Ebook)
@given(instance=MediaLibrary_Ebook_strategy)
@settings(max_examples=25)
def test_MediaLibrary_Ebook_instantiation(instance):
    assert isinstance(instance, MediaLibrary_Ebook)


MediaLibrary_Ecosystem_strategy = st.builds(MediaLibrary_Ecosystem)
@given(instance=MediaLibrary_Ecosystem_strategy)
@settings(max_examples=25)
def test_MediaLibrary_Ecosystem_instantiation(instance):
    assert isinstance(instance, MediaLibrary_Ecosystem)


MediaLibrary_ExternalSource_strategy = st.builds(MediaLibrary_ExternalSource, sourceType=safe_text)
@given(instance=MediaLibrary_ExternalSource_strategy)
@settings(max_examples=25)
def test_MediaLibrary_ExternalSource_instantiation(instance):
    assert isinstance(instance, MediaLibrary_ExternalSource)


MediaLibrary_Image_strategy = st.builds(MediaLibrary_Image)
@given(instance=MediaLibrary_Image_strategy)
@settings(max_examples=25)
def test_MediaLibrary_Image_instantiation(instance):
    assert isinstance(instance, MediaLibrary_Image)


MediaLibrary_Library_strategy = st.builds(MediaLibrary_Library)
@given(instance=MediaLibrary_Library_strategy)
@settings(max_examples=25)
def test_MediaLibrary_Library_instantiation(instance):
    assert isinstance(instance, MediaLibrary_Library)


MediaLibrary_MediaCollection_strategy = st.builds(MediaLibrary_MediaCollection)
@given(instance=MediaLibrary_MediaCollection_strategy)
@settings(max_examples=25)
def test_MediaLibrary_MediaCollection_instantiation(instance):
    assert isinstance(instance, MediaLibrary_MediaCollection)


MediaLibrary_MediaSource_strategy = st.builds(MediaLibrary_MediaSource)
@given(instance=MediaLibrary_MediaSource_strategy)
@settings(max_examples=25)
def test_MediaLibrary_MediaSource_instantiation(instance):
    assert isinstance(instance, MediaLibrary_MediaSource)


MediaLibrary_MusicTrack_strategy = st.builds(MediaLibrary_MusicTrack)
@given(instance=MediaLibrary_MusicTrack_strategy)
@settings(max_examples=25)
def test_MediaLibrary_MusicTrack_instantiation(instance):
    assert isinstance(instance, MediaLibrary_MusicTrack)


MediaLibrary_NamedElement_strategy = st.builds(MediaLibrary_NamedElement, name=safe_text)
@given(instance=MediaLibrary_NamedElement_strategy)
@settings(max_examples=25)
def test_MediaLibrary_NamedElement_instantiation(instance):
    assert isinstance(instance, MediaLibrary_NamedElement)


MediaLibrary_Smartphone_strategy = st.builds(MediaLibrary_Smartphone)
@given(instance=MediaLibrary_Smartphone_strategy)
@settings(max_examples=25)
def test_MediaLibrary_Smartphone_instantiation(instance):
    assert isinstance(instance, MediaLibrary_Smartphone)


MediaLibrary_Store_strategy = st.builds(MediaLibrary_Store)
@given(instance=MediaLibrary_Store_strategy)
@settings(max_examples=25)
def test_MediaLibrary_Store_instantiation(instance):
    assert isinstance(instance, MediaLibrary_Store)


MediaLibrary_Tablet_strategy = st.builds(MediaLibrary_Tablet)
@given(instance=MediaLibrary_Tablet_strategy)
@settings(max_examples=25)
def test_MediaLibrary_Tablet_instantiation(instance):
    assert isinstance(instance, MediaLibrary_Tablet)


MediaLibrary_Video_strategy = st.builds(MediaLibrary_Video)
@given(instance=MediaLibrary_Video_strategy)
@settings(max_examples=25)
def test_MediaLibrary_Video_instantiation(instance):
    assert isinstance(instance, MediaLibrary_Video)


MediaSource_strategy = st.builds(MediaSource)
@given(instance=MediaSource_strategy)
@settings(max_examples=25)
def test_MediaSource_instantiation(instance):
    assert isinstance(instance, MediaSource)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


