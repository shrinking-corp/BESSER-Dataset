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
    Counted,
    Enum,
    Labelled,
    Named,
    PlaceHolder,
    SequenceType,
    abstractmethod,
    date,
    datetime,
    publication_Counted,
    publication_Labelled,
    publication_Named,
    publication_Paper,
    publication_Paragraph,
    publication_PlaceHolder,
    publication_PlaceHolderPP,
    publication_PlaceHolderRn,
    publication_PlaceHolderRs,
    publication_PlaceHolderRule,
    publication_Progress,
    publication_PublicationPhase,
    publication_PublicationProcess,
    publication_PublicationStructure,
    publication_PublicationSystem,
    publication_Researcher,
    publication_Review,
    publication_ReviewNote,
    publication_Rule,
    publication_Sequence,
    publication_Write,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_4 = python_code_.publication_ReviewNote(content=complex(1128.9185, 1880.554))
    assert isinstance(var_4, python_code_.publication_ReviewNote)
    var_6 = 5607
    var_7 = python_code_.publication_Progress(percent=['Q"AILx%fQ"F\t'], time=var_6)
    assert isinstance(var_7, python_code_.publication_Progress)
    python_code_.publication_PublicationProcess(
        minTime=b'\r"\x01Q\xb05\xfb\x12\xa5\xda\xd8\xc8L',
        maxTime=var_6,
        publication_PublicationProcess35=var_7,
    )


def test_1():
    var_4 = python_code_.publication_Progress(percent=-2576, time=-2473, progress=None)
    assert isinstance(var_4, python_code_.publication_Progress)


def test_2():
    var_26 = python_code_.publication_PlaceHolderPP()
    var_27 = python_code_.publication_Researcher(
        name=var_26,
        forName=var_26,
        position=b"%EL8\x07\xc7O\xbb",
        publication_Researcher45=var_26,
        Researcher29=var_26,
    )
    assert isinstance(var_27, python_code_.publication_Researcher)
    var_28 = 0
    var_29 = python_code_.publication_Counted
    var_30 = python_code_.publication_Progress(
        percent=var_28, time=complex(-349.9, -3034.73), publication_Progress=var_29
    )
    assert isinstance(var_30, python_code_.publication_Progress)


def test_3():
    var_13 = 2663
    var_14 = python_code_.publication_Progress(
        percent=var_13, time=var_13, progress=var_13, Progress=None
    )
    assert isinstance(var_14, python_code_.publication_Progress)


def test_4():
    var_13 = 2663
    var_14 = python_code_.publication_Progress(
        percent=var_13, time=var_13, progress=None, Progress=var_13
    )
    assert isinstance(var_14, python_code_.publication_Progress)


def test_5():
    var_26 = python_code_.publication_PlaceHolderPP()
    var_27 = python_code_.publication_Researcher(
        name="0x?WAGq\x0b#2>",
        forName="_publication_Sequence__publication_Sequence15._publication_Researcher__publication_Researcher.publication_Review",
        position="publication_PublicationPhase7:finishToStart",
        neededPerson={
            "publication_PlaceHolderPPpublication_ReviewNote_publication_Progress__Progress_publication_Progress__progress"
        },
        publication_Researcher22={var_26},
    )
    assert isinstance(var_27, python_code_.publication_Researcher)


def test_6():
    var_26 = python_code_.publication_PlaceHolderPP()
    var_27 = python_code_.publication_Researcher(
        name="_publication_Rule__publication_Rule18",
        forName='5h^eOWau"{K-.i\x0bCQ!',
        position="_publication_PublicationPhase__publication_PublicationPhase16:publication_ReviewNote:_publication_Sequence__publication_Sequence15",
        publication_Researcher22={False, "Oh"},
        Researcher=var_26,
        authors=set(),
        Researcher29=None,
    )
    assert isinstance(var_27, python_code_.publication_Researcher)


def test_7():
    var_26 = python_code_.publication_PlaceHolderPP()
    var_27 = python_code_.publication_Researcher(
        name="*ydgH~,vi9l\t\r ",
        forName="[lQE-\x0boQwZ",
        position="51'mHN0l^Ftj>MQ",
        publication_Researcher={var_26},
        publication_Researcher22={-931, var_26},
        authors={var_26, 2828},
        publication_Researcher25=var_26,
    )
    assert isinstance(var_27, python_code_.publication_Researcher)


def test_8():
    python_code_.publication_Sequence(
        sequenceType="\tG\x0c-f]v", publication_Sequence15=None
    )
    var_10 = "eWv\n70s:bGx<h"
    var_11 = python_code_.publication_Researcher(
        name=var_10, forName=var_10, position=var_10
    )
    assert isinstance(var_11, python_code_.publication_Researcher)


