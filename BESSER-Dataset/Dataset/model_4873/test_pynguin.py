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
    ConfigurableElement,
    Enum,
    Interface,
    Persistency,
    Property,
    PropertyTypes,
    Security,
    Source,
    SourceActiveStates,
    SourceState,
    abstractmethod,
    application_ApplicationKeyConfig,
    application_ConfigurableElement,
    application_Configuration,
    application_DataSet,
    application_Database,
    application_FEEDInterface,
    application_Interface,
    application_MappingRule,
    application_Mashup,
    application_MashupAdmin,
    application_MashupContainer,
    application_OAuthAdmin,
    application_OAuthClientConfig,
    application_OAuthClientScope,
    application_OAuthConfig,
    application_OCLRestrictedProperty,
    application_Persistency,
    application_Property,
    application_RESTInterface,
    application_Security,
    application_Source,
    application_XMLFile,
    date,
    datetime,
    time,
)


def test_0():
    var_1 = "?[u|Jd<1"
    var_2 = python_code_.application_ConfigurableElement(
        name=var_1,
        configurationImage={False, False},
        description=var_1,
        changeable=var_1,
        hidden=False,
        ident=var_1,
    )
    assert isinstance(var_2, python_code_.application_ConfigurableElement)
    var_2.getPropertyValue(application_key=var_2)


def test_1():
    var_0 = python_code_.application_Database()
    var_1 = "Qa>"
    var_2 = lambda *args, **kwargs: []
    var_3 = "G b}+HLY6!d\tAnH!)"
    var_4 = "k\\llukb%e>;m/\\9+v3E"
    var_5 = python_code_.application_OAuthClientScope(
        positiveTag=var_1,
        negativeTag="~LFQaoHJu^#n}",
        positiveMetaTag=var_3,
        negativeMetaTag=var_4,
        positiveCategory=var_1,
        negativeCategory=var_4,
        positivePerson=var_3,
        negativePerson=var_3,
        positiveOrganisation="CPYDn>l1AK?\x0c\\",
        negativeOrganisation="mashup7:application_Interface",
        identSpecification=var_4,
        allowPersons=var_4,
        allowContents="mashupAdmins,_application_Interface__application_Interface",
        allowOrganisations="application_Mashup16:application_MashupContainer15",
        maximumAge="Stoped UploadFile Integer _application_Mashup__application_Mashup",
    )
    var_6 = "application_OAuthConfig29.application_OAuthAdmin.WaitingForUpdate"
    var_7 = python_code_.application_Interface(
        urlSuffix=var_6,
        frontEndCaching=var_5,
        application_Interface=b"c\xe1\xdfZ\xd2\xae\xf4vc\xb0\x1fQ\x17\x08n{",
        interfaces=["w"],
    )
    assert isinstance(var_7, python_code_.application_Interface)
    var_8 = python_code_.application_Property(
        changeable={
            "-\tyAvZ\"7JJ%0'M\\": -704.43,
            "_application_MashupAdmin__application_MashupAdmin.Updating.MashupAdmin": 207,
        },
        possibleValues=var_2,
        helpText=var_4,
        required=var_5,
        propertyType=1589.05,
        Key=var_0,
        Value=var_0,
        hidden=b"\xbd\x922]\x01\xb3\x163|",
        application_Property=var_2,
    )
    var_8.isValueRange()


def test_2():
    var_9 = lambda *args, **kwargs: True
    python_code_.application_OAuthAdmin(
        username=set(), passwordHash=var_9, application_OAuthAdmin=var_9
    )


def test_3():
    var_1 = "?[u|J<1"
    var_2 = python_code_.application_ConfigurableElement(
        name=var_1,
        configurationImage={False, False},
        description=var_1,
        changeable=var_1,
        hidden=False,
        ident=var_1,
    )
    assert isinstance(var_2, python_code_.application_ConfigurableElement)
    var_2.getPropertyValue(application_key=var_2)
    var_34 = 'Axf"|\t,K<0aV9nGk]'
    var_35 = ""
    python_code_.application_OAuthAdmin(username=var_34, passwordHash=var_35)


def test_4():
    var_1 = "?[u|Jd<1"
    var_2 = python_code_.application_ConfigurableElement(
        name=var_1,
        configurationImage={False, False},
        description=var_1,
        changeable=var_1,
        hidden=False,
        ident=var_1,
    )
    assert isinstance(var_2, python_code_.application_ConfigurableElement)
    var_28 = python_code_.application_OAuthConfig(useScopeInterfaceOnRedirect=var_1)
    assert isinstance(var_28, python_code_.application_OAuthConfig)


def test_5():
    var_1 = "?[u|J<1"
    var_2 = python_code_.application_ConfigurableElement(
        name=var_1,
        configurationImage=var_1,
        description="UploadZipFile:application_OAuthClientConfig",
        changeable=">@8!;s,Z",
        hidden=var_1,
        ident="S[k",
    )
    assert isinstance(var_2, python_code_.application_ConfigurableElement)
    var_26 = "=g9S*:U_o[)'p\tyc[U"
    var_27 = "aaIQ?\\!C\tZ\nR"
    var_28 = python_code_.application_MashupContainer(
        backupConfiguration=var_27,
        backupIntervall=var_26,
        immediateSave=var_26,
        createAccountsAtLoginTry=var_27,
        identCounter=var_26,
    )
    assert isinstance(var_28, python_code_.application_MashupContainer)


