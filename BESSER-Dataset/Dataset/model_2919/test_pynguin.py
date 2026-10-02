#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import pytest
import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    ABC,
    Association,
    Attribute,
    Cardinality,
    Classifier,
    DatabaseTechnologies,
    DateDetails,
    Enum,
    Feature,
    Label,
    ModelLabelFeature,
    NamedDisplayElement,
    NamedElement,
    OrmTechnologies,
    PathElement,
    ResourceAttribute,
    abstractmethod,
    date,
    datetime,
    isHasChoices,
    persistence_Association,
    persistence_AssociationKey,
    persistence_AssociationWithContainment,
    persistence_AssociationWithoutContainment,
    persistence_Attribute,
    persistence_DataType,
    persistence_DataTypeAttribute,
    persistence_DateAttribute,
    persistence_DatePathElement,
    persistence_Entity,
    persistence_Expression,
    persistence_Feature,
    persistence_FileAttribute,
    persistence_ImageAttribute,
    persistence_Label,
    persistence_LocationAttribute,
    persistence_ModelLabel,
    persistence_ModelLabelAssociation,
    persistence_ModelLabelAttribute,
    persistence_ModelLabelFeature,
    persistence_PathElement,
    persistence_Persistence,
    persistence_ResourceAttribute,
    persistence_SerializationGroup,
    persistence_StaticPathElement,
    persistence_UrlAttribute,
    time,
)


def test_0():
    var_0 = "e\x0bj90"
    var_1 = python_code_.persistence_UrlAttribute(displayValue=var_0)
    assert isinstance(var_1, python_code_.persistence_UrlAttribute)
    var_2 = python_code_.persistence_Label()
    var_3 = False
    var_4 = (
        lambda *args, **kwargs: "persistence_ModelLabelFeatureIdiormpersistence_Feature50"
    )
    var_5 = python_code_.persistence_DataTypeAttribute(
        obfuscateFormFields=var_3, caseInsensitive=var_2, encrypt=var_4
    )
    assert isinstance(var_5, python_code_.persistence_DataTypeAttribute)
    var_7 = python_code_.persistence_ResourceAttribute(
        validUploadExtensions=393.78,
        uploadsWithinWebsite=var_3,
        maximumUploadSize=var_4,
        validUploadMimeTypes=(),
    )
    assert isinstance(var_7, python_code_.persistence_ResourceAttribute)
    var_8 = python_code_.Association()
    var_9 = "/a"
    var_10 = python_code_.persistence_StaticPathElement(element=var_9)
    assert isinstance(var_10, python_code_.persistence_StaticPathElement)
    var_11 = True
    var_12 = python_code_.persistence_AssociationWithoutContainment(
        targetCardinality=var_4, targetUnique=var_11
    )
    assert isinstance(var_12, python_code_.persistence_AssociationWithoutContainment)
    var_14 = python_code_.Cardinality.Required
    var_16 = "_persistence_Persistence__persistence_Persistence2:_persistence_ModelLabelAssociation__persistence_ModelLabelAssociation"
    var_17 = python_code_.persistence_ModelLabelAttribute(dateFormat=var_16)
    assert isinstance(var_17, python_code_.persistence_ModelLabelAttribute)
    var_18 = "dYV??Q!1J&+53KIGi)"
    var_19 = python_code_.persistence_AssociationWithoutContainment
    var_20 = "!,'I.a=CO'"
    var_21 = "_persistence_Association__Association,_persistence_Feature__persistence_Feature39,_persistence_Attribute__persistence_Attribute11"
    var_22 = python_code_.persistence_Association(
        bidirectional=var_11,
        unique=var_8,
        pivotTableName=var_11,
        targetFeatureName=var_18,
        targetPrimaryKey=var_19,
        targetColumnName=var_18,
        targetDisplayLabel=var_18,
        targetHeaderClass=var_9,
        targetInputClass=2140,
        targetDisplayClass=var_2,
        targetFooterClass=var_20,
        pseudo=var_4,
        inputColumnClass=var_21,
        inputElementClass=var_14,
        serializationMaxDepth=set(),
    )
    assert isinstance(var_22, python_code_.persistence_Association)


