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
    model_BNode,
    model_Book,
    model_BookBNode,
    model_ETypes,
    model_Library,
    model_Location,
    model_MappedLibrary,
    model_Person,
    model_PersonBNode,
    model_PrimaryObject,
    model_TargetObject,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_2 = lambda *args, **kwargs: 3993
    var_18 = ["a!5T=(^pV", -2814, -3459.34]
    var_20 = 4240
    var_21 = "Book"
    var_22 = "nJzTQj$;g`/v[5"
    var_23 = "_model_Location__model_Location-_model_TargetObject__model_TargetObject37-model_MappedLibrary"
    var_24 = python_code_.model_TargetObject(
        id=var_18, singleAttribute=var_23, arrayAttribute=(), model_TargetObject34=var_2
    )
    var_25 = {var_24, var_24}
    python_code_.model_PrimaryObject(
        id=var_20,
        name=var_21,
        unsettableAttribute=var_22,
        unsettableAttributeWithDefault=var_22,
        featureMapReferenceCollection=var_21,
        featureMapAttributeType1=None,
        featureMapAttributeType2=var_21,
        featureMapAttributeCollection=var_2,
        model_PrimaryObject27=var_24,
        model_PrimaryObject42=var_25,
        model_PrimaryObject45=var_25,
    )


def test_1():
    var_36 = bool
    var_38 = "6GBw&"
    var_39 = "n~s'1)T@(p]\tq:"
    var_40 = -481
    var_41 = python_code_.model_TargetObject(
        id=var_40,
        singleAttribute=var_38,
        arrayAttribute=var_36,
        model_TargetObject37=var_39,
        model_TargetObject40={"Cw<": True},
    )
    assert isinstance(var_41, python_code_.model_TargetObject)


@pytest.mark.xfail(strict=True)
def test_2():
    var_0 = "3'\")&,\x0cra\n$OOAm"
    var_1 = python_code_.model_MappedLibrary(books=var_0)
    assert isinstance(var_1, python_code_.model_MappedLibrary)
    var_2 = python_code_.model_MappedLibrary(books=var_0)
    var_3 = str
    var_4 = "pnU;"
    var_5 = "n1<"
    var_6 = "_model_PersonBNode__model_PersonBNode5 model_BNode"
    var_7 = ""
    var_8 = python_code_.model_TargetObject(
        id=var_2,
        singleAttribute=var_7,
        arrayAttribute=var_7,
        model_TargetObject28=var_2,
        model_TargetObject34=var_5,
        model_TargetObject40=var_3,
    )
    assert isinstance(var_8, python_code_.model_TargetObject)
    python_code_.model_PrimaryObject(
        id=var_3,
        name=var_4,
        unsettableAttribute=var_5,
        unsettableAttributeWithDefault=var_3,
        featureMapReferenceCollection=var_0,
        featureMapAttributeType1=var_6,
        featureMapAttributeType2=set(),
        featureMapAttributeCollection=var_6,
        model_PrimaryObject=var_8,
    )


def test_3():
    var_0 = "Ck"
    var_2 = python_code_.model_BNode(id=2591.62)
    var_3 = python_code_.model_Library()
    python_code_.model_Location(address=var_0, id=-2338.52, model_Location=var_3)
    var_5 = "_model_Book__model_Book.model_TargetObject40"
    var_7 = list
    var_8 = 699.46
    var_11 = python_code_.model_BNode(id=var_7, model_BNode=var_2)
    assert isinstance(var_11, python_code_.model_BNode)
    var_12 = python_code_.model_TargetObject(
        id=var_8, singleAttribute=var_5, arrayAttribute=(), model_TargetObject=var_7
    )
    assert isinstance(var_12, python_code_.model_TargetObject)


def test_4():
    var_18 = "_model_Book__model_Book24,_model_Pers3n__authors"
    var_19 = set
    var_20 = python_code_.model_PrimaryObject(
        id=-1,
        name="oT7Vp:wZ?QA\rgzY",
        unsettableAttribute="?/a}M$i",
        unsettableAttributeWithDefault=var_18,
        featureMapReferenceCollection="\n4@Tv3+|n|Pm>C",
        featureMapAttributeType1="n!/",
        featureMapAttributeType2=var_18,
        featureMapAttributeCollection="qC<G6e\t~AH+r;P?f1G",
        model_PrimaryObject45={1917.22, var_18, var_19},
    )
    assert isinstance(var_20, python_code_.model_PrimaryObject)
    var_22 = "Pk:})\x0bF[nlOCP"
    var_23 = python_code_.model_TargetObject(
        id=-447,
        singleAttribute=complex(2872.5, -1070.6424395),
        arrayAttribute=var_22,
        model_TargetObject31=var_19,
        model_TargetObject34=var_18,
        model_TargetObject49=var_20,
    )
    assert isinstance(var_23, python_code_.model_TargetObject)


def test_5():
    var_1 = "e"
    var_3 = set
    var_6 = "_model_TargetObject__model_TargetObject _model_TargetObject__model_TargetObject43"
    var_8 = python_code_.model_TargetObject(
        id={"W~MO]h+q=0Ec}St)": 452},
        singleAttribute=var_1,
        arrayAttribute=var_6,
        model_TargetObject43=var_3,
    )
    assert isinstance(var_8, python_code_.model_TargetObject)
    python_code_.model_BookBNode(title=[])