@pytest.mark.xfail(strict=True)
def test_6():
    var_0 = python_code_.Property()
    var_1 = python_code_.application_DataSet
    var_2 = "application_MashupContainer"
    var_3 = python_code_.application_MashupContainer(
        backupConfiguration=var_1,
        backupIntervall=(True, True, True),
        immediateSave=var_2,
        createAccountsAtLoginTry=var_0,
        identCounter=var_2,
    )
    assert isinstance(var_3, python_code_.application_MashupContainer)
    var_5 = ".6Eh>"
    var_6 = python_code_.application_ConfigurableElement(
        name=var_2,
        configurationImage=var_2,
        description=var_5,
        changeable="sources",
        hidden=var_2,
        ident=var_2,
    )
    assert isinstance(var_6, python_code_.application_ConfigurableElement)
    var_6.getPropertyValueElseDefault(
        application_key=var_6, application_defaultValue=b"\x9d[\x9d\xb5<\x87\xa7\xaeI"
    )
    var_8 = python_code_.application_OCLRestrictedProperty(OCLRestriction=var_2)
    assert isinstance(var_8, python_code_.application_OCLRestrictedProperty)
    var_6.getProperty(application_key=var_8)
    var_10 = set
    python_code_.application_OAuthAdmin(username=var_10, passwordHash=var_2)
    var_12 = var_3.setNewIdentFor(application_configurableElement=var_5)
    var_14 = python_code_.application_Security()
    var_17 = '7~o"{{9./Sq@'
    var_22 = "application_MappingRule Source"
    var_23 = "5j#ln"
    var_24 = "b_Z1CLnAgKY=+"
    var_25 = "r"
    var_26 = "application_OAuthConfig"
    var_27 = var_3.getNewIdentNumber()
    var_28 = python_code_.application_Mashup(
        workingDirectory=var_8,
        cacheAttachments=var_25,
        cacheDataSet=var_2,
        backupDataSet={-214, 1321.61},
        backupIntervall=var_26,
        cacheDelay=var_26,
        sourceIdentCounter=b"\x00<\xe4\xb43\tg\xec~\xb0\x97U\x17/B\x83",
        keepDeletedItemsList=var_10,
        configurableMashups=var_27,
    )
    assert isinstance(var_28, python_code_.application_Mashup)
    var_29 = python_code_.application_Source(
        bundleId=None,
        state=var_1,
        activeState=var_23,
        logLevel=var_1,
        removeDataOnStop=var_1,
        updateRound=var_24,
        application_Source2=(372, 1491, "_application_Interface__interfaces"),
        Source=var_28,
    )
    assert isinstance(var_29, python_code_.application_Source)
    var_30 = var_29.start()
    var_31 = "_application_Mashup__application_Mashup"
    var_32 = (
        lambda *args, **kwargs: "_application_MashupContainer__application_MashupContainer18._application_MashupAdmin__MashupAdmin.sources._application_Property__application_Property"
    )
    var_33 = '\x0b!*y0R#^Q"Y@uK'
    var_34 = python_code_.application_Property(
        changeable=var_5,
        possibleValues=var_32,
        helpText={},
        required=1,
        propertyType=var_5,
        Key=var_23,
        Value=var_33,
        hidden=b"d\xbbs\x82",
    )
    var_35 = var_34.getMaxValue()
    var_36 = python_code_.application_MashupAdmin(
        provider=None,
        id=var_30,
        name=var_31,
        localIdent=var_14,
        isConfigurationAdmin=var_32,
        profileImage=var_22,
        email=var_25,
        MashupAdmin=-1368.12,
        mashupAdmins=var_35,
    )
    assert isinstance(var_36, python_code_.application_MashupAdmin)
    var_38 = var_29.pause()
    python_code_.application_MashupContainer(
        backupConfiguration=var_10,
        backupIntervall=var_10,
        immediateSave=var_23,
        createAccountsAtLoginTry=var_17,
        identCounter=var_12,
        application_MashupContainer13={
            "_application_MashupAdmin__application_MashupAdmin"
        },
        application_MashupContainer15=var_38,
        application_MashupContainer18=1782,
        application_MashupContainer21=(),
    )


@pytest.mark.xfail(strict=True)
def test_7():
    var_0 = python_code_.application_OAuthConfig(useScopeInterfaceOnRedirect={})
    assert isinstance(var_0, python_code_.application_OAuthConfig)
    var_1 = python_code_.Security()
    var_2 = bool
    var_3 = "_application_Mashup__Mashup33:_application_Interface__interface"
    var_4 = python_code_.application_Source(
        bundleId=var_2,
        state=var_3,
        activeState=var_2,
        logLevel=var_3,
        removeDataOnStop=(),
        updateRound=var_1,
        Source=-801.74,
    )
    assert isinstance(var_4, python_code_.application_Source)
    var_5 = var_4.stop()
    var_6 = "R,-29g_)GjidG"
    var_7 = "vB=~r"
    var_8 = "application_Mashup"
    var_9 = python_code_.application_ConfigurableElement(
        name=var_6,
        configurationImage=var_2,
        description=var_6,
        changeable=var_7,
        hidden=var_3,
        ident=var_8,
    )
    assert isinstance(var_9, python_code_.application_ConfigurableElement)
    var_10 = var_9.addProperty(application_property=var_2)
    var_11 = python_code_.application_MashupContainer(
        backupConfiguration=var_3,
        backupIntervall=None,
        immediateSave=False,
        createAccountsAtLoginTry=var_3,
        identCounter=var_3,
        application_MashupContainer15=var_10,
    )
    assert isinstance(var_11, python_code_.application_MashupContainer)
    var_12 = var_11.getMashupWithIdent(application_ident=2373.24)
    var_13 = bool
    python_code_.application_MashupContainer(
        backupConfiguration=var_3,
        backupIntervall="s_JIm",
        immediateSave=-883.31,
        createAccountsAtLoginTry=b"]\x07\xc4\xed\xd9\xe3",
        identCounter=var_2,
        application_MashupContainer=var_5,
        application_MashupContainer13=var_12,
        application_MashupContainer18=var_13,
    )


def test_8():
    var_1 = "?[u|J<1"
    var_2 = python_code_.application_ConfigurableElement(
        name="Yj",
        configurationImage=var_1,
        description=var_1,
        changeable=var_1,
        hidden=var_1,
        ident="ZXVp[\x0bRrm",
    )
    assert isinstance(var_2, python_code_.application_ConfigurableElement)
    var_2.getPropertyValue(application_key=var_2)
    var_4 = "BMr`\t|T4-PiM"
    var_5 = python_code_.PropertyTypes
    var_6 = "[Ru\x0c<He"
    var_7 = python_code_.application_Property(
        changeable=var_4,
        possibleValues=var_1,
        helpText=var_5,
        required=var_6,
        propertyType=set(),
        Key=var_5,
        Value={},
        hidden=var_6,
    )
    var_7.getMaxValue()