def test_9():
    var_26 = python_code_.publication_PlaceHolderPP()
    var_27 = python_code_.publication_Researcher(
        name=var_26,
        forName=var_26,
        position=b"%EL8\x07\xc7O\xbb",
        publication_Researcher45=var_26,
        Researcher29=var_26,
    )
    assert isinstance(var_27, python_code_.publication_Researcher)


def test_10():
    python_code_.publication_Sequence(
        sequenceType="publication_Review",
        publication_Sequence12=None,
        publication_Sequence=None,
    )


def test_11():
    var_10 = python_code_.publication_Sequence(
        sequenceType=[],
        publication_Sequence15={},
        publication_Sequence=[331.76, 331.28, -2225],
    )
    assert isinstance(var_10, python_code_.publication_Sequence)


def test_12():
    var_0 = "publication_PulicationStructure"
    var_1 = python_code_.publication_PlaceHolderRn
    var_2 = python_code_.publication_PublicationPhase(
        name=var_0,
        minTime=1709,
        maxTime=2812,
        publication_PublicationPhase=var_0,
        publication_PublicationPhase13=var_1,
        publication_PublicationPhase4=set(),
    )
    assert isinstance(var_2, python_code_.publication_PublicationPhase)
    var_3 = python_code_.publication_Sequence(
        sequenceType=var_0,
        publication_Sequence12=complex(-1086.8053182, -262.548638),
        publication_Sequence=var_2,
    )
    assert isinstance(var_3, python_code_.publication_Sequence)
    var_24 = python_code_.publication_Named(name=[True, 1672.24])
    assert isinstance(var_24, python_code_.publication_Named)


def test_13():
    var_14 = -2984
    var_15 = python_code_.publication_Rule(
        text="publication_Paper",
        key='~8*al"OGy5@\x0bdq0BxB',
        publication_Rule=var_14,
        publication_Rule8=None,
    )
    assert isinstance(var_15, python_code_.publication_Rule)
    var_16 = {var_15, var_15, var_15}
    var_17 = python_code_.publication_PublicationProcess(
        minTime=var_14,
        maxTime=1696,
        publication_PublicationProcess=var_16,
        publication_PublicationProcess2=var_16,
        publication_PublicationProcess35=var_15,
    )
    assert isinstance(var_17, python_code_.publication_PublicationProcess)


def test_14():
    python_code_.publication_Rule(
        text="IB)X",
        key="publication_PublicationPhase7._publication_Paragraph__publication_Paragraph31",
    )


def test_15():
    var_14 = -2984
    var_15 = python_code_.publication_Rule(
        text=var_14,
        key={
            "_publication_Researcher__Researcher29": False,
            "publication_PlaceHolderPP:paper:publication_Sequence:paper": -320,
        },
        publication_Rule8=var_14,
    )
    assert isinstance(var_15, python_code_.publication_Rule)
    var_16 = {var_15, var_15, var_15}
    var_17 = python_code_.publication_PublicationProcess(
        minTime=var_14, maxTime=var_14, publication_PublicationProcess2=var_16
    )
    assert isinstance(var_17, python_code_.publication_PublicationProcess)


def test_16():
    python_code_.publication_Rule(text=None, key=[True, False, -1640])
    var_7 = python_code_.publication_Rule(
        text=(),
        key=(-1235, False),
        publication_Rule18=(False, 1594),
        publication_Rule8=b"_}\x00\x0eL",
    )
    assert isinstance(var_7, python_code_.publication_Rule)


def test_17():
    var_4 = python_code_.publication_Progress(percent=-2576, time=-2473, progress=None)
    assert isinstance(var_4, python_code_.publication_Progress)
    var_18 = "_publication_PublicationPhase__publication_PublicationPhase10:publication_Paragraph31:_publication_Rule__publication_Rule18:_publication_PublicationPhase__publication_PublicationPhase16"
    var_19 = python_code_.publication_PublicationPhase(
        name=var_4,
        minTime=[],
        maxTime=var_18,
        publication_PublicationPhase=1379.21,
        publication_PublicationPhase7=(),
    )
    assert isinstance(var_19, python_code_.publication_PublicationPhase)


def test_18():
    python_code_.publication_Sequence(
        sequenceType="\tG\x0c-f]v", publication_Sequence15=None
    )
    var_15 = '"]93'
    var_16 = python_code_.publication_PublicationPhase(
        name=var_15, minTime=2370.53, maxTime=var_15, phaseParticipation=var_15
    )
    assert isinstance(var_16, python_code_.publication_PublicationPhase)


