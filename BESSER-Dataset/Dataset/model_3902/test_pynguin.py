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
    Collaboration,
    FreeFormValue,
    NodeDescriptor,
    Participant,
    date,
    datetime,
    soaml_Agent,
    soaml_Artifact,
    soaml_Attachment,
    soaml_Capability,
    soaml_Catalog,
    soaml_Categorization,
    soaml_Category,
    soaml_CategoryValue,
    soaml_Class,
    soaml_Collaboration,
    soaml_CollaborationUse,
    soaml_Comment,
    soaml_Connector,
    soaml_Consumer,
    soaml_DataType,
    soaml_Dependency,
    soaml_Expose,
    soaml_FreeFormDescriptor,
    soaml_FreeFormValue,
    soaml_Interface,
    soaml_MessageType,
    soaml_Milestone,
    soaml_MotivationRealization,
    soaml_NodeDescriptor,
    soaml_Package,
    soaml_Participant,
    soaml_Port,
    soaml_Property,
    soaml_Provider,
    soaml_Realization,
    soaml_Request,
    soaml_Service,
    soaml_ServiceArchitecture,
    soaml_ServiceChannel,
    soaml_ServiceContract,
    soaml_ServiceInterface,
    soaml_Signal,
    soaml_ValueSpecification,
    time,
)


def test_0():
    python_code_.soaml_MessageType(
        encoding="_soaml_Milestone__soaml_Milestone42",
        soaml_MessageType=None,
        soaml_MessageType34=None,
    )


def test_1():
    var_8 = python_code_.soaml_FreeFormDescriptor()
    python_code_.soaml_MessageType(encoding="UU|q&", soaml_MessageType36=var_8)


def test_2():
    var_8 = python_code_.soaml_FreeFormDescriptor()
    python_code_.soaml_MessageType(
        encoding="orsoPv5UZe/VA5\tTHC", soaml_MessageType34=var_8
    )


def test_3():
    var_9 = python_code_.soaml_Class()
    python_code_.soaml_MessageType(encoding="H3[*fng#MK", soaml_MessageType=var_9)


@pytest.mark.xfail(strict=True)
def test_4():
    var_18 = {
        "F\r&g#0skw/`]_#]Yle": 1480.89,
        "WK'OQE%6y-?Y": 3204.79,
        "|dc4v%\r^\rG": "n:w}",
    }
    var_19 = "_soaml_Property__soaml_Property49,_saml_Property__soaml_Property27,soaml_Class,soaml_Class32"
    var_20 = python_code_.soaml_Property(isID=var_19)
    python_code_.soaml_Attachment(
        encoding=var_18, mimeType=var_19, soaml_Attachment=var_20
    )


@pytest.mark.xfail(strict=True)
def test_5():
    var_42 = python_code_.soaml_FreeFormDescriptor()
    var_44 = python_code_.soaml_Property(isID=2, soaml_Property27=-783.84)
    assert isinstance(var_44, python_code_.soaml_Property)
    var_45 = "yFjHe\\"
    var_46 = python_code_.soaml_Attachment(encoding=var_45, mimeType=var_45)
    python_code_.soaml_Property(
        isID=var_42, soaml_Property=var_44, soaml_Property30=var_46
    )


def test_6():
    python_code_.soaml_Property(isID="MNm?R(&")


def test_7():
    var_47 = python_code_.soaml_Property(
        isID=complex(2054.296321, 1887.0168), soaml_Property27=(), soaml_Property30=True
    )
    assert isinstance(var_47, python_code_.soaml_Property)


def test_8():
    var_42 = python_code_.soaml_FreeFormDescriptor()
    python_code_.soaml_Property(
        isID="iRd) _", soaml_Property27=None, soaml_Property49=var_42
    )


@pytest.mark.xfail(strict=True)
def test_9():
    var_39 = python_code_.soaml_Property(isID=complex(-3289.40642, -1567.3514885))
    python_code_.soaml_Property(isID="1\\|0)o\r\x0c_\tr go5we", soaml_Property=var_39)


def test_10():
    python_code_.soaml_Port(connectorRequired="zys }E}l~-B7}7:m2")


def test_11():
    var_0 = "}@"
    var_4 = python_code_.soaml_Port(
        connectorRequired=var_0, soaml_Port23=complex(1355.3, 2098.8374418)
    )
    assert isinstance(var_4, python_code_.soaml_Port)


def test_12():
    var_0 = "soaml_Serice"
    var_4 = python_code_.soaml_Port(connectorRequired='0e\nd<"(sxw', soaml_Port25=var_0)
    assert isinstance(var_4, python_code_.soaml_Port)


@pytest.mark.xfail(strict=True)
def test_13():
    var_0 = python_code_.FreeFormValue()
    var_2 = python_code_.soaml_Service()
    var_3 = python_code_.soaml_Port(connectorRequired=var_0, soaml_Port25=var_2)
    var_4 = lambda *args, **kwargs: True
    python_code_.soaml_Port(
        connectorRequired=var_0, soaml_Port=var_3, soaml_Port20=var_4
    )


