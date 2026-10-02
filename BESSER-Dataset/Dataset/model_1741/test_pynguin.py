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
    Artifact,
    Device,
    DurationArtifact,
    Enum,
    MediaLibrary_Artifact,
    MediaLibrary_AudioBook,
    MediaLibrary_Computer,
    MediaLibrary_Device,
    MediaLibrary_DurationArtifact,
    MediaLibrary_EReader,
    MediaLibrary_Ebook,
    MediaLibrary_Ecosystem,
    MediaLibrary_ExternalSource,
    MediaLibrary_Image,
    MediaLibrary_Library,
    MediaLibrary_MediaCollection,
    MediaLibrary_MediaSource,
    MediaLibrary_MusicTrack,
    MediaLibrary_Smartphone,
    MediaLibrary_Store,
    MediaLibrary_Tablet,
    MediaLibrary_Video,
    MediaSource,
    SourceType,
    abstractmethod,
    date,
    datetime,
    time,
)


def test_0():
    var_16 = python_code_.MediaLibrary_MediaCollection(
        name='sM?8m{7?#"c"X`bR(',
        MediaLibrary_MediaCollection10=set(),
        collections={-1497.22, "!>B)>", 285.34},
        MediaCollection17=None,
    )
    assert isinstance(var_16, python_code_.MediaLibrary_MediaCollection)


def test_1():
    var_2 = python_code_.MediaLibrary_MediaCollection(name='"5k+W&\x0cd~b')
    assert isinstance(var_2, python_code_.MediaLibrary_MediaCollection)


def test_2():
    var_0 = python_code_.MediaLibrary_Device
    var_7 = python_code_.MediaLibrary_MediaCollection(
        name="AKBpE6KBV", hostOf=None, MediaCollection=None, MediaCollection17=var_0
    )
    assert isinstance(var_7, python_code_.MediaLibrary_MediaCollection)


def test_3():
    var_16 = python_code_.MediaLibrary_MediaCollection(
        name=1884, MediaLibrary_MediaCollection=-2.31
    )
    assert isinstance(var_16, python_code_.MediaLibrary_MediaCollection)


def test_4():
    var_0 = python_code_.MediaLibrary_Smartphone
    var_1 = python_code_.MediaLibrary_MediaCollection(
        name="xX:Q7]Q}>(sM", hostOf=var_0, MediaCollection=var_0, MediaCollection17=None
    )
    assert isinstance(var_1, python_code_.MediaLibrary_MediaCollection)


def test_5():
    var_20 = python_code_.MediaLibrary_MediaCollection(
        name={"GF<y6.J9;Mv)yA": 0}, hostOf=()
    )
    assert isinstance(var_20, python_code_.MediaLibrary_MediaCollection)


def test_6():
    var_53 = python_code_.MediaLibrary_Artifact(
        name="_MediaLibrary_MediaCollection__MediaLibrary_MediaCollection.MediaCollection17",
        author="",
    )
    assert isinstance(var_53, python_code_.MediaLibrary_Artifact)


def test_7():
    var_9 = "z/1f]LS"
    var_10 = python_code_.MediaLibrary_Artifact(
        name=complex(-555.0, 1340.524763), author=var_9, contents=var_9
    )
    assert isinstance(var_10, python_code_.MediaLibrary_Artifact)


def test_8():
    var_2 = python_code_.MediaLibrary_MediaCollection(
        name="_MediaLibrary_MediaCollection__MediaLibrary_MediaCollection-_MediaLibrary_Artifact__Artifact",
        MediaLibrary_MediaCollection10={2, False, "$oV54n"},
        collections={True, True},
        MediaCollection=None,
        MediaCollection17=None,
    )
    assert isinstance(var_2, python_code_.MediaLibrary_MediaCollection)
    var_10 = python_code_.MediaLibrary_Artifact(
        name="Aa-m?<!*(WD8F\t2b\x0c*",
        author="_-k?<kn-.6ae",
        MediaLibrary_Artifact=None,
        MediaLibrary_Artifact11=var_2,
    )
    assert isinstance(var_10, python_code_.MediaLibrary_Artifact)