def test_9():
    var_0 = python_code_.Interface()
    var_1 = "?[u|J<1"
    var_2 = python_code_.application_ConfigurableElement(
        name=var_1,
        configurationImage={False, False},
        description=var_1,
        changeable=var_1,
        hidden=False,
        ident=var_1,
    )
    assert isinstance(var_2, python_code_.application_ConfigurableElement)
    var_2.getPropertyValue(application_key=var_1)
    var_6 = "[Ru\x0c<He"
    var_26 = "[Ru\x0c<He"
    var_27 = ",~/Rx\x0c@0Uk<[H`"
    var_29 = "Boolean"
    var_30 = "tMDA9mA"
    var_31 = "SM\te_\x0c){|"
    var_32 = "Unknown"
    var_33 = lambda *args, **kwargs: False
    var_34 = "Error_application_MashupContainer__application_MashupContainer15Float_application_OAuthConfig__application_OAuthConfig"
    var_35 = python_code_.application_MashupAdmin(
        provider=var_32,
        id=var_33,
        name=var_34,
        localIdent=set(),
        isConfigurationAdmin=None,
        profileImage=var_26,
        email=var_27,
    )
    assert isinstance(var_35, python_code_.application_MashupAdmin)
    var_36 = python_code_.application_Mashup(
        workingDirectory=None,
        cacheAttachments=var_6,
        cacheDataSet=var_29,
        backupDataSet=var_0,
        backupIntervall=var_27,
        cacheDelay=var_30,
        sourceIdentCounter=var_31,
        keepDeletedItemsList=None,
        application_Mashup=var_30,
        Mashup33=var_35,
    )
    assert isinstance(var_36, python_code_.application_Mashup)


def test_10():
    var_45 = '"m9X9ID_SwcGhF\tO'
    var_46 = "/^Sg>*yuAkcnOE?"
    var_47 = "_application_Interface__interfaces:_application_Interface__Interface:_application_Interface__interfaces"
    var_48 = python_code_.application_Mashup(
        workingDirectory=var_45,
        cacheAttachments=var_45,
        cacheDataSet=var_46,
        backupDataSet=None,
        backupIntervall=var_45,
        cacheDelay=var_47,
        sourceIdentCounter=b"\xbd\xe4:[O9\xbe\x9f\xe5&\x96",
        keepDeletedItemsList=var_45,
        configurableMashups=var_46,
    )
    assert isinstance(var_48, python_code_.application_Mashup)


def test_11():
    var_4 = "k\\llukb%e>;m/\\9+v3E"
    var_41 = " *P`=v`D;>\nH]"
    var_46 = "/^Sg>*yuAkcnOE?"
    var_48 = python_code_.application_Mashup(
        workingDirectory="R]w\t{^`M]A,",
        cacheAttachments=var_46,
        cacheDataSet="cy!<-,zK",
        backupDataSet="application_OAuthAdmin_application_Interface__Interface26_application_OAuthClientConfig__application_OAuthClientConfig31",
        backupIntervall=var_41,
        cacheDelay=var_46,
        sourceIdentCounter=var_4,
        keepDeletedItemsList=var_46,
    )
    assert isinstance(var_48, python_code_.application_Mashup)


def test_12():
    var_0 = python_code_.ConfigurableElement()
    var_1 = "w(E]h!J\t5y9."
    var_2 = python_code_.application_Security()
    var_3 = python_code_.application_Interface(
        urlSuffix=var_1, frontEndCaching=var_1, Interface26=var_2
    )
    assert isinstance(var_3, python_code_.application_Interface)
    var_4 = "Gn9/"
    var_5 = "_application_OAuthConfig__application_OAuthConfig"
    var_6 = "WtVAQ_`\x0cgiYlcC*7'c"
    var_7 = "M)w**2b/oK?"
    var_8 = python_code_.application_OCLRestrictedProperty
    var_9 = "application_Security"
    var_10 = "MkS&8Fdxy!Agc"
    var_11 = python_code_.application_Persistency()
    var_12 = python_code_.application_Source(
        bundleId=var_8,
        state=var_6,
        activeState=var_9,
        logLevel=var_9,
        removeDataOnStop={},
        updateRound=var_10,
        application_Source=var_11,
    )
    assert isinstance(var_12, python_code_.application_Source)
    var_13 = var_12.pause()
    var_14 = "-PQd0A,7|"
    var_15 = "Paused"
    var_16 = python_code_.application_MashupAdmin(
        provider=None,
        id=var_14,
        name="application_MashupContainer15-_application_Interface__interfaces",
        localIdent=var_12,
        isConfigurationAdmin=var_15,
        profileImage=var_4,
        email="{\\,*B4r8Ah",
    )
    assert isinstance(var_16, python_code_.application_MashupAdmin)
    var_17 = "h!tD:J#"
    var_18 = "4z\x0c,DAg\x0cW7?aN./q2|"
    var_19 = "d"
    var_20 = python_code_.application_Property(
        changeable=[-1012, "application_MashupContainer18", -1],
        possibleValues=var_14,
        helpText=var_19,
        required=complex(-1588.2356211, -4884.3),
        propertyType=var_5,
        Key=var_12,
        Value=var_10,
        hidden=complex(1665.5768039, -438.155306),
        application_Property=var_8,
    )
    var_21 = var_20.getMinValue()
    var_22 = python_code_.application_MashupContainer(
        backupConfiguration=var_17,
        backupIntervall=213.82,
        immediateSave=var_18,
        createAccountsAtLoginTry=var_10,
        identCounter=complex(-330.0519, -3875.663),
        application_MashupContainer15=var_21,
    )
    assert isinstance(var_22, python_code_.application_MashupContainer)
    var_23 = python_code_.application_Mashup(
        workingDirectory=var_1,
        cacheAttachments=(),
        cacheDataSet=var_0,
        backupDataSet=var_5,
        backupIntervall=var_6,
        cacheDelay=var_7,
        sourceIdentCounter=var_5,
        keepDeletedItemsList=var_8,
        mashup=var_13,
        Mashup33=var_16,
        application_Mashup11=var_8,
        application_Mashup19=var_22,
    )
    assert isinstance(var_23, python_code_.application_Mashup)
    python_code_.application_Source(
        bundleId=var_2,
        state=var_1,
        activeState=var_4,
        logLevel=-3539,
        removeDataOnStop=var_4,
        updateRound=var_4,
        application_Source=var_2,
        sources=("4Ydml&3U= udiF",),
        Source=var_23,
    )
    var_12.start()


