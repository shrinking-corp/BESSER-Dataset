from python_code import website_AssociationWithContainment

def test_website_AssociationWithContainment___init__():
    assert website_AssociationWithContainment.__init__(website_AssociationWithContainment(True), False) == None


from python_code import website_AssociationWithoutContainment

def test_website_AssociationWithoutContainment___init__():
    assert website_AssociationWithoutContainment.__init__(website_AssociationWithoutContainment('', False), '', False) == None


from python_code import website_ActionMenuEntry
from python_code import website_ContentUnit
from python_code import website_UnitContainer

def test_website_ContentUnit___init__():
    assert website_ContentUnit.__init__(website_ContentUnit(False, '', '', '', '', False, '', website_ContentUnit=website_ActionMenuEntry(), ContentUnit=website_UnitContainer(), units=website_UnitContainer()), False, '\x00', '', '', '', False, '', website_ContentUnit=website_ActionMenuEntry(), ContentUnit=website_UnitContainer(), units=website_UnitContainer()) == None


from python_code import website_CreateSitemapUnit

def test_website_CreateSitemapUnit___init__():
    assert website_CreateSitemapUnit.__init__(website_CreateSitemapUnit('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import website_CreateUnit

def test_website_CreateUnit___init__():
    assert website_CreateUnit.__init__(website_CreateUnit(''), '') == None


from python_code import website_CreateUpdateUnit

def test_website_CreateUpdateUnit___init__():
    assert website_CreateUpdateUnit.__init__(website_CreateUpdateUnit('', '', '\x00\x00'), '', '', '') == None


from python_code import website_DateAttribute

def test_website_DateAttribute___init__():
    assert website_DateAttribute.__init__(website_DateAttribute('', '\x00'), '\x00\x00', '') == None


from python_code import website_DateField

def test_website_DateField___init__():
    assert website_DateField.__init__(website_DateField('', '\x00'), '\x00\x00', '') == None


from python_code import website_DatePathElement

def test_website_DatePathElement___init__():
    assert website_DatePathElement.__init__(website_DatePathElement(''), '') == None


from python_code import website_DetailsUnit

def test_website_DetailsUnit___init__():
    assert website_DetailsUnit.__init__(website_DetailsUnit(False, False, '', ''), False, False, '', '') == None


from python_code import website_EncapsulatedFeature

def test_website_EncapsulatedFeature___init__():
    assert website_EncapsulatedFeature.__init__(website_EncapsulatedFeature('', '', '\x00\x00'), '', '', '') == None


from python_code import website_EntityAttribute

def test_website_EntityAttribute___init__():
    assert website_EntityAttribute.__init__(website_EntityAttribute(False, False, '', '', ''), True, False, '', '', '') == None


from python_code import website_ImageIndexUnit

def test_website_ImageIndexUnit___init__():
    assert website_ImageIndexUnit.__init__(website_ImageIndexUnit('', '\x00'), '\x00\x00', '') == None


from python_code import website_InlineAction
from python_code import website_InlineActionContainer
from python_code import website_Predicate

def test_website_InlineAction___init__():
    assert website_InlineAction.__init__(website_InlineAction(False, '', '', '', '', '', website_InlineAction=website_Predicate(), website_InlineAction278=website_Predicate(), InlineAction=website_InlineActionContainer(), actions=website_InlineActionContainer()), False, '', '', '', '\x00', '', website_InlineAction=website_Predicate(), website_InlineAction278=website_Predicate(), InlineAction=website_InlineActionContainer(), actions=website_InlineActionContainer()) == None


from python_code import website_NamedDisplayElement

def test_website_NamedDisplayElement___init__():
    assert website_NamedDisplayElement.__init__(website_NamedDisplayElement(''), '') == None


from python_code import website_NamedElement

def test_website_NamedElement___init__():
    assert website_NamedElement.__init__(website_NamedElement(''), '') == None


from python_code import website_ResourceAttribute

def test_website_ResourceAttribute___init__():
    assert website_ResourceAttribute.__init__(website_ResourceAttribute(0, '', '', True, website_ResourceAttribute=set()), 0, '', '', False, website_ResourceAttribute=set()) == None


from python_code import website_SliderUnit

def test_website_SliderUnit___init__():
    assert website_SliderUnit.__init__(website_SliderUnit('', '\x00'), '\x00\x00', '') == None


from python_code import website_StaticPathElement

def test_website_StaticPathElement___init__():
    assert website_StaticPathElement.__init__(website_StaticPathElement(''), '') == None


from python_code import website_StaticUnit

def test_website_StaticUnit___init__():
    assert website_StaticUnit.__init__(website_StaticUnit('', '', '\x00\x00'), '', '', '') == None


from python_code import website_ThumbnailFilter

def test_website_ThumbnailFilter___init__():
    assert website_ThumbnailFilter.__init__(website_ThumbnailFilter(0, 0), 0, 0) == None


from python_code import website_Expression
from python_code import website_UnitFeature

def test_website_UnitFeature___init__():
    assert website_UnitFeature.__init__(website_UnitFeature(False, '', False, '', '', False, '', '', '', '', website_UnitFeature=website_Expression()), False, '', False, '', '\x00', False, '', '', '', '', website_UnitFeature=website_Expression()) == None


from python_code import website_UpdateUnit

def test_website_UpdateUnit___init__():
    assert website_UpdateUnit.__init__(website_UpdateUnit(''), '') == None


from python_code import website_UrlAttribute

def test_website_UrlAttribute___init__():
    assert website_UrlAttribute.__init__(website_UrlAttribute(''), '') == None