def test_1():
    var_1 = bytes
    var_2 = python_code_.persistence_ModelLabel(
        format='{~L"A|!66,;Zpi|?Wc"', customise=False, ModelLabel47=var_1
    )
    assert isinstance(var_2, python_code_.persistence_ModelLabel)
    var_9 = "]bdQM'\x0b$H}"
    var_10 = True
    var_11 = set()
    var_12 = python_code_.persistence_ResourceAttribute(
        validUploadExtensions=var_9,
        uploadsWithinWebsite=var_10,
        maximumUploadSize="]",
        validUploadMimeTypes={},
        persistence_ResourceAttribute=var_11,
    )
    assert isinstance(var_12, python_code_.persistence_ResourceAttribute)
    var_4 = "persistence_DataType_persistence_Attribute__persistence_Attribute_persistence_Association__persistence_Association_persistence_Entity__persistence_Entity52"
    var_8 = python_code_.persistence_DateAttribute(details=var_4, format=var_4)
    assert isinstance(var_8, python_code_.persistence_DateAttribute)


def test_2():
    var_7 = python_code_.persistence_ModelLabel(
        format="_persistence_Feature__persistence_Feature50",
        customise=False,
        persistence_ModelLabel27=None,
        ModelLabel47=None,
    )
    assert isinstance(var_7, python_code_.persistence_ModelLabel)
    var_10 = True
    var_11 = python_code_.persistence_DataTypeAttribute(
        obfuscateFormFields=-1062.7, caseInsensitive=var_10, encrypt=()
    )
    assert isinstance(var_11, python_code_.persistence_DataTypeAttribute)


def test_3():
    var_0 = False
    var_1 = python_code_.persistence_ModelLabelAssociation(isSourceAssociation=var_0)
    assert isinstance(var_1, python_code_.persistence_ModelLabelAssociation)


def test_4():
    var_1 = bytes
    var_2 = python_code_.persistence_ModelLabel(
        format='{~L"A|!66,;Zpi|?Wc"', customise=False, ModelLabel47=var_1
    )
    assert isinstance(var_2, python_code_.persistence_ModelLabel)
    var_13 = "persistence_ModelLabel._persistence_Associatizn__persistence_Association._persistence_Feature__persistence_Feature63"
    var_16 = python_code_.persistence_ModelLabelAssociation(
        isSourceAssociation=var_13, persistence_ModelLabelAssociation26=True
    )
    assert isinstance(var_16, python_code_.persistence_ModelLabelAssociation)


def test_5():
    var_27 = "i{g#&9uI_HT|^~8#M+"
    var_28 = python_code_.persistence_ModelLabelAttribute(dateFormat=var_27)
    assert isinstance(var_28, python_code_.persistence_ModelLabelAttribute)


def test_6():
    var_0 = True
    var_3 = ":6yW/)|iv\\SE]5JK8D"
    var_4 = python_code_.persistence_Expression()
    var_5 = python_code_.persistence_Attribute(
        inputElementClass="H#YnXvqM",
        hidden=var_0,
        containerUnique=var_0,
        persistentType=var_3,
        ormType=var_3,
        interfaceType=var_0,
        unique=var_0,
        placeholder=var_3,
        validationPattern=459.83,
        inputColumnClass=var_0,
        persistence_Attribute11=var_4,
    )
    assert isinstance(var_5, python_code_.persistence_Attribute)


def test_7():
    var_0 = False
    var_3 = ":6yW/)|iv\\SE]5JK8D"
    var_5 = python_code_.persistence_Attribute(
        inputElementClass=var_3,
        hidden=var_0,
        containerUnique=var_0,
        persistentType=var_3,
        ormType="ChI9a&#<75!Q",
        interfaceType=var_3,
        unique=var_0,
        placeholder="r@(pjM?[\twJ",
        validationPattern=var_3,
        inputColumnClass=var_3,
        persistence_Attribute8=set(),
        persistence_Attribute11=None,
    )
    assert isinstance(var_5, python_code_.persistence_Attribute)


