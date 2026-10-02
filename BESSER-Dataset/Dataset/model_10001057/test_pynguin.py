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
    Agenda,
    Contacto,
    Direccion,
    Foto,
    Telefono,
    annotations,
    date,
    datetime,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_0 = python_code_.Contacto(
        nombre="contacto10",
        email="direccionPrincipal3,Direccion,Foto,contacto6",
        agenda1=None,
    )
    var_3 = -1348
    python_code_.Foto(
        alto=var_3,
        ancho={
            "nd3_\x0bk'Gew\\iCx1jeQ": 1,
            "/xl2": ".\txj",
            "contacto8._Contacto__telefonoAlternativo9._Contacto__direccionPrincipal3": "contacto2",
        },
        contacto10=var_0,
    )


def test_1():
    python_code_.Foto(alto=-1201.9, ancho=complex(857.0, 1635.16))


def test_2():
    var_48 = python_code_.Agenda(Introduccion="w ZV")
    assert isinstance(var_48, python_code_.Agenda)
    var_65 = "telefonoPrincipal7 Telefono"
    var_66 = python_code_.Contacto(
        nombre=b"\xed\x0f\r\xc9\x13\x06\xe85\x9d\xb0\xdd\xfb\x00\xc1\x9d\x0b\xef\xcb",
        email=var_65,
        agenda1=var_48,
        telefonoPrincipal7=620,
    )
    assert isinstance(var_66, python_code_.Contacto)
    var_67 = {var_66, var_66}
    python_code_.Agenda(Introduccion=var_65, contacto0=var_67)
    var_69 = (
        lambda *args, **kwargs: "_Telefono__contacto6:_Contacto__foto11:direccionPrincipal3:Telefono"
    )
    python_code_.Foto(alto=b"\x8ay", ancho=var_66, contacto10=var_69)


def test_3():
    var_0 = python_code_.Contacto(
        nombre="_Agenda__contacto0.Direccion.direccionAlternativa5",
        email="qM\r=",
        direccionAlternativa5=None,
        telefonoAlternativo9=None,
    )
    var_48 = 1
    var_49 = 198
    python_code_.Telefono(codigo=var_48, prefijo=var_49, numero=var_0)


def test_4():
    var_1 = dict
    python_code_.Foto(alto=(), ancho=var_1)
    var_12 = 3
    var_44 = python_code_.Telefono(
        codigo=(887.41,),
        prefijo={"TelefonoContactofoto11", False},
        numero=var_12,
        contacto6=var_12,
    )
    assert var_44.contacto6 == 3


@pytest.mark.xfail(strict=True)
def test_5():
    var_1 = "U[6^.%C|bTM\\AUB"
    var_2 = 1199
    var_6 = python_code_.Contacto(nombre="o\\;rcrHl", email=var_1, foto11=var_1)
    assert isinstance(var_6, python_code_.Contacto)
    python_code_.Telefono(codigo=var_2, prefijo=var_2, numero=var_2, contacto8=var_6)
    assert isinstance(var_6.telefonoAlternativo9, python_code_.Telefono)


@pytest.mark.xfail(strict=True)
def test_6():
    var_0 = python_code_.Foto(alto=1993, ancho=-416)
    var_1 = "U[6^.%C|bTM\\AUB"
    var_5 = 2
    var_6 = ")!&Cq#qW7;="
    var_7 = python_code_.Foto(alto=var_5, ancho=var_5, contacto10=var_5)
    assert isinstance(var_7, python_code_.Foto)
    var_9 = python_code_.Telefono(
        codigo=var_0, prefijo=[1, 3], numero=var_1, contacto8=var_6
    )
    assert isinstance(var_9, python_code_.Telefono)
    python_code_.Contacto(nombre=var_6, email=var_6, foto11=var_7)


@pytest.mark.xfail(strict=True)
def test_7():
    var_0 = python_code_.Contacto(
        nombre="_Contacto__telefonoPrincipal7",
        email="_Foto__contacto10:telefonoPrincipal7",
        agenda1=None,
        direccionAlternativa5=None,
        foto11=None,
    )
    var_49 = "telefonoPrincipal7contacto2_Telefono__contacto6"
    var_50 = lambda *args, **kwargs: "_Contacto__agenda1"
    var_51 = "Telefono telefonoPrincipal7 _Foto__contacto10 _Agenda__contacto0"
    python_code_.Direccion(
        nombre=var_49, codigo=None, ciudad=var_50, pais=var_51, contacto4=var_0
    )
    assert isinstance(var_0.direccionAlternativa5, python_code_.Direccion)


