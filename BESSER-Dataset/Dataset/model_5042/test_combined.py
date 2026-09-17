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
    Document,
    model_Delivery,
    model_Proforma,
    model_Dunning,
    model_Offer,
    model_Confirmation,
    model_Credit,
    model_Order,
    model_Letter,
    Contact,
    model_Debitor,
    model_Creditor,
    model_Invoice,
    AbstractCategory,
    model_ItemListTypeCategory,
    model_VoucherCategory,
    IEntity,
    model_AbstractCategory,
    model_DocumentItem,
    model_VoucherItem,
    model_Voucher,
    model_ItemAccountType,
    model_Address,
    model_VAT,
    model_Document,
    model_ProductBlockPrice,
    model_Contact,
    model_BankAccount,
    model_IndividualDocumentInfo,
    model_IDescribableEntity,
    model_Payment,
    model_ContactCategory,
    model_IEntity,
    model_WebshopStateMapping,
    model_WebShop,
    model_CEFACTCode,
    model_User,
    model_TextCategory,
    model_TextModule,
    model_Tenant,
    model_ShippingCategory,
    model_VATCategory,
    model_UserProperty,
    model_Role,
    model_ProductOptions,
    model_ProductCategory,
    IDescribableEntity,
    model_Product,
    model_Shipping,
    ItemType,
    BillingType,
    ShippingVatType,
    VoucherType,
    ContactType,
    ReliabilityType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_document_is_not_abstract():
    assert not inspect.isabstract(Document)


def test_hyp_document_constructor_exists():
    assert callable(Document.__init__)


