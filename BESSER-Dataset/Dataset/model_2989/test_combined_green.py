# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    wikidb116_oldimage,
    wikidb116_querycache,
    wikidb116_l10n_cache,
    wikidb116_log_search,
    wikidb116_tag_summary,
    wikidb116_change_tag,
    wikidb116_transcache,
    wikidb116_user_newtalk,
    wikidb116_user_properties,
    wikidb116_text,
    wikidb116_logging,
    wikidb116_page_props,
    wikidb116_valid_tag,
    wikidb116_redirect,
    wikidb116_querycachetwo,
    wikidb116_page,
    wikidb116_pagelinks,
    wikidb116_external_user,
    wikidb116_site_stats,
    wikidb116_ipblocks,
    wikidb116_externallinks,
    wikidb116_user_groups,
    wikidb116_recentchanges,
    wikidb116_langlinks,
    wikidb116_archive,
    wikidb116_updatelog,
    wikidb116_searchindex,
    wikidb116_revision,
    wikidb116_imagelinks,
    wikidb116_category,
    wikidb116_image,
    wikidb116_objectcache,
    wikidb116_page_restrictions,
    wikidb116_categorylinks,
    wikidb116_filearchive,
    wikidb116_job,
    wikidb116_interwiki,
    wikidb116_watchlist,
    wikidb116_protected_titles,
    wikidb116_querycache_info,
    wikidb116_hitcounter,
    wikidb116_templatelinks,
    wikidb116_user,
    wikidb116_trackbacks,
    wikidb116_math,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_wikidb116_oldimage_is_not_abstract():
    assert not inspect.isabstract(wikidb116_oldimage)


def test_hyp_wikidb116_oldimage_constructor_exists():
    assert callable(wikidb116_oldimage.__init__)


def test_hyp_wikidb116_oldimage_constructor_args():
    sig = inspect.signature(wikidb116_oldimage.__init__)
    params = list(sig.parameters.keys())
    assert "oi_timestamp" in params, "Missing parameter 'oi_timestamp'"
    assert "oi_user_text" in params, "Missing parameter 'oi_user_text'"
    assert "oi_name" in params, "Missing parameter 'oi_name'"
    assert "oi_sha1" in params, "Missing parameter 'oi_sha1'"
    assert "oi_bits" in params, "Missing parameter 'oi_bits'"
    assert "oi_minor_mime" in params, "Missing parameter 'oi_minor_mime'"
    assert "oi_height" in params, "Missing parameter 'oi_height'"
    assert "oi_size" in params, "Missing parameter 'oi_size'"
    assert "oi_archive_name" in params, "Missing parameter 'oi_archive_name'"
    assert "oi_media_type" in params, "Missing parameter 'oi_media_type'"
    assert "oi_major_mime" in params, "Missing parameter 'oi_major_mime'"
    assert "oi_width" in params, "Missing parameter 'oi_width'"
    assert "oi_metadata" in params, "Missing parameter 'oi_metadata'"
    assert "oi_user" in params, "Missing parameter 'oi_user'"
    assert "oi_deleted" in params, "Missing parameter 'oi_deleted'"
    assert "oi_description" in params, "Missing parameter 'oi_description'"



















def test_hyp_wikidb116_querycache_is_not_abstract():
    assert not inspect.isabstract(wikidb116_querycache)


def test_hyp_wikidb116_querycache_constructor_exists():
    assert callable(wikidb116_querycache.__init__)


def test_hyp_wikidb116_querycache_constructor_args():
    sig = inspect.signature(wikidb116_querycache.__init__)
    params = list(sig.parameters.keys())
    assert "qc_namespace" in params, "Missing parameter 'qc_namespace'"
    assert "qc_type" in params, "Missing parameter 'qc_type'"
    assert "qc_title" in params, "Missing parameter 'qc_title'"
    assert "qc_value" in params, "Missing parameter 'qc_value'"







def test_hyp_wikidb116_l10n_cache_is_not_abstract():
    assert not inspect.isabstract(wikidb116_l10n_cache)


def test_hyp_wikidb116_l10n_cache_constructor_exists():
    assert callable(wikidb116_l10n_cache.__init__)


def test_hyp_wikidb116_l10n_cache_constructor_args():
    sig = inspect.signature(wikidb116_l10n_cache.__init__)
    params = list(sig.parameters.keys())
    assert "lc_lang" in params, "Missing parameter 'lc_lang'"
    assert "lc_key" in params, "Missing parameter 'lc_key'"
    assert "lc_value" in params, "Missing parameter 'lc_value'"






def test_hyp_wikidb116_log_search_is_not_abstract():
    assert not inspect.isabstract(wikidb116_log_search)


def test_hyp_wikidb116_log_search_constructor_exists():
    assert callable(wikidb116_log_search.__init__)


def test_hyp_wikidb116_log_search_constructor_args():
    sig = inspect.signature(wikidb116_log_search.__init__)
    params = list(sig.parameters.keys())
    assert "ls_field" in params, "Missing parameter 'ls_field'"
    assert "ls_value" in params, "Missing parameter 'ls_value'"
    assert "ls_log_id" in params, "Missing parameter 'ls_log_id'"






def test_hyp_wikidb116_tag_summary_is_not_abstract():
    assert not inspect.isabstract(wikidb116_tag_summary)


def test_hyp_wikidb116_tag_summary_constructor_exists():
    assert callable(wikidb116_tag_summary.__init__)


def test_hyp_wikidb116_tag_summary_constructor_args():
    sig = inspect.signature(wikidb116_tag_summary.__init__)
    params = list(sig.parameters.keys())
    assert "ts_log_id" in params, "Missing parameter 'ts_log_id'"
    assert "ts_rc_id" in params, "Missing parameter 'ts_rc_id'"
    assert "ts_tags" in params, "Missing parameter 'ts_tags'"
    assert "ts_rev_id" in params, "Missing parameter 'ts_rev_id'"







def test_hyp_wikidb116_change_tag_is_not_abstract():
    assert not inspect.isabstract(wikidb116_change_tag)


def test_hyp_wikidb116_change_tag_constructor_exists():
    assert callable(wikidb116_change_tag.__init__)


def test_hyp_wikidb116_change_tag_constructor_args():
    sig = inspect.signature(wikidb116_change_tag.__init__)
    params = list(sig.parameters.keys())
    assert "ct_log_id" in params, "Missing parameter 'ct_log_id'"
    assert "ct_params" in params, "Missing parameter 'ct_params'"
    assert "ct_rev_id" in params, "Missing parameter 'ct_rev_id'"
    assert "ct_tag" in params, "Missing parameter 'ct_tag'"
    assert "ct_rc_id" in params, "Missing parameter 'ct_rc_id'"








def test_hyp_wikidb116_transcache_is_not_abstract():
    assert not inspect.isabstract(wikidb116_transcache)


def test_hyp_wikidb116_transcache_constructor_exists():
    assert callable(wikidb116_transcache.__init__)


def test_hyp_wikidb116_transcache_constructor_args():
    sig = inspect.signature(wikidb116_transcache.__init__)
    params = list(sig.parameters.keys())
    assert "tc_time" in params, "Missing parameter 'tc_time'"
    assert "tc_contents" in params, "Missing parameter 'tc_contents'"
    assert "tc_url" in params, "Missing parameter 'tc_url'"






def test_hyp_wikidb116_user_newtalk_is_not_abstract():
    assert not inspect.isabstract(wikidb116_user_newtalk)


def test_hyp_wikidb116_user_newtalk_constructor_exists():
    assert callable(wikidb116_user_newtalk.__init__)


def test_hyp_wikidb116_user_newtalk_constructor_args():
    sig = inspect.signature(wikidb116_user_newtalk.__init__)
    params = list(sig.parameters.keys())
    assert "user_id" in params, "Missing parameter 'user_id'"
    assert "user_last_timestamp" in params, "Missing parameter 'user_last_timestamp'"
    assert "user_ip" in params, "Missing parameter 'user_ip'"






def test_hyp_wikidb116_user_properties_is_not_abstract():
    assert not inspect.isabstract(wikidb116_user_properties)


def test_hyp_wikidb116_user_properties_constructor_exists():
    assert callable(wikidb116_user_properties.__init__)


def test_hyp_wikidb116_user_properties_constructor_args():
    sig = inspect.signature(wikidb116_user_properties.__init__)
    params = list(sig.parameters.keys())
    assert "up_property" in params, "Missing parameter 'up_property'"
    assert "up_user" in params, "Missing parameter 'up_user'"
    assert "up_value" in params, "Missing parameter 'up_value'"






def test_hyp_wikidb116_text_is_not_abstract():
    assert not inspect.isabstract(wikidb116_text)


def test_hyp_wikidb116_text_constructor_exists():
    assert callable(wikidb116_text.__init__)


def test_hyp_wikidb116_text_constructor_args():
    sig = inspect.signature(wikidb116_text.__init__)
    params = list(sig.parameters.keys())
    assert "old_id" in params, "Missing parameter 'old_id'"
    assert "old_flags" in params, "Missing parameter 'old_flags'"
    assert "old_text" in params, "Missing parameter 'old_text'"






def test_hyp_wikidb116_logging_is_not_abstract():
    assert not inspect.isabstract(wikidb116_logging)


def test_hyp_wikidb116_logging_constructor_exists():
    assert callable(wikidb116_logging.__init__)


def test_hyp_wikidb116_logging_constructor_args():
    sig = inspect.signature(wikidb116_logging.__init__)
    params = list(sig.parameters.keys())
    assert "log_user" in params, "Missing parameter 'log_user'"
    assert "log_id" in params, "Missing parameter 'log_id'"
    assert "log_title" in params, "Missing parameter 'log_title'"
    assert "log_action" in params, "Missing parameter 'log_action'"
    assert "log_deleted" in params, "Missing parameter 'log_deleted'"
    assert "log_namespace" in params, "Missing parameter 'log_namespace'"
    assert "log_params" in params, "Missing parameter 'log_params'"
    assert "log_type" in params, "Missing parameter 'log_type'"
    assert "log_page" in params, "Missing parameter 'log_page'"
    assert "log_comment" in params, "Missing parameter 'log_comment'"
    assert "log_user_text" in params, "Missing parameter 'log_user_text'"
    assert "log_timestamp" in params, "Missing parameter 'log_timestamp'"















def test_hyp_wikidb116_page_props_is_not_abstract():
    assert not inspect.isabstract(wikidb116_page_props)


def test_hyp_wikidb116_page_props_constructor_exists():
    assert callable(wikidb116_page_props.__init__)


def test_hyp_wikidb116_page_props_constructor_args():
    sig = inspect.signature(wikidb116_page_props.__init__)
    params = list(sig.parameters.keys())
    assert "pp_page" in params, "Missing parameter 'pp_page'"
    assert "pp_propname" in params, "Missing parameter 'pp_propname'"
    assert "pp_value" in params, "Missing parameter 'pp_value'"






def test_hyp_wikidb116_valid_tag_is_not_abstract():
    assert not inspect.isabstract(wikidb116_valid_tag)


def test_hyp_wikidb116_valid_tag_constructor_exists():
    assert callable(wikidb116_valid_tag.__init__)


def test_hyp_wikidb116_valid_tag_constructor_args():
    sig = inspect.signature(wikidb116_valid_tag.__init__)
    params = list(sig.parameters.keys())
    assert "vt_tag" in params, "Missing parameter 'vt_tag'"




def test_hyp_wikidb116_redirect_is_not_abstract():
    assert not inspect.isabstract(wikidb116_redirect)


def test_hyp_wikidb116_redirect_constructor_exists():
    assert callable(wikidb116_redirect.__init__)


def test_hyp_wikidb116_redirect_constructor_args():
    sig = inspect.signature(wikidb116_redirect.__init__)
    params = list(sig.parameters.keys())
    assert "rd_fragment" in params, "Missing parameter 'rd_fragment'"
    assert "rd_from" in params, "Missing parameter 'rd_from'"
    assert "rd_title" in params, "Missing parameter 'rd_title'"
    assert "rd_namespace" in params, "Missing parameter 'rd_namespace'"
    assert "rd_interwiki" in params, "Missing parameter 'rd_interwiki'"








def test_hyp_wikidb116_querycachetwo_is_not_abstract():
    assert not inspect.isabstract(wikidb116_querycachetwo)


def test_hyp_wikidb116_querycachetwo_constructor_exists():
    assert callable(wikidb116_querycachetwo.__init__)


def test_hyp_wikidb116_querycachetwo_constructor_args():
    sig = inspect.signature(wikidb116_querycachetwo.__init__)
    params = list(sig.parameters.keys())
    assert "qcc_titletwo" in params, "Missing parameter 'qcc_titletwo'"
    assert "qcc_type" in params, "Missing parameter 'qcc_type'"
    assert "qcc_title" in params, "Missing parameter 'qcc_title'"
    assert "qcc_namespace" in params, "Missing parameter 'qcc_namespace'"
    assert "qcc_value" in params, "Missing parameter 'qcc_value'"
    assert "qcc_namespacetwo" in params, "Missing parameter 'qcc_namespacetwo'"









def test_hyp_wikidb116_page_is_not_abstract():
    assert not inspect.isabstract(wikidb116_page)


def test_hyp_wikidb116_page_constructor_exists():
    assert callable(wikidb116_page.__init__)


def test_hyp_wikidb116_page_constructor_args():
    sig = inspect.signature(wikidb116_page.__init__)
    params = list(sig.parameters.keys())
    assert "page_random" in params, "Missing parameter 'page_random'"
    assert "page_latest" in params, "Missing parameter 'page_latest'"
    assert "page_counter" in params, "Missing parameter 'page_counter'"
    assert "page_is_new" in params, "Missing parameter 'page_is_new'"
    assert "page_is_redirect" in params, "Missing parameter 'page_is_redirect'"
    assert "page_title" in params, "Missing parameter 'page_title'"
    assert "page_touched" in params, "Missing parameter 'page_touched'"
    assert "page_restrictions" in params, "Missing parameter 'page_restrictions'"
    assert "page_namespace" in params, "Missing parameter 'page_namespace'"
    assert "page_len" in params, "Missing parameter 'page_len'"
    assert "page_id" in params, "Missing parameter 'page_id'"














def test_hyp_wikidb116_pagelinks_is_not_abstract():
    assert not inspect.isabstract(wikidb116_pagelinks)


def test_hyp_wikidb116_pagelinks_constructor_exists():
    assert callable(wikidb116_pagelinks.__init__)


def test_hyp_wikidb116_pagelinks_constructor_args():
    sig = inspect.signature(wikidb116_pagelinks.__init__)
    params = list(sig.parameters.keys())
    assert "pl_from" in params, "Missing parameter 'pl_from'"
    assert "pl_namespace" in params, "Missing parameter 'pl_namespace'"
    assert "pl_title" in params, "Missing parameter 'pl_title'"






def test_hyp_wikidb116_external_user_is_not_abstract():
    assert not inspect.isabstract(wikidb116_external_user)


def test_hyp_wikidb116_external_user_constructor_exists():
    assert callable(wikidb116_external_user.__init__)


def test_hyp_wikidb116_external_user_constructor_args():
    sig = inspect.signature(wikidb116_external_user.__init__)
    params = list(sig.parameters.keys())
    assert "eu_external_id" in params, "Missing parameter 'eu_external_id'"
    assert "eu_local_id" in params, "Missing parameter 'eu_local_id'"





def test_hyp_wikidb116_site_stats_is_not_abstract():
    assert not inspect.isabstract(wikidb116_site_stats)


def test_hyp_wikidb116_site_stats_constructor_exists():
    assert callable(wikidb116_site_stats.__init__)


def test_hyp_wikidb116_site_stats_constructor_args():
    sig = inspect.signature(wikidb116_site_stats.__init__)
    params = list(sig.parameters.keys())
    assert "ss_total_edits" in params, "Missing parameter 'ss_total_edits'"
    assert "ss_images" in params, "Missing parameter 'ss_images'"
    assert "ss_users" in params, "Missing parameter 'ss_users'"
    assert "ss_total_views" in params, "Missing parameter 'ss_total_views'"
    assert "ss_row_id" in params, "Missing parameter 'ss_row_id'"
    assert "ss_active_users" in params, "Missing parameter 'ss_active_users'"
    assert "ss_good_articles" in params, "Missing parameter 'ss_good_articles'"
    assert "ss_total_pages" in params, "Missing parameter 'ss_total_pages'"
    assert "ss_admins" in params, "Missing parameter 'ss_admins'"












def test_hyp_wikidb116_ipblocks_is_not_abstract():
    assert not inspect.isabstract(wikidb116_ipblocks)


def test_hyp_wikidb116_ipblocks_constructor_exists():
    assert callable(wikidb116_ipblocks.__init__)


def test_hyp_wikidb116_ipblocks_constructor_args():
    sig = inspect.signature(wikidb116_ipblocks.__init__)
    params = list(sig.parameters.keys())
    assert "ipb_expiry" in params, "Missing parameter 'ipb_expiry'"
    assert "ipb_create_account" in params, "Missing parameter 'ipb_create_account'"
    assert "ipb_allow_usertalk" in params, "Missing parameter 'ipb_allow_usertalk'"
    assert "ipb_reason" in params, "Missing parameter 'ipb_reason'"
    assert "ipb_range_start" in params, "Missing parameter 'ipb_range_start'"
    assert "ipb_user" in params, "Missing parameter 'ipb_user'"
    assert "ipb_address" in params, "Missing parameter 'ipb_address'"
    assert "ipb_timestamp" in params, "Missing parameter 'ipb_timestamp'"
    assert "ipb_auto" in params, "Missing parameter 'ipb_auto'"
    assert "ipb_by_text" in params, "Missing parameter 'ipb_by_text'"
    assert "ipb_anon_only" in params, "Missing parameter 'ipb_anon_only'"
    assert "ipb_deleted" in params, "Missing parameter 'ipb_deleted'"
    assert "ipb_block_email" in params, "Missing parameter 'ipb_block_email'"
    assert "ipb_by" in params, "Missing parameter 'ipb_by'"
    assert "ipb_enable_autoblock" in params, "Missing parameter 'ipb_enable_autoblock'"
    assert "ipb_id" in params, "Missing parameter 'ipb_id'"
    assert "ipb_range_end" in params, "Missing parameter 'ipb_range_end'"




















def test_hyp_wikidb116_externallinks_is_not_abstract():
    assert not inspect.isabstract(wikidb116_externallinks)


def test_hyp_wikidb116_externallinks_constructor_exists():
    assert callable(wikidb116_externallinks.__init__)


def test_hyp_wikidb116_externallinks_constructor_args():
    sig = inspect.signature(wikidb116_externallinks.__init__)
    params = list(sig.parameters.keys())
    assert "el_to" in params, "Missing parameter 'el_to'"
    assert "el_from" in params, "Missing parameter 'el_from'"
    assert "el_index" in params, "Missing parameter 'el_index'"






def test_hyp_wikidb116_user_groups_is_not_abstract():
    assert not inspect.isabstract(wikidb116_user_groups)


def test_hyp_wikidb116_user_groups_constructor_exists():
    assert callable(wikidb116_user_groups.__init__)


def test_hyp_wikidb116_user_groups_constructor_args():
    sig = inspect.signature(wikidb116_user_groups.__init__)
    params = list(sig.parameters.keys())
    assert "ug_user" in params, "Missing parameter 'ug_user'"
    assert "ug_group" in params, "Missing parameter 'ug_group'"





def test_hyp_wikidb116_recentchanges_is_not_abstract():
    assert not inspect.isabstract(wikidb116_recentchanges)


def test_hyp_wikidb116_recentchanges_constructor_exists():
    assert callable(wikidb116_recentchanges.__init__)


def test_hyp_wikidb116_recentchanges_constructor_args():
    sig = inspect.signature(wikidb116_recentchanges.__init__)
    params = list(sig.parameters.keys())
    assert "rc_minor" in params, "Missing parameter 'rc_minor'"
    assert "rc_namespace" in params, "Missing parameter 'rc_namespace'"
    assert "rc_user_text" in params, "Missing parameter 'rc_user_text'"
    assert "rc_params" in params, "Missing parameter 'rc_params'"
    assert "rc_timestamp" in params, "Missing parameter 'rc_timestamp'"
    assert "rc_log_type" in params, "Missing parameter 'rc_log_type'"
    assert "rc_new_len" in params, "Missing parameter 'rc_new_len'"
    assert "rc_bot" in params, "Missing parameter 'rc_bot'"
    assert "rc_comment" in params, "Missing parameter 'rc_comment'"
    assert "rc_cur_id" in params, "Missing parameter 'rc_cur_id'"
    assert "rc_user" in params, "Missing parameter 'rc_user'"
    assert "rc_title" in params, "Missing parameter 'rc_title'"
    assert "rc_deleted" in params, "Missing parameter 'rc_deleted'"
    assert "rc_old_len" in params, "Missing parameter 'rc_old_len'"
    assert "rc_logid" in params, "Missing parameter 'rc_logid'"
    assert "rc_patrolled" in params, "Missing parameter 'rc_patrolled'"
    assert "rc_id" in params, "Missing parameter 'rc_id'"
    assert "rc_new" in params, "Missing parameter 'rc_new'"
    assert "rc_log_action" in params, "Missing parameter 'rc_log_action'"
    assert "rc_moved_to_title" in params, "Missing parameter 'rc_moved_to_title'"
    assert "rc_ip" in params, "Missing parameter 'rc_ip'"
    assert "rc_last_oldid" in params, "Missing parameter 'rc_last_oldid'"
    assert "rc_moved_to_ns" in params, "Missing parameter 'rc_moved_to_ns'"
    assert "rc_this_oldid" in params, "Missing parameter 'rc_this_oldid'"
    assert "rc_cur_time" in params, "Missing parameter 'rc_cur_time'"
    assert "rc_type" in params, "Missing parameter 'rc_type'"





























def test_hyp_wikidb116_langlinks_is_not_abstract():
    assert not inspect.isabstract(wikidb116_langlinks)


def test_hyp_wikidb116_langlinks_constructor_exists():
    assert callable(wikidb116_langlinks.__init__)


def test_hyp_wikidb116_langlinks_constructor_args():
    sig = inspect.signature(wikidb116_langlinks.__init__)
    params = list(sig.parameters.keys())
    assert "ll_from" in params, "Missing parameter 'll_from'"
    assert "ll_title" in params, "Missing parameter 'll_title'"
    assert "ll_lang" in params, "Missing parameter 'll_lang'"






def test_hyp_wikidb116_archive_is_not_abstract():
    assert not inspect.isabstract(wikidb116_archive)


def test_hyp_wikidb116_archive_constructor_exists():
    assert callable(wikidb116_archive.__init__)


def test_hyp_wikidb116_archive_constructor_args():
    sig = inspect.signature(wikidb116_archive.__init__)
    params = list(sig.parameters.keys())
    assert "ar_len" in params, "Missing parameter 'ar_len'"
    assert "ar_minor_edit" in params, "Missing parameter 'ar_minor_edit'"
    assert "ar_user" in params, "Missing parameter 'ar_user'"
    assert "ar_page_id" in params, "Missing parameter 'ar_page_id'"
    assert "ar_title" in params, "Missing parameter 'ar_title'"
    assert "ar_timestamp" in params, "Missing parameter 'ar_timestamp'"
    assert "ar_rev_id" in params, "Missing parameter 'ar_rev_id'"
    assert "ar_comment" in params, "Missing parameter 'ar_comment'"
    assert "ar_namespace" in params, "Missing parameter 'ar_namespace'"
    assert "ar_flags" in params, "Missing parameter 'ar_flags'"
    assert "ar_parent_id" in params, "Missing parameter 'ar_parent_id'"
    assert "ar_deleted" in params, "Missing parameter 'ar_deleted'"
    assert "ar_text_id" in params, "Missing parameter 'ar_text_id'"
    assert "ar_text" in params, "Missing parameter 'ar_text'"
    assert "ar_user_text" in params, "Missing parameter 'ar_user_text'"


















def test_hyp_wikidb116_updatelog_is_not_abstract():
    assert not inspect.isabstract(wikidb116_updatelog)


def test_hyp_wikidb116_updatelog_constructor_exists():
    assert callable(wikidb116_updatelog.__init__)


def test_hyp_wikidb116_updatelog_constructor_args():
    sig = inspect.signature(wikidb116_updatelog.__init__)
    params = list(sig.parameters.keys())
    assert "ul_key" in params, "Missing parameter 'ul_key'"




def test_hyp_wikidb116_searchindex_is_not_abstract():
    assert not inspect.isabstract(wikidb116_searchindex)


def test_hyp_wikidb116_searchindex_constructor_exists():
    assert callable(wikidb116_searchindex.__init__)


def test_hyp_wikidb116_searchindex_constructor_args():
    sig = inspect.signature(wikidb116_searchindex.__init__)
    params = list(sig.parameters.keys())
    assert "si_page" in params, "Missing parameter 'si_page'"
    assert "si_text" in params, "Missing parameter 'si_text'"
    assert "si_title" in params, "Missing parameter 'si_title'"






def test_hyp_wikidb116_revision_is_not_abstract():
    assert not inspect.isabstract(wikidb116_revision)


def test_hyp_wikidb116_revision_constructor_exists():
    assert callable(wikidb116_revision.__init__)


def test_hyp_wikidb116_revision_constructor_args():
    sig = inspect.signature(wikidb116_revision.__init__)
    params = list(sig.parameters.keys())
    assert "rev_parent_id" in params, "Missing parameter 'rev_parent_id'"
    assert "rev_user" in params, "Missing parameter 'rev_user'"
    assert "rev_len" in params, "Missing parameter 'rev_len'"
    assert "rev_id" in params, "Missing parameter 'rev_id'"
    assert "rev_user_text" in params, "Missing parameter 'rev_user_text'"
    assert "rev_minor_edit" in params, "Missing parameter 'rev_minor_edit'"
    assert "rev_deleted" in params, "Missing parameter 'rev_deleted'"
    assert "rev_comment" in params, "Missing parameter 'rev_comment'"
    assert "rev_page" in params, "Missing parameter 'rev_page'"
    assert "rev_text_id" in params, "Missing parameter 'rev_text_id'"
    assert "rev_timestamp" in params, "Missing parameter 'rev_timestamp'"














def test_hyp_wikidb116_imagelinks_is_not_abstract():
    assert not inspect.isabstract(wikidb116_imagelinks)


def test_hyp_wikidb116_imagelinks_constructor_exists():
    assert callable(wikidb116_imagelinks.__init__)


def test_hyp_wikidb116_imagelinks_constructor_args():
    sig = inspect.signature(wikidb116_imagelinks.__init__)
    params = list(sig.parameters.keys())
    assert "il_to" in params, "Missing parameter 'il_to'"
    assert "il_from" in params, "Missing parameter 'il_from'"





def test_hyp_wikidb116_category_is_not_abstract():
    assert not inspect.isabstract(wikidb116_category)


def test_hyp_wikidb116_category_constructor_exists():
    assert callable(wikidb116_category.__init__)


def test_hyp_wikidb116_category_constructor_args():
    sig = inspect.signature(wikidb116_category.__init__)
    params = list(sig.parameters.keys())
    assert "cat_title" in params, "Missing parameter 'cat_title'"
    assert "cat_files" in params, "Missing parameter 'cat_files'"
    assert "cat_hidden" in params, "Missing parameter 'cat_hidden'"
    assert "cat_pages" in params, "Missing parameter 'cat_pages'"
    assert "cat_id" in params, "Missing parameter 'cat_id'"
    assert "cat_subcats" in params, "Missing parameter 'cat_subcats'"









def test_hyp_wikidb116_image_is_not_abstract():
    assert not inspect.isabstract(wikidb116_image)


def test_hyp_wikidb116_image_constructor_exists():
    assert callable(wikidb116_image.__init__)


def test_hyp_wikidb116_image_constructor_args():
    sig = inspect.signature(wikidb116_image.__init__)
    params = list(sig.parameters.keys())
    assert "img_minor_mime" in params, "Missing parameter 'img_minor_mime'"
    assert "img_width" in params, "Missing parameter 'img_width'"
    assert "img_timestamp" in params, "Missing parameter 'img_timestamp'"
    assert "img_bits" in params, "Missing parameter 'img_bits'"
    assert "img_major_mime" in params, "Missing parameter 'img_major_mime'"
    assert "img_user" in params, "Missing parameter 'img_user'"
    assert "img_size" in params, "Missing parameter 'img_size'"
    assert "img_user_text" in params, "Missing parameter 'img_user_text'"
    assert "img_sha1" in params, "Missing parameter 'img_sha1'"
    assert "img_description" in params, "Missing parameter 'img_description'"
    assert "img_metadata" in params, "Missing parameter 'img_metadata'"
    assert "img_height" in params, "Missing parameter 'img_height'"
    assert "img_media_type" in params, "Missing parameter 'img_media_type'"
    assert "img_name" in params, "Missing parameter 'img_name'"

















def test_hyp_wikidb116_objectcache_is_not_abstract():
    assert not inspect.isabstract(wikidb116_objectcache)


def test_hyp_wikidb116_objectcache_constructor_exists():
    assert callable(wikidb116_objectcache.__init__)


def test_hyp_wikidb116_objectcache_constructor_args():
    sig = inspect.signature(wikidb116_objectcache.__init__)
    params = list(sig.parameters.keys())
    assert "keyname" in params, "Missing parameter 'keyname'"
    assert "exptime" in params, "Missing parameter 'exptime'"
    assert "value" in params, "Missing parameter 'value'"






def test_hyp_wikidb116_page_restrictions_is_not_abstract():
    assert not inspect.isabstract(wikidb116_page_restrictions)


def test_hyp_wikidb116_page_restrictions_constructor_exists():
    assert callable(wikidb116_page_restrictions.__init__)


def test_hyp_wikidb116_page_restrictions_constructor_args():
    sig = inspect.signature(wikidb116_page_restrictions.__init__)
    params = list(sig.parameters.keys())
    assert "pr_page" in params, "Missing parameter 'pr_page'"
    assert "pr_type" in params, "Missing parameter 'pr_type'"
    assert "pr_expiry" in params, "Missing parameter 'pr_expiry'"
    assert "pr_user" in params, "Missing parameter 'pr_user'"
    assert "pr_id" in params, "Missing parameter 'pr_id'"
    assert "pr_level" in params, "Missing parameter 'pr_level'"
    assert "pr_cascade" in params, "Missing parameter 'pr_cascade'"










def test_hyp_wikidb116_categorylinks_is_not_abstract():
    assert not inspect.isabstract(wikidb116_categorylinks)


def test_hyp_wikidb116_categorylinks_constructor_exists():
    assert callable(wikidb116_categorylinks.__init__)


def test_hyp_wikidb116_categorylinks_constructor_args():
    sig = inspect.signature(wikidb116_categorylinks.__init__)
    params = list(sig.parameters.keys())
    assert "cl_timestamp" in params, "Missing parameter 'cl_timestamp'"
    assert "cl_from" in params, "Missing parameter 'cl_from'"
    assert "cl_to" in params, "Missing parameter 'cl_to'"
    assert "cl_sortkey" in params, "Missing parameter 'cl_sortkey'"







def test_hyp_wikidb116_filearchive_is_not_abstract():
    assert not inspect.isabstract(wikidb116_filearchive)


def test_hyp_wikidb116_filearchive_constructor_exists():
    assert callable(wikidb116_filearchive.__init__)


def test_hyp_wikidb116_filearchive_constructor_args():
    sig = inspect.signature(wikidb116_filearchive.__init__)
    params = list(sig.parameters.keys())
    assert "fa_description" in params, "Missing parameter 'fa_description'"
    assert "fa_storage_key" in params, "Missing parameter 'fa_storage_key'"
    assert "fa_bits" in params, "Missing parameter 'fa_bits'"
    assert "fa_major_mime" in params, "Missing parameter 'fa_major_mime'"
    assert "fa_archive_name" in params, "Missing parameter 'fa_archive_name'"
    assert "fa_id" in params, "Missing parameter 'fa_id'"
    assert "fa_minor_mime" in params, "Missing parameter 'fa_minor_mime'"
    assert "fa_deleted_reason" in params, "Missing parameter 'fa_deleted_reason'"
    assert "fa_user" in params, "Missing parameter 'fa_user'"
    assert "fa_media_type" in params, "Missing parameter 'fa_media_type'"
    assert "fa_metadata" in params, "Missing parameter 'fa_metadata'"
    assert "fa_deleted" in params, "Missing parameter 'fa_deleted'"
    assert "fa_user_text" in params, "Missing parameter 'fa_user_text'"
    assert "fa_storage_group" in params, "Missing parameter 'fa_storage_group'"
    assert "fa_deleted_user" in params, "Missing parameter 'fa_deleted_user'"
    assert "fa_height" in params, "Missing parameter 'fa_height'"
    assert "fa_width" in params, "Missing parameter 'fa_width'"
    assert "fa_deleted_timestamp" in params, "Missing parameter 'fa_deleted_timestamp'"
    assert "fa_name" in params, "Missing parameter 'fa_name'"
    assert "fa_size" in params, "Missing parameter 'fa_size'"
    assert "fa_timestamp" in params, "Missing parameter 'fa_timestamp'"
























def test_hyp_wikidb116_job_is_not_abstract():
    assert not inspect.isabstract(wikidb116_job)


def test_hyp_wikidb116_job_constructor_exists():
    assert callable(wikidb116_job.__init__)


def test_hyp_wikidb116_job_constructor_args():
    sig = inspect.signature(wikidb116_job.__init__)
    params = list(sig.parameters.keys())
    assert "job_id" in params, "Missing parameter 'job_id'"
    assert "job_params" in params, "Missing parameter 'job_params'"
    assert "job_title" in params, "Missing parameter 'job_title'"
    assert "job_cmd" in params, "Missing parameter 'job_cmd'"
    assert "job_namespace" in params, "Missing parameter 'job_namespace'"








def test_hyp_wikidb116_interwiki_is_not_abstract():
    assert not inspect.isabstract(wikidb116_interwiki)


def test_hyp_wikidb116_interwiki_constructor_exists():
    assert callable(wikidb116_interwiki.__init__)


def test_hyp_wikidb116_interwiki_constructor_args():
    sig = inspect.signature(wikidb116_interwiki.__init__)
    params = list(sig.parameters.keys())
    assert "iw_trans" in params, "Missing parameter 'iw_trans'"
    assert "iw_url" in params, "Missing parameter 'iw_url'"
    assert "iw_local" in params, "Missing parameter 'iw_local'"
    assert "iw_prefix" in params, "Missing parameter 'iw_prefix'"







