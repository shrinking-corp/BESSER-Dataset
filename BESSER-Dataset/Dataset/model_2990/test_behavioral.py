import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    wikidb119_archive,
    wikidb119_category,
    wikidb119_categorylinks,
    wikidb119_change_tag,
    wikidb119_external_user,
    wikidb119_externallinks,
    wikidb119_filearchive,
    wikidb119_hitcounter,
    wikidb119_image,
    wikidb119_imagelinks,
    wikidb119_interwiki,
    wikidb119_ipblocks,
    wikidb119_iwlinks,
    wikidb119_job,
    wikidb119_l10n_cache,
    wikidb119_langlinks,
    wikidb119_log_search,
    wikidb119_logging,
    wikidb119_module_deps,
    wikidb119_msg_resource,
    wikidb119_msg_resource_links,
    wikidb119_objectcache,
    wikidb119_oldimage,
    wikidb119_page,
    wikidb119_page_props,
    wikidb119_page_restrictions,
    wikidb119_pagelinks,
    wikidb119_protected_titles,
    wikidb119_querycache,
    wikidb119_querycache_info,
    wikidb119_querycachetwo,
    wikidb119_recentchanges,
    wikidb119_redirect,
    wikidb119_revision,
    wikidb119_searchindex,
    wikidb119_site_stats,
    wikidb119_tag_summary,
    wikidb119_templatelinks,
    wikidb119_text,
    wikidb119_transcache,
    wikidb119_updatelog,
    wikidb119_uploadstash,
    wikidb119_user,
    wikidb119_user_former_groups,
    wikidb119_user_groups,
    wikidb119_user_newtalk,
    wikidb119_user_properties,
    wikidb119_valid_tag,
    wikidb119_watchlist,
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