def test_6():
    var_0 = -913
    var_1 = "Vr:hx/T2'6 H~"
    var_2 = "UK["
    var_3 = set
    var_4 = python_code_.model_PrimaryObject(
        id=var_0,
        name=var_1,
        unsettableAttribute=3666.0,
        unsettableAttributeWithDefault=var_0,
        featureMapReferenceCollection=True,
        featureMapAttributeType1=var_1,
        featureMapAttributeType2=var_0,
        featureMapAttributeCollection=var_2,
        model_PrimaryObject27=var_3,
    )
    assert isinstance(var_4, python_code_.model_PrimaryObject)


def test_7():
    var_1 = "Vr:hx/T2'6 H~"
    var_2 = "UK["
    var_3 = set
    var_4 = python_code_.model_PrimaryObject(
        id=-2709,
        name="model_BookBNode_model_PrimaryObject__model_PrimaryObject48_model_Book__Book_model_Person__authors",
        unsettableAttribute="!]M{!",
        unsettableAttributeWithDefault=var_1,
        featureMapReferenceCollection="85Ax\ra^yUJv\x0c=d4`\x0c",
        featureMapAttributeType1="\rS",
        featureMapAttributeType2="Yr$<jk",
        featureMapAttributeCollection=")",
        model_PrimaryObject27=var_3,
        model_PrimaryObject30={3120.33},
        model_PrimaryObject33=None,
        model_PrimaryObject39=var_2,
        model_PrimaryObject48={
            -3131.68,
            "model_Book16-model_BookBNode4-model_BookBNode",
        },
    )
    assert isinstance(var_4, python_code_.model_PrimaryObject)


def test_8():
    var_1 = "e"
    var_2 = "_model_Book__model_Book16 _model_BookBNode__model_BookBNode4"
    var_3 = set
    var_4 = python_code_.model_PrimaryObject(
        id=-1,
        name="oT7Vp:wZ?QA\rgzY",
        unsettableAttribute="?/a}M$i",
        unsettableAttributeWithDefault=var_1,
        featureMapReferenceCollection="\n4@Tv3+|n|Pm>C",
        featureMapAttributeType1="n!/",
        featureMapAttributeType2=var_2,
        featureMapAttributeCollection="qC<G6e\t~AH+r;P?f1G",
        model_PrimaryObject45={1917.22, var_2, var_3},
    )
    assert isinstance(var_4, python_code_.model_PrimaryObject)


def test_9():
    var_2 = lambda *args, **kwargs: 3993
    var_18 = "_model_Book__model_Book24,_model_Pers3n__authors"
    var_20 = python_code_.model_PrimaryObject(
        id=2813,
        name=var_18,
        unsettableAttribute=var_18,
        unsettableAttributeWithDefault=var_18,
        featureMapReferenceCollection="/P3-)KwY\x0bDF4\t<m`v\\",
        featureMapAttributeType1=var_18,
        featureMapAttributeType2="fqn\x0c+sV,A?j;",
        featureMapAttributeCollection="model_TargetObject34._model_BNode__model_BNode6._model_Location__model_Location18._model_TargetObject__model_TargetObject31",
        model_PrimaryObject30=set(),
        model_PrimaryObject36=set(),
        model_PrimaryObject39=None,
        model_PrimaryObject=var_2,
        model_PrimaryObject48=set(),
    )
    assert isinstance(var_20, python_code_.model_PrimaryObject)
    var_22 = "Pk:})\x0bF[nlOCP"
    var_24 = python_code_.model_Location(address=var_22, id=var_18, model_Location=None)
    var_25 = 914
    var_26 = python_code_.model_TargetObject(
        id=var_25,
        singleAttribute=var_18,
        arrayAttribute=var_24,
        model_TargetObject34=complex(-579.70162, -2455.0941),
        model_TargetObject37=var_20,
        model_TargetObject43="model_TargetObject49._model_PersonBNode__model_PersonBNode5.model_MappedLibrary20._model_TargetObject__model_TargetObject40",
        model_TargetObject=var_2,
    )
    assert isinstance(var_26, python_code_.model_TargetObject)


def test_10():
    var_2 = python_code_.model_BNode(id=2591.62)
    var_3 = python_code_.model_Library()
    var_11 = python_code_.model_MappedLibrary(books=var_3)
    assert isinstance(var_11, python_code_.model_MappedLibrary)
    var_12 = {var_2, var_2, var_2}
    var_13 = python_code_.model_BNode(
        id=(
            995.63,
            1,
            "model_BookBNode4:_model_BNode__model_BNode6:_model_MappedLibrary__model_MappedLibrary20:model_MappedLibrary",
        ),
        model_BNode6=var_12,
    )
    assert isinstance(var_13, python_code_.model_BNode)


def test_11():
    var_50 = python_code_.model_MappedLibrary(books="e*", model_MappedLibrary23=set())
    assert isinstance(var_50, python_code_.model_MappedLibrary)


def test_12():
    python_code_.model_BookBNode(title="VleTb\n", model_BookBNode4={"", 830})
    var_32 = python_code_.model_MappedLibrary(
        books="_model_Book__model_Book16 _model_Book__model_Book21 _model_MappedLibrary__model_MappedLibrary",
        model_MappedLibrary=None,
        model_MappedLibrary20=set(),
    )
    assert isinstance(var_32, python_code_.model_MappedLibrary)


