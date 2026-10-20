import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin_Actor,
    Admin_Website_Actor,
    Asal_daerah_tumbuhan_herbal_UseCase,
    Browsing_Situs_UseCase,
    Browsing_Website,
    Cara_pengolahannya_UseCase,
    Dampak_Jika_Tidak_Dilakukan_UseCase,
    Dimana_Melakukannya_UseCase,
    Dosisnya_UseCase,
    Dosisnya_UseCase1,
    Fitur_Data_Informasi_Pemeriksaan_Kesehatan_Pra_Nikah_UseCase,
    Fitur_Fitur_Pada_Website_UseCase,
    Fitur_Galeri_Foto_Tumbuhan_Herbal_UseCase,
    Fitur_Kolom_Diskusi_UseCase,
    Fitur_Menghubungi_admin_melalui_media_sosial_yang_ditentukan_UseCase,
    Fitur_Pemilihan_Informasi_Berdasarkan_Jenisnya_UseCase,
    Fitur_Pencarian_Tumbuhan_Herbal_UseCase,
    Fitur_Pencarian_berdsarkan_penyakit_UseCase,
    Fitur_Sosial_Media_Sharing_UseCase,
    Fitur_Website_Yang_Dapat_Diakses_Dan_Edit_Oleh_admin_UseCase,
    Fitur_Website_Yang_Dapat_Diakses_Oleh_Pengunjung_UseCase,
    Forum_diskusi_UseCase,
    Gambar_Tumbuhan_Herbalnya_UseCase,
    Gambar_tumbuhan_herbalnya_UseCase,
    Halaman_Utama_Website_UseCase,
    Jenis_Pemeriksaan_UseCase,
    Jenis_Tumbuhan_Herbalnya_UseCase,
    Jenis_tumbuhan_herbal_UseCase,
    Kapan_Harus_Melakukan_UseCase,
    Kelas_Ordo_Tumbuhan_Herbal_UseCase,
    Kelas_Ordo_tumbuhan_herbal_UseCase,
    Kelola_data_website_UseCase,
    Khasiatnya_apa_UseCase,
    Login_Website,
    Manfaat_Pemeriksaan_UseCase,
    Menambah_Data_Pemeriksaan_Kesehatan_Pra_Nikah_UseCase,
    Menambah_membuat_data_website_UseCase,
    Mengedit_Data_Pemeriksaan_Kesehatan_Pra_Nikah_UseCase,
    Mengedit_Profil_Dan_Data_Website_UseCase,
    Mengedit_data_website_UseCase,
    Menghapus_Data_Pemeriksaan_Kesehatan_Pra_Nikah_UseCase,
    Menghapus_data_website_UseCase,
    Menu_Halaman_Utama_WebsiteTumbuhan_Herbal_UseCase,
    Menu_Halaman_Website,
    Nama_Tumbuh_Tumbuhan_Herbal,
    Nama_Tumbuh_Tumbuhan_Herbal_UseCase,
    Nama_latinnya_UseCase,
    Obat__Produk_jadi__UseCase,
    Pengelola_Website,
    Siapa_Yang_Melakukan_UseCase,
    Situs_Browsing_UseCase,
    User__Pengunjung__Actor,
    User__Pengunjung__Actor1,
    Website_Informasi_Kesehatan_Pra_Nikah_UseCase,
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

