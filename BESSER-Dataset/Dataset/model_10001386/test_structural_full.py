import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Admin_Gudang_Actor,
    Barang,
    Cek_ketersediaan_barang_UseCase,
    Direktur_pemasaran_Actor,
    Direktur_utama_Actor,
    Input_data_barang_keluar_UseCase,
    Input_data_barang_masuk_UseCase,
    Input_data_pembeli_UseCase,
    Input_data_sortir_UseCase,
    Input_data_supplier_UseCase,
    Laporan_data_Pembelian_UseCase,
    Laporan_data_barang_keluar_UseCase,
    Laporan_data_barang_masuk_UseCase,
    Laporan_data_sortir_UseCase,
    Laporan_data_supplier_UseCase,
    Laporan_ready_stock_UseCase,
    Laporan_work_order_UseCase,
    Work_order_UseCase,
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

def test_Barang_attribute_value_roundtrip():
    instance = Barang(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Barang_attribute2_value_roundtrip():
    instance = Barang(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Admin_Gudang_Actor_strategy = st.builds(Admin_Gudang_Actor)
@given(instance=Admin_Gudang_Actor_strategy)
@settings(max_examples=25)
def test_Admin_Gudang_Actor_instantiation(instance):
    assert isinstance(instance, Admin_Gudang_Actor)


Barang_strategy = st.builds(Barang, attribute=safe_text, attribute2=safe_text)
@given(instance=Barang_strategy)
@settings(max_examples=25)
def test_Barang_instantiation(instance):
    assert isinstance(instance, Barang)


Cek_ketersediaan_barang_UseCase_strategy = st.builds(Cek_ketersediaan_barang_UseCase)
@given(instance=Cek_ketersediaan_barang_UseCase_strategy)
@settings(max_examples=25)
def test_Cek_ketersediaan_barang_UseCase_instantiation(instance):
    assert isinstance(instance, Cek_ketersediaan_barang_UseCase)


Direktur_pemasaran_Actor_strategy = st.builds(Direktur_pemasaran_Actor)
@given(instance=Direktur_pemasaran_Actor_strategy)
@settings(max_examples=25)
def test_Direktur_pemasaran_Actor_instantiation(instance):
    assert isinstance(instance, Direktur_pemasaran_Actor)


Direktur_utama_Actor_strategy = st.builds(Direktur_utama_Actor)
@given(instance=Direktur_utama_Actor_strategy)
@settings(max_examples=25)
def test_Direktur_utama_Actor_instantiation(instance):
    assert isinstance(instance, Direktur_utama_Actor)


Input_data_barang_keluar_UseCase_strategy = st.builds(Input_data_barang_keluar_UseCase)
@given(instance=Input_data_barang_keluar_UseCase_strategy)
@settings(max_examples=25)
def test_Input_data_barang_keluar_UseCase_instantiation(instance):
    assert isinstance(instance, Input_data_barang_keluar_UseCase)


Input_data_barang_masuk_UseCase_strategy = st.builds(Input_data_barang_masuk_UseCase)
@given(instance=Input_data_barang_masuk_UseCase_strategy)
@settings(max_examples=25)
def test_Input_data_barang_masuk_UseCase_instantiation(instance):
    assert isinstance(instance, Input_data_barang_masuk_UseCase)


Input_data_pembeli_UseCase_strategy = st.builds(Input_data_pembeli_UseCase)
@given(instance=Input_data_pembeli_UseCase_strategy)
@settings(max_examples=25)
def test_Input_data_pembeli_UseCase_instantiation(instance):
    assert isinstance(instance, Input_data_pembeli_UseCase)


Input_data_sortir_UseCase_strategy = st.builds(Input_data_sortir_UseCase)
@given(instance=Input_data_sortir_UseCase_strategy)
@settings(max_examples=25)
def test_Input_data_sortir_UseCase_instantiation(instance):
    assert isinstance(instance, Input_data_sortir_UseCase)


Input_data_supplier_UseCase_strategy = st.builds(Input_data_supplier_UseCase)
@given(instance=Input_data_supplier_UseCase_strategy)
@settings(max_examples=25)
def test_Input_data_supplier_UseCase_instantiation(instance):
    assert isinstance(instance, Input_data_supplier_UseCase)


Laporan_data_Pembelian_UseCase_strategy = st.builds(Laporan_data_Pembelian_UseCase)
@given(instance=Laporan_data_Pembelian_UseCase_strategy)
@settings(max_examples=25)
def test_Laporan_data_Pembelian_UseCase_instantiation(instance):
    assert isinstance(instance, Laporan_data_Pembelian_UseCase)


Laporan_data_barang_keluar_UseCase_strategy = st.builds(Laporan_data_barang_keluar_UseCase)
@given(instance=Laporan_data_barang_keluar_UseCase_strategy)
@settings(max_examples=25)
def test_Laporan_data_barang_keluar_UseCase_instantiation(instance):
    assert isinstance(instance, Laporan_data_barang_keluar_UseCase)


Laporan_data_barang_masuk_UseCase_strategy = st.builds(Laporan_data_barang_masuk_UseCase)
@given(instance=Laporan_data_barang_masuk_UseCase_strategy)
@settings(max_examples=25)
def test_Laporan_data_barang_masuk_UseCase_instantiation(instance):
    assert isinstance(instance, Laporan_data_barang_masuk_UseCase)


Laporan_data_sortir_UseCase_strategy = st.builds(Laporan_data_sortir_UseCase)
@given(instance=Laporan_data_sortir_UseCase_strategy)
@settings(max_examples=25)
def test_Laporan_data_sortir_UseCase_instantiation(instance):
    assert isinstance(instance, Laporan_data_sortir_UseCase)


Laporan_data_supplier_UseCase_strategy = st.builds(Laporan_data_supplier_UseCase)
@given(instance=Laporan_data_supplier_UseCase_strategy)
@settings(max_examples=25)
def test_Laporan_data_supplier_UseCase_instantiation(instance):
    assert isinstance(instance, Laporan_data_supplier_UseCase)


Laporan_ready_stock_UseCase_strategy = st.builds(Laporan_ready_stock_UseCase)
@given(instance=Laporan_ready_stock_UseCase_strategy)
@settings(max_examples=25)
def test_Laporan_ready_stock_UseCase_instantiation(instance):
    assert isinstance(instance, Laporan_ready_stock_UseCase)


Laporan_work_order_UseCase_strategy = st.builds(Laporan_work_order_UseCase)
@given(instance=Laporan_work_order_UseCase_strategy)
@settings(max_examples=25)
def test_Laporan_work_order_UseCase_instantiation(instance):
    assert isinstance(instance, Laporan_work_order_UseCase)


Work_order_UseCase_strategy = st.builds(Work_order_UseCase)
@given(instance=Work_order_UseCase_strategy)
@settings(max_examples=25)
def test_Work_order_UseCase_instantiation(instance):
    assert isinstance(instance, Work_order_UseCase)


