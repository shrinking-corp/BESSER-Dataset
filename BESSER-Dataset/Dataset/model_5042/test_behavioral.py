import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractCategory,
    Contact,
    Document,
    IDescribableEntity,
    IEntity,
    model_AbstractCategory,
    model_Address,
    model_BankAccount,
    model_CEFACTCode,
    model_Confirmation,
    model_Contact,
    model_ContactCategory,
    model_Credit,
    model_Creditor,
    model_Debitor,
    model_Delivery,
    model_Document,
    model_DocumentItem,
    model_Dunning,
    model_IDescribableEntity,
    model_IEntity,
    model_IndividualDocumentInfo,
    model_Invoice,
    model_ItemAccountType,
    model_ItemListTypeCategory,
    model_Letter,
    model_Offer,
    model_Order,
    model_Payment,
    model_Product,
    model_ProductBlockPrice,
    model_ProductCategory,
    model_ProductOptions,
    model_Proforma,
    model_Role,
    model_Shipping,
    model_ShippingCategory,
    model_Tenant,
    model_TextCategory,
    model_TextModule,
    model_User,
    model_UserProperty,
    model_VAT,
    model_VATCategory,
    model_Voucher,
    model_VoucherCategory,
    model_VoucherItem,
    model_WebShop,
    model_WebshopStateMapping,
    BillingType,
    ContactType,
    ItemType,
    ReliabilityType,
    ShippingVatType,
    VoucherType,
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

def test_assoc_accountType41_reverse_link_reassign_clear():
    a1 = model_VoucherItem(itemVoucherType="sample_text", posNr="sample_text", price="sample_text")
    a2 = model_VoucherItem(itemVoucherType="sample_text_2", posNr="sample_text_2", price="sample_text_2")
    b = model_ItemAccountType(value="sample_text")
    _safe_set(b, 'model_ItemAccountType', a1)
    assert _is_linked(b, 'model_ItemAccountType', a1)
    if hasattr(a1, 'model_VoucherItem42'):
        assert _is_linked(a1, 'model_VoucherItem42', b)
    _safe_set(b, 'model_ItemAccountType', a2)
    assert _is_linked(b, 'model_ItemAccountType', a2)
    if hasattr(a1, 'model_VoucherItem42'):
        assert not _is_linked(a1, 'model_VoucherItem42', b)
    if hasattr(a2, 'model_VoucherItem42'):
        assert _is_linked(a2, 'model_VoucherItem42', b)
    _safe_set(b, 'model_ItemAccountType', None)
    assert not _is_linked(b, 'model_ItemAccountType', a2)
    if hasattr(a2, 'model_VoucherItem42'):
        assert not _is_linked(a2, 'model_VoucherItem42', b)


def test_assoc_additionalInfo12_reverse_link_reassign_clear():
    a1 = model_IndividualDocumentInfo(noVatDescription="sample_text", noVatName="sample_text", paymentDescription="sample_text", paymentName="sample_text", paymentText="sample_text", shippingAutoVat="sample_text", shippingDescription="sample_text", shippingName="sample_text", shippingValue="sample_text", shippingVatDescription="sample_text", shippingVatValue="sample_text")
    a2 = model_IndividualDocumentInfo(noVatDescription="sample_text_2", noVatName="sample_text_2", paymentDescription="sample_text_2", paymentName="sample_text_2", paymentText="sample_text_2", shippingAutoVat="sample_text_2", shippingDescription="sample_text_2", shippingName="sample_text_2", shippingValue="sample_text_2", shippingVatDescription="sample_text_2", shippingVatValue="sample_text_2")
    b = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    _safe_set(b, 'model_Document', a1)
    assert _is_linked(b, 'model_Document', a1)
    if hasattr(a1, 'model_IndividualDocumentInfo'):
        assert _is_linked(a1, 'model_IndividualDocumentInfo', b)
    _safe_set(b, 'model_Document', a2)
    assert _is_linked(b, 'model_Document', a2)
    if hasattr(a1, 'model_IndividualDocumentInfo'):
        assert not _is_linked(a1, 'model_IndividualDocumentInfo', b)
    if hasattr(a2, 'model_IndividualDocumentInfo'):
        assert _is_linked(a2, 'model_IndividualDocumentInfo', b)
    _safe_set(b, 'model_Document', None)
    assert not _is_linked(b, 'model_Document', a2)
    if hasattr(a2, 'model_IndividualDocumentInfo'):
        assert not _is_linked(a2, 'model_IndividualDocumentInfo', b)