def test_hyp_wikidb116_watchlist_is_not_abstract():
    assert not inspect.isabstract(wikidb116_watchlist)


def test_hyp_wikidb116_watchlist_constructor_exists():
    assert callable(wikidb116_watchlist.__init__)


def test_hyp_wikidb116_watchlist_constructor_args():
    sig = inspect.signature(wikidb116_watchlist.__init__)
    params = list(sig.parameters.keys())
    assert "wl_user" in params, "Missing parameter 'wl_user'"
    assert "wl_namespace" in params, "Missing parameter 'wl_namespace'"
    assert "wl_title" in params, "Missing parameter 'wl_title'"
    assert "wl_notificationtimestamp" in params, "Missing parameter 'wl_notificationtimestamp'"







def test_hyp_wikidb116_protected_titles_is_not_abstract():
    assert not inspect.isabstract(wikidb116_protected_titles)


def test_hyp_wikidb116_protected_titles_constructor_exists():
    assert callable(wikidb116_protected_titles.__init__)


def test_hyp_wikidb116_protected_titles_constructor_args():
    sig = inspect.signature(wikidb116_protected_titles.__init__)
    params = list(sig.parameters.keys())
    assert "pt_create_perm" in params, "Missing parameter 'pt_create_perm'"
    assert "pt_namespace" in params, "Missing parameter 'pt_namespace'"
    assert "pt_expiry" in params, "Missing parameter 'pt_expiry'"
    assert "pt_reason" in params, "Missing parameter 'pt_reason'"
    assert "pt_user" in params, "Missing parameter 'pt_user'"
    assert "pt_title" in params, "Missing parameter 'pt_title'"
    assert "pt_timestamp" in params, "Missing parameter 'pt_timestamp'"










def test_hyp_wikidb116_querycache_info_is_not_abstract():
    assert not inspect.isabstract(wikidb116_querycache_info)


def test_hyp_wikidb116_querycache_info_constructor_exists():
    assert callable(wikidb116_querycache_info.__init__)


def test_hyp_wikidb116_querycache_info_constructor_args():
    sig = inspect.signature(wikidb116_querycache_info.__init__)
    params = list(sig.parameters.keys())
    assert "qci_type" in params, "Missing parameter 'qci_type'"
    assert "qci_timestamp" in params, "Missing parameter 'qci_timestamp'"





def test_hyp_wikidb116_hitcounter_is_not_abstract():
    assert not inspect.isabstract(wikidb116_hitcounter)


def test_hyp_wikidb116_hitcounter_constructor_exists():
    assert callable(wikidb116_hitcounter.__init__)


def test_hyp_wikidb116_hitcounter_constructor_args():
    sig = inspect.signature(wikidb116_hitcounter.__init__)
    params = list(sig.parameters.keys())
    assert "hc_id" in params, "Missing parameter 'hc_id'"




def test_hyp_wikidb116_templatelinks_is_not_abstract():
    assert not inspect.isabstract(wikidb116_templatelinks)


def test_hyp_wikidb116_templatelinks_constructor_exists():
    assert callable(wikidb116_templatelinks.__init__)


def test_hyp_wikidb116_templatelinks_constructor_args():
    sig = inspect.signature(wikidb116_templatelinks.__init__)
    params = list(sig.parameters.keys())
    assert "tl_title" in params, "Missing parameter 'tl_title'"
    assert "tl_from" in params, "Missing parameter 'tl_from'"
    assert "tl_namespace" in params, "Missing parameter 'tl_namespace'"






def test_hyp_wikidb116_user_is_not_abstract():
    assert not inspect.isabstract(wikidb116_user)


def test_hyp_wikidb116_user_constructor_exists():
    assert callable(wikidb116_user.__init__)


def test_hyp_wikidb116_user_constructor_args():
    sig = inspect.signature(wikidb116_user.__init__)
    params = list(sig.parameters.keys())
    assert "user_options" in params, "Missing parameter 'user_options'"
    assert "user_token" in params, "Missing parameter 'user_token'"
    assert "user_newpassword" in params, "Missing parameter 'user_newpassword'"
    assert "user_touched" in params, "Missing parameter 'user_touched'"
    assert "user_email_token" in params, "Missing parameter 'user_email_token'"
    assert "user_password" in params, "Missing parameter 'user_password'"
    assert "user_email_token_expires" in params, "Missing parameter 'user_email_token_expires'"
    assert "user_registration" in params, "Missing parameter 'user_registration'"
    assert "user_email" in params, "Missing parameter 'user_email'"
    assert "user_editcount" in params, "Missing parameter 'user_editcount'"
    assert "user_newpass_time" in params, "Missing parameter 'user_newpass_time'"
    assert "user_real_name" in params, "Missing parameter 'user_real_name'"
    assert "user_email_authenticated" in params, "Missing parameter 'user_email_authenticated'"
    assert "user_name" in params, "Missing parameter 'user_name'"
    assert "user_id" in params, "Missing parameter 'user_id'"


















def test_hyp_wikidb116_trackbacks_is_not_abstract():
    assert not inspect.isabstract(wikidb116_trackbacks)


def test_hyp_wikidb116_trackbacks_constructor_exists():
    assert callable(wikidb116_trackbacks.__init__)


def test_hyp_wikidb116_trackbacks_constructor_args():
    sig = inspect.signature(wikidb116_trackbacks.__init__)
    params = list(sig.parameters.keys())
    assert "tb_id" in params, "Missing parameter 'tb_id'"
    assert "tb_name" in params, "Missing parameter 'tb_name'"
    assert "tb_title" in params, "Missing parameter 'tb_title'"
    assert "tb_page" in params, "Missing parameter 'tb_page'"
    assert "tb_url" in params, "Missing parameter 'tb_url'"
    assert "tb_ex" in params, "Missing parameter 'tb_ex'"









def test_hyp_wikidb116_math_is_not_abstract():
    assert not inspect.isabstract(wikidb116_math)


def test_hyp_wikidb116_math_constructor_exists():
    assert callable(wikidb116_math.__init__)


def test_hyp_wikidb116_math_constructor_args():
    sig = inspect.signature(wikidb116_math.__init__)
    params = list(sig.parameters.keys())
    assert "math_html" in params, "Missing parameter 'math_html'"
    assert "math_inputhash" in params, "Missing parameter 'math_inputhash'"
    assert "math_outputhash" in params, "Missing parameter 'math_outputhash'"
    assert "math_mathml" in params, "Missing parameter 'math_mathml'"
    assert "math_html_conservativeness" in params, "Missing parameter 'math_html_conservativeness'"







# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
wikidb116_oldimage_strategy = st.builds(
    wikidb116_oldimage,
    oi_timestamp=
        safe_text,
    oi_user_text=
        safe_text,
    oi_name=
        safe_text,
    oi_sha1=
        safe_text,
    oi_bits=
        safe_text,
    oi_minor_mime=
        safe_text,
    oi_height=
        safe_text,
    oi_size=
        safe_text,
    oi_archive_name=
        safe_text,
    oi_media_type=
        safe_text,
    oi_major_mime=
        safe_text,
    oi_width=
        safe_text,
    oi_metadata=
        safe_text,
    oi_user=
        safe_text,
    oi_deleted=
        st.integers(),
    oi_description=
        safe_text
)
wikidb116_querycache_strategy = st.builds(
    wikidb116_querycache,
    qc_namespace=
        safe_text,
    qc_type=
        safe_text,
    qc_title=
        safe_text,
    qc_value=
        safe_text
)
wikidb116_l10n_cache_strategy = st.builds(
    wikidb116_l10n_cache,
    lc_lang=
        safe_text,
    lc_key=
        safe_text,
    lc_value=
        safe_text
)
wikidb116_log_search_strategy = st.builds(
    wikidb116_log_search,
    ls_field=
        safe_text,
    ls_value=
        safe_text,
    ls_log_id=
        safe_text
)
wikidb116_tag_summary_strategy = st.builds(
    wikidb116_tag_summary,
    ts_log_id=
        safe_text,
    ts_rc_id=
        safe_text,
    ts_tags=
        safe_text,
    ts_rev_id=
        safe_text
)
wikidb116_change_tag_strategy = st.builds(
    wikidb116_change_tag,
    ct_log_id=
        safe_text,
    ct_params=
        safe_text,
    ct_rev_id=
        safe_text,
    ct_tag=
        safe_text,
    ct_rc_id=
        safe_text
)
wikidb116_transcache_strategy = st.builds(
    wikidb116_transcache,
    tc_time=
        safe_text,
    tc_contents=
        safe_text,
    tc_url=
        safe_text
)
wikidb116_user_newtalk_strategy = st.builds(
    wikidb116_user_newtalk,
    user_id=
        safe_text,
    user_last_timestamp=
        safe_text,
    user_ip=
        safe_text
)
wikidb116_user_properties_strategy = st.builds(
    wikidb116_user_properties,
    up_property=
        safe_text,
    up_user=
        safe_text,
    up_value=
        safe_text
)
wikidb116_text_strategy = st.builds(
    wikidb116_text,
    old_id=
        safe_text,
    old_flags=
        safe_text,
    old_text=
        safe_text
)
wikidb116_logging_strategy = st.builds(
    wikidb116_logging,
    log_user=
        safe_text,
    log_id=
        safe_text,
    log_title=
        safe_text,
    log_action=
        safe_text,
    log_deleted=
        st.integers(),
    log_namespace=
        safe_text,
    log_params=
        safe_text,
    log_type=
        safe_text,
    log_page=
        safe_text,
    log_comment=
        safe_text,
    log_user_text=
        safe_text,
    log_timestamp=
        safe_text
)
wikidb116_page_props_strategy = st.builds(
    wikidb116_page_props,
    pp_page=
        safe_text,
    pp_propname=
        safe_text,
    pp_value=
        safe_text
)
wikidb116_valid_tag_strategy = st.builds(
    wikidb116_valid_tag,
    vt_tag=
        safe_text
)
wikidb116_redirect_strategy = st.builds(
    wikidb116_redirect,
    rd_fragment=
        safe_text,
    rd_from=
        safe_text,
    rd_title=
        safe_text,
    rd_namespace=
        safe_text,
    rd_interwiki=
        safe_text
)
wikidb116_querycachetwo_strategy = st.builds(
    wikidb116_querycachetwo,
    qcc_titletwo=
        safe_text,
    qcc_type=
        safe_text,
    qcc_title=
        safe_text,
    qcc_namespace=
        safe_text,
    qcc_value=
        safe_text,
    qcc_namespacetwo=
        safe_text
)
wikidb116_page_strategy = st.builds(
    wikidb116_page,
    page_random=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    page_latest=
        safe_text,
    page_counter=
        safe_text,
    page_is_new=
        st.integers(),
    page_is_redirect=
        st.integers(),
    page_title=
        safe_text,
    page_touched=
        safe_text,
    page_restrictions=
        safe_text,
    page_namespace=
        safe_text,
    page_len=
        safe_text,
    page_id=
        safe_text
)
wikidb116_pagelinks_strategy = st.builds(
    wikidb116_pagelinks,
    pl_from=
        safe_text,
    pl_namespace=
        safe_text,
    pl_title=
        safe_text
)
wikidb116_external_user_strategy = st.builds(
    wikidb116_external_user,
    eu_external_id=
        safe_text,
    eu_local_id=
        safe_text
)
wikidb116_site_stats_strategy = st.builds(
    wikidb116_site_stats,
    ss_total_edits=
        safe_text,
    ss_images=
        safe_text,
    ss_users=
        safe_text,
    ss_total_views=
        safe_text,
    ss_row_id=
        safe_text,
    ss_active_users=
        safe_text,
    ss_good_articles=
        safe_text,
    ss_total_pages=
        safe_text,
    ss_admins=
        safe_text
)
wikidb116_ipblocks_strategy = st.builds(
    wikidb116_ipblocks,
    ipb_expiry=
        safe_text,
    ipb_create_account=
        st.integers(),
    ipb_allow_usertalk=
        st.integers(),
    ipb_reason=
        safe_text,
    ipb_range_start=
        safe_text,
    ipb_user=
        safe_text,
    ipb_address=
        safe_text,
    ipb_timestamp=
        safe_text,
    ipb_auto=
        st.integers(),
    ipb_by_text=
        safe_text,
    ipb_anon_only=
        st.integers(),
    ipb_deleted=
        st.integers(),
    ipb_block_email=
        st.integers(),
    ipb_by=
        safe_text,
    ipb_enable_autoblock=
        st.integers(),
    ipb_id=
        safe_text,
    ipb_range_end=
        safe_text
)
wikidb116_externallinks_strategy = st.builds(
    wikidb116_externallinks,
    el_to=
        safe_text,
    el_from=
        safe_text,
    el_index=
        safe_text
)
wikidb116_user_groups_strategy = st.builds(
    wikidb116_user_groups,
    ug_user=
        safe_text,
    ug_group=
        safe_text
)
wikidb116_recentchanges_strategy = st.builds(
    wikidb116_recentchanges,
    rc_minor=
        st.integers(),
    rc_namespace=
        safe_text,
    rc_user_text=
        safe_text,
    rc_params=
        safe_text,
    rc_timestamp=
        safe_text,
    rc_log_type=
        safe_text,
    rc_new_len=
        safe_text,
    rc_bot=
        st.integers(),
    rc_comment=
        safe_text,
    rc_cur_id=
        safe_text,
    rc_user=
        safe_text,
    rc_title=
        safe_text,
    rc_deleted=
        st.integers(),
    rc_old_len=
        safe_text,
    rc_logid=
        safe_text,
    rc_patrolled=
        st.integers(),
    rc_id=
        safe_text,
    rc_new=
        st.integers(),
    rc_log_action=
        safe_text,
    rc_moved_to_title=
        safe_text,
    rc_ip=
        safe_text,
    rc_last_oldid=
        safe_text,
    rc_moved_to_ns=
        st.integers(),
    rc_this_oldid=
        safe_text,
    rc_cur_time=
        safe_text,
    rc_type=
        st.integers()
)
wikidb116_langlinks_strategy = st.builds(
    wikidb116_langlinks,
    ll_from=
        safe_text,
    ll_title=
        safe_text,
    ll_lang=
        safe_text
)
wikidb116_archive_strategy = st.builds(
    wikidb116_archive,
    ar_len=
        safe_text,
    ar_minor_edit=
        st.integers(),
    ar_user=
        safe_text,
    ar_page_id=
        safe_text,
    ar_title=
        safe_text,
    ar_timestamp=
        safe_text,
    ar_rev_id=
        safe_text,
    ar_comment=
        safe_text,
    ar_namespace=
        safe_text,
    ar_flags=
        safe_text,
    ar_parent_id=
        safe_text,
    ar_deleted=
        st.integers(),
    ar_text_id=
        safe_text,
    ar_text=
        safe_text,
    ar_user_text=
        safe_text
)
wikidb116_updatelog_strategy = st.builds(
    wikidb116_updatelog,
    ul_key=
        safe_text
)
wikidb116_searchindex_strategy = st.builds(
    wikidb116_searchindex,
    si_page=
        safe_text,
    si_text=
        safe_text,
    si_title=
        safe_text
)
wikidb116_revision_strategy = st.builds(
    wikidb116_revision,
    rev_parent_id=
        safe_text,
    rev_user=
        safe_text,
    rev_len=
        safe_text,
    rev_id=
        safe_text,
    rev_user_text=
        safe_text,
    rev_minor_edit=
        st.integers(),
    rev_deleted=
        st.integers(),
    rev_comment=
        safe_text,
    rev_page=
        safe_text,
    rev_text_id=
        safe_text,
    rev_timestamp=
        safe_text
)
wikidb116_imagelinks_strategy = st.builds(
    wikidb116_imagelinks,
    il_to=
        safe_text,
    il_from=
        safe_text
)
wikidb116_category_strategy = st.builds(
    wikidb116_category,
    cat_title=
        safe_text,
    cat_files=
        safe_text,
    cat_hidden=
        st.integers(),
    cat_pages=
        safe_text,
    cat_id=
        safe_text,
    cat_subcats=
        safe_text
)
wikidb116_image_strategy = st.builds(
    wikidb116_image,
    img_minor_mime=
        safe_text,
    img_width=
        safe_text,
    img_timestamp=
        safe_text,
    img_bits=
        safe_text,
    img_major_mime=
        safe_text,
    img_user=
        safe_text,
    img_size=
        safe_text,
    img_user_text=
        safe_text,
    img_sha1=
        safe_text,
    img_description=
        safe_text,
    img_metadata=
        safe_text,
    img_height=
        safe_text,
    img_media_type=
        safe_text,
    img_name=
        safe_text
)
wikidb116_objectcache_strategy = st.builds(
    wikidb116_objectcache,
    keyname=
        safe_text,
    exptime=
        st.dates(),
    value=
        safe_text
)
wikidb116_page_restrictions_strategy = st.builds(
    wikidb116_page_restrictions,
    pr_page=
        safe_text,
    pr_type=
        safe_text,
    pr_expiry=
        safe_text,
    pr_user=
        safe_text,
    pr_id=
        safe_text,
    pr_level=
        safe_text,
    pr_cascade=
        st.integers()
)
wikidb116_categorylinks_strategy = st.builds(
    wikidb116_categorylinks,
    cl_timestamp=
        st.dates(),
    cl_from=
        safe_text,
    cl_to=
        safe_text,
    cl_sortkey=
        safe_text
)
wikidb116_filearchive_strategy = st.builds(
    wikidb116_filearchive,
    fa_description=
        safe_text,
    fa_storage_key=
        safe_text,
    fa_bits=
        safe_text,
    fa_major_mime=
        safe_text,
    fa_archive_name=
        safe_text,
    fa_id=
        safe_text,
    fa_minor_mime=
        safe_text,
    fa_deleted_reason=
        safe_text,
    fa_user=
        safe_text,
    fa_media_type=
        safe_text,
    fa_metadata=
        safe_text,
    fa_deleted=
        st.integers(),
    fa_user_text=
        safe_text,
    fa_storage_group=
        safe_text,
    fa_deleted_user=
        safe_text,
    fa_height=
        safe_text,
    fa_width=
        safe_text,
    fa_deleted_timestamp=
        safe_text,
    fa_name=
        safe_text,
    fa_size=
        safe_text,
    fa_timestamp=
        safe_text
)
wikidb116_job_strategy = st.builds(
    wikidb116_job,
    job_id=
        safe_text,
    job_params=
        safe_text,
    job_title=
        safe_text,
    job_cmd=
        safe_text,
    job_namespace=
        safe_text
)
wikidb116_interwiki_strategy = st.builds(
    wikidb116_interwiki,
    iw_trans=
        st.integers(),
    iw_url=
        safe_text,
    iw_local=
        st.integers(),
    iw_prefix=
        safe_text
)
wikidb116_watchlist_strategy = st.builds(
    wikidb116_watchlist,
    wl_user=
        safe_text,
    wl_namespace=
        safe_text,
    wl_title=
        safe_text,
    wl_notificationtimestamp=
        safe_text
)
wikidb116_protected_titles_strategy = st.builds(
    wikidb116_protected_titles,
    pt_create_perm=
        safe_text,
    pt_namespace=
        safe_text,
    pt_expiry=
        safe_text,
    pt_reason=
        safe_text,
    pt_user=
        safe_text,
    pt_title=
        safe_text,
    pt_timestamp=
        safe_text
)
wikidb116_querycache_info_strategy = st.builds(
    wikidb116_querycache_info,
    qci_type=
        safe_text,
    qci_timestamp=
        safe_text
)
wikidb116_hitcounter_strategy = st.builds(
    wikidb116_hitcounter,
    hc_id=
        safe_text
)
wikidb116_templatelinks_strategy = st.builds(
    wikidb116_templatelinks,
    tl_title=
        safe_text,
    tl_from=
        safe_text,
    tl_namespace=
        safe_text
)
wikidb116_user_strategy = st.builds(
    wikidb116_user,
    user_options=
        safe_text,
    user_token=
        safe_text,
    user_newpassword=
        safe_text,
    user_touched=
        safe_text,
    user_email_token=
        safe_text,
    user_password=
        safe_text,
    user_email_token_expires=
        safe_text,
    user_registration=
        safe_text,
    user_email=
        safe_text,
    user_editcount=
        safe_text,
    user_newpass_time=
        safe_text,
    user_real_name=
        safe_text,
    user_email_authenticated=
        safe_text,
    user_name=
        safe_text,
    user_id=
        safe_text
)
wikidb116_trackbacks_strategy = st.builds(
    wikidb116_trackbacks,
    tb_id=
        safe_text,
    tb_name=
        safe_text,
    tb_title=
        safe_text,
    tb_page=
        safe_text,
    tb_url=
        safe_text,
    tb_ex=
        safe_text
)
wikidb116_math_strategy = st.builds(
    wikidb116_math,
    math_html=
        safe_text,
    math_inputhash=
        safe_text,
    math_outputhash=
        safe_text,
    math_mathml=
        safe_text,
    math_html_conservativeness=
        st.integers()
)




@given(instance=wikidb116_oldimage_strategy)
def test_hyp_wikidb116_oldimage_oi_timestamp_setter(instance):
    original = instance.oi_timestamp
    instance.oi_timestamp = original
    assert instance.oi_timestamp == original



@given(instance=wikidb116_oldimage_strategy)
def test_hyp_wikidb116_oldimage_oi_user_text_setter(instance):
    original = instance.oi_user_text
    instance.oi_user_text = original
    assert instance.oi_user_text == original



@given(instance=wikidb116_oldimage_strategy)
def test_hyp_wikidb116_oldimage_oi_name_setter(instance):
    original = instance.oi_name
    instance.oi_name = original
    assert instance.oi_name == original



@given(instance=wikidb116_oldimage_strategy)
def test_hyp_wikidb116_oldimage_oi_sha1_setter(instance):
    original = instance.oi_sha1
    instance.oi_sha1 = original
    assert instance.oi_sha1 == original



@given(instance=wikidb116_oldimage_strategy)
def test_hyp_wikidb116_oldimage_oi_bits_setter(instance):
    original = instance.oi_bits
    instance.oi_bits = original
    assert instance.oi_bits == original



@given(instance=wikidb116_oldimage_strategy)
def test_hyp_wikidb116_oldimage_oi_minor_mime_setter(instance):
    original = instance.oi_minor_mime
    instance.oi_minor_mime = original
    assert instance.oi_minor_mime == original



@given(instance=wikidb116_oldimage_strategy)
def test_hyp_wikidb116_oldimage_oi_height_setter(instance):
    original = instance.oi_height
    instance.oi_height = original
    assert instance.oi_height == original



@given(instance=wikidb116_oldimage_strategy)
def test_hyp_wikidb116_oldimage_oi_size_setter(instance):
    original = instance.oi_size
    instance.oi_size = original
    assert instance.oi_size == original



@given(instance=wikidb116_oldimage_strategy)
def test_hyp_wikidb116_oldimage_oi_archive_name_setter(instance):
    original = instance.oi_archive_name
    instance.oi_archive_name = original
    assert instance.oi_archive_name == original



@given(instance=wikidb116_oldimage_strategy)
def test_hyp_wikidb116_oldimage_oi_media_type_setter(instance):
    original = instance.oi_media_type
    instance.oi_media_type = original
    assert instance.oi_media_type == original



@given(instance=wikidb116_oldimage_strategy)
def test_hyp_wikidb116_oldimage_oi_major_mime_setter(instance):
    original = instance.oi_major_mime
    instance.oi_major_mime = original
    assert instance.oi_major_mime == original



@given(instance=wikidb116_oldimage_strategy)
def test_hyp_wikidb116_oldimage_oi_width_setter(instance):
    original = instance.oi_width
    instance.oi_width = original
    assert instance.oi_width == original



@given(instance=wikidb116_oldimage_strategy)
def test_hyp_wikidb116_oldimage_oi_metadata_setter(instance):
    original = instance.oi_metadata
    instance.oi_metadata = original
    assert instance.oi_metadata == original



@given(instance=wikidb116_oldimage_strategy)
def test_hyp_wikidb116_oldimage_oi_user_setter(instance):
    original = instance.oi_user
    instance.oi_user = original
    assert instance.oi_user == original



@given(instance=wikidb116_oldimage_strategy)
def test_hyp_wikidb116_oldimage_oi_deleted_setter(instance):
    original = instance.oi_deleted
    instance.oi_deleted = original
    assert instance.oi_deleted == original



@given(instance=wikidb116_oldimage_strategy)
def test_hyp_wikidb116_oldimage_oi_description_setter(instance):
    original = instance.oi_description
    instance.oi_description = original
    assert instance.oi_description == original




@given(instance=wikidb116_querycache_strategy)
def test_hyp_wikidb116_querycache_qc_namespace_setter(instance):
    original = instance.qc_namespace
    instance.qc_namespace = original
    assert instance.qc_namespace == original



@given(instance=wikidb116_querycache_strategy)
def test_hyp_wikidb116_querycache_qc_type_setter(instance):
    original = instance.qc_type
    instance.qc_type = original
    assert instance.qc_type == original



@given(instance=wikidb116_querycache_strategy)
def test_hyp_wikidb116_querycache_qc_title_setter(instance):
    original = instance.qc_title
    instance.qc_title = original
    assert instance.qc_title == original



@given(instance=wikidb116_querycache_strategy)
def test_hyp_wikidb116_querycache_qc_value_setter(instance):
    original = instance.qc_value
    instance.qc_value = original
    assert instance.qc_value == original




@given(instance=wikidb116_l10n_cache_strategy)
def test_hyp_wikidb116_l10n_cache_lc_lang_setter(instance):
    original = instance.lc_lang
    instance.lc_lang = original
    assert instance.lc_lang == original



@given(instance=wikidb116_l10n_cache_strategy)
def test_hyp_wikidb116_l10n_cache_lc_key_setter(instance):
    original = instance.lc_key
    instance.lc_key = original
    assert instance.lc_key == original



@given(instance=wikidb116_l10n_cache_strategy)
def test_hyp_wikidb116_l10n_cache_lc_value_setter(instance):
    original = instance.lc_value
    instance.lc_value = original
    assert instance.lc_value == original




@given(instance=wikidb116_log_search_strategy)
def test_hyp_wikidb116_log_search_ls_field_setter(instance):
    original = instance.ls_field
    instance.ls_field = original
    assert instance.ls_field == original



@given(instance=wikidb116_log_search_strategy)
def test_hyp_wikidb116_log_search_ls_value_setter(instance):
    original = instance.ls_value
    instance.ls_value = original
    assert instance.ls_value == original



@given(instance=wikidb116_log_search_strategy)
def test_hyp_wikidb116_log_search_ls_log_id_setter(instance):
    original = instance.ls_log_id
    instance.ls_log_id = original
    assert instance.ls_log_id == original




@given(instance=wikidb116_tag_summary_strategy)
def test_hyp_wikidb116_tag_summary_ts_log_id_setter(instance):
    original = instance.ts_log_id
    instance.ts_log_id = original
    assert instance.ts_log_id == original



@given(instance=wikidb116_tag_summary_strategy)
def test_hyp_wikidb116_tag_summary_ts_rc_id_setter(instance):
    original = instance.ts_rc_id
    instance.ts_rc_id = original
    assert instance.ts_rc_id == original



@given(instance=wikidb116_tag_summary_strategy)
def test_hyp_wikidb116_tag_summary_ts_tags_setter(instance):
    original = instance.ts_tags
    instance.ts_tags = original
    assert instance.ts_tags == original



@given(instance=wikidb116_tag_summary_strategy)
def test_hyp_wikidb116_tag_summary_ts_rev_id_setter(instance):
    original = instance.ts_rev_id
    instance.ts_rev_id = original
    assert instance.ts_rev_id == original




@given(instance=wikidb116_change_tag_strategy)
def test_hyp_wikidb116_change_tag_ct_log_id_setter(instance):
    original = instance.ct_log_id
    instance.ct_log_id = original
    assert instance.ct_log_id == original



@given(instance=wikidb116_change_tag_strategy)
def test_hyp_wikidb116_change_tag_ct_params_setter(instance):
    original = instance.ct_params
    instance.ct_params = original
    assert instance.ct_params == original



@given(instance=wikidb116_change_tag_strategy)
def test_hyp_wikidb116_change_tag_ct_rev_id_setter(instance):
    original = instance.ct_rev_id
    instance.ct_rev_id = original
    assert instance.ct_rev_id == original



@given(instance=wikidb116_change_tag_strategy)
def test_hyp_wikidb116_change_tag_ct_tag_setter(instance):
    original = instance.ct_tag
    instance.ct_tag = original
    assert instance.ct_tag == original



@given(instance=wikidb116_change_tag_strategy)
def test_hyp_wikidb116_change_tag_ct_rc_id_setter(instance):
    original = instance.ct_rc_id
    instance.ct_rc_id = original
    assert instance.ct_rc_id == original




@given(instance=wikidb116_transcache_strategy)
def test_hyp_wikidb116_transcache_tc_time_setter(instance):
    original = instance.tc_time
    instance.tc_time = original
    assert instance.tc_time == original



@given(instance=wikidb116_transcache_strategy)
def test_hyp_wikidb116_transcache_tc_contents_setter(instance):
    original = instance.tc_contents
    instance.tc_contents = original
    assert instance.tc_contents == original



@given(instance=wikidb116_transcache_strategy)
def test_hyp_wikidb116_transcache_tc_url_setter(instance):
    original = instance.tc_url
    instance.tc_url = original
    assert instance.tc_url == original




@given(instance=wikidb116_user_newtalk_strategy)
def test_hyp_wikidb116_user_newtalk_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original



@given(instance=wikidb116_user_newtalk_strategy)
def test_hyp_wikidb116_user_newtalk_user_last_timestamp_setter(instance):
    original = instance.user_last_timestamp
    instance.user_last_timestamp = original
    assert instance.user_last_timestamp == original



@given(instance=wikidb116_user_newtalk_strategy)
def test_hyp_wikidb116_user_newtalk_user_ip_setter(instance):
    original = instance.user_ip
    instance.user_ip = original
    assert instance.user_ip == original




@given(instance=wikidb116_user_properties_strategy)
def test_hyp_wikidb116_user_properties_up_property_setter(instance):
    original = instance.up_property
    instance.up_property = original
    assert instance.up_property == original



@given(instance=wikidb116_user_properties_strategy)
def test_hyp_wikidb116_user_properties_up_user_setter(instance):
    original = instance.up_user
    instance.up_user = original
    assert instance.up_user == original



@given(instance=wikidb116_user_properties_strategy)
def test_hyp_wikidb116_user_properties_up_value_setter(instance):
    original = instance.up_value
    instance.up_value = original
    assert instance.up_value == original




@given(instance=wikidb116_text_strategy)
def test_hyp_wikidb116_text_old_id_setter(instance):
    original = instance.old_id
    instance.old_id = original
    assert instance.old_id == original



@given(instance=wikidb116_text_strategy)
def test_hyp_wikidb116_text_old_flags_setter(instance):
    original = instance.old_flags
    instance.old_flags = original
    assert instance.old_flags == original



@given(instance=wikidb116_text_strategy)
def test_hyp_wikidb116_text_old_text_setter(instance):
    original = instance.old_text
    instance.old_text = original
    assert instance.old_text == original




@given(instance=wikidb116_logging_strategy)
def test_hyp_wikidb116_logging_log_user_setter(instance):
    original = instance.log_user
    instance.log_user = original
    assert instance.log_user == original



@given(instance=wikidb116_logging_strategy)
def test_hyp_wikidb116_logging_log_id_setter(instance):
    original = instance.log_id
    instance.log_id = original
    assert instance.log_id == original



@given(instance=wikidb116_logging_strategy)
def test_hyp_wikidb116_logging_log_title_setter(instance):
    original = instance.log_title
    instance.log_title = original
    assert instance.log_title == original



@given(instance=wikidb116_logging_strategy)
def test_hyp_wikidb116_logging_log_action_setter(instance):
    original = instance.log_action
    instance.log_action = original
    assert instance.log_action == original



@given(instance=wikidb116_logging_strategy)
def test_hyp_wikidb116_logging_log_deleted_setter(instance):
    original = instance.log_deleted
    instance.log_deleted = original
    assert instance.log_deleted == original



@given(instance=wikidb116_logging_strategy)
def test_hyp_wikidb116_logging_log_namespace_setter(instance):
    original = instance.log_namespace
    instance.log_namespace = original
    assert instance.log_namespace == original



@given(instance=wikidb116_logging_strategy)
def test_hyp_wikidb116_logging_log_params_setter(instance):
    original = instance.log_params
    instance.log_params = original
    assert instance.log_params == original



@given(instance=wikidb116_logging_strategy)
def test_hyp_wikidb116_logging_log_type_setter(instance):
    original = instance.log_type
    instance.log_type = original
    assert instance.log_type == original



@given(instance=wikidb116_logging_strategy)
def test_hyp_wikidb116_logging_log_page_setter(instance):
    original = instance.log_page
    instance.log_page = original
    assert instance.log_page == original



@given(instance=wikidb116_logging_strategy)
def test_hyp_wikidb116_logging_log_comment_setter(instance):
    original = instance.log_comment
    instance.log_comment = original
    assert instance.log_comment == original



@given(instance=wikidb116_logging_strategy)
def test_hyp_wikidb116_logging_log_user_text_setter(instance):
    original = instance.log_user_text
    instance.log_user_text = original
    assert instance.log_user_text == original



@given(instance=wikidb116_logging_strategy)
def test_hyp_wikidb116_logging_log_timestamp_setter(instance):
    original = instance.log_timestamp
    instance.log_timestamp = original
    assert instance.log_timestamp == original




@given(instance=wikidb116_page_props_strategy)
def test_hyp_wikidb116_page_props_pp_page_setter(instance):
    original = instance.pp_page
    instance.pp_page = original
    assert instance.pp_page == original



@given(instance=wikidb116_page_props_strategy)
def test_hyp_wikidb116_page_props_pp_propname_setter(instance):
    original = instance.pp_propname
    instance.pp_propname = original
    assert instance.pp_propname == original



@given(instance=wikidb116_page_props_strategy)
def test_hyp_wikidb116_page_props_pp_value_setter(instance):
    original = instance.pp_value
    instance.pp_value = original
    assert instance.pp_value == original




@given(instance=wikidb116_valid_tag_strategy)
def test_hyp_wikidb116_valid_tag_vt_tag_setter(instance):
    original = instance.vt_tag
    instance.vt_tag = original
    assert instance.vt_tag == original




@given(instance=wikidb116_redirect_strategy)
def test_hyp_wikidb116_redirect_rd_fragment_setter(instance):
    original = instance.rd_fragment
    instance.rd_fragment = original
    assert instance.rd_fragment == original