def test_13():
    var_27 = ">^d>_-H'z4\reXhn5F"
    var_29 = "-PQ0A,7|"
    var_30 = "Paused"
    var_31 = "h!tD:J#"
    var_44 = "zy}h-U\x0c[>4"
    var_45 = lambda *args, **kwargs: []
    var_46 = "+'o%n\t?@P\tR_/8"
    var_47 = "uDxuY&lTN"
    var_51 = python_code_.application_OAuthConfig(useScopeInterfaceOnRedirect=var_29)
    assert isinstance(var_51, python_code_.application_OAuthConfig)
    var_52 = python_code_.application_OAuthClientConfig(
        type=var_46,
        redirectionURL=var_45,
        name=var_30,
        description=var_31,
        clientID=var_45,
        clientSecret=b"P\xa0JV\xb3\x9d\xa9\xea",
        code=var_45,
        grantType=var_46,
        refreshToken=var_31,
        accessToken=None,
        accessTokenCreationDate=var_45,
        accessTokenExpirationDate=var_31,
        forbiddenMetaTags=complex(3189.773, -5149.0),
        allowedMetaTags=complex(-651.3656699, 942.165),
        oAuthScopeLevel=var_27,
        application_OAuthClientConfig=var_51,
    )
    assert isinstance(var_52, python_code_.application_OAuthClientConfig)
    var_53 = 'm*U5a~"Lx9p+~{-9x'
    var_54 = "J"
    var_55 = python_code_.application_Mashup(
        workingDirectory=var_46,
        cacheAttachments=var_44,
        cacheDataSet=var_47,
        backupDataSet=var_53,
        backupIntervall=var_27,
        cacheDelay=var_30,
        sourceIdentCounter=var_54,
        keepDeletedItemsList=(),
        application_Mashup16=4691.25,
    )
    assert isinstance(var_55, python_code_.application_Mashup)
    var_55.getSourceWithIdent(application_ident=var_55)


@pytest.mark.xfail(strict=True)
def test_14():
    var_0 = '"mUm&1VmF$6~'
    var_1 = repr
    var_3 = ""
    var_4 = "application_OAuthAdmin"
    var_5 = "sources:_application_OAuthClientConfig__application_OAuthClientConfig:application_Mashup:_application_OAuthClientConfig__application_OAuthClientConfig"
    var_6 = lambda *args, **kwargs: 2863
    var_7 = python_code_.application_Persistency()
    var_8 = "Interface-mashup7"
    var_9 = "_application_Mashup__application_Mashup"
    var_10 = "_application_Property__application_Property,_application_Mashup__application_Mashup16,String,Initialized"
    var_11 = python_code_.application_Mashup(
        workingDirectory=set(),
        cacheAttachments=var_1,
        cacheDataSet=var_8,
        backupDataSet=var_9,
        backupIntervall=["\x0c+S/H[x-{Xu|mr"],
        cacheDelay=var_10,
        sourceIdentCounter={True, "sD+]jbPM[6zmO2YTY&?"},
        keepDeletedItemsList=var_3,
    )
    assert isinstance(var_11, python_code_.application_Mashup)
    python_code_.application_Source(
        bundleId=var_0,
        state=3,
        activeState=None,
        logLevel=var_5,
        removeDataOnStop=var_6,
        updateRound=var_4,
        application_Source=var_7,
        application_Source2=var_1,
        sources=var_11,
    )


def test_15():
    var_1 = "?[u|J<1"
    var_2 = python_code_.application_ConfigurableElement(
        name=var_1,
        configurationImage={False, False},
        description=var_1,
        changeable=var_1,
        hidden=False,
        ident=var_1,
    )
    assert isinstance(var_2, python_code_.application_ConfigurableElement)
    var_3 = var_2.getPropertyValue(application_key=var_2)
    var_4 = "BMr`\t|T4-PiM"
    var_5 = python_code_.PropertyTypes
    var_6 = "[Ru\x0c<He"
    var_7 = python_code_.application_Property(
        changeable=var_4,
        possibleValues=var_1,
        helpText=var_5,
        required=var_6,
        propertyType=set(),
        Key=var_5,
        Value={},
        hidden=var_6,
    )
    var_7.getMaxValue()
    var_9 = ",~/Rx\x0c@0Uk<[H`"
    var_10 = "_Ki{zwq@Ptu~O|Z@"
    var_11 = "mashup7"
    var_12 = python_code_.application_Mashup(
        workingDirectory=var_6,
        cacheAttachments=var_9,
        cacheDataSet=var_5,
        backupDataSet=(),
        backupIntervall=var_10,
        cacheDelay=var_11,
        sourceIdentCounter=None,
        keepDeletedItemsList=False,
        Mashup=var_2,
        application_Mashup={True, False, 27.1},
        application_Mashup16=b'"F',
        application_Mashup19=var_3,
    )
    assert isinstance(var_12, python_code_.application_Mashup)
    var_12.getNewSourceIdent()
    var_2.getProperty(application_key=var_11)
    var_16 = "N\x0b.C n"
    var_17 = "0dda\t"
    var_18 = "mashupAdmins"
    var_19 = python_code_.application_Source(
        bundleId=var_5,
        state=var_6,
        activeState=var_16,
        logLevel=var_17,
        removeDataOnStop=var_16,
        updateRound=var_18,
        application_Source2=complex(-1381.24378, -645.9785),
        Source=var_12,
    )
    assert isinstance(var_19, python_code_.application_Source)
    var_19.pause()


def test_16():
    var_1 = "?[u|J<1"
    var_2 = python_code_.application_ConfigurableElement(
        name=var_1,
        configurationImage=var_1,
        description="UploadZipFile:application_OAuthClientConfig",
        changeable=">@8!;s,Z",
        hidden=var_1,
        ident="S[k",
    )
    assert isinstance(var_2, python_code_.application_ConfigurableElement)
    var_26 = "=g9S*:U_o[)'p\tyc[U"
    var_27 = "aaIQ?\\!C\tZ\n?"
    var_28 = python_code_.application_MashupContainer(
        backupConfiguration=var_27,
        backupIntervall=var_26,
        immediateSave=var_26,
        createAccountsAtLoginTry=var_27,
        identCounter=var_26,
    )
    assert isinstance(var_28, python_code_.application_MashupContainer)
    var_42 = "mashup7"
    var_44 = "N\x0b.C n"
    var_46 = "mashupAdmins"
    var_47 = python_code_.application_Source
    var_48 = "Paused._application_OAuthConfig__application_OAuthConfig"
    var_49 = python_code_.application_Source(
        bundleId=var_1,
        state=var_47,
        activeState=var_44,
        logLevel=var_42,
        removeDataOnStop=var_48,
        updateRound=(-710, True),
        sources=var_47,
        Source=var_46,
    )
    assert isinstance(var_49, python_code_.application_Source)
    var_49.start()