def test_13():
    var_19 = "3\n-"
    python_code_.model_BookBNode(title=var_19)
    var_21 = "^M)v`6\n+\x0cW(lJ"
    python_code_.model_Location(address=var_21, id=var_21)


def test_14():
    var_24 = "nv+PfC=G6O|$"
    var_26 = python_code_.model_PersonBNode(name=var_24)
    python_code_.model_BNode(id=False)
    var_28 = dict
    python_code_.model_Location(
        address=var_26,
        id=var_28,
        model_Location15=var_26,
        model_Location=var_28,
        model_Location18=var_24,
    )


def test_15():
    var_0 = 478
    var_1 = bool
    python_code_.model_BNode(id=var_0, model_BNode=var_1)


def test_16():
    var_24 = "n~s'1)T@(p]\tq:"
    python_code_.model_PersonBNode(name=var_24)
    python_code_.model_BNode(id=False)


def test_17():
    var_2 = "U[\\"
    python_code_.model_BookBNode(
        title="_model_TargetObject__model_TargetObject43-model_Library12-model_MappedLibrary",
        model_BookBNode=var_2,
        model_BookBNode4=set(),
    )


def test_18():
    var_28 = (
        lambda *args, **kwargs: "_model_BNode__model_BNode model_BookBNode4 _model_BookBNode__model_BookBNode"
    )
    python_code_.model_BookBNode(
        title="_model_MappedLibrary__model_MappedLibrary23", model_BookBNode=var_28
    )


def test_19():
    var_0 = "3'\")&,\x0cra\n$OOAm"
    var_2 = python_code_.model_MappedLibrary(books=var_0)
    assert isinstance(var_2, python_code_.model_MappedLibrary)
    var_58 = "model_Library,model_MappedLibrary,model_BNode6,_model_Book__model_Book24"
    var_59 = "hmC"
    var_60 = python_code_.model_BookBNode(title=var_2)
    var_61 = python_code_.model_PersonBNode(
        name=var_0, model_PersonBNode=var_58, model_PersonBNode5=var_60
    )
    assert isinstance(var_61, python_code_.model_PersonBNode)
    var_62 = python_code_.model_BookBNode(title=[], model_BookBNode=var_61)
    assert isinstance(var_62, python_code_.model_BookBNode)
    python_code_.model_PersonBNode(name=var_59, model_PersonBNode5=var_60)


def test_20():
    var_0 = '&z" ]q('
    var_1 = sorted
    var_2 = python_code_.model_PersonBNode(name=var_0, model_PersonBNode5=var_1)
    var_3 = {var_2, var_2, var_2, var_2, var_2}
    var_4 = python_code_.model_BookBNode(
        title=var_0, model_BookBNode=var_2, model_BookBNode4=var_3
    )
    assert isinstance(var_4, python_code_.model_BookBNode)


def test_21():
    var_2 = lambda *args, **kwargs: 3993
    var_15 = "UK["
    python_code_.model_Book(
        title=var_15,
        tags="5HJ($6=Z\t^",
        data=var_15,
        Book=var_15,
        books={-4657, var_2},
        model_Book=None,
    )


def test_22():
    var_0 = "'f8Yl(IopH^oNT"
    python_code_.model_Book(
        title=";=8>",
        tags="&E}0\rLJq&GJZ'$%V",
        data=var_0,
        model_Book=var_0,
        model_Book21=None,
    )


def test_23():
    var_0 = "model_Location15 _model_PrimaryObject__model_PrimaryObject48 model_MappedLibrary20 _model_TargetObject__model_TargetObject28"
    var_1 = python_code_.model_Person(name=var_0)
    var_2 = "w04~u?GlCW\x0cod4"
    var_3 = python_code_.model_PersonBNode
    var_4 = "9_WKO"
    var_5 = python_code_.model_MappedLibrary(books=var_4, model_MappedLibrary23=[])
    assert isinstance(var_5, python_code_.model_MappedLibrary)
    var_6 = python_code_.model_Book(
        title=var_2,
        tags=var_3,
        data=var_1,
        model_Book21=var_5,
        model_Book24=-7,
        model_Book13=True,
    )
    assert isinstance(var_6, python_code_.model_Book)
    var_22 = "7"
    python_code_.model_Book(title=var_3, tags=False, data=var_5)
    var_32 = "kp^Bf<_K'H)P]<E)z7w"
    var_33 = python_code_.model_Book(
        title=var_2,
        tags=var_32,
        data=var_22,
        model_Book21=var_2,
        model_Book24=var_5,
        model_Book13=var_5,
    )
    assert isinstance(var_33, python_code_.model_Book)


def test_24():
    var_0 = "'f8Yl(IopH^oNT"
    python_code_.model_Book(
        title=";=8>",
        tags="&E}0\rLJq&GJZ'$%V",
        data=var_0,
        model_Book=var_0,
        model_Book21=None,
    )
    var_24 = python_code_.model_Library
    var_26 = "hN\nP"
    var_27 = python_code_.model_Library()
    python_code_.model_Book(
        title=var_26,
        tags=[-428.48, "6tuCD", 3660.15],
        data=var_24,
        model_Book=var_27,
        model_Book13=var_27,
    )