def test_19():
    var_0 = "publication_PulicationStructure"
    var_1 = python_code_.publication_PlaceHolderRn
    var_2 = python_code_.publication_PublicationPhase(
        name=var_0,
        minTime=1709,
        maxTime=2812,
        publication_PublicationPhase=var_0,
        publication_PublicationPhase13=var_1,
        publication_PublicationPhase4=set(),
    )
    assert isinstance(var_2, python_code_.publication_PublicationPhase)


def test_20():
    var_10 = "eWv\n70s:bGx<h"
    var_11 = python_code_.publication_Researcher(
        name="yzKW7sK$fS%2VPyf",
        forName=var_10,
        position=var_10,
        publication_Researcher45=var_10,
        publication_Researcher22={var_10, var_10, var_10},
        authors={False},
    )
    assert isinstance(var_11, python_code_.publication_Researcher)
    var_12 = -3420
    var_13 = {var_11, var_11}
    var_14 = python_code_.publication_PublicationPhase(
        name=var_11,
        minTime=complex(-2101.0, 2865.0),
        maxTime=var_10,
        publication_PublicationPhase=var_12,
        PublicationPhase='wqUGH;XZo/d ,S"',
        publication_PublicationPhase4="publication_Review publication_Write",
        phaseParticipation=var_13,
    )
    assert isinstance(var_14, python_code_.publication_PublicationPhase)


def test_21():
    var_1 = "z7{BMiR`"
    var_21 = python_code_.publication_Paragraph(
        content="%Gd'I|My.", publication_Paragraph31=set(), publication_Paragraph=var_1
    )
    assert isinstance(var_21, python_code_.publication_Paragraph)
    var_23 = python_code_.publication_PlaceHolderPP()
    var_24 = "Paper"
    var_25 = -838
    var_26 = python_code_.publication_Paragraph
    var_27 = set()
    var_28 = python_code_.publication_PublicationPhase(
        name=var_24,
        minTime=var_25,
        maxTime=var_26,
        publication_PublicationPhase16=var_25,
        publication_PublicationPhase7=var_27,
        publication_PublicationPhase10=var_26,
    )
    assert isinstance(var_28, python_code_.publication_PublicationPhase)
    var_29 = {var_28, var_28, var_28}
    var_30 = python_code_.publication_Researcher(
        name=var_24,
        forName=var_23,
        position=var_1,
        neededPerson=var_29,
        authors=var_29,
        publication_Researcher25=var_26,
        Researcher29=var_26,
    )
    assert isinstance(var_30, python_code_.publication_Researcher)


def test_22():
    var_0 = "publication_PublicationStructure"
    var_1 = bool
    var_2 = python_code_.publication_PublicationPhase(
        name=var_0, minTime=var_0, maxTime=var_1, publication_PublicationPhase10=var_0
    )
    assert isinstance(var_2, python_code_.publication_PublicationPhase)
    var_40 = python_code_.publication_Rule(
        text=(),
        key=(-1235, False),
        publication_Rule18=(False, 1594),
        publication_Rule8=b"_}\x00\x0eL",
    )
    assert isinstance(var_40, python_code_.publication_Rule)


def test_23():
    var_4 = python_code_.publication_ReviewNote(
        content="Researcher", publication_ReviewNote=None, publication_ReviewNote33=None
    )
    assert isinstance(var_4, python_code_.publication_ReviewNote)


def test_24():
    var_4 = python_code_.publication_Progress(
        percent=1, time=-93, publication_Progress=None
    )
    assert isinstance(var_4, python_code_.publication_Progress)
    var_18 = python_code_.publication_PlaceHolderRule()
    var_20 = python_code_.publication_ReviewNote(
        content="_publication_Researcher__publication_Researcher22,finishToStart,publication_Rule8,publication_PlaceHolderRule",
        publication_ReviewNote43=var_18,
    )
    assert isinstance(var_20, python_code_.publication_ReviewNote)


def test_25():
    var_19 = python_code_.publication_Named(name="1\x0ceSDN'PuM[M^")
    assert isinstance(var_19, python_code_.publication_Named)
    var_21 = python_code_.publication_PlaceHolderRn()
    var_22 = python_code_.publication_ReviewNote(
        content="Paper37", publication_ReviewNote33=var_21
    )
    assert isinstance(var_22, python_code_.publication_ReviewNote)


def test_26():
    var_2 = python_code_.publication_Paragraph(
        content="_publication_Progress__progresspublication_Paragraph",
        publication_Paragraph40=None,
    )
    assert isinstance(var_2, python_code_.publication_Paragraph)


def test_27():
    var_11 = python_code_.publication_PublicationProcess(minTime=-1, maxTime=-507)
    assert isinstance(var_11, python_code_.publication_PublicationProcess)