def test_9():
    var_12 = "NrA5.7B(P{CD)yP"
    var_17 = python_code_.MediaLibrary_Artifact(
        name=var_12,
        author=var_12,
        MediaLibrary_Artifact=var_12,
        MediaLibrary_Artifact11=None,
    )
    assert isinstance(var_17, python_code_.MediaLibrary_Artifact)


def test_10():
    var_12 = "NrA5.7B(P{CD)yP"
    var_17 = python_code_.MediaLibrary_Artifact(
        name=var_12, author=var_12, MediaLibrary_Artifact=None, Artifact={}
    )
    assert isinstance(var_17, python_code_.MediaLibrary_Artifact)


def test_11():
    var_5 = python_code_.MediaLibrary_Device(
        MACAddress="lFBr[A}\x0c",
        resolutionWidth=210,
        resolutionHeight=-1702,
        Device14=None,
        host=set(),
    )
    assert isinstance(var_5, python_code_.MediaLibrary_Device)


def test_12():
    var_5 = python_code_.MediaLibrary_Device(
        MACAddress="collections MediaLibrary_Artifact MediaCollection17",
        resolutionWidth=-3,
        resolutionHeight=1484,
        Device=None,
    )
    assert isinstance(var_5, python_code_.MediaLibrary_Device)


def test_13():
    python_code_.MediaLibrary_Device(
        MACAddress="MediaLibrary_Ecosystem6-MediaLibrary_Artifact11-MediaLibrary_Ecosystem2",
        resolutionWidth=-38,
        resolutionHeight=-595,
        MediaLibrary_Device=None,
        Device=None,
        Device14=None,
        host={1, False, 1751.42},
        syncedDevices=set(),
    )
    assert isinstance(
        python_code_.MediaLibrary_Device.Device,
        python_code_.MediaLibrary_MediaCollection,
    )


def test_14():
    var_3 = 2117
    var_5 = python_code_.MediaLibrary_Device(
        MACAddress="{0\\rn-W,",
        resolutionWidth=-2613,
        resolutionHeight=-3006,
        MediaLibrary_Device=None,
        Device14=var_3,
        host=set(),
    )
    assert isinstance(var_5, python_code_.MediaLibrary_Device)


def test_15():
    var_3 = -10
    python_code_.MediaLibrary_Device(
        MACAddress="\\YC", resolutionWidth=-2782, resolutionHeight=var_3, host=set()
    )
    assert isinstance(
        python_code_.MediaLibrary_Device.Device,
        python_code_.MediaLibrary_MediaCollection,
    )


@pytest.mark.xfail(strict=True)
def test_16():
    var_3 = 0
    var_4 = lambda *args, **kwargs: ":v2wC*y.VQ/"
    python_code_.MediaLibrary_Device(
        MACAddress=(),
        resolutionWidth=var_3,
        resolutionHeight=var_3,
        Device=var_4,
        host=var_3,
    )


def test_17():
    var_2 = lambda *args, **kwargs: []
    var_4 = 0
    var_6 = python_code_.MediaLibrary_Smartphone()
    var_7 = "X."
    var_8 = python_code_.MediaLibrary_Device(
        MACAddress={0, False, False},
        resolutionWidth=var_4,
        resolutionHeight=var_4,
        MediaLibrary_Device=complex(907.69, -1678.7349),
        Device14=var_6,
    )
    assert isinstance(
        python_code_.MediaLibrary_Device.Device,
        python_code_.MediaLibrary_MediaCollection,
    )
    var_9 = python_code_.MediaLibrary_MediaCollection(
        name=var_7,
        MediaLibrary_MediaCollection10=set(),
        MediaCollection=var_8,
        MediaCollection17=var_8,
    )
    python_code_.MediaLibrary_Artifact(
        name=var_7, author=b"\xc2\xa4\xe7'#\xdfK\xaf5\xd6"
    )
    var_13 = 2
    var_32 = -1532
    var_33 = python_code_.MediaLibrary_Ecosystem()
    var_34 = {var_9, var_9, var_9, var_9, var_13}
    python_code_.MediaLibrary_Device(
        MACAddress=var_2,
        resolutionWidth=var_4,
        resolutionHeight=var_32,
        MediaLibrary_Device=var_33,
        syncedDevices=var_34,
    )