def test_25():
    var_0 = "model_Location15 _model_PrimaryObject__model_PrimaryObject48 model_MappedLibrary20 _model_TargetObject__model_TargetObject28"
    python_code_.model_Person(name='.v\n"Q\rd\nOo:\x0c\ri', authors=set())
    var_2 = "_model_Book__model_Book21_model_TargetObject__model_TargetObject40model_Location"
    var_3 = python_code_.model_PersonBNode
    var_4 = "9_WKO"
    var_5 = python_code_.model_MappedLibrary(books=var_4, model_MappedLibrary23=[])
    assert isinstance(var_5, python_code_.model_MappedLibrary)
    var_6 = python_code_.model_Book(
        title=var_2, tags="", data=var_0, model_Book21=var_5, model_Book24=None
    )
    assert isinstance(var_6, python_code_.model_Book)
    python_code_.model_Book(title=var_3, tags=False, data=var_5)


def test_26():
    var_42 = "UK["
    var_43 = set
    python_code_.model_Person(name=var_43, authors=var_42)


def test_27():
    var_2 = "UK["
    var_5 = "\x0b9m4TRGj\n'A3Z~L\r"
    python_code_.model_Person(name=var_2, Person=var_5)


def test_28():
    var_0 = -600
    python_code_.model_BNode(id=var_0)
    var_2 = lambda *args, **kwargs: 3993
    var_3 = "_model_TargetObject__model_TargetObject34._model_PrimaryObject__model_PrimaryObject._model_TargetObject__model_TargetObject28._model_Book__model_Book"
    var_4 = python_code_.model_Person(name=var_3, Person=var_2)
    var_5 = {var_4, var_4}
    var_6 = python_code_.model_Book(
        title=var_0,
        tags=var_2,
        data=var_3,
        Book=b"b\xca\xd6\x97\x1f\xfcX{\xfd",
        books=var_5,
    )
    assert isinstance(var_6, python_code_.model_Book)
    var_7 = "_model_Location__model_Location"
    python_code_.model_PersonBNode(name=var_7)
    python_code_.model_BookBNode(title=var_7, model_BookBNode4=']2"l~')


def test_29():
    var_0 = '&z" ]q('
    var_5 = python_code_.model_Book(
        title="rd};P1ODe'j", tags=var_0, data="%UA'g\tw2\t!", books={var_0, True, True}
    )
    var_6 = {var_5}
    var_7 = python_code_.model_Person(name=var_5, authors=var_6, Person=var_5)
    assert isinstance(var_7, python_code_.model_Person)


def test_30():
    var_0 = "model_Location15 _model_PrimaryObject__model_PrimaryObject48 model_MappedLibrary20 _model_TargetObject__model_TargetObject28"
    var_1 = python_code_.model_Person(name=var_0)
    var_2 = "w04~u?GlCW\x0cod4"
    var_3 = python_code_.model_PersonBNode
    var_4 = "9_WKO"
    var_5 = python_code_.model_MappedLibrary(books=var_4, model_MappedLibrary23=[])
    assert isinstance(var_5, python_code_.model_MappedLibrary)
    var_6 = python_code_.model_Book(
        title=var_2,
        tags=var_3,
        data=var_1,
        model_Book21=var_5,
        model_Book24=-7,
        model_Book13=True,
    )
    assert isinstance(var_6, python_code_.model_Book)
    var_8 = ",_*d\r\r"
    python_code_.model_Book(title=var_3, tags=var_2, data=var_8)
    var_10 = "model_TargetObject31 _model_BookBNode__model_BookBNode"
    var_11 = python_code_.model_BookBNode(title=var_10)
    var_12 = {var_11}
    var_13 = python_code_.model_PersonBNode(name=var_1, model_PersonBNode=var_12)
    assert isinstance(var_13, python_code_.model_PersonBNode)
    python_code_.model_PersonBNode(name=var_0)


def test_31():
    var_6 = "_model_Location__model_Location"
    var_7 = python_code_.model_PersonBNode(name=var_6)
    var_8 = python_code_.model_BookBNode(title=var_6, model_BookBNode=var_7)
    assert isinstance(var_8, python_code_.model_BookBNode)
    python_code_.model_BookBNode(title=var_6, model_BookBNode4=']2"l~')


def test_32():
    var_0 = "Ck"
    var_1 = python_code_.model_Person(name=var_0)
    python_code_.model_BNode(id=2591.62)
    var_3 = python_code_.model_Library()
    python_code_.model_Location(address=var_0, id=-2338.52, model_Location=var_3)
    var_7 = list
    var_8 = 699.46
    var_9 = 3440
    python_code_.model_ETypes(
        eBigDecimal=2702.72,
        eBigInteger=var_1,
        eBoolean=set(),
        eByte=var_0,
        eByteArray=var_3,
        eChar=var_0,
        eDate=var_7,
        eDouble=var_8,
        eFloat=-553,
        eInt=var_9,
        eLong=var_0,
        eShort={},
        eString=var_0,
        uris=var_9,
    )