def test_17():
    var_1 = "?[u{|Jj<1"
    var_33 = python_code_.application_OAuthConfig(useScopeInterfaceOnRedirect=var_1)
    assert isinstance(var_33, python_code_.application_OAuthConfig)
    var_44 = "Date"
    var_45 = "_application_Source__sources"
    var_46 = "x3/\n}~a<-*"
    var_47 = python_code_.application_Source(
        bundleId=var_44,
        state={},
        activeState={"@P<ebSst^2dz": "^H>)y=!yzps", "application_Security": -3314.95},
        logLevel=var_45,
        removeDataOnStop=var_46,
        updateRound=893.58,
        application_Source=(-3106.65, 252.47),
    )
    assert isinstance(var_47, python_code_.application_Source)
    var_47.start()


def test_18():
    var_44 = python_code_.application_Persistency()
    var_46 = "Paused"
    var_57 = lambda *args, **kwargs: 173
    var_58 = python_code_.application_DataSet()
    var_59 = python_code_.application_Interface
    var_60 = python_code_.application_Source(
        bundleId=complex(301.621, -2443.0),
        state={},
        activeState=var_46,
        logLevel=var_44,
        removeDataOnStop=var_57,
        updateRound=var_57,
        application_Source2=var_58,
        sources=var_58,
        Source=var_59,
    )
    assert isinstance(var_60, python_code_.application_Source)
    var_60.start()
    var_51 = lambda *args, **kwargs: []
    var_52 = "+'o%n\t?@P\tR_/8"
    var_53 = "uDuY&lTN"
    var_54 = "_application_ConfigurableElement__application_ConfigurableElement"
    var_55 = python_code_.application_OAuthConfig(useScopeInterfaceOnRedirect=var_52)
    assert isinstance(var_55, python_code_.application_OAuthConfig)
    var_56 = python_code_.application_OAuthClientConfig(
        type=var_52,
        redirectionURL=var_51,
        name=var_46,
        description=var_53,
        clientID=var_51,
        clientSecret=b"P\xa0JV\xb3\x9d\xa9\xea",
        code=var_51,
        grantType=var_52,
        refreshToken=var_53,
        accessToken=None,
        accessTokenCreationDate=var_51,
        accessTokenExpirationDate=var_53,
        forbiddenMetaTags=complex(3189.773, -5149.0),
        allowedMetaTags=complex(-651.3656699, 942.165),
        oAuthScopeLevel=var_54,
        application_OAuthClientConfig=var_55,
    )
    assert isinstance(var_56, python_code_.application_OAuthClientConfig)


def test_19():
    var_1 = "w(E]h!J\t5y9."
    var_2 = python_code_.application_Security()
    var_3 = python_code_.application_Interface(
        urlSuffix=var_1, frontEndCaching=var_1, Interface26=var_2
    )
    assert isinstance(var_3, python_code_.application_Interface)


@pytest.mark.xfail(strict=True)
def test_20():
    var_0 = "UploadZipFile-_application_MashupContainer__application_MashupContainer21"
    var_1 = python_code_.application_Database
    var_2 = python_code_.application_Property(
        changeable=var_0,
        possibleValues=var_1,
        helpText=var_0,
        required=-1555.24,
        propertyType=False,
        Key=var_0,
        Value=var_0,
        hidden=var_1,
    )
    var_3 = var_2.getListOfValues()
    var_4 = python_code_.application_OAuthConfig(useScopeInterfaceOnRedirect=var_0)
    assert isinstance(var_4, python_code_.application_OAuthConfig)
    var_5 = "Boolean"
    var_6 = "kQ[zRtR"
    var_7 = "Active"
    var_8 = "R"
    var_9 = "ApWc_q/}|jLT[<"
    var_10 = python_code_.application_ConfigurableElement(
        name=var_9,
        configurationImage=var_8,
        description=var_9,
        changeable=b"\\\xd6=",
        hidden=var_1,
        ident=var_7,
    )
    assert isinstance(var_10, python_code_.application_ConfigurableElement)
    var_11 = var_10.getPropertyValue(application_key=var_1)
    var_12 = "k:3U"
    var_13 = "4BD<>DZ3Y3y|EU2"
    var_14 = python_code_.application_Mashup(
        workingDirectory=var_8,
        cacheAttachments=2623,
        cacheDataSet=var_9,
        backupDataSet=var_8,
        backupIntervall=(),
        cacheDelay=var_1,
        sourceIdentCounter=var_1,
        keepDeletedItemsList=False,
        Mashup33=var_1,
        application_Mashup19="application_Mashup16",
    )
    assert isinstance(var_14, python_code_.application_Mashup)
    var_15 = python_code_.application_Interface(
        urlSuffix=var_12, frontEndCaching=var_13, Interface=var_14
    )
    assert isinstance(var_15, python_code_.application_Interface)
    python_code_.application_Mashup(
        workingDirectory=var_6,
        cacheAttachments=var_7,
        cacheDataSet=[
            "Integer._application_Source__application_Source2",
            1504.23,
            -2398.64,
        ],
        backupDataSet=var_8,
        backupIntervall=var_8,
        cacheDelay=var_8,
        sourceIdentCounter=")H",
        keepDeletedItemsList=var_5,
        application_Mashup=var_1,
        configurableMashups=var_11,
        Mashup33=False,
        application_Mashup19=var_3,
        Mashup24=var_15,
    )


def test_21():
    python_code_.Interface()


def test_22():
    var_2 = "application_MashupCBntainer"
    var_3 = python_code_.application_MashupContainer(
        backupConfiguration="^zo-*Tr==jK=\n=~cJ_6",
        backupIntervall=var_2,
        immediateSave=var_2,
        createAccountsAtLoginTry=var_2,
        identCounter="{SFSSeWgc",
        application_MashupContainer={var_2, var_2},
        application_MashupContainer18=set(),
    )
    assert isinstance(var_3, python_code_.application_MashupContainer)
    var_3.setNewIdentFor(application_configurableElement=None)
    var_5 = "B/!./|4J<Y8rn%"
    var_6 = python_code_.application_ConfigurableElement(
        name=var_2,
        configurationImage=var_2,
        description=var_5,
        changeable="sources",
        hidden=var_2,
        ident=var_2,
    )
    assert isinstance(var_6, python_code_.application_ConfigurableElement)
    var_6.getPropertyValueElseDefault(
        application_key=var_6, application_defaultValue=b"\x9d[\x9d\xb5<\x87\xa7\xaeI"
    )
    var_8 = python_code_.application_OCLRestrictedProperty(OCLRestriction=var_2)
    assert isinstance(var_8, python_code_.application_OCLRestrictedProperty)
    var_6.getProperty(application_key=var_8)
    var_10 = set
    python_code_.application_OAuthAdmin(
        username=var_2, passwordHash='sl]Ut"\\}mz!m#', application_OAuthAdmin=None
    )
    var_25 = "r"
    var_26 = "application_OAuthConfig"
    var_27 = var_3.getNewIdentNumber()
    var_28 = python_code_.application_Mashup(
        workingDirectory=var_8,
        cacheAttachments=var_25,
        cacheDataSet=var_2,
        backupDataSet={-214, 1321.61},
        backupIntervall=var_26,
        cacheDelay=var_26,
        sourceIdentCounter=b"\x00<\xe4\xb43\tg\xec~\xb0\x97U\x17/B\x83",
        keepDeletedItemsList=var_10,
        configurableMashups=var_27,
    )
    assert isinstance(var_28, python_code_.application_Mashup)