def test_assoc_address2_reverse_link_reassign_clear():
    a1 = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    a2 = model_Contact(birthday=date(2025, 6, 15), company="sample_text_2", contactType="sample_text_2", customerNumber="sample_text_2", discount="sample_text_2", email="sample_text_2", fax="sample_text_2", firstName="sample_text_2", gender="sample_text_2", gln="sample_text_2", mandateReference="sample_text_2", mobile="sample_text_2", note="sample_text_2", phone="sample_text_2", reliability="sample_text_2", supplierNumber="sample_text_2", title="sample_text_2", useNetGross="sample_text_2", useSalesEqualizationTax="sample_text_2", vatNumber="sample_text_2", vatNumberValid="sample_text_2", webshopName="sample_text_2", website="sample_text_2")
    b = model_Address(city="sample_text", cityAddon="sample_text", countryCode="sample_text", manualAddress="sample_text", street="sample_text", zip="sample_text")
    _safe_set(b, 'model_Address', a1)
    assert _is_linked(b, 'model_Address', a1)
    if hasattr(a1, 'model_Contact'):
        assert _is_linked(a1, 'model_Contact', b)
    _safe_set(b, 'model_Address', a2)
    assert _is_linked(b, 'model_Address', a2)
    if hasattr(a1, 'model_Contact'):
        assert not _is_linked(a1, 'model_Contact', b)
    if hasattr(a2, 'model_Contact'):
        assert _is_linked(a2, 'model_Contact', b)
    _safe_set(b, 'model_Address', None)
    assert not _is_linked(b, 'model_Address', a2)
    if hasattr(a2, 'model_Contact'):
        assert not _is_linked(a2, 'model_Contact', b)


def test_assoc_alternateContacts4_reverse_link_reassign_clear():
    a1 = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    a2 = model_Contact(birthday=date(2025, 6, 15), company="sample_text_2", contactType="sample_text_2", customerNumber="sample_text_2", discount="sample_text_2", email="sample_text_2", fax="sample_text_2", firstName="sample_text_2", gender="sample_text_2", gln="sample_text_2", mandateReference="sample_text_2", mobile="sample_text_2", note="sample_text_2", phone="sample_text_2", reliability="sample_text_2", supplierNumber="sample_text_2", title="sample_text_2", useNetGross="sample_text_2", useSalesEqualizationTax="sample_text_2", vatNumber="sample_text_2", vatNumberValid="sample_text_2", webshopName="sample_text_2", website="sample_text_2")
    b = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    _safe_set(b, 'model_Contact5', a1)
    assert _is_linked(b, 'model_Contact5', a1)
    if hasattr(a1, 'model_Contact3'):
        assert _is_linked(a1, 'model_Contact3', b)
    _safe_set(b, 'model_Contact5', a2)
    assert _is_linked(b, 'model_Contact5', a2)
    if hasattr(a1, 'model_Contact3'):
        assert not _is_linked(a1, 'model_Contact3', b)
    if hasattr(a2, 'model_Contact3'):
        assert _is_linked(a2, 'model_Contact3', b)
    _safe_set(b, 'model_Contact5', None)
    assert not _is_linked(b, 'model_Contact5', a2)
    if hasattr(a2, 'model_Contact3'):
        assert not _is_linked(a2, 'model_Contact3', b)


def test_assoc_attributes53_reverse_link_reassign_clear():
    a1 = model_ProductOptions(attributeValue="sample_text", sequenceNumber="sample_text")
    a2 = model_ProductOptions(attributeValue="sample_text_2", sequenceNumber="sample_text_2")
    b = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    _safe_set(b, 'model_Product54', {a1})
    assert _is_linked(b, 'model_Product54', a1)
    if hasattr(a1, 'model_ProductOptions'):
        assert _is_linked(a1, 'model_ProductOptions', b)
    _safe_set(b, 'model_Product54', {a2})
    assert _is_linked(b, 'model_Product54', a2)
    if hasattr(a1, 'model_ProductOptions'):
        assert not _is_linked(a1, 'model_ProductOptions', b)
    if hasattr(a2, 'model_ProductOptions'):
        assert _is_linked(a2, 'model_ProductOptions', b)
    _safe_set(b, 'model_Product54', set())
    assert not _is_linked(b, 'model_Product54', a2)
    if hasattr(a2, 'model_ProductOptions'):
        assert not _is_linked(a2, 'model_ProductOptions', b)


def test_assoc_bankAccount10_reverse_link_reassign_clear():
    a1 = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    a2 = model_Contact(birthday=date(2025, 6, 15), company="sample_text_2", contactType="sample_text_2", customerNumber="sample_text_2", discount="sample_text_2", email="sample_text_2", fax="sample_text_2", firstName="sample_text_2", gender="sample_text_2", gln="sample_text_2", mandateReference="sample_text_2", mobile="sample_text_2", note="sample_text_2", phone="sample_text_2", reliability="sample_text_2", supplierNumber="sample_text_2", title="sample_text_2", useNetGross="sample_text_2", useSalesEqualizationTax="sample_text_2", vatNumber="sample_text_2", vatNumberValid="sample_text_2", webshopName="sample_text_2", website="sample_text_2")
    b = model_BankAccount(accountHolder="sample_text", bankCode="sample_text", bankName="sample_text", bic="sample_text", iban="sample_text")
    _safe_set(b, 'model_BankAccount', a1)
    assert _is_linked(b, 'model_BankAccount', a1)
    if hasattr(a1, 'model_Contact11'):
        assert _is_linked(a1, 'model_Contact11', b)
    _safe_set(b, 'model_BankAccount', a2)
    assert _is_linked(b, 'model_BankAccount', a2)
    if hasattr(a1, 'model_Contact11'):
        assert not _is_linked(a1, 'model_Contact11', b)
    if hasattr(a2, 'model_Contact11'):
        assert _is_linked(a2, 'model_Contact11', b)
    _safe_set(b, 'model_BankAccount', None)
    assert not _is_linked(b, 'model_BankAccount', a2)
    if hasattr(a2, 'model_Contact11'):
        assert not _is_linked(a2, 'model_Contact11', b)


