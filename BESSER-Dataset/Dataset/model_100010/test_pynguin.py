#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    AuthorField,
    BibtexEntryTypes,
    bibTeX_AddressField,
    bibTeX_Article,
    bibTeX_AuthorField,
    bibTeX_Authors,
    bibTeX_BibtexEntryTypes,
    bibTeX_Book,
    bibTeX_CiteKey,
    bibTeX_EObject,
    bibTeX_EditionField,
    bibTeX_EditorField,
    bibTeX_Fullname,
    bibTeX_IsbnField,
    bibTeX_JournalField,
    bibTeX_Model,
    bibTeX_MonthField,
    bibTeX_NoteField,
    bibTeX_NumberField,
    bibTeX_PagesField,
    bibTeX_PublisherField,
    bibTeX_SeriesField,
    bibTeX_TitleField,
    bibTeX_UnknownField,
    bibTeX_UnknownType,
    bibTeX_UnknownValue,
    bibTeX_VolumeField,
    bibTeX_YearField,
    date,
    datetime,
    time,
)


def test_0():
    python_code_.bibTeX_UnknownValue(value="RXSa\x0czF")


def test_1():
    var_0 = python_code_.bibTeX_Article()
    python_code_.bibTeX_UnknownValue(value=var_0, bibTeX_UnknownValue=var_0)


def test_2():
    python_code_.bibTeX_Fullname(
        lastname={"T+": -2161, "5V|pdw": False, ")": 4337.78}, firstname={}
    )


def test_3():
    var_19 = "bibTeX_BibtexEntryTypes6 bibTeX_BibtexEntryTypes4 _bibTeX_VolumeField__bibTeX_VolumeField"
    var_16 = python_code_.bibTeX_Fullname(
        lastname=var_19,
        firstname="bibTeX_Article17 bibTeX_Book24 _bibTeX_IsbnField__bibTeX_IsbnField bibTeX_Book",
        bibTeX_Fullname="bibTeX_Book24 bibTeX_UnknownField37",
    )
    assert isinstance(var_16, python_code_.bibTeX_Fullname)


def test_4():
    var_17 = python_code_.bibTeX_EditionField(
        edition=complex(1523.745547, -938.0), bibTeX_EditionField=b"\xdc\xb9I\xdf"
    )
    assert isinstance(var_17, python_code_.bibTeX_EditionField)


def test_5():
    python_code_.bibTeX_EditionField(
        edition="_bibTeX_PagesField__bibTeX_PagesField", bibTeX_EditionField=None
    )


def test_6():
    python_code_.bibTeX_AddressField(address={})


def test_7():
    python_code_.bibTeX_UnknownType(type="X\tq[2tZ(QC;)")


def test_8():
    var_19 = "bibTeX_BibtexEntryHypwes6 bibTeX_BibtexEntryTypes4 _bibTeX)VolumeField_iPbibTeX_VolumeField"
    var_22 = python_code_.bibTeX_UnknownType(type=var_19, bibTeX_UnknownType=var_19)
    assert isinstance(var_22, python_code_.bibTeX_UnknownType)


def test_9():
    python_code_.bibTeX_IsbnField(isbn="")


def test_10():
    var_28 = python_code_.bibTeX_AuthorField()
    python_code_.bibTeX_IsbnField(isbn=var_28, bibTeX_IsbnField=var_28)


def test_11():
    python_code_.bibTeX_PagesField(pages=-2476)


def test_12():
    var_0 = python_code_.bibTeX_PagesField(pages="nCSvMHaW*>!}%i")
    python_code_.bibTeX_PagesField(pages=var_0, bibTeX_PagesField=var_0)


def test_13():
    python_code_.bibTeX_SeriesField(
        series="_bibTeX_YearField__bibTeX_YearField_bibTeX_EditionField__bibTeX_EditionFieldbibTeX_UnknownField_bibTeX_NumberField__bibTeX_NumberField"
    )