def test_23():
    var_0 = python_code_.application_Database()
    var_1 = "Qa>"
    var_2 = lambda *args, **kwargs: []
    var_4 = "k\\llukb%e>;m/\\9+v3E"
    var_39 = 'm|5c2"f7'
    var_50 = "application_MashupContainer15-Active"
    var_51 = "obP@B6c<|\\s \x0c:g"
    var_52 = python_code_.application_ConfigurableElement(
        name=var_2,
        configurationImage=b"/\x19\xa3n\x14:\xba\xbf\x94)",
        description=var_50,
        changeable=var_51,
        hidden=var_0,
        ident=var_4,
        application_ConfigurableElement=var_1,
    )
    assert isinstance(var_52, python_code_.application_ConfigurableElement)
    var_52.isPropertyTrue(application_key=var_39)


def test_24():
    var_1 = "?[u|J<1"
    var_26 = 'p#"ScN6-dKM9'
    var_30 = python_code_.application_ApplicationKeyConfig(applicationKeys=var_26)
    assert isinstance(var_30, python_code_.application_ApplicationKeyConfig)
    var_33 = python_code_.application_OAuthConfig(useScopeInterfaceOnRedirect=var_1)
    assert isinstance(var_33, python_code_.application_OAuthConfig)
    var_34 = "rE=LcVd 7r"
    var_35 = python_code_.application_OCLRestrictedProperty(OCLRestriction=var_34)
    assert isinstance(var_35, python_code_.application_OCLRestrictedProperty)


def test_25():
    var_39 = dict
    var_40 = ";X%\\f\\\r0"
    var_42 = "V9\tce'"
    var_43 = "MkS&8Fdxy!Agc"
    var_44 = python_code_.application_Persistency()
    var_45 = python_code_.application_Source(
        bundleId=var_39,
        state=var_42,
        activeState=var_40,
        logLevel=var_40,
        removeDataOnStop={},
        updateRound=var_43,
        application_Source=var_44,
    )
    assert isinstance(var_45, python_code_.application_Source)
    var_45.pause()
    var_47 = "-PQd0A,7|"
    var_48 = "Paused"
    var_49 = python_code_.application_MashupAdmin(
        provider=None,
        id=var_47,
        name="application_MashupContainer15-_application_Interface__interfaces",
        localIdent=var_45,
        isConfigurationAdmin=var_48,
        profileImage=var_42,
        email="{\\,*B4r8Ah",
    )
    assert isinstance(var_49, python_code_.application_MashupAdmin)
    var_52 = "d"
    var_53 = python_code_.application_Property(
        changeable=[-1012, "application_MashupContainer18", -1],
        possibleValues=var_47,
        helpText=var_52,
        required=complex(-1588.2356211, -4884.3),
        propertyType=var_43,
        Key=var_45,
        Value=var_43,
        hidden=complex(1665.5768039, -438.155306),
        application_Property=var_39,
    )
    assert isinstance(var_53, python_code_.application_Property)
    var_53.getMinValue()
    var_53.isValueList()


def test_26():
    var_0 = "UploadZipFile-_application_MashupContainer__application_MashupContainer21"
    var_1 = python_code_.application_Database
    var_2 = python_code_.application_Property(
        changeable=var_0,
        possibleValues=var_1,
        helpText=var_0,
        required=-1555.24,
        propertyType=False,
        Key=var_0,
        Value=var_0,
        hidden=var_1,
    )
    var_3 = var_2.getListOfValues()
    var_4 = python_code_.application_OAuthConfig(
        useScopeInterfaceOnRedirect=var_0, application_OAuthConfig={var_3, var_0, var_3}
    )
    assert isinstance(var_4, python_code_.application_OAuthConfig)
    var_50 = 'm|5c2"f7'
    var_59 = python_code_.application_RESTInterface(type=var_50)
    assert isinstance(var_59, python_code_.application_RESTInterface)


def test_27():
    var_1 = "?[u|J<1"
    var_2 = python_code_.application_ConfigurableElement(
        name=var_1,
        configurationImage={False, False},
        description=var_1,
        changeable=var_1,
        hidden=False,
        ident=var_1,
    )
    assert isinstance(var_2, python_code_.application_ConfigurableElement)
    var_2.getPropertyValue(application_key=var_2)
    var_4 = "BMr`\t|T4-PiM"
    var_5 = python_code_.PropertyTypes
    var_6 = "[Ru\x0c<He"
    var_7 = python_code_.application_Property(
        changeable=var_4,
        possibleValues=var_1,
        helpText=var_5,
        required=var_6,
        propertyType=set(),
        Key=var_5,
        Value={},
        hidden=var_6,
    )
    var_7.getMaxValue()
    var_21 = "_application_ConfigurableElement__application_ConfigurableElement-_application_ConfigurableElement__application_ConfigurableElement-WaitingForUpdate"
    var_22 = "_application_Mashup__mashup7"
    var_23 = "@qt$Cc|V\tV\x0bXx%u="
    var_24 = "rePs'8RlQ(a/7X"
    var_25 = python_code_.application_Source(
        bundleId=var_21,
        state=var_22,
        activeState=var_24,
        logLevel=var_23,
        removeDataOnStop="application_Configuration:_application_MashupContainer__application_MashupContainer21:_application_Mashup__Mashup24:Filling",
        updateRound=var_24,
        application_Source=False,
    )
    assert isinstance(var_25, python_code_.application_Source)
    var_25.getLogLevelIntValue()
    var_27 = python_code_.application_RESTInterface(type=var_5)
    assert isinstance(var_27, python_code_.application_RESTInterface)
    var_28 = python_code_.application_XMLFile()
    var_25.pause()
    var_32 = "Date"
    var_33 = python_code_.application_MashupAdmin(
        provider=var_28,
        id=var_32,
        name={
            '\x0cBof".}@NCzJ ': 0,
            "]gg<LaO\\7'|R[TA": 299,
            "application_Persistency application_MappingRule _application_MashupContainer__application_MashupContainer13": 114,
        },
        localIdent=var_23,
        isConfigurationAdmin=None,
        profileImage=var_5,
        email=var_24,
    )
    assert isinstance(var_33, python_code_.application_MashupAdmin)