@pytest.mark.xfail(strict=True)
def test_8():
    var_0 = python_code_.Contacto(
        nombre="7\rZ*/S?_6y|Cj;!q>)",
        email="zGQ\r\\c=EH.tR L<o\\S)",
        direccionAlternativa5=None,
        telefonoAlternativo9=None,
        foto11=None,
    )
    var_50 = "contacto10"
    var_51 = python_code_.Agenda(Introduccion=var_50, contacto0=var_50)
    assert isinstance(var_51, python_code_.Agenda)
    var_52 = "D&\tM\r^%[U-"
    var_53 = python_code_.Direccion
    var_54 = python_code_.Direccion(
        nombre=var_52, codigo=var_53, ciudad=None, pais=var_50
    )
    var_55 = 3
    var_56 = python_code_.Foto(alto=var_55, ancho=var_53, contacto10=var_53)
    python_code_.Contacto(
        nombre=var_0,
        email=var_50,
        agenda1=var_51,
        direccionPrincipal3=var_54,
        foto11=var_56,
    )


@pytest.mark.xfail(strict=True)
def test_9():
    var_0 = python_code_.Foto(alto=1993, ancho=-416)
    var_1 = "U[6^.%C|bTM\\AUB"
    var_2 = 1225
    var_3 = python_code_.Contacto(
        nombre="bNFH",
        email="contacto8.Telefono._Contacto__agenda1",
        direccionPrincipal3=var_0,
    )
    python_code_.Direccion(
        nombre=var_1, codigo=var_2, ciudad=False, pais=2543, contacto4=var_3
    )
    assert isinstance(var_3.direccionAlternativa5, python_code_.Direccion)


@pytest.mark.xfail(strict=True)
def test_10():
    var_0 = python_code_.Contacto(
        nombre="_Contacto__direccionPrincipal3._Agenda__contacto0.contacto6._Contacto__direccionAlternativa5",
        email="_Contacto__agenda1_Agenda__contacto0",
        agenda1=None,
        direccionAlternativa5=None,
        foto11=None,
    )
    var_51 = "direccionAlternativa5Foto_Foto__contacto10telefonoPrincipal7"
    var_52 = lambda *args, **kwargs: [1827.57, False]
    python_code_.Direccion(
        nombre=var_51,
        codigo=(False, -762, False),
        ciudad=var_52,
        pais=var_0,
        contacto2=var_0,
    )


def test_11():
    python_code_.Contacto(
        nombre="_Contacto__direccionPrincipal3._Agenda__contacto0.contacto6._Contacto__direccionAlternativa5",
        email="_Contacto__agenda1_Agenda__contacto0",
        agenda1=None,
        direccionAlternativa5=None,
        foto11=None,
    )


def test_12():
    var_0 = ""
    var_1 = python_code_.Direccion(nombre=None, codigo=389.63, ciudad=var_0, pais=var_0)
    var_2 = lambda *args, **kwargs: "telefonoAlternativo9"
    var_3 = 'b\n m"tb$GJ0n>'
    python_code_.Contacto(nombre=var_0, email=[False])
    var_6 = python_code_.Agenda(Introduccion=var_1)
    assert isinstance(var_6, python_code_.Agenda)
    var_11 = ' J5lN75"d@d;&'
    var_12 = python_code_.Contacto(
        nombre=var_11,
        email=var_6,
        agenda1=var_2,
        direccionAlternativa5=var_3,
        foto11=None,
    )
    assert var_12.direccionAlternativa5 == 'b\n m"tb$GJ0n>'


def test_13():
    var_48 = python_code_.Agenda(Introduccion="G1n,}vTZZf3.FnT")
    assert isinstance(var_48, python_code_.Agenda)
    var_70 = ";;a)A.G(_~"
    var_71 = abs
    var_72 = python_code_.Contacto(
        nombre={
            "_Contacto__agenda1:direccionAlternativa5:contacto6:_Contacto__foto11",
            False,
        },
        email=var_70,
        agenda1=var_48,
        foto11=var_71,
    )
    assert isinstance(var_72, python_code_.Contacto)


def test_14():
    var_52 = python_code_.Contacto(
        nombre=complex(-2206.2, -2452.96), email=set(), agenda1=()
    )
    assert isinstance(var_52, python_code_.Contacto)


def test_15():
    var_0 = python_code_.Contacto(
        nombre=2799.36, email=[], direccionPrincipal3=(207.34,)
    )
    assert isinstance(var_0, python_code_.Contacto)