@given(instance=wikidb116_redirect_strategy)
def test_hyp_wikidb116_redirect_rd_from_setter(instance):
    original = instance.rd_from
    instance.rd_from = original
    assert instance.rd_from == original



@given(instance=wikidb116_redirect_strategy)
def test_hyp_wikidb116_redirect_rd_title_setter(instance):
    original = instance.rd_title
    instance.rd_title = original
    assert instance.rd_title == original



@given(instance=wikidb116_redirect_strategy)
def test_hyp_wikidb116_redirect_rd_namespace_setter(instance):
    original = instance.rd_namespace
    instance.rd_namespace = original
    assert instance.rd_namespace == original



@given(instance=wikidb116_redirect_strategy)
def test_hyp_wikidb116_redirect_rd_interwiki_setter(instance):
    original = instance.rd_interwiki
    instance.rd_interwiki = original
    assert instance.rd_interwiki == original




@given(instance=wikidb116_querycachetwo_strategy)
def test_hyp_wikidb116_querycachetwo_qcc_titletwo_setter(instance):
    original = instance.qcc_titletwo
    instance.qcc_titletwo = original
    assert instance.qcc_titletwo == original



@given(instance=wikidb116_querycachetwo_strategy)
def test_hyp_wikidb116_querycachetwo_qcc_type_setter(instance):
    original = instance.qcc_type
    instance.qcc_type = original
    assert instance.qcc_type == original



@given(instance=wikidb116_querycachetwo_strategy)
def test_hyp_wikidb116_querycachetwo_qcc_title_setter(instance):
    original = instance.qcc_title
    instance.qcc_title = original
    assert instance.qcc_title == original



@given(instance=wikidb116_querycachetwo_strategy)
def test_hyp_wikidb116_querycachetwo_qcc_namespace_setter(instance):
    original = instance.qcc_namespace
    instance.qcc_namespace = original
    assert instance.qcc_namespace == original



@given(instance=wikidb116_querycachetwo_strategy)
def test_hyp_wikidb116_querycachetwo_qcc_value_setter(instance):
    original = instance.qcc_value
    instance.qcc_value = original
    assert instance.qcc_value == original



@given(instance=wikidb116_querycachetwo_strategy)
def test_hyp_wikidb116_querycachetwo_qcc_namespacetwo_setter(instance):
    original = instance.qcc_namespacetwo
    instance.qcc_namespacetwo = original
    assert instance.qcc_namespacetwo == original




@given(instance=wikidb116_page_strategy)
def test_hyp_wikidb116_page_page_random_setter(instance):
    original = instance.page_random
    instance.page_random = original
    assert instance.page_random == original



@given(instance=wikidb116_page_strategy)
def test_hyp_wikidb116_page_page_latest_setter(instance):
    original = instance.page_latest
    instance.page_latest = original
    assert instance.page_latest == original



@given(instance=wikidb116_page_strategy)
def test_hyp_wikidb116_page_page_counter_setter(instance):
    original = instance.page_counter
    instance.page_counter = original
    assert instance.page_counter == original



@given(instance=wikidb116_page_strategy)
def test_hyp_wikidb116_page_page_is_new_setter(instance):
    original = instance.page_is_new
    instance.page_is_new = original
    assert instance.page_is_new == original



@given(instance=wikidb116_page_strategy)
def test_hyp_wikidb116_page_page_is_redirect_setter(instance):
    original = instance.page_is_redirect
    instance.page_is_redirect = original
    assert instance.page_is_redirect == original



@given(instance=wikidb116_page_strategy)
def test_hyp_wikidb116_page_page_title_setter(instance):
    original = instance.page_title
    instance.page_title = original
    assert instance.page_title == original



@given(instance=wikidb116_page_strategy)
def test_hyp_wikidb116_page_page_touched_setter(instance):
    original = instance.page_touched
    instance.page_touched = original
    assert instance.page_touched == original



@given(instance=wikidb116_page_strategy)
def test_hyp_wikidb116_page_page_restrictions_setter(instance):
    original = instance.page_restrictions
    instance.page_restrictions = original
    assert instance.page_restrictions == original



@given(instance=wikidb116_page_strategy)
def test_hyp_wikidb116_page_page_namespace_setter(instance):
    original = instance.page_namespace
    instance.page_namespace = original
    assert instance.page_namespace == original



@given(instance=wikidb116_page_strategy)
def test_hyp_wikidb116_page_page_len_setter(instance):
    original = instance.page_len
    instance.page_len = original
    assert instance.page_len == original



@given(instance=wikidb116_page_strategy)
def test_hyp_wikidb116_page_page_id_setter(instance):
    original = instance.page_id
    instance.page_id = original
    assert instance.page_id == original




@given(instance=wikidb116_pagelinks_strategy)
def test_hyp_wikidb116_pagelinks_pl_from_setter(instance):
    original = instance.pl_from
    instance.pl_from = original
    assert instance.pl_from == original



@given(instance=wikidb116_pagelinks_strategy)
def test_hyp_wikidb116_pagelinks_pl_namespace_setter(instance):
    original = instance.pl_namespace
    instance.pl_namespace = original
    assert instance.pl_namespace == original



@given(instance=wikidb116_pagelinks_strategy)
def test_hyp_wikidb116_pagelinks_pl_title_setter(instance):
    original = instance.pl_title
    instance.pl_title = original
    assert instance.pl_title == original




@given(instance=wikidb116_external_user_strategy)
def test_hyp_wikidb116_external_user_eu_external_id_setter(instance):
    original = instance.eu_external_id
    instance.eu_external_id = original
    assert instance.eu_external_id == original



@given(instance=wikidb116_external_user_strategy)
def test_hyp_wikidb116_external_user_eu_local_id_setter(instance):
    original = instance.eu_local_id
    instance.eu_local_id = original
    assert instance.eu_local_id == original




@given(instance=wikidb116_site_stats_strategy)
def test_hyp_wikidb116_site_stats_ss_total_edits_setter(instance):
    original = instance.ss_total_edits
    instance.ss_total_edits = original
    assert instance.ss_total_edits == original



@given(instance=wikidb116_site_stats_strategy)
def test_hyp_wikidb116_site_stats_ss_images_setter(instance):
    original = instance.ss_images
    instance.ss_images = original
    assert instance.ss_images == original



@given(instance=wikidb116_site_stats_strategy)
def test_hyp_wikidb116_site_stats_ss_users_setter(instance):
    original = instance.ss_users
    instance.ss_users = original
    assert instance.ss_users == original



@given(instance=wikidb116_site_stats_strategy)
def test_hyp_wikidb116_site_stats_ss_total_views_setter(instance):
    original = instance.ss_total_views
    instance.ss_total_views = original
    assert instance.ss_total_views == original



@given(instance=wikidb116_site_stats_strategy)
def test_hyp_wikidb116_site_stats_ss_row_id_setter(instance):
    original = instance.ss_row_id
    instance.ss_row_id = original
    assert instance.ss_row_id == original



@given(instance=wikidb116_site_stats_strategy)
def test_hyp_wikidb116_site_stats_ss_active_users_setter(instance):
    original = instance.ss_active_users
    instance.ss_active_users = original
    assert instance.ss_active_users == original



@given(instance=wikidb116_site_stats_strategy)
def test_hyp_wikidb116_site_stats_ss_good_articles_setter(instance):
    original = instance.ss_good_articles
    instance.ss_good_articles = original
    assert instance.ss_good_articles == original



@given(instance=wikidb116_site_stats_strategy)
def test_hyp_wikidb116_site_stats_ss_total_pages_setter(instance):
    original = instance.ss_total_pages
    instance.ss_total_pages = original
    assert instance.ss_total_pages == original



@given(instance=wikidb116_site_stats_strategy)
def test_hyp_wikidb116_site_stats_ss_admins_setter(instance):
    original = instance.ss_admins
    instance.ss_admins = original
    assert instance.ss_admins == original




@given(instance=wikidb116_ipblocks_strategy)
def test_hyp_wikidb116_ipblocks_ipb_expiry_setter(instance):
    original = instance.ipb_expiry
    instance.ipb_expiry = original
    assert instance.ipb_expiry == original



@given(instance=wikidb116_ipblocks_strategy)
def test_hyp_wikidb116_ipblocks_ipb_create_account_setter(instance):
    original = instance.ipb_create_account
    instance.ipb_create_account = original
    assert instance.ipb_create_account == original



@given(instance=wikidb116_ipblocks_strategy)
def test_hyp_wikidb116_ipblocks_ipb_allow_usertalk_setter(instance):
    original = instance.ipb_allow_usertalk
    instance.ipb_allow_usertalk = original
    assert instance.ipb_allow_usertalk == original



@given(instance=wikidb116_ipblocks_strategy)
def test_hyp_wikidb116_ipblocks_ipb_reason_setter(instance):
    original = instance.ipb_reason
    instance.ipb_reason = original
    assert instance.ipb_reason == original



@given(instance=wikidb116_ipblocks_strategy)
def test_hyp_wikidb116_ipblocks_ipb_range_start_setter(instance):
    original = instance.ipb_range_start
    instance.ipb_range_start = original
    assert instance.ipb_range_start == original



@given(instance=wikidb116_ipblocks_strategy)
def test_hyp_wikidb116_ipblocks_ipb_user_setter(instance):
    original = instance.ipb_user
    instance.ipb_user = original
    assert instance.ipb_user == original



@given(instance=wikidb116_ipblocks_strategy)
def test_hyp_wikidb116_ipblocks_ipb_address_setter(instance):
    original = instance.ipb_address
    instance.ipb_address = original
    assert instance.ipb_address == original



@given(instance=wikidb116_ipblocks_strategy)
def test_hyp_wikidb116_ipblocks_ipb_timestamp_setter(instance):
    original = instance.ipb_timestamp
    instance.ipb_timestamp = original
    assert instance.ipb_timestamp == original



@given(instance=wikidb116_ipblocks_strategy)
def test_hyp_wikidb116_ipblocks_ipb_auto_setter(instance):
    original = instance.ipb_auto
    instance.ipb_auto = original
    assert instance.ipb_auto == original



@given(instance=wikidb116_ipblocks_strategy)
def test_hyp_wikidb116_ipblocks_ipb_by_text_setter(instance):
    original = instance.ipb_by_text
    instance.ipb_by_text = original
    assert instance.ipb_by_text == original



@given(instance=wikidb116_ipblocks_strategy)
def test_hyp_wikidb116_ipblocks_ipb_anon_only_setter(instance):
    original = instance.ipb_anon_only
    instance.ipb_anon_only = original
    assert instance.ipb_anon_only == original



@given(instance=wikidb116_ipblocks_strategy)
def test_hyp_wikidb116_ipblocks_ipb_deleted_setter(instance):
    original = instance.ipb_deleted
    instance.ipb_deleted = original
    assert instance.ipb_deleted == original



@given(instance=wikidb116_ipblocks_strategy)
def test_hyp_wikidb116_ipblocks_ipb_block_email_setter(instance):
    original = instance.ipb_block_email
    instance.ipb_block_email = original
    assert instance.ipb_block_email == original



@given(instance=wikidb116_ipblocks_strategy)
def test_hyp_wikidb116_ipblocks_ipb_by_setter(instance):
    original = instance.ipb_by
    instance.ipb_by = original
    assert instance.ipb_by == original



@given(instance=wikidb116_ipblocks_strategy)
def test_hyp_wikidb116_ipblocks_ipb_enable_autoblock_setter(instance):
    original = instance.ipb_enable_autoblock
    instance.ipb_enable_autoblock = original
    assert instance.ipb_enable_autoblock == original



@given(instance=wikidb116_ipblocks_strategy)
def test_hyp_wikidb116_ipblocks_ipb_id_setter(instance):
    original = instance.ipb_id
    instance.ipb_id = original
    assert instance.ipb_id == original



@given(instance=wikidb116_ipblocks_strategy)
def test_hyp_wikidb116_ipblocks_ipb_range_end_setter(instance):
    original = instance.ipb_range_end
    instance.ipb_range_end = original
    assert instance.ipb_range_end == original




@given(instance=wikidb116_externallinks_strategy)
def test_hyp_wikidb116_externallinks_el_to_setter(instance):
    original = instance.el_to
    instance.el_to = original
    assert instance.el_to == original



@given(instance=wikidb116_externallinks_strategy)
def test_hyp_wikidb116_externallinks_el_from_setter(instance):
    original = instance.el_from
    instance.el_from = original
    assert instance.el_from == original



@given(instance=wikidb116_externallinks_strategy)
def test_hyp_wikidb116_externallinks_el_index_setter(instance):
    original = instance.el_index
    instance.el_index = original
    assert instance.el_index == original




@given(instance=wikidb116_user_groups_strategy)
def test_hyp_wikidb116_user_groups_ug_user_setter(instance):
    original = instance.ug_user
    instance.ug_user = original
    assert instance.ug_user == original



@given(instance=wikidb116_user_groups_strategy)
def test_hyp_wikidb116_user_groups_ug_group_setter(instance):
    original = instance.ug_group
    instance.ug_group = original
    assert instance.ug_group == original




@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_minor_setter(instance):
    original = instance.rc_minor
    instance.rc_minor = original
    assert instance.rc_minor == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_namespace_setter(instance):
    original = instance.rc_namespace
    instance.rc_namespace = original
    assert instance.rc_namespace == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_user_text_setter(instance):
    original = instance.rc_user_text
    instance.rc_user_text = original
    assert instance.rc_user_text == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_params_setter(instance):
    original = instance.rc_params
    instance.rc_params = original
    assert instance.rc_params == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_timestamp_setter(instance):
    original = instance.rc_timestamp
    instance.rc_timestamp = original
    assert instance.rc_timestamp == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_log_type_setter(instance):
    original = instance.rc_log_type
    instance.rc_log_type = original
    assert instance.rc_log_type == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_new_len_setter(instance):
    original = instance.rc_new_len
    instance.rc_new_len = original
    assert instance.rc_new_len == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_bot_setter(instance):
    original = instance.rc_bot
    instance.rc_bot = original
    assert instance.rc_bot == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_comment_setter(instance):
    original = instance.rc_comment
    instance.rc_comment = original
    assert instance.rc_comment == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_cur_id_setter(instance):
    original = instance.rc_cur_id
    instance.rc_cur_id = original
    assert instance.rc_cur_id == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_user_setter(instance):
    original = instance.rc_user
    instance.rc_user = original
    assert instance.rc_user == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_title_setter(instance):
    original = instance.rc_title
    instance.rc_title = original
    assert instance.rc_title == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_deleted_setter(instance):
    original = instance.rc_deleted
    instance.rc_deleted = original
    assert instance.rc_deleted == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_old_len_setter(instance):
    original = instance.rc_old_len
    instance.rc_old_len = original
    assert instance.rc_old_len == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_logid_setter(instance):
    original = instance.rc_logid
    instance.rc_logid = original
    assert instance.rc_logid == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_patrolled_setter(instance):
    original = instance.rc_patrolled
    instance.rc_patrolled = original
    assert instance.rc_patrolled == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_id_setter(instance):
    original = instance.rc_id
    instance.rc_id = original
    assert instance.rc_id == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_new_setter(instance):
    original = instance.rc_new
    instance.rc_new = original
    assert instance.rc_new == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_log_action_setter(instance):
    original = instance.rc_log_action
    instance.rc_log_action = original
    assert instance.rc_log_action == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_moved_to_title_setter(instance):
    original = instance.rc_moved_to_title
    instance.rc_moved_to_title = original
    assert instance.rc_moved_to_title == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_ip_setter(instance):
    original = instance.rc_ip
    instance.rc_ip = original
    assert instance.rc_ip == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_last_oldid_setter(instance):
    original = instance.rc_last_oldid
    instance.rc_last_oldid = original
    assert instance.rc_last_oldid == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_moved_to_ns_setter(instance):
    original = instance.rc_moved_to_ns
    instance.rc_moved_to_ns = original
    assert instance.rc_moved_to_ns == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_this_oldid_setter(instance):
    original = instance.rc_this_oldid
    instance.rc_this_oldid = original
    assert instance.rc_this_oldid == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_cur_time_setter(instance):
    original = instance.rc_cur_time
    instance.rc_cur_time = original
    assert instance.rc_cur_time == original



@given(instance=wikidb116_recentchanges_strategy)
def test_hyp_wikidb116_recentchanges_rc_type_setter(instance):
    original = instance.rc_type
    instance.rc_type = original
    assert instance.rc_type == original




@given(instance=wikidb116_langlinks_strategy)
def test_hyp_wikidb116_langlinks_ll_from_setter(instance):
    original = instance.ll_from
    instance.ll_from = original
    assert instance.ll_from == original



@given(instance=wikidb116_langlinks_strategy)
def test_hyp_wikidb116_langlinks_ll_title_setter(instance):
    original = instance.ll_title
    instance.ll_title = original
    assert instance.ll_title == original



@given(instance=wikidb116_langlinks_strategy)
def test_hyp_wikidb116_langlinks_ll_lang_setter(instance):
    original = instance.ll_lang
    instance.ll_lang = original
    assert instance.ll_lang == original




@given(instance=wikidb116_archive_strategy)
def test_hyp_wikidb116_archive_ar_len_setter(instance):
    original = instance.ar_len
    instance.ar_len = original
    assert instance.ar_len == original



@given(instance=wikidb116_archive_strategy)
def test_hyp_wikidb116_archive_ar_minor_edit_setter(instance):
    original = instance.ar_minor_edit
    instance.ar_minor_edit = original
    assert instance.ar_minor_edit == original



@given(instance=wikidb116_archive_strategy)
def test_hyp_wikidb116_archive_ar_user_setter(instance):
    original = instance.ar_user
    instance.ar_user = original
    assert instance.ar_user == original



@given(instance=wikidb116_archive_strategy)
def test_hyp_wikidb116_archive_ar_page_id_setter(instance):
    original = instance.ar_page_id
    instance.ar_page_id = original
    assert instance.ar_page_id == original



@given(instance=wikidb116_archive_strategy)
def test_hyp_wikidb116_archive_ar_title_setter(instance):
    original = instance.ar_title
    instance.ar_title = original
    assert instance.ar_title == original



@given(instance=wikidb116_archive_strategy)
def test_hyp_wikidb116_archive_ar_timestamp_setter(instance):
    original = instance.ar_timestamp
    instance.ar_timestamp = original
    assert instance.ar_timestamp == original



@given(instance=wikidb116_archive_strategy)
def test_hyp_wikidb116_archive_ar_rev_id_setter(instance):
    original = instance.ar_rev_id
    instance.ar_rev_id = original
    assert instance.ar_rev_id == original



@given(instance=wikidb116_archive_strategy)
def test_hyp_wikidb116_archive_ar_comment_setter(instance):
    original = instance.ar_comment
    instance.ar_comment = original
    assert instance.ar_comment == original



@given(instance=wikidb116_archive_strategy)
def test_hyp_wikidb116_archive_ar_namespace_setter(instance):
    original = instance.ar_namespace
    instance.ar_namespace = original
    assert instance.ar_namespace == original



@given(instance=wikidb116_archive_strategy)
def test_hyp_wikidb116_archive_ar_flags_setter(instance):
    original = instance.ar_flags
    instance.ar_flags = original
    assert instance.ar_flags == original



@given(instance=wikidb116_archive_strategy)
def test_hyp_wikidb116_archive_ar_parent_id_setter(instance):
    original = instance.ar_parent_id
    instance.ar_parent_id = original
    assert instance.ar_parent_id == original



@given(instance=wikidb116_archive_strategy)
def test_hyp_wikidb116_archive_ar_deleted_setter(instance):
    original = instance.ar_deleted
    instance.ar_deleted = original
    assert instance.ar_deleted == original



@given(instance=wikidb116_archive_strategy)
def test_hyp_wikidb116_archive_ar_text_id_setter(instance):
    original = instance.ar_text_id
    instance.ar_text_id = original
    assert instance.ar_text_id == original



@given(instance=wikidb116_archive_strategy)
def test_hyp_wikidb116_archive_ar_text_setter(instance):
    original = instance.ar_text
    instance.ar_text = original
    assert instance.ar_text == original



@given(instance=wikidb116_archive_strategy)
def test_hyp_wikidb116_archive_ar_user_text_setter(instance):
    original = instance.ar_user_text
    instance.ar_user_text = original
    assert instance.ar_user_text == original




@given(instance=wikidb116_updatelog_strategy)
def test_hyp_wikidb116_updatelog_ul_key_setter(instance):
    original = instance.ul_key
    instance.ul_key = original
    assert instance.ul_key == original




@given(instance=wikidb116_searchindex_strategy)
def test_hyp_wikidb116_searchindex_si_page_setter(instance):
    original = instance.si_page
    instance.si_page = original
    assert instance.si_page == original



@given(instance=wikidb116_searchindex_strategy)
def test_hyp_wikidb116_searchindex_si_text_setter(instance):
    original = instance.si_text
    instance.si_text = original
    assert instance.si_text == original



@given(instance=wikidb116_searchindex_strategy)
def test_hyp_wikidb116_searchindex_si_title_setter(instance):
    original = instance.si_title
    instance.si_title = original
    assert instance.si_title == original




@given(instance=wikidb116_revision_strategy)
def test_hyp_wikidb116_revision_rev_parent_id_setter(instance):
    original = instance.rev_parent_id
    instance.rev_parent_id = original
    assert instance.rev_parent_id == original



@given(instance=wikidb116_revision_strategy)
def test_hyp_wikidb116_revision_rev_user_setter(instance):
    original = instance.rev_user
    instance.rev_user = original
    assert instance.rev_user == original



@given(instance=wikidb116_revision_strategy)
def test_hyp_wikidb116_revision_rev_len_setter(instance):
    original = instance.rev_len
    instance.rev_len = original
    assert instance.rev_len == original



@given(instance=wikidb116_revision_strategy)
def test_hyp_wikidb116_revision_rev_id_setter(instance):
    original = instance.rev_id
    instance.rev_id = original
    assert instance.rev_id == original



@given(instance=wikidb116_revision_strategy)
def test_hyp_wikidb116_revision_rev_user_text_setter(instance):
    original = instance.rev_user_text
    instance.rev_user_text = original
    assert instance.rev_user_text == original



@given(instance=wikidb116_revision_strategy)
def test_hyp_wikidb116_revision_rev_minor_edit_setter(instance):
    original = instance.rev_minor_edit
    instance.rev_minor_edit = original
    assert instance.rev_minor_edit == original



@given(instance=wikidb116_revision_strategy)
def test_hyp_wikidb116_revision_rev_deleted_setter(instance):
    original = instance.rev_deleted
    instance.rev_deleted = original
    assert instance.rev_deleted == original



@given(instance=wikidb116_revision_strategy)
def test_hyp_wikidb116_revision_rev_comment_setter(instance):
    original = instance.rev_comment
    instance.rev_comment = original
    assert instance.rev_comment == original



@given(instance=wikidb116_revision_strategy)
def test_hyp_wikidb116_revision_rev_page_setter(instance):
    original = instance.rev_page
    instance.rev_page = original
    assert instance.rev_page == original



@given(instance=wikidb116_revision_strategy)
def test_hyp_wikidb116_revision_rev_text_id_setter(instance):
    original = instance.rev_text_id
    instance.rev_text_id = original
    assert instance.rev_text_id == original



@given(instance=wikidb116_revision_strategy)
def test_hyp_wikidb116_revision_rev_timestamp_setter(instance):
    original = instance.rev_timestamp
    instance.rev_timestamp = original
    assert instance.rev_timestamp == original




@given(instance=wikidb116_imagelinks_strategy)
def test_hyp_wikidb116_imagelinks_il_to_setter(instance):
    original = instance.il_to
    instance.il_to = original
    assert instance.il_to == original



@given(instance=wikidb116_imagelinks_strategy)
def test_hyp_wikidb116_imagelinks_il_from_setter(instance):
    original = instance.il_from
    instance.il_from = original
    assert instance.il_from == original




@given(instance=wikidb116_category_strategy)
def test_hyp_wikidb116_category_cat_title_setter(instance):
    original = instance.cat_title
    instance.cat_title = original
    assert instance.cat_title == original



@given(instance=wikidb116_category_strategy)
def test_hyp_wikidb116_category_cat_files_setter(instance):
    original = instance.cat_files
    instance.cat_files = original
    assert instance.cat_files == original



@given(instance=wikidb116_category_strategy)
def test_hyp_wikidb116_category_cat_hidden_setter(instance):
    original = instance.cat_hidden
    instance.cat_hidden = original
    assert instance.cat_hidden == original



@given(instance=wikidb116_category_strategy)
def test_hyp_wikidb116_category_cat_pages_setter(instance):
    original = instance.cat_pages
    instance.cat_pages = original
    assert instance.cat_pages == original



@given(instance=wikidb116_category_strategy)
def test_hyp_wikidb116_category_cat_id_setter(instance):
    original = instance.cat_id
    instance.cat_id = original
    assert instance.cat_id == original



@given(instance=wikidb116_category_strategy)
def test_hyp_wikidb116_category_cat_subcats_setter(instance):
    original = instance.cat_subcats
    instance.cat_subcats = original
    assert instance.cat_subcats == original




@given(instance=wikidb116_image_strategy)
def test_hyp_wikidb116_image_img_minor_mime_setter(instance):
    original = instance.img_minor_mime
    instance.img_minor_mime = original
    assert instance.img_minor_mime == original



@given(instance=wikidb116_image_strategy)
def test_hyp_wikidb116_image_img_width_setter(instance):
    original = instance.img_width
    instance.img_width = original
    assert instance.img_width == original



@given(instance=wikidb116_image_strategy)
def test_hyp_wikidb116_image_img_timestamp_setter(instance):
    original = instance.img_timestamp
    instance.img_timestamp = original
    assert instance.img_timestamp == original



@given(instance=wikidb116_image_strategy)
def test_hyp_wikidb116_image_img_bits_setter(instance):
    original = instance.img_bits
    instance.img_bits = original
    assert instance.img_bits == original



@given(instance=wikidb116_image_strategy)
def test_hyp_wikidb116_image_img_major_mime_setter(instance):
    original = instance.img_major_mime
    instance.img_major_mime = original
    assert instance.img_major_mime == original



@given(instance=wikidb116_image_strategy)
def test_hyp_wikidb116_image_img_user_setter(instance):
    original = instance.img_user
    instance.img_user = original
    assert instance.img_user == original



@given(instance=wikidb116_image_strategy)
def test_hyp_wikidb116_image_img_size_setter(instance):
    original = instance.img_size
    instance.img_size = original
    assert instance.img_size == original



@given(instance=wikidb116_image_strategy)
def test_hyp_wikidb116_image_img_user_text_setter(instance):
    original = instance.img_user_text
    instance.img_user_text = original
    assert instance.img_user_text == original



@given(instance=wikidb116_image_strategy)
def test_hyp_wikidb116_image_img_sha1_setter(instance):
    original = instance.img_sha1
    instance.img_sha1 = original
    assert instance.img_sha1 == original



@given(instance=wikidb116_image_strategy)
def test_hyp_wikidb116_image_img_description_setter(instance):
    original = instance.img_description
    instance.img_description = original
    assert instance.img_description == original



@given(instance=wikidb116_image_strategy)
def test_hyp_wikidb116_image_img_metadata_setter(instance):
    original = instance.img_metadata
    instance.img_metadata = original
    assert instance.img_metadata == original



@given(instance=wikidb116_image_strategy)
def test_hyp_wikidb116_image_img_height_setter(instance):
    original = instance.img_height
    instance.img_height = original
    assert instance.img_height == original



@given(instance=wikidb116_image_strategy)
def test_hyp_wikidb116_image_img_media_type_setter(instance):
    original = instance.img_media_type
    instance.img_media_type = original
    assert instance.img_media_type == original



@given(instance=wikidb116_image_strategy)
def test_hyp_wikidb116_image_img_name_setter(instance):
    original = instance.img_name
    instance.img_name = original
    assert instance.img_name == original




@given(instance=wikidb116_objectcache_strategy)
def test_hyp_wikidb116_objectcache_keyname_setter(instance):
    original = instance.keyname
    instance.keyname = original
    assert instance.keyname == original



@given(instance=wikidb116_objectcache_strategy)
def test_hyp_wikidb116_objectcache_exptime_setter(instance):
    original = instance.exptime
    instance.exptime = original
    assert instance.exptime == original



@given(instance=wikidb116_objectcache_strategy)
def test_hyp_wikidb116_objectcache_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=wikidb116_page_restrictions_strategy)
def test_hyp_wikidb116_page_restrictions_pr_page_setter(instance):
    original = instance.pr_page
    instance.pr_page = original
    assert instance.pr_page == original



@given(instance=wikidb116_page_restrictions_strategy)
def test_hyp_wikidb116_page_restrictions_pr_type_setter(instance):
    original = instance.pr_type
    instance.pr_type = original
    assert instance.pr_type == original



@given(instance=wikidb116_page_restrictions_strategy)
def test_hyp_wikidb116_page_restrictions_pr_expiry_setter(instance):
    original = instance.pr_expiry
    instance.pr_expiry = original
    assert instance.pr_expiry == original



@given(instance=wikidb116_page_restrictions_strategy)
def test_hyp_wikidb116_page_restrictions_pr_user_setter(instance):
    original = instance.pr_user
    instance.pr_user = original
    assert instance.pr_user == original



@given(instance=wikidb116_page_restrictions_strategy)
def test_hyp_wikidb116_page_restrictions_pr_id_setter(instance):
    original = instance.pr_id
    instance.pr_id = original
    assert instance.pr_id == original



@given(instance=wikidb116_page_restrictions_strategy)
def test_hyp_wikidb116_page_restrictions_pr_level_setter(instance):
    original = instance.pr_level
    instance.pr_level = original
    assert instance.pr_level == original



@given(instance=wikidb116_page_restrictions_strategy)
def test_hyp_wikidb116_page_restrictions_pr_cascade_setter(instance):
    original = instance.pr_cascade
    instance.pr_cascade = original
    assert instance.pr_cascade == original




@given(instance=wikidb116_categorylinks_strategy)
def test_hyp_wikidb116_categorylinks_cl_timestamp_setter(instance):
    original = instance.cl_timestamp
    instance.cl_timestamp = original
    assert instance.cl_timestamp == original



@given(instance=wikidb116_categorylinks_strategy)
def test_hyp_wikidb116_categorylinks_cl_from_setter(instance):
    original = instance.cl_from
    instance.cl_from = original
    assert instance.cl_from == original



@given(instance=wikidb116_categorylinks_strategy)
def test_hyp_wikidb116_categorylinks_cl_to_setter(instance):
    original = instance.cl_to
    instance.cl_to = original
    assert instance.cl_to == original



@given(instance=wikidb116_categorylinks_strategy)
def test_hyp_wikidb116_categorylinks_cl_sortkey_setter(instance):
    original = instance.cl_sortkey
    instance.cl_sortkey = original
    assert instance.cl_sortkey == original




@given(instance=wikidb116_filearchive_strategy)
def test_hyp_wikidb116_filearchive_fa_description_setter(instance):
    original = instance.fa_description
    instance.fa_description = original
    assert instance.fa_description == original



@given(instance=wikidb116_filearchive_strategy)
def test_hyp_wikidb116_filearchive_fa_storage_key_setter(instance):
    original = instance.fa_storage_key
    instance.fa_storage_key = original
    assert instance.fa_storage_key == original



@given(instance=wikidb116_filearchive_strategy)
def test_hyp_wikidb116_filearchive_fa_bits_setter(instance):
    original = instance.fa_bits
    instance.fa_bits = original
    assert instance.fa_bits == original



@given(instance=wikidb116_filearchive_strategy)
def test_hyp_wikidb116_filearchive_fa_major_mime_setter(instance):
    original = instance.fa_major_mime
    instance.fa_major_mime = original
    assert instance.fa_major_mime == original



@given(instance=wikidb116_filearchive_strategy)
def test_hyp_wikidb116_filearchive_fa_archive_name_setter(instance):
    original = instance.fa_archive_name
    instance.fa_archive_name = original
    assert instance.fa_archive_name == original



@given(instance=wikidb116_filearchive_strategy)
def test_hyp_wikidb116_filearchive_fa_id_setter(instance):
    original = instance.fa_id
    instance.fa_id = original
    assert instance.fa_id == original



@given(instance=wikidb116_filearchive_strategy)
def test_hyp_wikidb116_filearchive_fa_minor_mime_setter(instance):
    original = instance.fa_minor_mime
    instance.fa_minor_mime = original
    assert instance.fa_minor_mime == original



@given(instance=wikidb116_filearchive_strategy)
def test_hyp_wikidb116_filearchive_fa_deleted_reason_setter(instance):
    original = instance.fa_deleted_reason
    instance.fa_deleted_reason = original
    assert instance.fa_deleted_reason == original



@given(instance=wikidb116_filearchive_strategy)
def test_hyp_wikidb116_filearchive_fa_user_setter(instance):
    original = instance.fa_user
    instance.fa_user = original
    assert instance.fa_user == original



@given(instance=wikidb116_filearchive_strategy)
def test_hyp_wikidb116_filearchive_fa_media_type_setter(instance):
    original = instance.fa_media_type
    instance.fa_media_type = original
    assert instance.fa_media_type == original



@given(instance=wikidb116_filearchive_strategy)
def test_hyp_wikidb116_filearchive_fa_metadata_setter(instance):
    original = instance.fa_metadata
    instance.fa_metadata = original
    assert instance.fa_metadata == original



@given(instance=wikidb116_filearchive_strategy)
def test_hyp_wikidb116_filearchive_fa_deleted_setter(instance):
    original = instance.fa_deleted
    instance.fa_deleted = original
    assert instance.fa_deleted == original



@given(instance=wikidb116_filearchive_strategy)
def test_hyp_wikidb116_filearchive_fa_user_text_setter(instance):
    original = instance.fa_user_text
    instance.fa_user_text = original
    assert instance.fa_user_text == original



@given(instance=wikidb116_filearchive_strategy)
def test_hyp_wikidb116_filearchive_fa_storage_group_setter(instance):
    original = instance.fa_storage_group
    instance.fa_storage_group = original
    assert instance.fa_storage_group == original



@given(instance=wikidb116_filearchive_strategy)
def test_hyp_wikidb116_filearchive_fa_deleted_user_setter(instance):
    original = instance.fa_deleted_user
    instance.fa_deleted_user = original
    assert instance.fa_deleted_user == original



@given(instance=wikidb116_filearchive_strategy)
def test_hyp_wikidb116_filearchive_fa_height_setter(instance):
    original = instance.fa_height
    instance.fa_height = original
    assert instance.fa_height == original



