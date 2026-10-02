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
    date,
    datetime,
    model_Actor,
    model_BNode,
    model_Book,
    model_BookBNode,
    model_ETypes,
    model_Library,
    model_Location,
    model_MappedLibrary,
    model_Movie,
    model_Person,
    model_PersonBNode,
    model_PrimaryObject,
    model_TargetObject,
    time,
)


def test_0():
    var_0 = -1335
    var_10 = lambda *args, **kwargs: False
    var_11 = python_code_.model_Actor(id=var_10, name=(), Actor=var_0)
    assert isinstance(var_11, python_code_.model_Actor)


def test_1():
    var_0 = -1314
    var_11 = python_code_.model_Actor(id=var_0, name="model_PrimaryObject33")
    assert isinstance(var_11, python_code_.model_Actor)


def test_2():
    var_2 = python_code_.model_Movie(id=1159, title="R%Ql8+X0Z-wG", actorOf=set())
    assert isinstance(var_2, python_code_.model_Movie)


def test_3():
    var_2 = python_code_.model_Movie(id=1644, title="Zoq\nJL3T")
    assert isinstance(var_2, python_code_.model_Movie)


def test_4():
    var_2 = python_code_.model_Movie(id=1159, title="R%Ql8+X0Z-wG", actorOf=set())
    assert isinstance(var_2, python_code_.model_Movie)
    var_6 = python_code_.model_Actor(id=2323, name="", actors={var_2, False, var_2})
    assert isinstance(var_6, python_code_.model_Actor)


@pytest.mark.xfail(strict=True)
def test_5():
    var_0 = python_code_.model_Library()
    var_1 = python_code_.model_Location(
        address=complex(-2495.9053049, -1947.178), id=2129.19, model_Location=var_0
    )
    var_28 = "_model_TargetObject__model_TargetObject34"
    var_29 = "books"
    var_30 = "model_MappedLibrary,_model_Location__model_Location18"
    var_31 = python_code_.model_TargetObject(
        id={"P*4e"},
        singleAttribute=var_29,
        arrayAttribute=var_30,
        model_TargetObject31=var_30,
    )
    assert isinstance(var_31, python_code_.model_TargetObject)
    var_32 = {var_31, var_31, var_31}
    python_code_.model_PrimaryObject(
        id=var_1,
        name=var_30,
        unsettableAttribute=var_28,
        unsettableAttributeWithDefault={
            "h^7.RJQ$hI#Z8": "model_TargetObject40_model_Book__books",
            "Q2~s<gU\txzeO]&/#*\x0b": -654.06,
        },
        featureMapReferenceCollection=None,
        featureMapAttributeType1=[],
        featureMapAttributeType2=True,
        featureMapAttributeCollection=var_0,
        model_PrimaryObject33=var_31,
        model_PrimaryObject42=var_32,
    )


def test_6():
    var_7 = -2292
    var_19 = python_code_.model_BookBNode
    python_code_.model_TargetObject(
        id=var_7,
        singleAttribute=var_19,
        arrayAttribute=b"\x95\xa63",
        model_TargetObject=var_19,
    )


def test_7():
    var_0 = 364
    var_1 = "]FY'ox>j"
    var_2 = "' D\\)B\x0c8"
    var_3 = lambda *args, **kwargs: -290
    var_4 = "_model_TargetObject__model_TargetObject46"
    var_5 = python_code_.model_PrimaryObject(
        id=var_0,
        name=var_1,
        unsettableAttribute=var_2,
        unsettableAttributeWithDefault=var_3,
        featureMapReferenceCollection=complex(-44.8, -1331.10226),
        featureMapAttributeType1=var_2,
        featureMapAttributeType2=var_4,
        featureMapAttributeCollection=var_4,
    )
    assert isinstance(var_5, python_code_.model_PrimaryObject)
    var_6 = "_model_PrimLaryObject__model_PrimaryObject30"
    var_7 = python_code_.model_TargetObject(
        id=var_1,
        singleAttribute=var_6,
        arrayAttribute=var_2,
        model_TargetObject34=287.97,
    )
    assert isinstance(var_7, python_code_.model_TargetObject)
    var_10 = "=`C\x0baCh="
    var_11 = python_code_.model_Person(name=var_4)
    var_12 = {var_11, var_11, var_11}
    python_code_.model_Book(
        title=b"^{\xc8\xff\xec\x99\x0e\xae\xec\xad",
        tags=var_10,
        data=var_3,
        books=var_12,
    )
    python_code_.model_MappedLibrary(books="j\"*[{b!'4 {0:-")


def test_8():
    var_7 = -2292
    var_8 = python_code_.model_Movie(id=var_7, title=var_7)
    assert isinstance(var_8, python_code_.model_Movie)
    var_16 = 'H\r!,~"QA'
    var_21 = -1
    var_22 = python_code_.model_TargetObject(
        id=var_21,
        singleAttribute=var_21,
        arrayAttribute=var_16,
        model_TargetObject37="_model_PrimaryObject__model_PrimaryObject39",
        model_TargetObject40=[0, -1254, 45],
    )
    assert isinstance(var_22, python_code_.model_TargetObject)


def test_9():
    var_1 = "Yyj5+"
    var_9 = lambda *args, **kwargs: False
    var_12 = "model_Location18"
    var_13 = "9btz\t!\nfMJSY2G"
    var_36 = "6?PF"
    python_code_.model_Location(address=[False, "e$gdC4_8x\x0bB]", False], id=var_36)
    var_18 = "Book model_PrimaryObject36"
    var_20 = ""
    var_21 = python_code_.model_PrimaryObject(
        id=b"\xa3\xf0",
        name=var_9,
        unsettableAttribute=complex(2414.86, -1785.93459),
        unsettableAttributeWithDefault=var_1,
        featureMapReferenceCollection=var_20,
        featureMapAttributeType1=var_18,
        featureMapAttributeType2=var_13,
        featureMapAttributeCollection=var_9,
        model_PrimaryObject39=set(),
        model_PrimaryObject42=b"\x83>w0\x19\r\xbf\xd0\xb1",
        model_PrimaryObject=var_20,
    )
    assert isinstance(var_21, python_code_.model_PrimaryObject)
    var_34 = python_code_.model_TargetObject(
        id=var_12,
        singleAttribute=937,
        arrayAttribute=False,
        model_TargetObject49=var_21,
    )
    assert isinstance(var_34, python_code_.model_TargetObject)