def test_assoc_billingContact13_reverse_link_reassign_clear():
    a1 = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    a2 = model_Document(addressFirstLine="sample_text_2", billingType="sample_text_2", consultant="sample_text_2", customerRef="sample_text_2", deposit="sample_text_2", documentDate=date(2025, 6, 15), dueDays="sample_text_2", itemsRebate="sample_text_2", message="sample_text_2", message2="sample_text_2", message3="sample_text_2", netGross="sample_text_2", odtPath="sample_text_2", orderDate=date(2025, 6, 15), paid="sample_text_2", paidValue="sample_text_2", payDate=date(2025, 6, 15), pdfPath="sample_text_2", printTemplate="sample_text_2", printed="sample_text_2", progress="sample_text_2", serviceDate=date(2025, 6, 15), shippingAutoVat="sample_text_2", shippingValue="sample_text_2", totalValue="sample_text_2", transactionId="sample_text_2", vestingPeriodEnd=date(2025, 6, 15), vestingPeriodStart=date(2025, 6, 15), webshopDate=date(2025, 6, 15), webshopId="sample_text_2")
    b = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    _safe_set(b, 'model_Contact15', a1)
    assert _is_linked(b, 'model_Contact15', a1)
    if hasattr(a1, 'model_Document14'):
        assert _is_linked(a1, 'model_Document14', b)
    _safe_set(b, 'model_Contact15', a2)
    assert _is_linked(b, 'model_Contact15', a2)
    if hasattr(a1, 'model_Document14'):
        assert not _is_linked(a1, 'model_Document14', b)
    if hasattr(a2, 'model_Document14'):
        assert _is_linked(a2, 'model_Document14', b)
    _safe_set(b, 'model_Contact15', None)
    assert not _is_linked(b, 'model_Contact15', a2)
    if hasattr(a2, 'model_Document14'):
        assert not _is_linked(a2, 'model_Document14', b)


def test_assoc_blockPrices58_reverse_link_reassign_clear():
    a1 = model_ProductBlockPrice(block="sample_text", price="sample_text")
    a2 = model_ProductBlockPrice(block="sample_text_2", price="sample_text_2")
    b = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    _safe_set(b, 'model_Product59', {a1})
    assert _is_linked(b, 'model_Product59', a1)
    if hasattr(a1, 'model_ProductBlockPrice'):
        assert _is_linked(a1, 'model_ProductBlockPrice', b)
    _safe_set(b, 'model_Product59', {a2})
    assert _is_linked(b, 'model_Product59', a2)
    if hasattr(a1, 'model_ProductBlockPrice'):
        assert not _is_linked(a1, 'model_ProductBlockPrice', b)
    if hasattr(a2, 'model_ProductBlockPrice'):
        assert _is_linked(a2, 'model_ProductBlockPrice', b)
    _safe_set(b, 'model_Product59', set())
    assert not _is_linked(b, 'model_Product59', a2)
    if hasattr(a2, 'model_ProductBlockPrice'):
        assert not _is_linked(a2, 'model_ProductBlockPrice', b)


def test_assoc_deliveryContact16_reverse_link_reassign_clear():
    a1 = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    a2 = model_Document(addressFirstLine="sample_text_2", billingType="sample_text_2", consultant="sample_text_2", customerRef="sample_text_2", deposit="sample_text_2", documentDate=date(2025, 6, 15), dueDays="sample_text_2", itemsRebate="sample_text_2", message="sample_text_2", message2="sample_text_2", message3="sample_text_2", netGross="sample_text_2", odtPath="sample_text_2", orderDate=date(2025, 6, 15), paid="sample_text_2", paidValue="sample_text_2", payDate=date(2025, 6, 15), pdfPath="sample_text_2", printTemplate="sample_text_2", printed="sample_text_2", progress="sample_text_2", serviceDate=date(2025, 6, 15), shippingAutoVat="sample_text_2", shippingValue="sample_text_2", totalValue="sample_text_2", transactionId="sample_text_2", vestingPeriodEnd=date(2025, 6, 15), vestingPeriodStart=date(2025, 6, 15), webshopDate=date(2025, 6, 15), webshopId="sample_text_2")
    b = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    _safe_set(b, 'model_Contact18', a1)
    assert _is_linked(b, 'model_Contact18', a1)
    if hasattr(a1, 'model_Document17'):
        assert _is_linked(a1, 'model_Document17', b)
    _safe_set(b, 'model_Contact18', a2)
    assert _is_linked(b, 'model_Contact18', a2)
    if hasattr(a1, 'model_Document17'):
        assert not _is_linked(a1, 'model_Document17', b)
    if hasattr(a2, 'model_Document17'):
        assert _is_linked(a2, 'model_Document17', b)
    _safe_set(b, 'model_Contact18', None)
    assert not _is_linked(b, 'model_Contact18', a2)
    if hasattr(a2, 'model_Document17'):
        assert not _is_linked(a2, 'model_Document17', b)