def test_8():
    var_10 = python_code_.DatabaseTechnologies
    var_11 = python_code_.DatabaseTechnologies.Oracle
    var_12 = python_code_.PathElement()
    var_13 = "<vu_G"
    var_15 = "persistence_Attribute23"
    var_16 = "kD!:Pm0nF>C{T\x0bM;8j=v"
    var_17 = '!<lv\r"I'
    var_18 = python_code_.persistence_Association(
        bidirectional=var_10,
        unique=var_10,
        pivotTableName=var_13,
        targetFeatureName=var_12,
        targetPrimaryKey=["\\?=H$!%", 3425.94, False],
        targetColumnName="ANS4:x1UJL-\n#8QH7V!",
        targetDisplayLabel=var_15,
        targetHeaderClass=var_13,
        targetInputClass=var_10,
        targetDisplayClass=var_13,
        targetFooterClass=var_10,
        pseudo=var_13,
        inputColumnClass=var_16,
        inputElementClass=var_17,
        serializationMaxDepth=var_11,
        persistence_Association=var_15,
        persistence_Association35=[False, 1530.06, "h j?KYOA\r[30q"],
    )
    assert isinstance(var_18, python_code_.persistence_Association)


def test_9():
    var_1 = set
    var_2 = python_code_.persistence_ModelLabel(
        format="N\t'CHo", customise=True, partOf={var_1}
    )
    assert isinstance(var_2, python_code_.persistence_ModelLabel)


def test_10():
    var_7 = python_code_.persistence_ModelLabel(
        format="_persistence_Feature__persistence_Feature50",
        customise=False,
        persistence_ModelLabel27=None,
        ModelLabel47=None,
    )
    assert isinstance(var_7, python_code_.persistence_ModelLabel)


def test_11():
    var_2 = python_code_.persistence_ModelLabel(
        format="h\\R\ny:o.Lu{!", customise=True, persistence_ModelLabel=set()
    )
    assert isinstance(var_2, python_code_.persistence_ModelLabel)


@pytest.mark.xfail(strict=True)
def test_12():
    var_0 = python_code_.persistence_ModelLabel
    var_1 = python_code_.persistence_UrlAttribute(displayValue=var_0)
    assert isinstance(var_1, python_code_.persistence_UrlAttribute)
    var_3 = True
    var_4 = python_code_.persistence_ModelLabelAssociation(isSourceAssociation=var_3)
    assert isinstance(var_4, python_code_.persistence_ModelLabelAssociation)
    var_5 = "2NJ!v]:\r\n"
    var_6 = '>_i\x0b";?#};'
    var_7 = False
    var_8 = python_code_.persistence_DataType()
    var_9 = {var_8, var_8, var_8, var_8, var_8}
    var_10 = python_code_.persistence_Persistence(
        ormTechnology=var_5,
        databaseTechnology=var_6,
        timestampCreation=var_7,
        timestampUpdates=var_1,
        persistence_Persistence2=var_9,
    )
    var_12 = python_code_.Association()
    var_13 = "t6[<-Xn<Jj$1m&)27hR"
    var_14 = True
    var_15 = python_code_.persistence_Entity(
        pluralisedName=var_5,
        singletonName=var_13,
        tableName={"": "Rj.-fe3$:"},
        autoKeyName=var_5,
        autoKeyPersistentType=set(),
        autoKeyGenerationStrategy=var_12,
        implementsUserInterface=var_0,
        allowFormTypeCustomisation=var_14,
        persistence_Entity31=var_9,
        Entity14=var_10,
        persistence_Entity38=var_9,
    )
    assert isinstance(var_15, python_code_.persistence_Entity)
    python_code_.persistence_ModelLabel(
        format=var_13,
        customise=b"\xf7i\x04\x87\x81{\x97\xed\x82\x98\xf2",
        labels=var_15,
        ModelLabel47=var_15,
    )


@pytest.mark.xfail(strict=True)
def test_13():
    var_0 = "persistence_Entity38,_persistence_ModelLabelAttribute__persistence_ModelLabelAttribute,DataMapper"
    var_1 = False
    var_2 = python_code_.DatabaseTechnologies
    python_code_.persistence_Persistence(
        ormTechnology=[],
        databaseTechnology=var_0,
        timestampCreation=var_1,
        timestampUpdates=var_2,
        persistence_Persistence=var_2,
    )
    var_12 = set()
    var_14 = "_persistence_Feature__Feature"
    python_code_.persistence_Entity(
        pluralisedName="THj6$k9<Ngqx\\\r7LA",
        singletonName=var_1,
        tableName=var_2,
        autoKeyName=var_0,
        autoKeyPersistentType=var_14,
        autoKeyGenerationStrategy=var_2,
        implementsUserInterface=var_1,
        allowFormTypeCustomisation=var_2,
        partOf29=False,
        persistence_Entity44=var_12,
        Entity=var_14,
    )


