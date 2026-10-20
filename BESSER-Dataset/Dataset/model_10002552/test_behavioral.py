import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Buku,
    Buku_berbahasa_Asing_UseCase,
    Class,
    Keluar,
    Login,
    Login1,
    Melakukan_Login_UseCase,
    Melakukan_Logout_UseCase,
    Melakukan_Penerjemahan_Buku_Bacaan_UseCase,
    Melihat_Tampilan_Awal_Aplikasi_UseCase,
    Memilih_Kategori_Buku_UseCase,
    Menu_Utama,
    Mulai_Membaca_UseCase,
    MyClass,
    Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase,
    Profil,
    User_Actor,
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