def test_28():
    var_11 = python_code_.publication_PublicationProcess(
        minTime=3,
        maxTime=-1112,
        publication_PublicationProcess2={-2708.6, -1},
        publication_PublicationProcess50=None,
    )
    assert isinstance(var_11, python_code_.publication_PublicationProcess)


def test_29():
    var_41 = 1525
    var_42 = python_code_.publication_Named
    var_43 = python_code_.publication_PublicationProcess(
        minTime="u/}pW",
        maxTime=var_41,
        publication_PublicationProcess35=var_42,
        publication_PublicationProcess50=var_42,
    )
    assert isinstance(var_43, python_code_.publication_PublicationProcess)


def test_30():
    python_code_.publication_PlaceHolderRs()


def test_31():
    var_5 = python_code_.publication_Labelled(lname="458&6W<")
    assert isinstance(var_5, python_code_.publication_Labelled)


def test_32():
    var_11 = python_code_.publication_Counted(id=complex(-207.879, 242.93))
    assert isinstance(var_11, python_code_.publication_Counted)


def test_33():
    var_19 = python_code_.publication_Named(
        name="_publication_Rule__publication_Rule8 _publication_Researcher__neededPerson _publication_ReviewNote__publication_ReviewNote"
    )
    assert isinstance(var_19, python_code_.publication_Named)


def test_34():
    var_11 = python_code_.publication_PublicationProcess(minTime=2731, maxTime=-1)
    assert isinstance(var_11, python_code_.publication_PublicationProcess)
    var_12 = "pM1r\\{!jL]#.:>"
    var_13 = python_code_.publication_Sequence(sequenceType=var_12)
    var_14 = {var_13, var_13, var_13, var_13, var_13}
    var_15 = python_code_.publication_PublicationPhase(
        name=var_12,
        minTime=var_12,
        maxTime=var_12,
        publication_PublicationPhase=var_11,
        publication_PublicationPhase4=var_14,
        publication_PublicationPhase10=-1282,
    )
    assert isinstance(var_15, python_code_.publication_PublicationPhase)


def test_35():
    var_0 = 2893
    var_2 = python_code_.publication_PublicationPhase(
        name="_publication_Sequence__publication_Sequence15_publication_PublicationPhase__phaseParticipationResearcher",
        minTime=var_0,
        maxTime=var_0,
        publication_PublicationPhase13=None,
        publication_PublicationPhase4={"VX`Mf;g%V&N7_esK==("},
        publication_PublicationPhase7={var_0},
    )
    assert isinstance(var_2, python_code_.publication_PublicationPhase)
    var_3 = {var_2, var_2, var_2, var_2, var_2}
    var_4 = python_code_.publication_PublicationProcess(
        minTime=var_0,
        maxTime=b"\xb7\xd7\xe42V\x84\xfd@\x84N\xd3",
        publication_PublicationProcess=var_3,
        publication_PublicationProcess35=1797,
    )
    assert isinstance(var_4, python_code_.publication_PublicationProcess)
    var_18 = python_code_.publication_PlaceHolderPP()
    python_code_.publication_PublicationProcess(
        minTime=var_4,
        maxTime=var_0,
        publication_PublicationProcess35=var_18,
        publication_PublicationProcess50="=jwu6Z^Z-YT^gd6t$Tn",
    )


@pytest.mark.xfail(strict=True)
def test_36():
    python_code_.publication_Rule(
        text="_publication_Researcher__publication_Researcher:_publication_Progress__progress:publication_Sequence15:startToFinish",
        key="CLAQjNFe",
        publication_Rule=None,
    )
    var_4 = "_publication_Progress__progress-publication_Paper"
    var_5 = 2706
    var_6 = python_code_.publication_Sequence(sequenceType=set())
    python_code_.publication_PublicationPhase(
        name=var_4,
        minTime=var_5,
        maxTime=var_4,
        publication_PublicationPhase16=var_6,
        publication_PublicationPhase10=False,
    )


def test_37():
    var_1 = python_code_.publication_Rule(text=None, key=[True, False, -1640])
    var_3 = python_code_.publication_PublicationSystem()
    var_4 = python_code_.publication_PlaceHolderRule
    var_5 = {var_1, var_1, var_1, var_1}
    var_6 = python_code_.publication_PublicationPhase(
        name=var_1,
        minTime=var_3,
        maxTime=var_4,
        publication_PublicationPhase7=var_5,
        publication_PublicationPhase10=[],
    )
    assert isinstance(var_6, python_code_.publication_PublicationPhase)


def test_38():
    var_1 = python_code_.publication_Rule(text=None, key=[True, False, -1640])
    var_2 = python_code_.publication_Paragraph(
        content={},
        publication_Paragraph40=b"7&\xaeM\xc6\xf6'\xfdk\x1dj\xc6\xbd1",
        publication_Paragraph=var_1,
    )
    assert isinstance(var_2, python_code_.publication_Paragraph)