def test_14():
    var_7 = "m/y'@Vm6\n{"
    var_8 = "_persistence_Feature__persistence_Feature60 ModelLabelFeature _persistence_Feature__persistence_Feature50 _persistence_Feature__persistence_Feature63"
    var_9 = "persistence_ModelLabel._persistence_Associatizn__persistence_Association._persistence_eature__persistence_Feature63"
    var_13 = python_code_.persistence_ModelLabelAssociation(isSourceAssociation=True)
    assert isinstance(var_13, python_code_.persistence_ModelLabelAssociation)
    var_28 = python_code_.persistence_AssociationWithContainment(sourceVisible=var_9)
    assert isinstance(var_28, python_code_.persistence_AssociationWithContainment)
    var_31 = python_code_.persistence_DateAttribute(details=var_7, format="0oKAZ+w~")
    assert isinstance(var_31, python_code_.persistence_DateAttribute)
    var_32 = "persistence_Entity38,_persistence_Entity__Entity,_persistence_ResourceAttribute__persistence_ResourceAttribute"
    var_33 = python_code_.DatabaseTechnologies
    var_34 = set()
    var_35 = python_code_.persistence_Entity(
        pluralisedName=var_9,
        singletonName=var_32,
        tableName=var_7,
        autoKeyName=var_32,
        autoKeyPersistentType=var_8,
        autoKeyGenerationStrategy=False,
        implementsUserInterface=var_28,
        allowFormTypeCustomisation=var_33,
        persistence_Entity31=None,
        persistence_Entity34=var_34,
        labelFor=var_7,
    )
    assert isinstance(var_35, python_code_.persistence_Entity)


@pytest.mark.xfail(strict=True)
def test_15():
    var_1 = python_code_.persistence_SerializationGroup()
    var_2 = "Q\t9kf]@q;4=rJ"
    var_3 = python_code_.persistence_UrlAttribute(displayValue=var_2)
    assert isinstance(var_3, python_code_.persistence_UrlAttribute)
    var_6 = False
    var_7 = False
    var_8 = python_code_.persistence_DataTypeAttribute(
        obfuscateFormFields=var_6, caseInsensitive=var_1, encrypt=var_7
    )
    assert isinstance(var_8, python_code_.persistence_DataTypeAttribute)
    var_9 = python_code_.persistence_ImageAttribute()
    var_12 = python_code_.Attribute()
    var_13 = "Nw(rehh"
    var_16 = python_code_.persistence_AssociationWithoutContainment(
        targetCardinality=var_13, targetUnique=True
    )
    assert isinstance(var_16, python_code_.persistence_AssociationWithoutContainment)
    var_17 = "Z'Hd\twp17NkKv)I"
    var_18 = python_code_.persistence_AssociationWithoutContainment(
        targetCardinality=var_17, targetUnique=var_12
    )
    var_32 = ",bC{9,3[77p+dL!&"
    var_40 = python_code_.Classifier
    var_44 = "KO8*Z@@yogT"
    var_45 = True
    python_code_.persistence_Entity(
        pluralisedName=var_40,
        singletonName=var_17,
        tableName=var_44,
        autoKeyName=var_13,
        autoKeyPersistentType=var_12,
        autoKeyGenerationStrategy=var_32,
        implementsUserInterface=var_45,
        allowFormTypeCustomisation=var_9,
        persistence_Entity31=var_44,
        persistence_Entity49=complex(2357.0, 208.858388),
        persistence_Entity=None,
        Entity=var_18,
    )


def test_16():
    var_0 = "persistence_Entity38,_persistence_ModelLabelAttribute__persistence_ModelLabelAttribute,DataMapper"
    var_1 = False
    var_2 = python_code_.DatabaseTechnologies
    python_code_.persistence_Persistence(
        ormTechnology=[],
        databaseTechnology=var_0,
        timestampCreation=var_1,
        timestampUpdates=var_2,
        persistence_Persistence=var_2,
    )
    var_21 = python_code_.persistence_ModelLabelAssociation(isSourceAssociation=var_1)
    assert isinstance(var_21, python_code_.persistence_ModelLabelAssociation)


def test_17():
    var_0 = False
    var_2 = python_code_.persistence_ModelLabel(
        format="_persistence_ModelLabel__partOf",
        customise=False,
        ModelLabel=None,
        persistence_ModelLabel27=var_0,
    )
    assert isinstance(var_2, python_code_.persistence_ModelLabel)
    var_4 = "DoctrineODM-persistence_Persistence-persistence_Feature39"
    var_5 = False
    python_code_.persistence_Persistence(
        ormTechnology=var_0,
        databaseTechnology=var_4,
        timestampCreation=var_5,
        timestampUpdates=[],
    )