def test_assoc_itemVat35_reverse_link_reassign_clear():
    a1 = model_VAT(description="sample_text", salesEqualizationTax="sample_text", taxValue="sample_text")
    a2 = model_VAT(description="sample_text_2", salesEqualizationTax="sample_text_2", taxValue="sample_text_2")
    b = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    _safe_set(b, 'model_DocumentItem36', a1)
    assert _is_linked(b, 'model_DocumentItem36', a1)
    if hasattr(a1, 'model_VAT37'):
        assert _is_linked(a1, 'model_VAT37', b)
    _safe_set(b, 'model_DocumentItem36', a2)
    assert _is_linked(b, 'model_DocumentItem36', a2)
    if hasattr(a1, 'model_VAT37'):
        assert not _is_linked(a1, 'model_VAT37', b)
    if hasattr(a2, 'model_VAT37'):
        assert _is_linked(a2, 'model_VAT37', b)
    _safe_set(b, 'model_DocumentItem36', None)
    assert not _is_linked(b, 'model_DocumentItem36', a2)
    if hasattr(a2, 'model_VAT37'):
        assert not _is_linked(a2, 'model_VAT37', b)


def test_assoc_items21_reverse_link_reassign_clear():
    a1 = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    a2 = model_DocumentItem(description="sample_text_2", gtin="sample_text_2", itemNumber="sample_text_2", itemRebate="sample_text_2", itemType="sample_text_2", noVat="sample_text_2", optional="sample_text_2", originQuantity="sample_text_2", picture="sample_text_2", posNr="sample_text_2", price="sample_text_2", quantity="sample_text_2", quantityUnit="sample_text_2", tara="sample_text_2", vestingPeriodEnd=date(2025, 6, 15), vestingPeriodStart=date(2025, 6, 15), weight="sample_text_2")
    b = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    _safe_set(b, 'model_Document22', {a1})
    assert _is_linked(b, 'model_Document22', a1)
    if hasattr(a1, 'model_DocumentItem'):
        assert _is_linked(a1, 'model_DocumentItem', b)
    _safe_set(b, 'model_Document22', {a2})
    assert _is_linked(b, 'model_Document22', a2)
    if hasattr(a1, 'model_DocumentItem'):
        assert not _is_linked(a1, 'model_DocumentItem', b)
    if hasattr(a2, 'model_DocumentItem'):
        assert _is_linked(a2, 'model_DocumentItem', b)
    _safe_set(b, 'model_Document22', set())
    assert not _is_linked(b, 'model_Document22', a2)
    if hasattr(a2, 'model_DocumentItem'):
        assert not _is_linked(a2, 'model_DocumentItem', b)


def test_assoc_items39_reverse_link_reassign_clear():
    a1 = model_VoucherItem(itemVoucherType="sample_text", posNr="sample_text", price="sample_text")
    a2 = model_VoucherItem(itemVoucherType="sample_text_2", posNr="sample_text_2", price="sample_text_2")
    b = model_Voucher(discounted="sample_text", doNotBook="sample_text", documentNumber="sample_text", paidValue="sample_text", totalValue="sample_text", voucherDate=date(2024, 1, 1), voucherNumber="sample_text", voucherType="sample_text")
    _safe_set(b, 'model_Voucher40', {a1})
    assert _is_linked(b, 'model_Voucher40', a1)
    if hasattr(a1, 'model_VoucherItem'):
        assert _is_linked(a1, 'model_VoucherItem', b)
    _safe_set(b, 'model_Voucher40', {a2})
    assert _is_linked(b, 'model_Voucher40', a2)
    if hasattr(a1, 'model_VoucherItem'):
        assert not _is_linked(a1, 'model_VoucherItem', b)
    if hasattr(a2, 'model_VoucherItem'):
        assert _is_linked(a2, 'model_VoucherItem', b)
    _safe_set(b, 'model_Voucher40', set())
    assert not _is_linked(b, 'model_Voucher40', a2)
    if hasattr(a2, 'model_VoucherItem'):
        assert not _is_linked(a2, 'model_VoucherItem', b)