def test_39():
    var_0 = "publication_PublicationStructure"
    var_5 = python_code_.publication_PublicationSystem()
    var_6 = python_code_.publication_PublicationStructure()
    var_28 = 53
    var_29 = python_code_.publication_PublicationPhase(
        name={}, minTime=(2165.62,), maxTime=var_28, PublicationPhase=var_0
    )
    assert isinstance(var_29, python_code_.publication_PublicationPhase)
    var_34 = python_code_.publication_Rule(
        text=(),
        key=(-1235, False),
        publication_Rule18=(False, 1594),
        publication_Rule8=b"_}\x00\x0eL",
    )
    assert isinstance(var_34, python_code_.publication_Rule)
    var_30 = {var_29, var_29, var_29, var_29, var_29, var_5}
    var_31 = python_code_.publication_Paper()
    var_32 = python_code_.publication_Researcher(
        name=var_0,
        forName=var_6,
        position={},
        neededPerson=var_30,
        publication_Researcher22=var_30,
        Researcher29=var_31,
    )
    assert isinstance(var_32, python_code_.publication_Researcher)


@pytest.mark.xfail(strict=True)
def test_40():
    var_1 = python_code_.publication_Rule(
        text="}yaUPsH!(H~(M`~<\x0c", key=".)W9NLM'", publication_Rule8=None
    )
    var_4 = "[:]"
    var_5 = 2706
    var_6 = python_code_.publication_Sequence(
        sequenceType="zTnZ!Cud4<=+Ug!\x0bmr", publication_Sequence=None
    )
    python_code_.publication_PublicationPhase(
        name="$}IMv^!)P@\ru,YR'@g",
        minTime=3311,
        maxTime=var_5,
        publication_PublicationPhase=None,
        publication_PublicationPhase13=var_6,
        PublicationPhase=var_5,
        phaseParticipation={var_1, True, var_4},
        publication_PublicationPhase10=var_4,
    )


@pytest.mark.xfail(strict=True)
def test_41():
    var_2 = "publication_PublicationSystem,publication_PublicationPhase16,publication_Sequence15,publication_Sequence12"
    var_3 = python_code_.publication_ReviewNote(content=var_2)
    assert isinstance(var_3, python_code_.publication_ReviewNote)
    var_5 = list
    var_46 = 1430
    var_47 = -2331
    var_48 = python_code_.publication_PublicationProcess(
        minTime=var_47,
        maxTime=var_46,
        publication_PublicationProcess2="_publication_Sequence__publication_Sequence12",
    )
    assert isinstance(var_48, python_code_.publication_PublicationProcess)
    var_49 = 53
    var_50 = python_code_.publication_PublicationPhase(
        name={}, minTime=(2165.62,), maxTime=var_49, PublicationPhase=var_2
    )
    assert isinstance(var_50, python_code_.publication_PublicationPhase)
    var_53 = python_code_.publication_Rule(
        text=(),
        key=(-1235, False),
        publication_Rule18=(False, 1594),
        publication_Rule8=b"_}\x00\x0eL",
    )
    assert isinstance(var_53, python_code_.publication_Rule)
    var_54 = {var_50, var_50, var_50, var_50, var_50}
    var_57 = "publication_PlaceHolderPP"
    var_58 = python_code_.publication_Sequence(
        sequenceType=var_2,
        publication_Sequence12={-132.09, "\t&'>c"},
        publication_Sequence15=2588,
        publication_Sequence=b".<\x08\xf0",
    )
    assert isinstance(var_58, python_code_.publication_Sequence)
    python_code_.publication_PublicationPhase(
        name=var_57,
        minTime=var_54,
        maxTime=var_49,
        publication_PublicationPhase13=var_58,
        PublicationPhase=var_5,
        publication_PublicationPhase10=var_47,
    )


@pytest.mark.xfail(strict=True)
def test_42():
    var_0 = 2893
    var_1 = "z7{BMiR`"
    var_2 = python_code_.publication_PublicationPhase(
        name=var_1,
        minTime=var_0,
        maxTime="\x0b$%*562|Cu!I_`m3N",
        PublicationPhase=var_0,
        publication_PublicationPhase4=None,
    )
    assert isinstance(var_2, python_code_.publication_PublicationPhase)
    var_3 = {var_2, var_2, var_2, var_2, var_2}
    var_4 = python_code_.publication_PublicationProcess(
        minTime=var_0,
        maxTime=b"\xb7\xd7\xe42V\x84\xfd@\x84N\xd3",
        publication_PublicationProcess=var_3,
        publication_PublicationProcess35=1797,
    )
    assert isinstance(var_4, python_code_.publication_PublicationProcess)
    python_code_.publication_Progress(
        percent=False, time={1042, 1703.62}, publication_Progress=var_4
    )