@pytest.mark.xfail(strict=True)
def test_33():
    var_0 = -600
    var_1 = python_code_.model_BNode(id=var_0)
    var_2 = lambda *args, **kwargs: 3993
    var_3 = "_model_TargetObject__model_TargetObject34._model_PrimaryObject__model_PrimaryObject._model_TargetObject__model_TargetObject28._model_Book__model_Book"
    python_code_.model_Person(name="")
    var_11 = set
    var_12 = python_code_.model_PrimaryObject(
        id=-1,
        name="oT7Vp:wZ?QA\rgzY",
        unsettableAttribute="?/a}M$i",
        unsettableAttributeWithDefault=var_3,
        featureMapReferenceCollection="\n4@Tv3+|n|Pm>C",
        featureMapAttributeType1="n!/",
        featureMapAttributeType2=var_3,
        featureMapAttributeCollection="qC<G6e\t~AH+r;P?f1G",
        model_PrimaryObject45={1917.22, var_3, var_11},
    )
    assert isinstance(var_12, python_code_.model_PrimaryObject)
    var_15 = python_code_.model_TargetObject(
        id=var_0,
        singleAttribute=var_1,
        arrayAttribute=True,
        model_TargetObject28=var_0,
        model_TargetObject40=29.82,
    )
    assert isinstance(var_15, python_code_.model_TargetObject)
    var_16 = 868
    var_17 = "qf \x0bQJCq+$X"
    python_code_.model_PrimaryObject(
        id=var_16,
        name=var_17,
        unsettableAttribute=var_12,
        unsettableAttributeWithDefault=var_3,
        featureMapReferenceCollection=var_11,
        featureMapAttributeType1=var_15,
        featureMapAttributeType2=var_1,
        featureMapAttributeCollection=var_3,
        model_PrimaryObject27=var_0,
        model_PrimaryObject33=var_2,
        model_PrimaryObject36=var_11,
    )


def test_34():
    var_1 = "e"
    var_2 = "_model_Book__model_Book16 _model_BookBNode__model_BookBNode4"
    var_4 = python_code_.model_PrimaryObject(
        id=1,
        name="e",
        unsettableAttribute=var_1,
        unsettableAttributeWithDefault=var_1,
        featureMapReferenceCollection=var_1,
        featureMapAttributeType1=var_1,
        featureMapAttributeType2=var_2,
        featureMapAttributeCollection=var_1,
        model_PrimaryObject30=set(),
        model_PrimaryObject33=None,
        model_PrimaryObject36={-1666.69, '|"\x0b+shr\x0b'},
        model_PrimaryObject45={'Zj7}@\r"2wQ.{p%]ni%', var_1},
    )
    assert isinstance(var_4, python_code_.model_PrimaryObject)


def test_35():
    var_1 = "?"
    var_2 = "_model_Book__model_Book16 _model_BookBNode__model_BookBNode4"
    var_4 = python_code_.model_PrimaryObject(
        id=169,
        name=var_2,
        unsettableAttribute="model_BookBNode",
        unsettableAttributeWithDefault="_model_Book__Book",
        featureMapReferenceCollection=var_1,
        featureMapAttributeType1="_model_Book__model_Book21,model_PrimaryObject30",
        featureMapAttributeType2="model_MappedLibrary20._model_Location__model_Location15",
        featureMapAttributeCollection=var_2,
        model_PrimaryObject36=set(),
    )
    assert isinstance(var_4, python_code_.model_PrimaryObject)


@pytest.mark.xfail(strict=True)
def test_36():
    var_42 = "UK["
    var_43 = python_code_.model_MappedLibrary(books=var_42, model_MappedLibrary=var_42)
    assert isinstance(var_43, python_code_.model_MappedLibrary)
    python_code_.model_Location(address=4914.17, id=var_42, model_Location18=var_43)


@pytest.mark.xfail(strict=True)
def test_37():
    var_1 = "e"
    var_2 = "_model_Book__model_Book16 _model_BookBNode__model_BookBNode4"
    var_3 = set
    var_6 = "_model_TargetObject__model_TargetObject _model_TargetObject__model_TargetObject43"
    var_7 = (
        lambda *args, **kwargs: "_model_BNode__model_BNode model_BookBNode4 _model_BookBNode__model_BookBNode"
    )
    var_8 = python_code_.model_TargetObject(
        id={"W~MO]h+q=0Ec}St)": 452},
        singleAttribute=var_1,
        arrayAttribute=var_6,
        model_TargetObject43=var_3,
    )
    assert isinstance(var_8, python_code_.model_TargetObject)
    python_code_.model_PrimaryObject(
        id=var_3,
        name=var_6,
        unsettableAttribute=var_1,
        unsettableAttributeWithDefault=var_2,
        featureMapReferenceCollection=var_6,
        featureMapAttributeType1=var_2,
        featureMapAttributeType2=var_2,
        featureMapAttributeCollection=var_7,
        model_PrimaryObject27=var_3,
        model_PrimaryObject33=var_8,
        model_PrimaryObject45=complex(4302.5, -842.3),
    )


def test_38():
    var_0 = -913
    var_1 = ()
    var_6 = python_code_.model_PrimaryObject(
        id=3,
        name=var_1,
        unsettableAttribute=var_1,
        unsettableAttributeWithDefault=var_1,
        featureMapReferenceCollection="model_TargetObject34",
        featureMapAttributeType1=var_1,
        featureMapAttributeType2=var_1,
        featureMapAttributeCollection="jMBqAE(tMw//",
        model_PrimaryObject33=None,
        model_PrimaryObject39=None,
        model_PrimaryObject42={"/K+Yy9", False, var_0},
    )
    assert isinstance(var_6, python_code_.model_PrimaryObject)
    var_7 = python_code_.model_Library()
    var_8 = "8a}-Y&Ay],"
    python_code_.model_Location(address=var_7, id=var_8, model_Location15=var_7)