def test_16():
    var_48 = python_code_.Agenda(Introduccion="zn]rq")
    assert isinstance(var_48, python_code_.Agenda)
    var_68 = "_Contacto__direccionPrincipal3 Foto contacto6"
    var_69 = python_code_.Direccion
    var_70 = python_code_.Contacto(
        nombre=var_68, email=var_69, agenda1=var_69, telefonoAlternativo9=var_68
    )
    assert (
        var_70.telefonoAlternativo9 == "_Contacto__direccionPrincipal3 Foto contacto6"
    )
    var_71 = 1530
    python_code_.Foto(alto=var_69, ancho=var_71)
    var_73 = {var_70}
    var_74 = python_code_.Agenda(Introduccion=var_68, contacto0=var_73)
    assert isinstance(var_74, python_code_.Agenda)


def test_17():
    var_6 = python_code_.Contacto(
        nombre=True,
        email=b"\xfbzT\xae",
        telefonoPrincipal7=b">\xfa\xfd.\xc9\xc0",
        telefonoAlternativo9=-1750,
    )
    assert var_6.telefonoAlternativo9 == -1750


def test_18():
    var_48 = python_code_.Agenda(Introduccion="/ELilt", contacto0=set())
    assert isinstance(var_48, python_code_.Agenda)


def test_19():
    var_48 = python_code_.Agenda(Introduccion="foto11,contacto10")
    assert isinstance(var_48, python_code_.Agenda)


@pytest.mark.xfail(strict=True)
def test_20():
    python_code_.Contacto(
        nombre="_Contacto__telefonoPrincipal7",
        email="_Foto__contacto10:telefonoPrincipal7",
        agenda1=None,
        direccionAlternativa5=None,
        foto11=None,
    )
    var_49 = "\thHq31CG8q.&nVT "
    var_50 = 2479
    var_51 = len
    var_52 = python_code_.Direccion(
        nombre=var_49,
        codigo=var_50,
        ciudad=var_51,
        pais=b"a\x93\xef\xde\x00!\xf8\x9d`k<",
        contacto4=var_51,
    )
    assert isinstance(var_52, python_code_.Direccion)
    python_code_.Contacto(
        nombre=var_49, email=var_49, direccionAlternativa5=var_52, telefonoPrincipal7={}
    )


@pytest.mark.xfail(strict=True)
def test_21():
    var_51 = "direc8ionAlternativa5Foto_Foto__contacto10telefonoPrincipal7"
    var_54 = "_rontacto__direccionPrincipal3,_Contacto__telefonoPrincipal7,contacto8,Contacto"
    var_55 = python_code_.Agenda(Introduccion=var_54)
    assert isinstance(var_55, python_code_.Agenda)
    var_58 = bool
    var_59 = python_code_.Contacto(
        nombre=[-346.57, 215.59, 2881.99], email=var_54, agenda1=var_55, foto11=var_58
    )
    assert isinstance(var_59, python_code_.Contacto)
    var_60 = (
        "_Telefono__contacto6,_Contacto__direccionAlternativa5,_Contacto__foto11,Foto"
    )
    var_61 = "TH/-6-Z@\x0c[(o$AtO~3q"
    var_62 = python_code_.Direccion(
        nombre=var_51, codigo=var_51, ciudad=-3484.37, pais=var_61, contacto2=var_58
    )
    assert isinstance(var_62, python_code_.Direccion)
    var_63 = python_code_.Telefono(codigo=var_58, prefijo=var_60, numero=1246)
    python_code_.Contacto(
        nombre=var_60,
        email=complex(2417.3, -3192.23494),
        direccionPrincipal3=var_62,
        telefonoAlternativo9=var_63,
    )
    assert isinstance(var_62.contacto2, python_code_.Contacto)


@pytest.mark.xfail(strict=True)
def test_22():
    var_0 = ""
    var_1 = python_code_.Direccion(nombre=None, codigo=389.63, ciudad=var_0, pais=var_0)
    var_2 = lambda *args, **kwargs: "telefonoAlternativo9"
    var_3 = 'b\n m"tb$GJ0n>'
    var_5 = python_code_.Contacto(
        nombre="\r%,(W`JhQ1",
        email=var_0,
        agenda1=var_1,
        direccionAlternativa5=None,
        telefonoAlternativo9=var_2,
        foto11=var_3,
    )
    assert isinstance(var_5, python_code_.Contacto)
    var_6 = python_code_.Agenda(Introduccion=var_1)
    assert isinstance(var_6, python_code_.Agenda)
    python_code_.Foto(alto=var_2, ancho=[-2416.73, -1828.97], contacto10=var_5)