def test_18():
    var_0 = "persistence_Entity38,_persistence_ModelLabelAttribute__persistence_ModelLabelAttribute,DataMapper"
    var_2 = python_code_.DatabaseTechnologies
    python_code_.persistence_Persistence(
        ormTechnology="2h&~F[f(_}?]GU_0",
        databaseTechnology="s?`'A:SV']FQV>TAk",
        timestampCreation=True,
        timestampUpdates=True,
        persistence_Persistence2=set(),
    )
    var_4 = python_code_.DatabaseTechnologies.Oracle
    var_5 = python_code_.PathElement()
    var_6 = "<vu_G"
    var_7 = True
    var_8 = "persistence_Attribute23"
    var_9 = "kD!:Pm0nF>C{T\x0bM;8j=v"
    var_10 = '!<lv\r"I'
    var_11 = python_code_.persistence_Association(
        bidirectional=var_2,
        unique=var_2,
        pivotTableName=var_0,
        targetFeatureName=var_5,
        targetPrimaryKey=["\\?=H$!%", 3425.94, False],
        targetColumnName="ANS4:x1UJL-\n#8QH7V!",
        targetDisplayLabel=var_8,
        targetHeaderClass=var_0,
        targetInputClass=var_2,
        targetDisplayClass=var_0,
        targetFooterClass=var_2,
        pseudo=var_6,
        inputColumnClass=var_9,
        inputElementClass=var_10,
        serializationMaxDepth=var_4,
        persistence_Association=var_8,
        persistence_Association35=[False, 1530.06, "h j?KYOA\r[30q"],
    )
    assert isinstance(var_11, python_code_.persistence_Association)
    var_20 = python_code_.persistence_AssociationWithoutContainment(
        targetCardinality=var_9, targetUnique=var_7
    )
    assert isinstance(var_20, python_code_.persistence_AssociationWithoutContainment)
    var_21 = python_code_.persistence_DateAttribute(details=var_8, format=var_2)
    assert isinstance(var_21, python_code_.persistence_DateAttribute)


def test_19():
    var_0 = python_code_.persistence_AssociationWithContainment(sourceVisible=2814)
    assert isinstance(var_0, python_code_.persistence_AssociationWithContainment)
    var_1 = "TimeOnly.persistence_Expression"
    var_2 = lambda *args, **kwargs: True
    var_5 = True
    var_6 = "IjjvrAxX8Cd"
    var_7 = "-\tfs;i1f{6^n#"
    var_8 = python_code_.persistence_Feature(
        cardinality=var_1,
        ordered=var_5,
        primaryKey=var_2,
        derived=(
            "Kohana",
            "Manypersistence_Entity34persistence_Attribute8persistence_Attribute",
            2055.24,
        ),
        customiseSet=var_1,
        booleanIsHasChoice=var_6,
        title=var_7,
        collectionOrmAllowAdd=var_5,
        collectionOrmAllowRemove=var_2,
        defaultDisplayValue=var_7,
        emptyDisplayValue=var_1,
        encodeUriKey=b".n\xcdL\xc3\xe9",
        singletonName=var_1,
        pluralisedName=var_6,
        columnName=var_2,
        headerClass=var_0,
        displayClass=var_1,
        footerClass=var_2,
        Feature=var_5,
        persistence_Feature53=var_0,
    )
    assert isinstance(var_8, python_code_.persistence_Feature)


def test_20():
    var_0 = False
    var_3 = python_code_.PathElement()
    var_4 = "<vu_(G"
    var_8 = '!<lv\r"I'
    var_10 = False
    var_11 = "_persistnce_Feature__Feature"
    var_12 = "persistence_SerializationGroup19-_persistence_Feature__persistence_Feature-_persistence_Entity__Entity"
    var_13 = python_code_.persistence_Feature(
        cardinality=b"\x90\xbd\xe6\x82\xa4|k\x98\x99\x11\x863\x94\xa1A\xf1F?\xa5",
        ordered=var_0,
        primaryKey=var_10,
        derived=var_0,
        customiseSet=var_10,
        booleanIsHasChoice=var_11,
        title=var_10,
        collectionOrmAllowAdd=complex(-1086.0, 2797.770498),
        collectionOrmAllowRemove=var_10,
        defaultDisplayValue=var_11,
        emptyDisplayValue=var_4,
        encodeUriKey=231.6,
        singletonName=0,
        pluralisedName=var_3,
        columnName="c'6\t?Dnq{]C<",
        headerClass=var_8,
        displayClass=var_12,
        footerClass=var_11,
        features=var_8,
    )
    assert isinstance(var_13, python_code_.persistence_Feature)