def test_43():
    var_1 = "publication_PublicationProcess:phaseParticipation:Researcher"
    var_2 = python_code_.publication_Paragraph(content=var_1)
    assert isinstance(var_2, python_code_.publication_Paragraph)
    var_3 = python_code_.publication_ReviewNote(
        content="lZm($", publication_ReviewNote43=None, publication_ReviewNote=var_2
    )
    assert isinstance(var_3, python_code_.publication_ReviewNote)


def test_44():
    var_0 = 2893
    var_2 = python_code_.publication_PublicationPhase(
        name="_publication_Sequence__publication_Sequence15_publication_PublicationPhase__phaseParticipationResearcher",
        minTime=var_0,
        maxTime=var_0,
        publication_PublicationPhase13=None,
        publication_PublicationPhase4={"VX`Mf;g%V&N7_esK==("},
        publication_PublicationPhase7={var_0},
    )
    assert isinstance(var_2, python_code_.publication_PublicationPhase)
    var_3 = {var_2, var_2, var_2, var_2, var_2}
    var_4 = python_code_.publication_PublicationProcess(
        minTime=var_0,
        maxTime=b"\xb7\xd7\xe42V\x84\xfd@\x84N\xd3",
        publication_PublicationProcess=var_3,
        publication_PublicationProcess35=1797,
    )
    assert isinstance(var_4, python_code_.publication_PublicationProcess)
    var_7 = python_code_.Labelled
    var_8 = python_code_.publication_Labelled(lname=var_7)
    assert isinstance(var_8, python_code_.publication_Labelled)
    var_10 = python_code_.publication_Named(name=var_3)
    assert isinstance(var_10, python_code_.publication_Named)
    var_12 = "{xLu}N$t#^X>;d"
    var_13 = python_code_.publication_ReviewNote(
        content=var_12, publication_ReviewNote=var_7
    )
    assert isinstance(var_13, python_code_.publication_ReviewNote)


def test_45():
    var_2 = python_code_.publication_Paragraph(
        content="]82JB\x0b4Lb", publication_Paragraph31=set()
    )
    assert isinstance(var_2, python_code_.publication_Paragraph)


def test_46():
    var_9 = python_code_.publication_Paragraph(
        content=b"\xf4\x14<\xd6\x12\xb2\x14z/\xff\tB\xe2\xdc\tV#\xc9",
        publication_Paragraph31=[""],
    )
    assert isinstance(var_9, python_code_.publication_Paragraph)
    var_11 = "n\n|$M_^Epa"
    var_12 = python_code_.publication_ReviewNote(
        content=var_11, publication_ReviewNote=var_9
    )
    assert isinstance(var_12, python_code_.publication_ReviewNote)
    var_13 = {var_12, var_12, var_12, var_12, var_12}
    python_code_.publication_Paragraph(content=var_11, publication_Paragraph31=var_13)
    var_15 = python_code_.publication_Counted(id=b"\x11\xd8\x04\x13\xf0")
    assert isinstance(var_15, python_code_.publication_Counted)


def test_47():
    var_0 = python_code_.publication_Review()
    var_2 = "publication_PublicationSystem,publication_PublicationPhase16,publication_Sequence15,publication_Sequence12"
    var_3 = python_code_.publication_ReviewNote(content=var_2)
    assert isinstance(var_3, python_code_.publication_ReviewNote)
    var_5 = python_code_.publication_PublicationProcess
    var_6 = -2415.3
    var_8 = {var_0}
    var_13 = python_code_.Named()
    var_15 = -88
    var_16 = python_code_.publication_PublicationPhase(
        name=var_2, minTime=var_15, maxTime=var_5, publication_PublicationPhase7=var_8
    )
    assert isinstance(var_16, python_code_.publication_PublicationPhase)
    var_17 = python_code_.publication_Researcher(
        name=var_5,
        forName=var_6,
        position=var_6,
        Researcher=var_16,
        Researcher29=var_13,
    )
    assert isinstance(var_17, python_code_.publication_Researcher)
    var_21 = -443
    var_22 = ":"
    var_23 = python_code_.publication_PlaceHolderRule()
    var_24 = python_code_.publication_Rule(
        text=var_8,
        key=var_22,
        publication_Rule=var_5,
        publication_Rule18=var_23,
        publication_Rule8=var_21,
    )
    assert isinstance(var_24, python_code_.publication_Rule)
    var_25 = set()
    var_26 = python_code_.publication_PublicationProcess(
        minTime=var_21, maxTime=var_21, publication_PublicationProcess2=var_25
    )
    assert isinstance(var_26, python_code_.publication_PublicationProcess)
    var_42 = python_code_.publication_Progress(
        percent=var_15, time=var_15, progress=var_15, Progress=None
    )
    assert isinstance(var_42, python_code_.publication_Progress)