def test_18():
    var_25 = python_code_.MediaLibrary_Library(
        name="\n33a}m$X-^]0\nvap$", MediaLibrary_Library8={True}
    )
    assert isinstance(var_25, python_code_.MediaLibrary_Library)


def test_19():
    var_2 = python_code_.MediaLibrary_Library(name="F\r")
    assert isinstance(var_2, python_code_.MediaLibrary_Library)


def test_20():
    var_0 = python_code_.Device()
    var_1 = python_code_.MediaLibrary_MediaSource()
    var_3 = "\r/ "
    var_4 = "wuWtC-DzLs@G$|Z-3"
    var_5 = lambda *args, **kwargs: []
    var_6 = python_code_.MediaLibrary_Artifact(
        name=var_3,
        author=var_4,
        MediaLibrary_Artifact=var_5,
        MediaLibrary_Artifact11=var_0,
    )
    assert isinstance(var_6, python_code_.MediaLibrary_Artifact)
    var_7 = {var_6}
    var_8 = python_code_.MediaLibrary_MediaCollection(
        name=var_3, MediaLibrary_MediaCollection10=var_7, MediaCollection17=var_5
    )
    assert isinstance(var_8, python_code_.MediaLibrary_MediaCollection)
    var_9 = python_code_.MediaLibrary_Library(
        name=var_4, MediaLibrary_Library=var_5, MediaLibrary_Library8=[]
    )
    assert isinstance(var_9, python_code_.MediaLibrary_Library)
    var_10 = python_code_.MediaLibrary_MediaCollection(
        name=var_4, MediaLibrary_MediaCollection=var_9, hostOf=var_1
    )
    assert isinstance(var_10, python_code_.MediaLibrary_MediaCollection)
    var_11 = python_code_.MediaLibrary_MediaCollection(
        name={},
        MediaLibrary_MediaCollection=var_5,
        MediaLibrary_MediaCollection10=set(),
        MediaCollection17=var_0,
    )
    var_12 = {var_8, var_8, var_10, var_11}
    var_13 = python_code_.MediaLibrary_Library(name=var_3, MediaLibrary_Library8=var_12)
    assert isinstance(var_13, python_code_.MediaLibrary_Library)


def test_21():
    var_6 = python_code_.MediaLibrary_Store(
        name='_S\t]g "VB4', url="MediaLibrary_LibraryMediaLibrary_Library"
    )
    assert isinstance(var_6, python_code_.MediaLibrary_Store)


def test_22():
    var_6 = python_code_.MediaLibrary_ExternalSource(
        sourceType=b"Ge\xc31Q#\x02\x9e\x85|\xd6\xa4%\xf0"
    )
    assert isinstance(var_6, python_code_.MediaLibrary_ExternalSource)


def test_23():
    var_54 = python_code_.MediaLibrary_Video(fps="MediaCollection17")
    assert isinstance(var_54, python_code_.MediaLibrary_Video)


def test_24():
    var_21 = python_code_.MediaLibrary_MusicTrack(label=None)
    assert isinstance(var_21, python_code_.MediaLibrary_MusicTrack)


def test_25():
    var_27 = python_code_.MediaLibrary_AudioBook(
        currentPosition={'8c$J"$==Xx<H1Pt': -531}
    )
    assert isinstance(var_27, python_code_.MediaLibrary_AudioBook)


