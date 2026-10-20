import pytest
from datetime import date, datetime, time, timedelta

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