def test_10():
    var_0 = float
    python_code_.model_Location(
        address=var_0, id=-186.54, model_Location=var_0, model_Location18=var_0
    )
    var_8 = "P/7`M\t`"
    var_12 = python_code_.model_TargetObject(
        id={"P*4e"},
        singleAttribute=var_8,
        arrayAttribute=var_8,
        model_TargetObject31=var_8,
    )
    assert isinstance(var_12, python_code_.model_TargetObject)
    var_13 = 2170
    var_14 = object
    var_15 = python_code_.model_Actor(id=var_13, name=var_8, Actor=var_14)
    assert isinstance(var_15, python_code_.model_Actor)


@pytest.mark.xfail(strict=True)
def test_11():
    var_0 = -1335
    var_1 = abs
    var_3 = False
    var_21 = "93}\"-U~\n'"
    python_code_.model_PersonBNode(name=var_21, model_PersonBNode5=var_3)
    var_13 = "]USwbY.rlSq5JA"
    var_14 = "model_Book24"
    var_15 = "GT#Z+A?rL\\0W}>"
    var_16 = python_code_.model_TargetObject(
        id=-156.7,
        singleAttribute=var_3,
        arrayAttribute=var_15,
        model_TargetObject31=var_14,
        model_TargetObject28=var_13,
    )
    assert isinstance(var_16, python_code_.model_TargetObject)
    var_17 = {var_16, var_16, var_16, var_16, var_16}
    var_18 = python_code_.model_PrimaryObject(
        id=var_0,
        name=var_13,
        unsettableAttribute=var_14,
        unsettableAttributeWithDefault=var_15,
        featureMapReferenceCollection=(),
        featureMapAttributeType1=var_13,
        featureMapAttributeType2=var_13,
        featureMapAttributeCollection=2751.22,
        model_PrimaryObject33=None,
        model_PrimaryObject42={},
        model_PrimaryObject27=var_1,
        model_PrimaryObject45=var_17,
    )
    assert isinstance(var_18, python_code_.model_PrimaryObject)
    var_19 = python_code_.model_TargetObject(
        id=var_0,
        singleAttribute=b"\x1c\xa69\x0b",
        arrayAttribute=var_14,
        model_TargetObject31={"toP^nfuo\x0b": -3482.23, "1?n[a": 855},
        model_TargetObject37=var_18,
        model_TargetObject43=var_18,
    )
    assert isinstance(var_19, python_code_.model_TargetObject)
    python_code_.model_PrimaryObject(
        id=var_1,
        name=var_13,
        unsettableAttribute=var_1,
        unsettableAttributeWithDefault=var_3,
        featureMapReferenceCollection=var_13,
        featureMapAttributeType1=var_1,
        featureMapAttributeType2=var_1,
        featureMapAttributeCollection=complex(2212.93066, -4106.6161),
        model_PrimaryObject30=var_13,
        model_PrimaryObject39=var_3,
        model_PrimaryObject=var_16,
    )


@pytest.mark.xfail(strict=True)
def test_12():
    var_0 = "R\x0cZ.oj3)>BK"
    var_1 = "G$9C\no_E91Zg\tJi"
    var_5 = "xcdn ,l}@"
    var_6 = 2547
    var_7 = ","
    var_8 = "!xpD=\x0bvD45Iu\nA5L)"
    var_9 = lambda *args, **kwargs: 11
    var_10 = "_model_Book__books_model_PrimaryObject__model_PrimaryObject30"
    var_11 = "_model_TargetObject__model_TargetObject37:model_PrimaryObject36"
    var_12 = python_code_.model_TargetObject(
        id=var_6,
        singleAttribute=var_9,
        arrayAttribute=var_0,
        model_TargetObject37=var_6,
        model_TargetObject=var_9,
        model_TargetObject28=complex(38.3644, -2503.9751304),
    )
    var_13 = {var_12, var_12, var_12}
    python_code_.model_PrimaryObject(
        id=var_1,
        name=var_6,
        unsettableAttribute=var_7,
        unsettableAttributeWithDefault=var_5,
        featureMapReferenceCollection=var_10,
        featureMapAttributeType1=var_7,
        featureMapAttributeType2="q^9Nv8_RM",
        featureMapAttributeCollection=var_11,
        model_PrimaryObject36=var_8,
        model_PrimaryObject42=var_13,
        model_PrimaryObject=None,
        model_PrimaryObject27=var_12,
    )


@pytest.mark.xfail(strict=True)
def test_13():
    var_1 = abs
    var_3 = False
    var_21 = "93}\"-U~\n'"
    python_code_.model_PersonBNode(name=var_21, model_PersonBNode5=var_3)
    var_13 = "]USwbY.rlSq5JA"
    var_14 = "model_Book24"
    var_15 = "GT#Z+A?rL\\0W}>"
    var_16 = python_code_.model_TargetObject(
        id=-156.7,
        singleAttribute=var_3,
        arrayAttribute=var_15,
        model_TargetObject31=var_14,
        model_TargetObject28=var_13,
    )
    assert isinstance(var_16, python_code_.model_TargetObject)
    python_code_.model_PrimaryObject(
        id=var_1,
        name=var_13,
        unsettableAttribute=var_1,
        unsettableAttributeWithDefault=var_3,
        featureMapReferenceCollection=var_13,
        featureMapAttributeType1=var_1,
        featureMapAttributeType2=var_1,
        featureMapAttributeCollection=complex(2212.93066, -4106.6161),
        model_PrimaryObject30=var_13,
        model_PrimaryObject39=var_3,
        model_PrimaryObject=var_16,
    )


def test_14():
    var_19 = python_code_.model_PrimaryObject
    var_20 = 'Y"JS\n'
    var_21 = python_code_.model_PrimaryObject(
        id=-1775,
        name=var_19,
        unsettableAttribute=var_19,
        unsettableAttributeWithDefault=None,
        featureMapReferenceCollection=var_19,
        featureMapAttributeType1=91.34,
        featureMapAttributeType2=complex(524.7, -397.9138),
        featureMapAttributeCollection=var_20,
    )
    assert isinstance(var_21, python_code_.model_PrimaryObject)