def test_26():
    var_13 = python_code_.MediaLibrary_Image(dateTaken=True)
    assert isinstance(var_13, python_code_.MediaLibrary_Image)


def test_27():
    var_7 = python_code_.MediaLibrary_Ebook(pages=5961)
    assert isinstance(var_7, python_code_.MediaLibrary_Ebook)


def test_28():
    var_12 = python_code_.MediaLibrary_DurationArtifact(duration=None)
    assert isinstance(var_12, python_code_.MediaLibrary_DurationArtifact)


def test_29():
    var_18 = python_code_.MediaLibrary_EReader(
        videoEnabled="ykmqNx~2&o*X", audioEnabled="wUttzKxe('w"
    )
    assert isinstance(var_18, python_code_.MediaLibrary_EReader)


def test_30():
    var_16 = python_code_.MediaLibrary_MediaCollection(
        name=1884, MediaLibrary_MediaCollection=-2.31
    )
    assert isinstance(var_16, python_code_.MediaLibrary_MediaCollection)
    var_17 = {var_16}
    var_18 = python_code_.MediaLibrary_Library(name=(), MediaLibrary_Library8=var_17)
    assert isinstance(var_18, python_code_.MediaLibrary_Library)


def test_31():
    var_5 = python_code_.MediaLibrary_Device(
        MACAddress="})<'iEyi\"\n[.\\D~h(O",
        resolutionWidth=1250,
        resolutionHeight=1706,
        MediaLibrary_Device=None,
    )
    assert isinstance(
        python_code_.MediaLibrary_Device.Device,
        python_code_.MediaLibrary_MediaCollection,
    )
    python_code_.MediaLibrary_MediaCollection(
        name="<*",
        MediaLibrary_MediaCollection10={True, 1, -1816.33},
        collections={True, var_5},
    )


def test_32():
    var_4 = "\x0bhR\\(,<7k|n"
    var_5 = python_code_.MediaLibrary_MediaCollection(
        name=var_4,
        MediaCollection17={
            "MediaCollection17": True,
            "CD-MediaCollection17": -2747.0,
            ":>": True,
        },
    )
    assert isinstance(var_5, python_code_.MediaLibrary_MediaCollection)


def test_33():
    var_0 = python_code_.MediaLibrary_Library
    var_9 = python_code_.MediaLibrary_MediaCollection(
        name='U\nz}/6"{gpOm1C',
        MediaLibrary_MediaCollection=var_0,
        MediaLibrary_MediaCollection10=set(),
    )
    assert isinstance(var_9, python_code_.MediaLibrary_MediaCollection)


def test_34():
    var_0 = python_code_.MediaLibrary_Smartphone
    var_1 = python_code_.MediaLibrary_MediaCollection(
        name="xX:Q7]Q}>(sM", hostOf=var_0, MediaCollection=var_0, MediaCollection17=None
    )
    assert isinstance(var_1, python_code_.MediaLibrary_MediaCollection)
    python_code_.MediaLibrary_Device(
        MACAddress="CD,MediaLibrary_Artifact11,_MediaLibrary_MediaCollection__MediaLibrary_MediaCollection10,_MediaLibrary_Artifact__MediaLibrary_Artifact",
        resolutionWidth=1339,
        resolutionHeight=-335,
        Device=var_1,
        host={var_1},
    )
    assert isinstance(
        python_code_.MediaLibrary_Device.Device,
        python_code_.MediaLibrary_MediaCollection,
    )


def test_35():
    var_0 = python_code_.MediaLibrary_Smartphone
    var_1 = python_code_.MediaLibrary_MediaCollection(
        name="xX:Q7]Q}>(sM", hostOf=var_0, MediaCollection=var_0, MediaCollection17=None
    )
    assert isinstance(var_1, python_code_.MediaLibrary_MediaCollection)
    python_code_.MediaLibrary_Device(
        MACAddress="CD,MediaLibrary_Artifact11,_MediaLibrary_MediaCollection__MediaLibrary_MediaCollection10,_MediaLibrary_Artifact__MediaLibrary_Artifact",
        resolutionWidth=1339,
        resolutionHeight=-335,
        Device=var_1,
        host={var_1},
    )