def test_14():
    var_4 = python_code_.soaml_Signal()
    var_5 = "B~"
    var_6 = python_code_.soaml_CategoryValue
    python_code_.soaml_Property(isID=var_5, soaml_Property27=var_6)
    var_9 = "b{\\P*@d)'}?j"
    python_code_.soaml_CollaborationUse(isStrict=var_9)
    python_code_.soaml_CollaborationUse(isStrict=var_9, soaml_CollaborationUse2=var_4)
    var_15 = python_code_.soaml_Port(connectorRequired=var_9, soaml_Port=[True])
    assert isinstance(var_15, python_code_.soaml_Port)
    python_code_.soaml_Attachment(encoding=[], mimeType=var_5)


def test_15():
    var_37 = python_code_.soaml_Milestone(progress="\\Tl'jc")
    assert isinstance(var_37, python_code_.soaml_Milestone)


def test_16():
    var_37 = python_code_.soaml_Milestone(
        progress="*esyU-", soaml_Milestone=set(), soaml_Milestone42=None
    )
    assert isinstance(var_37, python_code_.soaml_Milestone)


def test_17():
    var_42 = python_code_.soaml_Milestone(progress=-3341.36, soaml_Milestone42=3110.64)
    assert isinstance(var_42, python_code_.soaml_Milestone)


def test_18():
    var_42 = dict
    var_43 = python_code_.soaml_Milestone(
        progress=var_42, soaml_Milestone39=var_42, soaml_Milestone42=var_42
    )
    assert isinstance(var_43, python_code_.soaml_Milestone)


@pytest.mark.xfail(strict=True)
def test_19():
    var_0 = "}@"
    var_1 = lambda *args, **kwargs: -81
    var_2 = python_code_.soaml_CollaborationUse(
        isStrict=var_0, soaml_CollaborationUse=var_1
    )
    python_code_.soaml_CollaborationUse(isStrict=var_0, soaml_CollaborationUse=var_2)


def test_20():
    python_code_.soaml_CollaborationUse(
        isStrict="_soaml_Property__soaml_Property30", soaml_CollaborationUse=None
    )


def test_21():
    var_43 = python_code_.soaml_CollaborationUse(
        isStrict="_soaml_Milestone__soaml_Milestone42",
        soaml_CollaborationUse=[False, "_soaml_Collaboration__soaml_Collaboration"],
    )
    assert isinstance(var_43, python_code_.soaml_CollaborationUse)


def test_22():
    var_7 = python_code_.soaml_CollaborationUse(
        isStrict={
            "U@X~UUh4{lH": True,
            "soaml_Class32soaml_Collaboration": 1937.49,
            "zQ/~:;": 4126,
        },
        soaml_CollaborationUse={
            "ZV4UOS,Q": "~lj(9GNt9VFkZ~#r",
            "A\x0c\\`Q`Es\r": 845.78,
            "f}yz": 647.76,
        },
        soaml_CollaborationUse2=-2626.15,
    )
    assert isinstance(var_7, python_code_.soaml_CollaborationUse)


def test_23():
    var_12 = python_code_.soaml_Collaboration(
        isStrict=[
            193,
            "soaml_Port:soaml_Comment:soaml_Port20",
            "_soaml_Milestone__soaml_Milestone39",
        ],
        soaml_Collaboration0=False,
    )
    assert isinstance(var_12, python_code_.soaml_Collaboration)


@pytest.mark.xfail(strict=True)
def test_24():
    var_38 = "`P<OpkW7]\t\x0c\x0bSxKL3"
    var_39 = python_code_.soaml_Collaboration(
        isStrict="Qa!B", soaml_Collaboration0=None
    )
    python_code_.soaml_Collaboration(isStrict=var_38, soaml_Collaboration0=var_39)


def test_25():
    python_code_.soaml_Collaboration(isStrict="0|vDHj6T~maoMLf")


def test_26():
    python_code_.soaml_Participant()


@pytest.mark.xfail(strict=True)
def test_27():
    var_0 = python_code_.soaml_ServiceInterface()
    var_2 = python_code_.soaml_FreeFormValue()
    var_3 = python_code_.soaml_Attachment(encoding=var_0, mimeType=var_2)
    var_5 = "7Xn^?@!4M-|0S"
    python_code_.soaml_Property(
        isID=var_5, soaml_Property=var_0, soaml_Property30=var_3
    )


@pytest.mark.xfail(strict=True)
def test_28():
    var_2 = "Er1btYtn?-=j6$<bm-("
    var_3 = python_code_.soaml_Signal()
    var_4 = python_code_.soaml_Comment()
    var_5 = python_code_.soaml_Milestone(
        progress=var_2, soaml_Milestone39=var_3, soaml_Milestone42=var_4
    )
    assert isinstance(var_5, python_code_.soaml_Milestone)
    var_7 = python_code_.soaml_Category()
    var_8 = python_code_.soaml_Artifact()
    python_code_.soaml_Collaboration(isStrict=True)
    python_code_.soaml_Attachment(encoding=var_2, mimeType=var_2)
    var_15 = python_code_.soaml_DataType()
    python_code_.soaml_MessageType(
        encoding=-1225, soaml_MessageType=var_8, soaml_MessageType34=var_15
    )
    var_21 = "soaml_Class32"
    var_22 = python_code_.soaml_Port(
        connectorRequired=var_21, soaml_Port=var_7, soaml_Port23=-3378
    )
    assert isinstance(var_22, python_code_.soaml_Port)
    python_code_.soaml_Port(connectorRequired=var_2, soaml_Port20=var_22)


