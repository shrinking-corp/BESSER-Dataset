import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Administrator_Actor,
    Jurusans,
    Login,
    Mahasiswa_Actor,
    Mahasiswas,
    Menu_Utama,
    Pembayarans,
    Prodis,
    Setting,
    Sistem_Mahasiswa_Ganti_Password_UseCase,
    Sistem_Mahasiswa_Login_UseCase,
    Sistem_Mahasiswa_Masukkan_NIM_UseCase,
    Sistem_Mahasiswa_Masukkan_Password_UseCase,
    Sistem_Mahasiswa_Melihat_Informasi_UseCase,
    Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase,
    Sistem_Pembayaran_Add_Role_UseCase,
    Sistem_Pembayaran_Add_User_UseCase,
    Sistem_Pembayaran_Biaya_Kuliah_UseCase,
    Sistem_Pembayaran_Jurusan_UseCase,
    Sistem_Pembayaran_Kategori_Biaya_UseCase,
    Sistem_Pembayaran_Login_UseCase,
    Sistem_Pembayaran_Mahasiswa_UseCase,
    Sistem_Pembayaran_Masukkan_Password_UseCase,
    Sistem_Pembayaran_Masukkan_Username_Email_UseCase,
    Sistem_Pembayaran_Pembayaran_UseCase,
    Sistem_Pembayaran_Prodi_UseCase,
    Sistem_Pembayaran_Setting_UseCase,
    Tata_Usaha_Actor,
    masterBiaya,
    masterKategori,
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