def test_15():
    var_0 = float
    var_1 = python_code_.model_Location(
        address="qy9", id="1k&e3kuK;", model_Location15=None
    )
    var_6 = 2
    var_13 = "bqG"
    var_14 = python_code_.model_PrimaryObject(
        id=var_6,
        name="I`~^5qiYs\x0c?)]pao",
        unsettableAttribute=var_13,
        unsettableAttributeWithDefault="model_Book16 _model_Book__model_Book16",
        featureMapReferenceCollection=var_13,
        featureMapAttributeType1="-4J'jix }cpM",
        featureMapAttributeType2="iF6}\x0c",
        featureMapAttributeCollection=var_13,
        model_PrimaryObject36={var_6},
        model_PrimaryObject27=var_1,
    )
    assert isinstance(var_14, python_code_.model_PrimaryObject)
    var_15 = python_code_.model_Movie(id="\tt+V", title=var_0)
    assert isinstance(var_15, python_code_.model_Movie)
    var_18 = python_code_.model_BNode(id=var_0)
    python_code_.model_BNode(id=var_15, model_BNode=b"\xa7e\x83", model_BNode6=var_13)
    var_22 = "_model_Location__model_Location18"
    python_code_.model_PersonBNode(name=var_22)
    var_24 = python_code_.model_Actor(id=var_14, name=var_0)
    assert isinstance(var_24, python_code_.model_Actor)
    python_code_.model_MappedLibrary(books=var_22, model_MappedLibrary=var_18)


def test_16():
    var_0 = float
    python_code_.model_Location(address="qy9", id="1k&e3kuK;", model_Location15=None)
    var_6 = 2
    var_13 = "\tE 'j7"
    var_14 = python_code_.model_PrimaryObject(
        id=var_6,
        name=1557.05,
        unsettableAttribute=var_13,
        unsettableAttributeWithDefault=var_13,
        featureMapReferenceCollection=var_13,
        featureMapAttributeType1=var_13,
        featureMapAttributeType2=complex(-1521.0999, 3801.7434),
        featureMapAttributeCollection=[
            True,
            "_model_MappedLibrary__model_MappedLibrary23model_TargetObject31",
            -113,
        ],
        model_PrimaryObject33=var_13,
    )
    assert isinstance(var_14, python_code_.model_PrimaryObject)
    var_15 = python_code_.model_Movie(id="\tt+V", title=var_0)
    assert isinstance(var_15, python_code_.model_Movie)
    var_18 = python_code_.model_BNode(id=var_0)
    python_code_.model_BNode(id=var_15, model_BNode=b"\xa7e\x83", model_BNode6=var_13)
    var_22 = "_model_Location__model_Location18"
    python_code_.model_PersonBNode(name=var_22)
    var_24 = python_code_.model_Actor(id=var_14, name=var_0)
    assert isinstance(var_24, python_code_.model_Actor)
    python_code_.model_MappedLibrary(books=var_22, model_MappedLibrary=var_18)
    var_26 = "_model_BookBNode__model_BookBNode.model_Movie.model_PrimaryObject30"
    var_27 = "model_TargetObject49model_PrimaryObject27model_MappedLibrary20_model_TargetObject__model_TargetObject34"
    var_28 = 'qK\n;"s\n6Vt'
    var_29 = python_code_.model_Person(name=var_28)
    var_30 = {var_29, var_29, var_29, var_29}
    python_code_.model_Book(title=var_26, tags=var_0, data=var_27, books=var_30)


@pytest.mark.xfail(strict=True)
def test_17():
    var_2 = python_code_.model_Library()
    var_9 = -530
    var_10 = lambda *args, **kwargs: 1268
    var_11 = ">\tl/lX 'c>bL*{nTddO"
    var_12 = 363
    var_13 = python_code_.model_PrimaryObject(
        id=var_10,
        name=var_11,
        unsettableAttribute=var_11,
        unsettableAttributeWithDefault=var_2,
        featureMapReferenceCollection=False,
        featureMapAttributeType1=var_9,
        featureMapAttributeType2=var_11,
        featureMapAttributeCollection=[],
        model_PrimaryObject27=var_11,
    )
    assert isinstance(var_13, python_code_.model_PrimaryObject)
    python_code_.model_TargetObject(
        id=var_12,
        singleAttribute=var_9,
        arrayAttribute=var_11,
        model_TargetObject31=var_13,
        model_TargetObject40=var_13,
        model_TargetObject=var_13,
        model_TargetObject46=True,
    )


def test_18():
    python_code_.model_MappedLibrary(
        books="_model_PrimaryObject__model_PrimaryObject33", model_MappedLibrary20=set()
    )


def test_19():
    var_8 = python_code_.model_Movie(
        id=-823,
        title="_model_TargetObject__model_TargetObject:_model_Movie__actorOf:_model_PrimaryObject__model_PrimaryObject45:_model_Book__model_Book",
    )
    assert isinstance(var_8, python_code_.model_Movie)
    python_code_.model_MappedLibrary(books="f<mGrCGS<ujLE", model_MappedLibrary=var_8)


def test_20():
    var_8 = python_code_.model_Movie(
        id=-823,
        title="_model_TargetObject__model_TargetObject:_model_Movie__actorOf:_model_PrimaryObject__model_PrimaryObject45:_model_Book__model_Book",
    )
    assert isinstance(var_8, python_code_.model_Movie)
    python_code_.model_MappedLibrary(books="(/2Y)", model_MappedLibrary23=set())


@pytest.mark.xfail(strict=True)
def test_21():
    var_0 = python_code_.model_Library()
    var_1 = python_code_.model_Location(
        address=complex(-2495.9053049, -1947.178), id=2129.19, model_Location=var_0
    )
    var_22 = abs
    var_31 = "~bMM"
    var_33 = "\x0b<T$k"
    var_35 = (
        "_model_PrimaryObject__model_PrimaryObject42:_model_BookBNode__model_BookBNode4"
    )
    python_code_.model_BookBNode(title=var_35, model_BookBNode=var_31)
    python_code_.model_PersonBNode(name=set())
    var_49 = "\r\t@|,K0?\t\x0bdKc"
    python_code_.model_Book(
        title=var_49,
        tags="_model_BookBNode__model_BookBNode4-actorOf-model_MappedLibrary23",
        data=var_31,
        model_Book16=var_1,
        model_Book=var_33,
        model_Book13=var_0,
        model_Book21=var_22,
    )


def test_22():
    var_0 = float
    python_code_.model_Location(
        address=var_0, id=-186.54, model_Location=var_0, model_Location18=var_0
    )