def test_48():
    var_18 = 1
    var_19 = python_code_.publication_PlaceHolderRn
    var_20 = -1079
    var_21 = python_code_.publication_PublicationProcess(minTime=set(), maxTime=var_20)
    assert isinstance(var_21, python_code_.publication_PublicationProcess)
    var_22 = ""
    var_23 = -2976
    var_24 = set()
    var_25 = python_code_.publication_PublicationPhase(
        name=var_22,
        minTime=var_23,
        maxTime=var_20,
        publication_PublicationPhase13=var_20,
        PublicationPhase=(),
        phaseParticipation=var_24,
        publication_PublicationPhase7=b"\xb3\xa0\xbb\xe1\x87\x06)L\xdc)",
        publication_PublicationPhase10=var_18,
    )
    assert isinstance(var_25, python_code_.publication_PublicationPhase)
    var_26 = python_code_.publication_Rule(
        text=var_19, key=var_19, publication_Rule=var_21, publication_Rule8=var_25
    )
    assert isinstance(var_26, python_code_.publication_Rule)
    var_28 = 3
    var_29 = -97
    var_30 = python_code_.publication_Progress(
        percent=var_28, time=var_29, progress=b"\xb4["
    )
    assert isinstance(var_30, python_code_.publication_Progress)


def test_49():
    var_9 = python_code_.publication_Paragraph(
        content="8uA{P|U",
        publication_Paragraph31=set(),
        publication_Paragraph40=None,
        publication_Paragraph=None,
    )
    assert isinstance(var_9, python_code_.publication_Paragraph)
    var_11 = "| oZC0A^)AH!/pZF"
    var_12 = python_code_.publication_ReviewNote(
        content=var_11, publication_ReviewNote=var_9
    )
    assert isinstance(var_12, python_code_.publication_ReviewNote)
    var_13 = {var_12, var_12, var_12, var_12}
    python_code_.publication_Paragraph(content=var_11, publication_Paragraph31=var_13)
    var_15 = python_code_.publication_Counted(id=b"\x11\xd8\x04\x13\xf0")
    assert isinstance(var_15, python_code_.publication_Counted)


def test_50():
    var_10 = "eWv\n70s:bGx<h"
    var_11 = python_code_.publication_Researcher(
        name=var_10,
        forName=var_10,
        position="5f%a j?-z",
        publication_Researcher={-838, var_10, var_10},
        authors=set(),
    )
    assert isinstance(var_11, python_code_.publication_Researcher)
    var_12 = -3420
    var_13 = {var_11, var_11}
    var_14 = python_code_.publication_PublicationPhase(
        name=var_11,
        minTime=complex(-2101.0, 2865.0),
        maxTime=var_10,
        publication_PublicationPhase=var_12,
        PublicationPhase='wqUGH;XZo/d ,S"',
        publication_PublicationPhase4="publication_Review publication_Write",
        phaseParticipation=var_13,
    )
    assert isinstance(var_14, python_code_.publication_PublicationPhase)
    var_15 = {var_14}
    var_16 = python_code_.publication_Counted
    var_17 = python_code_.publication_PublicationProcess(
        minTime=var_11,
        maxTime=var_12,
        publication_PublicationProcess=var_15,
        publication_PublicationProcess50=var_16,
    )
    assert isinstance(var_17, python_code_.publication_PublicationProcess)
    var_19 = python_code_.publication_PublicationPhase(
        name=var_10,
        minTime=var_12,
        maxTime='o"#',
        publication_PublicationPhase=var_17,
        publication_PublicationPhase13={
            "1@TIX&)z'=uv;5 SHk": "publication_Write-_publication_PublicationPhase__phaseParticipation-_publication_ReviewNote__publication_ReviewNote33-publication_Rule"
        },
    )
    assert isinstance(var_19, python_code_.publication_PublicationPhase)


def test_51():
    var_11 = python_code_.publication_PublicationProcess(minTime=3586, maxTime=-899)
    assert isinstance(var_11, python_code_.publication_PublicationProcess)
    var_13 = python_code_.publication_Paper
    var_14 = "phaseParticipation-publication_Write-publication_Rule"
    var_15 = -661
    var_16 = "Q$O"
    var_17 = python_code_.publication_Rule(
        text=var_16,
        key=complex(-551.1, -1569.5),
        publication_Rule18=-910,
        publication_Rule8=var_11,
    )
    assert isinstance(var_17, python_code_.publication_Rule)
    var_18 = {var_17, var_17, var_17, var_17, var_17}
    var_19 = python_code_.publication_PublicationPhase(
        name=var_14,
        minTime=var_15,
        maxTime=var_13,
        publication_PublicationPhase4=None,
        publication_PublicationPhase7=var_18,
        publication_PublicationPhase10=var_14,
    )
    assert isinstance(var_19, python_code_.publication_PublicationPhase)