def test_39():
    var_0 = "Ck"
    var_2 = python_code_.model_BNode(id=2591.62)
    var_3 = python_code_.model_Library()
    python_code_.model_Location(address=var_0, id=-2338.52, model_Location=var_3)
    var_7 = list
    var_11 = python_code_.model_BNode(id=var_7, model_BNode=var_2)
    assert isinstance(var_11, python_code_.model_BNode)


@pytest.mark.xfail(strict=True)
def test_40():
    var_1 = "e"
    var_2 = "uYo8<hfO$"
    var_3 = python_code_.model_MappedLibrary
    var_4 = python_code_.model_PrimaryObject(
        id=-1,
        name="oT7Vp:wZ?QA\rgzY",
        unsettableAttribute="?/a}M$i",
        unsettableAttributeWithDefault=var_1,
        featureMapReferenceCollection="\n4@Tv3+|n|Pm>C",
        featureMapAttributeType1="n!/",
        featureMapAttributeType2=var_2,
        featureMapAttributeCollection="qC<G6e\t~AH+r;P?f1G",
        model_PrimaryObject45={1917.22, var_2, var_3},
    )
    assert isinstance(var_4, python_code_.model_PrimaryObject)
    var_6 = 2834
    var_7 = "_model_TargetObject__model_TargetObject49 model_Location18"
    python_code_.model_TargetObject(
        id=var_6,
        singleAttribute=var_7,
        arrayAttribute={"model_TargetObject28model_BNode", True, -1},
        model_TargetObject37=var_6,
        model_TargetObject40=var_4,
    )


@pytest.mark.xfail(strict=True)
def test_41():
    var_0 = -600
    python_code_.model_BNode(id=var_0, model_BNode6={1184.32, var_0})
    var_2 = lambda *args, **kwargs: 3993
    var_3 = "_model_TargetOject__model_TaNgetObject34._model_PrimaryObject__model_PrimaryObject._model_TargetObject__model_TargetObject28._model_Book__model_Book"
    var_4 = python_code_.model_Person(name=var_3, Person=var_2)
    var_5 = {var_4, var_4}
    var_11 = "model_TargetObjct46:model_PrimaryObjec45:model_TargetObject49"
    var_13 = python_code_.model_MappedLibrary(
        books="B9OQ",
        model_MappedLibrary23=[
            True,
            "model_MappedLibrary _model_Location__model_Location Person",
            "{|\r^",
        ],
    )
    assert isinstance(var_13, python_code_.model_MappedLibrary)
    var_14 = "aUe8LOn/F^q{\x0buS"
    var_15 = "z}aVSFR3"
    var_16 = "model_PrimaryObject45authors"
    var_17 = "OCHrbuoZ<\n\rUf"
    var_18 = "#AElqN-d"
    var_19 = "%f/i]AE{xWoX"
    var_22 = "G.w^XRI7%f)0rN4z1L_"
    var_23 = python_code_.model_PrimaryObject(
        id=499,
        name="bZ\td||5Pnf\rJ]g",
        unsettableAttribute=":)'i\rhPzul\"?#",
        unsettableAttributeWithDefault=var_22,
        featureMapReferenceCollection=var_3,
        featureMapAttributeType1=var_11,
        featureMapAttributeType2=var_16,
        featureMapAttributeCollection=var_19,
        model_PrimaryObject30=var_5,
        model_PrimaryObject33=var_17,
        model_PrimaryObject36=var_5,
        model_PrimaryObject=None,
    )
    assert isinstance(var_23, python_code_.model_PrimaryObject)
    var_24 = python_code_.model_TargetObject(
        id=3396,
        singleAttribute=var_3,
        arrayAttribute=var_14,
        model_TargetObject31=var_23,
        model_TargetObject43=var_23,
        model_TargetObject46=None,
    )
    assert isinstance(var_24, python_code_.model_TargetObject)
    python_code_.model_PrimaryObject(
        id=var_15,
        name=var_3,
        unsettableAttribute=var_2,
        unsettableAttributeWithDefault=var_16,
        featureMapReferenceCollection=var_17,
        featureMapAttributeType1=1902,
        featureMapAttributeType2=141.33,
        featureMapAttributeCollection=var_18,
        model_PrimaryObject27=var_24,
        model_PrimaryObject30=-3843.52,
        model_PrimaryObject39=var_24,
    )


@pytest.mark.xfail(strict=True)
def test_42():
    var_33 = "model_Location18_model_PersonBNode_lmodel_PersonBNodemodel_Location18model_MappedLibrary"
    var_42 = "_model_PrimaryObject__model_PrimaryObject"
    var_43 = python_code_.model_Book
    var_44 = python_code_.model_Location(address=var_33, id=var_42)
    python_code_.model_Book(
        title=var_42,
        tags="model_MappedLibrary",
        data=var_42,
        Book=var_43,
        model_Book16=var_44,
    )


def test_43():
    var_0 = "YG-u-v50\r:g.LCg"
    var_1 = python_code_.model_TargetObject
    var_2 = python_code_.model_Person(name=var_1)
    var_3 = python_code_.model_Library()
    var_4 = python_code_.model_Book(
        title=var_0,
        tags=var_0,
        data=214.25,
        Book=var_2,
        model_Book=var_3,
        model_Book21=complex(-218.0, -5073.99087),
        model_Book13=var_3,
        model_Book16="_model_PrimaryObject__model_PrimaryObject,books,_model_MappedLibrary__model_MappedLibrary23",
    )
    assert isinstance(var_4, python_code_.model_Book)
    var_5 = True
    var_6 = "%-QCI\x0c(&?spBY4-u\t"
    var_7 = "_model_PersonBNode__model_PersonBNode5 _model_PrimaryObject__model_PrimaryObject36"
    python_code_.model_ETypes(
        eBigDecimal=var_1,
        eBigInteger=var_0,
        eBoolean=var_5,
        eByte=var_4,
        eByteArray=var_6,
        eChar=False,
        eDate=var_4,
        eDouble=var_1,
        eFloat=416,
        eInt=var_1,
        eLong=var_6,
        eShort=var_7,
        eString=var_7,
        uris=var_0,
    )
    var_9 = 1069
    python_code_.model_BNode(id=var_9)