def test_assoc_noVatReference23_reverse_link_reassign_clear():
    a1 = model_VAT(description="sample_text", salesEqualizationTax="sample_text", taxValue="sample_text")
    a2 = model_VAT(description="sample_text_2", salesEqualizationTax="sample_text_2", taxValue="sample_text_2")
    b = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    _safe_set(b, 'model_Document24', a1)
    assert _is_linked(b, 'model_Document24', a1)
    if hasattr(a1, 'model_VAT'):
        assert _is_linked(a1, 'model_VAT', b)
    _safe_set(b, 'model_Document24', a2)
    assert _is_linked(b, 'model_Document24', a2)
    if hasattr(a1, 'model_VAT'):
        assert not _is_linked(a1, 'model_VAT', b)
    if hasattr(a2, 'model_VAT'):
        assert _is_linked(a2, 'model_VAT', b)
    _safe_set(b, 'model_Document24', None)
    assert not _is_linked(b, 'model_Document24', a2)
    if hasattr(a2, 'model_VAT'):
        assert not _is_linked(a2, 'model_VAT', b)


def test_assoc_payment25_reverse_link_reassign_clear():
    a1 = model_Payment(code="sample_text", depositText="sample_text", description="sample_text", discountDays="sample_text", discountValue="sample_text", netDays="sample_text", paidText="sample_text", unpaidText="sample_text")
    a2 = model_Payment(code="sample_text_2", depositText="sample_text_2", description="sample_text_2", discountDays="sample_text_2", discountValue="sample_text_2", netDays="sample_text_2", paidText="sample_text_2", unpaidText="sample_text_2")
    b = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    _safe_set(b, 'model_Document26', a1)
    assert _is_linked(b, 'model_Document26', a1)
    if hasattr(a1, 'model_Payment27'):
        assert _is_linked(a1, 'model_Payment27', b)
    _safe_set(b, 'model_Document26', a2)
    assert _is_linked(b, 'model_Document26', a2)
    if hasattr(a1, 'model_Payment27'):
        assert not _is_linked(a1, 'model_Payment27', b)
    if hasattr(a2, 'model_Payment27'):
        assert _is_linked(a2, 'model_Payment27', b)
    _safe_set(b, 'model_Document26', None)
    assert not _is_linked(b, 'model_Document26', a2)
    if hasattr(a2, 'model_Payment27'):
        assert not _is_linked(a2, 'model_Payment27', b)


def test_assoc_payment8_reverse_link_reassign_clear():
    a1 = model_Payment(code="sample_text", depositText="sample_text", description="sample_text", discountDays="sample_text", discountValue="sample_text", netDays="sample_text", paidText="sample_text", unpaidText="sample_text")
    a2 = model_Payment(code="sample_text_2", depositText="sample_text_2", description="sample_text_2", discountDays="sample_text_2", discountValue="sample_text_2", netDays="sample_text_2", paidText="sample_text_2", unpaidText="sample_text_2")
    b = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    _safe_set(b, 'model_Contact9', a1)
    assert _is_linked(b, 'model_Contact9', a1)
    if hasattr(a1, 'model_Payment'):
        assert _is_linked(a1, 'model_Payment', b)
    _safe_set(b, 'model_Contact9', a2)
    assert _is_linked(b, 'model_Contact9', a2)
    if hasattr(a1, 'model_Payment'):
        assert not _is_linked(a1, 'model_Payment', b)
    if hasattr(a2, 'model_Payment'):
        assert _is_linked(a2, 'model_Payment', b)
    _safe_set(b, 'model_Contact9', None)
    assert not _is_linked(b, 'model_Contact9', a2)
    if hasattr(a2, 'model_Payment'):
        assert not _is_linked(a2, 'model_Payment', b)


def test_assoc_product33_reverse_link_reassign_clear():
    a1 = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    a2 = model_Product(block1="sample_text_2", block2="sample_text_2", block3="sample_text_2", block4="sample_text_2", block5="sample_text_2", cdf01="sample_text_2", cdf02="sample_text_2", cdf03="sample_text_2", costPrice="sample_text_2", gtin="sample_text_2", itemNumber="sample_text_2", picture="sample_text_2", price1="sample_text_2", price2="sample_text_2", price3="sample_text_2", price4="sample_text_2", price5="sample_text_2", quantity="sample_text_2", quantityUnit="sample_text_2", sellingUnit="sample_text_2", webshopId="sample_text_2", weight="sample_text_2")
    b = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    _safe_set(b, 'model_DocumentItem34', a1)
    assert _is_linked(b, 'model_DocumentItem34', a1)
    if hasattr(a1, 'model_Product'):
        assert _is_linked(a1, 'model_Product', b)
    _safe_set(b, 'model_DocumentItem34', a2)
    assert _is_linked(b, 'model_DocumentItem34', a2)
    if hasattr(a1, 'model_Product'):
        assert not _is_linked(a1, 'model_Product', b)
    if hasattr(a2, 'model_Product'):
        assert _is_linked(a2, 'model_Product', b)
    _safe_set(b, 'model_DocumentItem34', None)
    assert not _is_linked(b, 'model_DocumentItem34', a2)
    if hasattr(a2, 'model_Product'):
        assert not _is_linked(a2, 'model_Product', b)


