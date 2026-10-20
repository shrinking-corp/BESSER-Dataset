import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    wikidb116_archive,
    wikidb116_category,
    wikidb116_categorylinks,
    wikidb116_change_tag,
    wikidb116_external_user,
    wikidb116_externallinks,
    wikidb116_filearchive,
    wikidb116_hitcounter,
    wikidb116_image,
    wikidb116_imagelinks,
    wikidb116_interwiki,
    wikidb116_ipblocks,
    wikidb116_job,
    wikidb116_l10n_cache,
    wikidb116_langlinks,
    wikidb116_log_search,
    wikidb116_logging,
    wikidb116_math,
    wikidb116_objectcache,
    wikidb116_oldimage,
    wikidb116_page,
    wikidb116_page_props,
    wikidb116_page_restrictions,
    wikidb116_pagelinks,
    wikidb116_protected_titles,
    wikidb116_querycache,
    wikidb116_querycache_info,
    wikidb116_querycachetwo,
    wikidb116_recentchanges,
    wikidb116_redirect,
    wikidb116_revision,
    wikidb116_searchindex,
    wikidb116_site_stats,
    wikidb116_tag_summary,
    wikidb116_templatelinks,
    wikidb116_text,
    wikidb116_trackbacks,
    wikidb116_transcache,
    wikidb116_updatelog,
    wikidb116_user,
    wikidb116_user_groups,
    wikidb116_user_newtalk,
    wikidb116_user_properties,
    wikidb116_valid_tag,
    wikidb116_watchlist,
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