def test_36():
    var_0 = python_code_.MediaLibrary_Device
    var_1 = python_code_.MediaLibrary_MediaCollection(
        name="xX:Q7]Q}>(sM", hostOf=var_0, MediaCollection=var_0, MediaCollection17=None
    )
    assert isinstance(var_1, python_code_.MediaLibrary_MediaCollection)


def test_37():
    var_12 = "Nr>A\x0c.7B(P{CD)yP"
    var_17 = python_code_.MediaLibrary_Artifact(
        name="MediaLibrary_MediaSourceMediaLibrary_Artifact11MediaLibrary_Library8_MediaLibrary_MediaCollection__MediaLibrary_MediaCollection",
        author=var_12,
        MediaLibrary_Artifact=var_12,
        MediaLibrary_Artifact11=var_12,
        Artifact=var_12,
    )
    assert isinstance(var_17, python_code_.MediaLibrary_Artifact)


@pytest.mark.xfail(strict=True)
def test_38():
    var_15 = 1080
    var_16 = -1369
    var_17 = list
    var_18 = python_code_.MediaLibrary_Device(
        MACAddress=[False, True, 2199],
        resolutionWidth=var_15,
        resolutionHeight=var_16,
        MediaLibrary_Device=var_17,
    )
    assert isinstance(var_18, python_code_.MediaLibrary_Device)
    var_19 = python_code_.MediaSource()
    var_22 = python_code_.MediaLibrary_MediaCollection(
        name=var_18, MediaCollection=var_17
    )
    assert isinstance(var_22, python_code_.MediaLibrary_MediaCollection)
    var_23 = python_code_.MediaLibrary_Artifact(
        name=True,
        author=var_18,
        MediaLibrary_Artifact=var_17,
        MediaLibrary_Artifact11=var_22,
    )
    assert isinstance(var_23, python_code_.MediaLibrary_Artifact)
    var_24 = {var_23, var_23}
    python_code_.MediaLibrary_MediaCollection(
        name={},
        MediaLibrary_MediaCollection10=var_24,
        hostOf=var_18,
        collections=1030.99,
        MediaCollection=var_19,
    )


def test_39():
    var_5 = python_code_.MediaLibrary_Device(
        MACAddress="Vn=/",
        resolutionWidth=-2188,
        resolutionHeight=3,
        MediaLibrary_Device=None,
    )
    assert isinstance(var_5, python_code_.MediaLibrary_Device)
    assert isinstance(
        python_code_.MediaLibrary_Device.Device,
        python_code_.MediaLibrary_MediaCollection,
    )
    var_7 = python_code_.MediaLibrary_MediaCollection(
        name=3023, MediaCollection17=var_5
    )
    assert isinstance(var_7, python_code_.MediaLibrary_MediaCollection)


def test_40():
    var_64 = python_code_.MediaLibrary_MediaCollection(
        name=1884, MediaLibrary_MediaCollection=-2.31
    )
    assert isinstance(var_64, python_code_.MediaLibrary_MediaCollection)
    var_65 = {var_64, var_64}
    var_66 = python_code_.MediaLibrary_Library(name=(), MediaLibrary_Library8=var_65)
    assert isinstance(var_66, python_code_.MediaLibrary_Library)
    var_70 = python_code_.MediaLibrary_AudioBook(currentPosition=-3383.12)
    assert isinstance(var_70, python_code_.MediaLibrary_AudioBook)
    var_74 = python_code_.MediaLibrary_Library(
        name=var_64, MediaLibrary_Library8=var_65
    )
    assert isinstance(var_74, python_code_.MediaLibrary_Library)