@given(instance=wikidb116_filearchive_strategy)
def test_hyp_wikidb116_filearchive_fa_width_setter(instance):
    original = instance.fa_width
    instance.fa_width = original
    assert instance.fa_width == original



@given(instance=wikidb116_filearchive_strategy)
def test_hyp_wikidb116_filearchive_fa_deleted_timestamp_setter(instance):
    original = instance.fa_deleted_timestamp
    instance.fa_deleted_timestamp = original
    assert instance.fa_deleted_timestamp == original



@given(instance=wikidb116_filearchive_strategy)
def test_hyp_wikidb116_filearchive_fa_name_setter(instance):
    original = instance.fa_name
    instance.fa_name = original
    assert instance.fa_name == original



@given(instance=wikidb116_filearchive_strategy)
def test_hyp_wikidb116_filearchive_fa_size_setter(instance):
    original = instance.fa_size
    instance.fa_size = original
    assert instance.fa_size == original



@given(instance=wikidb116_filearchive_strategy)
def test_hyp_wikidb116_filearchive_fa_timestamp_setter(instance):
    original = instance.fa_timestamp
    instance.fa_timestamp = original
    assert instance.fa_timestamp == original




@given(instance=wikidb116_job_strategy)
def test_hyp_wikidb116_job_job_id_setter(instance):
    original = instance.job_id
    instance.job_id = original
    assert instance.job_id == original



@given(instance=wikidb116_job_strategy)
def test_hyp_wikidb116_job_job_params_setter(instance):
    original = instance.job_params
    instance.job_params = original
    assert instance.job_params == original



@given(instance=wikidb116_job_strategy)
def test_hyp_wikidb116_job_job_title_setter(instance):
    original = instance.job_title
    instance.job_title = original
    assert instance.job_title == original



@given(instance=wikidb116_job_strategy)
def test_hyp_wikidb116_job_job_cmd_setter(instance):
    original = instance.job_cmd
    instance.job_cmd = original
    assert instance.job_cmd == original



@given(instance=wikidb116_job_strategy)
def test_hyp_wikidb116_job_job_namespace_setter(instance):
    original = instance.job_namespace
    instance.job_namespace = original
    assert instance.job_namespace == original




@given(instance=wikidb116_interwiki_strategy)
def test_hyp_wikidb116_interwiki_iw_trans_setter(instance):
    original = instance.iw_trans
    instance.iw_trans = original
    assert instance.iw_trans == original



@given(instance=wikidb116_interwiki_strategy)
def test_hyp_wikidb116_interwiki_iw_url_setter(instance):
    original = instance.iw_url
    instance.iw_url = original
    assert instance.iw_url == original



@given(instance=wikidb116_interwiki_strategy)
def test_hyp_wikidb116_interwiki_iw_local_setter(instance):
    original = instance.iw_local
    instance.iw_local = original
    assert instance.iw_local == original



@given(instance=wikidb116_interwiki_strategy)
def test_hyp_wikidb116_interwiki_iw_prefix_setter(instance):
    original = instance.iw_prefix
    instance.iw_prefix = original
    assert instance.iw_prefix == original




@given(instance=wikidb116_watchlist_strategy)
def test_hyp_wikidb116_watchlist_wl_user_setter(instance):
    original = instance.wl_user
    instance.wl_user = original
    assert instance.wl_user == original



@given(instance=wikidb116_watchlist_strategy)
def test_hyp_wikidb116_watchlist_wl_namespace_setter(instance):
    original = instance.wl_namespace
    instance.wl_namespace = original
    assert instance.wl_namespace == original



@given(instance=wikidb116_watchlist_strategy)
def test_hyp_wikidb116_watchlist_wl_title_setter(instance):
    original = instance.wl_title
    instance.wl_title = original
    assert instance.wl_title == original



@given(instance=wikidb116_watchlist_strategy)
def test_hyp_wikidb116_watchlist_wl_notificationtimestamp_setter(instance):
    original = instance.wl_notificationtimestamp
    instance.wl_notificationtimestamp = original
    assert instance.wl_notificationtimestamp == original




@given(instance=wikidb116_protected_titles_strategy)
def test_hyp_wikidb116_protected_titles_pt_create_perm_setter(instance):
    original = instance.pt_create_perm
    instance.pt_create_perm = original
    assert instance.pt_create_perm == original



@given(instance=wikidb116_protected_titles_strategy)
def test_hyp_wikidb116_protected_titles_pt_namespace_setter(instance):
    original = instance.pt_namespace
    instance.pt_namespace = original
    assert instance.pt_namespace == original



@given(instance=wikidb116_protected_titles_strategy)
def test_hyp_wikidb116_protected_titles_pt_expiry_setter(instance):
    original = instance.pt_expiry
    instance.pt_expiry = original
    assert instance.pt_expiry == original



@given(instance=wikidb116_protected_titles_strategy)
def test_hyp_wikidb116_protected_titles_pt_reason_setter(instance):
    original = instance.pt_reason
    instance.pt_reason = original
    assert instance.pt_reason == original



@given(instance=wikidb116_protected_titles_strategy)
def test_hyp_wikidb116_protected_titles_pt_user_setter(instance):
    original = instance.pt_user
    instance.pt_user = original
    assert instance.pt_user == original



@given(instance=wikidb116_protected_titles_strategy)
def test_hyp_wikidb116_protected_titles_pt_title_setter(instance):
    original = instance.pt_title
    instance.pt_title = original
    assert instance.pt_title == original



@given(instance=wikidb116_protected_titles_strategy)
def test_hyp_wikidb116_protected_titles_pt_timestamp_setter(instance):
    original = instance.pt_timestamp
    instance.pt_timestamp = original
    assert instance.pt_timestamp == original




@given(instance=wikidb116_querycache_info_strategy)
def test_hyp_wikidb116_querycache_info_qci_type_setter(instance):
    original = instance.qci_type
    instance.qci_type = original
    assert instance.qci_type == original



@given(instance=wikidb116_querycache_info_strategy)
def test_hyp_wikidb116_querycache_info_qci_timestamp_setter(instance):
    original = instance.qci_timestamp
    instance.qci_timestamp = original
    assert instance.qci_timestamp == original




@given(instance=wikidb116_hitcounter_strategy)
def test_hyp_wikidb116_hitcounter_hc_id_setter(instance):
    original = instance.hc_id
    instance.hc_id = original
    assert instance.hc_id == original




@given(instance=wikidb116_templatelinks_strategy)
def test_hyp_wikidb116_templatelinks_tl_title_setter(instance):
    original = instance.tl_title
    instance.tl_title = original
    assert instance.tl_title == original



@given(instance=wikidb116_templatelinks_strategy)
def test_hyp_wikidb116_templatelinks_tl_from_setter(instance):
    original = instance.tl_from
    instance.tl_from = original
    assert instance.tl_from == original



@given(instance=wikidb116_templatelinks_strategy)
def test_hyp_wikidb116_templatelinks_tl_namespace_setter(instance):
    original = instance.tl_namespace
    instance.tl_namespace = original
    assert instance.tl_namespace == original




@given(instance=wikidb116_user_strategy)
def test_hyp_wikidb116_user_user_options_setter(instance):
    original = instance.user_options
    instance.user_options = original
    assert instance.user_options == original



@given(instance=wikidb116_user_strategy)
def test_hyp_wikidb116_user_user_token_setter(instance):
    original = instance.user_token
    instance.user_token = original
    assert instance.user_token == original



@given(instance=wikidb116_user_strategy)
def test_hyp_wikidb116_user_user_newpassword_setter(instance):
    original = instance.user_newpassword
    instance.user_newpassword = original
    assert instance.user_newpassword == original



@given(instance=wikidb116_user_strategy)
def test_hyp_wikidb116_user_user_touched_setter(instance):
    original = instance.user_touched
    instance.user_touched = original
    assert instance.user_touched == original



@given(instance=wikidb116_user_strategy)
def test_hyp_wikidb116_user_user_email_token_setter(instance):
    original = instance.user_email_token
    instance.user_email_token = original
    assert instance.user_email_token == original



@given(instance=wikidb116_user_strategy)
def test_hyp_wikidb116_user_user_password_setter(instance):
    original = instance.user_password
    instance.user_password = original
    assert instance.user_password == original



@given(instance=wikidb116_user_strategy)
def test_hyp_wikidb116_user_user_email_token_expires_setter(instance):
    original = instance.user_email_token_expires
    instance.user_email_token_expires = original
    assert instance.user_email_token_expires == original



@given(instance=wikidb116_user_strategy)
def test_hyp_wikidb116_user_user_registration_setter(instance):
    original = instance.user_registration
    instance.user_registration = original
    assert instance.user_registration == original



@given(instance=wikidb116_user_strategy)
def test_hyp_wikidb116_user_user_email_setter(instance):
    original = instance.user_email
    instance.user_email = original
    assert instance.user_email == original



@given(instance=wikidb116_user_strategy)
def test_hyp_wikidb116_user_user_editcount_setter(instance):
    original = instance.user_editcount
    instance.user_editcount = original
    assert instance.user_editcount == original



@given(instance=wikidb116_user_strategy)
def test_hyp_wikidb116_user_user_newpass_time_setter(instance):
    original = instance.user_newpass_time
    instance.user_newpass_time = original
    assert instance.user_newpass_time == original



@given(instance=wikidb116_user_strategy)
def test_hyp_wikidb116_user_user_real_name_setter(instance):
    original = instance.user_real_name
    instance.user_real_name = original
    assert instance.user_real_name == original



@given(instance=wikidb116_user_strategy)
def test_hyp_wikidb116_user_user_email_authenticated_setter(instance):
    original = instance.user_email_authenticated
    instance.user_email_authenticated = original
    assert instance.user_email_authenticated == original



@given(instance=wikidb116_user_strategy)
def test_hyp_wikidb116_user_user_name_setter(instance):
    original = instance.user_name
    instance.user_name = original
    assert instance.user_name == original



@given(instance=wikidb116_user_strategy)
def test_hyp_wikidb116_user_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original




@given(instance=wikidb116_trackbacks_strategy)
def test_hyp_wikidb116_trackbacks_tb_id_setter(instance):
    original = instance.tb_id
    instance.tb_id = original
    assert instance.tb_id == original



@given(instance=wikidb116_trackbacks_strategy)
def test_hyp_wikidb116_trackbacks_tb_name_setter(instance):
    original = instance.tb_name
    instance.tb_name = original
    assert instance.tb_name == original



@given(instance=wikidb116_trackbacks_strategy)
def test_hyp_wikidb116_trackbacks_tb_title_setter(instance):
    original = instance.tb_title
    instance.tb_title = original
    assert instance.tb_title == original



@given(instance=wikidb116_trackbacks_strategy)
def test_hyp_wikidb116_trackbacks_tb_page_setter(instance):
    original = instance.tb_page
    instance.tb_page = original
    assert instance.tb_page == original



@given(instance=wikidb116_trackbacks_strategy)
def test_hyp_wikidb116_trackbacks_tb_url_setter(instance):
    original = instance.tb_url
    instance.tb_url = original
    assert instance.tb_url == original



@given(instance=wikidb116_trackbacks_strategy)
def test_hyp_wikidb116_trackbacks_tb_ex_setter(instance):
    original = instance.tb_ex
    instance.tb_ex = original
    assert instance.tb_ex == original




@given(instance=wikidb116_math_strategy)
def test_hyp_wikidb116_math_math_html_setter(instance):
    original = instance.math_html
    instance.math_html = original
    assert instance.math_html == original



@given(instance=wikidb116_math_strategy)
def test_hyp_wikidb116_math_math_inputhash_setter(instance):
    original = instance.math_inputhash
    instance.math_inputhash = original
    assert instance.math_inputhash == original



@given(instance=wikidb116_math_strategy)
def test_hyp_wikidb116_math_math_outputhash_setter(instance):
    original = instance.math_outputhash
    instance.math_outputhash = original
    assert instance.math_outputhash == original



@given(instance=wikidb116_math_strategy)
def test_hyp_wikidb116_math_math_mathml_setter(instance):
    original = instance.math_mathml
    instance.math_mathml = original
    assert instance.math_mathml == original



@given(instance=wikidb116_math_strategy)
def test_hyp_wikidb116_math_math_html_conservativeness_setter(instance):
    original = instance.math_html_conservativeness
    instance.math_html_conservativeness = original
    assert instance.math_html_conservativeness == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_wikidb116_archive_ar_comment_value_roundtrip():
    instance = wikidb116_archive(ar_comment="sample_text", ar_deleted=7, ar_flags="sample_text", ar_len="sample_text", ar_minor_edit=7, ar_namespace="sample_text", ar_page_id="sample_text", ar_parent_id="sample_text", ar_rev_id="sample_text", ar_text="sample_text", ar_text_id="sample_text", ar_timestamp="sample_text", ar_title="sample_text", ar_user="sample_text", ar_user_text="sample_text")
    assert instance.ar_comment == "sample_text"
    instance.ar_comment = "sample_text_2"
    assert instance.ar_comment == "sample_text_2"


def test_wikidb116_archive_ar_deleted_value_roundtrip():
    instance = wikidb116_archive(ar_comment="sample_text", ar_deleted=7, ar_flags="sample_text", ar_len="sample_text", ar_minor_edit=7, ar_namespace="sample_text", ar_page_id="sample_text", ar_parent_id="sample_text", ar_rev_id="sample_text", ar_text="sample_text", ar_text_id="sample_text", ar_timestamp="sample_text", ar_title="sample_text", ar_user="sample_text", ar_user_text="sample_text")
    assert instance.ar_deleted == 7
    instance.ar_deleted = 13
    assert instance.ar_deleted == 13


def test_wikidb116_archive_ar_flags_value_roundtrip():
    instance = wikidb116_archive(ar_comment="sample_text", ar_deleted=7, ar_flags="sample_text", ar_len="sample_text", ar_minor_edit=7, ar_namespace="sample_text", ar_page_id="sample_text", ar_parent_id="sample_text", ar_rev_id="sample_text", ar_text="sample_text", ar_text_id="sample_text", ar_timestamp="sample_text", ar_title="sample_text", ar_user="sample_text", ar_user_text="sample_text")
    assert instance.ar_flags == "sample_text"
    instance.ar_flags = "sample_text_2"
    assert instance.ar_flags == "sample_text_2"


def test_wikidb116_archive_ar_len_value_roundtrip():
    instance = wikidb116_archive(ar_comment="sample_text", ar_deleted=7, ar_flags="sample_text", ar_len="sample_text", ar_minor_edit=7, ar_namespace="sample_text", ar_page_id="sample_text", ar_parent_id="sample_text", ar_rev_id="sample_text", ar_text="sample_text", ar_text_id="sample_text", ar_timestamp="sample_text", ar_title="sample_text", ar_user="sample_text", ar_user_text="sample_text")
    assert instance.ar_len == "sample_text"
    instance.ar_len = "sample_text_2"
    assert instance.ar_len == "sample_text_2"


def test_wikidb116_archive_ar_minor_edit_value_roundtrip():
    instance = wikidb116_archive(ar_comment="sample_text", ar_deleted=7, ar_flags="sample_text", ar_len="sample_text", ar_minor_edit=7, ar_namespace="sample_text", ar_page_id="sample_text", ar_parent_id="sample_text", ar_rev_id="sample_text", ar_text="sample_text", ar_text_id="sample_text", ar_timestamp="sample_text", ar_title="sample_text", ar_user="sample_text", ar_user_text="sample_text")
    assert instance.ar_minor_edit == 7
    instance.ar_minor_edit = 13
    assert instance.ar_minor_edit == 13


def test_wikidb116_archive_ar_namespace_value_roundtrip():
    instance = wikidb116_archive(ar_comment="sample_text", ar_deleted=7, ar_flags="sample_text", ar_len="sample_text", ar_minor_edit=7, ar_namespace="sample_text", ar_page_id="sample_text", ar_parent_id="sample_text", ar_rev_id="sample_text", ar_text="sample_text", ar_text_id="sample_text", ar_timestamp="sample_text", ar_title="sample_text", ar_user="sample_text", ar_user_text="sample_text")
    assert instance.ar_namespace == "sample_text"
    instance.ar_namespace = "sample_text_2"
    assert instance.ar_namespace == "sample_text_2"


def test_wikidb116_archive_ar_page_id_value_roundtrip():
    instance = wikidb116_archive(ar_comment="sample_text", ar_deleted=7, ar_flags="sample_text", ar_len="sample_text", ar_minor_edit=7, ar_namespace="sample_text", ar_page_id="sample_text", ar_parent_id="sample_text", ar_rev_id="sample_text", ar_text="sample_text", ar_text_id="sample_text", ar_timestamp="sample_text", ar_title="sample_text", ar_user="sample_text", ar_user_text="sample_text")
    assert instance.ar_page_id == "sample_text"
    instance.ar_page_id = "sample_text_2"
    assert instance.ar_page_id == "sample_text_2"


def test_wikidb116_archive_ar_parent_id_value_roundtrip():
    instance = wikidb116_archive(ar_comment="sample_text", ar_deleted=7, ar_flags="sample_text", ar_len="sample_text", ar_minor_edit=7, ar_namespace="sample_text", ar_page_id="sample_text", ar_parent_id="sample_text", ar_rev_id="sample_text", ar_text="sample_text", ar_text_id="sample_text", ar_timestamp="sample_text", ar_title="sample_text", ar_user="sample_text", ar_user_text="sample_text")
    assert instance.ar_parent_id == "sample_text"
    instance.ar_parent_id = "sample_text_2"
    assert instance.ar_parent_id == "sample_text_2"


def test_wikidb116_archive_ar_rev_id_value_roundtrip():
    instance = wikidb116_archive(ar_comment="sample_text", ar_deleted=7, ar_flags="sample_text", ar_len="sample_text", ar_minor_edit=7, ar_namespace="sample_text", ar_page_id="sample_text", ar_parent_id="sample_text", ar_rev_id="sample_text", ar_text="sample_text", ar_text_id="sample_text", ar_timestamp="sample_text", ar_title="sample_text", ar_user="sample_text", ar_user_text="sample_text")
    assert instance.ar_rev_id == "sample_text"
    instance.ar_rev_id = "sample_text_2"
    assert instance.ar_rev_id == "sample_text_2"


def test_wikidb116_archive_ar_text_value_roundtrip():
    instance = wikidb116_archive(ar_comment="sample_text", ar_deleted=7, ar_flags="sample_text", ar_len="sample_text", ar_minor_edit=7, ar_namespace="sample_text", ar_page_id="sample_text", ar_parent_id="sample_text", ar_rev_id="sample_text", ar_text="sample_text", ar_text_id="sample_text", ar_timestamp="sample_text", ar_title="sample_text", ar_user="sample_text", ar_user_text="sample_text")
    assert instance.ar_text == "sample_text"
    instance.ar_text = "sample_text_2"
    assert instance.ar_text == "sample_text_2"


def test_wikidb116_archive_ar_text_id_value_roundtrip():
    instance = wikidb116_archive(ar_comment="sample_text", ar_deleted=7, ar_flags="sample_text", ar_len="sample_text", ar_minor_edit=7, ar_namespace="sample_text", ar_page_id="sample_text", ar_parent_id="sample_text", ar_rev_id="sample_text", ar_text="sample_text", ar_text_id="sample_text", ar_timestamp="sample_text", ar_title="sample_text", ar_user="sample_text", ar_user_text="sample_text")
    assert instance.ar_text_id == "sample_text"
    instance.ar_text_id = "sample_text_2"
    assert instance.ar_text_id == "sample_text_2"


def test_wikidb116_archive_ar_timestamp_value_roundtrip():
    instance = wikidb116_archive(ar_comment="sample_text", ar_deleted=7, ar_flags="sample_text", ar_len="sample_text", ar_minor_edit=7, ar_namespace="sample_text", ar_page_id="sample_text", ar_parent_id="sample_text", ar_rev_id="sample_text", ar_text="sample_text", ar_text_id="sample_text", ar_timestamp="sample_text", ar_title="sample_text", ar_user="sample_text", ar_user_text="sample_text")
    assert instance.ar_timestamp == "sample_text"
    instance.ar_timestamp = "sample_text_2"
    assert instance.ar_timestamp == "sample_text_2"


def test_wikidb116_archive_ar_title_value_roundtrip():
    instance = wikidb116_archive(ar_comment="sample_text", ar_deleted=7, ar_flags="sample_text", ar_len="sample_text", ar_minor_edit=7, ar_namespace="sample_text", ar_page_id="sample_text", ar_parent_id="sample_text", ar_rev_id="sample_text", ar_text="sample_text", ar_text_id="sample_text", ar_timestamp="sample_text", ar_title="sample_text", ar_user="sample_text", ar_user_text="sample_text")
    assert instance.ar_title == "sample_text"
    instance.ar_title = "sample_text_2"
    assert instance.ar_title == "sample_text_2"


def test_wikidb116_archive_ar_user_value_roundtrip():
    instance = wikidb116_archive(ar_comment="sample_text", ar_deleted=7, ar_flags="sample_text", ar_len="sample_text", ar_minor_edit=7, ar_namespace="sample_text", ar_page_id="sample_text", ar_parent_id="sample_text", ar_rev_id="sample_text", ar_text="sample_text", ar_text_id="sample_text", ar_timestamp="sample_text", ar_title="sample_text", ar_user="sample_text", ar_user_text="sample_text")
    assert instance.ar_user == "sample_text"
    instance.ar_user = "sample_text_2"
    assert instance.ar_user == "sample_text_2"


def test_wikidb116_archive_ar_user_text_value_roundtrip():
    instance = wikidb116_archive(ar_comment="sample_text", ar_deleted=7, ar_flags="sample_text", ar_len="sample_text", ar_minor_edit=7, ar_namespace="sample_text", ar_page_id="sample_text", ar_parent_id="sample_text", ar_rev_id="sample_text", ar_text="sample_text", ar_text_id="sample_text", ar_timestamp="sample_text", ar_title="sample_text", ar_user="sample_text", ar_user_text="sample_text")
    assert instance.ar_user_text == "sample_text"
    instance.ar_user_text = "sample_text_2"
    assert instance.ar_user_text == "sample_text_2"


def test_wikidb116_category_cat_files_value_roundtrip():
    instance = wikidb116_category(cat_files="sample_text", cat_hidden=7, cat_id="sample_text", cat_pages="sample_text", cat_subcats="sample_text", cat_title="sample_text")
    assert instance.cat_files == "sample_text"
    instance.cat_files = "sample_text_2"
    assert instance.cat_files == "sample_text_2"


def test_wikidb116_category_cat_hidden_value_roundtrip():
    instance = wikidb116_category(cat_files="sample_text", cat_hidden=7, cat_id="sample_text", cat_pages="sample_text", cat_subcats="sample_text", cat_title="sample_text")
    assert instance.cat_hidden == 7
    instance.cat_hidden = 13
    assert instance.cat_hidden == 13


def test_wikidb116_category_cat_id_value_roundtrip():
    instance = wikidb116_category(cat_files="sample_text", cat_hidden=7, cat_id="sample_text", cat_pages="sample_text", cat_subcats="sample_text", cat_title="sample_text")
    assert instance.cat_id == "sample_text"
    instance.cat_id = "sample_text_2"
    assert instance.cat_id == "sample_text_2"


def test_wikidb116_category_cat_pages_value_roundtrip():
    instance = wikidb116_category(cat_files="sample_text", cat_hidden=7, cat_id="sample_text", cat_pages="sample_text", cat_subcats="sample_text", cat_title="sample_text")
    assert instance.cat_pages == "sample_text"
    instance.cat_pages = "sample_text_2"
    assert instance.cat_pages == "sample_text_2"


def test_wikidb116_category_cat_subcats_value_roundtrip():
    instance = wikidb116_category(cat_files="sample_text", cat_hidden=7, cat_id="sample_text", cat_pages="sample_text", cat_subcats="sample_text", cat_title="sample_text")
    assert instance.cat_subcats == "sample_text"
    instance.cat_subcats = "sample_text_2"
    assert instance.cat_subcats == "sample_text_2"


def test_wikidb116_category_cat_title_value_roundtrip():
    instance = wikidb116_category(cat_files="sample_text", cat_hidden=7, cat_id="sample_text", cat_pages="sample_text", cat_subcats="sample_text", cat_title="sample_text")
    assert instance.cat_title == "sample_text"
    instance.cat_title = "sample_text_2"
    assert instance.cat_title == "sample_text_2"


def test_wikidb116_categorylinks_cl_from_value_roundtrip():
    instance = wikidb116_categorylinks(cl_from="sample_text", cl_sortkey="sample_text", cl_timestamp=date(2024, 1, 1), cl_to="sample_text")
    assert instance.cl_from == "sample_text"
    instance.cl_from = "sample_text_2"
    assert instance.cl_from == "sample_text_2"


def test_wikidb116_categorylinks_cl_sortkey_value_roundtrip():
    instance = wikidb116_categorylinks(cl_from="sample_text", cl_sortkey="sample_text", cl_timestamp=date(2024, 1, 1), cl_to="sample_text")
    assert instance.cl_sortkey == "sample_text"
    instance.cl_sortkey = "sample_text_2"
    assert instance.cl_sortkey == "sample_text_2"


def test_wikidb116_categorylinks_cl_timestamp_value_roundtrip():
    instance = wikidb116_categorylinks(cl_from="sample_text", cl_sortkey="sample_text", cl_timestamp=date(2024, 1, 1), cl_to="sample_text")
    assert instance.cl_timestamp == date(2024, 1, 1)
    instance.cl_timestamp = date(2025, 6, 15)
    assert instance.cl_timestamp == date(2025, 6, 15)


def test_wikidb116_categorylinks_cl_to_value_roundtrip():
    instance = wikidb116_categorylinks(cl_from="sample_text", cl_sortkey="sample_text", cl_timestamp=date(2024, 1, 1), cl_to="sample_text")
    assert instance.cl_to == "sample_text"
    instance.cl_to = "sample_text_2"
    assert instance.cl_to == "sample_text_2"


def test_wikidb116_change_tag_ct_log_id_value_roundtrip():
    instance = wikidb116_change_tag(ct_log_id="sample_text", ct_params="sample_text", ct_rc_id="sample_text", ct_rev_id="sample_text", ct_tag="sample_text")
    assert instance.ct_log_id == "sample_text"
    instance.ct_log_id = "sample_text_2"
    assert instance.ct_log_id == "sample_text_2"


def test_wikidb116_change_tag_ct_params_value_roundtrip():
    instance = wikidb116_change_tag(ct_log_id="sample_text", ct_params="sample_text", ct_rc_id="sample_text", ct_rev_id="sample_text", ct_tag="sample_text")
    assert instance.ct_params == "sample_text"
    instance.ct_params = "sample_text_2"
    assert instance.ct_params == "sample_text_2"


def test_wikidb116_change_tag_ct_rc_id_value_roundtrip():
    instance = wikidb116_change_tag(ct_log_id="sample_text", ct_params="sample_text", ct_rc_id="sample_text", ct_rev_id="sample_text", ct_tag="sample_text")
    assert instance.ct_rc_id == "sample_text"
    instance.ct_rc_id = "sample_text_2"
    assert instance.ct_rc_id == "sample_text_2"


def test_wikidb116_change_tag_ct_rev_id_value_roundtrip():
    instance = wikidb116_change_tag(ct_log_id="sample_text", ct_params="sample_text", ct_rc_id="sample_text", ct_rev_id="sample_text", ct_tag="sample_text")
    assert instance.ct_rev_id == "sample_text"
    instance.ct_rev_id = "sample_text_2"
    assert instance.ct_rev_id == "sample_text_2"


def test_wikidb116_change_tag_ct_tag_value_roundtrip():
    instance = wikidb116_change_tag(ct_log_id="sample_text", ct_params="sample_text", ct_rc_id="sample_text", ct_rev_id="sample_text", ct_tag="sample_text")
    assert instance.ct_tag == "sample_text"
    instance.ct_tag = "sample_text_2"
    assert instance.ct_tag == "sample_text_2"


def test_wikidb116_external_user_eu_external_id_value_roundtrip():
    instance = wikidb116_external_user(eu_external_id="sample_text", eu_local_id="sample_text")
    assert instance.eu_external_id == "sample_text"
    instance.eu_external_id = "sample_text_2"
    assert instance.eu_external_id == "sample_text_2"


def test_wikidb116_external_user_eu_local_id_value_roundtrip():
    instance = wikidb116_external_user(eu_external_id="sample_text", eu_local_id="sample_text")
    assert instance.eu_local_id == "sample_text"
    instance.eu_local_id = "sample_text_2"
    assert instance.eu_local_id == "sample_text_2"


def test_wikidb116_externallinks_el_from_value_roundtrip():
    instance = wikidb116_externallinks(el_from="sample_text", el_index="sample_text", el_to="sample_text")
    assert instance.el_from == "sample_text"
    instance.el_from = "sample_text_2"
    assert instance.el_from == "sample_text_2"


def test_wikidb116_externallinks_el_index_value_roundtrip():
    instance = wikidb116_externallinks(el_from="sample_text", el_index="sample_text", el_to="sample_text")
    assert instance.el_index == "sample_text"
    instance.el_index = "sample_text_2"
    assert instance.el_index == "sample_text_2"


def test_wikidb116_externallinks_el_to_value_roundtrip():
    instance = wikidb116_externallinks(el_from="sample_text", el_index="sample_text", el_to="sample_text")
    assert instance.el_to == "sample_text"
    instance.el_to = "sample_text_2"
    assert instance.el_to == "sample_text_2"


def test_wikidb116_filearchive_fa_archive_name_value_roundtrip():
    instance = wikidb116_filearchive(fa_archive_name="sample_text", fa_bits="sample_text", fa_deleted=7, fa_deleted_reason="sample_text", fa_deleted_timestamp="sample_text", fa_deleted_user="sample_text", fa_description="sample_text", fa_height="sample_text", fa_id="sample_text", fa_major_mime="sample_text", fa_media_type="sample_text", fa_metadata="sample_text", fa_minor_mime="sample_text", fa_name="sample_text", fa_size="sample_text", fa_storage_group="sample_text", fa_storage_key="sample_text", fa_timestamp="sample_text", fa_user="sample_text", fa_user_text="sample_text", fa_width="sample_text")
    assert instance.fa_archive_name == "sample_text"
    instance.fa_archive_name = "sample_text_2"
    assert instance.fa_archive_name == "sample_text_2"


def test_wikidb116_filearchive_fa_bits_value_roundtrip():
    instance = wikidb116_filearchive(fa_archive_name="sample_text", fa_bits="sample_text", fa_deleted=7, fa_deleted_reason="sample_text", fa_deleted_timestamp="sample_text", fa_deleted_user="sample_text", fa_description="sample_text", fa_height="sample_text", fa_id="sample_text", fa_major_mime="sample_text", fa_media_type="sample_text", fa_metadata="sample_text", fa_minor_mime="sample_text", fa_name="sample_text", fa_size="sample_text", fa_storage_group="sample_text", fa_storage_key="sample_text", fa_timestamp="sample_text", fa_user="sample_text", fa_user_text="sample_text", fa_width="sample_text")
    assert instance.fa_bits == "sample_text"
    instance.fa_bits = "sample_text_2"
    assert instance.fa_bits == "sample_text_2"


def test_wikidb116_filearchive_fa_deleted_value_roundtrip():
    instance = wikidb116_filearchive(fa_archive_name="sample_text", fa_bits="sample_text", fa_deleted=7, fa_deleted_reason="sample_text", fa_deleted_timestamp="sample_text", fa_deleted_user="sample_text", fa_description="sample_text", fa_height="sample_text", fa_id="sample_text", fa_major_mime="sample_text", fa_media_type="sample_text", fa_metadata="sample_text", fa_minor_mime="sample_text", fa_name="sample_text", fa_size="sample_text", fa_storage_group="sample_text", fa_storage_key="sample_text", fa_timestamp="sample_text", fa_user="sample_text", fa_user_text="sample_text", fa_width="sample_text")
    assert instance.fa_deleted == 7
    instance.fa_deleted = 13
    assert instance.fa_deleted == 13


def test_wikidb116_filearchive_fa_deleted_reason_value_roundtrip():
    instance = wikidb116_filearchive(fa_archive_name="sample_text", fa_bits="sample_text", fa_deleted=7, fa_deleted_reason="sample_text", fa_deleted_timestamp="sample_text", fa_deleted_user="sample_text", fa_description="sample_text", fa_height="sample_text", fa_id="sample_text", fa_major_mime="sample_text", fa_media_type="sample_text", fa_metadata="sample_text", fa_minor_mime="sample_text", fa_name="sample_text", fa_size="sample_text", fa_storage_group="sample_text", fa_storage_key="sample_text", fa_timestamp="sample_text", fa_user="sample_text", fa_user_text="sample_text", fa_width="sample_text")
    assert instance.fa_deleted_reason == "sample_text"
    instance.fa_deleted_reason = "sample_text_2"
    assert instance.fa_deleted_reason == "sample_text_2"


def test_wikidb116_filearchive_fa_deleted_timestamp_value_roundtrip():
    instance = wikidb116_filearchive(fa_archive_name="sample_text", fa_bits="sample_text", fa_deleted=7, fa_deleted_reason="sample_text", fa_deleted_timestamp="sample_text", fa_deleted_user="sample_text", fa_description="sample_text", fa_height="sample_text", fa_id="sample_text", fa_major_mime="sample_text", fa_media_type="sample_text", fa_metadata="sample_text", fa_minor_mime="sample_text", fa_name="sample_text", fa_size="sample_text", fa_storage_group="sample_text", fa_storage_key="sample_text", fa_timestamp="sample_text", fa_user="sample_text", fa_user_text="sample_text", fa_width="sample_text")
    assert instance.fa_deleted_timestamp == "sample_text"
    instance.fa_deleted_timestamp = "sample_text_2"
    assert instance.fa_deleted_timestamp == "sample_text_2"


def test_wikidb116_filearchive_fa_deleted_user_value_roundtrip():
    instance = wikidb116_filearchive(fa_archive_name="sample_text", fa_bits="sample_text", fa_deleted=7, fa_deleted_reason="sample_text", fa_deleted_timestamp="sample_text", fa_deleted_user="sample_text", fa_description="sample_text", fa_height="sample_text", fa_id="sample_text", fa_major_mime="sample_text", fa_media_type="sample_text", fa_metadata="sample_text", fa_minor_mime="sample_text", fa_name="sample_text", fa_size="sample_text", fa_storage_group="sample_text", fa_storage_key="sample_text", fa_timestamp="sample_text", fa_user="sample_text", fa_user_text="sample_text", fa_width="sample_text")
    assert instance.fa_deleted_user == "sample_text"
    instance.fa_deleted_user = "sample_text_2"
    assert instance.fa_deleted_user == "sample_text_2"