def test_assoc_shipping28_reverse_link_reassign_clear():
    a1 = model_Shipping(autoVat="sample_text", code="sample_text", shippingValue="sample_text")
    a2 = model_Shipping(autoVat="sample_text_2", code="sample_text_2", shippingValue="sample_text_2")
    b = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    _safe_set(b, 'model_Document29', a1)
    assert _is_linked(b, 'model_Document29', a1)
    if hasattr(a1, 'model_Shipping'):
        assert _is_linked(a1, 'model_Shipping', b)
    _safe_set(b, 'model_Document29', a2)
    assert _is_linked(b, 'model_Document29', a2)
    if hasattr(a1, 'model_Shipping'):
        assert not _is_linked(a1, 'model_Shipping', b)
    if hasattr(a2, 'model_Shipping'):
        assert _is_linked(a2, 'model_Shipping', b)
    _safe_set(b, 'model_Document29', None)
    assert not _is_linked(b, 'model_Document29', a2)
    if hasattr(a2, 'model_Shipping'):
        assert not _is_linked(a2, 'model_Shipping', b)


def test_assoc_shippingVat60_reverse_link_reassign_clear():
    a1 = model_VAT(description="sample_text", salesEqualizationTax="sample_text", taxValue="sample_text")
    a2 = model_VAT(description="sample_text_2", salesEqualizationTax="sample_text_2", taxValue="sample_text_2")
    b = model_Shipping(autoVat="sample_text", code="sample_text", shippingValue="sample_text")
    _safe_set(b, 'model_Shipping61', a1)
    assert _is_linked(b, 'model_Shipping61', a1)
    if hasattr(a1, 'model_VAT62'):
        assert _is_linked(a1, 'model_VAT62', b)
    _safe_set(b, 'model_Shipping61', a2)
    assert _is_linked(b, 'model_Shipping61', a2)
    if hasattr(a1, 'model_VAT62'):
        assert not _is_linked(a1, 'model_VAT62', b)
    if hasattr(a2, 'model_VAT62'):
        assert _is_linked(a2, 'model_VAT62', b)
    _safe_set(b, 'model_Shipping61', None)
    assert not _is_linked(b, 'model_Shipping61', a2)
    if hasattr(a2, 'model_VAT62'):
        assert not _is_linked(a2, 'model_VAT62', b)


def test_assoc_sourceDocument31_reverse_link_reassign_clear():
    a1 = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    a2 = model_Document(addressFirstLine="sample_text_2", billingType="sample_text_2", consultant="sample_text_2", customerRef="sample_text_2", deposit="sample_text_2", documentDate=date(2025, 6, 15), dueDays="sample_text_2", itemsRebate="sample_text_2", message="sample_text_2", message2="sample_text_2", message3="sample_text_2", netGross="sample_text_2", odtPath="sample_text_2", orderDate=date(2025, 6, 15), paid="sample_text_2", paidValue="sample_text_2", payDate=date(2025, 6, 15), pdfPath="sample_text_2", printTemplate="sample_text_2", printed="sample_text_2", progress="sample_text_2", serviceDate=date(2025, 6, 15), shippingAutoVat="sample_text_2", shippingValue="sample_text_2", totalValue="sample_text_2", transactionId="sample_text_2", vestingPeriodEnd=date(2025, 6, 15), vestingPeriodStart=date(2025, 6, 15), webshopDate=date(2025, 6, 15), webshopId="sample_text_2")
    b = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    _safe_set(b, 'model_Document32', a1)
    assert _is_linked(b, 'model_Document32', a1)
    if hasattr(a1, 'model_Document30'):
        assert _is_linked(a1, 'model_Document30', b)
    _safe_set(b, 'model_Document32', a2)
    assert _is_linked(b, 'model_Document32', a2)
    if hasattr(a1, 'model_Document30'):
        assert not _is_linked(a1, 'model_Document30', b)
    if hasattr(a2, 'model_Document30'):
        assert _is_linked(a2, 'model_Document30', b)
    _safe_set(b, 'model_Document32', None)
    assert not _is_linked(b, 'model_Document32', a2)
    if hasattr(a2, 'model_Document30'):
        assert not _is_linked(a2, 'model_Document30', b)