def test_41():
    var_13 = python_code_.MediaLibrary_Image(dateTaken="q*HMj$")
    assert isinstance(var_13, python_code_.MediaLibrary_Image)
    var_16 = "MediaLibrary_Artifact11"
    var_18 = python_code_.SourceType.HDD
    var_19 = "]bZ,m9r\\]@\tuS"
    var_21 = python_code_.MediaLibrary_MediaCollection(name=var_16, collections=(2627,))
    assert isinstance(var_21, python_code_.MediaLibrary_MediaCollection)
    var_22 = python_code_.MediaLibrary_Device(
        MACAddress=var_19,
        resolutionWidth=complex(1028.0, 1191.424),
        resolutionHeight=var_18,
        Device14=var_21,
    )
    assert isinstance(var_22, python_code_.MediaLibrary_Device)
    assert isinstance(
        python_code_.MediaLibrary_Device.Device,
        python_code_.MediaLibrary_MediaCollection,
    )


def test_42():
    var_0 = python_code_.MediaLibrary_Device
    var_1 = python_code_.MediaLibrary_MediaCollection(
        name="xX:Q7]Q}>(sM", hostOf=var_0, MediaCollection=var_0, MediaCollection17=None
    )
    assert isinstance(var_1, python_code_.MediaLibrary_MediaCollection)
    var_2 = python_code_.MediaLibrary_Device(
        MACAddress="CD,MediaLibrary_Artifact11,_MediaLibrary_MediaCollection__MediaLibrary_MediaCollection10,_MediaLibrary_Artifact__MediaLibrary_Artifact",
        resolutionWidth=1339,
        resolutionHeight=-335,
        Device=var_1,
        host={var_1},
    )
    assert isinstance(var_2, python_code_.MediaLibrary_Device)
    assert isinstance(
        python_code_.MediaLibrary_Device.Device,
        python_code_.MediaLibrary_MediaCollection,
    )


def test_43():
    var_0 = python_code_.MediaLibrary_Smartphone
    var_1 = python_code_.MediaLibrary_MediaCollection(
        name="xX:Q7]Q}>(sM", hostOf=var_0, MediaCollection=var_0, MediaCollection17=None
    )
    assert isinstance(var_1, python_code_.MediaLibrary_MediaCollection)
    var_2 = python_code_.MediaLibrary_Device(
        MACAddress="CD,MediaLibrary_Artifact11,_MediaLibrary_MediaCollection__MediaLibrary_MediaCollection10,_MediaLibrary_Artifact__MediaLibrary_Artifact",
        resolutionWidth=1339,
        resolutionHeight=-335,
        Device=var_1,
        host={var_1},
    )
    assert isinstance(var_2, python_code_.MediaLibrary_Device)
    assert isinstance(
        python_code_.MediaLibrary_Device.Device,
        python_code_.MediaLibrary_MediaCollection,
    )
    var_4 = -6357
    var_5 = {var_1, var_1, var_1, var_1}
    var_6 = python_code_.MediaLibrary_Device(
        MACAddress=var_1,
        resolutionWidth=var_0,
        resolutionHeight=var_4,
        Device=var_1,
        Device14=var_1,
        host=[],
        syncedDevices=var_5,
    )
    assert isinstance(var_6, python_code_.MediaLibrary_Device)
    python_code_.MediaLibrary_MediaCollection(
        name="Zoxw_3;gtb@7",
        MediaLibrary_MediaCollection=var_1,
        hostOf={"CASSETTE-MediaLibrary_Library": -1019.07},
        MediaCollection17=var_2,
    )