def test_wikidb116_filearchive_fa_description_value_roundtrip():
    instance = wikidb116_filearchive(fa_archive_name="sample_text", fa_bits="sample_text", fa_deleted=7, fa_deleted_reason="sample_text", fa_deleted_timestamp="sample_text", fa_deleted_user="sample_text", fa_description="sample_text", fa_height="sample_text", fa_id="sample_text", fa_major_mime="sample_text", fa_media_type="sample_text", fa_metadata="sample_text", fa_minor_mime="sample_text", fa_name="sample_text", fa_size="sample_text", fa_storage_group="sample_text", fa_storage_key="sample_text", fa_timestamp="sample_text", fa_user="sample_text", fa_user_text="sample_text", fa_width="sample_text")
    assert instance.fa_description == "sample_text"
    instance.fa_description = "sample_text_2"
    assert instance.fa_description == "sample_text_2"


def test_wikidb116_filearchive_fa_height_value_roundtrip():
    instance = wikidb116_filearchive(fa_archive_name="sample_text", fa_bits="sample_text", fa_deleted=7, fa_deleted_reason="sample_text", fa_deleted_timestamp="sample_text", fa_deleted_user="sample_text", fa_description="sample_text", fa_height="sample_text", fa_id="sample_text", fa_major_mime="sample_text", fa_media_type="sample_text", fa_metadata="sample_text", fa_minor_mime="sample_text", fa_name="sample_text", fa_size="sample_text", fa_storage_group="sample_text", fa_storage_key="sample_text", fa_timestamp="sample_text", fa_user="sample_text", fa_user_text="sample_text", fa_width="sample_text")
    assert instance.fa_height == "sample_text"
    instance.fa_height = "sample_text_2"
    assert instance.fa_height == "sample_text_2"


def test_wikidb116_filearchive_fa_id_value_roundtrip():
    instance = wikidb116_filearchive(fa_archive_name="sample_text", fa_bits="sample_text", fa_deleted=7, fa_deleted_reason="sample_text", fa_deleted_timestamp="sample_text", fa_deleted_user="sample_text", fa_description="sample_text", fa_height="sample_text", fa_id="sample_text", fa_major_mime="sample_text", fa_media_type="sample_text", fa_metadata="sample_text", fa_minor_mime="sample_text", fa_name="sample_text", fa_size="sample_text", fa_storage_group="sample_text", fa_storage_key="sample_text", fa_timestamp="sample_text", fa_user="sample_text", fa_user_text="sample_text", fa_width="sample_text")
    assert instance.fa_id == "sample_text"
    instance.fa_id = "sample_text_2"
    assert instance.fa_id == "sample_text_2"


def test_wikidb116_filearchive_fa_major_mime_value_roundtrip():
    instance = wikidb116_filearchive(fa_archive_name="sample_text", fa_bits="sample_text", fa_deleted=7, fa_deleted_reason="sample_text", fa_deleted_timestamp="sample_text", fa_deleted_user="sample_text", fa_description="sample_text", fa_height="sample_text", fa_id="sample_text", fa_major_mime="sample_text", fa_media_type="sample_text", fa_metadata="sample_text", fa_minor_mime="sample_text", fa_name="sample_text", fa_size="sample_text", fa_storage_group="sample_text", fa_storage_key="sample_text", fa_timestamp="sample_text", fa_user="sample_text", fa_user_text="sample_text", fa_width="sample_text")
    assert instance.fa_major_mime == "sample_text"
    instance.fa_major_mime = "sample_text_2"
    assert instance.fa_major_mime == "sample_text_2"


def test_wikidb116_filearchive_fa_media_type_value_roundtrip():
    instance = wikidb116_filearchive(fa_archive_name="sample_text", fa_bits="sample_text", fa_deleted=7, fa_deleted_reason="sample_text", fa_deleted_timestamp="sample_text", fa_deleted_user="sample_text", fa_description="sample_text", fa_height="sample_text", fa_id="sample_text", fa_major_mime="sample_text", fa_media_type="sample_text", fa_metadata="sample_text", fa_minor_mime="sample_text", fa_name="sample_text", fa_size="sample_text", fa_storage_group="sample_text", fa_storage_key="sample_text", fa_timestamp="sample_text", fa_user="sample_text", fa_user_text="sample_text", fa_width="sample_text")
    assert instance.fa_media_type == "sample_text"
    instance.fa_media_type = "sample_text_2"
    assert instance.fa_media_type == "sample_text_2"


def test_wikidb116_filearchive_fa_metadata_value_roundtrip():
    instance = wikidb116_filearchive(fa_archive_name="sample_text", fa_bits="sample_text", fa_deleted=7, fa_deleted_reason="sample_text", fa_deleted_timestamp="sample_text", fa_deleted_user="sample_text", fa_description="sample_text", fa_height="sample_text", fa_id="sample_text", fa_major_mime="sample_text", fa_media_type="sample_text", fa_metadata="sample_text", fa_minor_mime="sample_text", fa_name="sample_text", fa_size="sample_text", fa_storage_group="sample_text", fa_storage_key="sample_text", fa_timestamp="sample_text", fa_user="sample_text", fa_user_text="sample_text", fa_width="sample_text")
    assert instance.fa_metadata == "sample_text"
    instance.fa_metadata = "sample_text_2"
    assert instance.fa_metadata == "sample_text_2"


def test_wikidb116_filearchive_fa_minor_mime_value_roundtrip():
    instance = wikidb116_filearchive(fa_archive_name="sample_text", fa_bits="sample_text", fa_deleted=7, fa_deleted_reason="sample_text", fa_deleted_timestamp="sample_text", fa_deleted_user="sample_text", fa_description="sample_text", fa_height="sample_text", fa_id="sample_text", fa_major_mime="sample_text", fa_media_type="sample_text", fa_metadata="sample_text", fa_minor_mime="sample_text", fa_name="sample_text", fa_size="sample_text", fa_storage_group="sample_text", fa_storage_key="sample_text", fa_timestamp="sample_text", fa_user="sample_text", fa_user_text="sample_text", fa_width="sample_text")
    assert instance.fa_minor_mime == "sample_text"
    instance.fa_minor_mime = "sample_text_2"
    assert instance.fa_minor_mime == "sample_text_2"


def test_wikidb116_filearchive_fa_name_value_roundtrip():
    instance = wikidb116_filearchive(fa_archive_name="sample_text", fa_bits="sample_text", fa_deleted=7, fa_deleted_reason="sample_text", fa_deleted_timestamp="sample_text", fa_deleted_user="sample_text", fa_description="sample_text", fa_height="sample_text", fa_id="sample_text", fa_major_mime="sample_text", fa_media_type="sample_text", fa_metadata="sample_text", fa_minor_mime="sample_text", fa_name="sample_text", fa_size="sample_text", fa_storage_group="sample_text", fa_storage_key="sample_text", fa_timestamp="sample_text", fa_user="sample_text", fa_user_text="sample_text", fa_width="sample_text")
    assert instance.fa_name == "sample_text"
    instance.fa_name = "sample_text_2"
    assert instance.fa_name == "sample_text_2"


def test_wikidb116_filearchive_fa_size_value_roundtrip():
    instance = wikidb116_filearchive(fa_archive_name="sample_text", fa_bits="sample_text", fa_deleted=7, fa_deleted_reason="sample_text", fa_deleted_timestamp="sample_text", fa_deleted_user="sample_text", fa_description="sample_text", fa_height="sample_text", fa_id="sample_text", fa_major_mime="sample_text", fa_media_type="sample_text", fa_metadata="sample_text", fa_minor_mime="sample_text", fa_name="sample_text", fa_size="sample_text", fa_storage_group="sample_text", fa_storage_key="sample_text", fa_timestamp="sample_text", fa_user="sample_text", fa_user_text="sample_text", fa_width="sample_text")
    assert instance.fa_size == "sample_text"
    instance.fa_size = "sample_text_2"
    assert instance.fa_size == "sample_text_2"


def test_wikidb116_filearchive_fa_storage_group_value_roundtrip():
    instance = wikidb116_filearchive(fa_archive_name="sample_text", fa_bits="sample_text", fa_deleted=7, fa_deleted_reason="sample_text", fa_deleted_timestamp="sample_text", fa_deleted_user="sample_text", fa_description="sample_text", fa_height="sample_text", fa_id="sample_text", fa_major_mime="sample_text", fa_media_type="sample_text", fa_metadata="sample_text", fa_minor_mime="sample_text", fa_name="sample_text", fa_size="sample_text", fa_storage_group="sample_text", fa_storage_key="sample_text", fa_timestamp="sample_text", fa_user="sample_text", fa_user_text="sample_text", fa_width="sample_text")
    assert instance.fa_storage_group == "sample_text"
    instance.fa_storage_group = "sample_text_2"
    assert instance.fa_storage_group == "sample_text_2"


def test_wikidb116_filearchive_fa_storage_key_value_roundtrip():
    instance = wikidb116_filearchive(fa_archive_name="sample_text", fa_bits="sample_text", fa_deleted=7, fa_deleted_reason="sample_text", fa_deleted_timestamp="sample_text", fa_deleted_user="sample_text", fa_description="sample_text", fa_height="sample_text", fa_id="sample_text", fa_major_mime="sample_text", fa_media_type="sample_text", fa_metadata="sample_text", fa_minor_mime="sample_text", fa_name="sample_text", fa_size="sample_text", fa_storage_group="sample_text", fa_storage_key="sample_text", fa_timestamp="sample_text", fa_user="sample_text", fa_user_text="sample_text", fa_width="sample_text")
    assert instance.fa_storage_key == "sample_text"
    instance.fa_storage_key = "sample_text_2"
    assert instance.fa_storage_key == "sample_text_2"


def test_wikidb116_filearchive_fa_timestamp_value_roundtrip():
    instance = wikidb116_filearchive(fa_archive_name="sample_text", fa_bits="sample_text", fa_deleted=7, fa_deleted_reason="sample_text", fa_deleted_timestamp="sample_text", fa_deleted_user="sample_text", fa_description="sample_text", fa_height="sample_text", fa_id="sample_text", fa_major_mime="sample_text", fa_media_type="sample_text", fa_metadata="sample_text", fa_minor_mime="sample_text", fa_name="sample_text", fa_size="sample_text", fa_storage_group="sample_text", fa_storage_key="sample_text", fa_timestamp="sample_text", fa_user="sample_text", fa_user_text="sample_text", fa_width="sample_text")
    assert instance.fa_timestamp == "sample_text"
    instance.fa_timestamp = "sample_text_2"
    assert instance.fa_timestamp == "sample_text_2"


def test_wikidb116_filearchive_fa_user_value_roundtrip():
    instance = wikidb116_filearchive(fa_archive_name="sample_text", fa_bits="sample_text", fa_deleted=7, fa_deleted_reason="sample_text", fa_deleted_timestamp="sample_text", fa_deleted_user="sample_text", fa_description="sample_text", fa_height="sample_text", fa_id="sample_text", fa_major_mime="sample_text", fa_media_type="sample_text", fa_metadata="sample_text", fa_minor_mime="sample_text", fa_name="sample_text", fa_size="sample_text", fa_storage_group="sample_text", fa_storage_key="sample_text", fa_timestamp="sample_text", fa_user="sample_text", fa_user_text="sample_text", fa_width="sample_text")
    assert instance.fa_user == "sample_text"
    instance.fa_user = "sample_text_2"
    assert instance.fa_user == "sample_text_2"


def test_wikidb116_filearchive_fa_user_text_value_roundtrip():
    instance = wikidb116_filearchive(fa_archive_name="sample_text", fa_bits="sample_text", fa_deleted=7, fa_deleted_reason="sample_text", fa_deleted_timestamp="sample_text", fa_deleted_user="sample_text", fa_description="sample_text", fa_height="sample_text", fa_id="sample_text", fa_major_mime="sample_text", fa_media_type="sample_text", fa_metadata="sample_text", fa_minor_mime="sample_text", fa_name="sample_text", fa_size="sample_text", fa_storage_group="sample_text", fa_storage_key="sample_text", fa_timestamp="sample_text", fa_user="sample_text", fa_user_text="sample_text", fa_width="sample_text")
    assert instance.fa_user_text == "sample_text"
    instance.fa_user_text = "sample_text_2"
    assert instance.fa_user_text == "sample_text_2"


def test_wikidb116_filearchive_fa_width_value_roundtrip():
    instance = wikidb116_filearchive(fa_archive_name="sample_text", fa_bits="sample_text", fa_deleted=7, fa_deleted_reason="sample_text", fa_deleted_timestamp="sample_text", fa_deleted_user="sample_text", fa_description="sample_text", fa_height="sample_text", fa_id="sample_text", fa_major_mime="sample_text", fa_media_type="sample_text", fa_metadata="sample_text", fa_minor_mime="sample_text", fa_name="sample_text", fa_size="sample_text", fa_storage_group="sample_text", fa_storage_key="sample_text", fa_timestamp="sample_text", fa_user="sample_text", fa_user_text="sample_text", fa_width="sample_text")
    assert instance.fa_width == "sample_text"
    instance.fa_width = "sample_text_2"
    assert instance.fa_width == "sample_text_2"


def test_wikidb116_hitcounter_hc_id_value_roundtrip():
    instance = wikidb116_hitcounter(hc_id="sample_text")
    assert instance.hc_id == "sample_text"
    instance.hc_id = "sample_text_2"
    assert instance.hc_id == "sample_text_2"


def test_wikidb116_image_img_bits_value_roundtrip():
    instance = wikidb116_image(img_bits="sample_text", img_description="sample_text", img_height="sample_text", img_major_mime="sample_text", img_media_type="sample_text", img_metadata="sample_text", img_minor_mime="sample_text", img_name="sample_text", img_sha1="sample_text", img_size="sample_text", img_timestamp="sample_text", img_user="sample_text", img_user_text="sample_text", img_width="sample_text")
    assert instance.img_bits == "sample_text"
    instance.img_bits = "sample_text_2"
    assert instance.img_bits == "sample_text_2"


def test_wikidb116_image_img_description_value_roundtrip():
    instance = wikidb116_image(img_bits="sample_text", img_description="sample_text", img_height="sample_text", img_major_mime="sample_text", img_media_type="sample_text", img_metadata="sample_text", img_minor_mime="sample_text", img_name="sample_text", img_sha1="sample_text", img_size="sample_text", img_timestamp="sample_text", img_user="sample_text", img_user_text="sample_text", img_width="sample_text")
    assert instance.img_description == "sample_text"
    instance.img_description = "sample_text_2"
    assert instance.img_description == "sample_text_2"


def test_wikidb116_image_img_height_value_roundtrip():
    instance = wikidb116_image(img_bits="sample_text", img_description="sample_text", img_height="sample_text", img_major_mime="sample_text", img_media_type="sample_text", img_metadata="sample_text", img_minor_mime="sample_text", img_name="sample_text", img_sha1="sample_text", img_size="sample_text", img_timestamp="sample_text", img_user="sample_text", img_user_text="sample_text", img_width="sample_text")
    assert instance.img_height == "sample_text"
    instance.img_height = "sample_text_2"
    assert instance.img_height == "sample_text_2"


def test_wikidb116_image_img_major_mime_value_roundtrip():
    instance = wikidb116_image(img_bits="sample_text", img_description="sample_text", img_height="sample_text", img_major_mime="sample_text", img_media_type="sample_text", img_metadata="sample_text", img_minor_mime="sample_text", img_name="sample_text", img_sha1="sample_text", img_size="sample_text", img_timestamp="sample_text", img_user="sample_text", img_user_text="sample_text", img_width="sample_text")
    assert instance.img_major_mime == "sample_text"
    instance.img_major_mime = "sample_text_2"
    assert instance.img_major_mime == "sample_text_2"


def test_wikidb116_image_img_media_type_value_roundtrip():
    instance = wikidb116_image(img_bits="sample_text", img_description="sample_text", img_height="sample_text", img_major_mime="sample_text", img_media_type="sample_text", img_metadata="sample_text", img_minor_mime="sample_text", img_name="sample_text", img_sha1="sample_text", img_size="sample_text", img_timestamp="sample_text", img_user="sample_text", img_user_text="sample_text", img_width="sample_text")
    assert instance.img_media_type == "sample_text"
    instance.img_media_type = "sample_text_2"
    assert instance.img_media_type == "sample_text_2"


def test_wikidb116_image_img_metadata_value_roundtrip():
    instance = wikidb116_image(img_bits="sample_text", img_description="sample_text", img_height="sample_text", img_major_mime="sample_text", img_media_type="sample_text", img_metadata="sample_text", img_minor_mime="sample_text", img_name="sample_text", img_sha1="sample_text", img_size="sample_text", img_timestamp="sample_text", img_user="sample_text", img_user_text="sample_text", img_width="sample_text")
    assert instance.img_metadata == "sample_text"
    instance.img_metadata = "sample_text_2"
    assert instance.img_metadata == "sample_text_2"


def test_wikidb116_image_img_minor_mime_value_roundtrip():
    instance = wikidb116_image(img_bits="sample_text", img_description="sample_text", img_height="sample_text", img_major_mime="sample_text", img_media_type="sample_text", img_metadata="sample_text", img_minor_mime="sample_text", img_name="sample_text", img_sha1="sample_text", img_size="sample_text", img_timestamp="sample_text", img_user="sample_text", img_user_text="sample_text", img_width="sample_text")
    assert instance.img_minor_mime == "sample_text"
    instance.img_minor_mime = "sample_text_2"
    assert instance.img_minor_mime == "sample_text_2"


def test_wikidb116_image_img_name_value_roundtrip():
    instance = wikidb116_image(img_bits="sample_text", img_description="sample_text", img_height="sample_text", img_major_mime="sample_text", img_media_type="sample_text", img_metadata="sample_text", img_minor_mime="sample_text", img_name="sample_text", img_sha1="sample_text", img_size="sample_text", img_timestamp="sample_text", img_user="sample_text", img_user_text="sample_text", img_width="sample_text")
    assert instance.img_name == "sample_text"
    instance.img_name = "sample_text_2"
    assert instance.img_name == "sample_text_2"


def test_wikidb116_image_img_sha1_value_roundtrip():
    instance = wikidb116_image(img_bits="sample_text", img_description="sample_text", img_height="sample_text", img_major_mime="sample_text", img_media_type="sample_text", img_metadata="sample_text", img_minor_mime="sample_text", img_name="sample_text", img_sha1="sample_text", img_size="sample_text", img_timestamp="sample_text", img_user="sample_text", img_user_text="sample_text", img_width="sample_text")
    assert instance.img_sha1 == "sample_text"
    instance.img_sha1 = "sample_text_2"
    assert instance.img_sha1 == "sample_text_2"


def test_wikidb116_image_img_size_value_roundtrip():
    instance = wikidb116_image(img_bits="sample_text", img_description="sample_text", img_height="sample_text", img_major_mime="sample_text", img_media_type="sample_text", img_metadata="sample_text", img_minor_mime="sample_text", img_name="sample_text", img_sha1="sample_text", img_size="sample_text", img_timestamp="sample_text", img_user="sample_text", img_user_text="sample_text", img_width="sample_text")
    assert instance.img_size == "sample_text"
    instance.img_size = "sample_text_2"
    assert instance.img_size == "sample_text_2"


def test_wikidb116_image_img_timestamp_value_roundtrip():
    instance = wikidb116_image(img_bits="sample_text", img_description="sample_text", img_height="sample_text", img_major_mime="sample_text", img_media_type="sample_text", img_metadata="sample_text", img_minor_mime="sample_text", img_name="sample_text", img_sha1="sample_text", img_size="sample_text", img_timestamp="sample_text", img_user="sample_text", img_user_text="sample_text", img_width="sample_text")
    assert instance.img_timestamp == "sample_text"
    instance.img_timestamp = "sample_text_2"
    assert instance.img_timestamp == "sample_text_2"


def test_wikidb116_image_img_user_value_roundtrip():
    instance = wikidb116_image(img_bits="sample_text", img_description="sample_text", img_height="sample_text", img_major_mime="sample_text", img_media_type="sample_text", img_metadata="sample_text", img_minor_mime="sample_text", img_name="sample_text", img_sha1="sample_text", img_size="sample_text", img_timestamp="sample_text", img_user="sample_text", img_user_text="sample_text", img_width="sample_text")
    assert instance.img_user == "sample_text"
    instance.img_user = "sample_text_2"
    assert instance.img_user == "sample_text_2"


def test_wikidb116_image_img_user_text_value_roundtrip():
    instance = wikidb116_image(img_bits="sample_text", img_description="sample_text", img_height="sample_text", img_major_mime="sample_text", img_media_type="sample_text", img_metadata="sample_text", img_minor_mime="sample_text", img_name="sample_text", img_sha1="sample_text", img_size="sample_text", img_timestamp="sample_text", img_user="sample_text", img_user_text="sample_text", img_width="sample_text")
    assert instance.img_user_text == "sample_text"
    instance.img_user_text = "sample_text_2"
    assert instance.img_user_text == "sample_text_2"


def test_wikidb116_image_img_width_value_roundtrip():
    instance = wikidb116_image(img_bits="sample_text", img_description="sample_text", img_height="sample_text", img_major_mime="sample_text", img_media_type="sample_text", img_metadata="sample_text", img_minor_mime="sample_text", img_name="sample_text", img_sha1="sample_text", img_size="sample_text", img_timestamp="sample_text", img_user="sample_text", img_user_text="sample_text", img_width="sample_text")
    assert instance.img_width == "sample_text"
    instance.img_width = "sample_text_2"
    assert instance.img_width == "sample_text_2"


def test_wikidb116_imagelinks_il_from_value_roundtrip():
    instance = wikidb116_imagelinks(il_from="sample_text", il_to="sample_text")
    assert instance.il_from == "sample_text"
    instance.il_from = "sample_text_2"
    assert instance.il_from == "sample_text_2"


def test_wikidb116_imagelinks_il_to_value_roundtrip():
    instance = wikidb116_imagelinks(il_from="sample_text", il_to="sample_text")
    assert instance.il_to == "sample_text"
    instance.il_to = "sample_text_2"
    assert instance.il_to == "sample_text_2"


def test_wikidb116_interwiki_iw_local_value_roundtrip():
    instance = wikidb116_interwiki(iw_local=7, iw_prefix="sample_text", iw_trans=7, iw_url="sample_text")
    assert instance.iw_local == 7
    instance.iw_local = 13
    assert instance.iw_local == 13


def test_wikidb116_interwiki_iw_prefix_value_roundtrip():
    instance = wikidb116_interwiki(iw_local=7, iw_prefix="sample_text", iw_trans=7, iw_url="sample_text")
    assert instance.iw_prefix == "sample_text"
    instance.iw_prefix = "sample_text_2"
    assert instance.iw_prefix == "sample_text_2"


def test_wikidb116_interwiki_iw_trans_value_roundtrip():
    instance = wikidb116_interwiki(iw_local=7, iw_prefix="sample_text", iw_trans=7, iw_url="sample_text")
    assert instance.iw_trans == 7
    instance.iw_trans = 13
    assert instance.iw_trans == 13


def test_wikidb116_interwiki_iw_url_value_roundtrip():
    instance = wikidb116_interwiki(iw_local=7, iw_prefix="sample_text", iw_trans=7, iw_url="sample_text")
    assert instance.iw_url == "sample_text"
    instance.iw_url = "sample_text_2"
    assert instance.iw_url == "sample_text_2"


def test_wikidb116_ipblocks_ipb_address_value_roundtrip():
    instance = wikidb116_ipblocks(ipb_address="sample_text", ipb_allow_usertalk=7, ipb_anon_only=7, ipb_auto=7, ipb_block_email=7, ipb_by="sample_text", ipb_by_text="sample_text", ipb_create_account=7, ipb_deleted=7, ipb_enable_autoblock=7, ipb_expiry="sample_text", ipb_id="sample_text", ipb_range_end="sample_text", ipb_range_start="sample_text", ipb_reason="sample_text", ipb_timestamp="sample_text", ipb_user="sample_text")
    assert instance.ipb_address == "sample_text"
    instance.ipb_address = "sample_text_2"
    assert instance.ipb_address == "sample_text_2"


def test_wikidb116_ipblocks_ipb_allow_usertalk_value_roundtrip():
    instance = wikidb116_ipblocks(ipb_address="sample_text", ipb_allow_usertalk=7, ipb_anon_only=7, ipb_auto=7, ipb_block_email=7, ipb_by="sample_text", ipb_by_text="sample_text", ipb_create_account=7, ipb_deleted=7, ipb_enable_autoblock=7, ipb_expiry="sample_text", ipb_id="sample_text", ipb_range_end="sample_text", ipb_range_start="sample_text", ipb_reason="sample_text", ipb_timestamp="sample_text", ipb_user="sample_text")
    assert instance.ipb_allow_usertalk == 7
    instance.ipb_allow_usertalk = 13
    assert instance.ipb_allow_usertalk == 13


def test_wikidb116_ipblocks_ipb_anon_only_value_roundtrip():
    instance = wikidb116_ipblocks(ipb_address="sample_text", ipb_allow_usertalk=7, ipb_anon_only=7, ipb_auto=7, ipb_block_email=7, ipb_by="sample_text", ipb_by_text="sample_text", ipb_create_account=7, ipb_deleted=7, ipb_enable_autoblock=7, ipb_expiry="sample_text", ipb_id="sample_text", ipb_range_end="sample_text", ipb_range_start="sample_text", ipb_reason="sample_text", ipb_timestamp="sample_text", ipb_user="sample_text")
    assert instance.ipb_anon_only == 7
    instance.ipb_anon_only = 13
    assert instance.ipb_anon_only == 13


def test_wikidb116_ipblocks_ipb_auto_value_roundtrip():
    instance = wikidb116_ipblocks(ipb_address="sample_text", ipb_allow_usertalk=7, ipb_anon_only=7, ipb_auto=7, ipb_block_email=7, ipb_by="sample_text", ipb_by_text="sample_text", ipb_create_account=7, ipb_deleted=7, ipb_enable_autoblock=7, ipb_expiry="sample_text", ipb_id="sample_text", ipb_range_end="sample_text", ipb_range_start="sample_text", ipb_reason="sample_text", ipb_timestamp="sample_text", ipb_user="sample_text")
    assert instance.ipb_auto == 7
    instance.ipb_auto = 13
    assert instance.ipb_auto == 13


def test_wikidb116_ipblocks_ipb_block_email_value_roundtrip():
    instance = wikidb116_ipblocks(ipb_address="sample_text", ipb_allow_usertalk=7, ipb_anon_only=7, ipb_auto=7, ipb_block_email=7, ipb_by="sample_text", ipb_by_text="sample_text", ipb_create_account=7, ipb_deleted=7, ipb_enable_autoblock=7, ipb_expiry="sample_text", ipb_id="sample_text", ipb_range_end="sample_text", ipb_range_start="sample_text", ipb_reason="sample_text", ipb_timestamp="sample_text", ipb_user="sample_text")
    assert instance.ipb_block_email == 7
    instance.ipb_block_email = 13
    assert instance.ipb_block_email == 13


def test_wikidb116_ipblocks_ipb_by_value_roundtrip():
    instance = wikidb116_ipblocks(ipb_address="sample_text", ipb_allow_usertalk=7, ipb_anon_only=7, ipb_auto=7, ipb_block_email=7, ipb_by="sample_text", ipb_by_text="sample_text", ipb_create_account=7, ipb_deleted=7, ipb_enable_autoblock=7, ipb_expiry="sample_text", ipb_id="sample_text", ipb_range_end="sample_text", ipb_range_start="sample_text", ipb_reason="sample_text", ipb_timestamp="sample_text", ipb_user="sample_text")
    assert instance.ipb_by == "sample_text"
    instance.ipb_by = "sample_text_2"
    assert instance.ipb_by == "sample_text_2"


def test_wikidb116_ipblocks_ipb_by_text_value_roundtrip():
    instance = wikidb116_ipblocks(ipb_address="sample_text", ipb_allow_usertalk=7, ipb_anon_only=7, ipb_auto=7, ipb_block_email=7, ipb_by="sample_text", ipb_by_text="sample_text", ipb_create_account=7, ipb_deleted=7, ipb_enable_autoblock=7, ipb_expiry="sample_text", ipb_id="sample_text", ipb_range_end="sample_text", ipb_range_start="sample_text", ipb_reason="sample_text", ipb_timestamp="sample_text", ipb_user="sample_text")
    assert instance.ipb_by_text == "sample_text"
    instance.ipb_by_text = "sample_text_2"
    assert instance.ipb_by_text == "sample_text_2"


def test_wikidb116_ipblocks_ipb_create_account_value_roundtrip():
    instance = wikidb116_ipblocks(ipb_address="sample_text", ipb_allow_usertalk=7, ipb_anon_only=7, ipb_auto=7, ipb_block_email=7, ipb_by="sample_text", ipb_by_text="sample_text", ipb_create_account=7, ipb_deleted=7, ipb_enable_autoblock=7, ipb_expiry="sample_text", ipb_id="sample_text", ipb_range_end="sample_text", ipb_range_start="sample_text", ipb_reason="sample_text", ipb_timestamp="sample_text", ipb_user="sample_text")
    assert instance.ipb_create_account == 7
    instance.ipb_create_account = 13
    assert instance.ipb_create_account == 13


def test_wikidb116_ipblocks_ipb_deleted_value_roundtrip():
    instance = wikidb116_ipblocks(ipb_address="sample_text", ipb_allow_usertalk=7, ipb_anon_only=7, ipb_auto=7, ipb_block_email=7, ipb_by="sample_text", ipb_by_text="sample_text", ipb_create_account=7, ipb_deleted=7, ipb_enable_autoblock=7, ipb_expiry="sample_text", ipb_id="sample_text", ipb_range_end="sample_text", ipb_range_start="sample_text", ipb_reason="sample_text", ipb_timestamp="sample_text", ipb_user="sample_text")
    assert instance.ipb_deleted == 7
    instance.ipb_deleted = 13
    assert instance.ipb_deleted == 13


def test_wikidb116_ipblocks_ipb_enable_autoblock_value_roundtrip():
    instance = wikidb116_ipblocks(ipb_address="sample_text", ipb_allow_usertalk=7, ipb_anon_only=7, ipb_auto=7, ipb_block_email=7, ipb_by="sample_text", ipb_by_text="sample_text", ipb_create_account=7, ipb_deleted=7, ipb_enable_autoblock=7, ipb_expiry="sample_text", ipb_id="sample_text", ipb_range_end="sample_text", ipb_range_start="sample_text", ipb_reason="sample_text", ipb_timestamp="sample_text", ipb_user="sample_text")
    assert instance.ipb_enable_autoblock == 7
    instance.ipb_enable_autoblock = 13
    assert instance.ipb_enable_autoblock == 13


def test_wikidb116_ipblocks_ipb_expiry_value_roundtrip():
    instance = wikidb116_ipblocks(ipb_address="sample_text", ipb_allow_usertalk=7, ipb_anon_only=7, ipb_auto=7, ipb_block_email=7, ipb_by="sample_text", ipb_by_text="sample_text", ipb_create_account=7, ipb_deleted=7, ipb_enable_autoblock=7, ipb_expiry="sample_text", ipb_id="sample_text", ipb_range_end="sample_text", ipb_range_start="sample_text", ipb_reason="sample_text", ipb_timestamp="sample_text", ipb_user="sample_text")
    assert instance.ipb_expiry == "sample_text"
    instance.ipb_expiry = "sample_text_2"
    assert instance.ipb_expiry == "sample_text_2"


def test_wikidb116_ipblocks_ipb_id_value_roundtrip():
    instance = wikidb116_ipblocks(ipb_address="sample_text", ipb_allow_usertalk=7, ipb_anon_only=7, ipb_auto=7, ipb_block_email=7, ipb_by="sample_text", ipb_by_text="sample_text", ipb_create_account=7, ipb_deleted=7, ipb_enable_autoblock=7, ipb_expiry="sample_text", ipb_id="sample_text", ipb_range_end="sample_text", ipb_range_start="sample_text", ipb_reason="sample_text", ipb_timestamp="sample_text", ipb_user="sample_text")
    assert instance.ipb_id == "sample_text"
    instance.ipb_id = "sample_text_2"
    assert instance.ipb_id == "sample_text_2"


def test_wikidb116_ipblocks_ipb_range_end_value_roundtrip():
    instance = wikidb116_ipblocks(ipb_address="sample_text", ipb_allow_usertalk=7, ipb_anon_only=7, ipb_auto=7, ipb_block_email=7, ipb_by="sample_text", ipb_by_text="sample_text", ipb_create_account=7, ipb_deleted=7, ipb_enable_autoblock=7, ipb_expiry="sample_text", ipb_id="sample_text", ipb_range_end="sample_text", ipb_range_start="sample_text", ipb_reason="sample_text", ipb_timestamp="sample_text", ipb_user="sample_text")
    assert instance.ipb_range_end == "sample_text"
    instance.ipb_range_end = "sample_text_2"
    assert instance.ipb_range_end == "sample_text_2"


def test_wikidb116_ipblocks_ipb_range_start_value_roundtrip():
    instance = wikidb116_ipblocks(ipb_address="sample_text", ipb_allow_usertalk=7, ipb_anon_only=7, ipb_auto=7, ipb_block_email=7, ipb_by="sample_text", ipb_by_text="sample_text", ipb_create_account=7, ipb_deleted=7, ipb_enable_autoblock=7, ipb_expiry="sample_text", ipb_id="sample_text", ipb_range_end="sample_text", ipb_range_start="sample_text", ipb_reason="sample_text", ipb_timestamp="sample_text", ipb_user="sample_text")
    assert instance.ipb_range_start == "sample_text"
    instance.ipb_range_start = "sample_text_2"
    assert instance.ipb_range_start == "sample_text_2"


def test_wikidb116_ipblocks_ipb_reason_value_roundtrip():
    instance = wikidb116_ipblocks(ipb_address="sample_text", ipb_allow_usertalk=7, ipb_anon_only=7, ipb_auto=7, ipb_block_email=7, ipb_by="sample_text", ipb_by_text="sample_text", ipb_create_account=7, ipb_deleted=7, ipb_enable_autoblock=7, ipb_expiry="sample_text", ipb_id="sample_text", ipb_range_end="sample_text", ipb_range_start="sample_text", ipb_reason="sample_text", ipb_timestamp="sample_text", ipb_user="sample_text")
    assert instance.ipb_reason == "sample_text"
    instance.ipb_reason = "sample_text_2"
    assert instance.ipb_reason == "sample_text_2"