def test_21():
    python_code_.persistence_LocationAttribute


def test_22():
    var_0 = python_code_.persistence_AssociationWithContainment(sourceVisible=2814)
    assert isinstance(var_0, python_code_.persistence_AssociationWithContainment)


def test_23():
    var_9 = "persistence_DataType_persistence_Attribute__persistence_Attribute_persistence_Association__persistence_Association_persistence_Entity__persistence_Entity52"
    var_10 = False
    var_11 = python_code_.persistence_AssociationWithoutContainment(
        targetCardinality=var_9, targetUnique=var_10
    )
    assert isinstance(var_11, python_code_.persistence_AssociationWithoutContainment)


def test_24():
    var_0 = python_code_.persistence_ModelLabelAssociation
    var_1 = python_code_.persistence_DatePathElement(format=var_0)
    assert isinstance(var_1, python_code_.persistence_DatePathElement)
    var_4 = True
    var_5 = python_code_.persistence_AssociationWithContainment(sourceVisible=var_4)
    assert isinstance(var_5, python_code_.persistence_AssociationWithContainment)


def test_25():
    var_8 = "_persistence_Feature__persistence_Feature60 ModelLabelFeature _persistence_Feature__persistence_Feature50 _persistence_Feature__persistence_Feature63"
    var_13 = python_code_.persistence_ModelLabelAssociation(
        isSourceAssociation=var_8, persistence_ModelLabelAssociation26=True
    )
    assert isinstance(var_13, python_code_.persistence_ModelLabelAssociation)
    var_21 = "M$,Y"
    var_22 = python_code_.persistence_StaticPathElement(element=var_21)
    assert isinstance(var_22, python_code_.persistence_StaticPathElement)
    var_23 = bytes
    var_24 = python_code_.persistence_ModelLabelAttribute(dateFormat=var_23)
    assert isinstance(var_24, python_code_.persistence_ModelLabelAttribute)


def test_26():
    var_0 = python_code_.persistence_ModelLabel
    var_1 = python_code_.persistence_UrlAttribute(displayValue=var_0)
    assert isinstance(var_1, python_code_.persistence_UrlAttribute)
    var_3 = True
    var_4 = python_code_.persistence_ModelLabelAssociation(isSourceAssociation=var_3)
    assert isinstance(var_4, python_code_.persistence_ModelLabelAssociation)
    var_18 = "i{g#&9uI_HT|^~8#NM+"
    var_19 = python_code_.persistence_ModelLabelAttribute(dateFormat=var_18)
    assert isinstance(var_19, python_code_.persistence_ModelLabelAttribute)


def test_27():
    var_27 = False
    var_28 = python_code_.persistence_AssociationWithContainment(sourceVisible=var_27)
    assert isinstance(var_28, python_code_.persistence_AssociationWithContainment)
    var_11 = python_code_.Classifier
    var_21 = True
    var_24 = "_persistence_Feature__features:Entity16:isA:_persistence_Association__persistence_Association"
    var_25 = python_code_.persistence_ModelLabel(
        format=var_24, customise=var_21, labels=var_11, ModelLabel47=var_11
    )
    assert isinstance(var_25, python_code_.persistence_ModelLabel)