def test_44():
    var_0 = python_code_.MediaLibrary_Tablet
    var_9 = -319
    var_10 = 242
    var_11 = python_code_.MediaLibrary_MediaCollection(
        name="\tdT/\nxk =5[=q", MediaCollection17=var_9
    )
    assert isinstance(var_11, python_code_.MediaLibrary_MediaCollection)
    var_12 = {var_11, var_11, var_11}
    var_13 = python_code_.MediaLibrary_Device(
        MACAddress=set(),
        resolutionWidth=var_9,
        resolutionHeight=var_10,
        Device=var_0,
        syncedDevices=var_12,
    )
    assert isinstance(var_13, python_code_.MediaLibrary_Device)
    assert isinstance(
        python_code_.MediaLibrary_Device.Device,
        python_code_.MediaLibrary_MediaCollection,
    )
    var_14 = {var_13, var_13}
    var_15 = python_code_.MediaLibrary_MediaCollection(
        name=[
            "_MediaLibrary_MediaCollection__MediaLibrary_MediaCollection10 OTHER Device MediaSource"
        ],
        collections=var_14,
        MediaCollection=var_13,
    )
    assert isinstance(var_15, python_code_.MediaLibrary_MediaCollection)


def test_45():
    var_2 = python_code_.MediaLibrary_MediaCollection(
        name="?`C`:aM|+,UNmo@",
        hostOf=None,
        collections=set(),
        MediaCollection=None,
        MediaCollection17=None,
    )
    assert isinstance(var_2, python_code_.MediaLibrary_MediaCollection)
    var_10 = lambda *args, **kwargs: True
    var_11 = "MediaLibrary_Library"
    var_12 = 2490
    var_13 = set()
    var_14 = python_code_.MediaLibrary_Device(
        MACAddress=var_11,
        resolutionWidth=var_12,
        resolutionHeight=var_2,
        Device14=var_2,
        host=var_13,
    )
    assert isinstance(var_14, python_code_.MediaLibrary_Device)
    var_15 = {var_14, var_14, var_14, var_14, var_14}
    var_16 = python_code_.MediaLibrary_MediaSource
    var_17 = python_code_.MediaLibrary_MediaCollection(
        name=var_10,
        MediaLibrary_MediaCollection10=b"u\x92\x9ee'\x04\xb2K\xc3(\xef\\\xac",
        hostOf=var_2,
        collections=var_15,
        MediaCollection=-4107,
        MediaCollection17=var_16,
    )
    assert isinstance(var_17, python_code_.MediaLibrary_MediaCollection)


def test_46():
    var_0 = python_code_.MediaLibrary_Device
    var_9 = -1397
    var_10 = python_code_.MediaLibrary_Library(name=complex(782.332, -594.004))
    assert isinstance(var_10, python_code_.MediaLibrary_Library)
    var_11 = python_code_.MediaLibrary_MediaCollection(
        name=var_0,
        MediaLibrary_MediaCollection=var_10,
        MediaLibrary_MediaCollection10=None,
        hostOf=b"\x90o,\x96A\xb3\xb4\x96\xd8\x86\xa2\xd1",
    )
    assert isinstance(var_11, python_code_.MediaLibrary_MediaCollection)
    var_12 = set()
    var_13 = "DeviceOTHER"
    var_14 = python_code_.MediaLibrary_Device(
        MACAddress=var_13,
        resolutionWidth=var_10,
        resolutionHeight=(False, -1810.53),
        MediaLibrary_Device=None,
    )
    assert isinstance(var_14, python_code_.MediaLibrary_Device)
    assert isinstance(
        python_code_.MediaLibrary_Device.Device,
        python_code_.MediaLibrary_MediaCollection,
    )
    var_15 = python_code_.MediaLibrary_MediaCollection(
        name=var_11, collections=var_12, MediaCollection=var_14
    )
    assert isinstance(var_15, python_code_.MediaLibrary_MediaCollection)
    var_16 = {var_11, var_15, var_15, var_15}
    var_17 = python_code_.MediaLibrary_Device(
        MACAddress=var_0,
        resolutionWidth=var_0,
        resolutionHeight=var_9,
        MediaLibrary_Device=":]_TyR6W@A|yjn",
        host=var_16,
    )
    assert isinstance(var_17, python_code_.MediaLibrary_Device)
    python_code_.MediaLibrary_MediaCollection(
        name={}, hostOf=var_0, MediaCollection=var_14
    )