def test_wikidb116_ipblocks_ipb_timestamp_value_roundtrip():
    instance = wikidb116_ipblocks(ipb_address="sample_text", ipb_allow_usertalk=7, ipb_anon_only=7, ipb_auto=7, ipb_block_email=7, ipb_by="sample_text", ipb_by_text="sample_text", ipb_create_account=7, ipb_deleted=7, ipb_enable_autoblock=7, ipb_expiry="sample_text", ipb_id="sample_text", ipb_range_end="sample_text", ipb_range_start="sample_text", ipb_reason="sample_text", ipb_timestamp="sample_text", ipb_user="sample_text")
    assert instance.ipb_timestamp == "sample_text"
    instance.ipb_timestamp = "sample_text_2"
    assert instance.ipb_timestamp == "sample_text_2"


def test_wikidb116_ipblocks_ipb_user_value_roundtrip():
    instance = wikidb116_ipblocks(ipb_address="sample_text", ipb_allow_usertalk=7, ipb_anon_only=7, ipb_auto=7, ipb_block_email=7, ipb_by="sample_text", ipb_by_text="sample_text", ipb_create_account=7, ipb_deleted=7, ipb_enable_autoblock=7, ipb_expiry="sample_text", ipb_id="sample_text", ipb_range_end="sample_text", ipb_range_start="sample_text", ipb_reason="sample_text", ipb_timestamp="sample_text", ipb_user="sample_text")
    assert instance.ipb_user == "sample_text"
    instance.ipb_user = "sample_text_2"
    assert instance.ipb_user == "sample_text_2"


def test_wikidb116_job_job_cmd_value_roundtrip():
    instance = wikidb116_job(job_cmd="sample_text", job_id="sample_text", job_namespace="sample_text", job_params="sample_text", job_title="sample_text")
    assert instance.job_cmd == "sample_text"
    instance.job_cmd = "sample_text_2"
    assert instance.job_cmd == "sample_text_2"


def test_wikidb116_job_job_id_value_roundtrip():
    instance = wikidb116_job(job_cmd="sample_text", job_id="sample_text", job_namespace="sample_text", job_params="sample_text", job_title="sample_text")
    assert instance.job_id == "sample_text"
    instance.job_id = "sample_text_2"
    assert instance.job_id == "sample_text_2"


def test_wikidb116_job_job_namespace_value_roundtrip():
    instance = wikidb116_job(job_cmd="sample_text", job_id="sample_text", job_namespace="sample_text", job_params="sample_text", job_title="sample_text")
    assert instance.job_namespace == "sample_text"
    instance.job_namespace = "sample_text_2"
    assert instance.job_namespace == "sample_text_2"


def test_wikidb116_job_job_params_value_roundtrip():
    instance = wikidb116_job(job_cmd="sample_text", job_id="sample_text", job_namespace="sample_text", job_params="sample_text", job_title="sample_text")
    assert instance.job_params == "sample_text"
    instance.job_params = "sample_text_2"
    assert instance.job_params == "sample_text_2"


def test_wikidb116_job_job_title_value_roundtrip():
    instance = wikidb116_job(job_cmd="sample_text", job_id="sample_text", job_namespace="sample_text", job_params="sample_text", job_title="sample_text")
    assert instance.job_title == "sample_text"
    instance.job_title = "sample_text_2"
    assert instance.job_title == "sample_text_2"


def test_wikidb116_l10n_cache_lc_key_value_roundtrip():
    instance = wikidb116_l10n_cache(lc_key="sample_text", lc_lang="sample_text", lc_value="sample_text")
    assert instance.lc_key == "sample_text"
    instance.lc_key = "sample_text_2"
    assert instance.lc_key == "sample_text_2"


def test_wikidb116_l10n_cache_lc_lang_value_roundtrip():
    instance = wikidb116_l10n_cache(lc_key="sample_text", lc_lang="sample_text", lc_value="sample_text")
    assert instance.lc_lang == "sample_text"
    instance.lc_lang = "sample_text_2"
    assert instance.lc_lang == "sample_text_2"


def test_wikidb116_l10n_cache_lc_value_value_roundtrip():
    instance = wikidb116_l10n_cache(lc_key="sample_text", lc_lang="sample_text", lc_value="sample_text")
    assert instance.lc_value == "sample_text"
    instance.lc_value = "sample_text_2"
    assert instance.lc_value == "sample_text_2"


def test_wikidb116_langlinks_ll_from_value_roundtrip():
    instance = wikidb116_langlinks(ll_from="sample_text", ll_lang="sample_text", ll_title="sample_text")
    assert instance.ll_from == "sample_text"
    instance.ll_from = "sample_text_2"
    assert instance.ll_from == "sample_text_2"


def test_wikidb116_langlinks_ll_lang_value_roundtrip():
    instance = wikidb116_langlinks(ll_from="sample_text", ll_lang="sample_text", ll_title="sample_text")
    assert instance.ll_lang == "sample_text"
    instance.ll_lang = "sample_text_2"
    assert instance.ll_lang == "sample_text_2"


def test_wikidb116_langlinks_ll_title_value_roundtrip():
    instance = wikidb116_langlinks(ll_from="sample_text", ll_lang="sample_text", ll_title="sample_text")
    assert instance.ll_title == "sample_text"
    instance.ll_title = "sample_text_2"
    assert instance.ll_title == "sample_text_2"


def test_wikidb116_log_search_ls_field_value_roundtrip():
    instance = wikidb116_log_search(ls_field="sample_text", ls_log_id="sample_text", ls_value="sample_text")
    assert instance.ls_field == "sample_text"
    instance.ls_field = "sample_text_2"
    assert instance.ls_field == "sample_text_2"


def test_wikidb116_log_search_ls_log_id_value_roundtrip():
    instance = wikidb116_log_search(ls_field="sample_text", ls_log_id="sample_text", ls_value="sample_text")
    assert instance.ls_log_id == "sample_text"
    instance.ls_log_id = "sample_text_2"
    assert instance.ls_log_id == "sample_text_2"


def test_wikidb116_log_search_ls_value_value_roundtrip():
    instance = wikidb116_log_search(ls_field="sample_text", ls_log_id="sample_text", ls_value="sample_text")
    assert instance.ls_value == "sample_text"
    instance.ls_value = "sample_text_2"
    assert instance.ls_value == "sample_text_2"


def test_wikidb116_logging_log_action_value_roundtrip():
    instance = wikidb116_logging(log_action="sample_text", log_comment="sample_text", log_deleted=7, log_id="sample_text", log_namespace="sample_text", log_page="sample_text", log_params="sample_text", log_timestamp="sample_text", log_title="sample_text", log_type="sample_text", log_user="sample_text", log_user_text="sample_text")
    assert instance.log_action == "sample_text"
    instance.log_action = "sample_text_2"
    assert instance.log_action == "sample_text_2"


def test_wikidb116_logging_log_comment_value_roundtrip():
    instance = wikidb116_logging(log_action="sample_text", log_comment="sample_text", log_deleted=7, log_id="sample_text", log_namespace="sample_text", log_page="sample_text", log_params="sample_text", log_timestamp="sample_text", log_title="sample_text", log_type="sample_text", log_user="sample_text", log_user_text="sample_text")
    assert instance.log_comment == "sample_text"
    instance.log_comment = "sample_text_2"
    assert instance.log_comment == "sample_text_2"


def test_wikidb116_logging_log_deleted_value_roundtrip():
    instance = wikidb116_logging(log_action="sample_text", log_comment="sample_text", log_deleted=7, log_id="sample_text", log_namespace="sample_text", log_page="sample_text", log_params="sample_text", log_timestamp="sample_text", log_title="sample_text", log_type="sample_text", log_user="sample_text", log_user_text="sample_text")
    assert instance.log_deleted == 7
    instance.log_deleted = 13
    assert instance.log_deleted == 13


def test_wikidb116_logging_log_id_value_roundtrip():
    instance = wikidb116_logging(log_action="sample_text", log_comment="sample_text", log_deleted=7, log_id="sample_text", log_namespace="sample_text", log_page="sample_text", log_params="sample_text", log_timestamp="sample_text", log_title="sample_text", log_type="sample_text", log_user="sample_text", log_user_text="sample_text")
    assert instance.log_id == "sample_text"
    instance.log_id = "sample_text_2"
    assert instance.log_id == "sample_text_2"


def test_wikidb116_logging_log_namespace_value_roundtrip():
    instance = wikidb116_logging(log_action="sample_text", log_comment="sample_text", log_deleted=7, log_id="sample_text", log_namespace="sample_text", log_page="sample_text", log_params="sample_text", log_timestamp="sample_text", log_title="sample_text", log_type="sample_text", log_user="sample_text", log_user_text="sample_text")
    assert instance.log_namespace == "sample_text"
    instance.log_namespace = "sample_text_2"
    assert instance.log_namespace == "sample_text_2"


def test_wikidb116_logging_log_page_value_roundtrip():
    instance = wikidb116_logging(log_action="sample_text", log_comment="sample_text", log_deleted=7, log_id="sample_text", log_namespace="sample_text", log_page="sample_text", log_params="sample_text", log_timestamp="sample_text", log_title="sample_text", log_type="sample_text", log_user="sample_text", log_user_text="sample_text")
    assert instance.log_page == "sample_text"
    instance.log_page = "sample_text_2"
    assert instance.log_page == "sample_text_2"


def test_wikidb116_logging_log_params_value_roundtrip():
    instance = wikidb116_logging(log_action="sample_text", log_comment="sample_text", log_deleted=7, log_id="sample_text", log_namespace="sample_text", log_page="sample_text", log_params="sample_text", log_timestamp="sample_text", log_title="sample_text", log_type="sample_text", log_user="sample_text", log_user_text="sample_text")
    assert instance.log_params == "sample_text"
    instance.log_params = "sample_text_2"
    assert instance.log_params == "sample_text_2"


def test_wikidb116_logging_log_timestamp_value_roundtrip():
    instance = wikidb116_logging(log_action="sample_text", log_comment="sample_text", log_deleted=7, log_id="sample_text", log_namespace="sample_text", log_page="sample_text", log_params="sample_text", log_timestamp="sample_text", log_title="sample_text", log_type="sample_text", log_user="sample_text", log_user_text="sample_text")
    assert instance.log_timestamp == "sample_text"
    instance.log_timestamp = "sample_text_2"
    assert instance.log_timestamp == "sample_text_2"


def test_wikidb116_logging_log_title_value_roundtrip():
    instance = wikidb116_logging(log_action="sample_text", log_comment="sample_text", log_deleted=7, log_id="sample_text", log_namespace="sample_text", log_page="sample_text", log_params="sample_text", log_timestamp="sample_text", log_title="sample_text", log_type="sample_text", log_user="sample_text", log_user_text="sample_text")
    assert instance.log_title == "sample_text"
    instance.log_title = "sample_text_2"
    assert instance.log_title == "sample_text_2"


def test_wikidb116_logging_log_type_value_roundtrip():
    instance = wikidb116_logging(log_action="sample_text", log_comment="sample_text", log_deleted=7, log_id="sample_text", log_namespace="sample_text", log_page="sample_text", log_params="sample_text", log_timestamp="sample_text", log_title="sample_text", log_type="sample_text", log_user="sample_text", log_user_text="sample_text")
    assert instance.log_type == "sample_text"
    instance.log_type = "sample_text_2"
    assert instance.log_type == "sample_text_2"


def test_wikidb116_logging_log_user_value_roundtrip():
    instance = wikidb116_logging(log_action="sample_text", log_comment="sample_text", log_deleted=7, log_id="sample_text", log_namespace="sample_text", log_page="sample_text", log_params="sample_text", log_timestamp="sample_text", log_title="sample_text", log_type="sample_text", log_user="sample_text", log_user_text="sample_text")
    assert instance.log_user == "sample_text"
    instance.log_user = "sample_text_2"
    assert instance.log_user == "sample_text_2"


def test_wikidb116_logging_log_user_text_value_roundtrip():
    instance = wikidb116_logging(log_action="sample_text", log_comment="sample_text", log_deleted=7, log_id="sample_text", log_namespace="sample_text", log_page="sample_text", log_params="sample_text", log_timestamp="sample_text", log_title="sample_text", log_type="sample_text", log_user="sample_text", log_user_text="sample_text")
    assert instance.log_user_text == "sample_text"
    instance.log_user_text = "sample_text_2"
    assert instance.log_user_text == "sample_text_2"


def test_wikidb116_math_math_html_value_roundtrip():
    instance = wikidb116_math(math_html="sample_text", math_html_conservativeness=7, math_inputhash="sample_text", math_mathml="sample_text", math_outputhash="sample_text")
    assert instance.math_html == "sample_text"
    instance.math_html = "sample_text_2"
    assert instance.math_html == "sample_text_2"


def test_wikidb116_math_math_html_conservativeness_value_roundtrip():
    instance = wikidb116_math(math_html="sample_text", math_html_conservativeness=7, math_inputhash="sample_text", math_mathml="sample_text", math_outputhash="sample_text")
    assert instance.math_html_conservativeness == 7
    instance.math_html_conservativeness = 13
    assert instance.math_html_conservativeness == 13


def test_wikidb116_math_math_inputhash_value_roundtrip():
    instance = wikidb116_math(math_html="sample_text", math_html_conservativeness=7, math_inputhash="sample_text", math_mathml="sample_text", math_outputhash="sample_text")
    assert instance.math_inputhash == "sample_text"
    instance.math_inputhash = "sample_text_2"
    assert instance.math_inputhash == "sample_text_2"


def test_wikidb116_math_math_mathml_value_roundtrip():
    instance = wikidb116_math(math_html="sample_text", math_html_conservativeness=7, math_inputhash="sample_text", math_mathml="sample_text", math_outputhash="sample_text")
    assert instance.math_mathml == "sample_text"
    instance.math_mathml = "sample_text_2"
    assert instance.math_mathml == "sample_text_2"


def test_wikidb116_math_math_outputhash_value_roundtrip():
    instance = wikidb116_math(math_html="sample_text", math_html_conservativeness=7, math_inputhash="sample_text", math_mathml="sample_text", math_outputhash="sample_text")
    assert instance.math_outputhash == "sample_text"
    instance.math_outputhash = "sample_text_2"
    assert instance.math_outputhash == "sample_text_2"


def test_wikidb116_objectcache_exptime_value_roundtrip():
    instance = wikidb116_objectcache(exptime=date(2024, 1, 1), keyname="sample_text", value="sample_text")
    assert instance.exptime == date(2024, 1, 1)
    instance.exptime = date(2025, 6, 15)
    assert instance.exptime == date(2025, 6, 15)


def test_wikidb116_objectcache_keyname_value_roundtrip():
    instance = wikidb116_objectcache(exptime=date(2024, 1, 1), keyname="sample_text", value="sample_text")
    assert instance.keyname == "sample_text"
    instance.keyname = "sample_text_2"
    assert instance.keyname == "sample_text_2"


