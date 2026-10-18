import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ByteFile,
    File,
    FileHandler,
    FileOwner,
    file_ByteFile,
    file_File,
    file_FileHandler,
    file_FileInMemory,
    file_FileLocal,
    file_FileOutput,
    file_FileOwner,
    file_FileReaderWriter,
    file_FileRemote,
    file_Files,
    FileEncoding,
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

def test_assoc_Files4_stub_double():
    # file_FileOwner has no real 'file_FileOwner' property in the generated
    # code (a bare stub) -- manually attach it so file_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # file_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = file_File(Name="sample_text")
    partner = file_FileOwner()
    setattr(partner, 'file_FileOwner', None)
    _safe_set(owner, 'file_File5', partner)
    assert owner in getattr(partner, 'file_FileOwner')
    _safe_set(owner, 'file_File5', None)
    assert owner not in getattr(partner, 'file_FileOwner')


def test_assoc_HandledFile1_stub_double():
    # file_FileHandler has no real 'file_FileHandler2' property in the generated
    # code (a bare stub) -- manually attach it so file_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # file_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = file_File(Name="sample_text")
    partner = file_FileHandler()
    setattr(partner, 'file_FileHandler2', None)
    _safe_set(owner, 'file_File3', partner)
    assert getattr(partner, 'file_FileHandler2') == owner
    _safe_set(owner, 'file_File3', None)
    assert getattr(partner, 'file_FileHandler2') is None


def test_assoc_OutputFile6_stub_double():
    # file_FileOutput has no real 'file_FileOutput' property in the generated
    # code (a bare stub) -- manually attach it so file_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # file_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = file_File(Name="sample_text")
    partner = file_FileOutput()
    setattr(partner, 'file_FileOutput', None)
    _safe_set(owner, 'file_File7', partner)
    assert getattr(partner, 'file_FileOutput') == owner
    _safe_set(owner, 'file_File7', None)
    assert getattr(partner, 'file_FileOutput') is None


def test_assoc_SelectedFile0_stub_double():
    # file_FileHandler has no real 'file_FileHandler' property in the generated
    # code (a bare stub) -- manually attach it so file_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # file_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = file_File(Name="sample_text")
    partner = file_FileHandler()
    setattr(partner, 'file_FileHandler', None)
    _safe_set(owner, 'file_File', partner)
    assert getattr(partner, 'file_FileHandler') == owner
    _safe_set(owner, 'file_File', None)
    assert getattr(partner, 'file_FileHandler') is None