def test_23():
    var_0 = lambda *args, **kwargs: []
    var_1 = python_code_.model_Location(
        address=var_0, id=var_0, model_Location18=2099.62
    )
    var_2 = 0
    var_3 = python_code_.model_BNode(id=set())
    var_4 = python_code_.model_BNode(id=var_2, model_BNode=var_3)
    assert isinstance(var_4, python_code_.model_BNode)
    var_5 = {var_3, var_3, var_3, var_4, var_4}
    var_6 = python_code_.model_BNode(id=var_2, model_BNode6=var_5)
    var_7 = "=@i&e"
    var_8 = python_code_.model_BookBNode(title=var_7, model_BookBNode=var_0)
    var_9 = python_code_.model_PersonBNode(
        name=var_7, model_PersonBNode=var_7, model_PersonBNode5=var_8
    )
    assert isinstance(var_9, python_code_.model_PersonBNode)
    var_10 = '_C6vF^2i"]h\r\tQ%F!\t\t'
    python_code_.model_Location(address=var_7, id=var_10, model_Location=var_6)
    var_12 = python_code_.model_Location(
        address=var_1, id=var_9, model_Location15=var_0
    )
    var_13 = -3092
    var_14 = python_code_.model_PrimaryObject(
        id=var_13,
        name=var_0,
        unsettableAttribute=var_12,
        unsettableAttributeWithDefault=var_7,
        featureMapReferenceCollection=var_13,
        featureMapAttributeType1=var_3,
        featureMapAttributeType2=var_0,
        featureMapAttributeCollection=var_10,
        model_PrimaryObject30=var_5,
    )
    assert isinstance(var_14, python_code_.model_PrimaryObject)
    var_15 = python_code_.model_PersonBNode(
        name=complex(-1093.489, 1119.32072), model_PersonBNode5=var_13
    )
    var_16 = python_code_.model_TargetObject(
        id=complex(33.3745055, 334.2116),
        singleAttribute=var_7,
        arrayAttribute=var_7,
        model_TargetObject31=complex(-93.22, 2236.01),
    )
    assert isinstance(var_16, python_code_.model_TargetObject)
    var_17 = -1894.87
    var_18 = "model_PersonBNode.model_Library12.model_MappedLibrary20.Book"
    python_code_.model_ETypes(
        eBigDecimal=(3164.11, 63.67, 1973.16),
        eBigInteger=var_8,
        eBoolean=True,
        eByte=var_0,
        eByteArray=var_10,
        eChar=var_16,
        eDate=var_0,
        eDouble="_model_Book__model_Book16,model_Actor,model_Book24",
        eFloat=var_17,
        eInt=None,
        eLong=None,
        eShort=var_18,
        eString=var_0,
        uris=var_15,
    )
    var_21 = python_code_.model_Movie(id=var_12, title=var_7, Movie=var_3)
    assert isinstance(var_21, python_code_.model_Movie)
    python_code_.model_TargetObject(
        id=-1897,
        singleAttribute=var_0,
        arrayAttribute={
            "^\x0bDWq~Q, ": False,
            "authors:model_MappedLibrary:_model_PersonBNode__model_PersonBNode5": False,
        },
        model_TargetObject49=var_0,
    )


def test_24():
    python_code_.model_Location(
        address="W&yv<!jGYr#peY{Ia:", id="\x0btiQq\t:&4I(D2m5%X"
    )
    var_6 = "model_MappedLibrary,_model_Location__model_Location18"
    var_23 = python_code_.model_Movie(id={}, title=var_6)
    assert isinstance(var_23, python_code_.model_Movie)
    var_25 = "F\x0bfv\x0c[,6[:+xhK,y"
    var_27 = python_code_.model_Book
    var_28 = "7^'P?)?U6zlGH Ah"
    var_29 = python_code_.model_Person(name=var_25, Person=var_23)
    python_code_.model_Book(
        title=-897.78, tags=var_27, data=var_28, Book=var_29, model_Book=var_27
    )


def test_25():
    var_0 = -1335
    var_1 = abs
    python_code_.model_BNode(id=var_0)
    python_code_.model_PersonBNode(name=var_1)


def test_26():
    var_0 = python_code_.model_Library()
    var_21 = hash
    var_22 = "0Jfc!\x0b_m{F#"
    var_23 = python_code_.model_BookBNode(title=var_22)
    var_24 = python_code_.model_PersonBNode(name=var_21, model_PersonBNode5=var_23)
    assert isinstance(var_24, python_code_.model_PersonBNode)
    var_25 = python_code_.model_BNode(id=var_0)
    var_26 = python_code_.model_BNode(id=var_21, model_BNode=var_25)
    assert isinstance(var_26, python_code_.model_BNode)


def test_27():
    python_code_.model_BookBNode(title=None)


def test_28():
    var_7 = -2292
    var_8 = python_code_.model_Movie(id=var_7, title=var_7)
    assert isinstance(var_8, python_code_.model_Movie)
    var_9 = "t8EGaf)Xvd:"
    var_10 = python_code_.model_BookBNode(title=var_9)
    var_11 = {var_10, var_10}
    var_12 = python_code_.model_PersonBNode(name=var_7, model_PersonBNode=var_11)
    assert isinstance(var_12, python_code_.model_PersonBNode)
    var_13 = {var_12, var_12}
    var_14 = python_code_.model_BookBNode(
        title=var_9,
        model_BookBNode=b"\xae-\xc7\xbe8bd\x14\x05==\xbf\xe2\x8d",
        model_BookBNode4=var_13,
    )
    assert isinstance(var_14, python_code_.model_BookBNode)


def test_29():
    var_22 = set()
    python_code_.model_PersonBNode(name=True, model_PersonBNode=var_22)


def test_30():
    var_2 = python_code_.model_Movie(id=139, title="a(mRWz5K;\x0c")
    assert isinstance(var_2, python_code_.model_Movie)
    var_7 = lambda *args, **kwargs: False
    python_code_.model_Book(
        title=var_7,
        tags=complex(844.1679, 1582.3665),
        data="k\x0c'LE\x0b3W5f9U$^x<#5",
        Book=var_7,
    )


@pytest.mark.xfail(strict=True)
def test_31():
    var_0 = float
    var_9 = "swX\tItNzr*pXRz\nO"
    python_code_.model_Book(title=var_0, tags=var_9, data=True, model_Book13=var_0)
    var_11 = -2960
    var_12 = "efh3McP"
    python_code_.model_Movie(id=var_11, title=var_12, actorOf=var_0)