def test_28():
    var_1 = "?[u|J<1"
    var_2 = python_code_.application_ConfigurableElement(
        name=var_1,
        configurationImage={False, False},
        description=var_1,
        changeable=var_1,
        hidden=False,
        ident=var_1,
    )
    assert isinstance(var_2, python_code_.application_ConfigurableElement)
    var_2.getPropertyValue(application_key=var_2)
    var_34 = 'Axf"|\t,K<0aV9nGk]'
    var_35 = ""
    python_code_.application_OAuthAdmin(username=var_34, passwordHash=var_35)
    var_38 = "Tn|%'Rq#U|U9#"
    var_39 = python_code_.application_Security()
    var_40 = python_code_.application_Interface(
        urlSuffix=var_38, frontEndCaching=var_38, interface=var_39
    )
    assert isinstance(var_40, python_code_.application_Interface)


def test_29():
    var_0 = python_code_.application_OCLRestrictedProperty(OCLRestriction=1414.14)
    assert isinstance(var_0, python_code_.application_OCLRestrictedProperty)
    var_20 = "application_Security"
    var_38 = "of#dB\x0cHP'zb\x0c3j"
    var_39 = "=g9=*:U_o[)'p\tyc[U"
    var_40 = "aaIQ?\\!C\tZ\n?"
    var_41 = python_code_.application_MashupContainer(
        backupConfiguration=var_38,
        backupIntervall=var_39,
        immediateSave=var_39,
        createAccountsAtLoginTry=var_40,
        identCounter=var_20,
    )
    assert isinstance(var_41, python_code_.application_MashupContainer)
    var_41.getConfigurationAdmins()


def test_30():
    var_1 = "?[u|J<1"
    var_30 = "Paused"
    var_44 = "zy}h-U\x0c[>4"
    var_45 = lambda *args, **kwargs: []
    var_47 = "uDuY&lTN"
    var_51 = python_code_.application_OAuthConfig(useScopeInterfaceOnRedirect=var_44)
    assert isinstance(var_51, python_code_.application_OAuthConfig)
    var_52 = python_code_.application_OAuthClientConfig(
        type=var_44,
        redirectionURL=var_45,
        name=var_1,
        description=var_47,
        clientID=var_45,
        clientSecret=b"P\xa0JV\xb3\x9d\xa9\xea",
        code=var_45,
        grantType=var_44,
        refreshToken=var_47,
        accessToken=None,
        accessTokenCreationDate=var_45,
        accessTokenExpirationDate=var_47,
        forbiddenMetaTags=complex(3189.773, -5149.0),
        allowedMetaTags=complex(-651.3656699, 942.165),
        oAuthScopeLevel=var_30,
        application_OAuthClientConfig=var_51,
    )
    assert isinstance(var_52, python_code_.application_OAuthClientConfig)


def test_31():
    var_0 = python_code_.ConfigurableElement()
    var_39 = "application_Security"
    var_41 = "of#dB\x0cHP'zb\x0c3j"
    var_42 = "=g9=*:U_o[)'p\tyc[U"
    var_43 = "aaIQ?\\!C\tZ\n?"
    var_44 = python_code_.application_MashupContainer(
        backupConfiguration=var_41,
        backupIntervall=var_42,
        immediateSave=var_42,
        createAccountsAtLoginTry=var_43,
        identCounter=var_39,
    )
    assert isinstance(var_44, python_code_.application_MashupContainer)
    var_44.getConfigurationAdmins()
    var_53 = "_application_Interface__Interface26:application_MashupAdmin:application_OAuthConfig29"
    var_54 = "\nnp[S"
    var_55 = "St\x0c<D\x0chX"
    var_56 = lambda *args, **kwargs: []
    var_57 = python_code_.application_OAuthClientConfig(
        type=[
            "application_OAuthConfig,application_Configuration,application_Security",
            "Mashup33-application_MashupContainer18-MashupAdmin",
        ],
        redirectionURL=var_39,
        name=var_44,
        description=var_53,
        clientID=var_0,
        clientSecret=var_42,
        code=var_54,
        grantType=var_55,
        refreshToken=complex(-947.115, 2240.3),
        accessToken=var_53,
        accessTokenCreationDate=False,
        accessTokenExpirationDate=None,
        forbiddenMetaTags=var_56,
        allowedMetaTags=var_55,
        oAuthScopeLevel=var_43,
        application_OAuthClientConfig31=var_41,
    )
    assert isinstance(var_57, python_code_.application_OAuthClientConfig)


def test_32():
    var_0 = "`za"
    var_1 = ".&S=9KCc"
    var_2 = python_code_.application_Configuration()
    var_3 = python_code_.application_ConfigurableElement(
        name=var_0,
        configurationImage=var_0,
        description=var_0,
        changeable=var_1,
        hidden=complex(-1489.403746, 585.479),
        ident=var_0,
        application_ConfigurableElement=var_2,
    )
    assert isinstance(var_3, python_code_.application_ConfigurableElement)
    var_4 = python_code_.application_Configuration
    var_3.addProperty(application_property=var_4)


