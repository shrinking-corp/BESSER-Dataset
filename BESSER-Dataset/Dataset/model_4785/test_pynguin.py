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
    ABC,
    Feature,
    NamedElement,
    PackageMember,
    ParameterizedType,
    PrimitiveType,
    Type,
    TypedElement,
    abstractmethod,
    date,
    datetime,
    time,
    types_ComplexType,
    types_EnumerationType,
    types_Enumerator,
    types_Event,
    types_Feature,
    types_Operation,
    types_Package,
    types_PackageMember,
    types_Parameter,
    types_ParameterizedType,
    types_PrimitiveType,
    types_Property,
    types_Type,
    types_TypeConstraint,
    types_TypeParameter,
    types_TypedElement,
)


def test_0():
    var_1 = python_code_.types_ComplexType(
        ComplexType=None, owningType=set(), types_ComplexType14=set()
    )
    assert isinstance(var_1, python_code_.types_ComplexType)


def test_1():
    var_1 = python_code_.types_ComplexType(types_ComplexType14=set())
    assert isinstance(var_1, python_code_.types_ComplexType)


def test_2():
    var_1 = python_code_.types_ComplexType()
    assert isinstance(var_1, python_code_.types_ComplexType)


def test_3():
    var_20 = python_code_.types_ComplexType(
        ComplexType=b"\x04\xf9\xbb\xde^\xb2\xbe3", types_ComplexType=[]
    )
    assert isinstance(var_20, python_code_.types_ComplexType)


def test_4():
    var_19 = python_code_.types_ComplexType(ComplexType=1019.31)
    assert isinstance(var_19, python_code_.types_ComplexType)


def test_5():
    var_24 = python_code_.types_Enumerator(
        literalValue=b"\xc8\xa6\xf4\xd2\xe0\x99\x1a\xa7Sr\xc1!"
    )
    assert isinstance(var_24, python_code_.types_Enumerator)


def test_6():
    var_38 = python_code_.types_Enumerator(
        literalValue={True, "7C#(~t&Fc", "Z\\`4%o4VuHvqB"}, Enumerator=-579.42
    )
    assert isinstance(var_38, python_code_.types_Enumerator)


def test_7():
    var_30 = "t;aks\ttp"
    var_31 = python_code_.types_Enumerator(literalValue=var_30, enumerator=("@[c",))
    assert isinstance(var_31, python_code_.types_Enumerator)


def test_8():
    var_15 = python_code_.types_TypeConstraint(value="Ik9J\nb=E8H }@hC'\rA")
    assert isinstance(var_15, python_code_.types_TypeConstraint)


def test_9():
    var_23 = python_code_.types_TypeConstraint(
        value=[], types_TypeConstraint=b"\xdc\xe3\xe3\x19\x15\xca\xed\xe8s\x13"
    )
    assert isinstance(var_23, python_code_.types_TypeConstraint)


def test_10():
    var_1 = python_code_.types_ComplexType()
    assert isinstance(var_1, python_code_.types_ComplexType)
    var_20 = python_code_.types_ComplexType(
        types_ComplexType=var_1, types_ComplexType14=()
    )
    assert isinstance(var_20, python_code_.types_ComplexType)


def test_11():
    var_29 = python_code_.types_ComplexType(ComplexType=None, types_ComplexType14=set())
    assert isinstance(var_29, python_code_.types_ComplexType)
    var_35 = python_code_.types_Enumerator(
        literalValue="_types_ComplexType__owningType_types_Enumerator__EnumeratorEnumerationTypetypes_ComplexType",
        Enumerator=var_29,
        enumerator=var_29,
    )
    assert isinstance(var_35, python_code_.types_Enumerator)
    var_29.getAllFeatures()


def test_12():
    var_1 = python_code_.types_ComplexType()
    assert isinstance(var_1, python_code_.types_ComplexType)
    var_20 = python_code_.types_ComplexType(
        types_ComplexType=var_1, types_ComplexType14=()
    )
    assert isinstance(var_20, python_code_.types_ComplexType)
    var_21 = python_code_.types_ComplexType(types_ComplexType=var_20)
    assert isinstance(var_21, python_code_.types_ComplexType)


def test_13():
    var_1 = python_code_.types_ComplexType(types_ComplexType14={-4131.22, 1300.91})
    assert isinstance(var_1, python_code_.types_ComplexType)
    var_22 = python_code_.types_ComplexType(types_ComplexType14={var_1, 2297.04})
    assert isinstance(var_22, python_code_.types_ComplexType)


def test_14():
    var_52 = python_code_.types_ComplexType(ComplexType=None, owningType=set())
    assert isinstance(var_52, python_code_.types_ComplexType)
    var_53 = python_code_.types_ComplexType(
        owningType={var_52, 1253.02, True}, types_ComplexType=var_52
    )
    assert isinstance(var_53, python_code_.types_ComplexType)
    var_54 = python_code_.types_ComplexType(
        owningType={var_53}, types_ComplexType14={"ew", True, var_53}
    )
    assert isinstance(var_54, python_code_.types_ComplexType)


def test_15():
    var_30 = python_code_.types_ComplexType(types_ComplexType=-275.9)
    assert isinstance(var_30, python_code_.types_ComplexType)
    var_32 = python_code_.types_ComplexType(types_ComplexType14={var_30, True})
    assert isinstance(var_32, python_code_.types_ComplexType)
    var_43 = python_code_.types_Enumerator(
        literalValue="_types_ComplexType__owningType_types_Enumerator__EnumeratorEnumerationTypetypes_ComplexType",
        Enumerator=var_32,
        enumerator=var_32,
    )
    assert isinstance(var_43, python_code_.types_Enumerator)