@pytest.mark.xfail(strict=True)
def test_44():
    var_0 = "Ck"
    var_2 = python_code_.model_BNode(id=2591.62)
    var_4 = python_code_.model_Location(address="\t\n`PvdW:\t6?&.L~", id=var_0)
    var_5 = "_model_Book__model_Book.model_TargetObject40"
    var_7 = list
    var_9 = 3440
    var_11 = python_code_.model_BNode(id=var_9, model_BNode=var_2)
    assert isinstance(var_11, python_code_.model_BNode)
    var_12 = "bJR.kinG5"
    var_14 = "_model_TargetObject__model_TargetObject49._model_Book__Book.model_BNode6.model_TargetObject49"
    python_code_.model_Book(title=var_12, tags=None, data=var_14, model_Book21=var_2)
    var_16 = -1
    var_17 = "pv+c`=U= CL,v1VH<he"
    var_18 = "E "
    var_19 = "5o|5C4rP)"
    var_20 = "D}C9DT@"
    var_21 = python_code_.model_PrimaryObject(
        id=set(),
        name={
            "aT\\r",
            "_model_MappedLibrary__model_MappedLibrary model_MappedLibrary model_PersonBNode",
            False,
        },
        unsettableAttribute=var_18,
        unsettableAttributeWithDefault=var_19,
        featureMapReferenceCollection={False, 3375.25, False},
        featureMapAttributeType1=var_4,
        featureMapAttributeType2=var_20,
        featureMapAttributeCollection=var_0,
        model_PrimaryObject48=var_0,
    )
    assert isinstance(var_21, python_code_.model_PrimaryObject)
    var_22 = python_code_.model_TargetObject(
        id=var_16,
        singleAttribute={
            "model_TargetObject46 model_TargetObject34 _model_BNode__model_BNode6 _model_Person__Person": -405
        },
        arrayAttribute=var_17,
        model_TargetObject31=b"\xe7\x82ti",
        model_TargetObject34=var_17,
        model_TargetObject43=var_7,
        model_TargetObject46=var_21,
    )
    assert isinstance(var_22, python_code_.model_TargetObject)
    python_code_.model_TargetObject(
        id=-698,
        singleAttribute="4dZ9-VoE9oCztH",
        arrayAttribute=var_5,
        model_TargetObject37=var_21,
        model_TargetObject40=var_21,
        model_TargetObject43=var_21,
        model_TargetObject49=None,
    )


def test_45():
    var_0 = -913
    var_1 = "Vr:hx/T2'6 H~"
    var_2 = ";6`MAVW"
    var_4 = python_code_.model_PrimaryObject(
        id=var_0,
        name="model_Book24",
        unsettableAttribute=var_1,
        unsettableAttributeWithDefault=var_2,
        featureMapReferenceCollection=var_2,
        featureMapAttributeType1=var_2,
        featureMapAttributeType2=var_2,
        featureMapAttributeCollection="?QXrfDz2,Q))T",
        model_PrimaryObject36=set(),
        model_PrimaryObject48=set(),
    )
    assert isinstance(var_4, python_code_.model_PrimaryObject)
    var_5 = python_code_.model_Book(
        title=var_1,
        tags=b"\xee\xa2_\xd0\xbc\xf83\xa4\xae\xa3\xe7\xd6\xf3\x06\x16?\xdb8]",
        data=var_2,
        Book=complex(1200.9327307, -78.6),
        model_Book=2095.88,
    )
    var_6 = {var_5}
    var_7 = python_code_.model_Person(name=var_5, authors=var_6, Person=var_5)
    assert isinstance(var_7, python_code_.model_Person)


@pytest.mark.xfail(strict=True)
def test_46():
    var_8 = python_code_.model_Library()
    var_9 = "_model_Book__model_Book.model_TargetObject40"
    var_11 = 699.46
    var_14 = python_code_.model_BNode(id=var_11, model_BNode6=var_9)
    python_code_.model_BNode(id=var_8, model_BNode=var_14, model_BNode6=var_8)


@pytest.mark.xfail(strict=True)
def test_47():
    var_42 = "UK["
    var_43 = set
    var_44 = python_code_.model_MappedLibrary
    var_45 = python_code_.model_Location(
        address=4914.17, id=var_42, model_Location18=var_43
    )
    python_code_.model_MappedLibrary(books=var_44, model_MappedLibrary=var_45)