def test_33():
    var_38 = "M)w**2b/oK?"
    var_39 = "application_Security"
    var_41 = "of#dB\x0cHP'zb\x0c3j"
    var_42 = "=g9=*:U_o[)'p\tyc[U"
    var_43 = "aaIQ?\\!C\tZ\n?"
    var_44 = python_code_.application_MashupContainer(
        backupConfiguration=var_41,
        backupIntervall=var_42,
        immediateSave=var_42,
        createAccountsAtLoginTry=var_43,
        identCounter=var_39,
    )
    assert isinstance(var_44, python_code_.application_MashupContainer)
    var_44.getConfigurationAdmins()
    var_58 = python_code_.ConfigurableElement()
    var_53 = "_application_Interface__Interface26:application_MashupAdmin:application_OAuthConfig29"
    var_55 = "St\x0c<D\x0chX"
    var_56 = lambda *args, **kwargs: []
    var_60 = python_code_.Source()
    var_62 = "[Ru\x0c<He"
    var_63 = ",~/Rx\x0c@0Uk<[H`"
    var_64 = "Source"
    var_65 = "application_OAuthClientScope"
    var_66 = python_code_.application_FEEDInterface(
        allowPersonFiltering=var_53,
        allowOrganisationFiltering=var_43,
        allowTypeFiltering=b"\x95E\x92 \xc1zgj\xd2\xd3\n\x11\xb2\xf9\x89\xe5\x82",
        allowTagFiltering=var_64,
        allowMetaTagFiltering=var_63,
        allowCategoryFiltering=var_38,
        language=var_58,
        feedType=var_65,
        feedTitle=var_60,
    )
    assert isinstance(var_66, python_code_.application_FEEDInterface)
    var_67 = "3F\nGq]Th\nsYr%&'UaH"
    var_68 = python_code_.application_ConfigurableElement(
        name=var_62,
        configurationImage=var_56,
        description=complex(464.62352, 608.22),
        changeable=var_67,
        hidden={True, False, -2350.82},
        ident=var_60,
    )
    assert isinstance(var_68, python_code_.application_ConfigurableElement)
    var_68.isPropertyTrueElseDefault(
        application_key=var_56, application_defaultValue=var_55
    )


@pytest.mark.xfail(strict=True)
def test_34():
    var_0 = python_code_.ConfigurableElement()
    var_1 = "w(E]h!J\t5y9."
    var_39 = "application_Security"
    var_41 = "of#dB\x0cHP'zb\x0c3j"
    var_42 = "=g9=*:U_o[)'p\tyc[U"
    var_43 = "aaIQ?\\!C\tZ\n?"
    var_44 = python_code_.application_MashupContainer(
        backupConfiguration=var_41,
        backupIntervall=var_42,
        immediateSave=var_42,
        createAccountsAtLoginTry=var_43,
        identCounter=var_39,
    )
    assert isinstance(var_44, python_code_.application_MashupContainer)
    var_46 = "(`N=U6&N2/#[N"
    var_53 = "_application_Interface__Interface26:application_MashupAdmin:application_OAuthConfig29"
    var_54 = "\nnp[S"
    var_55 = "St\x0c<D\x0chX"
    var_56 = lambda *args, **kwargs: []
    var_57 = python_code_.application_OAuthClientConfig(
        type=[
            "application_OAuthConfig,application_Configuration,application_Security",
            "Mashup33-application_MashupContainer18-MashupAdmin",
        ],
        redirectionURL=var_39,
        name=var_44,
        description=var_53,
        clientID=var_0,
        clientSecret=var_42,
        code=var_54,
        grantType=var_55,
        refreshToken=complex(-947.115, 2240.3),
        accessToken=var_53,
        accessTokenCreationDate=False,
        accessTokenExpirationDate=None,
        forbiddenMetaTags=var_56,
        allowedMetaTags=var_55,
        oAuthScopeLevel=var_43,
        application_OAuthClientConfig31=var_41,
    )
    assert isinstance(var_57, python_code_.application_OAuthClientConfig)
    var_47 = python_code_.application_Persistency()
    var_50 = "h!tD:J#"
    var_60 = "rE=LcVd 7r"
    var_61 = python_code_.application_OCLRestrictedProperty(OCLRestriction=var_60)
    assert isinstance(var_61, python_code_.application_OCLRestrictedProperty)
    var_62 = "#+ |K"
    var_63 = "\\16W'C*KyZc"
    var_64 = "_application_Source__application_Source"
    var_65 = "_application_Interface__Interface_application_MashupAdmin__application_MashupAdminapplication_OAuthConfig"
    var_66 = ".m2EM`QO_\tRV]Ky57W("
    var_67 = "FVv}"
    var_68 = "AB9j"
    var_69 = python_code_.application_ConfigurableElement(
        name=-1,
        configurationImage=var_67,
        description=b"|\xa9\xb1L\xb7\x0b\x83V\xcb,V\x8d\r\xfe\x06\x01}",
        changeable=0,
        hidden=909,
        ident=var_56,
        application_ConfigurableElement={-1912, 1175, "pZqaYe_d"},
    )
    assert isinstance(var_69, python_code_.application_ConfigurableElement)
    var_70 = var_69.getProperty(application_key=var_0)
    var_71 = python_code_.application_Mashup(
        workingDirectory=var_47,
        cacheAttachments=var_1,
        cacheDataSet=set(),
        backupDataSet=var_56,
        backupIntervall=889,
        cacheDelay=var_67,
        sourceIdentCounter=var_68,
        keepDeletedItemsList=set(),
        configurableMashups=var_70,
        application_Mashup11=var_44,
        application_Mashup19=var_44,
    )
    assert isinstance(var_71, python_code_.application_Mashup)
    var_72 = python_code_.application_Source(
        bundleId=var_0,
        state=var_46,
        activeState=var_50,
        logLevel=var_56,
        removeDataOnStop=var_66,
        updateRound=var_56,
        application_Source2=-2042,
        sources=var_1,
        Source=var_71,
    )
    assert isinstance(var_72, python_code_.application_Source)
    python_code_.application_Mashup(
        workingDirectory=var_57,
        cacheAttachments=var_62,
        cacheDataSet=var_63,
        backupDataSet=complex(-825.571, 89.2),
        backupIntervall=var_64,
        cacheDelay=var_56,
        sourceIdentCounter={},
        keepDeletedItemsList=var_65,
        Mashup=var_72,
        application_Mashup11=None,
    )


@pytest.mark.xfail(strict=True)
def test_35():
    var_2 = lambda *args, **kwargs: []
    var_4 = "k\\llukb%e>;m/\\9+v3!E"
    var_39 = 'm|5c2"f7'
    var_59 = "Date"
    var_60 = "_application_Source__sources"
    var_61 = "x3/\n}~a<-*"
    var_62 = python_code_.application_Source(
        bundleId=var_59,
        state={},
        activeState={"@P<ebSst^2dz": "^H>)y=!yzps", "application_Security": -3314.95},
        logLevel=var_60,
        removeDataOnStop=var_61,
        updateRound=893.58,
        application_Source=(-3106.65, 252.47),
    )
    assert isinstance(var_62, python_code_.application_Source)
    var_62.start()
    var_65 = "'|CoV"
    var_66 = "EO"
    python_code_.application_MashupContainer(
        backupConfiguration=var_65,
        backupIntervall=var_39,
        immediateSave=var_4,
        createAccountsAtLoginTry=var_66,
        identCounter=var_4,
        application_MashupContainer15=341.99,
        application_MashupContainer18=var_2,
    )