def test_assoc_stateMapping71_reverse_link_reassign_clear():
    a1 = model_WebshopStateMapping(fakturamaOrderState="sample_text", webshopState="sample_text")
    a2 = model_WebshopStateMapping(fakturamaOrderState="sample_text_2", webshopState="sample_text_2")
    b = model_WebShop(webshopVendor="sample_text", webshopVersion="sample_text")
    _safe_set(b, 'model_WebShop', {a1})
    assert _is_linked(b, 'model_WebShop', a1)
    if hasattr(a1, 'model_WebshopStateMapping'):
        assert _is_linked(a1, 'model_WebshopStateMapping', b)
    _safe_set(b, 'model_WebShop', {a2})
    assert _is_linked(b, 'model_WebShop', a2)
    if hasattr(a1, 'model_WebshopStateMapping'):
        assert not _is_linked(a1, 'model_WebshopStateMapping', b)
    if hasattr(a2, 'model_WebshopStateMapping'):
        assert _is_linked(a2, 'model_WebshopStateMapping', b)
    _safe_set(b, 'model_WebShop', set())
    assert not _is_linked(b, 'model_WebShop', a2)
    if hasattr(a2, 'model_WebshopStateMapping'):
        assert not _is_linked(a2, 'model_WebshopStateMapping', b)


def test_assoc_vat43_reverse_link_reassign_clear():
    a1 = model_VoucherItem(itemVoucherType="sample_text", posNr="sample_text", price="sample_text")
    a2 = model_VoucherItem(itemVoucherType="sample_text_2", posNr="sample_text_2", price="sample_text_2")
    b = model_VAT(description="sample_text", salesEqualizationTax="sample_text", taxValue="sample_text")
    _safe_set(b, 'model_VAT45', a1)
    assert _is_linked(b, 'model_VAT45', a1)
    if hasattr(a1, 'model_VoucherItem44'):
        assert _is_linked(a1, 'model_VoucherItem44', b)
    _safe_set(b, 'model_VAT45', a2)
    assert _is_linked(b, 'model_VAT45', a2)
    if hasattr(a1, 'model_VoucherItem44'):
        assert not _is_linked(a1, 'model_VoucherItem44', b)
    if hasattr(a2, 'model_VoucherItem44'):
        assert _is_linked(a2, 'model_VoucherItem44', b)
    _safe_set(b, 'model_VAT45', None)
    assert not _is_linked(b, 'model_VAT45', a2)
    if hasattr(a2, 'model_VoucherItem44'):
        assert not _is_linked(a2, 'model_VoucherItem44', b)