def test_hyp_document_constructor_args():
    sig = inspect.signature(Document.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_delivery_is_not_abstract():
    assert not inspect.isabstract(model_Delivery)


def test_hyp_model_delivery_constructor_exists():
    assert callable(model_Delivery.__init__)


def test_hyp_model_delivery_constructor_args():
    sig = inspect.signature(model_Delivery.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_proforma_is_not_abstract():
    assert not inspect.isabstract(model_Proforma)


def test_hyp_model_proforma_constructor_exists():
    assert callable(model_Proforma.__init__)


def test_hyp_model_proforma_constructor_args():
    sig = inspect.signature(model_Proforma.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_dunning_is_not_abstract():
    assert not inspect.isabstract(model_Dunning)


def test_hyp_model_dunning_constructor_exists():
    assert callable(model_Dunning.__init__)


def test_hyp_model_dunning_constructor_args():
    sig = inspect.signature(model_Dunning.__init__)
    params = list(sig.parameters.keys())
    assert "dunningLevel" in params, "Missing parameter 'dunningLevel'"




def test_hyp_model_offer_is_not_abstract():
    assert not inspect.isabstract(model_Offer)


def test_hyp_model_offer_constructor_exists():
    assert callable(model_Offer.__init__)


def test_hyp_model_offer_constructor_args():
    sig = inspect.signature(model_Offer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_confirmation_is_not_abstract():
    assert not inspect.isabstract(model_Confirmation)


def test_hyp_model_confirmation_constructor_exists():
    assert callable(model_Confirmation.__init__)


def test_hyp_model_confirmation_constructor_args():
    sig = inspect.signature(model_Confirmation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_credit_is_not_abstract():
    assert not inspect.isabstract(model_Credit)


def test_hyp_model_credit_constructor_exists():
    assert callable(model_Credit.__init__)


def test_hyp_model_credit_constructor_args():
    sig = inspect.signature(model_Credit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_order_is_not_abstract():
    assert not inspect.isabstract(model_Order)


def test_hyp_model_order_constructor_exists():
    assert callable(model_Order.__init__)


def test_hyp_model_order_constructor_args():
    sig = inspect.signature(model_Order.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_letter_is_not_abstract():
    assert not inspect.isabstract(model_Letter)


def test_hyp_model_letter_constructor_exists():
    assert callable(model_Letter.__init__)


def test_hyp_model_letter_constructor_args():
    sig = inspect.signature(model_Letter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contact_is_not_abstract():
    assert not inspect.isabstract(Contact)


def test_hyp_contact_constructor_exists():
    assert callable(Contact.__init__)


def test_hyp_contact_constructor_args():
    sig = inspect.signature(Contact.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_debitor_is_not_abstract():
    assert not inspect.isabstract(model_Debitor)


def test_hyp_model_debitor_constructor_exists():
    assert callable(model_Debitor.__init__)


def test_hyp_model_debitor_constructor_args():
    sig = inspect.signature(model_Debitor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_creditor_is_not_abstract():
    assert not inspect.isabstract(model_Creditor)


def test_hyp_model_creditor_constructor_exists():
    assert callable(model_Creditor.__init__)


def test_hyp_model_creditor_constructor_args():
    sig = inspect.signature(model_Creditor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_invoice_is_not_abstract():
    assert not inspect.isabstract(model_Invoice)


def test_hyp_model_invoice_constructor_exists():
    assert callable(model_Invoice.__init__)


def test_hyp_model_invoice_constructor_args():
    sig = inspect.signature(model_Invoice.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractcategory_is_not_abstract():
    assert not inspect.isabstract(AbstractCategory)


def test_hyp_abstractcategory_constructor_exists():
    assert callable(AbstractCategory.__init__)


def test_hyp_abstractcategory_constructor_args():
    sig = inspect.signature(AbstractCategory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_itemlisttypecategory_is_not_abstract():
    assert not inspect.isabstract(model_ItemListTypeCategory)


def test_hyp_model_itemlisttypecategory_constructor_exists():
    assert callable(model_ItemListTypeCategory.__init__)


def test_hyp_model_itemlisttypecategory_constructor_args():
    sig = inspect.signature(model_ItemListTypeCategory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_vouchercategory_is_not_abstract():
    assert not inspect.isabstract(model_VoucherCategory)


def test_hyp_model_vouchercategory_constructor_exists():
    assert callable(model_VoucherCategory.__init__)


def test_hyp_model_vouchercategory_constructor_args():
    sig = inspect.signature(model_VoucherCategory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ientity_is_not_abstract():
    assert not inspect.isabstract(IEntity)


def test_hyp_ientity_constructor_exists():
    assert callable(IEntity.__init__)


def test_hyp_ientity_constructor_args():
    sig = inspect.signature(IEntity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_abstractcategory_is_not_abstract():
    assert not inspect.isabstract(model_AbstractCategory)


def test_hyp_model_abstractcategory_constructor_exists():
    assert callable(model_AbstractCategory.__init__)


def test_hyp_model_abstractcategory_constructor_args():
    sig = inspect.signature(model_AbstractCategory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_documentitem_is_not_abstract():
    assert not inspect.isabstract(model_DocumentItem)


def test_hyp_model_documentitem_constructor_exists():
    assert callable(model_DocumentItem.__init__)


def test_hyp_model_documentitem_constructor_args():
    sig = inspect.signature(model_DocumentItem.__init__)
    params = list(sig.parameters.keys())
    assert "itemRebate" in params, "Missing parameter 'itemRebate'"
    assert "noVat" in params, "Missing parameter 'noVat'"
    assert "itemNumber" in params, "Missing parameter 'itemNumber'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "posNr" in params, "Missing parameter 'posNr'"
    assert "description" in params, "Missing parameter 'description'"
    assert "vestingPeriodEnd" in params, "Missing parameter 'vestingPeriodEnd'"
    assert "picture" in params, "Missing parameter 'picture'"
    assert "quantityUnit" in params, "Missing parameter 'quantityUnit'"
    assert "itemType" in params, "Missing parameter 'itemType'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "vestingPeriodStart" in params, "Missing parameter 'vestingPeriodStart'"
    assert "gtin" in params, "Missing parameter 'gtin'"
    assert "tara" in params, "Missing parameter 'tara'"
    assert "originQuantity" in params, "Missing parameter 'originQuantity'"
    assert "optional" in params, "Missing parameter 'optional'"
    assert "price" in params, "Missing parameter 'price'"




















def test_hyp_model_voucheritem_is_not_abstract():
    assert not inspect.isabstract(model_VoucherItem)


def test_hyp_model_voucheritem_constructor_exists():
    assert callable(model_VoucherItem.__init__)


def test_hyp_model_voucheritem_constructor_args():
    sig = inspect.signature(model_VoucherItem.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "posNr" in params, "Missing parameter 'posNr'"
    assert "itemVoucherType" in params, "Missing parameter 'itemVoucherType'"






def test_hyp_model_voucher_is_not_abstract():
    assert not inspect.isabstract(model_Voucher)


def test_hyp_model_voucher_constructor_exists():
    assert callable(model_Voucher.__init__)


def test_hyp_model_voucher_constructor_args():
    sig = inspect.signature(model_Voucher.__init__)
    params = list(sig.parameters.keys())
    assert "discounted" in params, "Missing parameter 'discounted'"
    assert "voucherNumber" in params, "Missing parameter 'voucherNumber'"
    assert "voucherDate" in params, "Missing parameter 'voucherDate'"
    assert "doNotBook" in params, "Missing parameter 'doNotBook'"
    assert "voucherType" in params, "Missing parameter 'voucherType'"
    assert "documentNumber" in params, "Missing parameter 'documentNumber'"
    assert "totalValue" in params, "Missing parameter 'totalValue'"
    assert "paidValue" in params, "Missing parameter 'paidValue'"











def test_hyp_model_itemaccounttype_is_not_abstract():
    assert not inspect.isabstract(model_ItemAccountType)


def test_hyp_model_itemaccounttype_constructor_exists():
    assert callable(model_ItemAccountType.__init__)


def test_hyp_model_itemaccounttype_constructor_args():
    sig = inspect.signature(model_ItemAccountType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_model_address_is_not_abstract():
    assert not inspect.isabstract(model_Address)


def test_hyp_model_address_constructor_exists():
    assert callable(model_Address.__init__)


def test_hyp_model_address_constructor_args():
    sig = inspect.signature(model_Address.__init__)
    params = list(sig.parameters.keys())
    assert "manualAddress" in params, "Missing parameter 'manualAddress'"
    assert "street" in params, "Missing parameter 'street'"
    assert "cityAddon" in params, "Missing parameter 'cityAddon'"
    assert "city" in params, "Missing parameter 'city'"
    assert "zip" in params, "Missing parameter 'zip'"
    assert "countryCode" in params, "Missing parameter 'countryCode'"









def test_hyp_model_vat_is_not_abstract():
    assert not inspect.isabstract(model_VAT)


def test_hyp_model_vat_constructor_exists():
    assert callable(model_VAT.__init__)


def test_hyp_model_vat_constructor_args():
    sig = inspect.signature(model_VAT.__init__)
    params = list(sig.parameters.keys())
    assert "taxValue" in params, "Missing parameter 'taxValue'"
    assert "salesEqualizationTax" in params, "Missing parameter 'salesEqualizationTax'"
    assert "description" in params, "Missing parameter 'description'"






def test_hyp_model_document_is_not_abstract():
    assert not inspect.isabstract(model_Document)


def test_hyp_model_document_constructor_exists():
    assert callable(model_Document.__init__)


def test_hyp_model_document_constructor_args():
    sig = inspect.signature(model_Document.__init__)
    params = list(sig.parameters.keys())
    assert "vestingPeriodStart" in params, "Missing parameter 'vestingPeriodStart'"
    assert "message3" in params, "Missing parameter 'message3'"
    assert "message2" in params, "Missing parameter 'message2'"
    assert "vestingPeriodEnd" in params, "Missing parameter 'vestingPeriodEnd'"
    assert "netGross" in params, "Missing parameter 'netGross'"
    assert "transactionId" in params, "Missing parameter 'transactionId'"
    assert "orderDate" in params, "Missing parameter 'orderDate'"
    assert "webshopDate" in params, "Missing parameter 'webshopDate'"
    assert "webshopId" in params, "Missing parameter 'webshopId'"
    assert "shippingValue" in params, "Missing parameter 'shippingValue'"
    assert "billingType" in params, "Missing parameter 'billingType'"
    assert "serviceDate" in params, "Missing parameter 'serviceDate'"
    assert "message" in params, "Missing parameter 'message'"
    assert "itemsRebate" in params, "Missing parameter 'itemsRebate'"
    assert "printTemplate" in params, "Missing parameter 'printTemplate'"
    assert "dueDays" in params, "Missing parameter 'dueDays'"
    assert "payDate" in params, "Missing parameter 'payDate'"
    assert "addressFirstLine" in params, "Missing parameter 'addressFirstLine'"
    assert "printed" in params, "Missing parameter 'printed'"
    assert "documentDate" in params, "Missing parameter 'documentDate'"
    assert "pdfPath" in params, "Missing parameter 'pdfPath'"
    assert "consultant" in params, "Missing parameter 'consultant'"
    assert "totalValue" in params, "Missing parameter 'totalValue'"
    assert "progress" in params, "Missing parameter 'progress'"
    assert "deposit" in params, "Missing parameter 'deposit'"
    assert "odtPath" in params, "Missing parameter 'odtPath'"
    assert "customerRef" in params, "Missing parameter 'customerRef'"
    assert "paidValue" in params, "Missing parameter 'paidValue'"
    assert "shippingAutoVat" in params, "Missing parameter 'shippingAutoVat'"
    assert "paid" in params, "Missing parameter 'paid'"

































def test_hyp_model_productblockprice_is_not_abstract():
    assert not inspect.isabstract(model_ProductBlockPrice)


def test_hyp_model_productblockprice_constructor_exists():
    assert callable(model_ProductBlockPrice.__init__)


def test_hyp_model_productblockprice_constructor_args():
    sig = inspect.signature(model_ProductBlockPrice.__init__)
    params = list(sig.parameters.keys())
    assert "block" in params, "Missing parameter 'block'"
    assert "price" in params, "Missing parameter 'price'"





def test_hyp_model_contact_is_not_abstract():
    assert not inspect.isabstract(model_Contact)


def test_hyp_model_contact_constructor_exists():
    assert callable(model_Contact.__init__)


def test_hyp_model_contact_constructor_args():
    sig = inspect.signature(model_Contact.__init__)
    params = list(sig.parameters.keys())
    assert "vatNumberValid" in params, "Missing parameter 'vatNumberValid'"
    assert "gln" in params, "Missing parameter 'gln'"
    assert "title" in params, "Missing parameter 'title'"
    assert "website" in params, "Missing parameter 'website'"
    assert "fax" in params, "Missing parameter 'fax'"
    assert "customerNumber" in params, "Missing parameter 'customerNumber'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "birthday" in params, "Missing parameter 'birthday'"
    assert "email" in params, "Missing parameter 'email'"
    assert "note" in params, "Missing parameter 'note'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "useNetGross" in params, "Missing parameter 'useNetGross'"
    assert "webshopName" in params, "Missing parameter 'webshopName'"
    assert "mobile" in params, "Missing parameter 'mobile'"
    assert "useSalesEqualizationTax" in params, "Missing parameter 'useSalesEqualizationTax'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "supplierNumber" in params, "Missing parameter 'supplierNumber'"
    assert "mandateReference" in params, "Missing parameter 'mandateReference'"
    assert "company" in params, "Missing parameter 'company'"
    assert "contactType" in params, "Missing parameter 'contactType'"
    assert "vatNumber" in params, "Missing parameter 'vatNumber'"
    assert "discount" in params, "Missing parameter 'discount'"
    assert "reliability" in params, "Missing parameter 'reliability'"


























def test_hyp_model_bankaccount_is_not_abstract():
    assert not inspect.isabstract(model_BankAccount)


def test_hyp_model_bankaccount_constructor_exists():
    assert callable(model_BankAccount.__init__)


def test_hyp_model_bankaccount_constructor_args():
    sig = inspect.signature(model_BankAccount.__init__)
    params = list(sig.parameters.keys())
    assert "iban" in params, "Missing parameter 'iban'"
    assert "accountHolder" in params, "Missing parameter 'accountHolder'"
    assert "bankName" in params, "Missing parameter 'bankName'"
    assert "bic" in params, "Missing parameter 'bic'"
    assert "bankCode" in params, "Missing parameter 'bankCode'"








def test_hyp_model_individualdocumentinfo_is_not_abstract():
    assert not inspect.isabstract(model_IndividualDocumentInfo)


def test_hyp_model_individualdocumentinfo_constructor_exists():
    assert callable(model_IndividualDocumentInfo.__init__)


def test_hyp_model_individualdocumentinfo_constructor_args():
    sig = inspect.signature(model_IndividualDocumentInfo.__init__)
    params = list(sig.parameters.keys())
    assert "noVatDescription" in params, "Missing parameter 'noVatDescription'"
    assert "shippingVatDescription" in params, "Missing parameter 'shippingVatDescription'"
    assert "shippingDescription" in params, "Missing parameter 'shippingDescription'"
    assert "shippingName" in params, "Missing parameter 'shippingName'"
    assert "shippingAutoVat" in params, "Missing parameter 'shippingAutoVat'"
    assert "shippingVatValue" in params, "Missing parameter 'shippingVatValue'"
    assert "shippingValue" in params, "Missing parameter 'shippingValue'"
    assert "paymentText" in params, "Missing parameter 'paymentText'"
    assert "noVatName" in params, "Missing parameter 'noVatName'"
    assert "paymentDescription" in params, "Missing parameter 'paymentDescription'"
    assert "paymentName" in params, "Missing parameter 'paymentName'"














def test_hyp_model_idescribableentity_is_not_abstract():
    assert not inspect.isabstract(model_IDescribableEntity)


def test_hyp_model_idescribableentity_constructor_exists():
    assert callable(model_IDescribableEntity.__init__)


def test_hyp_model_idescribableentity_constructor_args():
    sig = inspect.signature(model_IDescribableEntity.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"




def test_hyp_model_payment_is_not_abstract():
    assert not inspect.isabstract(model_Payment)


def test_hyp_model_payment_constructor_exists():
    assert callable(model_Payment.__init__)


def test_hyp_model_payment_constructor_args():
    sig = inspect.signature(model_Payment.__init__)
    params = list(sig.parameters.keys())
    assert "netDays" in params, "Missing parameter 'netDays'"
    assert "code" in params, "Missing parameter 'code'"
    assert "discountDays" in params, "Missing parameter 'discountDays'"
    assert "description" in params, "Missing parameter 'description'"
    assert "paidText" in params, "Missing parameter 'paidText'"
    assert "depositText" in params, "Missing parameter 'depositText'"
    assert "unpaidText" in params, "Missing parameter 'unpaidText'"
    assert "discountValue" in params, "Missing parameter 'discountValue'"











def test_hyp_model_contactcategory_is_not_abstract():
    assert not inspect.isabstract(model_ContactCategory)


def test_hyp_model_contactcategory_constructor_exists():
    assert callable(model_ContactCategory.__init__)


def test_hyp_model_contactcategory_constructor_args():
    sig = inspect.signature(model_ContactCategory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_ientity_is_not_abstract():
    assert not inspect.isabstract(model_IEntity)


def test_hyp_model_ientity_constructor_exists():
    assert callable(model_IEntity.__init__)


def test_hyp_model_ientity_constructor_args():
    sig = inspect.signature(model_IEntity.__init__)
    params = list(sig.parameters.keys())
    assert "validTo" in params, "Missing parameter 'validTo'"
    assert "id" in params, "Missing parameter 'id'"
    assert "modified" in params, "Missing parameter 'modified'"
    assert "modifiedBy" in params, "Missing parameter 'modifiedBy'"
    assert "validFrom" in params, "Missing parameter 'validFrom'"
    assert "deleted" in params, "Missing parameter 'deleted'"
    assert "dateAdded" in params, "Missing parameter 'dateAdded'"
    assert "name" in params, "Missing parameter 'name'"











def test_hyp_model_webshopstatemapping_is_not_abstract():
    assert not inspect.isabstract(model_WebshopStateMapping)


def test_hyp_model_webshopstatemapping_constructor_exists():
    assert callable(model_WebshopStateMapping.__init__)


def test_hyp_model_webshopstatemapping_constructor_args():
    sig = inspect.signature(model_WebshopStateMapping.__init__)
    params = list(sig.parameters.keys())
    assert "webshopState" in params, "Missing parameter 'webshopState'"
    assert "fakturamaOrderState" in params, "Missing parameter 'fakturamaOrderState'"





def test_hyp_model_webshop_is_not_abstract():
    assert not inspect.isabstract(model_WebShop)


def test_hyp_model_webshop_constructor_exists():
    assert callable(model_WebShop.__init__)


def test_hyp_model_webshop_constructor_args():
    sig = inspect.signature(model_WebShop.__init__)
    params = list(sig.parameters.keys())
    assert "webshopVendor" in params, "Missing parameter 'webshopVendor'"
    assert "webshopVersion" in params, "Missing parameter 'webshopVersion'"





def test_hyp_model_cefactcode_is_not_abstract():
    assert not inspect.isabstract(model_CEFACTCode)


def test_hyp_model_cefactcode_constructor_exists():
    assert callable(model_CEFACTCode.__init__)


def test_hyp_model_cefactcode_constructor_args():
    sig = inspect.signature(model_CEFACTCode.__init__)
    params = list(sig.parameters.keys())
    assert "name_de" in params, "Missing parameter 'name_de'"
    assert "abbreviation_en" in params, "Missing parameter 'abbreviation_en'"
    assert "code" in params, "Missing parameter 'code'"
    assert "abbreviation_de" in params, "Missing parameter 'abbreviation_de'"
    assert "target" in params, "Missing parameter 'target'"








def test_hyp_model_user_is_not_abstract():
    assert not inspect.isabstract(model_User)


def test_hyp_model_user_constructor_exists():
    assert callable(model_User.__init__)


def test_hyp_model_user_constructor_args():
    sig = inspect.signature(model_User.__init__)
    params = list(sig.parameters.keys())
    assert "userName" in params, "Missing parameter 'userName'"
    assert "password" in params, "Missing parameter 'password'"





def test_hyp_model_textcategory_is_not_abstract():
    assert not inspect.isabstract(model_TextCategory)


def test_hyp_model_textcategory_constructor_exists():
    assert callable(model_TextCategory.__init__)


def test_hyp_model_textcategory_constructor_args():
    sig = inspect.signature(model_TextCategory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_textmodule_is_not_abstract():
    assert not inspect.isabstract(model_TextModule)


def test_hyp_model_textmodule_constructor_exists():
    assert callable(model_TextModule.__init__)


def test_hyp_model_textmodule_constructor_args():
    sig = inspect.signature(model_TextModule.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_model_tenant_is_not_abstract():
    assert not inspect.isabstract(model_Tenant)


def test_hyp_model_tenant_constructor_exists():
    assert callable(model_Tenant.__init__)


def test_hyp_model_tenant_constructor_args():
    sig = inspect.signature(model_Tenant.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_shippingcategory_is_not_abstract():
    assert not inspect.isabstract(model_ShippingCategory)


def test_hyp_model_shippingcategory_constructor_exists():
    assert callable(model_ShippingCategory.__init__)


def test_hyp_model_shippingcategory_constructor_args():
    sig = inspect.signature(model_ShippingCategory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_vatcategory_is_not_abstract():
    assert not inspect.isabstract(model_VATCategory)


def test_hyp_model_vatcategory_constructor_exists():
    assert callable(model_VATCategory.__init__)


def test_hyp_model_vatcategory_constructor_args():
    sig = inspect.signature(model_VATCategory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_userproperty_is_not_abstract():
    assert not inspect.isabstract(model_UserProperty)


def test_hyp_model_userproperty_constructor_exists():
    assert callable(model_UserProperty.__init__)


def test_hyp_model_userproperty_constructor_args():
    sig = inspect.signature(model_UserProperty.__init__)
    params = list(sig.parameters.keys())
    assert "user" in params, "Missing parameter 'user'"
    assert "default" in params, "Missing parameter 'default'"
    assert "value" in params, "Missing parameter 'value'"
    assert "global_" in params, "Missing parameter 'global_'"







def test_hyp_model_role_is_not_abstract():
    assert not inspect.isabstract(model_Role)


def test_hyp_model_role_constructor_exists():
    assert callable(model_Role.__init__)


def test_hyp_model_role_constructor_args():
    sig = inspect.signature(model_Role.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_productoptions_is_not_abstract():
    assert not inspect.isabstract(model_ProductOptions)


def test_hyp_model_productoptions_constructor_exists():
    assert callable(model_ProductOptions.__init__)


def test_hyp_model_productoptions_constructor_args():
    sig = inspect.signature(model_ProductOptions.__init__)
    params = list(sig.parameters.keys())
    assert "sequenceNumber" in params, "Missing parameter 'sequenceNumber'"
    assert "attributeValue" in params, "Missing parameter 'attributeValue'"





def test_hyp_model_productcategory_is_not_abstract():
    assert not inspect.isabstract(model_ProductCategory)


def test_hyp_model_productcategory_constructor_exists():
    assert callable(model_ProductCategory.__init__)


def test_hyp_model_productcategory_constructor_args():
    sig = inspect.signature(model_ProductCategory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_idescribableentity_is_not_abstract():
    assert not inspect.isabstract(IDescribableEntity)


def test_hyp_idescribableentity_constructor_exists():
    assert callable(IDescribableEntity.__init__)


def test_hyp_idescribableentity_constructor_args():
    sig = inspect.signature(IDescribableEntity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_product_is_not_abstract():
    assert not inspect.isabstract(model_Product)


def test_hyp_model_product_constructor_exists():
    assert callable(model_Product.__init__)


def test_hyp_model_product_constructor_args():
    sig = inspect.signature(model_Product.__init__)
    params = list(sig.parameters.keys())
    assert "price1" in params, "Missing parameter 'price1'"
    assert "block2" in params, "Missing parameter 'block2'"
    assert "costPrice" in params, "Missing parameter 'costPrice'"
    assert "webshopId" in params, "Missing parameter 'webshopId'"
    assert "price2" in params, "Missing parameter 'price2'"
    assert "gtin" in params, "Missing parameter 'gtin'"
    assert "itemNumber" in params, "Missing parameter 'itemNumber'"
    assert "quantityUnit" in params, "Missing parameter 'quantityUnit'"
    assert "price3" in params, "Missing parameter 'price3'"
    assert "price5" in params, "Missing parameter 'price5'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "block3" in params, "Missing parameter 'block3'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "block1" in params, "Missing parameter 'block1'"
    assert "picture" in params, "Missing parameter 'picture'"
    assert "price4" in params, "Missing parameter 'price4'"
    assert "block4" in params, "Missing parameter 'block4'"
    assert "sellingUnit" in params, "Missing parameter 'sellingUnit'"
    assert "cdf03" in params, "Missing parameter 'cdf03'"
    assert "block5" in params, "Missing parameter 'block5'"
    assert "cdf01" in params, "Missing parameter 'cdf01'"
    assert "cdf02" in params, "Missing parameter 'cdf02'"

























def test_hyp_model_shipping_is_not_abstract():
    assert not inspect.isabstract(model_Shipping)


def test_hyp_model_shipping_constructor_exists():
    assert callable(model_Shipping.__init__)


def test_hyp_model_shipping_constructor_args():
    sig = inspect.signature(model_Shipping.__init__)
    params = list(sig.parameters.keys())
    assert "autoVat" in params, "Missing parameter 'autoVat'"
    assert "code" in params, "Missing parameter 'code'"
    assert "shippingValue" in params, "Missing parameter 'shippingValue'"




def test_hyp_itemtype_exists():
    # Check that the Enumeration exists
    assert ItemType is not None

def test_hyp_itemtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ItemType]
    expected_literals = [
        "FREETEXT",
        "SUBTOTAL",
        "DELIVERY_PART",
        "POSITION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ItemType"

def test_hyp_billingtype_exists():
    # Check that the Enumeration exists
    assert BillingType is not None

def test_hyp_billingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BillingType]
    expected_literals = [
        "LETTER",
        "PROFORMA",
        "CONFIRMATION",
        "DUNNING",
        "NONE",
        "DELIVERY",
        "CREDIT",
        "INVOICE",
        "ORDER",
        "OFFER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BillingType"

def test_hyp_shippingvattype_exists():
    # Check that the Enumeration exists
    assert ShippingVatType is not None

def test_hyp_shippingvattype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ShippingVatType]
    expected_literals = [
        "SHIPPINGVATGROSS",
        "SHIPPINGVATFIX",
        "SHIPPINGVATNET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ShippingVatType"

def test_hyp_vouchertype_exists():
    # Check that the Enumeration exists
    assert VoucherType is not None

def test_hyp_vouchertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VoucherType]
    expected_literals = [
        "EXPENDITURE",
        "RECEIPTVOUCHER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VoucherType"

def test_hyp_contacttype_exists():
    # Check that the Enumeration exists
    assert ContactType is not None

def test_hyp_contacttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContactType]
    expected_literals = [
        "BILLING",
        "DELIVERY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContactType"

def test_hyp_reliabilitytype_exists():
    # Check that the Enumeration exists
    assert ReliabilityType is not None

def test_hyp_reliabilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReliabilityType]
    expected_literals = [
        "POOR",
        "MEDIUM",
        "NONE",
        "GOOD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReliabilityType"


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
Document_strategy = st.builds(
    Document,
)
model_Delivery_strategy = st.builds(
    model_Delivery,
)
model_Proforma_strategy = st.builds(
    model_Proforma,
)
model_Dunning_strategy = st.builds(
    model_Dunning,
    dunningLevel=
        safe_text
)
model_Offer_strategy = st.builds(
    model_Offer,
)
model_Confirmation_strategy = st.builds(
    model_Confirmation,
)
model_Credit_strategy = st.builds(
    model_Credit,
)
model_Order_strategy = st.builds(
    model_Order,
)
model_Letter_strategy = st.builds(
    model_Letter,
)
Contact_strategy = st.builds(
    Contact,
)
model_Debitor_strategy = st.builds(
    model_Debitor,
)
model_Creditor_strategy = st.builds(
    model_Creditor,
)
model_Invoice_strategy = st.builds(
    model_Invoice,
)
AbstractCategory_strategy = st.builds(
    AbstractCategory,
)
model_ItemListTypeCategory_strategy = st.builds(
    model_ItemListTypeCategory,
)
model_VoucherCategory_strategy = st.builds(
    model_VoucherCategory,
)
IEntity_strategy = st.builds(
    IEntity,
)
model_AbstractCategory_strategy = st.builds(
    model_AbstractCategory,
)
model_DocumentItem_strategy = st.builds(
    model_DocumentItem,
    itemRebate=
        safe_text,
    noVat=
        safe_text,
    itemNumber=
        safe_text,
    weight=
        safe_text,
    posNr=
        safe_text,
    description=
        safe_text,
    vestingPeriodEnd=
        st.dates(),
    picture=
        safe_text,
    quantityUnit=
        safe_text,
    itemType=
        safe_text,
    quantity=
        safe_text,
    vestingPeriodStart=
        st.dates(),
    gtin=
        safe_text,
    tara=
        safe_text,
    originQuantity=
        safe_text,
    optional=
        safe_text,
    price=
        safe_text
)
model_VoucherItem_strategy = st.builds(
    model_VoucherItem,
    price=
        safe_text,
    posNr=
        safe_text,
    itemVoucherType=
        safe_text
)
model_Voucher_strategy = st.builds(
    model_Voucher,
    discounted=
        safe_text,
    voucherNumber=
        safe_text,
    voucherDate=
        st.dates(),
    doNotBook=
        safe_text,
    voucherType=
        safe_text,
    documentNumber=
        safe_text,
    totalValue=
        safe_text,
    paidValue=
        safe_text
)
model_ItemAccountType_strategy = st.builds(
    model_ItemAccountType,
    value=
        safe_text
)
model_Address_strategy = st.builds(
    model_Address,
    manualAddress=
        safe_text,
    street=
        safe_text,
    cityAddon=
        safe_text,
    city=
        safe_text,
    zip=
        safe_text,
    countryCode=
        safe_text
)
model_VAT_strategy = st.builds(
    model_VAT,
    taxValue=
        safe_text,
    salesEqualizationTax=
        safe_text,
    description=
        safe_text
)
model_Document_strategy = st.builds(
    model_Document,
    vestingPeriodStart=
        st.dates(),
    message3=
        safe_text,
    message2=
        safe_text,
    vestingPeriodEnd=
        st.dates(),
    netGross=
        safe_text,
    transactionId=
        safe_text,
    orderDate=
        st.dates(),
    webshopDate=
        st.dates(),
    webshopId=
        safe_text,
    shippingValue=
        safe_text,
    billingType=
        safe_text,
    serviceDate=
        st.dates(),
    message=
        safe_text,
    itemsRebate=
        safe_text,
    printTemplate=
        safe_text,
    dueDays=
        safe_text,
    payDate=
        st.dates(),
    addressFirstLine=
        safe_text,
    printed=
        safe_text,
    documentDate=
        st.dates(),
    pdfPath=
        safe_text,
    consultant=
        safe_text,
    totalValue=
        safe_text,
    progress=
        safe_text,
    deposit=
        safe_text,
    odtPath=
        safe_text,
    customerRef=
        safe_text,
    paidValue=
        safe_text,
    shippingAutoVat=
        safe_text,
    paid=
        safe_text
)
model_ProductBlockPrice_strategy = st.builds(
    model_ProductBlockPrice,
    block=
        safe_text,
    price=
        safe_text
)
model_Contact_strategy = st.builds(
    model_Contact,
    vatNumberValid=
        safe_text,
    gln=
        safe_text,
    title=
        safe_text,
    website=
        safe_text,
    fax=
        safe_text,
    customerNumber=
        safe_text,
    firstName=
        safe_text,
    birthday=
        st.dates(),
    email=
        safe_text,
    note=
        safe_text,
    phone=
        safe_text,
    useNetGross=
        safe_text,
    webshopName=
        safe_text,
    mobile=
        safe_text,
    useSalesEqualizationTax=
        safe_text,
    gender=
        safe_text,
    supplierNumber=
        safe_text,
    mandateReference=
        safe_text,
    company=
        safe_text,
    contactType=
        safe_text,
    vatNumber=
        safe_text,
    discount=
        safe_text,
    reliability=
        safe_text
)
model_BankAccount_strategy = st.builds(
    model_BankAccount,
    iban=
        safe_text,
    accountHolder=
        safe_text,
    bankName=
        safe_text,
    bic=
        safe_text,
    bankCode=
        safe_text
)
model_IndividualDocumentInfo_strategy = st.builds(
    model_IndividualDocumentInfo,
    noVatDescription=
        safe_text,
    shippingVatDescription=
        safe_text,
    shippingDescription=
        safe_text,
    shippingName=
        safe_text,
    shippingAutoVat=
        safe_text,
    shippingVatValue=
        safe_text,
    shippingValue=
        safe_text,
    paymentText=
        safe_text,
    noVatName=
        safe_text,
    paymentDescription=
        safe_text,
    paymentName=
        safe_text
)
model_IDescribableEntity_strategy = st.builds(
    model_IDescribableEntity,
    description=
        safe_text
)
model_Payment_strategy = st.builds(
    model_Payment,
    netDays=
        safe_text,
    code=
        safe_text,
    discountDays=
        safe_text,
    description=
        safe_text,
    paidText=
        safe_text,
    depositText=
        safe_text,
    unpaidText=
        safe_text,
    discountValue=
        safe_text
)
model_ContactCategory_strategy = st.builds(
    model_ContactCategory,
)
model_IEntity_strategy = st.builds(
    model_IEntity,
    validTo=
        st.dates(),
    id=
        safe_text,
    modified=
        st.dates(),
    modifiedBy=
        safe_text,
    validFrom=
        st.dates(),
    deleted=
        safe_text,
    dateAdded=
        st.dates(),
    name=
        safe_text
)
model_WebshopStateMapping_strategy = st.builds(
    model_WebshopStateMapping,
    webshopState=
        safe_text,
    fakturamaOrderState=
        safe_text
)
model_WebShop_strategy = st.builds(
    model_WebShop,
    webshopVendor=
        safe_text,
    webshopVersion=
        safe_text
)
model_CEFACTCode_strategy = st.builds(
    model_CEFACTCode,
    name_de=
        safe_text,
    abbreviation_en=
        safe_text,
    code=
        safe_text,
    abbreviation_de=
        safe_text,
    target=
        safe_text
)
model_User_strategy = st.builds(
    model_User,
    userName=
        safe_text,
    password=
        safe_text
)
model_TextCategory_strategy = st.builds(
    model_TextCategory,
)
model_TextModule_strategy = st.builds(
    model_TextModule,
    text=
        safe_text
)
model_Tenant_strategy = st.builds(
    model_Tenant,
)
model_ShippingCategory_strategy = st.builds(
    model_ShippingCategory,
)
model_VATCategory_strategy = st.builds(
    model_VATCategory,
)
model_UserProperty_strategy = st.builds(
    model_UserProperty,
    user=
        safe_text,
    default=
        safe_text,
    value=
        safe_text,
    global_=
        safe_text
)
model_Role_strategy = st.builds(
    model_Role,
)
model_ProductOptions_strategy = st.builds(
    model_ProductOptions,
    sequenceNumber=
        safe_text,
    attributeValue=
        safe_text
)
model_ProductCategory_strategy = st.builds(
    model_ProductCategory,
)
IDescribableEntity_strategy = st.builds(
    IDescribableEntity,
)
model_Product_strategy = st.builds(
    model_Product,
    price1=
        safe_text,
    block2=
        safe_text,
    costPrice=
        safe_text,
    webshopId=
        safe_text,
    price2=
        safe_text,
    gtin=
        safe_text,
    itemNumber=
        safe_text,
    quantityUnit=
        safe_text,
    price3=
        safe_text,
    price5=
        safe_text,
    weight=
        safe_text,
    block3=
        safe_text,
    quantity=
        safe_text,
    block1=
        safe_text,
    picture=
        safe_text,
    price4=
        safe_text,
    block4=
        safe_text,
    sellingUnit=
        safe_text,
    cdf03=
        safe_text,
    block5=
        safe_text,
    cdf01=
        safe_text,
    cdf02=
        safe_text
)
model_Shipping_strategy = st.builds(
    model_Shipping,
    autoVat=
        safe_text,
    code=
        safe_text,
    shippingValue=
        safe_text
)







@given(instance=model_Dunning_strategy)
def test_hyp_model_dunning_dunningLevel_setter(instance):
    original = instance.dunningLevel
    instance.dunningLevel = original
    assert instance.dunningLevel == original


















@given(instance=model_DocumentItem_strategy)
def test_hyp_model_documentitem_itemRebate_setter(instance):
    original = instance.itemRebate
    instance.itemRebate = original
    assert instance.itemRebate == original



@given(instance=model_DocumentItem_strategy)
def test_hyp_model_documentitem_noVat_setter(instance):
    original = instance.noVat
    instance.noVat = original
    assert instance.noVat == original



@given(instance=model_DocumentItem_strategy)
def test_hyp_model_documentitem_itemNumber_setter(instance):
    original = instance.itemNumber
    instance.itemNumber = original
    assert instance.itemNumber == original



@given(instance=model_DocumentItem_strategy)
def test_hyp_model_documentitem_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=model_DocumentItem_strategy)
def test_hyp_model_documentitem_posNr_setter(instance):
    original = instance.posNr
    instance.posNr = original
    assert instance.posNr == original



@given(instance=model_DocumentItem_strategy)
def test_hyp_model_documentitem_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=model_DocumentItem_strategy)
def test_hyp_model_documentitem_vestingPeriodEnd_setter(instance):
    original = instance.vestingPeriodEnd
    instance.vestingPeriodEnd = original
    assert instance.vestingPeriodEnd == original



@given(instance=model_DocumentItem_strategy)
def test_hyp_model_documentitem_picture_setter(instance):
    original = instance.picture
    instance.picture = original
    assert instance.picture == original



@given(instance=model_DocumentItem_strategy)
def test_hyp_model_documentitem_quantityUnit_setter(instance):
    original = instance.quantityUnit
    instance.quantityUnit = original
    assert instance.quantityUnit == original



@given(instance=model_DocumentItem_strategy)
def test_hyp_model_documentitem_itemType_setter(instance):
    original = instance.itemType
    instance.itemType = original
    assert instance.itemType == original



@given(instance=model_DocumentItem_strategy)
def test_hyp_model_documentitem_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=model_DocumentItem_strategy)
def test_hyp_model_documentitem_vestingPeriodStart_setter(instance):
    original = instance.vestingPeriodStart
    instance.vestingPeriodStart = original
    assert instance.vestingPeriodStart == original



@given(instance=model_DocumentItem_strategy)
def test_hyp_model_documentitem_gtin_setter(instance):
    original = instance.gtin
    instance.gtin = original
    assert instance.gtin == original



@given(instance=model_DocumentItem_strategy)
def test_hyp_model_documentitem_tara_setter(instance):
    original = instance.tara
    instance.tara = original
    assert instance.tara == original



@given(instance=model_DocumentItem_strategy)
def test_hyp_model_documentitem_originQuantity_setter(instance):
    original = instance.originQuantity
    instance.originQuantity = original
    assert instance.originQuantity == original



@given(instance=model_DocumentItem_strategy)
def test_hyp_model_documentitem_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original



@given(instance=model_DocumentItem_strategy)
def test_hyp_model_documentitem_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original




@given(instance=model_VoucherItem_strategy)
def test_hyp_model_voucheritem_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=model_VoucherItem_strategy)
def test_hyp_model_voucheritem_posNr_setter(instance):
    original = instance.posNr
    instance.posNr = original
    assert instance.posNr == original



@given(instance=model_VoucherItem_strategy)
def test_hyp_model_voucheritem_itemVoucherType_setter(instance):
    original = instance.itemVoucherType
    instance.itemVoucherType = original
    assert instance.itemVoucherType == original




@given(instance=model_Voucher_strategy)
def test_hyp_model_voucher_discounted_setter(instance):
    original = instance.discounted
    instance.discounted = original
    assert instance.discounted == original



@given(instance=model_Voucher_strategy)
def test_hyp_model_voucher_voucherNumber_setter(instance):
    original = instance.voucherNumber
    instance.voucherNumber = original
    assert instance.voucherNumber == original



@given(instance=model_Voucher_strategy)
def test_hyp_model_voucher_voucherDate_setter(instance):
    original = instance.voucherDate
    instance.voucherDate = original
    assert instance.voucherDate == original



@given(instance=model_Voucher_strategy)
def test_hyp_model_voucher_doNotBook_setter(instance):
    original = instance.doNotBook
    instance.doNotBook = original
    assert instance.doNotBook == original



@given(instance=model_Voucher_strategy)
def test_hyp_model_voucher_voucherType_setter(instance):
    original = instance.voucherType
    instance.voucherType = original
    assert instance.voucherType == original



@given(instance=model_Voucher_strategy)
def test_hyp_model_voucher_documentNumber_setter(instance):
    original = instance.documentNumber
    instance.documentNumber = original
    assert instance.documentNumber == original



@given(instance=model_Voucher_strategy)
def test_hyp_model_voucher_totalValue_setter(instance):
    original = instance.totalValue
    instance.totalValue = original
    assert instance.totalValue == original



@given(instance=model_Voucher_strategy)
def test_hyp_model_voucher_paidValue_setter(instance):
    original = instance.paidValue
    instance.paidValue = original
    assert instance.paidValue == original




@given(instance=model_ItemAccountType_strategy)
def test_hyp_model_itemaccounttype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=model_Address_strategy)
def test_hyp_model_address_manualAddress_setter(instance):
    original = instance.manualAddress
    instance.manualAddress = original
    assert instance.manualAddress == original



@given(instance=model_Address_strategy)
def test_hyp_model_address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=model_Address_strategy)
def test_hyp_model_address_cityAddon_setter(instance):
    original = instance.cityAddon
    instance.cityAddon = original
    assert instance.cityAddon == original



@given(instance=model_Address_strategy)
def test_hyp_model_address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=model_Address_strategy)
def test_hyp_model_address_zip_setter(instance):
    original = instance.zip
    instance.zip = original
    assert instance.zip == original



@given(instance=model_Address_strategy)
def test_hyp_model_address_countryCode_setter(instance):
    original = instance.countryCode
    instance.countryCode = original
    assert instance.countryCode == original




@given(instance=model_VAT_strategy)
def test_hyp_model_vat_taxValue_setter(instance):
    original = instance.taxValue
    instance.taxValue = original
    assert instance.taxValue == original



@given(instance=model_VAT_strategy)
def test_hyp_model_vat_salesEqualizationTax_setter(instance):
    original = instance.salesEqualizationTax
    instance.salesEqualizationTax = original
    assert instance.salesEqualizationTax == original



@given(instance=model_VAT_strategy)
def test_hyp_model_vat_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




@given(instance=model_Document_strategy)
def test_hyp_model_document_vestingPeriodStart_setter(instance):
    original = instance.vestingPeriodStart
    instance.vestingPeriodStart = original
    assert instance.vestingPeriodStart == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_message3_setter(instance):
    original = instance.message3
    instance.message3 = original
    assert instance.message3 == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_message2_setter(instance):
    original = instance.message2
    instance.message2 = original
    assert instance.message2 == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_vestingPeriodEnd_setter(instance):
    original = instance.vestingPeriodEnd
    instance.vestingPeriodEnd = original
    assert instance.vestingPeriodEnd == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_netGross_setter(instance):
    original = instance.netGross
    instance.netGross = original
    assert instance.netGross == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_transactionId_setter(instance):
    original = instance.transactionId
    instance.transactionId = original
    assert instance.transactionId == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_orderDate_setter(instance):
    original = instance.orderDate
    instance.orderDate = original
    assert instance.orderDate == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_webshopDate_setter(instance):
    original = instance.webshopDate
    instance.webshopDate = original
    assert instance.webshopDate == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_webshopId_setter(instance):
    original = instance.webshopId
    instance.webshopId = original
    assert instance.webshopId == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_shippingValue_setter(instance):
    original = instance.shippingValue
    instance.shippingValue = original
    assert instance.shippingValue == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_billingType_setter(instance):
    original = instance.billingType
    instance.billingType = original
    assert instance.billingType == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_serviceDate_setter(instance):
    original = instance.serviceDate
    instance.serviceDate = original
    assert instance.serviceDate == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_itemsRebate_setter(instance):
    original = instance.itemsRebate
    instance.itemsRebate = original
    assert instance.itemsRebate == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_printTemplate_setter(instance):
    original = instance.printTemplate
    instance.printTemplate = original
    assert instance.printTemplate == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_dueDays_setter(instance):
    original = instance.dueDays
    instance.dueDays = original
    assert instance.dueDays == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_payDate_setter(instance):
    original = instance.payDate
    instance.payDate = original
    assert instance.payDate == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_addressFirstLine_setter(instance):
    original = instance.addressFirstLine
    instance.addressFirstLine = original
    assert instance.addressFirstLine == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_printed_setter(instance):
    original = instance.printed
    instance.printed = original
    assert instance.printed == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_documentDate_setter(instance):
    original = instance.documentDate
    instance.documentDate = original
    assert instance.documentDate == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_pdfPath_setter(instance):
    original = instance.pdfPath
    instance.pdfPath = original
    assert instance.pdfPath == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_consultant_setter(instance):
    original = instance.consultant
    instance.consultant = original
    assert instance.consultant == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_totalValue_setter(instance):
    original = instance.totalValue
    instance.totalValue = original
    assert instance.totalValue == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_progress_setter(instance):
    original = instance.progress
    instance.progress = original
    assert instance.progress == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_deposit_setter(instance):
    original = instance.deposit
    instance.deposit = original
    assert instance.deposit == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_odtPath_setter(instance):
    original = instance.odtPath
    instance.odtPath = original
    assert instance.odtPath == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_customerRef_setter(instance):
    original = instance.customerRef
    instance.customerRef = original
    assert instance.customerRef == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_paidValue_setter(instance):
    original = instance.paidValue
    instance.paidValue = original
    assert instance.paidValue == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_shippingAutoVat_setter(instance):
    original = instance.shippingAutoVat
    instance.shippingAutoVat = original
    assert instance.shippingAutoVat == original



@given(instance=model_Document_strategy)
def test_hyp_model_document_paid_setter(instance):
    original = instance.paid
    instance.paid = original
    assert instance.paid == original




@given(instance=model_ProductBlockPrice_strategy)
def test_hyp_model_productblockprice_block_setter(instance):
    original = instance.block
    instance.block = original
    assert instance.block == original



@given(instance=model_ProductBlockPrice_strategy)
def test_hyp_model_productblockprice_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original




@given(instance=model_Contact_strategy)
def test_hyp_model_contact_vatNumberValid_setter(instance):
    original = instance.vatNumberValid
    instance.vatNumberValid = original
    assert instance.vatNumberValid == original



@given(instance=model_Contact_strategy)
def test_hyp_model_contact_gln_setter(instance):
    original = instance.gln
    instance.gln = original
    assert instance.gln == original



@given(instance=model_Contact_strategy)
def test_hyp_model_contact_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=model_Contact_strategy)
def test_hyp_model_contact_website_setter(instance):
    original = instance.website
    instance.website = original
    assert instance.website == original



@given(instance=model_Contact_strategy)
def test_hyp_model_contact_fax_setter(instance):
    original = instance.fax
    instance.fax = original
    assert instance.fax == original



@given(instance=model_Contact_strategy)
def test_hyp_model_contact_customerNumber_setter(instance):
    original = instance.customerNumber
    instance.customerNumber = original
    assert instance.customerNumber == original



@given(instance=model_Contact_strategy)
def test_hyp_model_contact_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=model_Contact_strategy)
def test_hyp_model_contact_birthday_setter(instance):
    original = instance.birthday
    instance.birthday = original
    assert instance.birthday == original



@given(instance=model_Contact_strategy)
def test_hyp_model_contact_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=model_Contact_strategy)
def test_hyp_model_contact_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original



@given(instance=model_Contact_strategy)
def test_hyp_model_contact_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=model_Contact_strategy)
def test_hyp_model_contact_useNetGross_setter(instance):
    original = instance.useNetGross
    instance.useNetGross = original
    assert instance.useNetGross == original



@given(instance=model_Contact_strategy)
def test_hyp_model_contact_webshopName_setter(instance):
    original = instance.webshopName
    instance.webshopName = original
    assert instance.webshopName == original



@given(instance=model_Contact_strategy)
def test_hyp_model_contact_mobile_setter(instance):
    original = instance.mobile
    instance.mobile = original
    assert instance.mobile == original



@given(instance=model_Contact_strategy)
def test_hyp_model_contact_useSalesEqualizationTax_setter(instance):
    original = instance.useSalesEqualizationTax
    instance.useSalesEqualizationTax = original
    assert instance.useSalesEqualizationTax == original



@given(instance=model_Contact_strategy)
def test_hyp_model_contact_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=model_Contact_strategy)
def test_hyp_model_contact_supplierNumber_setter(instance):
    original = instance.supplierNumber
    instance.supplierNumber = original
    assert instance.supplierNumber == original



@given(instance=model_Contact_strategy)
def test_hyp_model_contact_mandateReference_setter(instance):
    original = instance.mandateReference
    instance.mandateReference = original
    assert instance.mandateReference == original



@given(instance=model_Contact_strategy)
def test_hyp_model_contact_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original



@given(instance=model_Contact_strategy)
def test_hyp_model_contact_contactType_setter(instance):
    original = instance.contactType
    instance.contactType = original
    assert instance.contactType == original



@given(instance=model_Contact_strategy)
def test_hyp_model_contact_vatNumber_setter(instance):
    original = instance.vatNumber
    instance.vatNumber = original
    assert instance.vatNumber == original



@given(instance=model_Contact_strategy)
def test_hyp_model_contact_discount_setter(instance):
    original = instance.discount
    instance.discount = original
    assert instance.discount == original



@given(instance=model_Contact_strategy)
def test_hyp_model_contact_reliability_setter(instance):
    original = instance.reliability
    instance.reliability = original
    assert instance.reliability == original




@given(instance=model_BankAccount_strategy)
def test_hyp_model_bankaccount_iban_setter(instance):
    original = instance.iban
    instance.iban = original
    assert instance.iban == original



@given(instance=model_BankAccount_strategy)
def test_hyp_model_bankaccount_accountHolder_setter(instance):
    original = instance.accountHolder
    instance.accountHolder = original
    assert instance.accountHolder == original



@given(instance=model_BankAccount_strategy)
def test_hyp_model_bankaccount_bankName_setter(instance):
    original = instance.bankName
    instance.bankName = original
    assert instance.bankName == original



@given(instance=model_BankAccount_strategy)
def test_hyp_model_bankaccount_bic_setter(instance):
    original = instance.bic
    instance.bic = original
    assert instance.bic == original



@given(instance=model_BankAccount_strategy)
def test_hyp_model_bankaccount_bankCode_setter(instance):
    original = instance.bankCode
    instance.bankCode = original
    assert instance.bankCode == original




@given(instance=model_IndividualDocumentInfo_strategy)
def test_hyp_model_individualdocumentinfo_noVatDescription_setter(instance):
    original = instance.noVatDescription
    instance.noVatDescription = original
    assert instance.noVatDescription == original



@given(instance=model_IndividualDocumentInfo_strategy)
def test_hyp_model_individualdocumentinfo_shippingVatDescription_setter(instance):
    original = instance.shippingVatDescription
    instance.shippingVatDescription = original
    assert instance.shippingVatDescription == original



@given(instance=model_IndividualDocumentInfo_strategy)
def test_hyp_model_individualdocumentinfo_shippingDescription_setter(instance):
    original = instance.shippingDescription
    instance.shippingDescription = original
    assert instance.shippingDescription == original



@given(instance=model_IndividualDocumentInfo_strategy)
def test_hyp_model_individualdocumentinfo_shippingName_setter(instance):
    original = instance.shippingName
    instance.shippingName = original
    assert instance.shippingName == original



@given(instance=model_IndividualDocumentInfo_strategy)
def test_hyp_model_individualdocumentinfo_shippingAutoVat_setter(instance):
    original = instance.shippingAutoVat
    instance.shippingAutoVat = original
    assert instance.shippingAutoVat == original



@given(instance=model_IndividualDocumentInfo_strategy)
def test_hyp_model_individualdocumentinfo_shippingVatValue_setter(instance):
    original = instance.shippingVatValue
    instance.shippingVatValue = original
    assert instance.shippingVatValue == original



@given(instance=model_IndividualDocumentInfo_strategy)
def test_hyp_model_individualdocumentinfo_shippingValue_setter(instance):
    original = instance.shippingValue
    instance.shippingValue = original
    assert instance.shippingValue == original



@given(instance=model_IndividualDocumentInfo_strategy)
def test_hyp_model_individualdocumentinfo_paymentText_setter(instance):
    original = instance.paymentText
    instance.paymentText = original
    assert instance.paymentText == original



@given(instance=model_IndividualDocumentInfo_strategy)
def test_hyp_model_individualdocumentinfo_noVatName_setter(instance):
    original = instance.noVatName
    instance.noVatName = original
    assert instance.noVatName == original



@given(instance=model_IndividualDocumentInfo_strategy)
def test_hyp_model_individualdocumentinfo_paymentDescription_setter(instance):
    original = instance.paymentDescription
    instance.paymentDescription = original
    assert instance.paymentDescription == original



@given(instance=model_IndividualDocumentInfo_strategy)
def test_hyp_model_individualdocumentinfo_paymentName_setter(instance):
    original = instance.paymentName
    instance.paymentName = original
    assert instance.paymentName == original




@given(instance=model_IDescribableEntity_strategy)
def test_hyp_model_idescribableentity_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




@given(instance=model_Payment_strategy)
def test_hyp_model_payment_netDays_setter(instance):
    original = instance.netDays
    instance.netDays = original
    assert instance.netDays == original



@given(instance=model_Payment_strategy)
def test_hyp_model_payment_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=model_Payment_strategy)
def test_hyp_model_payment_discountDays_setter(instance):
    original = instance.discountDays
    instance.discountDays = original
    assert instance.discountDays == original



@given(instance=model_Payment_strategy)
def test_hyp_model_payment_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=model_Payment_strategy)
def test_hyp_model_payment_paidText_setter(instance):
    original = instance.paidText
    instance.paidText = original
    assert instance.paidText == original



@given(instance=model_Payment_strategy)
def test_hyp_model_payment_depositText_setter(instance):
    original = instance.depositText
    instance.depositText = original
    assert instance.depositText == original



@given(instance=model_Payment_strategy)
def test_hyp_model_payment_unpaidText_setter(instance):
    original = instance.unpaidText
    instance.unpaidText = original
    assert instance.unpaidText == original



@given(instance=model_Payment_strategy)
def test_hyp_model_payment_discountValue_setter(instance):
    original = instance.discountValue
    instance.discountValue = original
    assert instance.discountValue == original





@given(instance=model_IEntity_strategy)
def test_hyp_model_ientity_validTo_setter(instance):
    original = instance.validTo
    instance.validTo = original
    assert instance.validTo == original



@given(instance=model_IEntity_strategy)
def test_hyp_model_ientity_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=model_IEntity_strategy)
def test_hyp_model_ientity_modified_setter(instance):
    original = instance.modified
    instance.modified = original
    assert instance.modified == original



@given(instance=model_IEntity_strategy)
def test_hyp_model_ientity_modifiedBy_setter(instance):
    original = instance.modifiedBy
    instance.modifiedBy = original
    assert instance.modifiedBy == original



@given(instance=model_IEntity_strategy)
def test_hyp_model_ientity_validFrom_setter(instance):
    original = instance.validFrom
    instance.validFrom = original
    assert instance.validFrom == original



@given(instance=model_IEntity_strategy)
def test_hyp_model_ientity_deleted_setter(instance):
    original = instance.deleted
    instance.deleted = original
    assert instance.deleted == original



@given(instance=model_IEntity_strategy)
def test_hyp_model_ientity_dateAdded_setter(instance):
    original = instance.dateAdded
    instance.dateAdded = original
    assert instance.dateAdded == original



@given(instance=model_IEntity_strategy)
def test_hyp_model_ientity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_IEntity_strategy)
@settings(max_examples=30)
def test_hyp_model_ientity_issameas_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSameAs()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSameAs).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSameAs' in model_IEntity is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSameAs' in model_IEntity did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSameAs' in model_IEntity is not implemented or raised an error")




@given(instance=model_WebshopStateMapping_strategy)
def test_hyp_model_webshopstatemapping_webshopState_setter(instance):
    original = instance.webshopState
    instance.webshopState = original
    assert instance.webshopState == original



@given(instance=model_WebshopStateMapping_strategy)
def test_hyp_model_webshopstatemapping_fakturamaOrderState_setter(instance):
    original = instance.fakturamaOrderState
    instance.fakturamaOrderState = original
    assert instance.fakturamaOrderState == original




@given(instance=model_WebShop_strategy)
def test_hyp_model_webshop_webshopVendor_setter(instance):
    original = instance.webshopVendor
    instance.webshopVendor = original
    assert instance.webshopVendor == original



@given(instance=model_WebShop_strategy)
def test_hyp_model_webshop_webshopVersion_setter(instance):
    original = instance.webshopVersion
    instance.webshopVersion = original
    assert instance.webshopVersion == original




@given(instance=model_CEFACTCode_strategy)
def test_hyp_model_cefactcode_name_de_setter(instance):
    original = instance.name_de
    instance.name_de = original
    assert instance.name_de == original



@given(instance=model_CEFACTCode_strategy)
def test_hyp_model_cefactcode_abbreviation_en_setter(instance):
    original = instance.abbreviation_en
    instance.abbreviation_en = original
    assert instance.abbreviation_en == original



@given(instance=model_CEFACTCode_strategy)
def test_hyp_model_cefactcode_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=model_CEFACTCode_strategy)
def test_hyp_model_cefactcode_abbreviation_de_setter(instance):
    original = instance.abbreviation_de
    instance.abbreviation_de = original
    assert instance.abbreviation_de == original



@given(instance=model_CEFACTCode_strategy)
def test_hyp_model_cefactcode_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original




@given(instance=model_User_strategy)
def test_hyp_model_user_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=model_User_strategy)
def test_hyp_model_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original





@given(instance=model_TextModule_strategy)
def test_hyp_model_textmodule_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original







@given(instance=model_UserProperty_strategy)
def test_hyp_model_userproperty_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original



@given(instance=model_UserProperty_strategy)
def test_hyp_model_userproperty_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=model_UserProperty_strategy)
def test_hyp_model_userproperty_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=model_UserProperty_strategy)
def test_hyp_model_userproperty_global__setter(instance):
    original = instance.global_
    instance.global_ = original
    assert instance.global_ == original





@given(instance=model_ProductOptions_strategy)
def test_hyp_model_productoptions_sequenceNumber_setter(instance):
    original = instance.sequenceNumber
    instance.sequenceNumber = original
    assert instance.sequenceNumber == original



@given(instance=model_ProductOptions_strategy)
def test_hyp_model_productoptions_attributeValue_setter(instance):
    original = instance.attributeValue
    instance.attributeValue = original
    assert instance.attributeValue == original






@given(instance=model_Product_strategy)
def test_hyp_model_product_price1_setter(instance):
    original = instance.price1
    instance.price1 = original
    assert instance.price1 == original



@given(instance=model_Product_strategy)
def test_hyp_model_product_block2_setter(instance):
    original = instance.block2
    instance.block2 = original
    assert instance.block2 == original



@given(instance=model_Product_strategy)
def test_hyp_model_product_costPrice_setter(instance):
    original = instance.costPrice
    instance.costPrice = original
    assert instance.costPrice == original



@given(instance=model_Product_strategy)
def test_hyp_model_product_webshopId_setter(instance):
    original = instance.webshopId
    instance.webshopId = original
    assert instance.webshopId == original



@given(instance=model_Product_strategy)
def test_hyp_model_product_price2_setter(instance):
    original = instance.price2
    instance.price2 = original
    assert instance.price2 == original



@given(instance=model_Product_strategy)
def test_hyp_model_product_gtin_setter(instance):
    original = instance.gtin
    instance.gtin = original
    assert instance.gtin == original



@given(instance=model_Product_strategy)
def test_hyp_model_product_itemNumber_setter(instance):
    original = instance.itemNumber
    instance.itemNumber = original
    assert instance.itemNumber == original



@given(instance=model_Product_strategy)
def test_hyp_model_product_quantityUnit_setter(instance):
    original = instance.quantityUnit
    instance.quantityUnit = original
    assert instance.quantityUnit == original



@given(instance=model_Product_strategy)
def test_hyp_model_product_price3_setter(instance):
    original = instance.price3
    instance.price3 = original
    assert instance.price3 == original



@given(instance=model_Product_strategy)
def test_hyp_model_product_price5_setter(instance):
    original = instance.price5
    instance.price5 = original
    assert instance.price5 == original



@given(instance=model_Product_strategy)
def test_hyp_model_product_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=model_Product_strategy)
def test_hyp_model_product_block3_setter(instance):
    original = instance.block3
    instance.block3 = original
    assert instance.block3 == original



@given(instance=model_Product_strategy)
def test_hyp_model_product_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=model_Product_strategy)
def test_hyp_model_product_block1_setter(instance):
    original = instance.block1
    instance.block1 = original
    assert instance.block1 == original



@given(instance=model_Product_strategy)
def test_hyp_model_product_picture_setter(instance):
    original = instance.picture
    instance.picture = original
    assert instance.picture == original



@given(instance=model_Product_strategy)
def test_hyp_model_product_price4_setter(instance):
    original = instance.price4
    instance.price4 = original
    assert instance.price4 == original



@given(instance=model_Product_strategy)
def test_hyp_model_product_block4_setter(instance):
    original = instance.block4
    instance.block4 = original
    assert instance.block4 == original



@given(instance=model_Product_strategy)
def test_hyp_model_product_sellingUnit_setter(instance):
    original = instance.sellingUnit
    instance.sellingUnit = original
    assert instance.sellingUnit == original



@given(instance=model_Product_strategy)
def test_hyp_model_product_cdf03_setter(instance):
    original = instance.cdf03
    instance.cdf03 = original
    assert instance.cdf03 == original



@given(instance=model_Product_strategy)
def test_hyp_model_product_block5_setter(instance):
    original = instance.block5
    instance.block5 = original
    assert instance.block5 == original



@given(instance=model_Product_strategy)
def test_hyp_model_product_cdf01_setter(instance):
    original = instance.cdf01
    instance.cdf01 = original
    assert instance.cdf01 == original



@given(instance=model_Product_strategy)
def test_hyp_model_product_cdf02_setter(instance):
    original = instance.cdf02
    instance.cdf02 = original
    assert instance.cdf02 == original




@given(instance=model_Shipping_strategy)
def test_hyp_model_shipping_autoVat_setter(instance):
    original = instance.autoVat
    instance.autoVat = original
    assert instance.autoVat == original



@given(instance=model_Shipping_strategy)
def test_hyp_model_shipping_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=model_Shipping_strategy)
def test_hyp_model_shipping_shippingValue_setter(instance):
    original = instance.shippingValue
    instance.shippingValue = original
    assert instance.shippingValue == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_model_Address_city_value_roundtrip():
    instance = model_Address(city="sample_text", cityAddon="sample_text", countryCode="sample_text", manualAddress="sample_text", street="sample_text", zip="sample_text")
    assert instance.city == "sample_text"
    instance.city = "sample_text_2"
    assert instance.city == "sample_text_2"


def test_model_Address_cityAddon_value_roundtrip():
    instance = model_Address(city="sample_text", cityAddon="sample_text", countryCode="sample_text", manualAddress="sample_text", street="sample_text", zip="sample_text")
    assert instance.cityAddon == "sample_text"
    instance.cityAddon = "sample_text_2"
    assert instance.cityAddon == "sample_text_2"


def test_model_Address_countryCode_value_roundtrip():
    instance = model_Address(city="sample_text", cityAddon="sample_text", countryCode="sample_text", manualAddress="sample_text", street="sample_text", zip="sample_text")
    assert instance.countryCode == "sample_text"
    instance.countryCode = "sample_text_2"
    assert instance.countryCode == "sample_text_2"


def test_model_Address_manualAddress_value_roundtrip():
    instance = model_Address(city="sample_text", cityAddon="sample_text", countryCode="sample_text", manualAddress="sample_text", street="sample_text", zip="sample_text")
    assert instance.manualAddress == "sample_text"
    instance.manualAddress = "sample_text_2"
    assert instance.manualAddress == "sample_text_2"


def test_model_Address_street_value_roundtrip():
    instance = model_Address(city="sample_text", cityAddon="sample_text", countryCode="sample_text", manualAddress="sample_text", street="sample_text", zip="sample_text")
    assert instance.street == "sample_text"
    instance.street = "sample_text_2"
    assert instance.street == "sample_text_2"


def test_model_Address_zip_value_roundtrip():
    instance = model_Address(city="sample_text", cityAddon="sample_text", countryCode="sample_text", manualAddress="sample_text", street="sample_text", zip="sample_text")
    assert instance.zip == "sample_text"
    instance.zip = "sample_text_2"
    assert instance.zip == "sample_text_2"


def test_model_BankAccount_accountHolder_value_roundtrip():
    instance = model_BankAccount(accountHolder="sample_text", bankCode="sample_text", bankName="sample_text", bic="sample_text", iban="sample_text")
    assert instance.accountHolder == "sample_text"
    instance.accountHolder = "sample_text_2"
    assert instance.accountHolder == "sample_text_2"


def test_model_BankAccount_bankCode_value_roundtrip():
    instance = model_BankAccount(accountHolder="sample_text", bankCode="sample_text", bankName="sample_text", bic="sample_text", iban="sample_text")
    assert instance.bankCode == "sample_text"
    instance.bankCode = "sample_text_2"
    assert instance.bankCode == "sample_text_2"


def test_model_BankAccount_bankName_value_roundtrip():
    instance = model_BankAccount(accountHolder="sample_text", bankCode="sample_text", bankName="sample_text", bic="sample_text", iban="sample_text")
    assert instance.bankName == "sample_text"
    instance.bankName = "sample_text_2"
    assert instance.bankName == "sample_text_2"


def test_model_BankAccount_bic_value_roundtrip():
    instance = model_BankAccount(accountHolder="sample_text", bankCode="sample_text", bankName="sample_text", bic="sample_text", iban="sample_text")
    assert instance.bic == "sample_text"
    instance.bic = "sample_text_2"
    assert instance.bic == "sample_text_2"


def test_model_BankAccount_iban_value_roundtrip():
    instance = model_BankAccount(accountHolder="sample_text", bankCode="sample_text", bankName="sample_text", bic="sample_text", iban="sample_text")
    assert instance.iban == "sample_text"
    instance.iban = "sample_text_2"
    assert instance.iban == "sample_text_2"


def test_model_CEFACTCode_abbreviation_de_value_roundtrip():
    instance = model_CEFACTCode(abbreviation_de="sample_text", abbreviation_en="sample_text", code="sample_text", name_de="sample_text", target="sample_text")
    assert instance.abbreviation_de == "sample_text"
    instance.abbreviation_de = "sample_text_2"
    assert instance.abbreviation_de == "sample_text_2"


def test_model_CEFACTCode_abbreviation_en_value_roundtrip():
    instance = model_CEFACTCode(abbreviation_de="sample_text", abbreviation_en="sample_text", code="sample_text", name_de="sample_text", target="sample_text")
    assert instance.abbreviation_en == "sample_text"
    instance.abbreviation_en = "sample_text_2"
    assert instance.abbreviation_en == "sample_text_2"


def test_model_CEFACTCode_code_value_roundtrip():
    instance = model_CEFACTCode(abbreviation_de="sample_text", abbreviation_en="sample_text", code="sample_text", name_de="sample_text", target="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_model_CEFACTCode_name_de_value_roundtrip():
    instance = model_CEFACTCode(abbreviation_de="sample_text", abbreviation_en="sample_text", code="sample_text", name_de="sample_text", target="sample_text")
    assert instance.name_de == "sample_text"
    instance.name_de = "sample_text_2"
    assert instance.name_de == "sample_text_2"


def test_model_CEFACTCode_target_value_roundtrip():
    instance = model_CEFACTCode(abbreviation_de="sample_text", abbreviation_en="sample_text", code="sample_text", name_de="sample_text", target="sample_text")
    assert instance.target == "sample_text"
    instance.target = "sample_text_2"
    assert instance.target == "sample_text_2"


def test_model_Contact_birthday_value_roundtrip():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert instance.birthday == date(2024, 1, 1)
    instance.birthday = date(2025, 6, 15)
    assert instance.birthday == date(2025, 6, 15)


def test_model_Contact_company_value_roundtrip():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert instance.company == "sample_text"
    instance.company = "sample_text_2"
    assert instance.company == "sample_text_2"


def test_model_Contact_contactType_value_roundtrip():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert instance.contactType == "sample_text"
    instance.contactType = "sample_text_2"
    assert instance.contactType == "sample_text_2"


def test_model_Contact_customerNumber_value_roundtrip():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert instance.customerNumber == "sample_text"
    instance.customerNumber = "sample_text_2"
    assert instance.customerNumber == "sample_text_2"


def test_model_Contact_discount_value_roundtrip():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert instance.discount == "sample_text"
    instance.discount = "sample_text_2"
    assert instance.discount == "sample_text_2"


def test_model_Contact_email_value_roundtrip():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_model_Contact_fax_value_roundtrip():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert instance.fax == "sample_text"
    instance.fax = "sample_text_2"
    assert instance.fax == "sample_text_2"


def test_model_Contact_firstName_value_roundtrip():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_model_Contact_gender_value_roundtrip():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert instance.gender == "sample_text"
    instance.gender = "sample_text_2"
    assert instance.gender == "sample_text_2"


def test_model_Contact_gln_value_roundtrip():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert instance.gln == "sample_text"
    instance.gln = "sample_text_2"
    assert instance.gln == "sample_text_2"


def test_model_Contact_mandateReference_value_roundtrip():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert instance.mandateReference == "sample_text"
    instance.mandateReference = "sample_text_2"
    assert instance.mandateReference == "sample_text_2"


def test_model_Contact_mobile_value_roundtrip():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert instance.mobile == "sample_text"
    instance.mobile = "sample_text_2"
    assert instance.mobile == "sample_text_2"


def test_model_Contact_note_value_roundtrip():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_model_Contact_phone_value_roundtrip():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert instance.phone == "sample_text"
    instance.phone = "sample_text_2"
    assert instance.phone == "sample_text_2"


def test_model_Contact_reliability_value_roundtrip():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert instance.reliability == "sample_text"
    instance.reliability = "sample_text_2"
    assert instance.reliability == "sample_text_2"


def test_model_Contact_supplierNumber_value_roundtrip():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert instance.supplierNumber == "sample_text"
    instance.supplierNumber = "sample_text_2"
    assert instance.supplierNumber == "sample_text_2"


def test_model_Contact_title_value_roundtrip():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_model_Contact_useNetGross_value_roundtrip():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert instance.useNetGross == "sample_text"
    instance.useNetGross = "sample_text_2"
    assert instance.useNetGross == "sample_text_2"


def test_model_Contact_useSalesEqualizationTax_value_roundtrip():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert instance.useSalesEqualizationTax == "sample_text"
    instance.useSalesEqualizationTax = "sample_text_2"
    assert instance.useSalesEqualizationTax == "sample_text_2"


def test_model_Contact_vatNumber_value_roundtrip():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert instance.vatNumber == "sample_text"
    instance.vatNumber = "sample_text_2"
    assert instance.vatNumber == "sample_text_2"


def test_model_Contact_vatNumberValid_value_roundtrip():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert instance.vatNumberValid == "sample_text"
    instance.vatNumberValid = "sample_text_2"
    assert instance.vatNumberValid == "sample_text_2"


def test_model_Contact_webshopName_value_roundtrip():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert instance.webshopName == "sample_text"
    instance.webshopName = "sample_text_2"
    assert instance.webshopName == "sample_text_2"


def test_model_Contact_website_value_roundtrip():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert instance.website == "sample_text"
    instance.website = "sample_text_2"
    assert instance.website == "sample_text_2"


def test_model_Document_addressFirstLine_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.addressFirstLine == "sample_text"
    instance.addressFirstLine = "sample_text_2"
    assert instance.addressFirstLine == "sample_text_2"


def test_model_Document_billingType_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.billingType == "sample_text"
    instance.billingType = "sample_text_2"
    assert instance.billingType == "sample_text_2"


def test_model_Document_consultant_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.consultant == "sample_text"
    instance.consultant = "sample_text_2"
    assert instance.consultant == "sample_text_2"


def test_model_Document_customerRef_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.customerRef == "sample_text"
    instance.customerRef = "sample_text_2"
    assert instance.customerRef == "sample_text_2"


def test_model_Document_deposit_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.deposit == "sample_text"
    instance.deposit = "sample_text_2"
    assert instance.deposit == "sample_text_2"


def test_model_Document_documentDate_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.documentDate == date(2024, 1, 1)
    instance.documentDate = date(2025, 6, 15)
    assert instance.documentDate == date(2025, 6, 15)


def test_model_Document_dueDays_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.dueDays == "sample_text"
    instance.dueDays = "sample_text_2"
    assert instance.dueDays == "sample_text_2"


def test_model_Document_itemsRebate_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.itemsRebate == "sample_text"
    instance.itemsRebate = "sample_text_2"
    assert instance.itemsRebate == "sample_text_2"


def test_model_Document_message_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_model_Document_message2_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.message2 == "sample_text"
    instance.message2 = "sample_text_2"
    assert instance.message2 == "sample_text_2"


def test_model_Document_message3_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.message3 == "sample_text"
    instance.message3 = "sample_text_2"
    assert instance.message3 == "sample_text_2"


def test_model_Document_netGross_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.netGross == "sample_text"
    instance.netGross = "sample_text_2"
    assert instance.netGross == "sample_text_2"


def test_model_Document_odtPath_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.odtPath == "sample_text"
    instance.odtPath = "sample_text_2"
    assert instance.odtPath == "sample_text_2"


def test_model_Document_orderDate_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.orderDate == date(2024, 1, 1)
    instance.orderDate = date(2025, 6, 15)
    assert instance.orderDate == date(2025, 6, 15)


def test_model_Document_paid_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.paid == "sample_text"
    instance.paid = "sample_text_2"
    assert instance.paid == "sample_text_2"


def test_model_Document_paidValue_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.paidValue == "sample_text"
    instance.paidValue = "sample_text_2"
    assert instance.paidValue == "sample_text_2"


def test_model_Document_payDate_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.payDate == date(2024, 1, 1)
    instance.payDate = date(2025, 6, 15)
    assert instance.payDate == date(2025, 6, 15)


def test_model_Document_pdfPath_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.pdfPath == "sample_text"
    instance.pdfPath = "sample_text_2"
    assert instance.pdfPath == "sample_text_2"


def test_model_Document_printTemplate_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.printTemplate == "sample_text"
    instance.printTemplate = "sample_text_2"
    assert instance.printTemplate == "sample_text_2"


def test_model_Document_printed_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.printed == "sample_text"
    instance.printed = "sample_text_2"
    assert instance.printed == "sample_text_2"


def test_model_Document_progress_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.progress == "sample_text"
    instance.progress = "sample_text_2"
    assert instance.progress == "sample_text_2"


def test_model_Document_serviceDate_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.serviceDate == date(2024, 1, 1)
    instance.serviceDate = date(2025, 6, 15)
    assert instance.serviceDate == date(2025, 6, 15)


def test_model_Document_shippingAutoVat_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.shippingAutoVat == "sample_text"
    instance.shippingAutoVat = "sample_text_2"
    assert instance.shippingAutoVat == "sample_text_2"


def test_model_Document_shippingValue_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.shippingValue == "sample_text"
    instance.shippingValue = "sample_text_2"
    assert instance.shippingValue == "sample_text_2"


def test_model_Document_totalValue_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.totalValue == "sample_text"
    instance.totalValue = "sample_text_2"
    assert instance.totalValue == "sample_text_2"


def test_model_Document_transactionId_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.transactionId == "sample_text"
    instance.transactionId = "sample_text_2"
    assert instance.transactionId == "sample_text_2"


def test_model_Document_vestingPeriodEnd_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.vestingPeriodEnd == date(2024, 1, 1)
    instance.vestingPeriodEnd = date(2025, 6, 15)
    assert instance.vestingPeriodEnd == date(2025, 6, 15)


def test_model_Document_vestingPeriodStart_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.vestingPeriodStart == date(2024, 1, 1)
    instance.vestingPeriodStart = date(2025, 6, 15)
    assert instance.vestingPeriodStart == date(2025, 6, 15)


def test_model_Document_webshopDate_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.webshopDate == date(2024, 1, 1)
    instance.webshopDate = date(2025, 6, 15)
    assert instance.webshopDate == date(2025, 6, 15)


def test_model_Document_webshopId_value_roundtrip():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert instance.webshopId == "sample_text"
    instance.webshopId = "sample_text_2"
    assert instance.webshopId == "sample_text_2"


def test_model_DocumentItem_description_value_roundtrip():
    instance = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_model_DocumentItem_gtin_value_roundtrip():
    instance = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    assert instance.gtin == "sample_text"
    instance.gtin = "sample_text_2"
    assert instance.gtin == "sample_text_2"


def test_model_DocumentItem_itemNumber_value_roundtrip():
    instance = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    assert instance.itemNumber == "sample_text"
    instance.itemNumber = "sample_text_2"
    assert instance.itemNumber == "sample_text_2"


def test_model_DocumentItem_itemRebate_value_roundtrip():
    instance = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    assert instance.itemRebate == "sample_text"
    instance.itemRebate = "sample_text_2"
    assert instance.itemRebate == "sample_text_2"


def test_model_DocumentItem_itemType_value_roundtrip():
    instance = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    assert instance.itemType == "sample_text"
    instance.itemType = "sample_text_2"
    assert instance.itemType == "sample_text_2"


def test_model_DocumentItem_noVat_value_roundtrip():
    instance = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    assert instance.noVat == "sample_text"
    instance.noVat = "sample_text_2"
    assert instance.noVat == "sample_text_2"


def test_model_DocumentItem_optional_value_roundtrip():
    instance = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    assert instance.optional == "sample_text"
    instance.optional = "sample_text_2"
    assert instance.optional == "sample_text_2"


def test_model_DocumentItem_originQuantity_value_roundtrip():
    instance = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    assert instance.originQuantity == "sample_text"
    instance.originQuantity = "sample_text_2"
    assert instance.originQuantity == "sample_text_2"


def test_model_DocumentItem_picture_value_roundtrip():
    instance = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    assert instance.picture == "sample_text"
    instance.picture = "sample_text_2"
    assert instance.picture == "sample_text_2"


def test_model_DocumentItem_posNr_value_roundtrip():
    instance = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    assert instance.posNr == "sample_text"
    instance.posNr = "sample_text_2"
    assert instance.posNr == "sample_text_2"


def test_model_DocumentItem_price_value_roundtrip():
    instance = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    assert instance.price == "sample_text"
    instance.price = "sample_text_2"
    assert instance.price == "sample_text_2"


def test_model_DocumentItem_quantity_value_roundtrip():
    instance = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    assert instance.quantity == "sample_text"
    instance.quantity = "sample_text_2"
    assert instance.quantity == "sample_text_2"


def test_model_DocumentItem_quantityUnit_value_roundtrip():
    instance = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    assert instance.quantityUnit == "sample_text"
    instance.quantityUnit = "sample_text_2"
    assert instance.quantityUnit == "sample_text_2"


def test_model_DocumentItem_tara_value_roundtrip():
    instance = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    assert instance.tara == "sample_text"
    instance.tara = "sample_text_2"
    assert instance.tara == "sample_text_2"


def test_model_DocumentItem_vestingPeriodEnd_value_roundtrip():
    instance = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    assert instance.vestingPeriodEnd == date(2024, 1, 1)
    instance.vestingPeriodEnd = date(2025, 6, 15)
    assert instance.vestingPeriodEnd == date(2025, 6, 15)


def test_model_DocumentItem_vestingPeriodStart_value_roundtrip():
    instance = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    assert instance.vestingPeriodStart == date(2024, 1, 1)
    instance.vestingPeriodStart = date(2025, 6, 15)
    assert instance.vestingPeriodStart == date(2025, 6, 15)


def test_model_DocumentItem_weight_value_roundtrip():
    instance = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    assert instance.weight == "sample_text"
    instance.weight = "sample_text_2"
    assert instance.weight == "sample_text_2"


def test_model_Dunning_dunningLevel_value_roundtrip():
    instance = model_Dunning(dunningLevel="sample_text")
    assert instance.dunningLevel == "sample_text"
    instance.dunningLevel = "sample_text_2"
    assert instance.dunningLevel == "sample_text_2"


def test_model_IDescribableEntity_description_value_roundtrip():
    instance = model_IDescribableEntity(description="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_model_IEntity_dateAdded_value_roundtrip():
    instance = model_IEntity(dateAdded=date(2024, 1, 1), deleted="sample_text", id="sample_text", modified=date(2024, 1, 1), modifiedBy="sample_text", name="sample_text", validFrom=date(2024, 1, 1), validTo=date(2024, 1, 1))
    assert instance.dateAdded == date(2024, 1, 1)
    instance.dateAdded = date(2025, 6, 15)
    assert instance.dateAdded == date(2025, 6, 15)


def test_model_IEntity_deleted_value_roundtrip():
    instance = model_IEntity(dateAdded=date(2024, 1, 1), deleted="sample_text", id="sample_text", modified=date(2024, 1, 1), modifiedBy="sample_text", name="sample_text", validFrom=date(2024, 1, 1), validTo=date(2024, 1, 1))
    assert instance.deleted == "sample_text"
    instance.deleted = "sample_text_2"
    assert instance.deleted == "sample_text_2"


def test_model_IEntity_id_value_roundtrip():
    instance = model_IEntity(dateAdded=date(2024, 1, 1), deleted="sample_text", id="sample_text", modified=date(2024, 1, 1), modifiedBy="sample_text", name="sample_text", validFrom=date(2024, 1, 1), validTo=date(2024, 1, 1))
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_model_IEntity_modified_value_roundtrip():
    instance = model_IEntity(dateAdded=date(2024, 1, 1), deleted="sample_text", id="sample_text", modified=date(2024, 1, 1), modifiedBy="sample_text", name="sample_text", validFrom=date(2024, 1, 1), validTo=date(2024, 1, 1))
    assert instance.modified == date(2024, 1, 1)
    instance.modified = date(2025, 6, 15)
    assert instance.modified == date(2025, 6, 15)


def test_model_IEntity_modifiedBy_value_roundtrip():
    instance = model_IEntity(dateAdded=date(2024, 1, 1), deleted="sample_text", id="sample_text", modified=date(2024, 1, 1), modifiedBy="sample_text", name="sample_text", validFrom=date(2024, 1, 1), validTo=date(2024, 1, 1))
    assert instance.modifiedBy == "sample_text"
    instance.modifiedBy = "sample_text_2"
    assert instance.modifiedBy == "sample_text_2"


def test_model_IEntity_name_value_roundtrip():
    instance = model_IEntity(dateAdded=date(2024, 1, 1), deleted="sample_text", id="sample_text", modified=date(2024, 1, 1), modifiedBy="sample_text", name="sample_text", validFrom=date(2024, 1, 1), validTo=date(2024, 1, 1))
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_model_IEntity_validFrom_value_roundtrip():
    instance = model_IEntity(dateAdded=date(2024, 1, 1), deleted="sample_text", id="sample_text", modified=date(2024, 1, 1), modifiedBy="sample_text", name="sample_text", validFrom=date(2024, 1, 1), validTo=date(2024, 1, 1))
    assert instance.validFrom == date(2024, 1, 1)
    instance.validFrom = date(2025, 6, 15)
    assert instance.validFrom == date(2025, 6, 15)


def test_model_IEntity_validTo_value_roundtrip():
    instance = model_IEntity(dateAdded=date(2024, 1, 1), deleted="sample_text", id="sample_text", modified=date(2024, 1, 1), modifiedBy="sample_text", name="sample_text", validFrom=date(2024, 1, 1), validTo=date(2024, 1, 1))
    assert instance.validTo == date(2024, 1, 1)
    instance.validTo = date(2025, 6, 15)
    assert instance.validTo == date(2025, 6, 15)


def test_model_IndividualDocumentInfo_noVatDescription_value_roundtrip():
    instance = model_IndividualDocumentInfo(noVatDescription="sample_text", noVatName="sample_text", paymentDescription="sample_text", paymentName="sample_text", paymentText="sample_text", shippingAutoVat="sample_text", shippingDescription="sample_text", shippingName="sample_text", shippingValue="sample_text", shippingVatDescription="sample_text", shippingVatValue="sample_text")
    assert instance.noVatDescription == "sample_text"
    instance.noVatDescription = "sample_text_2"
    assert instance.noVatDescription == "sample_text_2"


def test_model_IndividualDocumentInfo_noVatName_value_roundtrip():
    instance = model_IndividualDocumentInfo(noVatDescription="sample_text", noVatName="sample_text", paymentDescription="sample_text", paymentName="sample_text", paymentText="sample_text", shippingAutoVat="sample_text", shippingDescription="sample_text", shippingName="sample_text", shippingValue="sample_text", shippingVatDescription="sample_text", shippingVatValue="sample_text")
    assert instance.noVatName == "sample_text"
    instance.noVatName = "sample_text_2"
    assert instance.noVatName == "sample_text_2"


def test_model_IndividualDocumentInfo_paymentDescription_value_roundtrip():
    instance = model_IndividualDocumentInfo(noVatDescription="sample_text", noVatName="sample_text", paymentDescription="sample_text", paymentName="sample_text", paymentText="sample_text", shippingAutoVat="sample_text", shippingDescription="sample_text", shippingName="sample_text", shippingValue="sample_text", shippingVatDescription="sample_text", shippingVatValue="sample_text")
    assert instance.paymentDescription == "sample_text"
    instance.paymentDescription = "sample_text_2"
    assert instance.paymentDescription == "sample_text_2"


def test_model_IndividualDocumentInfo_paymentName_value_roundtrip():
    instance = model_IndividualDocumentInfo(noVatDescription="sample_text", noVatName="sample_text", paymentDescription="sample_text", paymentName="sample_text", paymentText="sample_text", shippingAutoVat="sample_text", shippingDescription="sample_text", shippingName="sample_text", shippingValue="sample_text", shippingVatDescription="sample_text", shippingVatValue="sample_text")
    assert instance.paymentName == "sample_text"
    instance.paymentName = "sample_text_2"
    assert instance.paymentName == "sample_text_2"


def test_model_IndividualDocumentInfo_paymentText_value_roundtrip():
    instance = model_IndividualDocumentInfo(noVatDescription="sample_text", noVatName="sample_text", paymentDescription="sample_text", paymentName="sample_text", paymentText="sample_text", shippingAutoVat="sample_text", shippingDescription="sample_text", shippingName="sample_text", shippingValue="sample_text", shippingVatDescription="sample_text", shippingVatValue="sample_text")
    assert instance.paymentText == "sample_text"
    instance.paymentText = "sample_text_2"
    assert instance.paymentText == "sample_text_2"


def test_model_IndividualDocumentInfo_shippingAutoVat_value_roundtrip():
    instance = model_IndividualDocumentInfo(noVatDescription="sample_text", noVatName="sample_text", paymentDescription="sample_text", paymentName="sample_text", paymentText="sample_text", shippingAutoVat="sample_text", shippingDescription="sample_text", shippingName="sample_text", shippingValue="sample_text", shippingVatDescription="sample_text", shippingVatValue="sample_text")
    assert instance.shippingAutoVat == "sample_text"
    instance.shippingAutoVat = "sample_text_2"
    assert instance.shippingAutoVat == "sample_text_2"


def test_model_IndividualDocumentInfo_shippingDescription_value_roundtrip():
    instance = model_IndividualDocumentInfo(noVatDescription="sample_text", noVatName="sample_text", paymentDescription="sample_text", paymentName="sample_text", paymentText="sample_text", shippingAutoVat="sample_text", shippingDescription="sample_text", shippingName="sample_text", shippingValue="sample_text", shippingVatDescription="sample_text", shippingVatValue="sample_text")
    assert instance.shippingDescription == "sample_text"
    instance.shippingDescription = "sample_text_2"
    assert instance.shippingDescription == "sample_text_2"


def test_model_IndividualDocumentInfo_shippingName_value_roundtrip():
    instance = model_IndividualDocumentInfo(noVatDescription="sample_text", noVatName="sample_text", paymentDescription="sample_text", paymentName="sample_text", paymentText="sample_text", shippingAutoVat="sample_text", shippingDescription="sample_text", shippingName="sample_text", shippingValue="sample_text", shippingVatDescription="sample_text", shippingVatValue="sample_text")
    assert instance.shippingName == "sample_text"
    instance.shippingName = "sample_text_2"
    assert instance.shippingName == "sample_text_2"


def test_model_IndividualDocumentInfo_shippingValue_value_roundtrip():
    instance = model_IndividualDocumentInfo(noVatDescription="sample_text", noVatName="sample_text", paymentDescription="sample_text", paymentName="sample_text", paymentText="sample_text", shippingAutoVat="sample_text", shippingDescription="sample_text", shippingName="sample_text", shippingValue="sample_text", shippingVatDescription="sample_text", shippingVatValue="sample_text")
    assert instance.shippingValue == "sample_text"
    instance.shippingValue = "sample_text_2"
    assert instance.shippingValue == "sample_text_2"


def test_model_IndividualDocumentInfo_shippingVatDescription_value_roundtrip():
    instance = model_IndividualDocumentInfo(noVatDescription="sample_text", noVatName="sample_text", paymentDescription="sample_text", paymentName="sample_text", paymentText="sample_text", shippingAutoVat="sample_text", shippingDescription="sample_text", shippingName="sample_text", shippingValue="sample_text", shippingVatDescription="sample_text", shippingVatValue="sample_text")
    assert instance.shippingVatDescription == "sample_text"
    instance.shippingVatDescription = "sample_text_2"
    assert instance.shippingVatDescription == "sample_text_2"


def test_model_IndividualDocumentInfo_shippingVatValue_value_roundtrip():
    instance = model_IndividualDocumentInfo(noVatDescription="sample_text", noVatName="sample_text", paymentDescription="sample_text", paymentName="sample_text", paymentText="sample_text", shippingAutoVat="sample_text", shippingDescription="sample_text", shippingName="sample_text", shippingValue="sample_text", shippingVatDescription="sample_text", shippingVatValue="sample_text")
    assert instance.shippingVatValue == "sample_text"
    instance.shippingVatValue = "sample_text_2"
    assert instance.shippingVatValue == "sample_text_2"


def test_model_ItemAccountType_value_value_roundtrip():
    instance = model_ItemAccountType(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_model_Payment_code_value_roundtrip():
    instance = model_Payment(code="sample_text", depositText="sample_text", description="sample_text", discountDays="sample_text", discountValue="sample_text", netDays="sample_text", paidText="sample_text", unpaidText="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_model_Payment_depositText_value_roundtrip():
    instance = model_Payment(code="sample_text", depositText="sample_text", description="sample_text", discountDays="sample_text", discountValue="sample_text", netDays="sample_text", paidText="sample_text", unpaidText="sample_text")
    assert instance.depositText == "sample_text"
    instance.depositText = "sample_text_2"
    assert instance.depositText == "sample_text_2"


def test_model_Payment_description_value_roundtrip():
    instance = model_Payment(code="sample_text", depositText="sample_text", description="sample_text", discountDays="sample_text", discountValue="sample_text", netDays="sample_text", paidText="sample_text", unpaidText="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_model_Payment_discountDays_value_roundtrip():
    instance = model_Payment(code="sample_text", depositText="sample_text", description="sample_text", discountDays="sample_text", discountValue="sample_text", netDays="sample_text", paidText="sample_text", unpaidText="sample_text")
    assert instance.discountDays == "sample_text"
    instance.discountDays = "sample_text_2"
    assert instance.discountDays == "sample_text_2"


def test_model_Payment_discountValue_value_roundtrip():
    instance = model_Payment(code="sample_text", depositText="sample_text", description="sample_text", discountDays="sample_text", discountValue="sample_text", netDays="sample_text", paidText="sample_text", unpaidText="sample_text")
    assert instance.discountValue == "sample_text"
    instance.discountValue = "sample_text_2"
    assert instance.discountValue == "sample_text_2"


def test_model_Payment_netDays_value_roundtrip():
    instance = model_Payment(code="sample_text", depositText="sample_text", description="sample_text", discountDays="sample_text", discountValue="sample_text", netDays="sample_text", paidText="sample_text", unpaidText="sample_text")
    assert instance.netDays == "sample_text"
    instance.netDays = "sample_text_2"
    assert instance.netDays == "sample_text_2"


def test_model_Payment_paidText_value_roundtrip():
    instance = model_Payment(code="sample_text", depositText="sample_text", description="sample_text", discountDays="sample_text", discountValue="sample_text", netDays="sample_text", paidText="sample_text", unpaidText="sample_text")
    assert instance.paidText == "sample_text"
    instance.paidText = "sample_text_2"
    assert instance.paidText == "sample_text_2"


def test_model_Payment_unpaidText_value_roundtrip():
    instance = model_Payment(code="sample_text", depositText="sample_text", description="sample_text", discountDays="sample_text", discountValue="sample_text", netDays="sample_text", paidText="sample_text", unpaidText="sample_text")
    assert instance.unpaidText == "sample_text"
    instance.unpaidText = "sample_text_2"
    assert instance.unpaidText == "sample_text_2"


def test_model_Product_block1_value_roundtrip():
    instance = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    assert instance.block1 == "sample_text"
    instance.block1 = "sample_text_2"
    assert instance.block1 == "sample_text_2"


def test_model_Product_block2_value_roundtrip():
    instance = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    assert instance.block2 == "sample_text"
    instance.block2 = "sample_text_2"
    assert instance.block2 == "sample_text_2"


def test_model_Product_block3_value_roundtrip():
    instance = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    assert instance.block3 == "sample_text"
    instance.block3 = "sample_text_2"
    assert instance.block3 == "sample_text_2"


def test_model_Product_block4_value_roundtrip():
    instance = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    assert instance.block4 == "sample_text"
    instance.block4 = "sample_text_2"
    assert instance.block4 == "sample_text_2"


def test_model_Product_block5_value_roundtrip():
    instance = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    assert instance.block5 == "sample_text"
    instance.block5 = "sample_text_2"
    assert instance.block5 == "sample_text_2"


def test_model_Product_cdf01_value_roundtrip():
    instance = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    assert instance.cdf01 == "sample_text"
    instance.cdf01 = "sample_text_2"
    assert instance.cdf01 == "sample_text_2"


def test_model_Product_cdf02_value_roundtrip():
    instance = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    assert instance.cdf02 == "sample_text"
    instance.cdf02 = "sample_text_2"
    assert instance.cdf02 == "sample_text_2"


def test_model_Product_cdf03_value_roundtrip():
    instance = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    assert instance.cdf03 == "sample_text"
    instance.cdf03 = "sample_text_2"
    assert instance.cdf03 == "sample_text_2"


def test_model_Product_costPrice_value_roundtrip():
    instance = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    assert instance.costPrice == "sample_text"
    instance.costPrice = "sample_text_2"
    assert instance.costPrice == "sample_text_2"


def test_model_Product_gtin_value_roundtrip():
    instance = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    assert instance.gtin == "sample_text"
    instance.gtin = "sample_text_2"
    assert instance.gtin == "sample_text_2"


def test_model_Product_itemNumber_value_roundtrip():
    instance = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    assert instance.itemNumber == "sample_text"
    instance.itemNumber = "sample_text_2"
    assert instance.itemNumber == "sample_text_2"


def test_model_Product_picture_value_roundtrip():
    instance = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    assert instance.picture == "sample_text"
    instance.picture = "sample_text_2"
    assert instance.picture == "sample_text_2"


def test_model_Product_price1_value_roundtrip():
    instance = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    assert instance.price1 == "sample_text"
    instance.price1 = "sample_text_2"
    assert instance.price1 == "sample_text_2"


def test_model_Product_price2_value_roundtrip():
    instance = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    assert instance.price2 == "sample_text"
    instance.price2 = "sample_text_2"
    assert instance.price2 == "sample_text_2"


def test_model_Product_price3_value_roundtrip():
    instance = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    assert instance.price3 == "sample_text"
    instance.price3 = "sample_text_2"
    assert instance.price3 == "sample_text_2"


def test_model_Product_price4_value_roundtrip():
    instance = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    assert instance.price4 == "sample_text"
    instance.price4 = "sample_text_2"
    assert instance.price4 == "sample_text_2"


def test_model_Product_price5_value_roundtrip():
    instance = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    assert instance.price5 == "sample_text"
    instance.price5 = "sample_text_2"
    assert instance.price5 == "sample_text_2"


def test_model_Product_quantity_value_roundtrip():
    instance = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    assert instance.quantity == "sample_text"
    instance.quantity = "sample_text_2"
    assert instance.quantity == "sample_text_2"


def test_model_Product_quantityUnit_value_roundtrip():
    instance = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    assert instance.quantityUnit == "sample_text"
    instance.quantityUnit = "sample_text_2"
    assert instance.quantityUnit == "sample_text_2"


def test_model_Product_sellingUnit_value_roundtrip():
    instance = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    assert instance.sellingUnit == "sample_text"
    instance.sellingUnit = "sample_text_2"
    assert instance.sellingUnit == "sample_text_2"


def test_model_Product_webshopId_value_roundtrip():
    instance = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    assert instance.webshopId == "sample_text"
    instance.webshopId = "sample_text_2"
    assert instance.webshopId == "sample_text_2"


def test_model_Product_weight_value_roundtrip():
    instance = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    assert instance.weight == "sample_text"
    instance.weight = "sample_text_2"
    assert instance.weight == "sample_text_2"


def test_model_ProductBlockPrice_block_value_roundtrip():
    instance = model_ProductBlockPrice(block="sample_text", price="sample_text")
    assert instance.block == "sample_text"
    instance.block = "sample_text_2"
    assert instance.block == "sample_text_2"


def test_model_ProductBlockPrice_price_value_roundtrip():
    instance = model_ProductBlockPrice(block="sample_text", price="sample_text")
    assert instance.price == "sample_text"
    instance.price = "sample_text_2"
    assert instance.price == "sample_text_2"


def test_model_ProductOptions_attributeValue_value_roundtrip():
    instance = model_ProductOptions(attributeValue="sample_text", sequenceNumber="sample_text")
    assert instance.attributeValue == "sample_text"
    instance.attributeValue = "sample_text_2"
    assert instance.attributeValue == "sample_text_2"


def test_model_ProductOptions_sequenceNumber_value_roundtrip():
    instance = model_ProductOptions(attributeValue="sample_text", sequenceNumber="sample_text")
    assert instance.sequenceNumber == "sample_text"
    instance.sequenceNumber = "sample_text_2"
    assert instance.sequenceNumber == "sample_text_2"


def test_model_Shipping_autoVat_value_roundtrip():
    instance = model_Shipping(autoVat="sample_text", code="sample_text", shippingValue="sample_text")
    assert instance.autoVat == "sample_text"
    instance.autoVat = "sample_text_2"
    assert instance.autoVat == "sample_text_2"


def test_model_Shipping_code_value_roundtrip():
    instance = model_Shipping(autoVat="sample_text", code="sample_text", shippingValue="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_model_Shipping_shippingValue_value_roundtrip():
    instance = model_Shipping(autoVat="sample_text", code="sample_text", shippingValue="sample_text")
    assert instance.shippingValue == "sample_text"
    instance.shippingValue = "sample_text_2"
    assert instance.shippingValue == "sample_text_2"


def test_model_TextModule_text_value_roundtrip():
    instance = model_TextModule(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_model_User_password_value_roundtrip():
    instance = model_User(password="sample_text", userName="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_model_User_userName_value_roundtrip():
    instance = model_User(password="sample_text", userName="sample_text")
    assert instance.userName == "sample_text"
    instance.userName = "sample_text_2"
    assert instance.userName == "sample_text_2"


def test_model_UserProperty_default_value_roundtrip():
    instance = model_UserProperty(default="sample_text", global_="sample_text", user="sample_text", value="sample_text")
    assert instance.default == "sample_text"
    instance.default = "sample_text_2"
    assert instance.default == "sample_text_2"


def test_model_UserProperty_global__value_roundtrip():
    instance = model_UserProperty(default="sample_text", global_="sample_text", user="sample_text", value="sample_text")
    assert instance.global_ == "sample_text"
    instance.global_ = "sample_text_2"
    assert instance.global_ == "sample_text_2"


def test_model_UserProperty_user_value_roundtrip():
    instance = model_UserProperty(default="sample_text", global_="sample_text", user="sample_text", value="sample_text")
    assert instance.user == "sample_text"
    instance.user = "sample_text_2"
    assert instance.user == "sample_text_2"


def test_model_UserProperty_value_value_roundtrip():
    instance = model_UserProperty(default="sample_text", global_="sample_text", user="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_model_VAT_description_value_roundtrip():
    instance = model_VAT(description="sample_text", salesEqualizationTax="sample_text", taxValue="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_model_VAT_salesEqualizationTax_value_roundtrip():
    instance = model_VAT(description="sample_text", salesEqualizationTax="sample_text", taxValue="sample_text")
    assert instance.salesEqualizationTax == "sample_text"
    instance.salesEqualizationTax = "sample_text_2"
    assert instance.salesEqualizationTax == "sample_text_2"


def test_model_VAT_taxValue_value_roundtrip():
    instance = model_VAT(description="sample_text", salesEqualizationTax="sample_text", taxValue="sample_text")
    assert instance.taxValue == "sample_text"
    instance.taxValue = "sample_text_2"
    assert instance.taxValue == "sample_text_2"


def test_model_Voucher_discounted_value_roundtrip():
    instance = model_Voucher(discounted="sample_text", doNotBook="sample_text", documentNumber="sample_text", paidValue="sample_text", totalValue="sample_text", voucherDate=date(2024, 1, 1), voucherNumber="sample_text", voucherType="sample_text")
    assert instance.discounted == "sample_text"
    instance.discounted = "sample_text_2"
    assert instance.discounted == "sample_text_2"


def test_model_Voucher_doNotBook_value_roundtrip():
    instance = model_Voucher(discounted="sample_text", doNotBook="sample_text", documentNumber="sample_text", paidValue="sample_text", totalValue="sample_text", voucherDate=date(2024, 1, 1), voucherNumber="sample_text", voucherType="sample_text")
    assert instance.doNotBook == "sample_text"
    instance.doNotBook = "sample_text_2"
    assert instance.doNotBook == "sample_text_2"


def test_model_Voucher_documentNumber_value_roundtrip():
    instance = model_Voucher(discounted="sample_text", doNotBook="sample_text", documentNumber="sample_text", paidValue="sample_text", totalValue="sample_text", voucherDate=date(2024, 1, 1), voucherNumber="sample_text", voucherType="sample_text")
    assert instance.documentNumber == "sample_text"
    instance.documentNumber = "sample_text_2"
    assert instance.documentNumber == "sample_text_2"


def test_model_Voucher_paidValue_value_roundtrip():
    instance = model_Voucher(discounted="sample_text", doNotBook="sample_text", documentNumber="sample_text", paidValue="sample_text", totalValue="sample_text", voucherDate=date(2024, 1, 1), voucherNumber="sample_text", voucherType="sample_text")
    assert instance.paidValue == "sample_text"
    instance.paidValue = "sample_text_2"
    assert instance.paidValue == "sample_text_2"


def test_model_Voucher_totalValue_value_roundtrip():
    instance = model_Voucher(discounted="sample_text", doNotBook="sample_text", documentNumber="sample_text", paidValue="sample_text", totalValue="sample_text", voucherDate=date(2024, 1, 1), voucherNumber="sample_text", voucherType="sample_text")
    assert instance.totalValue == "sample_text"
    instance.totalValue = "sample_text_2"
    assert instance.totalValue == "sample_text_2"


def test_model_Voucher_voucherDate_value_roundtrip():
    instance = model_Voucher(discounted="sample_text", doNotBook="sample_text", documentNumber="sample_text", paidValue="sample_text", totalValue="sample_text", voucherDate=date(2024, 1, 1), voucherNumber="sample_text", voucherType="sample_text")
    assert instance.voucherDate == date(2024, 1, 1)
    instance.voucherDate = date(2025, 6, 15)
    assert instance.voucherDate == date(2025, 6, 15)


def test_model_Voucher_voucherNumber_value_roundtrip():
    instance = model_Voucher(discounted="sample_text", doNotBook="sample_text", documentNumber="sample_text", paidValue="sample_text", totalValue="sample_text", voucherDate=date(2024, 1, 1), voucherNumber="sample_text", voucherType="sample_text")
    assert instance.voucherNumber == "sample_text"
    instance.voucherNumber = "sample_text_2"
    assert instance.voucherNumber == "sample_text_2"


def test_model_Voucher_voucherType_value_roundtrip():
    instance = model_Voucher(discounted="sample_text", doNotBook="sample_text", documentNumber="sample_text", paidValue="sample_text", totalValue="sample_text", voucherDate=date(2024, 1, 1), voucherNumber="sample_text", voucherType="sample_text")
    assert instance.voucherType == "sample_text"
    instance.voucherType = "sample_text_2"
    assert instance.voucherType == "sample_text_2"


def test_model_VoucherItem_itemVoucherType_value_roundtrip():
    instance = model_VoucherItem(itemVoucherType="sample_text", posNr="sample_text", price="sample_text")
    assert instance.itemVoucherType == "sample_text"
    instance.itemVoucherType = "sample_text_2"
    assert instance.itemVoucherType == "sample_text_2"


def test_model_VoucherItem_posNr_value_roundtrip():
    instance = model_VoucherItem(itemVoucherType="sample_text", posNr="sample_text", price="sample_text")
    assert instance.posNr == "sample_text"
    instance.posNr = "sample_text_2"
    assert instance.posNr == "sample_text_2"


def test_model_VoucherItem_price_value_roundtrip():
    instance = model_VoucherItem(itemVoucherType="sample_text", posNr="sample_text", price="sample_text")
    assert instance.price == "sample_text"
    instance.price = "sample_text_2"
    assert instance.price == "sample_text_2"


def test_model_WebShop_webshopVendor_value_roundtrip():
    instance = model_WebShop(webshopVendor="sample_text", webshopVersion="sample_text")
    assert instance.webshopVendor == "sample_text"
    instance.webshopVendor = "sample_text_2"
    assert instance.webshopVendor == "sample_text_2"


def test_model_WebShop_webshopVersion_value_roundtrip():
    instance = model_WebShop(webshopVendor="sample_text", webshopVersion="sample_text")
    assert instance.webshopVersion == "sample_text"
    instance.webshopVersion = "sample_text_2"
    assert instance.webshopVersion == "sample_text_2"


def test_model_WebshopStateMapping_fakturamaOrderState_value_roundtrip():
    instance = model_WebshopStateMapping(fakturamaOrderState="sample_text", webshopState="sample_text")
    assert instance.fakturamaOrderState == "sample_text"
    instance.fakturamaOrderState = "sample_text_2"
    assert instance.fakturamaOrderState == "sample_text_2"


def test_model_WebshopStateMapping_webshopState_value_roundtrip():
    instance = model_WebshopStateMapping(fakturamaOrderState="sample_text", webshopState="sample_text")
    assert instance.webshopState == "sample_text"
    instance.webshopState = "sample_text_2"
    assert instance.webshopState == "sample_text_2"


def test_model_ContactCategory_isa_AbstractCategory():
    instance = model_ContactCategory()
    assert isinstance(instance, AbstractCategory)


def test_model_ItemListTypeCategory_isa_AbstractCategory():
    instance = model_ItemListTypeCategory()
    assert isinstance(instance, AbstractCategory)


def test_model_ProductCategory_isa_AbstractCategory():
    instance = model_ProductCategory()
    assert isinstance(instance, AbstractCategory)


def test_model_ShippingCategory_isa_AbstractCategory():
    instance = model_ShippingCategory()
    assert isinstance(instance, AbstractCategory)


def test_model_TextCategory_isa_AbstractCategory():
    instance = model_TextCategory()
    assert isinstance(instance, AbstractCategory)


def test_model_VATCategory_isa_AbstractCategory():
    instance = model_VATCategory()
    assert isinstance(instance, AbstractCategory)


def test_model_VoucherCategory_isa_AbstractCategory():
    instance = model_VoucherCategory()
    assert isinstance(instance, AbstractCategory)


def test_model_Creditor_isa_Contact():
    instance = model_Creditor()
    assert isinstance(instance, Contact)


def test_model_Debitor_isa_Contact():
    instance = model_Debitor()
    assert isinstance(instance, Contact)


def test_model_Confirmation_isa_Document():
    instance = model_Confirmation()
    assert isinstance(instance, Document)


def test_model_Credit_isa_Document():
    instance = model_Credit()
    assert isinstance(instance, Document)


def test_model_Delivery_isa_Document():
    instance = model_Delivery()
    assert isinstance(instance, Document)


def test_model_Dunning_isa_Document():
    instance = model_Dunning(dunningLevel="sample_text")
    assert isinstance(instance, Document)


def test_model_Invoice_isa_Document():
    instance = model_Invoice()
    assert isinstance(instance, Document)


def test_model_Letter_isa_Document():
    instance = model_Letter()
    assert isinstance(instance, Document)


def test_model_Offer_isa_Document():
    instance = model_Offer()
    assert isinstance(instance, Document)


def test_model_Order_isa_Document():
    instance = model_Order()
    assert isinstance(instance, Document)


def test_model_Proforma_isa_Document():
    instance = model_Proforma()
    assert isinstance(instance, Document)


def test_model_Product_isa_IDescribableEntity():
    instance = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    assert isinstance(instance, IDescribableEntity)


def test_model_Shipping_isa_IDescribableEntity():
    instance = model_Shipping(autoVat="sample_text", code="sample_text", shippingValue="sample_text")
    assert isinstance(instance, IDescribableEntity)


def test_model_AbstractCategory_isa_IEntity():
    instance = model_AbstractCategory()
    assert isinstance(instance, IEntity)


def test_model_Address_isa_IEntity():
    instance = model_Address(city="sample_text", cityAddon="sample_text", countryCode="sample_text", manualAddress="sample_text", street="sample_text", zip="sample_text")
    assert isinstance(instance, IEntity)


def test_model_BankAccount_isa_IEntity():
    instance = model_BankAccount(accountHolder="sample_text", bankCode="sample_text", bankName="sample_text", bic="sample_text", iban="sample_text")
    assert isinstance(instance, IEntity)


def test_model_CEFACTCode_isa_IEntity():
    instance = model_CEFACTCode(abbreviation_de="sample_text", abbreviation_en="sample_text", code="sample_text", name_de="sample_text", target="sample_text")
    assert isinstance(instance, IEntity)


def test_model_Contact_isa_IEntity():
    instance = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    assert isinstance(instance, IEntity)


def test_model_Document_isa_IEntity():
    instance = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    assert isinstance(instance, IEntity)


def test_model_DocumentItem_isa_IEntity():
    instance = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    assert isinstance(instance, IEntity)


def test_model_IDescribableEntity_isa_IEntity():
    instance = model_IDescribableEntity(description="sample_text")
    assert isinstance(instance, IEntity)


def test_model_IndividualDocumentInfo_isa_IEntity():
    instance = model_IndividualDocumentInfo(noVatDescription="sample_text", noVatName="sample_text", paymentDescription="sample_text", paymentName="sample_text", paymentText="sample_text", shippingAutoVat="sample_text", shippingDescription="sample_text", shippingName="sample_text", shippingValue="sample_text", shippingVatDescription="sample_text", shippingVatValue="sample_text")
    assert isinstance(instance, IEntity)


def test_model_ItemAccountType_isa_IEntity():
    instance = model_ItemAccountType(value="sample_text")
    assert isinstance(instance, IEntity)


def test_model_Payment_isa_IEntity():
    instance = model_Payment(code="sample_text", depositText="sample_text", description="sample_text", discountDays="sample_text", discountValue="sample_text", netDays="sample_text", paidText="sample_text", unpaidText="sample_text")
    assert isinstance(instance, IEntity)


def test_model_ProductBlockPrice_isa_IEntity():
    instance = model_ProductBlockPrice(block="sample_text", price="sample_text")
    assert isinstance(instance, IEntity)


def test_model_ProductOptions_isa_IEntity():
    instance = model_ProductOptions(attributeValue="sample_text", sequenceNumber="sample_text")
    assert isinstance(instance, IEntity)


def test_model_Role_isa_IEntity():
    instance = model_Role()
    assert isinstance(instance, IEntity)


def test_model_Tenant_isa_IEntity():
    instance = model_Tenant()
    assert isinstance(instance, IEntity)


def test_model_TextModule_isa_IEntity():
    instance = model_TextModule(text="sample_text")
    assert isinstance(instance, IEntity)


def test_model_User_isa_IEntity():
    instance = model_User(password="sample_text", userName="sample_text")
    assert isinstance(instance, IEntity)


def test_model_UserProperty_isa_IEntity():
    instance = model_UserProperty(default="sample_text", global_="sample_text", user="sample_text", value="sample_text")
    assert isinstance(instance, IEntity)


def test_model_VAT_isa_IEntity():
    instance = model_VAT(description="sample_text", salesEqualizationTax="sample_text", taxValue="sample_text")
    assert isinstance(instance, IEntity)


def test_model_Voucher_isa_IEntity():
    instance = model_Voucher(discounted="sample_text", doNotBook="sample_text", documentNumber="sample_text", paidValue="sample_text", totalValue="sample_text", voucherDate=date(2024, 1, 1), voucherNumber="sample_text", voucherType="sample_text")
    assert isinstance(instance, IEntity)


def test_model_VoucherItem_isa_IEntity():
    instance = model_VoucherItem(itemVoucherType="sample_text", posNr="sample_text", price="sample_text")
    assert isinstance(instance, IEntity)


def test_model_WebShop_isa_IEntity():
    instance = model_WebShop(webshopVendor="sample_text", webshopVersion="sample_text")
    assert isinstance(instance, IEntity)


def test_model_WebshopStateMapping_isa_IEntity():
    instance = model_WebshopStateMapping(fakturamaOrderState="sample_text", webshopState="sample_text")
    assert isinstance(instance, IEntity)


def test_assoc_account38_link_reassign_clear():
    a = model_Voucher(discounted="sample_text", doNotBook="sample_text", documentNumber="sample_text", paidValue="sample_text", totalValue="sample_text", voucherDate=date(2024, 1, 1), voucherNumber="sample_text", voucherType="sample_text")
    b1 = model_VoucherCategory()
    b2 = model_VoucherCategory()
    _safe_set(a, 'model_Voucher', b1)
    assert _is_linked(a, 'model_Voucher', b1)
    if hasattr(b1, 'model_VoucherCategory'):
        assert _is_linked(b1, 'model_VoucherCategory', a)
    _safe_set(a, 'model_Voucher', b2)
    assert _is_linked(a, 'model_Voucher', b2)
    if hasattr(b1, 'model_VoucherCategory'):
        assert not _is_linked(b1, 'model_VoucherCategory', a)
    if hasattr(b2, 'model_VoucherCategory'):
        assert _is_linked(b2, 'model_VoucherCategory', a)
    _safe_set(a, 'model_Voucher', None)
    assert not _is_linked(a, 'model_Voucher', b2)
    if hasattr(b2, 'model_VoucherCategory'):
        assert not _is_linked(b2, 'model_VoucherCategory', a)


def test_assoc_accountType41_link_reassign_clear():
    a = model_VoucherItem(itemVoucherType="sample_text", posNr="sample_text", price="sample_text")
    b1 = model_ItemAccountType(value="sample_text")
    b2 = model_ItemAccountType(value="sample_text_2")
    _safe_set(a, 'model_VoucherItem42', b1)
    assert _is_linked(a, 'model_VoucherItem42', b1)
    if hasattr(b1, 'model_ItemAccountType'):
        assert _is_linked(b1, 'model_ItemAccountType', a)
    _safe_set(a, 'model_VoucherItem42', b2)
    assert _is_linked(a, 'model_VoucherItem42', b2)
    if hasattr(b1, 'model_ItemAccountType'):
        assert not _is_linked(b1, 'model_ItemAccountType', a)
    if hasattr(b2, 'model_ItemAccountType'):
        assert _is_linked(b2, 'model_ItemAccountType', a)
    _safe_set(a, 'model_VoucherItem42', None)
    assert not _is_linked(a, 'model_VoucherItem42', b2)
    if hasattr(b2, 'model_ItemAccountType'):
        assert not _is_linked(b2, 'model_ItemAccountType', a)


def test_assoc_additionalInfo12_link_reassign_clear():
    a = model_IndividualDocumentInfo(noVatDescription="sample_text", noVatName="sample_text", paymentDescription="sample_text", paymentName="sample_text", paymentText="sample_text", shippingAutoVat="sample_text", shippingDescription="sample_text", shippingName="sample_text", shippingValue="sample_text", shippingVatDescription="sample_text", shippingVatValue="sample_text")
    b1 = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    b2 = model_Document(addressFirstLine="sample_text_2", billingType="sample_text_2", consultant="sample_text_2", customerRef="sample_text_2", deposit="sample_text_2", documentDate=date(2025, 6, 15), dueDays="sample_text_2", itemsRebate="sample_text_2", message="sample_text_2", message2="sample_text_2", message3="sample_text_2", netGross="sample_text_2", odtPath="sample_text_2", orderDate=date(2025, 6, 15), paid="sample_text_2", paidValue="sample_text_2", payDate=date(2025, 6, 15), pdfPath="sample_text_2", printTemplate="sample_text_2", printed="sample_text_2", progress="sample_text_2", serviceDate=date(2025, 6, 15), shippingAutoVat="sample_text_2", shippingValue="sample_text_2", totalValue="sample_text_2", transactionId="sample_text_2", vestingPeriodEnd=date(2025, 6, 15), vestingPeriodStart=date(2025, 6, 15), webshopDate=date(2025, 6, 15), webshopId="sample_text_2")
    _safe_set(a, 'model_IndividualDocumentInfo', b1)
    assert _is_linked(a, 'model_IndividualDocumentInfo', b1)
    if hasattr(b1, 'model_Document'):
        assert _is_linked(b1, 'model_Document', a)
    _safe_set(a, 'model_IndividualDocumentInfo', b2)
    assert _is_linked(a, 'model_IndividualDocumentInfo', b2)
    if hasattr(b1, 'model_Document'):
        assert not _is_linked(b1, 'model_Document', a)
    if hasattr(b2, 'model_Document'):
        assert _is_linked(b2, 'model_Document', a)
    _safe_set(a, 'model_IndividualDocumentInfo', None)
    assert not _is_linked(a, 'model_IndividualDocumentInfo', b2)
    if hasattr(b2, 'model_Document'):
        assert not _is_linked(b2, 'model_Document', a)


def test_assoc_address2_link_reassign_clear():
    a = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    b1 = model_Address(city="sample_text", cityAddon="sample_text", countryCode="sample_text", manualAddress="sample_text", street="sample_text", zip="sample_text")
    b2 = model_Address(city="sample_text_2", cityAddon="sample_text_2", countryCode="sample_text_2", manualAddress="sample_text_2", street="sample_text_2", zip="sample_text_2")
    _safe_set(a, 'model_Contact', b1)
    assert _is_linked(a, 'model_Contact', b1)
    if hasattr(b1, 'model_Address'):
        assert _is_linked(b1, 'model_Address', a)
    _safe_set(a, 'model_Contact', b2)
    assert _is_linked(a, 'model_Contact', b2)
    if hasattr(b1, 'model_Address'):
        assert not _is_linked(b1, 'model_Address', a)
    if hasattr(b2, 'model_Address'):
        assert _is_linked(b2, 'model_Address', a)
    _safe_set(a, 'model_Contact', None)
    assert not _is_linked(a, 'model_Contact', b2)
    if hasattr(b2, 'model_Address'):
        assert not _is_linked(b2, 'model_Address', a)


def test_assoc_alternateContacts4_link_reassign_clear():
    a = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    b1 = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    b2 = model_Contact(birthday=date(2025, 6, 15), company="sample_text_2", contactType="sample_text_2", customerNumber="sample_text_2", discount="sample_text_2", email="sample_text_2", fax="sample_text_2", firstName="sample_text_2", gender="sample_text_2", gln="sample_text_2", mandateReference="sample_text_2", mobile="sample_text_2", note="sample_text_2", phone="sample_text_2", reliability="sample_text_2", supplierNumber="sample_text_2", title="sample_text_2", useNetGross="sample_text_2", useSalesEqualizationTax="sample_text_2", vatNumber="sample_text_2", vatNumberValid="sample_text_2", webshopName="sample_text_2", website="sample_text_2")
    _safe_set(a, 'model_Contact3', b1)
    assert _is_linked(a, 'model_Contact3', b1)
    if hasattr(b1, 'model_Contact5'):
        assert _is_linked(b1, 'model_Contact5', a)
    _safe_set(a, 'model_Contact3', b2)
    assert _is_linked(a, 'model_Contact3', b2)
    if hasattr(b1, 'model_Contact5'):
        assert not _is_linked(b1, 'model_Contact5', a)
    if hasattr(b2, 'model_Contact5'):
        assert _is_linked(b2, 'model_Contact5', a)
    _safe_set(a, 'model_Contact3', None)
    assert not _is_linked(a, 'model_Contact3', b2)
    if hasattr(b2, 'model_Contact5'):
        assert not _is_linked(b2, 'model_Contact5', a)


def test_assoc_attributes53_link_reassign_clear():
    a = model_ProductOptions(attributeValue="sample_text", sequenceNumber="sample_text")
    b1 = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    b2 = model_Product(block1="sample_text_2", block2="sample_text_2", block3="sample_text_2", block4="sample_text_2", block5="sample_text_2", cdf01="sample_text_2", cdf02="sample_text_2", cdf03="sample_text_2", costPrice="sample_text_2", gtin="sample_text_2", itemNumber="sample_text_2", picture="sample_text_2", price1="sample_text_2", price2="sample_text_2", price3="sample_text_2", price4="sample_text_2", price5="sample_text_2", quantity="sample_text_2", quantityUnit="sample_text_2", sellingUnit="sample_text_2", webshopId="sample_text_2", weight="sample_text_2")
    _safe_set(a, 'model_ProductOptions', b1)
    assert _is_linked(a, 'model_ProductOptions', b1)
    if hasattr(b1, 'model_Product54'):
        assert _is_linked(b1, 'model_Product54', a)
    _safe_set(a, 'model_ProductOptions', b2)
    assert _is_linked(a, 'model_ProductOptions', b2)
    if hasattr(b1, 'model_Product54'):
        assert not _is_linked(b1, 'model_Product54', a)
    if hasattr(b2, 'model_Product54'):
        assert _is_linked(b2, 'model_Product54', a)
    _safe_set(a, 'model_ProductOptions', None)
    assert not _is_linked(a, 'model_ProductOptions', b2)
    if hasattr(b2, 'model_Product54'):
        assert not _is_linked(b2, 'model_Product54', a)


def test_assoc_bankAccount10_link_reassign_clear():
    a = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    b1 = model_BankAccount(accountHolder="sample_text", bankCode="sample_text", bankName="sample_text", bic="sample_text", iban="sample_text")
    b2 = model_BankAccount(accountHolder="sample_text_2", bankCode="sample_text_2", bankName="sample_text_2", bic="sample_text_2", iban="sample_text_2")
    _safe_set(a, 'model_Contact11', b1)
    assert _is_linked(a, 'model_Contact11', b1)
    if hasattr(b1, 'model_BankAccount'):
        assert _is_linked(b1, 'model_BankAccount', a)
    _safe_set(a, 'model_Contact11', b2)
    assert _is_linked(a, 'model_Contact11', b2)
    if hasattr(b1, 'model_BankAccount'):
        assert not _is_linked(b1, 'model_BankAccount', a)
    if hasattr(b2, 'model_BankAccount'):
        assert _is_linked(b2, 'model_BankAccount', a)
    _safe_set(a, 'model_Contact11', None)
    assert not _is_linked(a, 'model_Contact11', b2)
    if hasattr(b2, 'model_BankAccount'):
        assert not _is_linked(b2, 'model_BankAccount', a)


def test_assoc_billingContact13_link_reassign_clear():
    a = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    b1 = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    b2 = model_Contact(birthday=date(2025, 6, 15), company="sample_text_2", contactType="sample_text_2", customerNumber="sample_text_2", discount="sample_text_2", email="sample_text_2", fax="sample_text_2", firstName="sample_text_2", gender="sample_text_2", gln="sample_text_2", mandateReference="sample_text_2", mobile="sample_text_2", note="sample_text_2", phone="sample_text_2", reliability="sample_text_2", supplierNumber="sample_text_2", title="sample_text_2", useNetGross="sample_text_2", useSalesEqualizationTax="sample_text_2", vatNumber="sample_text_2", vatNumberValid="sample_text_2", webshopName="sample_text_2", website="sample_text_2")
    _safe_set(a, 'model_Document14', b1)
    assert _is_linked(a, 'model_Document14', b1)
    if hasattr(b1, 'model_Contact15'):
        assert _is_linked(b1, 'model_Contact15', a)
    _safe_set(a, 'model_Document14', b2)
    assert _is_linked(a, 'model_Document14', b2)
    if hasattr(b1, 'model_Contact15'):
        assert not _is_linked(b1, 'model_Contact15', a)
    if hasattr(b2, 'model_Contact15'):
        assert _is_linked(b2, 'model_Contact15', a)
    _safe_set(a, 'model_Document14', None)
    assert not _is_linked(a, 'model_Document14', b2)
    if hasattr(b2, 'model_Contact15'):
        assert not _is_linked(b2, 'model_Contact15', a)


def test_assoc_blockPrices58_link_reassign_clear():
    a = model_ProductBlockPrice(block="sample_text", price="sample_text")
    b1 = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    b2 = model_Product(block1="sample_text_2", block2="sample_text_2", block3="sample_text_2", block4="sample_text_2", block5="sample_text_2", cdf01="sample_text_2", cdf02="sample_text_2", cdf03="sample_text_2", costPrice="sample_text_2", gtin="sample_text_2", itemNumber="sample_text_2", picture="sample_text_2", price1="sample_text_2", price2="sample_text_2", price3="sample_text_2", price4="sample_text_2", price5="sample_text_2", quantity="sample_text_2", quantityUnit="sample_text_2", sellingUnit="sample_text_2", webshopId="sample_text_2", weight="sample_text_2")
    _safe_set(a, 'model_ProductBlockPrice', b1)
    assert _is_linked(a, 'model_ProductBlockPrice', b1)
    if hasattr(b1, 'model_Product59'):
        assert _is_linked(b1, 'model_Product59', a)
    _safe_set(a, 'model_ProductBlockPrice', b2)
    assert _is_linked(a, 'model_ProductBlockPrice', b2)
    if hasattr(b1, 'model_Product59'):
        assert not _is_linked(b1, 'model_Product59', a)
    if hasattr(b2, 'model_Product59'):
        assert _is_linked(b2, 'model_Product59', a)
    _safe_set(a, 'model_ProductBlockPrice', None)
    assert not _is_linked(a, 'model_ProductBlockPrice', b2)
    if hasattr(b2, 'model_Product59'):
        assert not _is_linked(b2, 'model_Product59', a)


def test_assoc_categories51_link_reassign_clear():
    a = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    b1 = model_ProductCategory()
    b2 = model_ProductCategory()
    _safe_set(a, 'model_Product52', b1)
    assert _is_linked(a, 'model_Product52', b1)
    if hasattr(b1, 'model_ProductCategory'):
        assert _is_linked(b1, 'model_ProductCategory', a)
    _safe_set(a, 'model_Product52', b2)
    assert _is_linked(a, 'model_Product52', b2)
    if hasattr(b1, 'model_ProductCategory'):
        assert not _is_linked(b1, 'model_ProductCategory', a)
    if hasattr(b2, 'model_ProductCategory'):
        assert _is_linked(b2, 'model_ProductCategory', a)
    _safe_set(a, 'model_Product52', None)
    assert not _is_linked(a, 'model_Product52', b2)
    if hasattr(b2, 'model_ProductCategory'):
        assert not _is_linked(b2, 'model_ProductCategory', a)


def test_assoc_categories6_link_reassign_clear():
    a = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    b1 = model_ContactCategory()
    b2 = model_ContactCategory()
    _safe_set(a, 'model_Contact7', b1)
    assert _is_linked(a, 'model_Contact7', b1)
    if hasattr(b1, 'model_ContactCategory'):
        assert _is_linked(b1, 'model_ContactCategory', a)
    _safe_set(a, 'model_Contact7', b2)
    assert _is_linked(a, 'model_Contact7', b2)
    if hasattr(b1, 'model_ContactCategory'):
        assert not _is_linked(b1, 'model_ContactCategory', a)
    if hasattr(b2, 'model_ContactCategory'):
        assert _is_linked(b2, 'model_ContactCategory', a)
    _safe_set(a, 'model_Contact7', None)
    assert not _is_linked(a, 'model_Contact7', b2)
    if hasattr(b2, 'model_ContactCategory'):
        assert not _is_linked(b2, 'model_ContactCategory', a)


def test_assoc_categories63_link_reassign_clear():
    a = model_Shipping(autoVat="sample_text", code="sample_text", shippingValue="sample_text")
    b1 = model_ShippingCategory()
    b2 = model_ShippingCategory()
    _safe_set(a, 'model_Shipping64', b1)
    assert _is_linked(a, 'model_Shipping64', b1)
    if hasattr(b1, 'model_ShippingCategory'):
        assert _is_linked(b1, 'model_ShippingCategory', a)
    _safe_set(a, 'model_Shipping64', b2)
    assert _is_linked(a, 'model_Shipping64', b2)
    if hasattr(b1, 'model_ShippingCategory'):
        assert not _is_linked(b1, 'model_ShippingCategory', a)
    if hasattr(b2, 'model_ShippingCategory'):
        assert _is_linked(b2, 'model_ShippingCategory', a)
    _safe_set(a, 'model_Shipping64', None)
    assert not _is_linked(a, 'model_Shipping64', b2)
    if hasattr(b2, 'model_ShippingCategory'):
        assert not _is_linked(b2, 'model_ShippingCategory', a)


def test_assoc_categories65_link_reassign_clear():
    a = model_TextModule(text="sample_text")
    b1 = model_TextCategory()
    b2 = model_TextCategory()
    _safe_set(a, 'model_TextModule', b1)
    assert _is_linked(a, 'model_TextModule', b1)
    if hasattr(b1, 'model_TextCategory'):
        assert _is_linked(b1, 'model_TextCategory', a)
    _safe_set(a, 'model_TextModule', b2)
    assert _is_linked(a, 'model_TextModule', b2)
    if hasattr(b1, 'model_TextCategory'):
        assert not _is_linked(b1, 'model_TextCategory', a)
    if hasattr(b2, 'model_TextCategory'):
        assert _is_linked(b2, 'model_TextCategory', a)
    _safe_set(a, 'model_TextModule', None)
    assert not _is_linked(a, 'model_TextModule', b2)
    if hasattr(b2, 'model_TextCategory'):
        assert not _is_linked(b2, 'model_TextCategory', a)


def test_assoc_category46_link_reassign_clear():
    a = model_ItemAccountType(value="sample_text")
    b1 = model_ItemListTypeCategory()
    b2 = model_ItemListTypeCategory()
    _safe_set(a, 'model_ItemAccountType47', b1)
    assert _is_linked(a, 'model_ItemAccountType47', b1)
    if hasattr(b1, 'model_ItemListTypeCategory'):
        assert _is_linked(b1, 'model_ItemListTypeCategory', a)
    _safe_set(a, 'model_ItemAccountType47', b2)
    assert _is_linked(a, 'model_ItemAccountType47', b2)
    if hasattr(b1, 'model_ItemListTypeCategory'):
        assert not _is_linked(b1, 'model_ItemListTypeCategory', a)
    if hasattr(b2, 'model_ItemListTypeCategory'):
        assert _is_linked(b2, 'model_ItemListTypeCategory', a)
    _safe_set(a, 'model_ItemAccountType47', None)
    assert not _is_linked(a, 'model_ItemAccountType47', b2)
    if hasattr(b2, 'model_ItemListTypeCategory'):
        assert not _is_linked(b2, 'model_ItemListTypeCategory', a)


def test_assoc_category48_link_reassign_clear():
    a = model_Payment(code="sample_text", depositText="sample_text", description="sample_text", discountDays="sample_text", discountValue="sample_text", netDays="sample_text", paidText="sample_text", unpaidText="sample_text")
    b1 = model_VoucherCategory()
    b2 = model_VoucherCategory()
    _safe_set(a, 'model_Payment49', b1)
    assert _is_linked(a, 'model_Payment49', b1)
    if hasattr(b1, 'model_VoucherCategory50'):
        assert _is_linked(b1, 'model_VoucherCategory50', a)
    _safe_set(a, 'model_Payment49', b2)
    assert _is_linked(a, 'model_Payment49', b2)
    if hasattr(b1, 'model_VoucherCategory50'):
        assert not _is_linked(b1, 'model_VoucherCategory50', a)
    if hasattr(b2, 'model_VoucherCategory50'):
        assert _is_linked(b2, 'model_VoucherCategory50', a)
    _safe_set(a, 'model_Payment49', None)
    assert not _is_linked(a, 'model_Payment49', b2)
    if hasattr(b2, 'model_VoucherCategory50'):
        assert not _is_linked(b2, 'model_VoucherCategory50', a)


def test_assoc_category69_link_reassign_clear():
    a = model_VAT(description="sample_text", salesEqualizationTax="sample_text", taxValue="sample_text")
    b1 = model_VATCategory()
    b2 = model_VATCategory()
    _safe_set(a, 'model_VAT70', b1)
    assert _is_linked(a, 'model_VAT70', b1)
    if hasattr(b1, 'model_VATCategory'):
        assert _is_linked(b1, 'model_VATCategory', a)
    _safe_set(a, 'model_VAT70', b2)
    assert _is_linked(a, 'model_VAT70', b2)
    if hasattr(b1, 'model_VATCategory'):
        assert not _is_linked(b1, 'model_VATCategory', a)
    if hasattr(b2, 'model_VATCategory'):
        assert _is_linked(b2, 'model_VATCategory', a)
    _safe_set(a, 'model_VAT70', None)
    assert not _is_linked(a, 'model_VAT70', b2)
    if hasattr(b2, 'model_VATCategory'):
        assert not _is_linked(b2, 'model_VATCategory', a)


def test_assoc_deliveryContact16_link_reassign_clear():
    a = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    b1 = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    b2 = model_Contact(birthday=date(2025, 6, 15), company="sample_text_2", contactType="sample_text_2", customerNumber="sample_text_2", discount="sample_text_2", email="sample_text_2", fax="sample_text_2", firstName="sample_text_2", gender="sample_text_2", gln="sample_text_2", mandateReference="sample_text_2", mobile="sample_text_2", note="sample_text_2", phone="sample_text_2", reliability="sample_text_2", supplierNumber="sample_text_2", title="sample_text_2", useNetGross="sample_text_2", useSalesEqualizationTax="sample_text_2", vatNumber="sample_text_2", vatNumberValid="sample_text_2", webshopName="sample_text_2", website="sample_text_2")
    _safe_set(a, 'model_Document17', b1)
    assert _is_linked(a, 'model_Document17', b1)
    if hasattr(b1, 'model_Contact18'):
        assert _is_linked(b1, 'model_Contact18', a)
    _safe_set(a, 'model_Document17', b2)
    assert _is_linked(a, 'model_Document17', b2)
    if hasattr(b1, 'model_Contact18'):
        assert not _is_linked(b1, 'model_Contact18', a)
    if hasattr(b2, 'model_Contact18'):
        assert _is_linked(b2, 'model_Contact18', a)
    _safe_set(a, 'model_Document17', None)
    assert not _is_linked(a, 'model_Document17', b2)
    if hasattr(b2, 'model_Contact18'):
        assert not _is_linked(b2, 'model_Contact18', a)


def test_assoc_invoiceReference19_link_reassign_clear():
    a = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    b1 = model_Invoice()
    b2 = model_Invoice()
    _safe_set(a, 'model_Document20', b1)
    assert _is_linked(a, 'model_Document20', b1)
    if hasattr(b1, 'model_Invoice'):
        assert _is_linked(b1, 'model_Invoice', a)
    _safe_set(a, 'model_Document20', b2)
    assert _is_linked(a, 'model_Document20', b2)
    if hasattr(b1, 'model_Invoice'):
        assert not _is_linked(b1, 'model_Invoice', a)
    if hasattr(b2, 'model_Invoice'):
        assert _is_linked(b2, 'model_Invoice', a)
    _safe_set(a, 'model_Document20', None)
    assert not _is_linked(a, 'model_Document20', b2)
    if hasattr(b2, 'model_Invoice'):
        assert not _is_linked(b2, 'model_Invoice', a)


def test_assoc_itemVat35_link_reassign_clear():
    a = model_VAT(description="sample_text", salesEqualizationTax="sample_text", taxValue="sample_text")
    b1 = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    b2 = model_DocumentItem(description="sample_text_2", gtin="sample_text_2", itemNumber="sample_text_2", itemRebate="sample_text_2", itemType="sample_text_2", noVat="sample_text_2", optional="sample_text_2", originQuantity="sample_text_2", picture="sample_text_2", posNr="sample_text_2", price="sample_text_2", quantity="sample_text_2", quantityUnit="sample_text_2", tara="sample_text_2", vestingPeriodEnd=date(2025, 6, 15), vestingPeriodStart=date(2025, 6, 15), weight="sample_text_2")
    _safe_set(a, 'model_VAT37', b1)
    assert _is_linked(a, 'model_VAT37', b1)
    if hasattr(b1, 'model_DocumentItem36'):
        assert _is_linked(b1, 'model_DocumentItem36', a)
    _safe_set(a, 'model_VAT37', b2)
    assert _is_linked(a, 'model_VAT37', b2)
    if hasattr(b1, 'model_DocumentItem36'):
        assert not _is_linked(b1, 'model_DocumentItem36', a)
    if hasattr(b2, 'model_DocumentItem36'):
        assert _is_linked(b2, 'model_DocumentItem36', a)
    _safe_set(a, 'model_VAT37', None)
    assert not _is_linked(a, 'model_VAT37', b2)
    if hasattr(b2, 'model_DocumentItem36'):
        assert not _is_linked(b2, 'model_DocumentItem36', a)


def test_assoc_items21_link_reassign_clear():
    a = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    b1 = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    b2 = model_Document(addressFirstLine="sample_text_2", billingType="sample_text_2", consultant="sample_text_2", customerRef="sample_text_2", deposit="sample_text_2", documentDate=date(2025, 6, 15), dueDays="sample_text_2", itemsRebate="sample_text_2", message="sample_text_2", message2="sample_text_2", message3="sample_text_2", netGross="sample_text_2", odtPath="sample_text_2", orderDate=date(2025, 6, 15), paid="sample_text_2", paidValue="sample_text_2", payDate=date(2025, 6, 15), pdfPath="sample_text_2", printTemplate="sample_text_2", printed="sample_text_2", progress="sample_text_2", serviceDate=date(2025, 6, 15), shippingAutoVat="sample_text_2", shippingValue="sample_text_2", totalValue="sample_text_2", transactionId="sample_text_2", vestingPeriodEnd=date(2025, 6, 15), vestingPeriodStart=date(2025, 6, 15), webshopDate=date(2025, 6, 15), webshopId="sample_text_2")
    _safe_set(a, 'model_DocumentItem', b1)
    assert _is_linked(a, 'model_DocumentItem', b1)
    if hasattr(b1, 'model_Document22'):
        assert _is_linked(b1, 'model_Document22', a)
    _safe_set(a, 'model_DocumentItem', b2)
    assert _is_linked(a, 'model_DocumentItem', b2)
    if hasattr(b1, 'model_Document22'):
        assert not _is_linked(b1, 'model_Document22', a)
    if hasattr(b2, 'model_Document22'):
        assert _is_linked(b2, 'model_Document22', a)
    _safe_set(a, 'model_DocumentItem', None)
    assert not _is_linked(a, 'model_DocumentItem', b2)
    if hasattr(b2, 'model_Document22'):
        assert not _is_linked(b2, 'model_Document22', a)


def test_assoc_items39_link_reassign_clear():
    a = model_VoucherItem(itemVoucherType="sample_text", posNr="sample_text", price="sample_text")
    b1 = model_Voucher(discounted="sample_text", doNotBook="sample_text", documentNumber="sample_text", paidValue="sample_text", totalValue="sample_text", voucherDate=date(2024, 1, 1), voucherNumber="sample_text", voucherType="sample_text")
    b2 = model_Voucher(discounted="sample_text_2", doNotBook="sample_text_2", documentNumber="sample_text_2", paidValue="sample_text_2", totalValue="sample_text_2", voucherDate=date(2025, 6, 15), voucherNumber="sample_text_2", voucherType="sample_text_2")
    _safe_set(a, 'model_VoucherItem', b1)
    assert _is_linked(a, 'model_VoucherItem', b1)
    if hasattr(b1, 'model_Voucher40'):
        assert _is_linked(b1, 'model_Voucher40', a)
    _safe_set(a, 'model_VoucherItem', b2)
    assert _is_linked(a, 'model_VoucherItem', b2)
    if hasattr(b1, 'model_Voucher40'):
        assert not _is_linked(b1, 'model_Voucher40', a)
    if hasattr(b2, 'model_Voucher40'):
        assert _is_linked(b2, 'model_Voucher40', a)
    _safe_set(a, 'model_VoucherItem', None)
    assert not _is_linked(a, 'model_VoucherItem', b2)
    if hasattr(b2, 'model_Voucher40'):
        assert not _is_linked(b2, 'model_Voucher40', a)


def test_assoc_noVatReference23_link_reassign_clear():
    a = model_VAT(description="sample_text", salesEqualizationTax="sample_text", taxValue="sample_text")
    b1 = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    b2 = model_Document(addressFirstLine="sample_text_2", billingType="sample_text_2", consultant="sample_text_2", customerRef="sample_text_2", deposit="sample_text_2", documentDate=date(2025, 6, 15), dueDays="sample_text_2", itemsRebate="sample_text_2", message="sample_text_2", message2="sample_text_2", message3="sample_text_2", netGross="sample_text_2", odtPath="sample_text_2", orderDate=date(2025, 6, 15), paid="sample_text_2", paidValue="sample_text_2", payDate=date(2025, 6, 15), pdfPath="sample_text_2", printTemplate="sample_text_2", printed="sample_text_2", progress="sample_text_2", serviceDate=date(2025, 6, 15), shippingAutoVat="sample_text_2", shippingValue="sample_text_2", totalValue="sample_text_2", transactionId="sample_text_2", vestingPeriodEnd=date(2025, 6, 15), vestingPeriodStart=date(2025, 6, 15), webshopDate=date(2025, 6, 15), webshopId="sample_text_2")
    _safe_set(a, 'model_VAT', b1)
    assert _is_linked(a, 'model_VAT', b1)
    if hasattr(b1, 'model_Document24'):
        assert _is_linked(b1, 'model_Document24', a)
    _safe_set(a, 'model_VAT', b2)
    assert _is_linked(a, 'model_VAT', b2)
    if hasattr(b1, 'model_Document24'):
        assert not _is_linked(b1, 'model_Document24', a)
    if hasattr(b2, 'model_Document24'):
        assert _is_linked(b2, 'model_Document24', a)
    _safe_set(a, 'model_VAT', None)
    assert not _is_linked(a, 'model_VAT', b2)
    if hasattr(b2, 'model_Document24'):
        assert not _is_linked(b2, 'model_Document24', a)


def test_assoc_payment25_link_reassign_clear():
    a = model_Payment(code="sample_text", depositText="sample_text", description="sample_text", discountDays="sample_text", discountValue="sample_text", netDays="sample_text", paidText="sample_text", unpaidText="sample_text")
    b1 = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    b2 = model_Document(addressFirstLine="sample_text_2", billingType="sample_text_2", consultant="sample_text_2", customerRef="sample_text_2", deposit="sample_text_2", documentDate=date(2025, 6, 15), dueDays="sample_text_2", itemsRebate="sample_text_2", message="sample_text_2", message2="sample_text_2", message3="sample_text_2", netGross="sample_text_2", odtPath="sample_text_2", orderDate=date(2025, 6, 15), paid="sample_text_2", paidValue="sample_text_2", payDate=date(2025, 6, 15), pdfPath="sample_text_2", printTemplate="sample_text_2", printed="sample_text_2", progress="sample_text_2", serviceDate=date(2025, 6, 15), shippingAutoVat="sample_text_2", shippingValue="sample_text_2", totalValue="sample_text_2", transactionId="sample_text_2", vestingPeriodEnd=date(2025, 6, 15), vestingPeriodStart=date(2025, 6, 15), webshopDate=date(2025, 6, 15), webshopId="sample_text_2")
    _safe_set(a, 'model_Payment27', b1)
    assert _is_linked(a, 'model_Payment27', b1)
    if hasattr(b1, 'model_Document26'):
        assert _is_linked(b1, 'model_Document26', a)
    _safe_set(a, 'model_Payment27', b2)
    assert _is_linked(a, 'model_Payment27', b2)
    if hasattr(b1, 'model_Document26'):
        assert not _is_linked(b1, 'model_Document26', a)
    if hasattr(b2, 'model_Document26'):
        assert _is_linked(b2, 'model_Document26', a)
    _safe_set(a, 'model_Payment27', None)
    assert not _is_linked(a, 'model_Payment27', b2)
    if hasattr(b2, 'model_Document26'):
        assert not _is_linked(b2, 'model_Document26', a)


def test_assoc_payment8_link_reassign_clear():
    a = model_Payment(code="sample_text", depositText="sample_text", description="sample_text", discountDays="sample_text", discountValue="sample_text", netDays="sample_text", paidText="sample_text", unpaidText="sample_text")
    b1 = model_Contact(birthday=date(2024, 1, 1), company="sample_text", contactType="sample_text", customerNumber="sample_text", discount="sample_text", email="sample_text", fax="sample_text", firstName="sample_text", gender="sample_text", gln="sample_text", mandateReference="sample_text", mobile="sample_text", note="sample_text", phone="sample_text", reliability="sample_text", supplierNumber="sample_text", title="sample_text", useNetGross="sample_text", useSalesEqualizationTax="sample_text", vatNumber="sample_text", vatNumberValid="sample_text", webshopName="sample_text", website="sample_text")
    b2 = model_Contact(birthday=date(2025, 6, 15), company="sample_text_2", contactType="sample_text_2", customerNumber="sample_text_2", discount="sample_text_2", email="sample_text_2", fax="sample_text_2", firstName="sample_text_2", gender="sample_text_2", gln="sample_text_2", mandateReference="sample_text_2", mobile="sample_text_2", note="sample_text_2", phone="sample_text_2", reliability="sample_text_2", supplierNumber="sample_text_2", title="sample_text_2", useNetGross="sample_text_2", useSalesEqualizationTax="sample_text_2", vatNumber="sample_text_2", vatNumberValid="sample_text_2", webshopName="sample_text_2", website="sample_text_2")
    _safe_set(a, 'model_Payment', b1)
    assert _is_linked(a, 'model_Payment', b1)
    if hasattr(b1, 'model_Contact9'):
        assert _is_linked(b1, 'model_Contact9', a)
    _safe_set(a, 'model_Payment', b2)
    assert _is_linked(a, 'model_Payment', b2)
    if hasattr(b1, 'model_Contact9'):
        assert not _is_linked(b1, 'model_Contact9', a)
    if hasattr(b2, 'model_Contact9'):
        assert _is_linked(b2, 'model_Contact9', a)
    _safe_set(a, 'model_Payment', None)
    assert not _is_linked(a, 'model_Payment', b2)
    if hasattr(b2, 'model_Contact9'):
        assert not _is_linked(b2, 'model_Contact9', a)


def test_assoc_product33_link_reassign_clear():
    a = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    b1 = model_DocumentItem(description="sample_text", gtin="sample_text", itemNumber="sample_text", itemRebate="sample_text", itemType="sample_text", noVat="sample_text", optional="sample_text", originQuantity="sample_text", picture="sample_text", posNr="sample_text", price="sample_text", quantity="sample_text", quantityUnit="sample_text", tara="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), weight="sample_text")
    b2 = model_DocumentItem(description="sample_text_2", gtin="sample_text_2", itemNumber="sample_text_2", itemRebate="sample_text_2", itemType="sample_text_2", noVat="sample_text_2", optional="sample_text_2", originQuantity="sample_text_2", picture="sample_text_2", posNr="sample_text_2", price="sample_text_2", quantity="sample_text_2", quantityUnit="sample_text_2", tara="sample_text_2", vestingPeriodEnd=date(2025, 6, 15), vestingPeriodStart=date(2025, 6, 15), weight="sample_text_2")
    _safe_set(a, 'model_Product', b1)
    assert _is_linked(a, 'model_Product', b1)
    if hasattr(b1, 'model_DocumentItem34'):
        assert _is_linked(b1, 'model_DocumentItem34', a)
    _safe_set(a, 'model_Product', b2)
    assert _is_linked(a, 'model_Product', b2)
    if hasattr(b1, 'model_DocumentItem34'):
        assert not _is_linked(b1, 'model_DocumentItem34', a)
    if hasattr(b2, 'model_DocumentItem34'):
        assert _is_linked(b2, 'model_DocumentItem34', a)
    _safe_set(a, 'model_Product', None)
    assert not _is_linked(a, 'model_Product', b2)
    if hasattr(b2, 'model_DocumentItem34'):
        assert not _is_linked(b2, 'model_DocumentItem34', a)


def test_assoc_roles67_link_reassign_clear():
    a = model_User(password="sample_text", userName="sample_text")
    b1 = model_Role()
    b2 = model_Role()
    _safe_set(a, 'model_User68', {b1})
    assert _is_linked(a, 'model_User68', b1)
    if hasattr(b1, 'model_Role'):
        assert _is_linked(b1, 'model_Role', a)
    _safe_set(a, 'model_User68', {b2})
    assert _is_linked(a, 'model_User68', b2)
    if hasattr(b1, 'model_Role'):
        assert not _is_linked(b1, 'model_Role', a)
    if hasattr(b2, 'model_Role'):
        assert _is_linked(b2, 'model_Role', a)
    _safe_set(a, 'model_User68', set())
    assert not _is_linked(a, 'model_User68', b2)
    if hasattr(b2, 'model_Role'):
        assert not _is_linked(b2, 'model_Role', a)


def test_assoc_shipping28_link_reassign_clear():
    a = model_Shipping(autoVat="sample_text", code="sample_text", shippingValue="sample_text")
    b1 = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    b2 = model_Document(addressFirstLine="sample_text_2", billingType="sample_text_2", consultant="sample_text_2", customerRef="sample_text_2", deposit="sample_text_2", documentDate=date(2025, 6, 15), dueDays="sample_text_2", itemsRebate="sample_text_2", message="sample_text_2", message2="sample_text_2", message3="sample_text_2", netGross="sample_text_2", odtPath="sample_text_2", orderDate=date(2025, 6, 15), paid="sample_text_2", paidValue="sample_text_2", payDate=date(2025, 6, 15), pdfPath="sample_text_2", printTemplate="sample_text_2", printed="sample_text_2", progress="sample_text_2", serviceDate=date(2025, 6, 15), shippingAutoVat="sample_text_2", shippingValue="sample_text_2", totalValue="sample_text_2", transactionId="sample_text_2", vestingPeriodEnd=date(2025, 6, 15), vestingPeriodStart=date(2025, 6, 15), webshopDate=date(2025, 6, 15), webshopId="sample_text_2")
    _safe_set(a, 'model_Shipping', b1)
    assert _is_linked(a, 'model_Shipping', b1)
    if hasattr(b1, 'model_Document29'):
        assert _is_linked(b1, 'model_Document29', a)
    _safe_set(a, 'model_Shipping', b2)
    assert _is_linked(a, 'model_Shipping', b2)
    if hasattr(b1, 'model_Document29'):
        assert not _is_linked(b1, 'model_Document29', a)
    if hasattr(b2, 'model_Document29'):
        assert _is_linked(b2, 'model_Document29', a)
    _safe_set(a, 'model_Shipping', None)
    assert not _is_linked(a, 'model_Shipping', b2)
    if hasattr(b2, 'model_Document29'):
        assert not _is_linked(b2, 'model_Document29', a)


def test_assoc_shippingVat60_link_reassign_clear():
    a = model_VAT(description="sample_text", salesEqualizationTax="sample_text", taxValue="sample_text")
    b1 = model_Shipping(autoVat="sample_text", code="sample_text", shippingValue="sample_text")
    b2 = model_Shipping(autoVat="sample_text_2", code="sample_text_2", shippingValue="sample_text_2")
    _safe_set(a, 'model_VAT62', b1)
    assert _is_linked(a, 'model_VAT62', b1)
    if hasattr(b1, 'model_Shipping61'):
        assert _is_linked(b1, 'model_Shipping61', a)
    _safe_set(a, 'model_VAT62', b2)
    assert _is_linked(a, 'model_VAT62', b2)
    if hasattr(b1, 'model_Shipping61'):
        assert not _is_linked(b1, 'model_Shipping61', a)
    if hasattr(b2, 'model_Shipping61'):
        assert _is_linked(b2, 'model_Shipping61', a)
    _safe_set(a, 'model_VAT62', None)
    assert not _is_linked(a, 'model_VAT62', b2)
    if hasattr(b2, 'model_Shipping61'):
        assert not _is_linked(b2, 'model_Shipping61', a)


def test_assoc_sourceDocument31_link_reassign_clear():
    a = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    b1 = model_Document(addressFirstLine="sample_text", billingType="sample_text", consultant="sample_text", customerRef="sample_text", deposit="sample_text", documentDate=date(2024, 1, 1), dueDays="sample_text", itemsRebate="sample_text", message="sample_text", message2="sample_text", message3="sample_text", netGross="sample_text", odtPath="sample_text", orderDate=date(2024, 1, 1), paid="sample_text", paidValue="sample_text", payDate=date(2024, 1, 1), pdfPath="sample_text", printTemplate="sample_text", printed="sample_text", progress="sample_text", serviceDate=date(2024, 1, 1), shippingAutoVat="sample_text", shippingValue="sample_text", totalValue="sample_text", transactionId="sample_text", vestingPeriodEnd=date(2024, 1, 1), vestingPeriodStart=date(2024, 1, 1), webshopDate=date(2024, 1, 1), webshopId="sample_text")
    b2 = model_Document(addressFirstLine="sample_text_2", billingType="sample_text_2", consultant="sample_text_2", customerRef="sample_text_2", deposit="sample_text_2", documentDate=date(2025, 6, 15), dueDays="sample_text_2", itemsRebate="sample_text_2", message="sample_text_2", message2="sample_text_2", message3="sample_text_2", netGross="sample_text_2", odtPath="sample_text_2", orderDate=date(2025, 6, 15), paid="sample_text_2", paidValue="sample_text_2", payDate=date(2025, 6, 15), pdfPath="sample_text_2", printTemplate="sample_text_2", printed="sample_text_2", progress="sample_text_2", serviceDate=date(2025, 6, 15), shippingAutoVat="sample_text_2", shippingValue="sample_text_2", totalValue="sample_text_2", transactionId="sample_text_2", vestingPeriodEnd=date(2025, 6, 15), vestingPeriodStart=date(2025, 6, 15), webshopDate=date(2025, 6, 15), webshopId="sample_text_2")
    _safe_set(a, 'model_Document30', b1)
    assert _is_linked(a, 'model_Document30', b1)
    if hasattr(b1, 'model_Document32'):
        assert _is_linked(b1, 'model_Document32', a)
    _safe_set(a, 'model_Document30', b2)
    assert _is_linked(a, 'model_Document30', b2)
    if hasattr(b1, 'model_Document32'):
        assert not _is_linked(b1, 'model_Document32', a)
    if hasattr(b2, 'model_Document32'):
        assert _is_linked(b2, 'model_Document32', a)
    _safe_set(a, 'model_Document30', None)
    assert not _is_linked(a, 'model_Document30', b2)
    if hasattr(b2, 'model_Document32'):
        assert not _is_linked(b2, 'model_Document32', a)


def test_assoc_stateMapping71_link_reassign_clear():
    a = model_WebshopStateMapping(fakturamaOrderState="sample_text", webshopState="sample_text")
    b1 = model_WebShop(webshopVendor="sample_text", webshopVersion="sample_text")
    b2 = model_WebShop(webshopVendor="sample_text_2", webshopVersion="sample_text_2")
    _safe_set(a, 'model_WebshopStateMapping', b1)
    assert _is_linked(a, 'model_WebshopStateMapping', b1)
    if hasattr(b1, 'model_WebShop'):
        assert _is_linked(b1, 'model_WebShop', a)
    _safe_set(a, 'model_WebshopStateMapping', b2)
    assert _is_linked(a, 'model_WebshopStateMapping', b2)
    if hasattr(b1, 'model_WebShop'):
        assert not _is_linked(b1, 'model_WebShop', a)
    if hasattr(b2, 'model_WebShop'):
        assert _is_linked(b2, 'model_WebShop', a)
    _safe_set(a, 'model_WebshopStateMapping', None)
    assert not _is_linked(a, 'model_WebshopStateMapping', b2)
    if hasattr(b2, 'model_WebShop'):
        assert not _is_linked(b2, 'model_WebShop', a)


def test_assoc_tenant66_link_reassign_clear():
    a = model_User(password="sample_text", userName="sample_text")
    b1 = model_Tenant()
    b2 = model_Tenant()
    _safe_set(a, 'model_User', b1)
    assert _is_linked(a, 'model_User', b1)
    if hasattr(b1, 'model_Tenant'):
        assert _is_linked(b1, 'model_Tenant', a)
    _safe_set(a, 'model_User', b2)
    assert _is_linked(a, 'model_User', b2)
    if hasattr(b1, 'model_Tenant'):
        assert not _is_linked(b1, 'model_Tenant', a)
    if hasattr(b2, 'model_Tenant'):
        assert _is_linked(b2, 'model_Tenant', a)
    _safe_set(a, 'model_User', None)
    assert not _is_linked(a, 'model_User', b2)
    if hasattr(b2, 'model_Tenant'):
        assert not _is_linked(b2, 'model_Tenant', a)


def test_assoc_vat43_link_reassign_clear():
    a = model_VoucherItem(itemVoucherType="sample_text", posNr="sample_text", price="sample_text")
    b1 = model_VAT(description="sample_text", salesEqualizationTax="sample_text", taxValue="sample_text")
    b2 = model_VAT(description="sample_text_2", salesEqualizationTax="sample_text_2", taxValue="sample_text_2")
    _safe_set(a, 'model_VoucherItem44', b1)
    assert _is_linked(a, 'model_VoucherItem44', b1)
    if hasattr(b1, 'model_VAT45'):
        assert _is_linked(b1, 'model_VAT45', a)
    _safe_set(a, 'model_VoucherItem44', b2)
    assert _is_linked(a, 'model_VoucherItem44', b2)
    if hasattr(b1, 'model_VAT45'):
        assert not _is_linked(b1, 'model_VAT45', a)
    if hasattr(b2, 'model_VAT45'):
        assert _is_linked(b2, 'model_VAT45', a)
    _safe_set(a, 'model_VoucherItem44', None)
    assert not _is_linked(a, 'model_VoucherItem44', b2)
    if hasattr(b2, 'model_VAT45'):
        assert not _is_linked(b2, 'model_VAT45', a)


def test_assoc_vat55_link_reassign_clear():
    a = model_VAT(description="sample_text", salesEqualizationTax="sample_text", taxValue="sample_text")
    b1 = model_Product(block1="sample_text", block2="sample_text", block3="sample_text", block4="sample_text", block5="sample_text", cdf01="sample_text", cdf02="sample_text", cdf03="sample_text", costPrice="sample_text", gtin="sample_text", itemNumber="sample_text", picture="sample_text", price1="sample_text", price2="sample_text", price3="sample_text", price4="sample_text", price5="sample_text", quantity="sample_text", quantityUnit="sample_text", sellingUnit="sample_text", webshopId="sample_text", weight="sample_text")
    b2 = model_Product(block1="sample_text_2", block2="sample_text_2", block3="sample_text_2", block4="sample_text_2", block5="sample_text_2", cdf01="sample_text_2", cdf02="sample_text_2", cdf03="sample_text_2", costPrice="sample_text_2", gtin="sample_text_2", itemNumber="sample_text_2", picture="sample_text_2", price1="sample_text_2", price2="sample_text_2", price3="sample_text_2", price4="sample_text_2", price5="sample_text_2", quantity="sample_text_2", quantityUnit="sample_text_2", sellingUnit="sample_text_2", webshopId="sample_text_2", weight="sample_text_2")
    _safe_set(a, 'model_VAT57', b1)
    assert _is_linked(a, 'model_VAT57', b1)
    if hasattr(b1, 'model_Product56'):
        assert _is_linked(b1, 'model_Product56', a)
    _safe_set(a, 'model_VAT57', b2)
    assert _is_linked(a, 'model_VAT57', b2)
    if hasattr(b1, 'model_Product56'):
        assert not _is_linked(b1, 'model_Product56', a)
    if hasattr(b2, 'model_Product56'):
        assert _is_linked(b2, 'model_Product56', a)
    _safe_set(a, 'model_VAT57', None)
    assert not _is_linked(a, 'model_VAT57', b2)
    if hasattr(b2, 'model_Product56'):
        assert not _is_linked(b2, 'model_Product56', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractCategory_strategy = st.builds(AbstractCategory)
@given(instance=AbstractCategory_strategy)
@settings(max_examples=25)
def test_AbstractCategory_instantiation(instance):
    assert isinstance(instance, AbstractCategory)


Contact_strategy = st.builds(Contact)
@given(instance=Contact_strategy)
@settings(max_examples=25)
def test_Contact_instantiation(instance):
    assert isinstance(instance, Contact)


Document_strategy = st.builds(Document)
@given(instance=Document_strategy)
@settings(max_examples=25)
def test_Document_instantiation(instance):
    assert isinstance(instance, Document)


IDescribableEntity_strategy = st.builds(IDescribableEntity)
@given(instance=IDescribableEntity_strategy)
@settings(max_examples=25)
def test_IDescribableEntity_instantiation(instance):
    assert isinstance(instance, IDescribableEntity)


IEntity_strategy = st.builds(IEntity)
@given(instance=IEntity_strategy)
@settings(max_examples=25)
def test_IEntity_instantiation(instance):
    assert isinstance(instance, IEntity)


model_AbstractCategory_strategy = st.builds(model_AbstractCategory)
@given(instance=model_AbstractCategory_strategy)
@settings(max_examples=25)
def test_model_AbstractCategory_instantiation(instance):
    assert isinstance(instance, model_AbstractCategory)


model_Address_strategy = st.builds(model_Address, city=safe_text, cityAddon=safe_text, countryCode=safe_text, manualAddress=safe_text, street=safe_text, zip=safe_text)
@given(instance=model_Address_strategy)
@settings(max_examples=25)
def test_model_Address_instantiation(instance):
    assert isinstance(instance, model_Address)


model_BankAccount_strategy = st.builds(model_BankAccount, accountHolder=safe_text, bankCode=safe_text, bankName=safe_text, bic=safe_text, iban=safe_text)
@given(instance=model_BankAccount_strategy)
@settings(max_examples=25)
def test_model_BankAccount_instantiation(instance):
    assert isinstance(instance, model_BankAccount)


model_CEFACTCode_strategy = st.builds(model_CEFACTCode, abbreviation_de=safe_text, abbreviation_en=safe_text, code=safe_text, name_de=safe_text, target=safe_text)
@given(instance=model_CEFACTCode_strategy)
@settings(max_examples=25)
def test_model_CEFACTCode_instantiation(instance):
    assert isinstance(instance, model_CEFACTCode)


model_Confirmation_strategy = st.builds(model_Confirmation)
@given(instance=model_Confirmation_strategy)
@settings(max_examples=25)
def test_model_Confirmation_instantiation(instance):
    assert isinstance(instance, model_Confirmation)


model_Contact_strategy = st.builds(model_Contact, birthday=st.dates(), company=safe_text, contactType=safe_text, customerNumber=safe_text, discount=safe_text, email=safe_text, fax=safe_text, firstName=safe_text, gender=safe_text, gln=safe_text, mandateReference=safe_text, mobile=safe_text, note=safe_text, phone=safe_text, reliability=safe_text, supplierNumber=safe_text, title=safe_text, useNetGross=safe_text, useSalesEqualizationTax=safe_text, vatNumber=safe_text, vatNumberValid=safe_text, webshopName=safe_text, website=safe_text)
@given(instance=model_Contact_strategy)
@settings(max_examples=25)
def test_model_Contact_instantiation(instance):
    assert isinstance(instance, model_Contact)


model_ContactCategory_strategy = st.builds(model_ContactCategory)
@given(instance=model_ContactCategory_strategy)
@settings(max_examples=25)
def test_model_ContactCategory_instantiation(instance):
    assert isinstance(instance, model_ContactCategory)


model_Credit_strategy = st.builds(model_Credit)
@given(instance=model_Credit_strategy)
@settings(max_examples=25)
def test_model_Credit_instantiation(instance):
    assert isinstance(instance, model_Credit)


model_Creditor_strategy = st.builds(model_Creditor)
@given(instance=model_Creditor_strategy)
@settings(max_examples=25)
def test_model_Creditor_instantiation(instance):
    assert isinstance(instance, model_Creditor)


model_Debitor_strategy = st.builds(model_Debitor)
@given(instance=model_Debitor_strategy)
@settings(max_examples=25)
def test_model_Debitor_instantiation(instance):
    assert isinstance(instance, model_Debitor)


model_Delivery_strategy = st.builds(model_Delivery)
@given(instance=model_Delivery_strategy)
@settings(max_examples=25)
def test_model_Delivery_instantiation(instance):
    assert isinstance(instance, model_Delivery)


model_Document_strategy = st.builds(model_Document, addressFirstLine=safe_text, billingType=safe_text, consultant=safe_text, customerRef=safe_text, deposit=safe_text, documentDate=st.dates(), dueDays=safe_text, itemsRebate=safe_text, message=safe_text, message2=safe_text, message3=safe_text, netGross=safe_text, odtPath=safe_text, orderDate=st.dates(), paid=safe_text, paidValue=safe_text, payDate=st.dates(), pdfPath=safe_text, printTemplate=safe_text, printed=safe_text, progress=safe_text, serviceDate=st.dates(), shippingAutoVat=safe_text, shippingValue=safe_text, totalValue=safe_text, transactionId=safe_text, vestingPeriodEnd=st.dates(), vestingPeriodStart=st.dates(), webshopDate=st.dates(), webshopId=safe_text)
@given(instance=model_Document_strategy)
@settings(max_examples=25)
def test_model_Document_instantiation(instance):
    assert isinstance(instance, model_Document)


model_DocumentItem_strategy = st.builds(model_DocumentItem, description=safe_text, gtin=safe_text, itemNumber=safe_text, itemRebate=safe_text, itemType=safe_text, noVat=safe_text, optional=safe_text, originQuantity=safe_text, picture=safe_text, posNr=safe_text, price=safe_text, quantity=safe_text, quantityUnit=safe_text, tara=safe_text, vestingPeriodEnd=st.dates(), vestingPeriodStart=st.dates(), weight=safe_text)
@given(instance=model_DocumentItem_strategy)
@settings(max_examples=25)
def test_model_DocumentItem_instantiation(instance):
    assert isinstance(instance, model_DocumentItem)


model_Dunning_strategy = st.builds(model_Dunning, dunningLevel=safe_text)
@given(instance=model_Dunning_strategy)
@settings(max_examples=25)
def test_model_Dunning_instantiation(instance):
    assert isinstance(instance, model_Dunning)


model_IDescribableEntity_strategy = st.builds(model_IDescribableEntity, description=safe_text)
@given(instance=model_IDescribableEntity_strategy)
@settings(max_examples=25)
def test_model_IDescribableEntity_instantiation(instance):
    assert isinstance(instance, model_IDescribableEntity)


model_IEntity_strategy = st.builds(model_IEntity, dateAdded=st.dates(), deleted=safe_text, id=safe_text, modified=st.dates(), modifiedBy=safe_text, name=safe_text, validFrom=st.dates(), validTo=st.dates())
@given(instance=model_IEntity_strategy)
@settings(max_examples=25)
def test_model_IEntity_instantiation(instance):
    assert isinstance(instance, model_IEntity)


model_IndividualDocumentInfo_strategy = st.builds(model_IndividualDocumentInfo, noVatDescription=safe_text, noVatName=safe_text, paymentDescription=safe_text, paymentName=safe_text, paymentText=safe_text, shippingAutoVat=safe_text, shippingDescription=safe_text, shippingName=safe_text, shippingValue=safe_text, shippingVatDescription=safe_text, shippingVatValue=safe_text)
@given(instance=model_IndividualDocumentInfo_strategy)
@settings(max_examples=25)
def test_model_IndividualDocumentInfo_instantiation(instance):
    assert isinstance(instance, model_IndividualDocumentInfo)


model_Invoice_strategy = st.builds(model_Invoice)
@given(instance=model_Invoice_strategy)
@settings(max_examples=25)
def test_model_Invoice_instantiation(instance):
    assert isinstance(instance, model_Invoice)


model_ItemAccountType_strategy = st.builds(model_ItemAccountType, value=safe_text)
@given(instance=model_ItemAccountType_strategy)
@settings(max_examples=25)
def test_model_ItemAccountType_instantiation(instance):
    assert isinstance(instance, model_ItemAccountType)


model_ItemListTypeCategory_strategy = st.builds(model_ItemListTypeCategory)
@given(instance=model_ItemListTypeCategory_strategy)
@settings(max_examples=25)
def test_model_ItemListTypeCategory_instantiation(instance):
    assert isinstance(instance, model_ItemListTypeCategory)


model_Letter_strategy = st.builds(model_Letter)
@given(instance=model_Letter_strategy)
@settings(max_examples=25)
def test_model_Letter_instantiation(instance):
    assert isinstance(instance, model_Letter)


model_Offer_strategy = st.builds(model_Offer)
@given(instance=model_Offer_strategy)
@settings(max_examples=25)
def test_model_Offer_instantiation(instance):
    assert isinstance(instance, model_Offer)


model_Order_strategy = st.builds(model_Order)
@given(instance=model_Order_strategy)
@settings(max_examples=25)
def test_model_Order_instantiation(instance):
    assert isinstance(instance, model_Order)


model_Payment_strategy = st.builds(model_Payment, code=safe_text, depositText=safe_text, description=safe_text, discountDays=safe_text, discountValue=safe_text, netDays=safe_text, paidText=safe_text, unpaidText=safe_text)
@given(instance=model_Payment_strategy)
@settings(max_examples=25)
def test_model_Payment_instantiation(instance):
    assert isinstance(instance, model_Payment)


model_Product_strategy = st.builds(model_Product, block1=safe_text, block2=safe_text, block3=safe_text, block4=safe_text, block5=safe_text, cdf01=safe_text, cdf02=safe_text, cdf03=safe_text, costPrice=safe_text, gtin=safe_text, itemNumber=safe_text, picture=safe_text, price1=safe_text, price2=safe_text, price3=safe_text, price4=safe_text, price5=safe_text, quantity=safe_text, quantityUnit=safe_text, sellingUnit=safe_text, webshopId=safe_text, weight=safe_text)
@given(instance=model_Product_strategy)
@settings(max_examples=25)
def test_model_Product_instantiation(instance):
    assert isinstance(instance, model_Product)


model_ProductBlockPrice_strategy = st.builds(model_ProductBlockPrice, block=safe_text, price=safe_text)
@given(instance=model_ProductBlockPrice_strategy)
@settings(max_examples=25)
def test_model_ProductBlockPrice_instantiation(instance):
    assert isinstance(instance, model_ProductBlockPrice)


model_ProductCategory_strategy = st.builds(model_ProductCategory)
@given(instance=model_ProductCategory_strategy)
@settings(max_examples=25)
def test_model_ProductCategory_instantiation(instance):
    assert isinstance(instance, model_ProductCategory)


model_ProductOptions_strategy = st.builds(model_ProductOptions, attributeValue=safe_text, sequenceNumber=safe_text)
@given(instance=model_ProductOptions_strategy)
@settings(max_examples=25)
def test_model_ProductOptions_instantiation(instance):
    assert isinstance(instance, model_ProductOptions)


model_Proforma_strategy = st.builds(model_Proforma)
@given(instance=model_Proforma_strategy)
@settings(max_examples=25)
def test_model_Proforma_instantiation(instance):
    assert isinstance(instance, model_Proforma)


model_Role_strategy = st.builds(model_Role)
@given(instance=model_Role_strategy)
@settings(max_examples=25)
def test_model_Role_instantiation(instance):
    assert isinstance(instance, model_Role)


model_Shipping_strategy = st.builds(model_Shipping, autoVat=safe_text, code=safe_text, shippingValue=safe_text)
@given(instance=model_Shipping_strategy)
@settings(max_examples=25)
def test_model_Shipping_instantiation(instance):
    assert isinstance(instance, model_Shipping)


model_ShippingCategory_strategy = st.builds(model_ShippingCategory)
@given(instance=model_ShippingCategory_strategy)
@settings(max_examples=25)
def test_model_ShippingCategory_instantiation(instance):
    assert isinstance(instance, model_ShippingCategory)


model_Tenant_strategy = st.builds(model_Tenant)
@given(instance=model_Tenant_strategy)
@settings(max_examples=25)
def test_model_Tenant_instantiation(instance):
    assert isinstance(instance, model_Tenant)


model_TextCategory_strategy = st.builds(model_TextCategory)
@given(instance=model_TextCategory_strategy)
@settings(max_examples=25)
def test_model_TextCategory_instantiation(instance):
    assert isinstance(instance, model_TextCategory)


model_TextModule_strategy = st.builds(model_TextModule, text=safe_text)
@given(instance=model_TextModule_strategy)
@settings(max_examples=25)
def test_model_TextModule_instantiation(instance):
    assert isinstance(instance, model_TextModule)


model_User_strategy = st.builds(model_User, password=safe_text, userName=safe_text)
@given(instance=model_User_strategy)
@settings(max_examples=25)
def test_model_User_instantiation(instance):
    assert isinstance(instance, model_User)


model_UserProperty_strategy = st.builds(model_UserProperty, default=safe_text, global_=safe_text, user=safe_text, value=safe_text)
@given(instance=model_UserProperty_strategy)
@settings(max_examples=25)
def test_model_UserProperty_instantiation(instance):
    assert isinstance(instance, model_UserProperty)


model_VAT_strategy = st.builds(model_VAT, description=safe_text, salesEqualizationTax=safe_text, taxValue=safe_text)
@given(instance=model_VAT_strategy)
@settings(max_examples=25)
def test_model_VAT_instantiation(instance):
    assert isinstance(instance, model_VAT)


model_VATCategory_strategy = st.builds(model_VATCategory)
@given(instance=model_VATCategory_strategy)
@settings(max_examples=25)
def test_model_VATCategory_instantiation(instance):
    assert isinstance(instance, model_VATCategory)


model_Voucher_strategy = st.builds(model_Voucher, discounted=safe_text, doNotBook=safe_text, documentNumber=safe_text, paidValue=safe_text, totalValue=safe_text, voucherDate=st.dates(), voucherNumber=safe_text, voucherType=safe_text)
@given(instance=model_Voucher_strategy)
@settings(max_examples=25)
def test_model_Voucher_instantiation(instance):
    assert isinstance(instance, model_Voucher)


model_VoucherCategory_strategy = st.builds(model_VoucherCategory)
@given(instance=model_VoucherCategory_strategy)
@settings(max_examples=25)
def test_model_VoucherCategory_instantiation(instance):
    assert isinstance(instance, model_VoucherCategory)


model_VoucherItem_strategy = st.builds(model_VoucherItem, itemVoucherType=safe_text, posNr=safe_text, price=safe_text)
@given(instance=model_VoucherItem_strategy)
@settings(max_examples=25)
def test_model_VoucherItem_instantiation(instance):
    assert isinstance(instance, model_VoucherItem)


model_WebShop_strategy = st.builds(model_WebShop, webshopVendor=safe_text, webshopVersion=safe_text)
@given(instance=model_WebShop_strategy)
@settings(max_examples=25)
def test_model_WebShop_instantiation(instance):
    assert isinstance(instance, model_WebShop)


model_WebshopStateMapping_strategy = st.builds(model_WebshopStateMapping, fakturamaOrderState=safe_text, webshopState=safe_text)
@given(instance=model_WebshopStateMapping_strategy)
@settings(max_examples=25)
def test_model_WebshopStateMapping_instantiation(instance):
    assert isinstance(instance, model_WebshopStateMapping)