@pytest.mark.xfail(strict=True)
def test_52():
    var_22 = python_code_.publication_Researcher
    var_23 = 4035
    var_24 = -1
    var_25 = -1873
    var_26 = python_code_.publication_PublicationProcess(
        minTime=var_25, maxTime=var_24, publication_PublicationProcess35=-5027.9
    )
    assert isinstance(var_26, python_code_.publication_PublicationProcess)
    var_27 = python_code_.publication_Sequence(
        sequenceType=var_24, publication_Sequence15=['+py"<>*e>92YYUL?', 1]
    )
    assert isinstance(var_27, python_code_.publication_Sequence)
    var_28 = set()
    var_29 = python_code_.publication_PlaceHolderPP()
    python_code_.publication_PublicationPhase(
        name=var_22,
        minTime=var_23,
        maxTime=var_24,
        publication_PublicationPhase=var_26,
        publication_PublicationPhase16=var_27,
        publication_PublicationPhase4=var_28,
        publication_PublicationPhase10=var_29,
    )


def test_53():
    var_0 = python_code_.publication_PlaceHolder()
    var_1 = python_code_.publication_PublicationStructure()
    var_3 = python_code_.Counted()
    var_4 = hash
    var_5 = -1271
    var_6 = python_code_.publication_PublicationPhase(
        name=var_3,
        minTime=var_4,
        maxTime=var_5,
        publication_PublicationPhase4="%q7JX#oPe'@|&\t",
    )
    assert isinstance(var_6, python_code_.publication_PublicationPhase)
    var_7 = python_code_.publication_Rule(
        text=var_3, key=var_0, publication_Rule8=var_6
    )
    assert isinstance(var_7, python_code_.publication_Rule)
    var_8 = lambda *args, **kwargs: False
    var_9 = python_code_.publication_PublicationProcess(minTime=var_8, maxTime=var_3)
    assert isinstance(var_9, python_code_.publication_PublicationProcess)
    var_14 = python_code_.publication_Paper()
    var_17 = python_code_.publication_Sequence(
        sequenceType=b"\xd4\xa4\xa1\x07\x979\xc4",
        publication_Sequence12=b'"|\xf2T\x9a\xe8\xaeO\xc5l',
        publication_Sequence="_publication_Rule__publication_Rule8 PublicationPhase _publication_Sequence__publication_Sequence12 publication_Paragraph31",
    )
    assert isinstance(var_17, python_code_.publication_Sequence)
    var_18 = {var_17}
    var_19 = python_code_.publication_PublicationPhase(
        name=var_1,
        minTime=[-258.04, 1010.44, -1856.41],
        maxTime={
            "publication_Progress _publication_ReviewNote__publication_ReviewNote publication_Sequence _publication_PublicationProcess__publication_PublicationProcess50",
            False,
            2938.39,
        },
        publication_PublicationPhase=var_9,
        publication_PublicationPhase4=var_18,
    )
    assert isinstance(var_19, python_code_.publication_PublicationPhase)
    python_code_.publication_Sequence(sequenceType=var_8)
    var_23 = "(luLZ"
    var_24 = lambda *args, **kwargs: [
        "_publication_Paragraph__publication_Paragraph31:neededPerson:_publication_ReviewNote__publication_ReviewNote33:_publication_PublicationPhase__publication_PublicationPhase7",
        "_publication_Rule__publication_Rule8",
    ]
    var_25 = python_code_.publication_ReviewNote(
        content=var_23, publication_ReviewNote43=var_24
    )
    assert isinstance(var_25, python_code_.publication_ReviewNote)
    var_27 = {var_7, var_7, var_7, var_7}
    var_31 = python_code_.publication_Counted(id="startToFinish-startToStart")
    assert isinstance(var_31, python_code_.publication_Counted)
    var_33 = python_code_.publication_Named(name=[])
    assert isinstance(var_33, python_code_.publication_Named)
    var_36 = python_code_.publication_Paragraph(
        content=var_23, publication_Paragraph31=var_27, publication_Paragraph=var_14
    )
    assert isinstance(var_36, python_code_.publication_Paragraph)
    python_code_.publication_PublicationPhase(
        name=var_23, minTime=2370.53, maxTime=var_23, phaseParticipation=var_23
    )