def test_32():
    var_0 = float
    python_code_.model_Location(
        address=var_0, id=-186.54, model_Location=var_0, model_Location18=var_0
    )
    var_8 = "P/7`M\t`"
    var_18 = python_code_.model_TargetObject(
        id={"P*4e"},
        singleAttribute=var_8,
        arrayAttribute=var_8,
        model_TargetObject31=var_8,
    )
    assert isinstance(var_18, python_code_.model_TargetObject)
    var_20 = object
    var_21 = python_code_.model_Actor(id=3, name='FEC"6qhn=Tm`CQ$')
    assert isinstance(var_21, python_code_.model_Actor)
    python_code_.model_Book(
        title=[],
        tags=2812.03,
        data=var_0,
        model_Book16=var_20,
        Book=var_20,
        model_Book=None,
    )
    var_23 = "9"
    var_24 = {var_21, var_21, var_21}
    var_25 = python_code_.model_Movie(id=var_0, title=var_23, actorOf=var_24)
    assert isinstance(var_25, python_code_.model_Movie)
    var_26 = {var_25, var_25, var_25, var_25, var_25}
    var_27 = python_code_.model_Actor(id=None, name=var_23, actors=var_26)
    assert isinstance(var_27, python_code_.model_Actor)


@pytest.mark.xfail(strict=True)
def test_33():
    var_0 = 364
    var_1 = "]FY'ox>j"
    var_2 = "' D\\)B\x0c8"
    var_3 = lambda *args, **kwargs: -290
    var_4 = "_model_TargetObject__model_TargetObject46"
    var_5 = python_code_.model_PrimaryObject(
        id=var_0,
        name=var_1,
        unsettableAttribute=var_2,
        unsettableAttributeWithDefault=var_3,
        featureMapReferenceCollection=complex(-44.8, -1331.10226),
        featureMapAttributeType1=var_2,
        featureMapAttributeType2=var_4,
        featureMapAttributeCollection=var_4,
    )
    assert isinstance(var_5, python_code_.model_PrimaryObject)
    var_6 = "_model_PrimaryObject__model_PrimaryObject30"
    var_7 = python_code_.model_TargetObject(
        id=var_1,
        singleAttribute=var_6,
        arrayAttribute=var_2,
        model_TargetObject34=287.97,
    )
    assert isinstance(var_7, python_code_.model_TargetObject)
    var_10 = "=`C\x0baCh="
    var_11 = python_code_.model_Person(name=var_4)
    var_12 = {var_11, var_11, var_11}
    var_13 = python_code_.model_Book(
        title=b"^{\xc8\xff\xec\x99\x0e\xae\xec\xad",
        tags=var_10,
        data=var_3,
        books=var_12,
    )
    var_14 = {var_13, var_13, var_13, var_13}
    python_code_.model_MappedLibrary(
        books=var_0, model_MappedLibrary20=var_14, model_MappedLibrary23=False
    )


@pytest.mark.xfail(strict=True)
def test_34():
    python_code_.model_BNode(id="_model_PersonBNode__model_PersonBNode5")
    var_1 = "_model_Book__model_Book16"
    python_code_.model_Person(name=var_1)
    var_3 = python_code_.model_Actor
    var_4 = python_code_.model_Book(
        title=var_1,
        tags=var_1,
        data=var_3,
        Book=var_1,
        model_Book13=(),
        model_Book21=588,
        model_Book24=var_3,
    )
    python_code_.model_Location(address=None, id=var_3, model_Location15=var_4)


def test_35():
    var_5 = "~2s#Gp-og;BcF{ct"
    python_code_.model_BookBNode(title="AWS>o\rC;*Q", model_BookBNode=None)
    python_code_.model_Person(name=var_5)


def test_36():
    python_code_.model_Library()


def test_37():
    var_15 = "model_TargetObject46"
    var_16 = 'H\r!,~"QA'
    var_17 = lambda *args, **kwargs: True
    var_19 = "model_Library12"
    var_20 = "t=Z3y\r("
    var_25 = "iK0\ra$Iv/0|\\=+Y"
    var_26 = "model_PrimaryObject33"
    var_27 = -1423.71
    var_28 = "?t2u#0Tgjb=Xc1Ns(?"
    var_29 = "_model_Location__model_Location18_model_TargetObject__model_TargetObject28_model_PrimaryObject__model_PrimaryObject42model_Book24"
    python_code_.model_ETypes(
        eBigDecimal=var_25,
        eBigInteger=var_20,
        eBoolean=var_17,
        eByte=var_19,
        eByteArray=var_26,
        eChar=var_25,
        eDate=var_17,
        eDouble=-628,
        eFloat=var_27,
        eInt=var_16,
        eLong=var_28,
        eShort=var_29,
        eString={},
        uris=var_15,
    )
    var_21 = python_code_.model_BookBNode(title=var_16)
    var_22 = python_code_.model_PersonBNode(name=var_20, model_PersonBNode5=var_21)
    assert isinstance(var_22, python_code_.model_PersonBNode)
    var_23 = {var_22}
    python_code_.model_BookBNode(title=var_19, model_BookBNode4=var_23)


def test_38():
    var_0 = -960
    var_1 = set()
    var_2 = python_code_.model_Movie(
        id=var_0, title=var_0, Movie={969, -792.31}, actorOf=var_1
    )
    assert isinstance(var_2, python_code_.model_Movie)
    var_3 = lambda *args, **kwargs: False
    var_4 = python_code_.model_Actor(id=var_3, name=(), Actor=var_0)
    assert isinstance(var_4, python_code_.model_Actor)