def test_14():
    var_0 = python_code_.bibTeX_Book()
    python_code_.bibTeX_SeriesField(series=399.57, bibTeX_SeriesField=var_0)


def test_15():
    python_code_.bibTeX_PublisherField(publisher=1)


def test_16():
    var_28 = python_code_.bibTeX_PublisherField(
        publisher=")<%E7W", bibTeX_PublisherField=complex(-1381.992632, 1371.1999556)
    )
    assert isinstance(var_28, python_code_.bibTeX_PublisherField)


def test_17():
    var_31 = python_code_.bibTeX_VolumeField(
        volume={}, bibTeX_VolumeField=":^tFwe\\9c{l \rt\x0bzPK"
    )
    assert isinstance(var_31, python_code_.bibTeX_VolumeField)


def test_18():
    python_code_.bibTeX_VolumeField(
        volume="_bibTeX_AddressField__bibTeX_AddressField", bibTeX_VolumeField=None
    )


def test_19():
    python_code_.bibTeX_JournalField(journal="bibTeX_Article15")


def test_20():
    var_3 = python_code_.bibTeX_JournalField(
        journal=b"\xd2", bibTeX_JournalField=complex(-190.77799, -1191.503)
    )
    assert isinstance(var_3, python_code_.bibTeX_JournalField)


def test_21():
    python_code_.bibTeX_NumberField(
        number="bibTeX_Book31,bibTeX_BibtexEntryTypes,_bibTeX_Fullname__bibTeX_Fullname,_bibTeX_EditionField__bibTeX_EditionField"
    )


def test_22():
    python_code_.bibTeX_MonthField(month=-521)


def test_23():
    var_22 = tuple
    var_23 = python_code_.bibTeX_MonthField(month=var_22, bibTeX_MonthField=2)
    assert isinstance(var_23, python_code_.bibTeX_MonthField)


def test_24():
    python_code_.bibTeX_YearField(
        year="_bibTeX_SeriesField__bibTeX_SeriesField bibTeX_UnknownField37"
    )


def test_25():
    python_code_.bibTeX_TitleField(title=b"[+a\x01}\x92\xc7\x1b\x15#\x98\x11l\x9b")


def test_26():
    var_22 = python_code_.bibTeX_BibtexEntryTypes()
    python_code_.bibTeX_TitleField(title=None, bibTeX_TitleField=var_22)


def test_27():
    python_code_.bibTeX_CiteKey(key=("ZCE\x0b\nBcAJ,lM", 237.15, ':&uk?fF":R'))


def test_28():
    var_22 = python_code_.bibTeX_BibtexEntryTypes()
    python_code_.bibTeX_CiteKey(key=complex(89.74, 2391.036), bibTeX_CiteKey=var_22)


def test_29():
    python_code_.bibTeX_NoteField(
        note="_bibTeX_NumberField__bibTeX_NumberField.bibTeX_Authors._bibTeX_VolumeField__bibTeX_VolumeField",
        bibTeX_NoteField=None,
    )


def test_30():
    var_0 = python_code_.bibTeX_NoteField(
        note=b"\xa0\xc9?\xfd\tL\x04\x88'$\x06\xc8\xc8",
        bibTeX_NoteField=b"\xb0y\xc5\xe1\x89",
    )
    assert isinstance(var_0, python_code_.bibTeX_NoteField)


def test_31():
    python_code_.bibTeX_EditorField(editor=[False])


def test_32():
    python_code_.bibTeX_Article()


def test_33():
    var_25 = python_code_.bibTeX_YearField(year=None, bibTeX_YearField=1221)
    assert isinstance(var_25, python_code_.bibTeX_YearField)


def test_34():
    var_24 = python_code_.bibTeX_NumberField(number="|E", bibTeX_NumberField=1)
    assert isinstance(var_24, python_code_.bibTeX_NumberField)


def test_35():
    var_32 = python_code_.bibTeX_AddressField(
        address="", bibTeX_AddressField={"tynF\nib\x0cOWX": False}
    )
    assert isinstance(var_32, python_code_.bibTeX_AddressField)