def test_23():
    var_48 = python_code_.Agenda(Introduccion='z:2@@\x0bNB"8Hkkc', contacto0=set())
    assert isinstance(var_48, python_code_.Agenda)
    var_59 = lambda *args, **kwargs: 2
    var_60 = python_code_.Contacto(
        nombre=var_59, email=var_59, agenda1=var_48, telefonoPrincipal7=var_48
    )
    assert isinstance(var_60, python_code_.Contacto)


@pytest.mark.xfail(strict=True)
def test_24():
    var_0 = python_code_.Contacto(
        nombre="_Contacto__direccionPrincipal3._Agenda__contacto0.contacto6._Contacto__direccionAlternativa5",
        email="_Contacto__agenda1_Agenda__contacto0",
        agenda1=None,
        direccionAlternativa5=None,
        foto11=None,
    )
    var_51 = -950
    python_code_.Telefono(codigo=set(), prefijo=var_51, numero=var_51, contacto6=var_0)


@pytest.mark.xfail(strict=True)
def test_25():
    var_1 = dict
    var_3 = python_code_.Foto(alto=(), ancho=var_1)
    var_8 = "DB )hPg"
    var_47 = -2826
    var_50 = python_code_.Telefono(
        codigo=(887.41,),
        prefijo={"TelefonoContactofoto11", False},
        numero=var_47,
        contacto6=var_47,
    )
    assert isinstance(var_50, python_code_.Telefono)
    python_code_.Contacto(nombre=var_8, email=var_3, telefonoPrincipal7=var_50)
    assert isinstance(var_50.contacto6, python_code_.Contacto)


@pytest.mark.xfail(strict=True)
def test_26():
    var_48 = python_code_.Agenda(Introduccion="w ZV")
    assert isinstance(var_48, python_code_.Agenda)
    var_69 = "telefonoPrincipal7 Telefono"
    var_70 = python_code_.Contacto(
        nombre=b"\xed\x0f\r\xc9\x13\x06\xe85\x9d\xb0\xdd\xfb\x00\xc1\x9d\x0b\xef\xcb",
        email=var_69,
        agenda1=var_48,
        telefonoPrincipal7=620,
    )
    assert isinstance(var_70, python_code_.Contacto)
    var_71 = {var_70, var_70}
    python_code_.Agenda(Introduccion="Foto:_Contacto__foto11", contacto0=var_71)
    var_73 = python_code_.Contacto(
        nombre="\t`wJ@u+=9", email=var_69, direccionPrincipal3=[True, 1]
    )
    assert isinstance(var_73, python_code_.Contacto)
    var_74 = -330
    var_75 = complex
    var_76 = python_code_.Telefono(
        codigo=(
            True,
            "contacto2-telefonoPrincipal7-_Contacto__agenda1-contacto4",
            -3025.04,
        ),
        prefijo=var_74,
        numero=var_75,
        contacto6=(),
        contacto8=(),
    )
    assert isinstance(var_76, python_code_.Telefono)
    python_code_.Contacto(
        nombre=var_69,
        email=var_69,
        telefonoPrincipal7=var_76,
        telefonoAlternativo9=complex(-1794.251, -774.440804),
    )
    assert isinstance(var_76.contacto6, python_code_.Contacto)


@pytest.mark.xfail(strict=True)
def test_27():
    python_code_.Contacto(
        nombre="_Contacto__direccionPrincipal3._Agenda__contacto0.contacto6._Contacto__direccionAlternativa5",
        email="_Contacto__agenda1_Agenda__contacto0",
        agenda1=None,
        direccionAlternativa5=None,
        foto11=None,
    )
    var_52 = "VU9g=\x0b}<3acT\x0b"
    var_56 = -2826
    var_58 = python_code_.Agenda(Introduccion=var_52)
    assert isinstance(var_58, python_code_.Agenda)
    var_59 = "Wu]6?Xp$n\r]B;)\x0bd"
    var_60 = 2964
    var_61 = 0
    var_62 = python_code_.Telefono(
        codigo=var_60, prefijo=var_58, numero=var_61, contacto8=True
    )
    assert isinstance(var_62, python_code_.Telefono)
    python_code_.Contacto(
        nombre=var_52,
        email=var_59,
        agenda1=var_56,
        telefonoAlternativo9=var_62,
        foto11=None,
    )