@pytest.mark.xfail(strict=True)
def test_39():
    var_0 = python_code_.model_Library()
    python_code_.model_Location(
        address=complex(-2495.9053049, -1947.178), id=2129.19, model_Location=var_0
    )
    var_22 = abs
    var_50 = '\r!,~"QA'
    var_51 = lambda *args, **kwargs: True
    var_52 = "Q1S0"
    var_53 = "h|7p*T#P['s~o"
    var_54 = python_code_.model_BookBNode(title=var_53)
    var_55 = {var_54, var_54, var_54, var_54, var_54}
    var_56 = python_code_.model_PersonBNode(
        name=var_52, model_PersonBNode=var_55, model_PersonBNode5=var_54
    )
    assert isinstance(var_56, python_code_.model_PersonBNode)
    var_57 = "_model_Movie__Movie,model_PrimaryObject36,model_Book24"
    var_58 = "model_Location15"
    var_59 = "o{~4A|ss,uA-b1*}"
    python_code_.model_TargetObject(
        id={"GFG;T9": "]Cc$?(N>~"},
        singleAttribute=var_58,
        arrayAttribute=var_58,
        model_TargetObject37=2885.26,
        model_TargetObject49=var_51,
    )
    var_61 = 757
    var_62 = -169
    var_64 = (
        "model_PersonBNode5,model_Location,model_PrimaryObject39,model_PrimaryObject"
    )
    var_65 = -3225
    var_66 = "model_PersonBNode5 _model_Book__model_Book21"
    var_67 = (
        "_model_Movie__actorOf,_model_PrimaryObject__model_PrimaryObject30,model_Movie"
    )
    var_68 = python_code_.model_PrimaryObject(
        id=False,
        name=var_65,
        unsettableAttribute=var_50,
        unsettableAttributeWithDefault=var_57,
        featureMapReferenceCollection=var_51,
        featureMapAttributeType1=var_56,
        featureMapAttributeType2=var_62,
        featureMapAttributeCollection=var_66,
        model_PrimaryObject48="_model_Person__Person",
    )
    assert isinstance(var_68, python_code_.model_PrimaryObject)
    var_69 = python_code_.model_TargetObject(
        id=var_65,
        singleAttribute=var_66,
        arrayAttribute=var_67,
        model_TargetObject31=var_68,
        model_TargetObject34=var_0,
        model_TargetObject37=var_22,
        model_TargetObject46=var_65,
    )
    assert isinstance(var_69, python_code_.model_TargetObject)
    python_code_.model_PrimaryObject(
        id=var_61,
        name=var_22,
        unsettableAttribute=var_58,
        unsettableAttributeWithDefault=var_59,
        featureMapReferenceCollection=var_64,
        featureMapAttributeType1=1676.63,
        featureMapAttributeType2={},
        featureMapAttributeCollection=var_22,
        model_PrimaryObject36=var_53,
        model_PrimaryObject39=var_69,
        model_PrimaryObject=var_69,
    )


@pytest.mark.xfail(strict=True)
def test_40():
    var_0 = python_code_.model_Actor(
        id="model_BNode6",
        name="model_TargetObject37-books-_model_MappedLibrary__model_MappedLibrary20",
    )
    assert isinstance(var_0, python_code_.model_Actor)
    var_1 = python_code_.model_Library()
    var_3 = "lM"
    var_4 = False
    var_5 = (
        lambda *args, **kwargs: "_model_PrimaryObject__model_PrimaryObject27:_model_TargetObject__model_TargetObject:model_PrimaryObject48"
    )
    var_6 = python_code_.model_ETypes(
        eBigDecimal=var_0,
        eBigInteger=var_3,
        eBoolean=var_4,
        eByte=None,
        eByteArray=var_1,
        eChar=var_3,
        eDate=var_0,
        eDouble=var_4,
        eFloat=var_5,
        eInt=None,
        eLong=var_3,
        eShort=var_1,
        eString=var_3,
        uris=var_3,
    )
    python_code_.model_MappedLibrary(books=var_3)
    python_code_.model_Person(name=var_5)
    var_9 = "xhecqRDw^Qj1"
    python_code_.model_Person(name=var_9, Person=set())
    var_11 = "xn?\x0c"
    var_12 = python_code_.model_Movie(id=var_4, title=var_11)
    assert isinstance(var_12, python_code_.model_Movie)
    var_13 = "model_Book16-_model_Person__authors-_model_Location__model_Location15"
    var_14 = python_code_.model_Book(
        title=var_5,
        tags=var_6,
        data=None,
        model_Book16=(),
        model_Book13=var_5,
        model_Book24=var_5,
    )
    python_code_.model_Location(
        address=var_9,
        id=var_13,
        model_Location15=var_14,
        model_Location=complex(-148.108, 978.161913),
    )


@pytest.mark.xfail(strict=True)
def test_41():
    var_0 = python_code_.model_Library()
    var_9 = "]"
    var_10 = python_code_.model_BNode
    var_11 = set()
    var_12 = 381
    var_13 = "J!c_Kkc T2+j#iHo)pX"
    var_14 = python_code_.model_PrimaryObject(
        id=None,
        name=1528.8,
        unsettableAttribute=-1567,
        unsettableAttributeWithDefault=-437.99,
        featureMapReferenceCollection=var_12,
        featureMapAttributeType1=var_0,
        featureMapAttributeType2=var_13,
        featureMapAttributeCollection=var_9,
        model_PrimaryObject39=var_11,
        model_PrimaryObject=var_13,
    )
    assert isinstance(var_14, python_code_.model_PrimaryObject)
    var_15 = python_code_.model_TargetObject(
        id=var_12,
        singleAttribute={
            "model_BookBNode,model_Book16": "P)YYX//vK7H",
            "?": True,
            "_model_TargetObject__model_TargetObject31": -461.53,
        },
        arrayAttribute="[2]YH][wis6)X5~",
        model_TargetObject43=var_14,
    )
    assert isinstance(var_15, python_code_.model_TargetObject)
    python_code_.model_PrimaryObject(
        id=var_9,
        name=var_9,
        unsettableAttribute=var_9,
        unsettableAttributeWithDefault=var_9,
        featureMapReferenceCollection=var_9,
        featureMapAttributeType1="model_PrimaryObject45 authors model_MappedLibrary _model_PersonBNode__model_PersonBNode",
        featureMapAttributeType2=var_10,
        featureMapAttributeCollection=2,
        model_PrimaryObject30=var_11,
        model_PrimaryObject39=1339,
        model_PrimaryObject=var_15,
        model_PrimaryObject45=var_11,
    )


def test_42():
    var_0 = python_code_.model_Library()
    python_code_.model_Location(
        address=complex(-2495.9053049, -1947.178), id=2129.19, model_Location=var_0
    )
    var_22 = abs
    var_23 = "_model_TargetObject__model_TargetObject31"
    var_24 = python_code_.model_Actor(id=-1289, name=var_22, Actor=False)
    assert isinstance(var_24, python_code_.model_Actor)
    var_25 = python_code_.model_Movie(id=var_22, title=var_23, Movie=var_24)
    assert isinstance(var_25, python_code_.model_Movie)
    var_26 = python_code_.model_Actor(
        id=set(),
        name=b"\xedel6\xab=$U",
        actors=b"9MI\x7fu\x16\x8eG\xac\xa7K\x1d\x13\xda4\xc84",
        Actor=var_25,
    )
    assert isinstance(var_26, python_code_.model_Actor)