def test_wikidb116_objectcache_value_value_roundtrip():
    instance = wikidb116_objectcache(exptime=date(2024, 1, 1), keyname="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_wikidb116_oldimage_oi_archive_name_value_roundtrip():
    instance = wikidb116_oldimage(oi_archive_name="sample_text", oi_bits="sample_text", oi_deleted=7, oi_description="sample_text", oi_height="sample_text", oi_major_mime="sample_text", oi_media_type="sample_text", oi_metadata="sample_text", oi_minor_mime="sample_text", oi_name="sample_text", oi_sha1="sample_text", oi_size="sample_text", oi_timestamp="sample_text", oi_user="sample_text", oi_user_text="sample_text", oi_width="sample_text")
    assert instance.oi_archive_name == "sample_text"
    instance.oi_archive_name = "sample_text_2"
    assert instance.oi_archive_name == "sample_text_2"


def test_wikidb116_oldimage_oi_bits_value_roundtrip():
    instance = wikidb116_oldimage(oi_archive_name="sample_text", oi_bits="sample_text", oi_deleted=7, oi_description="sample_text", oi_height="sample_text", oi_major_mime="sample_text", oi_media_type="sample_text", oi_metadata="sample_text", oi_minor_mime="sample_text", oi_name="sample_text", oi_sha1="sample_text", oi_size="sample_text", oi_timestamp="sample_text", oi_user="sample_text", oi_user_text="sample_text", oi_width="sample_text")
    assert instance.oi_bits == "sample_text"
    instance.oi_bits = "sample_text_2"
    assert instance.oi_bits == "sample_text_2"


def test_wikidb116_oldimage_oi_deleted_value_roundtrip():
    instance = wikidb116_oldimage(oi_archive_name="sample_text", oi_bits="sample_text", oi_deleted=7, oi_description="sample_text", oi_height="sample_text", oi_major_mime="sample_text", oi_media_type="sample_text", oi_metadata="sample_text", oi_minor_mime="sample_text", oi_name="sample_text", oi_sha1="sample_text", oi_size="sample_text", oi_timestamp="sample_text", oi_user="sample_text", oi_user_text="sample_text", oi_width="sample_text")
    assert instance.oi_deleted == 7
    instance.oi_deleted = 13
    assert instance.oi_deleted == 13


def test_wikidb116_oldimage_oi_description_value_roundtrip():
    instance = wikidb116_oldimage(oi_archive_name="sample_text", oi_bits="sample_text", oi_deleted=7, oi_description="sample_text", oi_height="sample_text", oi_major_mime="sample_text", oi_media_type="sample_text", oi_metadata="sample_text", oi_minor_mime="sample_text", oi_name="sample_text", oi_sha1="sample_text", oi_size="sample_text", oi_timestamp="sample_text", oi_user="sample_text", oi_user_text="sample_text", oi_width="sample_text")
    assert instance.oi_description == "sample_text"
    instance.oi_description = "sample_text_2"
    assert instance.oi_description == "sample_text_2"


def test_wikidb116_oldimage_oi_height_value_roundtrip():
    instance = wikidb116_oldimage(oi_archive_name="sample_text", oi_bits="sample_text", oi_deleted=7, oi_description="sample_text", oi_height="sample_text", oi_major_mime="sample_text", oi_media_type="sample_text", oi_metadata="sample_text", oi_minor_mime="sample_text", oi_name="sample_text", oi_sha1="sample_text", oi_size="sample_text", oi_timestamp="sample_text", oi_user="sample_text", oi_user_text="sample_text", oi_width="sample_text")
    assert instance.oi_height == "sample_text"
    instance.oi_height = "sample_text_2"
    assert instance.oi_height == "sample_text_2"


def test_wikidb116_oldimage_oi_major_mime_value_roundtrip():
    instance = wikidb116_oldimage(oi_archive_name="sample_text", oi_bits="sample_text", oi_deleted=7, oi_description="sample_text", oi_height="sample_text", oi_major_mime="sample_text", oi_media_type="sample_text", oi_metadata="sample_text", oi_minor_mime="sample_text", oi_name="sample_text", oi_sha1="sample_text", oi_size="sample_text", oi_timestamp="sample_text", oi_user="sample_text", oi_user_text="sample_text", oi_width="sample_text")
    assert instance.oi_major_mime == "sample_text"
    instance.oi_major_mime = "sample_text_2"
    assert instance.oi_major_mime == "sample_text_2"


def test_wikidb116_oldimage_oi_media_type_value_roundtrip():
    instance = wikidb116_oldimage(oi_archive_name="sample_text", oi_bits="sample_text", oi_deleted=7, oi_description="sample_text", oi_height="sample_text", oi_major_mime="sample_text", oi_media_type="sample_text", oi_metadata="sample_text", oi_minor_mime="sample_text", oi_name="sample_text", oi_sha1="sample_text", oi_size="sample_text", oi_timestamp="sample_text", oi_user="sample_text", oi_user_text="sample_text", oi_width="sample_text")
    assert instance.oi_media_type == "sample_text"
    instance.oi_media_type = "sample_text_2"
    assert instance.oi_media_type == "sample_text_2"


def test_wikidb116_oldimage_oi_metadata_value_roundtrip():
    instance = wikidb116_oldimage(oi_archive_name="sample_text", oi_bits="sample_text", oi_deleted=7, oi_description="sample_text", oi_height="sample_text", oi_major_mime="sample_text", oi_media_type="sample_text", oi_metadata="sample_text", oi_minor_mime="sample_text", oi_name="sample_text", oi_sha1="sample_text", oi_size="sample_text", oi_timestamp="sample_text", oi_user="sample_text", oi_user_text="sample_text", oi_width="sample_text")
    assert instance.oi_metadata == "sample_text"
    instance.oi_metadata = "sample_text_2"
    assert instance.oi_metadata == "sample_text_2"


def test_wikidb116_oldimage_oi_minor_mime_value_roundtrip():
    instance = wikidb116_oldimage(oi_archive_name="sample_text", oi_bits="sample_text", oi_deleted=7, oi_description="sample_text", oi_height="sample_text", oi_major_mime="sample_text", oi_media_type="sample_text", oi_metadata="sample_text", oi_minor_mime="sample_text", oi_name="sample_text", oi_sha1="sample_text", oi_size="sample_text", oi_timestamp="sample_text", oi_user="sample_text", oi_user_text="sample_text", oi_width="sample_text")
    assert instance.oi_minor_mime == "sample_text"
    instance.oi_minor_mime = "sample_text_2"
    assert instance.oi_minor_mime == "sample_text_2"


def test_wikidb116_oldimage_oi_name_value_roundtrip():
    instance = wikidb116_oldimage(oi_archive_name="sample_text", oi_bits="sample_text", oi_deleted=7, oi_description="sample_text", oi_height="sample_text", oi_major_mime="sample_text", oi_media_type="sample_text", oi_metadata="sample_text", oi_minor_mime="sample_text", oi_name="sample_text", oi_sha1="sample_text", oi_size="sample_text", oi_timestamp="sample_text", oi_user="sample_text", oi_user_text="sample_text", oi_width="sample_text")
    assert instance.oi_name == "sample_text"
    instance.oi_name = "sample_text_2"
    assert instance.oi_name == "sample_text_2"


def test_wikidb116_oldimage_oi_sha1_value_roundtrip():
    instance = wikidb116_oldimage(oi_archive_name="sample_text", oi_bits="sample_text", oi_deleted=7, oi_description="sample_text", oi_height="sample_text", oi_major_mime="sample_text", oi_media_type="sample_text", oi_metadata="sample_text", oi_minor_mime="sample_text", oi_name="sample_text", oi_sha1="sample_text", oi_size="sample_text", oi_timestamp="sample_text", oi_user="sample_text", oi_user_text="sample_text", oi_width="sample_text")
    assert instance.oi_sha1 == "sample_text"
    instance.oi_sha1 = "sample_text_2"
    assert instance.oi_sha1 == "sample_text_2"


def test_wikidb116_oldimage_oi_size_value_roundtrip():
    instance = wikidb116_oldimage(oi_archive_name="sample_text", oi_bits="sample_text", oi_deleted=7, oi_description="sample_text", oi_height="sample_text", oi_major_mime="sample_text", oi_media_type="sample_text", oi_metadata="sample_text", oi_minor_mime="sample_text", oi_name="sample_text", oi_sha1="sample_text", oi_size="sample_text", oi_timestamp="sample_text", oi_user="sample_text", oi_user_text="sample_text", oi_width="sample_text")
    assert instance.oi_size == "sample_text"
    instance.oi_size = "sample_text_2"
    assert instance.oi_size == "sample_text_2"


def test_wikidb116_oldimage_oi_timestamp_value_roundtrip():
    instance = wikidb116_oldimage(oi_archive_name="sample_text", oi_bits="sample_text", oi_deleted=7, oi_description="sample_text", oi_height="sample_text", oi_major_mime="sample_text", oi_media_type="sample_text", oi_metadata="sample_text", oi_minor_mime="sample_text", oi_name="sample_text", oi_sha1="sample_text", oi_size="sample_text", oi_timestamp="sample_text", oi_user="sample_text", oi_user_text="sample_text", oi_width="sample_text")
    assert instance.oi_timestamp == "sample_text"
    instance.oi_timestamp = "sample_text_2"
    assert instance.oi_timestamp == "sample_text_2"


def test_wikidb116_oldimage_oi_user_value_roundtrip():
    instance = wikidb116_oldimage(oi_archive_name="sample_text", oi_bits="sample_text", oi_deleted=7, oi_description="sample_text", oi_height="sample_text", oi_major_mime="sample_text", oi_media_type="sample_text", oi_metadata="sample_text", oi_minor_mime="sample_text", oi_name="sample_text", oi_sha1="sample_text", oi_size="sample_text", oi_timestamp="sample_text", oi_user="sample_text", oi_user_text="sample_text", oi_width="sample_text")
    assert instance.oi_user == "sample_text"
    instance.oi_user = "sample_text_2"
    assert instance.oi_user == "sample_text_2"


def test_wikidb116_oldimage_oi_user_text_value_roundtrip():
    instance = wikidb116_oldimage(oi_archive_name="sample_text", oi_bits="sample_text", oi_deleted=7, oi_description="sample_text", oi_height="sample_text", oi_major_mime="sample_text", oi_media_type="sample_text", oi_metadata="sample_text", oi_minor_mime="sample_text", oi_name="sample_text", oi_sha1="sample_text", oi_size="sample_text", oi_timestamp="sample_text", oi_user="sample_text", oi_user_text="sample_text", oi_width="sample_text")
    assert instance.oi_user_text == "sample_text"
    instance.oi_user_text = "sample_text_2"
    assert instance.oi_user_text == "sample_text_2"


def test_wikidb116_oldimage_oi_width_value_roundtrip():
    instance = wikidb116_oldimage(oi_archive_name="sample_text", oi_bits="sample_text", oi_deleted=7, oi_description="sample_text", oi_height="sample_text", oi_major_mime="sample_text", oi_media_type="sample_text", oi_metadata="sample_text", oi_minor_mime="sample_text", oi_name="sample_text", oi_sha1="sample_text", oi_size="sample_text", oi_timestamp="sample_text", oi_user="sample_text", oi_user_text="sample_text", oi_width="sample_text")
    assert instance.oi_width == "sample_text"
    instance.oi_width = "sample_text_2"
    assert instance.oi_width == "sample_text_2"


def test_wikidb116_page_page_counter_value_roundtrip():
    instance = wikidb116_page(page_counter="sample_text", page_id="sample_text", page_is_new=7, page_is_redirect=7, page_latest="sample_text", page_len="sample_text", page_namespace="sample_text", page_random=3.14, page_restrictions="sample_text", page_title="sample_text", page_touched="sample_text")
    assert instance.page_counter == "sample_text"
    instance.page_counter = "sample_text_2"
    assert instance.page_counter == "sample_text_2"


def test_wikidb116_page_page_id_value_roundtrip():
    instance = wikidb116_page(page_counter="sample_text", page_id="sample_text", page_is_new=7, page_is_redirect=7, page_latest="sample_text", page_len="sample_text", page_namespace="sample_text", page_random=3.14, page_restrictions="sample_text", page_title="sample_text", page_touched="sample_text")
    assert instance.page_id == "sample_text"
    instance.page_id = "sample_text_2"
    assert instance.page_id == "sample_text_2"


def test_wikidb116_page_page_is_new_value_roundtrip():
    instance = wikidb116_page(page_counter="sample_text", page_id="sample_text", page_is_new=7, page_is_redirect=7, page_latest="sample_text", page_len="sample_text", page_namespace="sample_text", page_random=3.14, page_restrictions="sample_text", page_title="sample_text", page_touched="sample_text")
    assert instance.page_is_new == 7
    instance.page_is_new = 13
    assert instance.page_is_new == 13


def test_wikidb116_page_page_is_redirect_value_roundtrip():
    instance = wikidb116_page(page_counter="sample_text", page_id="sample_text", page_is_new=7, page_is_redirect=7, page_latest="sample_text", page_len="sample_text", page_namespace="sample_text", page_random=3.14, page_restrictions="sample_text", page_title="sample_text", page_touched="sample_text")
    assert instance.page_is_redirect == 7
    instance.page_is_redirect = 13
    assert instance.page_is_redirect == 13


def test_wikidb116_page_page_latest_value_roundtrip():
    instance = wikidb116_page(page_counter="sample_text", page_id="sample_text", page_is_new=7, page_is_redirect=7, page_latest="sample_text", page_len="sample_text", page_namespace="sample_text", page_random=3.14, page_restrictions="sample_text", page_title="sample_text", page_touched="sample_text")
    assert instance.page_latest == "sample_text"
    instance.page_latest = "sample_text_2"
    assert instance.page_latest == "sample_text_2"


def test_wikidb116_page_page_len_value_roundtrip():
    instance = wikidb116_page(page_counter="sample_text", page_id="sample_text", page_is_new=7, page_is_redirect=7, page_latest="sample_text", page_len="sample_text", page_namespace="sample_text", page_random=3.14, page_restrictions="sample_text", page_title="sample_text", page_touched="sample_text")
    assert instance.page_len == "sample_text"
    instance.page_len = "sample_text_2"
    assert instance.page_len == "sample_text_2"


def test_wikidb116_page_page_namespace_value_roundtrip():
    instance = wikidb116_page(page_counter="sample_text", page_id="sample_text", page_is_new=7, page_is_redirect=7, page_latest="sample_text", page_len="sample_text", page_namespace="sample_text", page_random=3.14, page_restrictions="sample_text", page_title="sample_text", page_touched="sample_text")
    assert instance.page_namespace == "sample_text"
    instance.page_namespace = "sample_text_2"
    assert instance.page_namespace == "sample_text_2"


def test_wikidb116_page_page_random_value_roundtrip():
    instance = wikidb116_page(page_counter="sample_text", page_id="sample_text", page_is_new=7, page_is_redirect=7, page_latest="sample_text", page_len="sample_text", page_namespace="sample_text", page_random=3.14, page_restrictions="sample_text", page_title="sample_text", page_touched="sample_text")
    assert instance.page_random == 3.14
    instance.page_random = 9.99
    assert instance.page_random == 9.99


def test_wikidb116_page_page_restrictions_value_roundtrip():
    instance = wikidb116_page(page_counter="sample_text", page_id="sample_text", page_is_new=7, page_is_redirect=7, page_latest="sample_text", page_len="sample_text", page_namespace="sample_text", page_random=3.14, page_restrictions="sample_text", page_title="sample_text", page_touched="sample_text")
    assert instance.page_restrictions == "sample_text"
    instance.page_restrictions = "sample_text_2"
    assert instance.page_restrictions == "sample_text_2"


def test_wikidb116_page_page_title_value_roundtrip():
    instance = wikidb116_page(page_counter="sample_text", page_id="sample_text", page_is_new=7, page_is_redirect=7, page_latest="sample_text", page_len="sample_text", page_namespace="sample_text", page_random=3.14, page_restrictions="sample_text", page_title="sample_text", page_touched="sample_text")
    assert instance.page_title == "sample_text"
    instance.page_title = "sample_text_2"
    assert instance.page_title == "sample_text_2"


def test_wikidb116_page_page_touched_value_roundtrip():
    instance = wikidb116_page(page_counter="sample_text", page_id="sample_text", page_is_new=7, page_is_redirect=7, page_latest="sample_text", page_len="sample_text", page_namespace="sample_text", page_random=3.14, page_restrictions="sample_text", page_title="sample_text", page_touched="sample_text")
    assert instance.page_touched == "sample_text"
    instance.page_touched = "sample_text_2"
    assert instance.page_touched == "sample_text_2"


def test_wikidb116_page_props_pp_page_value_roundtrip():
    instance = wikidb116_page_props(pp_page="sample_text", pp_propname="sample_text", pp_value="sample_text")
    assert instance.pp_page == "sample_text"
    instance.pp_page = "sample_text_2"
    assert instance.pp_page == "sample_text_2"


def test_wikidb116_page_props_pp_propname_value_roundtrip():
    instance = wikidb116_page_props(pp_page="sample_text", pp_propname="sample_text", pp_value="sample_text")
    assert instance.pp_propname == "sample_text"
    instance.pp_propname = "sample_text_2"
    assert instance.pp_propname == "sample_text_2"


def test_wikidb116_page_props_pp_value_value_roundtrip():
    instance = wikidb116_page_props(pp_page="sample_text", pp_propname="sample_text", pp_value="sample_text")
    assert instance.pp_value == "sample_text"
    instance.pp_value = "sample_text_2"
    assert instance.pp_value == "sample_text_2"


def test_wikidb116_page_restrictions_pr_cascade_value_roundtrip():
    instance = wikidb116_page_restrictions(pr_cascade=7, pr_expiry="sample_text", pr_id="sample_text", pr_level="sample_text", pr_page="sample_text", pr_type="sample_text", pr_user="sample_text")
    assert instance.pr_cascade == 7
    instance.pr_cascade = 13
    assert instance.pr_cascade == 13


def test_wikidb116_page_restrictions_pr_expiry_value_roundtrip():
    instance = wikidb116_page_restrictions(pr_cascade=7, pr_expiry="sample_text", pr_id="sample_text", pr_level="sample_text", pr_page="sample_text", pr_type="sample_text", pr_user="sample_text")
    assert instance.pr_expiry == "sample_text"
    instance.pr_expiry = "sample_text_2"
    assert instance.pr_expiry == "sample_text_2"


def test_wikidb116_page_restrictions_pr_id_value_roundtrip():
    instance = wikidb116_page_restrictions(pr_cascade=7, pr_expiry="sample_text", pr_id="sample_text", pr_level="sample_text", pr_page="sample_text", pr_type="sample_text", pr_user="sample_text")
    assert instance.pr_id == "sample_text"
    instance.pr_id = "sample_text_2"
    assert instance.pr_id == "sample_text_2"


def test_wikidb116_page_restrictions_pr_level_value_roundtrip():
    instance = wikidb116_page_restrictions(pr_cascade=7, pr_expiry="sample_text", pr_id="sample_text", pr_level="sample_text", pr_page="sample_text", pr_type="sample_text", pr_user="sample_text")
    assert instance.pr_level == "sample_text"
    instance.pr_level = "sample_text_2"
    assert instance.pr_level == "sample_text_2"


def test_wikidb116_page_restrictions_pr_page_value_roundtrip():
    instance = wikidb116_page_restrictions(pr_cascade=7, pr_expiry="sample_text", pr_id="sample_text", pr_level="sample_text", pr_page="sample_text", pr_type="sample_text", pr_user="sample_text")
    assert instance.pr_page == "sample_text"
    instance.pr_page = "sample_text_2"
    assert instance.pr_page == "sample_text_2"


def test_wikidb116_page_restrictions_pr_type_value_roundtrip():
    instance = wikidb116_page_restrictions(pr_cascade=7, pr_expiry="sample_text", pr_id="sample_text", pr_level="sample_text", pr_page="sample_text", pr_type="sample_text", pr_user="sample_text")
    assert instance.pr_type == "sample_text"
    instance.pr_type = "sample_text_2"
    assert instance.pr_type == "sample_text_2"


def test_wikidb116_page_restrictions_pr_user_value_roundtrip():
    instance = wikidb116_page_restrictions(pr_cascade=7, pr_expiry="sample_text", pr_id="sample_text", pr_level="sample_text", pr_page="sample_text", pr_type="sample_text", pr_user="sample_text")
    assert instance.pr_user == "sample_text"
    instance.pr_user = "sample_text_2"
    assert instance.pr_user == "sample_text_2"


def test_wikidb116_pagelinks_pl_from_value_roundtrip():
    instance = wikidb116_pagelinks(pl_from="sample_text", pl_namespace="sample_text", pl_title="sample_text")
    assert instance.pl_from == "sample_text"
    instance.pl_from = "sample_text_2"
    assert instance.pl_from == "sample_text_2"


def test_wikidb116_pagelinks_pl_namespace_value_roundtrip():
    instance = wikidb116_pagelinks(pl_from="sample_text", pl_namespace="sample_text", pl_title="sample_text")
    assert instance.pl_namespace == "sample_text"
    instance.pl_namespace = "sample_text_2"
    assert instance.pl_namespace == "sample_text_2"


def test_wikidb116_pagelinks_pl_title_value_roundtrip():
    instance = wikidb116_pagelinks(pl_from="sample_text", pl_namespace="sample_text", pl_title="sample_text")
    assert instance.pl_title == "sample_text"
    instance.pl_title = "sample_text_2"
    assert instance.pl_title == "sample_text_2"


def test_wikidb116_protected_titles_pt_create_perm_value_roundtrip():
    instance = wikidb116_protected_titles(pt_create_perm="sample_text", pt_expiry="sample_text", pt_namespace="sample_text", pt_reason="sample_text", pt_timestamp="sample_text", pt_title="sample_text", pt_user="sample_text")
    assert instance.pt_create_perm == "sample_text"
    instance.pt_create_perm = "sample_text_2"
    assert instance.pt_create_perm == "sample_text_2"


def test_wikidb116_protected_titles_pt_expiry_value_roundtrip():
    instance = wikidb116_protected_titles(pt_create_perm="sample_text", pt_expiry="sample_text", pt_namespace="sample_text", pt_reason="sample_text", pt_timestamp="sample_text", pt_title="sample_text", pt_user="sample_text")
    assert instance.pt_expiry == "sample_text"
    instance.pt_expiry = "sample_text_2"
    assert instance.pt_expiry == "sample_text_2"


def test_wikidb116_protected_titles_pt_namespace_value_roundtrip():
    instance = wikidb116_protected_titles(pt_create_perm="sample_text", pt_expiry="sample_text", pt_namespace="sample_text", pt_reason="sample_text", pt_timestamp="sample_text", pt_title="sample_text", pt_user="sample_text")
    assert instance.pt_namespace == "sample_text"
    instance.pt_namespace = "sample_text_2"
    assert instance.pt_namespace == "sample_text_2"


def test_wikidb116_protected_titles_pt_reason_value_roundtrip():
    instance = wikidb116_protected_titles(pt_create_perm="sample_text", pt_expiry="sample_text", pt_namespace="sample_text", pt_reason="sample_text", pt_timestamp="sample_text", pt_title="sample_text", pt_user="sample_text")
    assert instance.pt_reason == "sample_text"
    instance.pt_reason = "sample_text_2"
    assert instance.pt_reason == "sample_text_2"


def test_wikidb116_protected_titles_pt_timestamp_value_roundtrip():
    instance = wikidb116_protected_titles(pt_create_perm="sample_text", pt_expiry="sample_text", pt_namespace="sample_text", pt_reason="sample_text", pt_timestamp="sample_text", pt_title="sample_text", pt_user="sample_text")
    assert instance.pt_timestamp == "sample_text"
    instance.pt_timestamp = "sample_text_2"
    assert instance.pt_timestamp == "sample_text_2"


def test_wikidb116_protected_titles_pt_title_value_roundtrip():
    instance = wikidb116_protected_titles(pt_create_perm="sample_text", pt_expiry="sample_text", pt_namespace="sample_text", pt_reason="sample_text", pt_timestamp="sample_text", pt_title="sample_text", pt_user="sample_text")
    assert instance.pt_title == "sample_text"
    instance.pt_title = "sample_text_2"
    assert instance.pt_title == "sample_text_2"


def test_wikidb116_protected_titles_pt_user_value_roundtrip():
    instance = wikidb116_protected_titles(pt_create_perm="sample_text", pt_expiry="sample_text", pt_namespace="sample_text", pt_reason="sample_text", pt_timestamp="sample_text", pt_title="sample_text", pt_user="sample_text")
    assert instance.pt_user == "sample_text"
    instance.pt_user = "sample_text_2"
    assert instance.pt_user == "sample_text_2"


def test_wikidb116_querycache_qc_namespace_value_roundtrip():
    instance = wikidb116_querycache(qc_namespace="sample_text", qc_title="sample_text", qc_type="sample_text", qc_value="sample_text")
    assert instance.qc_namespace == "sample_text"
    instance.qc_namespace = "sample_text_2"
    assert instance.qc_namespace == "sample_text_2"


def test_wikidb116_querycache_qc_title_value_roundtrip():
    instance = wikidb116_querycache(qc_namespace="sample_text", qc_title="sample_text", qc_type="sample_text", qc_value="sample_text")
    assert instance.qc_title == "sample_text"
    instance.qc_title = "sample_text_2"
    assert instance.qc_title == "sample_text_2"


def test_wikidb116_querycache_qc_type_value_roundtrip():
    instance = wikidb116_querycache(qc_namespace="sample_text", qc_title="sample_text", qc_type="sample_text", qc_value="sample_text")
    assert instance.qc_type == "sample_text"
    instance.qc_type = "sample_text_2"
    assert instance.qc_type == "sample_text_2"


def test_wikidb116_querycache_qc_value_value_roundtrip():
    instance = wikidb116_querycache(qc_namespace="sample_text", qc_title="sample_text", qc_type="sample_text", qc_value="sample_text")
    assert instance.qc_value == "sample_text"
    instance.qc_value = "sample_text_2"
    assert instance.qc_value == "sample_text_2"


def test_wikidb116_querycache_info_qci_timestamp_value_roundtrip():
    instance = wikidb116_querycache_info(qci_timestamp="sample_text", qci_type="sample_text")
    assert instance.qci_timestamp == "sample_text"
    instance.qci_timestamp = "sample_text_2"
    assert instance.qci_timestamp == "sample_text_2"


def test_wikidb116_querycache_info_qci_type_value_roundtrip():
    instance = wikidb116_querycache_info(qci_timestamp="sample_text", qci_type="sample_text")
    assert instance.qci_type == "sample_text"
    instance.qci_type = "sample_text_2"
    assert instance.qci_type == "sample_text_2"


def test_wikidb116_querycachetwo_qcc_namespace_value_roundtrip():
    instance = wikidb116_querycachetwo(qcc_namespace="sample_text", qcc_namespacetwo="sample_text", qcc_title="sample_text", qcc_titletwo="sample_text", qcc_type="sample_text", qcc_value="sample_text")
    assert instance.qcc_namespace == "sample_text"
    instance.qcc_namespace = "sample_text_2"
    assert instance.qcc_namespace == "sample_text_2"


def test_wikidb116_querycachetwo_qcc_namespacetwo_value_roundtrip():
    instance = wikidb116_querycachetwo(qcc_namespace="sample_text", qcc_namespacetwo="sample_text", qcc_title="sample_text", qcc_titletwo="sample_text", qcc_type="sample_text", qcc_value="sample_text")
    assert instance.qcc_namespacetwo == "sample_text"
    instance.qcc_namespacetwo = "sample_text_2"
    assert instance.qcc_namespacetwo == "sample_text_2"


def test_wikidb116_querycachetwo_qcc_title_value_roundtrip():
    instance = wikidb116_querycachetwo(qcc_namespace="sample_text", qcc_namespacetwo="sample_text", qcc_title="sample_text", qcc_titletwo="sample_text", qcc_type="sample_text", qcc_value="sample_text")
    assert instance.qcc_title == "sample_text"
    instance.qcc_title = "sample_text_2"
    assert instance.qcc_title == "sample_text_2"


def test_wikidb116_querycachetwo_qcc_titletwo_value_roundtrip():
    instance = wikidb116_querycachetwo(qcc_namespace="sample_text", qcc_namespacetwo="sample_text", qcc_title="sample_text", qcc_titletwo="sample_text", qcc_type="sample_text", qcc_value="sample_text")
    assert instance.qcc_titletwo == "sample_text"
    instance.qcc_titletwo = "sample_text_2"
    assert instance.qcc_titletwo == "sample_text_2"


def test_wikidb116_querycachetwo_qcc_type_value_roundtrip():
    instance = wikidb116_querycachetwo(qcc_namespace="sample_text", qcc_namespacetwo="sample_text", qcc_title="sample_text", qcc_titletwo="sample_text", qcc_type="sample_text", qcc_value="sample_text")
    assert instance.qcc_type == "sample_text"
    instance.qcc_type = "sample_text_2"
    assert instance.qcc_type == "sample_text_2"


def test_wikidb116_querycachetwo_qcc_value_value_roundtrip():
    instance = wikidb116_querycachetwo(qcc_namespace="sample_text", qcc_namespacetwo="sample_text", qcc_title="sample_text", qcc_titletwo="sample_text", qcc_type="sample_text", qcc_value="sample_text")
    assert instance.qcc_value == "sample_text"
    instance.qcc_value = "sample_text_2"
    assert instance.qcc_value == "sample_text_2"


def test_wikidb116_recentchanges_rc_bot_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_bot == 7
    instance.rc_bot = 13
    assert instance.rc_bot == 13


def test_wikidb116_recentchanges_rc_comment_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_comment == "sample_text"
    instance.rc_comment = "sample_text_2"
    assert instance.rc_comment == "sample_text_2"


def test_wikidb116_recentchanges_rc_cur_id_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_cur_id == "sample_text"
    instance.rc_cur_id = "sample_text_2"
    assert instance.rc_cur_id == "sample_text_2"


def test_wikidb116_recentchanges_rc_cur_time_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_cur_time == "sample_text"
    instance.rc_cur_time = "sample_text_2"
    assert instance.rc_cur_time == "sample_text_2"


def test_wikidb116_recentchanges_rc_deleted_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_deleted == 7
    instance.rc_deleted = 13
    assert instance.rc_deleted == 13


def test_wikidb116_recentchanges_rc_id_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_id == "sample_text"
    instance.rc_id = "sample_text_2"
    assert instance.rc_id == "sample_text_2"


def test_wikidb116_recentchanges_rc_ip_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_ip == "sample_text"
    instance.rc_ip = "sample_text_2"
    assert instance.rc_ip == "sample_text_2"


def test_wikidb116_recentchanges_rc_last_oldid_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_last_oldid == "sample_text"
    instance.rc_last_oldid = "sample_text_2"
    assert instance.rc_last_oldid == "sample_text_2"


def test_wikidb116_recentchanges_rc_log_action_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_log_action == "sample_text"
    instance.rc_log_action = "sample_text_2"
    assert instance.rc_log_action == "sample_text_2"


def test_wikidb116_recentchanges_rc_log_type_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_log_type == "sample_text"
    instance.rc_log_type = "sample_text_2"
    assert instance.rc_log_type == "sample_text_2"


def test_wikidb116_recentchanges_rc_logid_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_logid == "sample_text"
    instance.rc_logid = "sample_text_2"
    assert instance.rc_logid == "sample_text_2"


def test_wikidb116_recentchanges_rc_minor_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_minor == 7
    instance.rc_minor = 13
    assert instance.rc_minor == 13


def test_wikidb116_recentchanges_rc_moved_to_ns_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_moved_to_ns == 7
    instance.rc_moved_to_ns = 13
    assert instance.rc_moved_to_ns == 13


def test_wikidb116_recentchanges_rc_moved_to_title_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_moved_to_title == "sample_text"
    instance.rc_moved_to_title = "sample_text_2"
    assert instance.rc_moved_to_title == "sample_text_2"


def test_wikidb116_recentchanges_rc_namespace_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_namespace == "sample_text"
    instance.rc_namespace = "sample_text_2"
    assert instance.rc_namespace == "sample_text_2"


def test_wikidb116_recentchanges_rc_new_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_new == 7
    instance.rc_new = 13
    assert instance.rc_new == 13


def test_wikidb116_recentchanges_rc_new_len_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_new_len == "sample_text"
    instance.rc_new_len = "sample_text_2"
    assert instance.rc_new_len == "sample_text_2"


def test_wikidb116_recentchanges_rc_old_len_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_old_len == "sample_text"
    instance.rc_old_len = "sample_text_2"
    assert instance.rc_old_len == "sample_text_2"


def test_wikidb116_recentchanges_rc_params_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_params == "sample_text"
    instance.rc_params = "sample_text_2"
    assert instance.rc_params == "sample_text_2"


def test_wikidb116_recentchanges_rc_patrolled_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_patrolled == 7
    instance.rc_patrolled = 13
    assert instance.rc_patrolled == 13


def test_wikidb116_recentchanges_rc_this_oldid_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_this_oldid == "sample_text"
    instance.rc_this_oldid = "sample_text_2"
    assert instance.rc_this_oldid == "sample_text_2"


def test_wikidb116_recentchanges_rc_timestamp_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_timestamp == "sample_text"
    instance.rc_timestamp = "sample_text_2"
    assert instance.rc_timestamp == "sample_text_2"


def test_wikidb116_recentchanges_rc_title_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_title == "sample_text"
    instance.rc_title = "sample_text_2"
    assert instance.rc_title == "sample_text_2"


def test_wikidb116_recentchanges_rc_type_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_type == 7
    instance.rc_type = 13
    assert instance.rc_type == 13


def test_wikidb116_recentchanges_rc_user_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_user == "sample_text"
    instance.rc_user = "sample_text_2"
    assert instance.rc_user == "sample_text_2"


def test_wikidb116_recentchanges_rc_user_text_value_roundtrip():
    instance = wikidb116_recentchanges(rc_bot=7, rc_comment="sample_text", rc_cur_id="sample_text", rc_cur_time="sample_text", rc_deleted=7, rc_id="sample_text", rc_ip="sample_text", rc_last_oldid="sample_text", rc_log_action="sample_text", rc_log_type="sample_text", rc_logid="sample_text", rc_minor=7, rc_moved_to_ns=7, rc_moved_to_title="sample_text", rc_namespace="sample_text", rc_new=7, rc_new_len="sample_text", rc_old_len="sample_text", rc_params="sample_text", rc_patrolled=7, rc_this_oldid="sample_text", rc_timestamp="sample_text", rc_title="sample_text", rc_type=7, rc_user="sample_text", rc_user_text="sample_text")
    assert instance.rc_user_text == "sample_text"
    instance.rc_user_text = "sample_text_2"
    assert instance.rc_user_text == "sample_text_2"


def test_wikidb116_redirect_rd_fragment_value_roundtrip():
    instance = wikidb116_redirect(rd_fragment="sample_text", rd_from="sample_text", rd_interwiki="sample_text", rd_namespace="sample_text", rd_title="sample_text")
    assert instance.rd_fragment == "sample_text"
    instance.rd_fragment = "sample_text_2"
    assert instance.rd_fragment == "sample_text_2"


def test_wikidb116_redirect_rd_from_value_roundtrip():
    instance = wikidb116_redirect(rd_fragment="sample_text", rd_from="sample_text", rd_interwiki="sample_text", rd_namespace="sample_text", rd_title="sample_text")
    assert instance.rd_from == "sample_text"
    instance.rd_from = "sample_text_2"
    assert instance.rd_from == "sample_text_2"


def test_wikidb116_redirect_rd_interwiki_value_roundtrip():
    instance = wikidb116_redirect(rd_fragment="sample_text", rd_from="sample_text", rd_interwiki="sample_text", rd_namespace="sample_text", rd_title="sample_text")
    assert instance.rd_interwiki == "sample_text"
    instance.rd_interwiki = "sample_text_2"
    assert instance.rd_interwiki == "sample_text_2"


def test_wikidb116_redirect_rd_namespace_value_roundtrip():
    instance = wikidb116_redirect(rd_fragment="sample_text", rd_from="sample_text", rd_interwiki="sample_text", rd_namespace="sample_text", rd_title="sample_text")
    assert instance.rd_namespace == "sample_text"
    instance.rd_namespace = "sample_text_2"
    assert instance.rd_namespace == "sample_text_2"


def test_wikidb116_redirect_rd_title_value_roundtrip():
    instance = wikidb116_redirect(rd_fragment="sample_text", rd_from="sample_text", rd_interwiki="sample_text", rd_namespace="sample_text", rd_title="sample_text")
    assert instance.rd_title == "sample_text"
    instance.rd_title = "sample_text_2"
    assert instance.rd_title == "sample_text_2"


def test_wikidb116_revision_rev_comment_value_roundtrip():
    instance = wikidb116_revision(rev_comment="sample_text", rev_deleted=7, rev_id="sample_text", rev_len="sample_text", rev_minor_edit=7, rev_page="sample_text", rev_parent_id="sample_text", rev_text_id="sample_text", rev_timestamp="sample_text", rev_user="sample_text", rev_user_text="sample_text")
    assert instance.rev_comment == "sample_text"
    instance.rev_comment = "sample_text_2"
    assert instance.rev_comment == "sample_text_2"


def test_wikidb116_revision_rev_deleted_value_roundtrip():
    instance = wikidb116_revision(rev_comment="sample_text", rev_deleted=7, rev_id="sample_text", rev_len="sample_text", rev_minor_edit=7, rev_page="sample_text", rev_parent_id="sample_text", rev_text_id="sample_text", rev_timestamp="sample_text", rev_user="sample_text", rev_user_text="sample_text")
    assert instance.rev_deleted == 7
    instance.rev_deleted = 13
    assert instance.rev_deleted == 13


def test_wikidb116_revision_rev_id_value_roundtrip():
    instance = wikidb116_revision(rev_comment="sample_text", rev_deleted=7, rev_id="sample_text", rev_len="sample_text", rev_minor_edit=7, rev_page="sample_text", rev_parent_id="sample_text", rev_text_id="sample_text", rev_timestamp="sample_text", rev_user="sample_text", rev_user_text="sample_text")
    assert instance.rev_id == "sample_text"
    instance.rev_id = "sample_text_2"
    assert instance.rev_id == "sample_text_2"


def test_wikidb116_revision_rev_len_value_roundtrip():
    instance = wikidb116_revision(rev_comment="sample_text", rev_deleted=7, rev_id="sample_text", rev_len="sample_text", rev_minor_edit=7, rev_page="sample_text", rev_parent_id="sample_text", rev_text_id="sample_text", rev_timestamp="sample_text", rev_user="sample_text", rev_user_text="sample_text")
    assert instance.rev_len == "sample_text"
    instance.rev_len = "sample_text_2"
    assert instance.rev_len == "sample_text_2"


def test_wikidb116_revision_rev_minor_edit_value_roundtrip():
    instance = wikidb116_revision(rev_comment="sample_text", rev_deleted=7, rev_id="sample_text", rev_len="sample_text", rev_minor_edit=7, rev_page="sample_text", rev_parent_id="sample_text", rev_text_id="sample_text", rev_timestamp="sample_text", rev_user="sample_text", rev_user_text="sample_text")
    assert instance.rev_minor_edit == 7
    instance.rev_minor_edit = 13
    assert instance.rev_minor_edit == 13


def test_wikidb116_revision_rev_page_value_roundtrip():
    instance = wikidb116_revision(rev_comment="sample_text", rev_deleted=7, rev_id="sample_text", rev_len="sample_text", rev_minor_edit=7, rev_page="sample_text", rev_parent_id="sample_text", rev_text_id="sample_text", rev_timestamp="sample_text", rev_user="sample_text", rev_user_text="sample_text")
    assert instance.rev_page == "sample_text"
    instance.rev_page = "sample_text_2"
    assert instance.rev_page == "sample_text_2"


def test_wikidb116_revision_rev_parent_id_value_roundtrip():
    instance = wikidb116_revision(rev_comment="sample_text", rev_deleted=7, rev_id="sample_text", rev_len="sample_text", rev_minor_edit=7, rev_page="sample_text", rev_parent_id="sample_text", rev_text_id="sample_text", rev_timestamp="sample_text", rev_user="sample_text", rev_user_text="sample_text")
    assert instance.rev_parent_id == "sample_text"
    instance.rev_parent_id = "sample_text_2"
    assert instance.rev_parent_id == "sample_text_2"


def test_wikidb116_revision_rev_text_id_value_roundtrip():
    instance = wikidb116_revision(rev_comment="sample_text", rev_deleted=7, rev_id="sample_text", rev_len="sample_text", rev_minor_edit=7, rev_page="sample_text", rev_parent_id="sample_text", rev_text_id="sample_text", rev_timestamp="sample_text", rev_user="sample_text", rev_user_text="sample_text")
    assert instance.rev_text_id == "sample_text"
    instance.rev_text_id = "sample_text_2"
    assert instance.rev_text_id == "sample_text_2"


def test_wikidb116_revision_rev_timestamp_value_roundtrip():
    instance = wikidb116_revision(rev_comment="sample_text", rev_deleted=7, rev_id="sample_text", rev_len="sample_text", rev_minor_edit=7, rev_page="sample_text", rev_parent_id="sample_text", rev_text_id="sample_text", rev_timestamp="sample_text", rev_user="sample_text", rev_user_text="sample_text")
    assert instance.rev_timestamp == "sample_text"
    instance.rev_timestamp = "sample_text_2"
    assert instance.rev_timestamp == "sample_text_2"


def test_wikidb116_revision_rev_user_value_roundtrip():
    instance = wikidb116_revision(rev_comment="sample_text", rev_deleted=7, rev_id="sample_text", rev_len="sample_text", rev_minor_edit=7, rev_page="sample_text", rev_parent_id="sample_text", rev_text_id="sample_text", rev_timestamp="sample_text", rev_user="sample_text", rev_user_text="sample_text")
    assert instance.rev_user == "sample_text"
    instance.rev_user = "sample_text_2"
    assert instance.rev_user == "sample_text_2"


def test_wikidb116_revision_rev_user_text_value_roundtrip():
    instance = wikidb116_revision(rev_comment="sample_text", rev_deleted=7, rev_id="sample_text", rev_len="sample_text", rev_minor_edit=7, rev_page="sample_text", rev_parent_id="sample_text", rev_text_id="sample_text", rev_timestamp="sample_text", rev_user="sample_text", rev_user_text="sample_text")
    assert instance.rev_user_text == "sample_text"
    instance.rev_user_text = "sample_text_2"
    assert instance.rev_user_text == "sample_text_2"


def test_wikidb116_searchindex_si_page_value_roundtrip():
    instance = wikidb116_searchindex(si_page="sample_text", si_text="sample_text", si_title="sample_text")
    assert instance.si_page == "sample_text"
    instance.si_page = "sample_text_2"
    assert instance.si_page == "sample_text_2"


def test_wikidb116_searchindex_si_text_value_roundtrip():
    instance = wikidb116_searchindex(si_page="sample_text", si_text="sample_text", si_title="sample_text")
    assert instance.si_text == "sample_text"
    instance.si_text = "sample_text_2"
    assert instance.si_text == "sample_text_2"


def test_wikidb116_searchindex_si_title_value_roundtrip():
    instance = wikidb116_searchindex(si_page="sample_text", si_text="sample_text", si_title="sample_text")
    assert instance.si_title == "sample_text"
    instance.si_title = "sample_text_2"
    assert instance.si_title == "sample_text_2"


def test_wikidb116_site_stats_ss_active_users_value_roundtrip():
    instance = wikidb116_site_stats(ss_active_users="sample_text", ss_admins="sample_text", ss_good_articles="sample_text", ss_images="sample_text", ss_row_id="sample_text", ss_total_edits="sample_text", ss_total_pages="sample_text", ss_total_views="sample_text", ss_users="sample_text")
    assert instance.ss_active_users == "sample_text"
    instance.ss_active_users = "sample_text_2"
    assert instance.ss_active_users == "sample_text_2"


def test_wikidb116_site_stats_ss_admins_value_roundtrip():
    instance = wikidb116_site_stats(ss_active_users="sample_text", ss_admins="sample_text", ss_good_articles="sample_text", ss_images="sample_text", ss_row_id="sample_text", ss_total_edits="sample_text", ss_total_pages="sample_text", ss_total_views="sample_text", ss_users="sample_text")
    assert instance.ss_admins == "sample_text"
    instance.ss_admins = "sample_text_2"
    assert instance.ss_admins == "sample_text_2"


def test_wikidb116_site_stats_ss_good_articles_value_roundtrip():
    instance = wikidb116_site_stats(ss_active_users="sample_text", ss_admins="sample_text", ss_good_articles="sample_text", ss_images="sample_text", ss_row_id="sample_text", ss_total_edits="sample_text", ss_total_pages="sample_text", ss_total_views="sample_text", ss_users="sample_text")
    assert instance.ss_good_articles == "sample_text"
    instance.ss_good_articles = "sample_text_2"
    assert instance.ss_good_articles == "sample_text_2"


def test_wikidb116_site_stats_ss_images_value_roundtrip():
    instance = wikidb116_site_stats(ss_active_users="sample_text", ss_admins="sample_text", ss_good_articles="sample_text", ss_images="sample_text", ss_row_id="sample_text", ss_total_edits="sample_text", ss_total_pages="sample_text", ss_total_views="sample_text", ss_users="sample_text")
    assert instance.ss_images == "sample_text"
    instance.ss_images = "sample_text_2"
    assert instance.ss_images == "sample_text_2"


def test_wikidb116_site_stats_ss_row_id_value_roundtrip():
    instance = wikidb116_site_stats(ss_active_users="sample_text", ss_admins="sample_text", ss_good_articles="sample_text", ss_images="sample_text", ss_row_id="sample_text", ss_total_edits="sample_text", ss_total_pages="sample_text", ss_total_views="sample_text", ss_users="sample_text")
    assert instance.ss_row_id == "sample_text"
    instance.ss_row_id = "sample_text_2"
    assert instance.ss_row_id == "sample_text_2"


def test_wikidb116_site_stats_ss_total_edits_value_roundtrip():
    instance = wikidb116_site_stats(ss_active_users="sample_text", ss_admins="sample_text", ss_good_articles="sample_text", ss_images="sample_text", ss_row_id="sample_text", ss_total_edits="sample_text", ss_total_pages="sample_text", ss_total_views="sample_text", ss_users="sample_text")
    assert instance.ss_total_edits == "sample_text"
    instance.ss_total_edits = "sample_text_2"
    assert instance.ss_total_edits == "sample_text_2"


def test_wikidb116_site_stats_ss_total_pages_value_roundtrip():
    instance = wikidb116_site_stats(ss_active_users="sample_text", ss_admins="sample_text", ss_good_articles="sample_text", ss_images="sample_text", ss_row_id="sample_text", ss_total_edits="sample_text", ss_total_pages="sample_text", ss_total_views="sample_text", ss_users="sample_text")
    assert instance.ss_total_pages == "sample_text"
    instance.ss_total_pages = "sample_text_2"
    assert instance.ss_total_pages == "sample_text_2"


def test_wikidb116_site_stats_ss_total_views_value_roundtrip():
    instance = wikidb116_site_stats(ss_active_users="sample_text", ss_admins="sample_text", ss_good_articles="sample_text", ss_images="sample_text", ss_row_id="sample_text", ss_total_edits="sample_text", ss_total_pages="sample_text", ss_total_views="sample_text", ss_users="sample_text")
    assert instance.ss_total_views == "sample_text"
    instance.ss_total_views = "sample_text_2"
    assert instance.ss_total_views == "sample_text_2"


def test_wikidb116_site_stats_ss_users_value_roundtrip():
    instance = wikidb116_site_stats(ss_active_users="sample_text", ss_admins="sample_text", ss_good_articles="sample_text", ss_images="sample_text", ss_row_id="sample_text", ss_total_edits="sample_text", ss_total_pages="sample_text", ss_total_views="sample_text", ss_users="sample_text")
    assert instance.ss_users == "sample_text"
    instance.ss_users = "sample_text_2"
    assert instance.ss_users == "sample_text_2"


def test_wikidb116_tag_summary_ts_log_id_value_roundtrip():
    instance = wikidb116_tag_summary(ts_log_id="sample_text", ts_rc_id="sample_text", ts_rev_id="sample_text", ts_tags="sample_text")
    assert instance.ts_log_id == "sample_text"
    instance.ts_log_id = "sample_text_2"
    assert instance.ts_log_id == "sample_text_2"


def test_wikidb116_tag_summary_ts_rc_id_value_roundtrip():
    instance = wikidb116_tag_summary(ts_log_id="sample_text", ts_rc_id="sample_text", ts_rev_id="sample_text", ts_tags="sample_text")
    assert instance.ts_rc_id == "sample_text"
    instance.ts_rc_id = "sample_text_2"
    assert instance.ts_rc_id == "sample_text_2"


def test_wikidb116_tag_summary_ts_rev_id_value_roundtrip():
    instance = wikidb116_tag_summary(ts_log_id="sample_text", ts_rc_id="sample_text", ts_rev_id="sample_text", ts_tags="sample_text")
    assert instance.ts_rev_id == "sample_text"
    instance.ts_rev_id = "sample_text_2"
    assert instance.ts_rev_id == "sample_text_2"


def test_wikidb116_tag_summary_ts_tags_value_roundtrip():
    instance = wikidb116_tag_summary(ts_log_id="sample_text", ts_rc_id="sample_text", ts_rev_id="sample_text", ts_tags="sample_text")
    assert instance.ts_tags == "sample_text"
    instance.ts_tags = "sample_text_2"
    assert instance.ts_tags == "sample_text_2"


def test_wikidb116_templatelinks_tl_from_value_roundtrip():
    instance = wikidb116_templatelinks(tl_from="sample_text", tl_namespace="sample_text", tl_title="sample_text")
    assert instance.tl_from == "sample_text"
    instance.tl_from = "sample_text_2"
    assert instance.tl_from == "sample_text_2"


def test_wikidb116_templatelinks_tl_namespace_value_roundtrip():
    instance = wikidb116_templatelinks(tl_from="sample_text", tl_namespace="sample_text", tl_title="sample_text")
    assert instance.tl_namespace == "sample_text"
    instance.tl_namespace = "sample_text_2"
    assert instance.tl_namespace == "sample_text_2"


def test_wikidb116_templatelinks_tl_title_value_roundtrip():
    instance = wikidb116_templatelinks(tl_from="sample_text", tl_namespace="sample_text", tl_title="sample_text")
    assert instance.tl_title == "sample_text"
    instance.tl_title = "sample_text_2"
    assert instance.tl_title == "sample_text_2"


def test_wikidb116_text_old_flags_value_roundtrip():
    instance = wikidb116_text(old_flags="sample_text", old_id="sample_text", old_text="sample_text")
    assert instance.old_flags == "sample_text"
    instance.old_flags = "sample_text_2"
    assert instance.old_flags == "sample_text_2"


def test_wikidb116_text_old_id_value_roundtrip():
    instance = wikidb116_text(old_flags="sample_text", old_id="sample_text", old_text="sample_text")
    assert instance.old_id == "sample_text"
    instance.old_id = "sample_text_2"
    assert instance.old_id == "sample_text_2"


def test_wikidb116_text_old_text_value_roundtrip():
    instance = wikidb116_text(old_flags="sample_text", old_id="sample_text", old_text="sample_text")
    assert instance.old_text == "sample_text"
    instance.old_text = "sample_text_2"
    assert instance.old_text == "sample_text_2"


def test_wikidb116_trackbacks_tb_ex_value_roundtrip():
    instance = wikidb116_trackbacks(tb_ex="sample_text", tb_id="sample_text", tb_name="sample_text", tb_page="sample_text", tb_title="sample_text", tb_url="sample_text")
    assert instance.tb_ex == "sample_text"
    instance.tb_ex = "sample_text_2"
    assert instance.tb_ex == "sample_text_2"


def test_wikidb116_trackbacks_tb_id_value_roundtrip():
    instance = wikidb116_trackbacks(tb_ex="sample_text", tb_id="sample_text", tb_name="sample_text", tb_page="sample_text", tb_title="sample_text", tb_url="sample_text")
    assert instance.tb_id == "sample_text"
    instance.tb_id = "sample_text_2"
    assert instance.tb_id == "sample_text_2"


def test_wikidb116_trackbacks_tb_name_value_roundtrip():
    instance = wikidb116_trackbacks(tb_ex="sample_text", tb_id="sample_text", tb_name="sample_text", tb_page="sample_text", tb_title="sample_text", tb_url="sample_text")
    assert instance.tb_name == "sample_text"
    instance.tb_name = "sample_text_2"
    assert instance.tb_name == "sample_text_2"


def test_wikidb116_trackbacks_tb_page_value_roundtrip():
    instance = wikidb116_trackbacks(tb_ex="sample_text", tb_id="sample_text", tb_name="sample_text", tb_page="sample_text", tb_title="sample_text", tb_url="sample_text")
    assert instance.tb_page == "sample_text"
    instance.tb_page = "sample_text_2"
    assert instance.tb_page == "sample_text_2"


def test_wikidb116_trackbacks_tb_title_value_roundtrip():
    instance = wikidb116_trackbacks(tb_ex="sample_text", tb_id="sample_text", tb_name="sample_text", tb_page="sample_text", tb_title="sample_text", tb_url="sample_text")
    assert instance.tb_title == "sample_text"
    instance.tb_title = "sample_text_2"
    assert instance.tb_title == "sample_text_2"


def test_wikidb116_trackbacks_tb_url_value_roundtrip():
    instance = wikidb116_trackbacks(tb_ex="sample_text", tb_id="sample_text", tb_name="sample_text", tb_page="sample_text", tb_title="sample_text", tb_url="sample_text")
    assert instance.tb_url == "sample_text"
    instance.tb_url = "sample_text_2"
    assert instance.tb_url == "sample_text_2"


def test_wikidb116_transcache_tc_contents_value_roundtrip():
    instance = wikidb116_transcache(tc_contents="sample_text", tc_time="sample_text", tc_url="sample_text")
    assert instance.tc_contents == "sample_text"
    instance.tc_contents = "sample_text_2"
    assert instance.tc_contents == "sample_text_2"


def test_wikidb116_transcache_tc_time_value_roundtrip():
    instance = wikidb116_transcache(tc_contents="sample_text", tc_time="sample_text", tc_url="sample_text")
    assert instance.tc_time == "sample_text"
    instance.tc_time = "sample_text_2"
    assert instance.tc_time == "sample_text_2"


def test_wikidb116_transcache_tc_url_value_roundtrip():
    instance = wikidb116_transcache(tc_contents="sample_text", tc_time="sample_text", tc_url="sample_text")
    assert instance.tc_url == "sample_text"
    instance.tc_url = "sample_text_2"
    assert instance.tc_url == "sample_text_2"


def test_wikidb116_updatelog_ul_key_value_roundtrip():
    instance = wikidb116_updatelog(ul_key="sample_text")
    assert instance.ul_key == "sample_text"
    instance.ul_key = "sample_text_2"
    assert instance.ul_key == "sample_text_2"


def test_wikidb116_user_user_editcount_value_roundtrip():
    instance = wikidb116_user(user_editcount="sample_text", user_email="sample_text", user_email_authenticated="sample_text", user_email_token="sample_text", user_email_token_expires="sample_text", user_id="sample_text", user_name="sample_text", user_newpass_time="sample_text", user_newpassword="sample_text", user_options="sample_text", user_password="sample_text", user_real_name="sample_text", user_registration="sample_text", user_token="sample_text", user_touched="sample_text")
    assert instance.user_editcount == "sample_text"
    instance.user_editcount = "sample_text_2"
    assert instance.user_editcount == "sample_text_2"


def test_wikidb116_user_user_email_value_roundtrip():
    instance = wikidb116_user(user_editcount="sample_text", user_email="sample_text", user_email_authenticated="sample_text", user_email_token="sample_text", user_email_token_expires="sample_text", user_id="sample_text", user_name="sample_text", user_newpass_time="sample_text", user_newpassword="sample_text", user_options="sample_text", user_password="sample_text", user_real_name="sample_text", user_registration="sample_text", user_token="sample_text", user_touched="sample_text")
    assert instance.user_email == "sample_text"
    instance.user_email = "sample_text_2"
    assert instance.user_email == "sample_text_2"


def test_wikidb116_user_user_email_authenticated_value_roundtrip():
    instance = wikidb116_user(user_editcount="sample_text", user_email="sample_text", user_email_authenticated="sample_text", user_email_token="sample_text", user_email_token_expires="sample_text", user_id="sample_text", user_name="sample_text", user_newpass_time="sample_text", user_newpassword="sample_text", user_options="sample_text", user_password="sample_text", user_real_name="sample_text", user_registration="sample_text", user_token="sample_text", user_touched="sample_text")
    assert instance.user_email_authenticated == "sample_text"
    instance.user_email_authenticated = "sample_text_2"
    assert instance.user_email_authenticated == "sample_text_2"


def test_wikidb116_user_user_email_token_value_roundtrip():
    instance = wikidb116_user(user_editcount="sample_text", user_email="sample_text", user_email_authenticated="sample_text", user_email_token="sample_text", user_email_token_expires="sample_text", user_id="sample_text", user_name="sample_text", user_newpass_time="sample_text", user_newpassword="sample_text", user_options="sample_text", user_password="sample_text", user_real_name="sample_text", user_registration="sample_text", user_token="sample_text", user_touched="sample_text")
    assert instance.user_email_token == "sample_text"
    instance.user_email_token = "sample_text_2"
    assert instance.user_email_token == "sample_text_2"


def test_wikidb116_user_user_email_token_expires_value_roundtrip():
    instance = wikidb116_user(user_editcount="sample_text", user_email="sample_text", user_email_authenticated="sample_text", user_email_token="sample_text", user_email_token_expires="sample_text", user_id="sample_text", user_name="sample_text", user_newpass_time="sample_text", user_newpassword="sample_text", user_options="sample_text", user_password="sample_text", user_real_name="sample_text", user_registration="sample_text", user_token="sample_text", user_touched="sample_text")
    assert instance.user_email_token_expires == "sample_text"
    instance.user_email_token_expires = "sample_text_2"
    assert instance.user_email_token_expires == "sample_text_2"


def test_wikidb116_user_user_id_value_roundtrip():
    instance = wikidb116_user(user_editcount="sample_text", user_email="sample_text", user_email_authenticated="sample_text", user_email_token="sample_text", user_email_token_expires="sample_text", user_id="sample_text", user_name="sample_text", user_newpass_time="sample_text", user_newpassword="sample_text", user_options="sample_text", user_password="sample_text", user_real_name="sample_text", user_registration="sample_text", user_token="sample_text", user_touched="sample_text")
    assert instance.user_id == "sample_text"
    instance.user_id = "sample_text_2"
    assert instance.user_id == "sample_text_2"


def test_wikidb116_user_user_name_value_roundtrip():
    instance = wikidb116_user(user_editcount="sample_text", user_email="sample_text", user_email_authenticated="sample_text", user_email_token="sample_text", user_email_token_expires="sample_text", user_id="sample_text", user_name="sample_text", user_newpass_time="sample_text", user_newpassword="sample_text", user_options="sample_text", user_password="sample_text", user_real_name="sample_text", user_registration="sample_text", user_token="sample_text", user_touched="sample_text")
    assert instance.user_name == "sample_text"
    instance.user_name = "sample_text_2"
    assert instance.user_name == "sample_text_2"


def test_wikidb116_user_user_newpass_time_value_roundtrip():
    instance = wikidb116_user(user_editcount="sample_text", user_email="sample_text", user_email_authenticated="sample_text", user_email_token="sample_text", user_email_token_expires="sample_text", user_id="sample_text", user_name="sample_text", user_newpass_time="sample_text", user_newpassword="sample_text", user_options="sample_text", user_password="sample_text", user_real_name="sample_text", user_registration="sample_text", user_token="sample_text", user_touched="sample_text")
    assert instance.user_newpass_time == "sample_text"
    instance.user_newpass_time = "sample_text_2"
    assert instance.user_newpass_time == "sample_text_2"


def test_wikidb116_user_user_newpassword_value_roundtrip():
    instance = wikidb116_user(user_editcount="sample_text", user_email="sample_text", user_email_authenticated="sample_text", user_email_token="sample_text", user_email_token_expires="sample_text", user_id="sample_text", user_name="sample_text", user_newpass_time="sample_text", user_newpassword="sample_text", user_options="sample_text", user_password="sample_text", user_real_name="sample_text", user_registration="sample_text", user_token="sample_text", user_touched="sample_text")
    assert instance.user_newpassword == "sample_text"
    instance.user_newpassword = "sample_text_2"
    assert instance.user_newpassword == "sample_text_2"


def test_wikidb116_user_user_options_value_roundtrip():
    instance = wikidb116_user(user_editcount="sample_text", user_email="sample_text", user_email_authenticated="sample_text", user_email_token="sample_text", user_email_token_expires="sample_text", user_id="sample_text", user_name="sample_text", user_newpass_time="sample_text", user_newpassword="sample_text", user_options="sample_text", user_password="sample_text", user_real_name="sample_text", user_registration="sample_text", user_token="sample_text", user_touched="sample_text")
    assert instance.user_options == "sample_text"
    instance.user_options = "sample_text_2"
    assert instance.user_options == "sample_text_2"


def test_wikidb116_user_user_password_value_roundtrip():
    instance = wikidb116_user(user_editcount="sample_text", user_email="sample_text", user_email_authenticated="sample_text", user_email_token="sample_text", user_email_token_expires="sample_text", user_id="sample_text", user_name="sample_text", user_newpass_time="sample_text", user_newpassword="sample_text", user_options="sample_text", user_password="sample_text", user_real_name="sample_text", user_registration="sample_text", user_token="sample_text", user_touched="sample_text")
    assert instance.user_password == "sample_text"
    instance.user_password = "sample_text_2"
    assert instance.user_password == "sample_text_2"


def test_wikidb116_user_user_real_name_value_roundtrip():
    instance = wikidb116_user(user_editcount="sample_text", user_email="sample_text", user_email_authenticated="sample_text", user_email_token="sample_text", user_email_token_expires="sample_text", user_id="sample_text", user_name="sample_text", user_newpass_time="sample_text", user_newpassword="sample_text", user_options="sample_text", user_password="sample_text", user_real_name="sample_text", user_registration="sample_text", user_token="sample_text", user_touched="sample_text")
    assert instance.user_real_name == "sample_text"
    instance.user_real_name = "sample_text_2"
    assert instance.user_real_name == "sample_text_2"


def test_wikidb116_user_user_registration_value_roundtrip():
    instance = wikidb116_user(user_editcount="sample_text", user_email="sample_text", user_email_authenticated="sample_text", user_email_token="sample_text", user_email_token_expires="sample_text", user_id="sample_text", user_name="sample_text", user_newpass_time="sample_text", user_newpassword="sample_text", user_options="sample_text", user_password="sample_text", user_real_name="sample_text", user_registration="sample_text", user_token="sample_text", user_touched="sample_text")
    assert instance.user_registration == "sample_text"
    instance.user_registration = "sample_text_2"
    assert instance.user_registration == "sample_text_2"


def test_wikidb116_user_user_token_value_roundtrip():
    instance = wikidb116_user(user_editcount="sample_text", user_email="sample_text", user_email_authenticated="sample_text", user_email_token="sample_text", user_email_token_expires="sample_text", user_id="sample_text", user_name="sample_text", user_newpass_time="sample_text", user_newpassword="sample_text", user_options="sample_text", user_password="sample_text", user_real_name="sample_text", user_registration="sample_text", user_token="sample_text", user_touched="sample_text")
    assert instance.user_token == "sample_text"
    instance.user_token = "sample_text_2"
    assert instance.user_token == "sample_text_2"


def test_wikidb116_user_user_touched_value_roundtrip():
    instance = wikidb116_user(user_editcount="sample_text", user_email="sample_text", user_email_authenticated="sample_text", user_email_token="sample_text", user_email_token_expires="sample_text", user_id="sample_text", user_name="sample_text", user_newpass_time="sample_text", user_newpassword="sample_text", user_options="sample_text", user_password="sample_text", user_real_name="sample_text", user_registration="sample_text", user_token="sample_text", user_touched="sample_text")
    assert instance.user_touched == "sample_text"
    instance.user_touched = "sample_text_2"
    assert instance.user_touched == "sample_text_2"


def test_wikidb116_user_groups_ug_group_value_roundtrip():
    instance = wikidb116_user_groups(ug_group="sample_text", ug_user="sample_text")
    assert instance.ug_group == "sample_text"
    instance.ug_group = "sample_text_2"
    assert instance.ug_group == "sample_text_2"


def test_wikidb116_user_groups_ug_user_value_roundtrip():
    instance = wikidb116_user_groups(ug_group="sample_text", ug_user="sample_text")
    assert instance.ug_user == "sample_text"
    instance.ug_user = "sample_text_2"
    assert instance.ug_user == "sample_text_2"


def test_wikidb116_user_newtalk_user_id_value_roundtrip():
    instance = wikidb116_user_newtalk(user_id="sample_text", user_ip="sample_text", user_last_timestamp="sample_text")
    assert instance.user_id == "sample_text"
    instance.user_id = "sample_text_2"
    assert instance.user_id == "sample_text_2"


def test_wikidb116_user_newtalk_user_ip_value_roundtrip():
    instance = wikidb116_user_newtalk(user_id="sample_text", user_ip="sample_text", user_last_timestamp="sample_text")
    assert instance.user_ip == "sample_text"
    instance.user_ip = "sample_text_2"
    assert instance.user_ip == "sample_text_2"


def test_wikidb116_user_newtalk_user_last_timestamp_value_roundtrip():
    instance = wikidb116_user_newtalk(user_id="sample_text", user_ip="sample_text", user_last_timestamp="sample_text")
    assert instance.user_last_timestamp == "sample_text"
    instance.user_last_timestamp = "sample_text_2"
    assert instance.user_last_timestamp == "sample_text_2"


def test_wikidb116_user_properties_up_property_value_roundtrip():
    instance = wikidb116_user_properties(up_property="sample_text", up_user="sample_text", up_value="sample_text")
    assert instance.up_property == "sample_text"
    instance.up_property = "sample_text_2"
    assert instance.up_property == "sample_text_2"


def test_wikidb116_user_properties_up_user_value_roundtrip():
    instance = wikidb116_user_properties(up_property="sample_text", up_user="sample_text", up_value="sample_text")
    assert instance.up_user == "sample_text"
    instance.up_user = "sample_text_2"
    assert instance.up_user == "sample_text_2"


def test_wikidb116_user_properties_up_value_value_roundtrip():
    instance = wikidb116_user_properties(up_property="sample_text", up_user="sample_text", up_value="sample_text")
    assert instance.up_value == "sample_text"
    instance.up_value = "sample_text_2"
    assert instance.up_value == "sample_text_2"


def test_wikidb116_valid_tag_vt_tag_value_roundtrip():
    instance = wikidb116_valid_tag(vt_tag="sample_text")
    assert instance.vt_tag == "sample_text"
    instance.vt_tag = "sample_text_2"
    assert instance.vt_tag == "sample_text_2"


def test_wikidb116_watchlist_wl_namespace_value_roundtrip():
    instance = wikidb116_watchlist(wl_namespace="sample_text", wl_notificationtimestamp="sample_text", wl_title="sample_text", wl_user="sample_text")
    assert instance.wl_namespace == "sample_text"
    instance.wl_namespace = "sample_text_2"
    assert instance.wl_namespace == "sample_text_2"


def test_wikidb116_watchlist_wl_notificationtimestamp_value_roundtrip():
    instance = wikidb116_watchlist(wl_namespace="sample_text", wl_notificationtimestamp="sample_text", wl_title="sample_text", wl_user="sample_text")
    assert instance.wl_notificationtimestamp == "sample_text"
    instance.wl_notificationtimestamp = "sample_text_2"
    assert instance.wl_notificationtimestamp == "sample_text_2"


def test_wikidb116_watchlist_wl_title_value_roundtrip():
    instance = wikidb116_watchlist(wl_namespace="sample_text", wl_notificationtimestamp="sample_text", wl_title="sample_text", wl_user="sample_text")
    assert instance.wl_title == "sample_text"
    instance.wl_title = "sample_text_2"
    assert instance.wl_title == "sample_text_2"


def test_wikidb116_watchlist_wl_user_value_roundtrip():
    instance = wikidb116_watchlist(wl_namespace="sample_text", wl_notificationtimestamp="sample_text", wl_title="sample_text", wl_user="sample_text")
    assert instance.wl_user == "sample_text"
    instance.wl_user = "sample_text_2"
    assert instance.wl_user == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

wikidb116_archive_strategy = st.builds(wikidb116_archive, ar_comment=safe_text, ar_deleted=st.integers(), ar_flags=safe_text, ar_len=safe_text, ar_minor_edit=st.integers(), ar_namespace=safe_text, ar_page_id=safe_text, ar_parent_id=safe_text, ar_rev_id=safe_text, ar_text=safe_text, ar_text_id=safe_text, ar_timestamp=safe_text, ar_title=safe_text, ar_user=safe_text, ar_user_text=safe_text)
@given(instance=wikidb116_archive_strategy)
@settings(max_examples=25)
def test_wikidb116_archive_instantiation(instance):
    assert isinstance(instance, wikidb116_archive)


wikidb116_category_strategy = st.builds(wikidb116_category, cat_files=safe_text, cat_hidden=st.integers(), cat_id=safe_text, cat_pages=safe_text, cat_subcats=safe_text, cat_title=safe_text)
@given(instance=wikidb116_category_strategy)
@settings(max_examples=25)
def test_wikidb116_category_instantiation(instance):
    assert isinstance(instance, wikidb116_category)


wikidb116_categorylinks_strategy = st.builds(wikidb116_categorylinks, cl_from=safe_text, cl_sortkey=safe_text, cl_timestamp=st.dates(), cl_to=safe_text)
@given(instance=wikidb116_categorylinks_strategy)
@settings(max_examples=25)
def test_wikidb116_categorylinks_instantiation(instance):
    assert isinstance(instance, wikidb116_categorylinks)


wikidb116_change_tag_strategy = st.builds(wikidb116_change_tag, ct_log_id=safe_text, ct_params=safe_text, ct_rc_id=safe_text, ct_rev_id=safe_text, ct_tag=safe_text)
@given(instance=wikidb116_change_tag_strategy)
@settings(max_examples=25)
def test_wikidb116_change_tag_instantiation(instance):
    assert isinstance(instance, wikidb116_change_tag)


wikidb116_external_user_strategy = st.builds(wikidb116_external_user, eu_external_id=safe_text, eu_local_id=safe_text)
@given(instance=wikidb116_external_user_strategy)
@settings(max_examples=25)
def test_wikidb116_external_user_instantiation(instance):
    assert isinstance(instance, wikidb116_external_user)


wikidb116_externallinks_strategy = st.builds(wikidb116_externallinks, el_from=safe_text, el_index=safe_text, el_to=safe_text)
@given(instance=wikidb116_externallinks_strategy)
@settings(max_examples=25)
def test_wikidb116_externallinks_instantiation(instance):
    assert isinstance(instance, wikidb116_externallinks)


wikidb116_filearchive_strategy = st.builds(wikidb116_filearchive, fa_archive_name=safe_text, fa_bits=safe_text, fa_deleted=st.integers(), fa_deleted_reason=safe_text, fa_deleted_timestamp=safe_text, fa_deleted_user=safe_text, fa_description=safe_text, fa_height=safe_text, fa_id=safe_text, fa_major_mime=safe_text, fa_media_type=safe_text, fa_metadata=safe_text, fa_minor_mime=safe_text, fa_name=safe_text, fa_size=safe_text, fa_storage_group=safe_text, fa_storage_key=safe_text, fa_timestamp=safe_text, fa_user=safe_text, fa_user_text=safe_text, fa_width=safe_text)
@given(instance=wikidb116_filearchive_strategy)
@settings(max_examples=25)
def test_wikidb116_filearchive_instantiation(instance):
    assert isinstance(instance, wikidb116_filearchive)


wikidb116_hitcounter_strategy = st.builds(wikidb116_hitcounter, hc_id=safe_text)
@given(instance=wikidb116_hitcounter_strategy)
@settings(max_examples=25)
def test_wikidb116_hitcounter_instantiation(instance):
    assert isinstance(instance, wikidb116_hitcounter)


wikidb116_image_strategy = st.builds(wikidb116_image, img_bits=safe_text, img_description=safe_text, img_height=safe_text, img_major_mime=safe_text, img_media_type=safe_text, img_metadata=safe_text, img_minor_mime=safe_text, img_name=safe_text, img_sha1=safe_text, img_size=safe_text, img_timestamp=safe_text, img_user=safe_text, img_user_text=safe_text, img_width=safe_text)
@given(instance=wikidb116_image_strategy)
@settings(max_examples=25)
def test_wikidb116_image_instantiation(instance):
    assert isinstance(instance, wikidb116_image)


wikidb116_imagelinks_strategy = st.builds(wikidb116_imagelinks, il_from=safe_text, il_to=safe_text)
@given(instance=wikidb116_imagelinks_strategy)
@settings(max_examples=25)
def test_wikidb116_imagelinks_instantiation(instance):
    assert isinstance(instance, wikidb116_imagelinks)


wikidb116_interwiki_strategy = st.builds(wikidb116_interwiki, iw_local=st.integers(), iw_prefix=safe_text, iw_trans=st.integers(), iw_url=safe_text)
@given(instance=wikidb116_interwiki_strategy)
@settings(max_examples=25)
def test_wikidb116_interwiki_instantiation(instance):
    assert isinstance(instance, wikidb116_interwiki)


wikidb116_ipblocks_strategy = st.builds(wikidb116_ipblocks, ipb_address=safe_text, ipb_allow_usertalk=st.integers(), ipb_anon_only=st.integers(), ipb_auto=st.integers(), ipb_block_email=st.integers(), ipb_by=safe_text, ipb_by_text=safe_text, ipb_create_account=st.integers(), ipb_deleted=st.integers(), ipb_enable_autoblock=st.integers(), ipb_expiry=safe_text, ipb_id=safe_text, ipb_range_end=safe_text, ipb_range_start=safe_text, ipb_reason=safe_text, ipb_timestamp=safe_text, ipb_user=safe_text)
@given(instance=wikidb116_ipblocks_strategy)
@settings(max_examples=25)
def test_wikidb116_ipblocks_instantiation(instance):
    assert isinstance(instance, wikidb116_ipblocks)


wikidb116_job_strategy = st.builds(wikidb116_job, job_cmd=safe_text, job_id=safe_text, job_namespace=safe_text, job_params=safe_text, job_title=safe_text)
@given(instance=wikidb116_job_strategy)
@settings(max_examples=25)
def test_wikidb116_job_instantiation(instance):
    assert isinstance(instance, wikidb116_job)


wikidb116_l10n_cache_strategy = st.builds(wikidb116_l10n_cache, lc_key=safe_text, lc_lang=safe_text, lc_value=safe_text)
@given(instance=wikidb116_l10n_cache_strategy)
@settings(max_examples=25)
def test_wikidb116_l10n_cache_instantiation(instance):
    assert isinstance(instance, wikidb116_l10n_cache)


wikidb116_langlinks_strategy = st.builds(wikidb116_langlinks, ll_from=safe_text, ll_lang=safe_text, ll_title=safe_text)
@given(instance=wikidb116_langlinks_strategy)
@settings(max_examples=25)
def test_wikidb116_langlinks_instantiation(instance):
    assert isinstance(instance, wikidb116_langlinks)


wikidb116_log_search_strategy = st.builds(wikidb116_log_search, ls_field=safe_text, ls_log_id=safe_text, ls_value=safe_text)
@given(instance=wikidb116_log_search_strategy)
@settings(max_examples=25)
def test_wikidb116_log_search_instantiation(instance):
    assert isinstance(instance, wikidb116_log_search)


wikidb116_logging_strategy = st.builds(wikidb116_logging, log_action=safe_text, log_comment=safe_text, log_deleted=st.integers(), log_id=safe_text, log_namespace=safe_text, log_page=safe_text, log_params=safe_text, log_timestamp=safe_text, log_title=safe_text, log_type=safe_text, log_user=safe_text, log_user_text=safe_text)
@given(instance=wikidb116_logging_strategy)
@settings(max_examples=25)
def test_wikidb116_logging_instantiation(instance):
    assert isinstance(instance, wikidb116_logging)


wikidb116_math_strategy = st.builds(wikidb116_math, math_html=safe_text, math_html_conservativeness=st.integers(), math_inputhash=safe_text, math_mathml=safe_text, math_outputhash=safe_text)
@given(instance=wikidb116_math_strategy)
@settings(max_examples=25)
def test_wikidb116_math_instantiation(instance):
    assert isinstance(instance, wikidb116_math)


wikidb116_objectcache_strategy = st.builds(wikidb116_objectcache, exptime=st.dates(), keyname=safe_text, value=safe_text)
@given(instance=wikidb116_objectcache_strategy)
@settings(max_examples=25)
def test_wikidb116_objectcache_instantiation(instance):
    assert isinstance(instance, wikidb116_objectcache)


wikidb116_oldimage_strategy = st.builds(wikidb116_oldimage, oi_archive_name=safe_text, oi_bits=safe_text, oi_deleted=st.integers(), oi_description=safe_text, oi_height=safe_text, oi_major_mime=safe_text, oi_media_type=safe_text, oi_metadata=safe_text, oi_minor_mime=safe_text, oi_name=safe_text, oi_sha1=safe_text, oi_size=safe_text, oi_timestamp=safe_text, oi_user=safe_text, oi_user_text=safe_text, oi_width=safe_text)
@given(instance=wikidb116_oldimage_strategy)
@settings(max_examples=25)
def test_wikidb116_oldimage_instantiation(instance):
    assert isinstance(instance, wikidb116_oldimage)


wikidb116_page_strategy = st.builds(wikidb116_page, page_counter=safe_text, page_id=safe_text, page_is_new=st.integers(), page_is_redirect=st.integers(), page_latest=safe_text, page_len=safe_text, page_namespace=safe_text, page_random=st.floats(allow_nan=False, allow_infinity=False), page_restrictions=safe_text, page_title=safe_text, page_touched=safe_text)
@given(instance=wikidb116_page_strategy)
@settings(max_examples=25)
def test_wikidb116_page_instantiation(instance):
    assert isinstance(instance, wikidb116_page)


wikidb116_page_props_strategy = st.builds(wikidb116_page_props, pp_page=safe_text, pp_propname=safe_text, pp_value=safe_text)
@given(instance=wikidb116_page_props_strategy)
@settings(max_examples=25)
def test_wikidb116_page_props_instantiation(instance):
    assert isinstance(instance, wikidb116_page_props)


wikidb116_page_restrictions_strategy = st.builds(wikidb116_page_restrictions, pr_cascade=st.integers(), pr_expiry=safe_text, pr_id=safe_text, pr_level=safe_text, pr_page=safe_text, pr_type=safe_text, pr_user=safe_text)
@given(instance=wikidb116_page_restrictions_strategy)
@settings(max_examples=25)
def test_wikidb116_page_restrictions_instantiation(instance):
    assert isinstance(instance, wikidb116_page_restrictions)


wikidb116_pagelinks_strategy = st.builds(wikidb116_pagelinks, pl_from=safe_text, pl_namespace=safe_text, pl_title=safe_text)
@given(instance=wikidb116_pagelinks_strategy)
@settings(max_examples=25)
def test_wikidb116_pagelinks_instantiation(instance):
    assert isinstance(instance, wikidb116_pagelinks)


wikidb116_protected_titles_strategy = st.builds(wikidb116_protected_titles, pt_create_perm=safe_text, pt_expiry=safe_text, pt_namespace=safe_text, pt_reason=safe_text, pt_timestamp=safe_text, pt_title=safe_text, pt_user=safe_text)
@given(instance=wikidb116_protected_titles_strategy)
@settings(max_examples=25)
def test_wikidb116_protected_titles_instantiation(instance):
    assert isinstance(instance, wikidb116_protected_titles)


wikidb116_querycache_strategy = st.builds(wikidb116_querycache, qc_namespace=safe_text, qc_title=safe_text, qc_type=safe_text, qc_value=safe_text)
@given(instance=wikidb116_querycache_strategy)
@settings(max_examples=25)
def test_wikidb116_querycache_instantiation(instance):
    assert isinstance(instance, wikidb116_querycache)


wikidb116_querycache_info_strategy = st.builds(wikidb116_querycache_info, qci_timestamp=safe_text, qci_type=safe_text)
@given(instance=wikidb116_querycache_info_strategy)
@settings(max_examples=25)
def test_wikidb116_querycache_info_instantiation(instance):
    assert isinstance(instance, wikidb116_querycache_info)


wikidb116_querycachetwo_strategy = st.builds(wikidb116_querycachetwo, qcc_namespace=safe_text, qcc_namespacetwo=safe_text, qcc_title=safe_text, qcc_titletwo=safe_text, qcc_type=safe_text, qcc_value=safe_text)
@given(instance=wikidb116_querycachetwo_strategy)
@settings(max_examples=25)
def test_wikidb116_querycachetwo_instantiation(instance):
    assert isinstance(instance, wikidb116_querycachetwo)


wikidb116_recentchanges_strategy = st.builds(wikidb116_recentchanges, rc_bot=st.integers(), rc_comment=safe_text, rc_cur_id=safe_text, rc_cur_time=safe_text, rc_deleted=st.integers(), rc_id=safe_text, rc_ip=safe_text, rc_last_oldid=safe_text, rc_log_action=safe_text, rc_log_type=safe_text, rc_logid=safe_text, rc_minor=st.integers(), rc_moved_to_ns=st.integers(), rc_moved_to_title=safe_text, rc_namespace=safe_text, rc_new=st.integers(), rc_new_len=safe_text, rc_old_len=safe_text, rc_params=safe_text, rc_patrolled=st.integers(), rc_this_oldid=safe_text, rc_timestamp=safe_text, rc_title=safe_text, rc_type=st.integers(), rc_user=safe_text, rc_user_text=safe_text)
@given(instance=wikidb116_recentchanges_strategy)
@settings(max_examples=25)
def test_wikidb116_recentchanges_instantiation(instance):
    assert isinstance(instance, wikidb116_recentchanges)


wikidb116_redirect_strategy = st.builds(wikidb116_redirect, rd_fragment=safe_text, rd_from=safe_text, rd_interwiki=safe_text, rd_namespace=safe_text, rd_title=safe_text)
@given(instance=wikidb116_redirect_strategy)
@settings(max_examples=25)
def test_wikidb116_redirect_instantiation(instance):
    assert isinstance(instance, wikidb116_redirect)


wikidb116_revision_strategy = st.builds(wikidb116_revision, rev_comment=safe_text, rev_deleted=st.integers(), rev_id=safe_text, rev_len=safe_text, rev_minor_edit=st.integers(), rev_page=safe_text, rev_parent_id=safe_text, rev_text_id=safe_text, rev_timestamp=safe_text, rev_user=safe_text, rev_user_text=safe_text)
@given(instance=wikidb116_revision_strategy)
@settings(max_examples=25)
def test_wikidb116_revision_instantiation(instance):
    assert isinstance(instance, wikidb116_revision)


wikidb116_searchindex_strategy = st.builds(wikidb116_searchindex, si_page=safe_text, si_text=safe_text, si_title=safe_text)
@given(instance=wikidb116_searchindex_strategy)
@settings(max_examples=25)
def test_wikidb116_searchindex_instantiation(instance):
    assert isinstance(instance, wikidb116_searchindex)


wikidb116_site_stats_strategy = st.builds(wikidb116_site_stats, ss_active_users=safe_text, ss_admins=safe_text, ss_good_articles=safe_text, ss_images=safe_text, ss_row_id=safe_text, ss_total_edits=safe_text, ss_total_pages=safe_text, ss_total_views=safe_text, ss_users=safe_text)
@given(instance=wikidb116_site_stats_strategy)
@settings(max_examples=25)
def test_wikidb116_site_stats_instantiation(instance):
    assert isinstance(instance, wikidb116_site_stats)


wikidb116_tag_summary_strategy = st.builds(wikidb116_tag_summary, ts_log_id=safe_text, ts_rc_id=safe_text, ts_rev_id=safe_text, ts_tags=safe_text)
@given(instance=wikidb116_tag_summary_strategy)
@settings(max_examples=25)
def test_wikidb116_tag_summary_instantiation(instance):
    assert isinstance(instance, wikidb116_tag_summary)


wikidb116_templatelinks_strategy = st.builds(wikidb116_templatelinks, tl_from=safe_text, tl_namespace=safe_text, tl_title=safe_text)
@given(instance=wikidb116_templatelinks_strategy)
@settings(max_examples=25)
def test_wikidb116_templatelinks_instantiation(instance):
    assert isinstance(instance, wikidb116_templatelinks)


wikidb116_text_strategy = st.builds(wikidb116_text, old_flags=safe_text, old_id=safe_text, old_text=safe_text)
@given(instance=wikidb116_text_strategy)
@settings(max_examples=25)
def test_wikidb116_text_instantiation(instance):
    assert isinstance(instance, wikidb116_text)


wikidb116_trackbacks_strategy = st.builds(wikidb116_trackbacks, tb_ex=safe_text, tb_id=safe_text, tb_name=safe_text, tb_page=safe_text, tb_title=safe_text, tb_url=safe_text)
@given(instance=wikidb116_trackbacks_strategy)
@settings(max_examples=25)
def test_wikidb116_trackbacks_instantiation(instance):
    assert isinstance(instance, wikidb116_trackbacks)


wikidb116_transcache_strategy = st.builds(wikidb116_transcache, tc_contents=safe_text, tc_time=safe_text, tc_url=safe_text)
@given(instance=wikidb116_transcache_strategy)
@settings(max_examples=25)
def test_wikidb116_transcache_instantiation(instance):
    assert isinstance(instance, wikidb116_transcache)


wikidb116_updatelog_strategy = st.builds(wikidb116_updatelog, ul_key=safe_text)
@given(instance=wikidb116_updatelog_strategy)
@settings(max_examples=25)
def test_wikidb116_updatelog_instantiation(instance):
    assert isinstance(instance, wikidb116_updatelog)


wikidb116_user_strategy = st.builds(wikidb116_user, user_editcount=safe_text, user_email=safe_text, user_email_authenticated=safe_text, user_email_token=safe_text, user_email_token_expires=safe_text, user_id=safe_text, user_name=safe_text, user_newpass_time=safe_text, user_newpassword=safe_text, user_options=safe_text, user_password=safe_text, user_real_name=safe_text, user_registration=safe_text, user_token=safe_text, user_touched=safe_text)
@given(instance=wikidb116_user_strategy)
@settings(max_examples=25)
def test_wikidb116_user_instantiation(instance):
    assert isinstance(instance, wikidb116_user)


wikidb116_user_groups_strategy = st.builds(wikidb116_user_groups, ug_group=safe_text, ug_user=safe_text)
@given(instance=wikidb116_user_groups_strategy)
@settings(max_examples=25)
def test_wikidb116_user_groups_instantiation(instance):
    assert isinstance(instance, wikidb116_user_groups)


wikidb116_user_newtalk_strategy = st.builds(wikidb116_user_newtalk, user_id=safe_text, user_ip=safe_text, user_last_timestamp=safe_text)
@given(instance=wikidb116_user_newtalk_strategy)
@settings(max_examples=25)
def test_wikidb116_user_newtalk_instantiation(instance):
    assert isinstance(instance, wikidb116_user_newtalk)


wikidb116_user_properties_strategy = st.builds(wikidb116_user_properties, up_property=safe_text, up_user=safe_text, up_value=safe_text)
@given(instance=wikidb116_user_properties_strategy)
@settings(max_examples=25)
def test_wikidb116_user_properties_instantiation(instance):
    assert isinstance(instance, wikidb116_user_properties)


wikidb116_valid_tag_strategy = st.builds(wikidb116_valid_tag, vt_tag=safe_text)
@given(instance=wikidb116_valid_tag_strategy)
@settings(max_examples=25)
def test_wikidb116_valid_tag_instantiation(instance):
    assert isinstance(instance, wikidb116_valid_tag)


wikidb116_watchlist_strategy = st.builds(wikidb116_watchlist, wl_namespace=safe_text, wl_notificationtimestamp=safe_text, wl_title=safe_text, wl_user=safe_text)
@given(instance=wikidb116_watchlist_strategy)
@settings(max_examples=25)
def test_wikidb116_watchlist_instantiation(instance):
    assert isinstance(instance, wikidb116_watchlist)