def test_28():
    var_0 = "contacto6"
    python_code_.Direccion(nombre=var_0, codigo=var_0, ciudad=var_0, pais=None)
    var_2 = "(<\x0b6\\K?U{(BU/5O"
    var_3 = hash
    var_5 = -563
    var_6 = python_code_.Foto(alto=var_5, ancho=var_2, contacto10=var_5)
    assert isinstance(var_6, python_code_.Foto)
    python_code_.Telefono(
        codigo={"\ruY", -3552.22, "iL\t=io&2Jeul-"},
        prefijo=var_3,
        numero=complex(-273.3, 1914.8846617),
    )
    python_code_.Foto(alto=var_5, ancho=var_5)
    var_9 = python_code_.Contacto(
        nombre=var_3,
        email=[1856, 3201],
        telefonoPrincipal7=[],
        telefonoAlternativo9="_Direccion__contacto4",
    )
    assert var_9.telefonoAlternativo9 == "_Direccion__contacto4"


def test_29():
    var_48 = python_code_.Agenda(
        Introduccion="telefonoAlternativo9_Contacto__foto11_Contacto__telefonoPrincipal7",
        contacto0={True, False},
    )
    assert isinstance(var_48, python_code_.Agenda)
    var_65 = "telefonoPrincipal7 Telefono"
    var_66 = python_code_.Contacto(
        nombre=b"\xed\x0f\r\xc9\x13\x06\xe85\x9d\xb0\xdd\xfb\x00\xc1\x9d\x0b\xef\xcb",
        email=var_65,
        agenda1=var_48,
        telefonoPrincipal7=620,
    )
    assert isinstance(var_66, python_code_.Contacto)
    var_67 = {var_66, var_66}
    python_code_.Agenda(Introduccion=var_65, contacto0=var_67)


def test_30():
    var_0 = python_code_.Contacto(
        nombre="_Contacto__telefonoPrincipal7",
        email="_Foto__contacto10:telefonoPrincipal7",
        agenda1=None,
        direccionAlternativa5=None,
        foto11=None,
    )
    var_55 = {var_0, var_0, var_0, var_0}
    var_56 = python_code_.Agenda(Introduccion=var_0, contacto0=var_55)
    assert isinstance(var_56, python_code_.Agenda)


@pytest.mark.xfail(strict=True)
def test_31():
    var_0 = python_code_.Foto(alto=1993, ancho=-416)
    var_1 = "_Contacto__foto11"
    var_2 = 1225
    var_3 = python_code_.Contacto(
        nombre="bNFH",
        email="contacto8.Telefono._Contacto__agenda1",
        direccionPrincipal3=var_0,
    )
    python_code_.Direccion(
        nombre=var_1, codigo=var_2, ciudad=False, pais=2543, contacto4=var_3
    )
    assert isinstance(var_3.direccionAlternativa5, python_code_.Direccion)
    var_10 = lambda *args, **kwargs: True
    var_11 = python_code_.Direccion(
        nombre=var_10,
        codigo=var_3,
        ciudad=False,
        pais=var_1,
        contacto2=var_3,
        contacto4=var_10,
    )
    assert isinstance(var_11, python_code_.Direccion)


@pytest.mark.xfail(strict=True)
def test_32():
    python_code_.Foto(alto=3, ancho=575, contacto10=None)
    var_1 = "U[6^.%C|bTM\\AU?"
    var_5 = 3
    var_6 = -1479
    var_7 = python_code_.Contacto(
        nombre=var_1,
        email={1896, "h]y=Z;`LYa%wzz7"},
        telefonoAlternativo9=(),
        foto11=var_6,
    )
    assert var_7.telefonoAlternativo9 == ()
    var_9 = "qCT\n\r#sK2k-'5V="
    var_10 = python_code_.Agenda
    var_11 = python_code_.Telefono(
        codigo=var_6, prefijo=var_6, numero=b"\x03\xa4TnX\xe5\xee", contacto8=var_10
    )
    python_code_.Contacto(
        nombre=var_1,
        email=var_9,
        direccionPrincipal3={},
        direccionAlternativa5=var_10,
        telefonoPrincipal7=var_11,
        foto11=True,
    )
    assert isinstance(var_11.contacto6, python_code_.Contacto)
    var_8 = python_code_.Telefono(
        codigo=var_5, prefijo=var_5, numero=var_6, contacto6=var_7, contacto8=var_7
    )
    assert isinstance(var_8, python_code_.Telefono)