@pytest.mark.xfail(strict=True)
def test_43():
    var_0 = "model_Library10"
    var_1 = python_code_.model_BookBNode(title=var_0)
    var_2 = python_code_.model_Movie(id=set(), title=var_1, Movie={})
    assert isinstance(var_2, python_code_.model_Movie)
    var_3 = list
    python_code_.model_BookBNode(title=var_0, model_BookBNode=var_3)
    var_7 = "6-"
    var_10 = "P/7`M\t`"
    var_43 = python_code_.model_TargetObject(
        id={"P*4e"},
        singleAttribute=var_7,
        arrayAttribute=var_10,
        model_TargetObject31=var_0,
    )
    assert isinstance(var_43, python_code_.model_TargetObject)
    var_44 = {var_43, var_43, var_43}
    var_47 = dict
    python_code_.model_Location(address=var_0, id=var_47)
    var_51 = python_code_.model_BNode
    var_52 = "_model_PrimaryObject__model_PrimaryObject33._model_Person__Person"
    python_code_.model_PrimaryObject(
        id=(-600, -1773, 1),
        name=var_7,
        unsettableAttribute=var_47,
        unsettableAttributeWithDefault=var_47,
        featureMapReferenceCollection=var_7,
        featureMapAttributeType1=var_51,
        featureMapAttributeType2=var_52,
        featureMapAttributeCollection=set(),
        model_PrimaryObject36=var_44,
        model_PrimaryObject=var_43,
        model_PrimaryObject27=var_43,
    )


@pytest.mark.xfail(strict=True)
def test_44():
    var_3 = False
    var_21 = "93}\"-U~\n'"
    python_code_.model_PersonBNode(name=var_21, model_PersonBNode5=var_3)
    var_13 = "]USwbY.rlSq5JA"
    var_23 = python_code_.model_BNode
    var_25 = "hI\\ZP#Z@k"
    var_27 = -2772
    var_28 = "Phs,V%$i/"
    var_29 = ')WV{\\Z9Fs,l;"N F'
    var_30 = "09I@"
    var_31 = ""
    var_32 = python_code_.model_TargetObject(
        id=var_3,
        singleAttribute=var_31,
        arrayAttribute=var_25,
        model_TargetObject37=var_25,
        model_TargetObject43=var_27,
    )
    assert isinstance(var_32, python_code_.model_TargetObject)
    var_33 = {var_32, var_32, var_32}
    python_code_.model_PrimaryObject(
        id=var_23,
        name=b'"\x1e\xa8\xbc\x8c\x13\x8c\xa4:\x12\xf8',
        unsettableAttribute=var_13,
        unsettableAttributeWithDefault=var_28,
        featureMapReferenceCollection=var_13,
        featureMapAttributeType1=var_29,
        featureMapAttributeType2=var_28,
        featureMapAttributeCollection=var_30,
        model_PrimaryObject30=var_33,
        model_PrimaryObject48=complex(-2723.863, 203.56387),
    )


@pytest.mark.xfail(strict=True)
def test_45():
    var_0 = "j%:T#Y&[0-t\\xt:Z\r&s"
    var_1 = set()
    var_2 = python_code_.model_MappedLibrary(
        books=var_0, model_MappedLibrary20=var_0, model_MappedLibrary23=var_1
    )
    var_3 = -809
    var_4 = "o>|8a6"
    var_5 = "R[7~I"
    var_6 = python_code_.model_Movie(id=var_3, title=var_5, actorOf=var_1)
    assert isinstance(var_6, python_code_.model_Movie)
    var_7 = python_code_.model_Actor(id=var_3, name=var_4, actors=var_0, Actor=var_6)
    assert isinstance(var_7, python_code_.model_Actor)
    var_8 = python_code_.model_Actor
    var_9 = python_code_.model_TargetObject(
        id=var_8,
        singleAttribute=-4339.97,
        arrayAttribute=var_8,
        model_TargetObject34=-842.04,
    )
    assert isinstance(var_9, python_code_.model_TargetObject)
    var_10 = "model_TargetObject49model_Actormodel_Book"
    var_11 = python_code_.model_Location(
        address=var_10, id=var_0, model_Location15=var_2
    )
    var_12 = hash
    var_13 = -3667
    var_14 = "model_TargetObject28-model_BNode-_model_Actor__Actor-_model_PrimaryObject__model_PrimaryObject42"
    var_15 = "_model_PrimaryObject__model_PrimaryObject39"
    var_16 = ""
    var_17 = python_code_.model_PrimaryObject(
        id=var_13,
        name=complex(-2617.868275, -2445.0961225),
        unsettableAttribute=["", -564.62, 1469.5],
        unsettableAttributeWithDefault=var_14,
        featureMapReferenceCollection=var_15,
        featureMapAttributeType1={2129.0},
        featureMapAttributeType2=var_16,
        featureMapAttributeCollection=var_10,
        model_PrimaryObject39=var_16,
        model_PrimaryObject27=set(),
        model_PrimaryObject45=var_1,
    )
    assert isinstance(var_17, python_code_.model_PrimaryObject)
    python_code_.model_TargetObject(
        id=var_9,
        singleAttribute=var_10,
        arrayAttribute=var_0,
        model_TargetObject31=var_11,
        model_TargetObject40=var_7,
        model_TargetObject43=var_10,
        model_TargetObject=var_12,
        model_TargetObject28=var_17,
        model_TargetObject49=var_17,
    )


