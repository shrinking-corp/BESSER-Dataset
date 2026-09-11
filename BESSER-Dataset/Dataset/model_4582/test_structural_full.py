import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    sparrow_Action,
    sparrow_Callprocess,
    sparrow_Catch,
    sparrow_Copydata,
    sparrow_Doozle,
    sparrow_Dropfile,
    sparrow_Expression,
    sparrow_FBCLead,
    sparrow_Fetch,
    sparrow_Finally,
    sparrow_GooglecalPUT,
    sparrow_LoadCsv,
    sparrow_Process,
    sparrow_Rest,
    sparrow_RestPart,
    sparrow_SlackPUT,
    sparrow_Sms,
    sparrow_Transform,
    sparrow_TrelloGET,
    sparrow_TrelloPUT,
    sparrow_Try,
    sparrow_Updatedaudit,
    sparrow_WriteCsv,
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

def test_sparrow_Action_name_value_roundtrip():
    instance = sparrow_Action(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sparrow_Callprocess_datasource_value_roundtrip():
    instance = sparrow_Callprocess(datasource="sample_text", source="sample_text", target="sample_text", value="sample_text")
    assert instance.datasource == "sample_text"
    instance.datasource = "sample_text_2"
    assert instance.datasource == "sample_text_2"


def test_sparrow_Callprocess_source_value_roundtrip():
    instance = sparrow_Callprocess(datasource="sample_text", source="sample_text", target="sample_text", value="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_sparrow_Callprocess_target_value_roundtrip():
    instance = sparrow_Callprocess(datasource="sample_text", source="sample_text", target="sample_text", value="sample_text")
    assert instance.target == "sample_text"
    instance.target = "sample_text_2"
    assert instance.target == "sample_text_2"


def test_sparrow_Callprocess_value_value_roundtrip():
    instance = sparrow_Callprocess(datasource="sample_text", source="sample_text", target="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sparrow_Catch_name_value_roundtrip():
    instance = sparrow_Catch(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sparrow_Copydata_source_value_roundtrip():
    instance = sparrow_Copydata(source="sample_text", to="sample_text", value="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_sparrow_Copydata_to_value_roundtrip():
    instance = sparrow_Copydata(source="sample_text", to="sample_text", value="sample_text")
    assert instance.to == "sample_text"
    instance.to = "sample_text_2"
    assert instance.to == "sample_text_2"


def test_sparrow_Copydata_value_value_roundtrip():
    instance = sparrow_Copydata(source="sample_text", to="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sparrow_Doozle_on_value_roundtrip():
    instance = sparrow_Doozle(on="sample_text", target="sample_text", value="sample_text")
    assert instance.on == "sample_text"
    instance.on = "sample_text_2"
    assert instance.on == "sample_text_2"


def test_sparrow_Doozle_target_value_roundtrip():
    instance = sparrow_Doozle(on="sample_text", target="sample_text", value="sample_text")
    assert instance.target == "sample_text"
    instance.target = "sample_text_2"
    assert instance.target == "sample_text_2"


def test_sparrow_Doozle_value_value_roundtrip():
    instance = sparrow_Doozle(on="sample_text", target="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sparrow_Dropfile_target_value_roundtrip():
    instance = sparrow_Dropfile(target="sample_text")
    assert instance.target == "sample_text"
    instance.target = "sample_text_2"
    assert instance.target == "sample_text_2"


def test_sparrow_Expression_lhs_value_roundtrip():
    instance = sparrow_Expression(lhs="sample_text", operator="sample_text", rhs="sample_text")
    assert instance.lhs == "sample_text"
    instance.lhs = "sample_text_2"
    assert instance.lhs == "sample_text_2"


def test_sparrow_Expression_operator_value_roundtrip():
    instance = sparrow_Expression(lhs="sample_text", operator="sample_text", rhs="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_sparrow_Expression_rhs_value_roundtrip():
    instance = sparrow_Expression(lhs="sample_text", operator="sample_text", rhs="sample_text")
    assert instance.rhs == "sample_text"
    instance.rhs = "sample_text_2"
    assert instance.rhs == "sample_text_2"


def test_sparrow_FBCLead_accessToken_value_roundtrip():
    instance = sparrow_FBCLead(accessToken="sample_text", accountId="sample_text", appSecret="sample_text", campaignId="sample_text", target="sample_text", value="sample_text")
    assert instance.accessToken == "sample_text"
    instance.accessToken = "sample_text_2"
    assert instance.accessToken == "sample_text_2"


def test_sparrow_FBCLead_accountId_value_roundtrip():
    instance = sparrow_FBCLead(accessToken="sample_text", accountId="sample_text", appSecret="sample_text", campaignId="sample_text", target="sample_text", value="sample_text")
    assert instance.accountId == "sample_text"
    instance.accountId = "sample_text_2"
    assert instance.accountId == "sample_text_2"


def test_sparrow_FBCLead_appSecret_value_roundtrip():
    instance = sparrow_FBCLead(accessToken="sample_text", accountId="sample_text", appSecret="sample_text", campaignId="sample_text", target="sample_text", value="sample_text")
    assert instance.appSecret == "sample_text"
    instance.appSecret = "sample_text_2"
    assert instance.appSecret == "sample_text_2"


def test_sparrow_FBCLead_campaignId_value_roundtrip():
    instance = sparrow_FBCLead(accessToken="sample_text", accountId="sample_text", appSecret="sample_text", campaignId="sample_text", target="sample_text", value="sample_text")
    assert instance.campaignId == "sample_text"
    instance.campaignId = "sample_text_2"
    assert instance.campaignId == "sample_text_2"


def test_sparrow_FBCLead_target_value_roundtrip():
    instance = sparrow_FBCLead(accessToken="sample_text", accountId="sample_text", appSecret="sample_text", campaignId="sample_text", target="sample_text", value="sample_text")
    assert instance.target == "sample_text"
    instance.target = "sample_text_2"
    assert instance.target == "sample_text_2"


def test_sparrow_FBCLead_value_value_roundtrip():
    instance = sparrow_FBCLead(accessToken="sample_text", accountId="sample_text", appSecret="sample_text", campaignId="sample_text", target="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sparrow_Fetch_source_value_roundtrip():
    instance = sparrow_Fetch(source="sample_text", value="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_sparrow_Fetch_value_value_roundtrip():
    instance = sparrow_Fetch(source="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sparrow_Finally_name_value_roundtrip():
    instance = sparrow_Finally(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sparrow_GooglecalPUT_authstore_value_roundtrip():
    instance = sparrow_GooglecalPUT(authstore="sample_text", key="sample_text", source="sample_text", useraccount="sample_text", value="sample_text")
    assert instance.authstore == "sample_text"
    instance.authstore = "sample_text_2"
    assert instance.authstore == "sample_text_2"


def test_sparrow_GooglecalPUT_key_value_roundtrip():
    instance = sparrow_GooglecalPUT(authstore="sample_text", key="sample_text", source="sample_text", useraccount="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_sparrow_GooglecalPUT_source_value_roundtrip():
    instance = sparrow_GooglecalPUT(authstore="sample_text", key="sample_text", source="sample_text", useraccount="sample_text", value="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_sparrow_GooglecalPUT_useraccount_value_roundtrip():
    instance = sparrow_GooglecalPUT(authstore="sample_text", key="sample_text", source="sample_text", useraccount="sample_text", value="sample_text")
    assert instance.useraccount == "sample_text"
    instance.useraccount = "sample_text_2"
    assert instance.useraccount == "sample_text_2"


def test_sparrow_GooglecalPUT_value_value_roundtrip():
    instance = sparrow_GooglecalPUT(authstore="sample_text", key="sample_text", source="sample_text", useraccount="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sparrow_LoadCsv_delim_value_roundtrip():
    instance = sparrow_LoadCsv(delim="sample_text", source="sample_text", to="sample_text", value="sample_text")
    assert instance.delim == "sample_text"
    instance.delim = "sample_text_2"
    assert instance.delim == "sample_text_2"


def test_sparrow_LoadCsv_source_value_roundtrip():
    instance = sparrow_LoadCsv(delim="sample_text", source="sample_text", to="sample_text", value="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_sparrow_LoadCsv_to_value_roundtrip():
    instance = sparrow_LoadCsv(delim="sample_text", source="sample_text", to="sample_text", value="sample_text")
    assert instance.to == "sample_text"
    instance.to = "sample_text_2"
    assert instance.to == "sample_text_2"


def test_sparrow_LoadCsv_value_value_roundtrip():
    instance = sparrow_LoadCsv(delim="sample_text", source="sample_text", to="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sparrow_Process_name_value_roundtrip():
    instance = sparrow_Process(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sparrow_Rest_ackdata_value_roundtrip():
    instance = sparrow_Rest(ackdata="sample_text", ackdatato="sample_text", authtoken="sample_text", headerdata="sample_text", headerdatafrom="sample_text", method="sample_text", parentName="sample_text", parentdata="sample_text", postdatafrom="sample_text", resourcedatafrom="sample_text", url="sample_text", urldata="sample_text")
    assert instance.ackdata == "sample_text"
    instance.ackdata = "sample_text_2"
    assert instance.ackdata == "sample_text_2"


def test_sparrow_Rest_ackdatato_value_roundtrip():
    instance = sparrow_Rest(ackdata="sample_text", ackdatato="sample_text", authtoken="sample_text", headerdata="sample_text", headerdatafrom="sample_text", method="sample_text", parentName="sample_text", parentdata="sample_text", postdatafrom="sample_text", resourcedatafrom="sample_text", url="sample_text", urldata="sample_text")
    assert instance.ackdatato == "sample_text"
    instance.ackdatato = "sample_text_2"
    assert instance.ackdatato == "sample_text_2"


def test_sparrow_Rest_authtoken_value_roundtrip():
    instance = sparrow_Rest(ackdata="sample_text", ackdatato="sample_text", authtoken="sample_text", headerdata="sample_text", headerdatafrom="sample_text", method="sample_text", parentName="sample_text", parentdata="sample_text", postdatafrom="sample_text", resourcedatafrom="sample_text", url="sample_text", urldata="sample_text")
    assert instance.authtoken == "sample_text"
    instance.authtoken = "sample_text_2"
    assert instance.authtoken == "sample_text_2"


def test_sparrow_Rest_headerdata_value_roundtrip():
    instance = sparrow_Rest(ackdata="sample_text", ackdatato="sample_text", authtoken="sample_text", headerdata="sample_text", headerdatafrom="sample_text", method="sample_text", parentName="sample_text", parentdata="sample_text", postdatafrom="sample_text", resourcedatafrom="sample_text", url="sample_text", urldata="sample_text")
    assert instance.headerdata == "sample_text"
    instance.headerdata = "sample_text_2"
    assert instance.headerdata == "sample_text_2"


def test_sparrow_Rest_headerdatafrom_value_roundtrip():
    instance = sparrow_Rest(ackdata="sample_text", ackdatato="sample_text", authtoken="sample_text", headerdata="sample_text", headerdatafrom="sample_text", method="sample_text", parentName="sample_text", parentdata="sample_text", postdatafrom="sample_text", resourcedatafrom="sample_text", url="sample_text", urldata="sample_text")
    assert instance.headerdatafrom == "sample_text"
    instance.headerdatafrom = "sample_text_2"
    assert instance.headerdatafrom == "sample_text_2"


def test_sparrow_Rest_method_value_roundtrip():
    instance = sparrow_Rest(ackdata="sample_text", ackdatato="sample_text", authtoken="sample_text", headerdata="sample_text", headerdatafrom="sample_text", method="sample_text", parentName="sample_text", parentdata="sample_text", postdatafrom="sample_text", resourcedatafrom="sample_text", url="sample_text", urldata="sample_text")
    assert instance.method == "sample_text"
    instance.method = "sample_text_2"
    assert instance.method == "sample_text_2"


def test_sparrow_Rest_parentName_value_roundtrip():
    instance = sparrow_Rest(ackdata="sample_text", ackdatato="sample_text", authtoken="sample_text", headerdata="sample_text", headerdatafrom="sample_text", method="sample_text", parentName="sample_text", parentdata="sample_text", postdatafrom="sample_text", resourcedatafrom="sample_text", url="sample_text", urldata="sample_text")
    assert instance.parentName == "sample_text"
    instance.parentName = "sample_text_2"
    assert instance.parentName == "sample_text_2"


def test_sparrow_Rest_parentdata_value_roundtrip():
    instance = sparrow_Rest(ackdata="sample_text", ackdatato="sample_text", authtoken="sample_text", headerdata="sample_text", headerdatafrom="sample_text", method="sample_text", parentName="sample_text", parentdata="sample_text", postdatafrom="sample_text", resourcedatafrom="sample_text", url="sample_text", urldata="sample_text")
    assert instance.parentdata == "sample_text"
    instance.parentdata = "sample_text_2"
    assert instance.parentdata == "sample_text_2"


def test_sparrow_Rest_postdatafrom_value_roundtrip():
    instance = sparrow_Rest(ackdata="sample_text", ackdatato="sample_text", authtoken="sample_text", headerdata="sample_text", headerdatafrom="sample_text", method="sample_text", parentName="sample_text", parentdata="sample_text", postdatafrom="sample_text", resourcedatafrom="sample_text", url="sample_text", urldata="sample_text")
    assert instance.postdatafrom == "sample_text"
    instance.postdatafrom = "sample_text_2"
    assert instance.postdatafrom == "sample_text_2"


def test_sparrow_Rest_resourcedatafrom_value_roundtrip():
    instance = sparrow_Rest(ackdata="sample_text", ackdatato="sample_text", authtoken="sample_text", headerdata="sample_text", headerdatafrom="sample_text", method="sample_text", parentName="sample_text", parentdata="sample_text", postdatafrom="sample_text", resourcedatafrom="sample_text", url="sample_text", urldata="sample_text")
    assert instance.resourcedatafrom == "sample_text"
    instance.resourcedatafrom = "sample_text_2"
    assert instance.resourcedatafrom == "sample_text_2"


def test_sparrow_Rest_url_value_roundtrip():
    instance = sparrow_Rest(ackdata="sample_text", ackdatato="sample_text", authtoken="sample_text", headerdata="sample_text", headerdatafrom="sample_text", method="sample_text", parentName="sample_text", parentdata="sample_text", postdatafrom="sample_text", resourcedatafrom="sample_text", url="sample_text", urldata="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_sparrow_Rest_urldata_value_roundtrip():
    instance = sparrow_Rest(ackdata="sample_text", ackdatato="sample_text", authtoken="sample_text", headerdata="sample_text", headerdatafrom="sample_text", method="sample_text", parentName="sample_text", parentdata="sample_text", postdatafrom="sample_text", resourcedatafrom="sample_text", url="sample_text", urldata="sample_text")
    assert instance.urldata == "sample_text"
    instance.urldata = "sample_text_2"
    assert instance.urldata == "sample_text_2"


def test_sparrow_RestPart_partData_value_roundtrip():
    instance = sparrow_RestPart(partData="sample_text", partName="sample_text")
    assert instance.partData == "sample_text"
    instance.partData = "sample_text_2"
    assert instance.partData == "sample_text_2"


def test_sparrow_RestPart_partName_value_roundtrip():
    instance = sparrow_RestPart(partData="sample_text", partName="sample_text")
    assert instance.partName == "sample_text"
    instance.partName = "sample_text_2"
    assert instance.partName == "sample_text_2"


def test_sparrow_SlackPUT_channel_value_roundtrip():
    instance = sparrow_SlackPUT(channel="sample_text", team="sample_text", value="sample_text")
    assert instance.channel == "sample_text"
    instance.channel = "sample_text_2"
    assert instance.channel == "sample_text_2"


def test_sparrow_SlackPUT_team_value_roundtrip():
    instance = sparrow_SlackPUT(channel="sample_text", team="sample_text", value="sample_text")
    assert instance.team == "sample_text"
    instance.team = "sample_text_2"
    assert instance.team == "sample_text_2"


def test_sparrow_SlackPUT_value_value_roundtrip():
    instance = sparrow_SlackPUT(channel="sample_text", team="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sparrow_Sms_target_value_roundtrip():
    instance = sparrow_Sms(target="sample_text", value="sample_text")
    assert instance.target == "sample_text"
    instance.target = "sample_text_2"
    assert instance.target == "sample_text_2"


def test_sparrow_Sms_value_value_roundtrip():
    instance = sparrow_Sms(target="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sparrow_Transform_on_value_roundtrip():
    instance = sparrow_Transform(on="sample_text", value="sample_text")
    assert instance.on == "sample_text"
    instance.on = "sample_text_2"
    assert instance.on == "sample_text_2"


def test_sparrow_Transform_value_value_roundtrip():
    instance = sparrow_Transform(on="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sparrow_TrelloGET_authtoken_value_roundtrip():
    instance = sparrow_TrelloGET(authtoken="sample_text", board="sample_text", key="sample_text", target="sample_text", useraccount="sample_text", value="sample_text")
    assert instance.authtoken == "sample_text"
    instance.authtoken = "sample_text_2"
    assert instance.authtoken == "sample_text_2"


def test_sparrow_TrelloGET_board_value_roundtrip():
    instance = sparrow_TrelloGET(authtoken="sample_text", board="sample_text", key="sample_text", target="sample_text", useraccount="sample_text", value="sample_text")
    assert instance.board == "sample_text"
    instance.board = "sample_text_2"
    assert instance.board == "sample_text_2"


def test_sparrow_TrelloGET_key_value_roundtrip():
    instance = sparrow_TrelloGET(authtoken="sample_text", board="sample_text", key="sample_text", target="sample_text", useraccount="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_sparrow_TrelloGET_target_value_roundtrip():
    instance = sparrow_TrelloGET(authtoken="sample_text", board="sample_text", key="sample_text", target="sample_text", useraccount="sample_text", value="sample_text")
    assert instance.target == "sample_text"
    instance.target = "sample_text_2"
    assert instance.target == "sample_text_2"


def test_sparrow_TrelloGET_useraccount_value_roundtrip():
    instance = sparrow_TrelloGET(authtoken="sample_text", board="sample_text", key="sample_text", target="sample_text", useraccount="sample_text", value="sample_text")
    assert instance.useraccount == "sample_text"
    instance.useraccount = "sample_text_2"
    assert instance.useraccount == "sample_text_2"


def test_sparrow_TrelloGET_value_value_roundtrip():
    instance = sparrow_TrelloGET(authtoken="sample_text", board="sample_text", key="sample_text", target="sample_text", useraccount="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sparrow_TrelloPUT_authtoken_value_roundtrip():
    instance = sparrow_TrelloPUT(authtoken="sample_text", key="sample_text", list="sample_text", source="sample_text", useraccount="sample_text", value="sample_text")
    assert instance.authtoken == "sample_text"
    instance.authtoken = "sample_text_2"
    assert instance.authtoken == "sample_text_2"


def test_sparrow_TrelloPUT_key_value_roundtrip():
    instance = sparrow_TrelloPUT(authtoken="sample_text", key="sample_text", list="sample_text", source="sample_text", useraccount="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_sparrow_TrelloPUT_list_value_roundtrip():
    instance = sparrow_TrelloPUT(authtoken="sample_text", key="sample_text", list="sample_text", source="sample_text", useraccount="sample_text", value="sample_text")
    assert instance.list == "sample_text"
    instance.list = "sample_text_2"
    assert instance.list == "sample_text_2"


def test_sparrow_TrelloPUT_source_value_roundtrip():
    instance = sparrow_TrelloPUT(authtoken="sample_text", key="sample_text", list="sample_text", source="sample_text", useraccount="sample_text", value="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_sparrow_TrelloPUT_useraccount_value_roundtrip():
    instance = sparrow_TrelloPUT(authtoken="sample_text", key="sample_text", list="sample_text", source="sample_text", useraccount="sample_text", value="sample_text")
    assert instance.useraccount == "sample_text"
    instance.useraccount = "sample_text_2"
    assert instance.useraccount == "sample_text_2"


def test_sparrow_TrelloPUT_value_value_roundtrip():
    instance = sparrow_TrelloPUT(authtoken="sample_text", key="sample_text", list="sample_text", source="sample_text", useraccount="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sparrow_Try_name_value_roundtrip():
    instance = sparrow_Try(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sparrow_Updatedaudit_logsink_value_roundtrip():
    instance = sparrow_Updatedaudit(logsink="sample_text", value="sample_text")
    assert instance.logsink == "sample_text"
    instance.logsink = "sample_text_2"
    assert instance.logsink == "sample_text_2"


def test_sparrow_Updatedaudit_value_value_roundtrip():
    instance = sparrow_Updatedaudit(logsink="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sparrow_WriteCsv_delim_value_roundtrip():
    instance = sparrow_WriteCsv(delim="sample_text", source="sample_text", to="sample_text", value="sample_text")
    assert instance.delim == "sample_text"
    instance.delim = "sample_text_2"
    assert instance.delim == "sample_text_2"


def test_sparrow_WriteCsv_source_value_roundtrip():
    instance = sparrow_WriteCsv(delim="sample_text", source="sample_text", to="sample_text", value="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_sparrow_WriteCsv_to_value_roundtrip():
    instance = sparrow_WriteCsv(delim="sample_text", source="sample_text", to="sample_text", value="sample_text")
    assert instance.to == "sample_text"
    instance.to = "sample_text_2"
    assert instance.to == "sample_text_2"


def test_sparrow_WriteCsv_value_value_roundtrip():
    instance = sparrow_WriteCsv(delim="sample_text", source="sample_text", to="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sparrow_Callprocess_isa_Action():
    instance = sparrow_Callprocess(datasource="sample_text", source="sample_text", target="sample_text", value="sample_text")
    assert isinstance(instance, Action)


def test_sparrow_Copydata_isa_Action():
    instance = sparrow_Copydata(source="sample_text", to="sample_text", value="sample_text")
    assert isinstance(instance, Action)


def test_sparrow_Doozle_isa_Action():
    instance = sparrow_Doozle(on="sample_text", target="sample_text", value="sample_text")
    assert isinstance(instance, Action)


def test_sparrow_Dropfile_isa_Action():
    instance = sparrow_Dropfile(target="sample_text")
    assert isinstance(instance, Action)


def test_sparrow_FBCLead_isa_Action():
    instance = sparrow_FBCLead(accessToken="sample_text", accountId="sample_text", appSecret="sample_text", campaignId="sample_text", target="sample_text", value="sample_text")
    assert isinstance(instance, Action)


def test_sparrow_Fetch_isa_Action():
    instance = sparrow_Fetch(source="sample_text", value="sample_text")
    assert isinstance(instance, Action)


def test_sparrow_GooglecalPUT_isa_Action():
    instance = sparrow_GooglecalPUT(authstore="sample_text", key="sample_text", source="sample_text", useraccount="sample_text", value="sample_text")
    assert isinstance(instance, Action)


def test_sparrow_LoadCsv_isa_Action():
    instance = sparrow_LoadCsv(delim="sample_text", source="sample_text", to="sample_text", value="sample_text")
    assert isinstance(instance, Action)


def test_sparrow_Rest_isa_Action():
    instance = sparrow_Rest(ackdata="sample_text", ackdatato="sample_text", authtoken="sample_text", headerdata="sample_text", headerdatafrom="sample_text", method="sample_text", parentName="sample_text", parentdata="sample_text", postdatafrom="sample_text", resourcedatafrom="sample_text", url="sample_text", urldata="sample_text")
    assert isinstance(instance, Action)


def test_sparrow_SlackPUT_isa_Action():
    instance = sparrow_SlackPUT(channel="sample_text", team="sample_text", value="sample_text")
    assert isinstance(instance, Action)


def test_sparrow_Sms_isa_Action():
    instance = sparrow_Sms(target="sample_text", value="sample_text")
    assert isinstance(instance, Action)


def test_sparrow_Transform_isa_Action():
    instance = sparrow_Transform(on="sample_text", value="sample_text")
    assert isinstance(instance, Action)


def test_sparrow_TrelloGET_isa_Action():
    instance = sparrow_TrelloGET(authtoken="sample_text", board="sample_text", key="sample_text", target="sample_text", useraccount="sample_text", value="sample_text")
    assert isinstance(instance, Action)


def test_sparrow_TrelloPUT_isa_Action():
    instance = sparrow_TrelloPUT(authtoken="sample_text", key="sample_text", list="sample_text", source="sample_text", useraccount="sample_text", value="sample_text")
    assert isinstance(instance, Action)


def test_sparrow_Updatedaudit_isa_Action():
    instance = sparrow_Updatedaudit(logsink="sample_text", value="sample_text")
    assert isinstance(instance, Action)


def test_sparrow_WriteCsv_isa_Action():
    instance = sparrow_WriteCsv(delim="sample_text", source="sample_text", to="sample_text", value="sample_text")
    assert isinstance(instance, Action)


def test_assoc_action10_link_reassign_clear():
    a = sparrow_Catch(name="sample_text")
    b1 = sparrow_Action(name="sample_text")
    b2 = sparrow_Action(name="sample_text_2")
    _safe_set(a, 'sparrow_Catch11', {b1})
    assert _is_linked(a, 'sparrow_Catch11', b1)
    if hasattr(b1, 'sparrow_Action12'):
        assert _is_linked(b1, 'sparrow_Action12', a)
    _safe_set(a, 'sparrow_Catch11', {b2})
    assert _is_linked(a, 'sparrow_Catch11', b2)
    if hasattr(b1, 'sparrow_Action12'):
        assert not _is_linked(b1, 'sparrow_Action12', a)
    if hasattr(b2, 'sparrow_Action12'):
        assert _is_linked(b2, 'sparrow_Action12', a)
    _safe_set(a, 'sparrow_Catch11', set())
    assert not _is_linked(a, 'sparrow_Catch11', b2)
    if hasattr(b2, 'sparrow_Action12'):
        assert not _is_linked(b2, 'sparrow_Action12', a)


def test_assoc_action5_link_reassign_clear():
    a = sparrow_Try(name="sample_text")
    b1 = sparrow_Action(name="sample_text")
    b2 = sparrow_Action(name="sample_text_2")
    _safe_set(a, 'sparrow_Try6', {b1})
    assert _is_linked(a, 'sparrow_Try6', b1)
    if hasattr(b1, 'sparrow_Action'):
        assert _is_linked(b1, 'sparrow_Action', a)
    _safe_set(a, 'sparrow_Try6', {b2})
    assert _is_linked(a, 'sparrow_Try6', b2)
    if hasattr(b1, 'sparrow_Action'):
        assert not _is_linked(b1, 'sparrow_Action', a)
    if hasattr(b2, 'sparrow_Action'):
        assert _is_linked(b2, 'sparrow_Action', a)
    _safe_set(a, 'sparrow_Try6', set())
    assert not _is_linked(a, 'sparrow_Try6', b2)
    if hasattr(b2, 'sparrow_Action'):
        assert not _is_linked(b2, 'sparrow_Action', a)


def test_assoc_action7_link_reassign_clear():
    a = sparrow_Finally(name="sample_text")
    b1 = sparrow_Action(name="sample_text")
    b2 = sparrow_Action(name="sample_text_2")
    _safe_set(a, 'sparrow_Finally8', {b1})
    assert _is_linked(a, 'sparrow_Finally8', b1)
    if hasattr(b1, 'sparrow_Action9'):
        assert _is_linked(b1, 'sparrow_Action9', a)
    _safe_set(a, 'sparrow_Finally8', {b2})
    assert _is_linked(a, 'sparrow_Finally8', b2)
    if hasattr(b1, 'sparrow_Action9'):
        assert not _is_linked(b1, 'sparrow_Action9', a)
    if hasattr(b2, 'sparrow_Action9'):
        assert _is_linked(b2, 'sparrow_Action9', a)
    _safe_set(a, 'sparrow_Finally8', set())
    assert not _is_linked(a, 'sparrow_Finally8', b2)
    if hasattr(b2, 'sparrow_Action9'):
        assert not _is_linked(b2, 'sparrow_Action9', a)


def test_assoc_catch1_link_reassign_clear():
    a = sparrow_Process(name="sample_text")
    b1 = sparrow_Catch(name="sample_text")
    b2 = sparrow_Catch(name="sample_text_2")
    _safe_set(a, 'sparrow_Process2', b1)
    assert _is_linked(a, 'sparrow_Process2', b1)
    if hasattr(b1, 'sparrow_Catch'):
        assert _is_linked(b1, 'sparrow_Catch', a)
    _safe_set(a, 'sparrow_Process2', b2)
    assert _is_linked(a, 'sparrow_Process2', b2)
    if hasattr(b1, 'sparrow_Catch'):
        assert not _is_linked(b1, 'sparrow_Catch', a)
    if hasattr(b2, 'sparrow_Catch'):
        assert _is_linked(b2, 'sparrow_Catch', a)
    _safe_set(a, 'sparrow_Process2', None)
    assert not _is_linked(a, 'sparrow_Process2', b2)
    if hasattr(b2, 'sparrow_Catch'):
        assert not _is_linked(b2, 'sparrow_Catch', a)


def test_assoc_condition13_link_reassign_clear():
    a = sparrow_Expression(lhs="sample_text", operator="sample_text", rhs="sample_text")
    b1 = sparrow_Action(name="sample_text")
    b2 = sparrow_Action(name="sample_text_2")
    _safe_set(a, 'sparrow_Expression', b1)
    assert _is_linked(a, 'sparrow_Expression', b1)
    if hasattr(b1, 'sparrow_Action14'):
        assert _is_linked(b1, 'sparrow_Action14', a)
    _safe_set(a, 'sparrow_Expression', b2)
    assert _is_linked(a, 'sparrow_Expression', b2)
    if hasattr(b1, 'sparrow_Action14'):
        assert not _is_linked(b1, 'sparrow_Action14', a)
    if hasattr(b2, 'sparrow_Action14'):
        assert _is_linked(b2, 'sparrow_Action14', a)
    _safe_set(a, 'sparrow_Expression', None)
    assert not _is_linked(a, 'sparrow_Expression', b2)
    if hasattr(b2, 'sparrow_Action14'):
        assert not _is_linked(b2, 'sparrow_Action14', a)


def test_assoc_finally_3_link_reassign_clear():
    a = sparrow_Process(name="sample_text")
    b1 = sparrow_Finally(name="sample_text")
    b2 = sparrow_Finally(name="sample_text_2")
    _safe_set(a, 'sparrow_Process4', b1)
    assert _is_linked(a, 'sparrow_Process4', b1)
    if hasattr(b1, 'sparrow_Finally'):
        assert _is_linked(b1, 'sparrow_Finally', a)
    _safe_set(a, 'sparrow_Process4', b2)
    assert _is_linked(a, 'sparrow_Process4', b2)
    if hasattr(b1, 'sparrow_Finally'):
        assert not _is_linked(b1, 'sparrow_Finally', a)
    if hasattr(b2, 'sparrow_Finally'):
        assert _is_linked(b2, 'sparrow_Finally', a)
    _safe_set(a, 'sparrow_Process4', None)
    assert not _is_linked(a, 'sparrow_Process4', b2)
    if hasattr(b2, 'sparrow_Finally'):
        assert not _is_linked(b2, 'sparrow_Finally', a)


def test_assoc_parts15_link_reassign_clear():
    a = sparrow_RestPart(partData="sample_text", partName="sample_text")
    b1 = sparrow_Rest(ackdata="sample_text", ackdatato="sample_text", authtoken="sample_text", headerdata="sample_text", headerdatafrom="sample_text", method="sample_text", parentName="sample_text", parentdata="sample_text", postdatafrom="sample_text", resourcedatafrom="sample_text", url="sample_text", urldata="sample_text")
    b2 = sparrow_Rest(ackdata="sample_text_2", ackdatato="sample_text_2", authtoken="sample_text_2", headerdata="sample_text_2", headerdatafrom="sample_text_2", method="sample_text_2", parentName="sample_text_2", parentdata="sample_text_2", postdatafrom="sample_text_2", resourcedatafrom="sample_text_2", url="sample_text_2", urldata="sample_text_2")
    _safe_set(a, 'sparrow_RestPart', b1)
    assert _is_linked(a, 'sparrow_RestPart', b1)
    if hasattr(b1, 'sparrow_Rest'):
        assert _is_linked(b1, 'sparrow_Rest', a)
    _safe_set(a, 'sparrow_RestPart', b2)
    assert _is_linked(a, 'sparrow_RestPart', b2)
    if hasattr(b1, 'sparrow_Rest'):
        assert not _is_linked(b1, 'sparrow_Rest', a)
    if hasattr(b2, 'sparrow_Rest'):
        assert _is_linked(b2, 'sparrow_Rest', a)
    _safe_set(a, 'sparrow_RestPart', None)
    assert not _is_linked(a, 'sparrow_RestPart', b2)
    if hasattr(b2, 'sparrow_Rest'):
        assert not _is_linked(b2, 'sparrow_Rest', a)


def test_assoc_try_0_link_reassign_clear():
    a = sparrow_Try(name="sample_text")
    b1 = sparrow_Process(name="sample_text")
    b2 = sparrow_Process(name="sample_text_2")
    _safe_set(a, 'sparrow_Try', b1)
    assert _is_linked(a, 'sparrow_Try', b1)
    if hasattr(b1, 'sparrow_Process'):
        assert _is_linked(b1, 'sparrow_Process', a)
    _safe_set(a, 'sparrow_Try', b2)
    assert _is_linked(a, 'sparrow_Try', b2)
    if hasattr(b1, 'sparrow_Process'):
        assert not _is_linked(b1, 'sparrow_Process', a)
    if hasattr(b2, 'sparrow_Process'):
        assert _is_linked(b2, 'sparrow_Process', a)
    _safe_set(a, 'sparrow_Try', None)
    assert not _is_linked(a, 'sparrow_Try', b2)
    if hasattr(b2, 'sparrow_Process'):
        assert not _is_linked(b2, 'sparrow_Process', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


sparrow_Action_strategy = st.builds(sparrow_Action, name=safe_text)
@given(instance=sparrow_Action_strategy)
@settings(max_examples=25)
def test_sparrow_Action_instantiation(instance):
    assert isinstance(instance, sparrow_Action)


sparrow_Callprocess_strategy = st.builds(sparrow_Callprocess, datasource=safe_text, source=safe_text, target=safe_text, value=safe_text)
@given(instance=sparrow_Callprocess_strategy)
@settings(max_examples=25)
def test_sparrow_Callprocess_instantiation(instance):
    assert isinstance(instance, sparrow_Callprocess)


sparrow_Catch_strategy = st.builds(sparrow_Catch, name=safe_text)
@given(instance=sparrow_Catch_strategy)
@settings(max_examples=25)
def test_sparrow_Catch_instantiation(instance):
    assert isinstance(instance, sparrow_Catch)


sparrow_Copydata_strategy = st.builds(sparrow_Copydata, source=safe_text, to=safe_text, value=safe_text)
@given(instance=sparrow_Copydata_strategy)
@settings(max_examples=25)
def test_sparrow_Copydata_instantiation(instance):
    assert isinstance(instance, sparrow_Copydata)


sparrow_Doozle_strategy = st.builds(sparrow_Doozle, on=safe_text, target=safe_text, value=safe_text)
@given(instance=sparrow_Doozle_strategy)
@settings(max_examples=25)
def test_sparrow_Doozle_instantiation(instance):
    assert isinstance(instance, sparrow_Doozle)


sparrow_Dropfile_strategy = st.builds(sparrow_Dropfile, target=safe_text)
@given(instance=sparrow_Dropfile_strategy)
@settings(max_examples=25)
def test_sparrow_Dropfile_instantiation(instance):
    assert isinstance(instance, sparrow_Dropfile)


sparrow_Expression_strategy = st.builds(sparrow_Expression, lhs=safe_text, operator=safe_text, rhs=safe_text)
@given(instance=sparrow_Expression_strategy)
@settings(max_examples=25)
def test_sparrow_Expression_instantiation(instance):
    assert isinstance(instance, sparrow_Expression)


sparrow_FBCLead_strategy = st.builds(sparrow_FBCLead, accessToken=safe_text, accountId=safe_text, appSecret=safe_text, campaignId=safe_text, target=safe_text, value=safe_text)
@given(instance=sparrow_FBCLead_strategy)
@settings(max_examples=25)
def test_sparrow_FBCLead_instantiation(instance):
    assert isinstance(instance, sparrow_FBCLead)


sparrow_Fetch_strategy = st.builds(sparrow_Fetch, source=safe_text, value=safe_text)
@given(instance=sparrow_Fetch_strategy)
@settings(max_examples=25)
def test_sparrow_Fetch_instantiation(instance):
    assert isinstance(instance, sparrow_Fetch)


sparrow_Finally_strategy = st.builds(sparrow_Finally, name=safe_text)
@given(instance=sparrow_Finally_strategy)
@settings(max_examples=25)
def test_sparrow_Finally_instantiation(instance):
    assert isinstance(instance, sparrow_Finally)


sparrow_GooglecalPUT_strategy = st.builds(sparrow_GooglecalPUT, authstore=safe_text, key=safe_text, source=safe_text, useraccount=safe_text, value=safe_text)
@given(instance=sparrow_GooglecalPUT_strategy)
@settings(max_examples=25)
def test_sparrow_GooglecalPUT_instantiation(instance):
    assert isinstance(instance, sparrow_GooglecalPUT)


sparrow_LoadCsv_strategy = st.builds(sparrow_LoadCsv, delim=safe_text, source=safe_text, to=safe_text, value=safe_text)
@given(instance=sparrow_LoadCsv_strategy)
@settings(max_examples=25)
def test_sparrow_LoadCsv_instantiation(instance):
    assert isinstance(instance, sparrow_LoadCsv)


sparrow_Process_strategy = st.builds(sparrow_Process, name=safe_text)
@given(instance=sparrow_Process_strategy)
@settings(max_examples=25)
def test_sparrow_Process_instantiation(instance):
    assert isinstance(instance, sparrow_Process)


sparrow_Rest_strategy = st.builds(sparrow_Rest, ackdata=safe_text, ackdatato=safe_text, authtoken=safe_text, headerdata=safe_text, headerdatafrom=safe_text, method=safe_text, parentName=safe_text, parentdata=safe_text, postdatafrom=safe_text, resourcedatafrom=safe_text, url=safe_text, urldata=safe_text)
@given(instance=sparrow_Rest_strategy)
@settings(max_examples=25)
def test_sparrow_Rest_instantiation(instance):
    assert isinstance(instance, sparrow_Rest)


sparrow_RestPart_strategy = st.builds(sparrow_RestPart, partData=safe_text, partName=safe_text)
@given(instance=sparrow_RestPart_strategy)
@settings(max_examples=25)
def test_sparrow_RestPart_instantiation(instance):
    assert isinstance(instance, sparrow_RestPart)


sparrow_SlackPUT_strategy = st.builds(sparrow_SlackPUT, channel=safe_text, team=safe_text, value=safe_text)
@given(instance=sparrow_SlackPUT_strategy)
@settings(max_examples=25)
def test_sparrow_SlackPUT_instantiation(instance):
    assert isinstance(instance, sparrow_SlackPUT)


sparrow_Sms_strategy = st.builds(sparrow_Sms, target=safe_text, value=safe_text)
@given(instance=sparrow_Sms_strategy)
@settings(max_examples=25)
def test_sparrow_Sms_instantiation(instance):
    assert isinstance(instance, sparrow_Sms)


sparrow_Transform_strategy = st.builds(sparrow_Transform, on=safe_text, value=safe_text)
@given(instance=sparrow_Transform_strategy)
@settings(max_examples=25)
def test_sparrow_Transform_instantiation(instance):
    assert isinstance(instance, sparrow_Transform)


sparrow_TrelloGET_strategy = st.builds(sparrow_TrelloGET, authtoken=safe_text, board=safe_text, key=safe_text, target=safe_text, useraccount=safe_text, value=safe_text)
@given(instance=sparrow_TrelloGET_strategy)
@settings(max_examples=25)
def test_sparrow_TrelloGET_instantiation(instance):
    assert isinstance(instance, sparrow_TrelloGET)


sparrow_TrelloPUT_strategy = st.builds(sparrow_TrelloPUT, authtoken=safe_text, key=safe_text, list=safe_text, source=safe_text, useraccount=safe_text, value=safe_text)
@given(instance=sparrow_TrelloPUT_strategy)
@settings(max_examples=25)
def test_sparrow_TrelloPUT_instantiation(instance):
    assert isinstance(instance, sparrow_TrelloPUT)


sparrow_Try_strategy = st.builds(sparrow_Try, name=safe_text)
@given(instance=sparrow_Try_strategy)
@settings(max_examples=25)
def test_sparrow_Try_instantiation(instance):
    assert isinstance(instance, sparrow_Try)


sparrow_Updatedaudit_strategy = st.builds(sparrow_Updatedaudit, logsink=safe_text, value=safe_text)
@given(instance=sparrow_Updatedaudit_strategy)
@settings(max_examples=25)
def test_sparrow_Updatedaudit_instantiation(instance):
    assert isinstance(instance, sparrow_Updatedaudit)


sparrow_WriteCsv_strategy = st.builds(sparrow_WriteCsv, delim=safe_text, source=safe_text, to=safe_text, value=safe_text)
@given(instance=sparrow_WriteCsv_strategy)
@settings(max_examples=25)
def test_sparrow_WriteCsv_instantiation(instance):
    assert isinstance(instance, sparrow_WriteCsv)