def test_28():
    var_1 = python_code_.Label()
    var_3 = python_code_.Cardinality.Many
    var_9 = "L\x0c"
    var_10 = False
    var_11 = python_code_.persistence_AssociationWithoutContainment(
        targetCardinality=var_9, targetUnique=var_10
    )
    assert isinstance(var_11, python_code_.persistence_AssociationWithoutContainment)
    var_12 = "]~Uka\nW4hxo\\g"
    var_13 = "persistence_ModelLabel27"
    var_14 = ">vbp*6*k.`*"
    var_15 = lambda *args, **kwargs: 642
    var_16 = True
    var_17 = "0/(RqHNfMzYm^SIMvk"
    var_18 = "f$^5D]"
    var_19 = python_code_.persistence_Feature(
        cardinality=var_12,
        ordered="_persistence_ModelLabel__partOf,_persistence_Feature__persistence_Feature60,Entity,persistence_ModelLabel",
        primaryKey=var_10,
        derived=var_10,
        customiseSet={},
        booleanIsHasChoice=var_13,
        title=var_14,
        collectionOrmAllowAdd=var_15,
        collectionOrmAllowRemove=var_16,
        defaultDisplayValue=var_17,
        emptyDisplayValue=var_17,
        encodeUriKey=set(),
        singletonName=var_17,
        pluralisedName=[],
        columnName=var_18,
        headerClass=var_14,
        displayClass=3,
        footerClass=var_1,
        Feature=var_14,
        persistence_Feature50=var_3,
    )
    assert isinstance(var_19, python_code_.persistence_Feature)
    var_22 = python_code_.persistence_AssociationWithContainment(sourceVisible=var_12)
    assert isinstance(var_22, python_code_.persistence_AssociationWithContainment)


def test_29():
    var_0 = False
    var_3 = False
    var_4 = ":6yW/)|iv\\SE]5JK8D"
    var_5 = python_code_.persistence_Expression()
    var_6 = python_code_.persistence_Attribute(
        inputElementClass="H#YnXvqM",
        hidden=var_0,
        containerUnique=var_3,
        persistentType=var_4,
        ormType=var_4,
        interfaceType=var_0,
        unique=var_3,
        placeholder=var_4,
        validationPattern=459.83,
        inputColumnClass=var_0,
        persistence_Attribute11=var_5,
    )
    assert isinstance(var_6, python_code_.persistence_Attribute)
    var_7 = python_code_.isHasChoices
    var_8 = python_code_.persistence_DataType()
    var_9 = python_code_.persistence_DataTypeAttribute(
        obfuscateFormFields=var_0,
        caseInsensitive=var_3,
        encrypt=var_7,
        persistence_DataTypeAttribute=var_8,
    )
    assert isinstance(var_9, python_code_.persistence_DataTypeAttribute)


def test_30():
    var_0 = False
    var_2 = python_code_.persistence_ModelLabel(
        format="_persistence_ModelLabel__partOf",
        customise=False,
        ModelLabel=None,
        persistence_ModelLabel27=var_0,
    )
    assert isinstance(var_2, python_code_.persistence_ModelLabel)


def test_31():
    var_1 = bytes
    var_16 = python_code_.persistence_ModelLabelAssociation(
        isSourceAssociation=True,
        persistence_ModelLabelAssociation=var_1,
        persistence_ModelLabelAssociation26=None,
    )
    assert isinstance(var_16, python_code_.persistence_ModelLabelAssociation)