@pytest.mark.xfail(strict=True)
def test_46():
    var_0 = "j%:T#Y&[0-t\\xt:Z\r&s"
    var_1 = set()
    var_2 = python_code_.model_MappedLibrary(
        books=var_0, model_MappedLibrary20=var_0, model_MappedLibrary23=var_1
    )
    var_3 = -816
    var_4 = "o>|8a6"
    var_5 = "R[7~I"
    var_8 = python_code_.model_Actor
    var_9 = python_code_.model_TargetObject(
        id=var_8,
        singleAttribute=-4339.97,
        arrayAttribute=var_8,
        model_TargetObject34=-842.04,
    )
    assert isinstance(var_9, python_code_.model_TargetObject)
    var_10 = "model_TargetObject49model_Actormodel_Book"
    python_code_.model_Location(address=var_10, id=var_0, model_Location15=var_2)
    var_15 = "_model_PrimaryObject__model_PrimaryObject39"
    var_37 = ""
    var_38 = python_code_.model_PrimaryObject(
        id=var_3,
        name=complex(-2617.868275, -2445.0961225),
        unsettableAttribute=["", -564.62, 1469.5],
        unsettableAttributeWithDefault=var_37,
        featureMapReferenceCollection=var_4,
        featureMapAttributeType1={2129.0},
        featureMapAttributeType2=var_37,
        featureMapAttributeCollection=var_5,
        model_PrimaryObject39=var_37,
        model_PrimaryObject27=set(),
        model_PrimaryObject45=var_1,
    )
    assert isinstance(var_38, python_code_.model_PrimaryObject)
    var_40 = "?WHxl"
    var_41 = "model_TargetObject49Actor_model_BNode__model_BNode6model_Location18"
    python_code_.model_PrimaryObject(
        id=[False, 4245, 1521.16],
        name=var_5,
        unsettableAttribute=var_37,
        unsettableAttributeWithDefault=var_40,
        featureMapReferenceCollection=var_15,
        featureMapAttributeType1=var_8,
        featureMapAttributeType2=var_40,
        featureMapAttributeCollection=var_41,
        model_PrimaryObject30=(),
        model_PrimaryObject33=var_9,
        model_PrimaryObject36=1153.8,
        model_PrimaryObject42=False,
        model_PrimaryObject45=var_1,
    )


def test_47():
    var_0 = -1335
    python_code_.model_BNode(id=3, model_BNode=var_0, model_BNode6={var_0, -758})
    var_4 = hash
    var_5 = "0Jfc!\x0b_m{F#"
    var_6 = python_code_.model_BookBNode(title=var_5)
    var_7 = python_code_.model_PersonBNode(name=var_4, model_PersonBNode5=var_6)
    assert isinstance(var_7, python_code_.model_PersonBNode)


@pytest.mark.xfail(strict=True)
def test_48():
    var_14 = '"P~x+&kQI_j]'
    var_15 = "C{~yY?m"
    var_16 = "~bMM"
    var_18 = (
        "_model_PrimaryObject__model_PrimaryObject42:_model_BookBNode__model_BookBNode4"
    )
    python_code_.model_BookBNode(title=var_18, model_BookBNode=var_16)
    var_22 = dict
    python_code_.model_Location(address=False, id=var_22, model_Location=set())
    var_24 = "model_PersonBNode5._model_PersonBNode__model_PersonBNode.model_Book._model_PrimaryObject__model_PrimaryObject30"
    var_25 = python_code_.model_Person(name=var_15)
    python_code_.model_Book(
        title=var_24, tags=var_14, data=var_14, Book=var_25, books=var_22
    )


def test_49():
    var_0 = "model_Library10"
    python_code_.model_PersonBNode(
        name="model_PrimaryObject27,_model_BookBNode__model_BookBNode,_model_Movie__actorOf",
        model_PersonBNode=set(),
        model_PersonBNode5=var_0,
    )


@pytest.mark.xfail(strict=True)
def test_50():
    var_0 = "model_Library10"
    python_code_.model_PersonBNode(
        name="model_PrimaryObject27,_model_BookBNode__model_BookBNode,_model_Movie__actorOf",
        model_PersonBNode=set(),
        model_PersonBNode5=var_0,
    )
    var_68 = python_code_.model_BNode
    var_70 = "hI\\ZP#Z@k"
    python_code_.model_Person(name=var_70, authors=var_68, Person={})


@pytest.mark.xfail(strict=True)
def test_51():
    var_8 = python_code_.model_Movie(
        id=-823,
        title="_model_TargetObject__model_TargetObject:_model_Movie__actorOf:_model_PrimaryObject__model_PrimaryObject45:_model_Book__model_Book",
    )
    assert isinstance(var_8, python_code_.model_Movie)
    var_15 = python_code_.model_MappedLibrary(
        books="f<mGrCGS<ujLE", model_MappedLibrary=var_8
    )
    var_16 = "actorOf_model_TargetObject__model_TargetObject46"
    python_code_.model_Location(
        address=b"*\xafgP\x7f\xb4\x0c\x94\xc9", id=var_16, model_Location18=var_15
    )


@pytest.mark.xfail(strict=True)
def test_52():
    python_code_.model_PersonBNode(name=("4bjt<zZ",))
    python_code_.model_Person(name="w{m", authors=set())
    var_2 = 871
    var_3 = "_model_Book__model_Book"
    var_4 = 820
    var_5 = python_code_.model_Actor(id=var_4, name=var_3, Actor={True})
    assert isinstance(var_5, python_code_.model_Actor)
    var_6 = {var_5, var_5, var_5}
    var_7 = python_code_.model_Movie(id=var_2, title=var_3, actorOf=var_6)
    assert isinstance(var_7, python_code_.model_Movie)
    var_11 = "l{"
    var_12 = python_code_.model_Person
    var_13 = ""
    var_14 = "MkG$I\\d"
    python_code_.model_PrimaryObject(
        id=var_12,
        name=b"\x03\xee!\x04\xe6W0\x1d\x80\x03\xd0",
        unsettableAttribute={"t@'v": True},
        unsettableAttributeWithDefault=("7_O%?Cq@_ ",),
        featureMapReferenceCollection=var_11,
        featureMapAttributeType1=var_5,
        featureMapAttributeType2=var_13,
        featureMapAttributeCollection=var_14,
        model_PrimaryObject36=var_2,
    )


@pytest.mark.xfail(strict=True)
def test_53():
    var_0 = "!07/aaX}"
    var_1 = "aI1k/J7j6%E`#2)Q"
    var_2 = -879
    var_3 = dict
    var_4 = "3s>!AvDBmi'+"
    var_5 = python_code_.model_PrimaryObject(
        id=var_2,
        name=var_3,
        unsettableAttribute=var_4,
        unsettableAttributeWithDefault=True,
        featureMapReferenceCollection=var_3,
        featureMapAttributeType1=var_1,
        featureMapAttributeType2=var_4,
        featureMapAttributeCollection=var_1,
        model_PrimaryObject33=var_1,
        model_PrimaryObject39=3365,
        model_PrimaryObject42=var_0,
        model_PrimaryObject27=var_4,
    )
    assert isinstance(var_5, python_code_.model_PrimaryObject)
    python_code_.model_TargetObject(
        id=False,
        singleAttribute=var_0,
        arrayAttribute=var_1,
        model_TargetObject34=var_5,
        model_TargetObject37=var_5,
        model_TargetObject=var_5,
        model_TargetObject28=var_0,
    )
