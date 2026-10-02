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
    annotations,
    date,
    datetime,
    marketing_Product,
    marketing_Review,
    system_Category,
    time,
    user_Address,
    user_Business,
    user_Provider,
    user_Tags,
    user_User,
)


def test_0():
    python_code_.system_Category(
        id="'E",
        section="`df2ijc.\tT6k%}ssQK=",
        name="T1:vMzb,9f09_",
        parent=None,
        icon=";vZS/c",
    )


def test_1():
    python_code_.user_Tags(id="Vk|GN+S4\n/&", name="q3!3WW")


def test_2():
    python_code_.marketing_Review(
        id="M", product=None, user=None, rating="pi>J2?ul_s|oi|F", description="U.\x0b"
    )


def test_3():
    var_0 = "kZmG;\tC9 k?V<6v=\x0c`U"
    var_1 = python_code_.user_Tags(id={"`3HSa\rJ4nP4sux": True}, name=var_0)
    var_2 = "N+s:.\x0cWp "
    var_3 = "w@p8Ahw[hh0\n'EBRj:"
    var_4 = python_code_.user_Tags
    var_5 = python_code_.marketing_Review(
        id=var_4, product=var_2, user=var_0, rating=None, description=var_4
    )
    var_6 = python_code_.marketing_Product(
        id=var_3,
        busId=var_4,
        name=var_1,
        ccategory=var_4,
        price=var_2,
        active=set(),
        created=3465.99,
        expires=var_0,
        reviews=var_5,
    )
    python_code_.user_Business(
        avgRatings=(False, "?\x0c7s!&2", -2092.92),
        tags=var_1,
        id=var_0,
        name={-1791, True},
        category=var_2,
        website=var_3,
        email=var_3,
        phone=var_3,
        address=complex(1259.097381, -1076.39862),
        adminUser=complex(-2373.8366, -470.55),
        staffUsers=-1394.33,
        products=var_6,
    )


def test_4():
    python_code_.user_Provider(
        uid=False, providerId=(), displayName={-762.97, 1164}, email=-1941, photoURL=[]
    )


def test_5():
    var_0 = "aO\toy; "
    var_1 = '#8?jY"caMY'
    var_2 = "%^4M\\@pZ\tk9I"
    python_code_.system_Category(
        id=var_0, section=var_1, name=var_2, parent=b"\xf7", icon=var_1
    )
    var_4 = "nu!SE$+%I7f#/{]S7q<"
    var_5 = bool
    var_6 = "9*-g:$5[)4+):),i\x0b"
    python_code_.marketing_Review(
        id=var_4,
        product=var_5,
        user={"p)oc": 1356, "c*Arb": True},
        rating={},
        description=var_6,
    )
    python_code_.user_Address(
        state=var_5, postcode=var_0, country=var_5, street=var_1, suburb=var_2
    )
    var_9 = "\x0b;W6A%N 4sgeWic"
    python_code_.user_Tags(id=var_6, name=var_9)


def test_6():
    var_0 = "sK>\r96/0)e0,l4:%-e"
    var_1 = lambda *args, **kwargs: 1708
    var_2 = 'V6?0"\rr^!HW~Vv1%'
    var_3 = python_code_.user_Address
    var_4 = "R1nL\x0c3x"
    var_5 = lambda *args, **kwargs: -1753
    var_6 = "gJb"
    var_7 = python_code_.user_Address(
        state=var_0, postcode=var_1, country=var_4, street=var_5, suburb=var_6
    )
    var_8 = "{ZA EqN"
    var_9 = abs
    var_10 = python_code_.system_Category(
        id=var_6, section=var_3, name=var_0, parent=var_9, icon=var_4
    )
    var_11 = python_code_.system_Category(
        id=var_1, section=var_8, name=var_5, parent=var_10, icon=var_7
    )
    var_12 = python_code_.marketing_Review(
        id="'",
        product=['F(ygz/NV`7aEit"5O', False],
        user=var_11,
        rating=var_7,
        description=var_4,
    )
    python_code_.user_User(
        id=False,
        fiirstName={},
        lastName={True},
        email=var_0,
        phone=var_1,
        displayName=var_2,
        photoURL=var_3,
        address=var_7,
        provider=var_2,
        interests=var_10,
        wishlist=var_5,
        purchaseHistory=var_0,
        reviews=var_12,
        business=var_0,
    )
    var_14 = python_code_.system_Category(
        id=(-2738, False), section=var_2, name=var_8, parent=var_11, icon=False
    )
    python_code_.user_Provider(
        uid={False, -3444.17, '\r\x0b&M/D+x="}\t'},
        providerId=var_14,
        displayName=var_14,
        email=var_3,
        photoURL=var_8,
    )