def test_29():
    var_2 = python_code_.soaml_Service()
    python_code_.soaml_Port(
        connectorRequired="^[IX1", soaml_Port20=None, soaml_Port23=var_2
    )
    var_7 = "|vtSP~XW<|iQ=LEX"
    python_code_.soaml_Port(connectorRequired=var_7)
    var_6 = python_code_.soaml_Collaboration(
        isStrict="_soaml_Collaboration__soaml_Collaboration",
        soaml_Collaboration=var_7,
        soaml_Collaboration0=None,
    )
    assert isinstance(var_6, python_code_.soaml_Collaboration)


@pytest.mark.xfail(strict=True)
def test_30():
    var_0 = python_code_.soaml_ServiceInterface()
    var_1 = python_code_.soaml_Attachment(encoding="=eDoRR)Uz!|)1t", mimeType="t=,^t;")
    var_3 = python_code_.soaml_Attachment(
        encoding="B&R*B:V%g\x0c%]>", mimeType="ia')j*Qx#E9", soaml_Attachment=var_1
    )
    var_5 = "7Xn^?@!4M-|0S"
    python_code_.soaml_Property(
        isID=var_5, soaml_Property=var_0, soaml_Property30=var_3
    )


@pytest.mark.xfail(strict=True)
def test_31():
    var_4 = lambda *args, **kwargs: True
    var_9 = python_code_.soaml_Collaboration(
        isStrict=[
            193,
            "soaml_Port:soaml_Comment:soaml_Port20",
            "_soaml_Milestone__soaml_Milestone39",
        ],
        soaml_Collaboration0=False,
    )
    assert isinstance(var_9, python_code_.soaml_Collaboration)
    python_code_.soaml_Collaboration(isStrict=var_4, soaml_Collaboration=var_9)


@pytest.mark.xfail(strict=True)
def test_32():
    var_2 = "_soaml_Property__soaml_Property27,soaml_Collaboration0,_soaml_Collaboration__soaml_Collaboration"
    python_code_.soaml_Property(isID=var_2)
    var_8 = "\r{33o|\nkr8S<i1[dz"
    var_9 = python_code_.soaml_Signal
    var_10 = python_code_.soaml_Collaboration(isStrict=var_8, soaml_Collaboration=var_9)
    var_11 = python_code_.soaml_Service()
    var_12 = python_code_.soaml_Port(
        connectorRequired="`C_.\x0c>=CWEaS2ET6d",
        soaml_Port=var_10,
        soaml_Port20=var_9,
        soaml_Port25=var_11,
    )
    python_code_.soaml_Port(connectorRequired=var_9, soaml_Port=var_12)


@pytest.mark.xfail(strict=True)
def test_33():
    var_35 = "w)|UqUcj"
    var_40 = python_code_.soaml_CollaborationUse(
        isStrict=var_35, soaml_CollaborationUse2=var_35
    )
    assert isinstance(var_40, python_code_.soaml_CollaborationUse)
    python_code_.soaml_CollaborationUse(isStrict=var_35, soaml_CollaborationUse=var_40)


@pytest.mark.xfail(strict=True)
def test_34():
    var_0 = "}@"
    var_1 = lambda *args, **kwargs: -81
    var_2 = python_code_.soaml_CollaborationUse(
        isStrict=var_0, soaml_CollaborationUse=var_1
    )
    python_code_.soaml_CollaborationUse(
        isStrict="N8u\x0cA0cd^3\\^f5", soaml_CollaborationUse2=var_2
    )


@pytest.mark.xfail(strict=True)
def test_35():
    var_0 = python_code_.soaml_ServiceChannel()
    var_11 = "K`5\x0bJi! "
    python_code_.soaml_MessageType(encoding=var_11, soaml_MessageType34=var_0)
    python_code_.soaml_CollaborationUse(isStrict=set())
    var_16 = python_code_.soaml_Request()
    var_17 = python_code_.soaml_FreeFormDescriptor()
    var_18 = python_code_.soaml_Property(
        isID=var_11, soaml_Property30=-1790, soaml_Property49=var_17
    )
    assert isinstance(var_18, python_code_.soaml_Property)
    python_code_.soaml_Attachment(
        encoding=var_16,
        mimeType=b"\xaa\xec\xcd\xcf=e8\xdbX\x14\tS",
        soaml_Attachment=var_18,
    )


@pytest.mark.xfail(strict=True)
def test_36():
    var_0 = '"Wi&@ZT=p'
    var_1 = python_code_.soaml_Package
    var_2 = python_code_.soaml_Property(isID=var_0, soaml_Property=var_1)
    python_code_.soaml_Property(isID={}, soaml_Property27=var_2)