def test_48():
    var_0 = "Ck"
    var_3 = python_code_.model_Library()
    var_4 = python_code_.model_Location(
        address="_model_Book__books._model_TargetObject__model_TargetObject.Person",
        id="\r]KujX8/d'Qg\x0bQ",
        model_Location=var_3,
    )
    var_7 = list
    var_12 = "bJR.kinG5"
    python_code_.model_Location(address={}, id=var_12)
    var_17 = "pv+c`=U= CL,v1VH<he"
    var_18 = "4\x0ct97x>"
    var_19 = "5o|5C4rP)"
    var_20 = "D}C9DT@"
    var_21 = python_code_.model_PrimaryObject(
        id=set(),
        name={
            "aT\\r",
            "_model_MappedLibrary__model_MappedLibrary model_MappedLibrary model_PersonBNode",
            False,
        },
        unsettableAttribute=var_18,
        unsettableAttributeWithDefault=var_19,
        featureMapReferenceCollection={False, 3375.25, False},
        featureMapAttributeType1=var_4,
        featureMapAttributeType2=var_20,
        featureMapAttributeCollection=var_0,
        model_PrimaryObject48=var_0,
    )
    assert isinstance(var_21, python_code_.model_PrimaryObject)
    var_27 = "Pk:})\x0bF[nlOCP"
    var_28 = python_code_.model_TargetObject(
        id=-447,
        singleAttribute=complex(2872.5, -1070.6424395),
        arrayAttribute=var_27,
        model_TargetObject31=var_7,
        model_TargetObject34=var_17,
        model_TargetObject49=var_21,
    )
    assert isinstance(var_28, python_code_.model_TargetObject)
    python_code_.model_Person(name=var_12)


def test_49():
    python_code_.model_PersonBNode(name=None)
    var_1 = -741
    var_2 = -4380
    var_3 = python_code_.model_BNode(id=var_2)
    var_4 = {var_3}
    var_5 = python_code_.model_BNode(id=var_1, model_BNode6=var_4)
    assert isinstance(var_5, python_code_.model_BNode)
    var_6 = dict
    var_7 = ""
    var_8 = "Vf3#5RNIP3glD\\w*X"
    var_9 = 792.79
    var_10 = 2057
    var_11 = "model_Library10-model_BNode6"
    var_12 = ""
    python_code_.model_ETypes(
        eBigDecimal=var_6,
        eBigInteger=var_7,
        eBoolean=var_2,
        eByte=var_5,
        eByteArray=var_8,
        eChar=var_6,
        eDate=var_6,
        eDouble=var_9,
        eFloat="Aht!+X5#<",
        eInt=var_10,
        eLong=var_11,
        eShort=1397.18,
        eString=var_12,
        uris=var_8,
    )
    python_code_.model_PersonBNode(name={}, model_PersonBNode5=var_6)
    var_16 = False
    var_19 = "\n^Lo8<q&;"
    var_22 = python_code_.model_TargetObject(
        id=var_16,
        singleAttribute=var_6,
        arrayAttribute=var_6,
        model_TargetObject31=var_19,
        model_TargetObject37="z",
        model_TargetObject46=b"\xd1\x1aS-A\xcd\xeb\x00\xae\xfa-;\x9a",
    )
    assert isinstance(var_22, python_code_.model_TargetObject)


def test_50():
    var_6 = "_model_Book__model_Book.model_TargetObject40"
    var_9 = set
    var_10 = "\x0c<X-rA&D3D ="
    var_11 = python_code_.model_Book(
        title=var_10, tags=True, data=var_6, model_Book24=var_9
    )
    var_12 = {var_11, var_11, var_11}
    var_13 = python_code_.model_MappedLibrary(books=var_9, model_MappedLibrary20=var_12)
    assert isinstance(var_13, python_code_.model_MappedLibrary)
    var_14 = -286
    var_15 = len
    var_16 = python_code_.model_BNode(id=var_14, model_BNode=var_15, model_BNode6=var_6)
    var_17 = {var_16}
    var_18 = python_code_.model_BNode(id=var_14, model_BNode6=var_17)
    assert isinstance(var_18, python_code_.model_BNode)


@pytest.mark.xfail(strict=True)
def test_51():
    var_24 = "n~s'1)T@(p]\tq:"
    var_28 = ";6`MAVW"
    var_30 = python_code_.model_Book(
        title=var_28,
        tags=b"\xee\xa2_\xd0\xbc\xf83\xa4\xae\xa3\xe7\xd6\xf3\x06\x16?\xdb8]",
        data=var_28,
        Book=complex(1200.9327307, -78.6),
        model_Book=2095.88,
    )
    var_33 = -2058
    var_34 = "F2SQxB9^)$aG\rh"
    var_35 = ">6!Kxc)R(g&kS,Y,M"
    var_36 = int
    var_37 = "model_PrimaryObject42 model_MappedLibrary model_PersonBNode5"
    var_38 = python_code_.model_TargetObject(
        id=2195,
        singleAttribute=var_37,
        arrayAttribute="C,u81G%M9s",
        model_TargetObject34=var_30,
        model_TargetObject49=var_36,
    )
    assert isinstance(var_38, python_code_.model_TargetObject)
    python_code_.model_PrimaryObject(
        id=var_33,
        name=var_28,
        unsettableAttribute=var_28,
        unsettableAttributeWithDefault=var_34,
        featureMapReferenceCollection=var_24,
        featureMapAttributeType1=var_35,
        featureMapAttributeType2=2016.91,
        featureMapAttributeCollection=var_24,
        model_PrimaryObject27=var_38,
        model_PrimaryObject30=var_33,
        model_PrimaryObject33=var_38,
        model_PrimaryObject39=819,
        model_PrimaryObject45=complex(-292.96212, 28.65459),
    )
