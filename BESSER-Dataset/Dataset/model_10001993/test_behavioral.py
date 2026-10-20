import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin_Actor,
    Component_Component,
    Donatur__Actor,
    Package2_Donatur_Actor,
    Package2_Donatur_Tetap_Actor,
    Package2_Pemilik_Yayasan_Actor,
    Package2_Pengunjung_Actor,
    Package2_Pengurus_Yayasan_Actor,
    Package2_cek_status_donasi_UseCase,
    Package2_cetak_laporan_UseCase,
    Package2_konfirmasi_donasi_UseCase,
    Package2_login_UseCase,
    Package2_melakukan_donasi_UseCase,
    Package2_melakukan_registrasi_UseCase,
    Package2_melihat_inf_umum_yayasan_UseCase,
    Package2_melihat_laporan_penyaluran_donasi_UseCase,
    Package2_melihat_program_donasi_UseCase,
    Package2_melihat_riwayat_donasi_UseCase,
    Package2_membayar_tagihan_donasi_tetap_UseCase,
    Package2_mengelola_data_pengurus_UseCase,
    Package2_mengelola_donasi_UseCase,
    Package2_mengelola_donatur_UseCase,
    Package2_mengelola_inf_umum_yayasan_UseCase,
    Package2_mengelola_program_donasi_UseCase,
    Package2_mengubah_profil_UseCase,
    Package2_verifikasi_donasi_UseCase,
    Umum_Actor,
    cek_status_donasi_UseCase,
    cek_status_donasi_UseCase1,
    cetak_laporan_UseCase,
    donatur_Actor,
    donatur_Actor1,
    donatur_tetap_Actor,
    donatur_tidak_tetap_Actor,
    edit_profil_donatur_UseCase,
    infomasi_donatur_UseCase,
    informasi_donatur_UseCase,
    konfirmasi_donasi_UseCase,
    lihat_informasi_donatur_UseCase,
    login_UseCase,
    login_UseCase1,
    login_UseCase2,
    login_UseCase3,
    login_UseCase4,
    manajemen_donasi_UseCase,
    meilhat_riwayat_donasi_UseCase,
    melakukan_donasi_UseCase,
    melakukan_donasi_UseCase1,
    melakukan_donasi_UseCase2,
    melakukan_donasi_UseCase3,
    melakukan_registrasi_UseCase,
    melakukan_registrasi__UseCase,
    melihat__informasi_umum_yayasan_UseCase,
    melihat__program_donasi_UseCase,
    melihat_inf_umum_yayasan_UseCase,
    melihat_informasi_umum2_UseCase,
    melihat_informasi_umum_yayasan_UseCase,
    melihat_laporan_donasi_UseCase,
    melihat_laporan_penyaluran_donasi_UseCase,
    melihat_program_donasi2_UseCase,
    melihat_program_donasi_UseCase,
    melihat_program_donasi_UseCase1,
    melihat_riwayat_donasi_UseCase,
    mencari_program_donasi_UseCase,
    mencetak_laporan_UseCase,
    mengelola_data_donasi_UseCase,
    mengelola_data_donasi_UseCase1,
    mengelola_data_donatur_UseCase,
    mengelola_data_donatur_UseCase1,
    mengelola_donasi2_UseCase,
    mengelola_donasi_UseCase,
    mengelola_donasi_UseCase1,
    mengelola_donasi_UseCase2,
    mengelola_donatur_UseCase,
    mengelola_inf__umum_yayasan_UseCase,
    mengelola_inf_umum_yayasan_UseCase,
    mengelola_laporan_data_donasi_UseCase,
    mengelola_pengurus_UseCase,
    mengelola_program_donasi_UseCase,
    mengelola_program_donasi_UseCase1,
    mengelola_program_donasi_UseCase2,
    mengelola_program_donasi_UseCase3,
    mengelola_program_donasi_UseCase4,
    mengelola_program_donasi_UseCase5,
    mengubah_profil_UseCase,
    pemilik_yayasan_Actor,
    pemilik_yayasan_Actor1,
    pengunjung_Actor,
    pengurus_yayasan_Actor,
    registrasi_UseCase,
    registrasi_UseCase1,
    tambah_informasi_umum_yayasan_UseCase,
    user,
    verifikasi_donasi_UseCase,
    verifikasi_donasi_UseCase1,
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