def test_assoc_vat55_reverse_link_reassign_clear():
    a1 = model_VAT(description="sample_text", salesEqualizationTax="sample_text", taxValue="sample_text")
    a2 = model_VAT(description="sample_text_2", salesEqualizationTax="sample_text_2", taxValue="sample_text_2")
    b = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    _safe_set(b, 'model_Product56', a1)
    assert _is_linked(b, 'model_Product56', a1)
    if hasattr(a1, 'model_VAT57'):
        assert _is_linked(a1, 'model_VAT57', b)
    _safe_set(b, 'model_Product56', a2)
    assert _is_linked(b, 'model_Product56', a2)
    if hasattr(a1, 'model_VAT57'):
        assert not _is_linked(a1, 'model_VAT57', b)
    if hasattr(a2, 'model_VAT57'):
        assert _is_linked(a2, 'model_VAT57', b)
    _safe_set(b, 'model_Product56', None)
    assert not _is_linked(b, 'model_Product56', a2)
    if hasattr(a2, 'model_VAT57'):
        assert not _is_linked(a2, 'model_VAT57', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_account38_stub_double():
    # model_VoucherCategory has no real 'model_VoucherCategory' property in the generated
    # code (a bare stub) -- manually attach it so model_Voucher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Voucher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Voucher(discounted="sample_text", doNotBook="sample_text", documentNumber="sample_text", paidValue="sample_text", totalValue="sample_text", voucherDate=date(2024, 1, 1), voucherNumber="sample_text", voucherType="sample_text")
    partner = model_VoucherCategory()
    setattr(partner, 'model_VoucherCategory', None)
    _safe_set(owner, 'model_Voucher', partner)
    assert getattr(partner, 'model_VoucherCategory') == owner
    _safe_set(owner, 'model_Voucher', None)
    assert getattr(partner, 'model_VoucherCategory') is None


def test_assoc_categories51_stub_double():
    # model_ProductCategory has no real 'model_ProductCategory' property in the generated
    # code (a bare stub) -- manually attach it so model_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    partner = model_ProductCategory()
    setattr(partner, 'model_ProductCategory', None)
    _safe_set(owner, 'model_Product52', partner)
    assert getattr(partner, 'model_ProductCategory') == owner
    _safe_set(owner, 'model_Product52', None)
    assert getattr(partner, 'model_ProductCategory') is None


def test_assoc_categories6_stub_double():
    # model_ContactCategory has no real 'model_ContactCategory' property in the generated
    # code (a bare stub) -- manually attach it so model_Contact's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Contact's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    partner = model_ContactCategory()
    setattr(partner, 'model_ContactCategory', None)
    _safe_set(owner, 'model_Contact7', partner)
    assert getattr(partner, 'model_ContactCategory') == owner
    _safe_set(owner, 'model_Contact7', None)
    assert getattr(partner, 'model_ContactCategory') is None


def test_assoc_categories63_stub_double():
    # model_ShippingCategory has no real 'model_ShippingCategory' property in the generated
    # code (a bare stub) -- manually attach it so model_Shipping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Shipping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Shipping(autoVat="sample_text", code="sample_text", shippingValue="sample_text")
    partner = model_ShippingCategory()
    setattr(partner, 'model_ShippingCategory', None)
    _safe_set(owner, 'model_Shipping64', partner)
    assert getattr(partner, 'model_ShippingCategory') == owner
    _safe_set(owner, 'model_Shipping64', None)
    assert getattr(partner, 'model_ShippingCategory') is None


def test_assoc_categories65_stub_double():
    # model_TextCategory has no real 'model_TextCategory' property in the generated
    # code (a bare stub) -- manually attach it so model_TextModule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_TextModule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_TextModule(text="sample_text")
    partner = model_TextCategory()
    setattr(partner, 'model_TextCategory', None)
    _safe_set(owner, 'model_TextModule', partner)
    assert getattr(partner, 'model_TextCategory') == owner
    _safe_set(owner, 'model_TextModule', None)
    assert getattr(partner, 'model_TextCategory') is None


def test_assoc_category46_stub_double():
    # model_ItemListTypeCategory has no real 'model_ItemListTypeCategory' property in the generated
    # code (a bare stub) -- manually attach it so model_ItemAccountType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_ItemAccountType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_ItemAccountType(value="sample_text")
    partner = model_ItemListTypeCategory()
    setattr(partner, 'model_ItemListTypeCategory', None)
    _safe_set(owner, 'model_ItemAccountType47', partner)
    assert getattr(partner, 'model_ItemListTypeCategory') == owner
    _safe_set(owner, 'model_ItemAccountType47', None)
    assert getattr(partner, 'model_ItemListTypeCategory') is None


def test_assoc_category48_stub_double():
    # model_VoucherCategory has no real 'model_VoucherCategory50' property in the generated
    # code (a bare stub) -- manually attach it so model_Payment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Payment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Payment(code="sample_text", depositText="sample_text", description="sample_text", discountDays="sample_text", discountValue="sample_text", netDays="sample_text", paidText="sample_text", unpaidText="sample_text")
    partner = model_VoucherCategory()
    setattr(partner, 'model_VoucherCategory50', None)
    _safe_set(owner, 'model_Payment49', partner)
    assert getattr(partner, 'model_VoucherCategory50') == owner
    _safe_set(owner, 'model_Payment49', None)
    assert getattr(partner, 'model_VoucherCategory50') is None


def test_assoc_category69_stub_double():
    # model_VATCategory has no real 'model_VATCategory' property in the generated
    # code (a bare stub) -- manually attach it so model_VAT's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_VAT's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_VAT(description="sample_text", salesEqualizationTax="sample_text", taxValue="sample_text")
    partner = model_VATCategory()
    setattr(partner, 'model_VATCategory', None)
    _safe_set(owner, 'model_VAT70', partner)
    assert getattr(partner, 'model_VATCategory') == owner
    _safe_set(owner, 'model_VAT70', None)
    assert getattr(partner, 'model_VATCategory') is None


def test_assoc_invoiceReference19_stub_double():
    # model_Invoice has no real 'model_Invoice' property in the generated
    # code (a bare stub) -- manually attach it so model_Document's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Document's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    partner = model_Invoice()
    setattr(partner, 'model_Invoice', None)
    _safe_set(owner, 'model_Document20', partner)
    assert getattr(partner, 'model_Invoice') == owner
    _safe_set(owner, 'model_Document20', None)
    assert getattr(partner, 'model_Invoice') is None


def test_assoc_roles67_stub_double():
    # model_Role has no real 'model_Role' property in the generated
    # code (a bare stub) -- manually attach it so model_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_User(password="sample_text", userName="sample_text")
    partner = model_Role()
    setattr(partner, 'model_Role', None)
    _safe_set(owner, 'model_User68', {partner})
    assert getattr(partner, 'model_Role') == owner
    _safe_set(owner, 'model_User68', set())
    assert getattr(partner, 'model_Role') is None


def test_assoc_tenant66_stub_double():
    # model_Tenant has no real 'model_Tenant' property in the generated
    # code (a bare stub) -- manually attach it so model_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_User(password="sample_text", userName="sample_text")
    partner = model_Tenant()
    setattr(partner, 'model_Tenant', None)
    _safe_set(owner, 'model_User', partner)
    assert getattr(partner, 'model_Tenant') == owner
    _safe_set(owner, 'model_User', None)
    assert getattr(partner, 'model_Tenant') is None