@pytest.mark.xfail(strict=True)
def test_32():
    var_0 = python_code_.persistence_ModelLabel
    var_1 = python_code_.persistence_UrlAttribute(displayValue=var_0)
    assert isinstance(var_1, python_code_.persistence_UrlAttribute)
    var_2 = python_code_.DatabaseTechnologies.Oracle
    var_3 = True
    var_4 = python_code_.persistence_ModelLabelAssociation(isSourceAssociation=var_3)
    assert isinstance(var_4, python_code_.persistence_ModelLabelAssociation)
    var_17 = python_code_.PathElement()
    var_18 = "<vu_G"
    var_19 = True
    var_20 = "persistence_Attribute23"
    var_21 = "kD!:Pm0nF>C{T\x0bM;8j=v"
    var_22 = '!<lv\r"I'
    var_23 = python_code_.persistence_Association(
        bidirectional=var_0,
        unique=var_0,
        pivotTableName=var_18,
        targetFeatureName=var_17,
        targetPrimaryKey=["\\?=H$!%", 3425.94, False],
        targetColumnName="ANS4:x1UJL-\n#8QH7V!",
        targetDisplayLabel=var_20,
        targetHeaderClass=var_18,
        targetInputClass=var_0,
        targetDisplayClass=var_18,
        targetFooterClass=var_0,
        pseudo=var_18,
        inputColumnClass=var_21,
        inputElementClass=var_22,
        serializationMaxDepth=var_2,
        persistence_Association=var_20,
        persistence_Association35=[False, 1530.06, "h j?KYOA\r[30q"],
    )
    assert isinstance(var_23, python_code_.persistence_Association)
    var_26 = python_code_.persistence_SerializationGroup()
    var_28 = "aB`91(]jDHk\rP\x0cW"
    var_29 = "persistence_Feature39"
    var_30 = "$g\t,~#8Q\x0b"
    var_31 = True
    var_32 = "[P$9gn\\fw~%+"
    var_33 = python_code_.persistence_AssociationKey()
    var_34 = python_code_.persistence_SerializationGroup()
    var_35 = python_code_.persistence_SerializationGroup()
    var_36 = {var_26, var_26, var_34, var_35, var_26}
    var_37 = python_code_.persistence_Feature(
        cardinality=var_17,
        ordered=var_20,
        primaryKey=var_22,
        derived=var_19,
        customiseSet=True,
        booleanIsHasChoice=var_0,
        title=var_30,
        collectionOrmAllowAdd={"1UVqlZpXtIt0Lh-}C3$": -4411.03},
        collectionOrmAllowRemove=var_3,
        defaultDisplayValue=var_22,
        emptyDisplayValue=var_28,
        encodeUriKey=var_31,
        singletonName=var_32,
        pluralisedName=b"\x96\xe0\xee\xb4\xec\x14lY\xe0\x19\x9d\x81U\x97",
        columnName=var_18,
        headerClass=var_17,
        displayClass=var_20,
        footerClass=var_21,
        persistence_Feature60=var_33,
        features=var_4,
        persistence_Feature=var_36,
    )
    assert isinstance(var_37, python_code_.persistence_Feature)
    var_38 = {var_37, var_37, var_37}
    python_code_.persistence_Entity(
        pluralisedName=None,
        singletonName=var_22,
        tableName=var_28,
        autoKeyName=894.18,
        autoKeyPersistentType=var_29,
        autoKeyGenerationStrategy=var_29,
        implementsUserInterface=var_3,
        allowFormTypeCustomisation=b"\x93{\x11\xafhE\x12",
        persistence_Entity38=var_0,
        persistence_Entity44=787.77,
        persistence_Entity52=var_38,
        persistence_Entity=var_2,
    )


def test_33():
    var_1 = "$-Ec.+e@"
    var_2 = python_code_.persistence_StaticPathElement(element=var_1)
    assert isinstance(var_2, python_code_.persistence_StaticPathElement)
    var_4 = bytes
    var_5 = True
    var_6 = "\t(=w"
    var_7 = python_code_.persistence_Attribute(
        inputElementClass=var_4,
        hidden={"T/:": True, "*A}/l q\tU' nRD\x0b$p/": 820, "k28Z3B": True},
        containerUnique=var_5,
        persistentType=var_4,
        ormType=var_1,
        interfaceType=[False, 2371],
        unique=var_5,
        placeholder=var_1,
        validationPattern=var_6,
        inputColumnClass=var_1,
        persistence_Attribute11=True,
    )
    assert isinstance(var_7, python_code_.persistence_Attribute)
    var_10 = python_code_.isHasChoices.isA
    var_13 = python_code_.persistence_DataTypeAttribute(
        obfuscateFormFields={
            "_persistence_ModelLabel__ModelLabel47 persistence_ModelLabelAttribute _persistence_Entity__persistence_Entity41": "_persistence_Association__persistence_Association._persistence_Entity__persistence_Entity41.Feature.Idiorm",
            "MK`B2)": 3,
        },
        caseInsensitive=var_5,
        encrypt=var_4,
    )
    assert isinstance(var_13, python_code_.persistence_DataTypeAttribute)
    var_14 = False
    var_20 = python_code_.persistence_LocationAttribute()
    var_21 = python_code_.persistence_DataTypeAttribute(
        obfuscateFormFields=b"\xe8\xb6\xbc\xeb\xfb\xdf\xbd",
        caseInsensitive=var_4,
        encrypt=var_14,
    )
    var_24 = "xxq(I+UK$.w\tj}dDBF"
    var_25 = "persistence_ModelLabel"
    python_code_.persistence_Attribute(
        inputElementClass=var_1,
        hidden=-1,
        containerUnique=[],
        persistentType=var_21,
        ormType=var_24,
        interfaceType=var_25,
        unique=var_20,
        placeholder=var_4,
        validationPattern=var_24,
        inputColumnClass=var_24,
        persistence_Attribute32=var_10,
    )
