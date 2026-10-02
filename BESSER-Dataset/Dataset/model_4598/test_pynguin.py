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
    Arc,
    Compartment,
    ComplexNodeShape,
    DOT_Anchor,
    DOT_Arc,
    DOT_ArrowShape,
    DOT_Compartment,
    DOT_ComplexLabel,
    DOT_ComplexNodeShape,
    DOT_DirectedArc,
    DOT_Graph,
    DOT_GraphElement,
    DOT_HorizontalCompartment,
    DOT_Label,
    DOT_Layer,
    DOT_MNodeShape,
    DOT_Node,
    DOT_NodeShape,
    DOT_Nodelike,
    DOT_PointNodeShape,
    DOT_PolygonNodeShape,
    DOT_RecordNodeShape,
    DOT_Shape,
    DOT_SimpleCompartment,
    DOT_SimpleLabel,
    DOT_SimpleNodeShape,
    DOT_SubGraph,
    DOT_UndirectedArc,
    DOT_VerticalCompartment,
    GraphElement,
    Label,
    NodeShape,
    Nodelike,
    Shape,
    abstractmethod,
    date,
    datetime,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_0 = set
    var_1 = False
    var_2 = python_code_.DOT_ArrowShape(clipping=var_0, isPlain=var_1, size=var_0)
    assert isinstance(var_2, python_code_.DOT_ArrowShape)
    python_code_.DOT_DirectedArc(
        tail_lp=-1359.72, head_lp=-130.91, DOT_DirectedArc=var_2
    )


def test_1():
    var_0 = python_code_.DOT_Anchor(name="EC\x0cr@J%7")
    var_2 = python_code_.DOT_ArrowShape(
        clipping=False,
        isPlain=var_0,
        size=var_0,
        DOT_ArrowShape=var_0,
        DOT_ArrowShape50=var_0,
    )
    assert isinstance(var_2, python_code_.DOT_ArrowShape)
    var_3 = python_code_.DOT_DirectedArc(tail_lp=None, head_lp=var_0)
    assert isinstance(var_3, python_code_.DOT_DirectedArc)


@pytest.mark.xfail(strict=True)
def test_2():
    var_1 = "_DOT_Layer__Layer"
    var_4 = -3
    var_5 = python_code_.NodeShape()
    var_6 = False
    var_7 = python_code_.DOT_Node(
        fixedSize=False, fontname=var_1, fontsize=var_6, height=var_4, width=var_4
    )
    assert isinstance(var_7, python_code_.DOT_Node)
    var_11 = lambda *args, **kwargs: "!_c%41^(\t<ra;Qo"
    var_12 = python_code_.DOT_DirectedArc(
        tail_lp=True, head_lp=var_7, DOT_DirectedArc=var_11, DOT_DirectedArc44=var_7
    )
    assert isinstance(var_12, python_code_.DOT_DirectedArc)
    python_code_.DOT_ArrowShape(
        clipping=var_1, isPlain=var_5, size=var_4, DOT_ArrowShape=var_12
    )


def test_3():
    var_2 = "^RwF"
    var_3 = python_code_.DOT_Compartment()
    python_code_.DOT_Anchor(name=var_2, anchor=var_3)
    var_5 = python_code_.DOT_SimpleCompartment(content=var_2)
    assert isinstance(var_5, python_code_.DOT_SimpleCompartment)
    var_6 = python_code_.DOT_MNodeShape()
    var_7 = -4872
    var_8 = python_code_.DOT_ArrowShape(
        clipping=var_3, isPlain=var_6, size=var_7, DOT_ArrowShape=var_2
    )
    assert isinstance(var_8, python_code_.DOT_ArrowShape)


def test_4():
    python_code_.DOT_Anchor(name="\njX\\\tjB/h\nf@OO T")
    var_3 = python_code_.DOT_DirectedArc(
        tail_lp=242.71, head_lp=998.61, DOT_DirectedArc46=None
    )
    assert isinstance(var_3, python_code_.DOT_DirectedArc)


def test_5():
    var_0 = python_code_.DOT_MNodeShape
    var_2 = python_code_.DOT_DirectedArc(
        tail_lp=-1137.92,
        head_lp=472.08,
        DOT_DirectedArc49=var_0,
        DOT_DirectedArc46=None,
    )
    assert isinstance(var_2, python_code_.DOT_DirectedArc)


def test_6():
    var_1 = python_code_.DOT_Label()
    var_3 = -2272.77
    var_4 = python_code_.DOT_DirectedArc(
        tail_lp=complex(-1473.75169, 34.06),
        head_lp=var_3,
        DOT_DirectedArc44=var_1,
        DOT_DirectedArc46=var_1,
    )
    assert isinstance(var_4, python_code_.DOT_DirectedArc)


def test_7():
    var_0 = 16.85
    var_1 = python_code_.DOT_Label()
    var_2 = python_code_.DOT_DirectedArc(
        tail_lp=-4533.92, head_lp=var_0, DOT_DirectedArc49=None, DOT_DirectedArc=var_1
    )
    assert isinstance(var_2, python_code_.DOT_DirectedArc)
    var_42 = True
    var_43 = "nods2"
    var_44 = python_code_.DOT_Arc(
        decorate=var_1,
        constraint=var_42,
        group=[393, 784],
        minlen=var_42,
        sameHead=var_43,
        sameTail=var_43,
        DOT_Arc=var_2,
    )
    assert isinstance(var_44, python_code_.DOT_Arc)


def test_8():
    python_code_.DOT_Anchor(name=True)
    var_1 = python_code_.Compartment()
    var_2 = -1108.93
    var_3 = python_code_.DOT_DirectedArc(
        tail_lp=735.21, head_lp=var_2, DOT_DirectedArc44=var_1
    )
    assert isinstance(var_3, python_code_.DOT_DirectedArc)


def test_9():
    var_1 = "_DOT_Layer__Layer"
    var_4 = 13
    var_6 = True
    var_7 = python_code_.DOT_Node(
        fixedSize=False, fontname=var_1, fontsize=var_6, height=var_4, width=var_4
    )
    assert isinstance(var_7, python_code_.DOT_Node)


def test_10():
    var_8 = False
    var_10 = lambda *args, **kwargs: False
    var_12 = "iSkVI,~obV"
    var_13 = python_code_.DOT_Node(
        fixedSize=var_10,
        fontname=var_12,
        fontsize=b"\xb3\x18\xd4GN\xb9\x1d\x7fL\xf1\xd1\xb6\x8f\x9c\xab\x8f\xf7\x11S",
        height=var_8,
        width=(True, 1065, 1786.65),
        DOT_Node=var_8,
    )
    assert isinstance(var_13, python_code_.DOT_Node)


def test_11():
    var_5 = python_code_.DOT_SubGraph(labelloc='K>U)?i tQH=L."fA;IW')
    assert isinstance(var_5, python_code_.DOT_SubGraph)


def test_12():
    var_1 = "_DOT_Layer__Layer"
    var_4 = -3
    var_5 = python_code_.NodeShape()
    var_6 = False
    var_7 = python_code_.DOT_Node(
        fixedSize=False, fontname=var_1, fontsize=var_6, height=var_4, width=var_4
    )
    assert isinstance(var_7, python_code_.DOT_Node)
    var_8 = python_code_.DOT_ComplexLabel()
    var_10 = True
    var_11 = python_code_.DOT_Layer(layerSeparator=var_1, Layer28=True, layers17=var_1)
    assert isinstance(var_11, python_code_.DOT_Layer)
    var_12 = {var_11, var_11, var_11}
    var_13 = python_code_.DOT_Nodelike()
    var_14 = python_code_.DOT_Arc(
        decorate=-202,
        constraint=var_10,
        group=var_8,
        minlen=None,
        sameHead=var_5,
        sameTail=var_1,
        arcs=var_12,
        refers=var_13,
        Arc20={2641, ";v[d*OB}^I", -872.2},
    )
    assert isinstance(var_14, python_code_.DOT_Arc)


def test_13():
    var_0 = "DOT_DiBrectedArc"
    var_1 = python_code_.DOT_PointNodeShape
    var_2 = python_code_.DOT_Nodelike()
    var_3 = python_code_.DOT_Arc(
        decorate=complex(1887.0, 1568.096592),
        constraint={},
        group=var_0,
        minlen=var_0,
        sameHead=var_0,
        sameTail=var_1,
        Arc20=var_1,
        DOT_Arc40=var_2,
    )
    assert isinstance(var_3, python_code_.DOT_Arc)
    var_7 = python_code_.DOT_SimpleLabel(content=var_0)
    assert isinstance(var_7, python_code_.DOT_SimpleLabel)
    var_9 = python_code_.DOT_Layer(layerSeparator=var_0, layers15=set(), Layer37=None)
    assert isinstance(var_9, python_code_.DOT_Layer)
    var_51 = python_code_.DOT_DirectedArc(
        tail_lp=-1137.92,
        head_lp=472.08,
        DOT_DirectedArc49=var_1,
        DOT_DirectedArc46=None,
    )
    assert isinstance(var_51, python_code_.DOT_DirectedArc)


def test_14():
    var_10 = python_code_.DOT_Layer(
        layerSeparator="_\th", Layer=None, layers=set(), layers15={False, -5633.4}
    )
    assert isinstance(var_10, python_code_.DOT_Layer)


def test_15():
    var_4 = "nodes24"
    var_11 = python_code_.DOT_Layer(layerSeparator=var_4)
    assert isinstance(var_11, python_code_.DOT_Layer)


def test_16():
    var_0 = python_code_.DOT_MNodeShape
    var_2 = python_code_.DOT_DirectedArc(
        tail_lp=-1137.92,
        head_lp=472.08,
        DOT_DirectedArc49=var_0,
        DOT_DirectedArc46=None,
    )
    assert isinstance(var_2, python_code_.DOT_DirectedArc)
    var_15 = python_code_.DOT_HorizontalCompartment()
    var_16 = python_code_.DOT_Nodelike()
    var_19 = '.wVBAl2p\\J"@'
    var_20 = python_code_.DOT_Layer(
        layerSeparator=var_19, Layer28=var_16, Layer37=var_15
    )
    assert isinstance(var_20, python_code_.DOT_Layer)


def test_17():
    var_3 = True
    var_4 = "nodes24"
    var_11 = python_code_.DOT_Layer(layerSeparator=var_4, Layer=var_3)
    assert isinstance(var_11, python_code_.DOT_Layer)


def test_18():
    var_4 = "nodes24"
    var_11 = python_code_.DOT_Layer(layerSeparator=var_4, layers15=set(), Layer37=var_4)
    assert isinstance(var_11, python_code_.DOT_Layer)


def test_19():
    var_0 = "_DOT_SubGraph__owner"
    var_1 = "H"
    var_2 = "DOT_Label47:_DOT_Arc__arcs:Nodelike30:layers15"
    var_3 = lambda *args, **kwargs: False
    var_4 = "`m5~_"
    var_5 = python_code_.DOT_Graph(
        type=var_0,
        rankDir=var_0,
        labeljust=var_1,
        labelloc=var_0,
        concentrate=set(),
        boundingBox=var_2,
        compound=None,
        nodeSeparation=var_0,
        ordering=var_3,
        size=var_2,
        ratio=var_4,
        center={-5506},
        Graph=var_0,
    )
    assert isinstance(var_5, python_code_.DOT_Graph)


def test_20():
    var_5 = python_code_.DOT_SimpleLabel(
        content="DOT_Graph_DOT_Layer__Layer28_DOT_GraphElement__element_DOT_ArrowShape__DOT_ArrowShape50"
    )
    assert isinstance(var_5, python_code_.DOT_SimpleLabel)
    var_17 = python_code_.DOT_GraphElement
    var_19 = 'kv5sv>:e|yF6"\t)'
    var_20 = False
    var_21 = 2245.87
    var_22 = python_code_.DOT_Graph(
        type=var_17,
        rankDir=var_19,
        labeljust=[363.36, -820.84],
        labelloc=var_19,
        concentrate=var_20,
        boundingBox=var_17,
        compound=var_20,
        nodeSeparation=var_21,
        ordering={"o\tJL(No": "Fm-Du"},
        size=var_19,
        ratio={
            ">f.PG2#O{^cJY": 0,
            "_DOT_GraphElement__GraphElement,graph11,DOT_DirectedArc49,_DOT_Arc__arcs": "'\"*#):uj",
        },
        center=var_19,
        Graph25=var_17,
        Graph=None,
    )
    assert isinstance(var_22, python_code_.DOT_Graph)


def test_21():
    var_55 = "H"
    var_56 = "DOT_Arc _DOT_ArrowShape__DOT_ArrowShape50 Nodelike35 DOT_Nodelike"
    var_59 = python_code_.DOT_Graph(
        type=var_56,
        rankDir="_DOT_Arc__DOT_Arc",
        labeljust="9",
        labelloc=var_56,
        concentrate=True,
        boundingBox="X",
        compound=True,
        nodeSeparation=-133.9,
        ordering="_DOT_Arc__Arc20 _DOT_Arc__refers",
        size='7e"S:qz/^6~FS\\|',
        ratio=var_55,
        center=True,
    )
    assert isinstance(var_59, python_code_.DOT_Graph)


def test_22():
    python_code_.DOT_Anchor(name=True)


def test_23():
    var_17 = "\x0c$G/nx\r3VCjD,ec"
    var_18 = "L8bxg"
    var_19 = python_code_.DOT_GraphElement(color=var_17, name=var_18, style=var_18)
    assert isinstance(var_19, python_code_.DOT_GraphElement)


def test_24():
    python_code_.DOT_Compartment()


def test_25():
    var_0 = python_code_.DOT_Shape(
        width=None, height=332.08, peripheries=("Z1C\nl\x0cyG",)
    )
    assert isinstance(var_0, python_code_.DOT_Shape)
    var_1 = "Fqk{' B\"7k%vN_F/+"
    var_2 = python_code_.DOT_GraphElement(
        color=var_1, name=b"2PAMD\xc9aa\xc6\xf9\xadv\x83o\x829", style=var_1
    )
    assert isinstance(var_2, python_code_.DOT_GraphElement)
    var_4 = 2
    var_5 = python_code_.DOT_Node(
        fixedSize=True,
        fontname="6j+F47z{gO.5[n,.",
        fontsize=var_4,
        height=-793,
        width=5673,
        DOT_Node=None,
    )
    assert isinstance(var_5, python_code_.DOT_Node)
    var_6 = python_code_.DOT_HorizontalCompartment()
    var_9 = True
    var_11 = "{r.w"
    python_code_.DOT_Anchor(name="s^Um", Anchor=var_11, anchor=var_6)
    var_13 = python_code_.DOT_PolygonNodeShape(
        sides=var_2, skew=None, distortion=var_9, isRegular=var_9, orientation=var_4
    )
    assert isinstance(var_13, python_code_.DOT_PolygonNodeShape)


def test_26():
    var_0 = python_code_.DOT_Shape(
        width=None, height=332.08, peripheries=("Z1C\nl\x0cyG",)
    )
    assert isinstance(var_0, python_code_.DOT_Shape)
    var_1 = "Fqk{' B\"7k%vN_F/+"
    var_2 = python_code_.DOT_GraphElement(
        color=var_1, name=b"2PAMD\xc9aa\xc6\xf9\xadv\x83o\x829", style=var_1
    )
    assert isinstance(var_2, python_code_.DOT_GraphElement)
    var_3 = python_code_.DOT_Anchor
    var_4 = 2
    var_5 = python_code_.DOT_Node(
        fixedSize=var_0, fontname=2814.07, fontsize=var_3, height=var_4, width=var_4
    )
    assert isinstance(var_5, python_code_.DOT_Node)
    var_11 = "{r.w"
    python_code_.DOT_Anchor(name=var_11)


def test_27():
    var_0 = python_code_.DOT_Anchor(name="0m3Mg1'\\V4R28>", anchor=None)
    var_2 = "DOT_NodeShape,Nodelike,_DOT_ArrowShape__DOT_ArrowShape50"
    var_3 = python_code_.DOT_Label
    var_4 = "_DOT_GraphElement__element-_DOT_Layer__Layer"
    var_5 = True
    var_6 = 661.45
    var_7 = "_DOT_SubGraph__SubGraph.Nodelike13.DOT_Compartment"
    var_8 = python_code_.DOT_Graph(
        type=var_0,
        rankDir=var_2,
        labeljust=var_3,
        labelloc=-2500.05,
        concentrate=(),
        boundingBox=var_4,
        compound=var_5,
        nodeSeparation=var_6,
        ordering=var_4,
        size=var_7,
        ratio=var_3,
        center=1051.47,
    )
    assert isinstance(var_8, python_code_.DOT_Graph)
    var_9 = python_code_.DOT_Nodelike()
    var_10 = {var_9, var_9, var_9}
    var_11 = python_code_.DOT_Layer(
        layerSeparator=var_0, Layer=var_8, layers=var_10, layers15=var_10, Layer28=var_9
    )
    assert isinstance(var_11, python_code_.DOT_Layer)


def test_28():
    var_16 = "DOT_La9yer"
    var_17 = python_code_.DOT_SubGraph(labelloc=var_16)
    assert isinstance(var_17, python_code_.DOT_SubGraph)
    var_18 = python_code_.DOT_SimpleCompartment(
        content={":w[Rzb3H6]MTk9Cv>7R", "Layer,DOT_Nodelike"}
    )
    assert isinstance(var_18, python_code_.DOT_SimpleCompartment)


def test_29():
    var_6 = python_code_.DOT_HorizontalCompartment()
    var_11 = "{r.w"
    python_code_.DOT_Anchor(name="s^Um", Anchor=var_11, anchor=var_6)


def test_30():
    var_1 = "_DOT_Layer__Layer"
    python_code_.DOT_Anchor(name=var_1, anchor=var_1)


@pytest.mark.xfail(strict=True)
def test_31():
    var_1 = False
    var_2 = python_code_.DOT_ArrowShape(
        clipping="9&yc]6g=WY(Oe\nRb ", isPlain=var_1, size=-56
    )
    assert isinstance(var_2, python_code_.DOT_ArrowShape)
    python_code_.DOT_DirectedArc(
        tail_lp=579.42, head_lp=-489.97, DOT_DirectedArc49=var_2, DOT_DirectedArc=None
    )


def test_32():
    var_3 = False
    var_4 = "nodes24"
    var_45 = lambda *args, **kwargs: False
    var_46 = python_code_.DOT_Arc(
        decorate=var_3,
        constraint=var_3,
        group=var_45,
        minlen=complex(2305.582, -3087.0),
        sameHead=var_4,
        sameTail=var_4,
        Arc=True,
        refers=var_45,
        DOT_Arc40=b"s\x92\xd9\xe1L\xb2\xd2\x1b\x9b\xd7\x05\xa6KE\xe6\x86\x19",
    )
    assert isinstance(var_46, python_code_.DOT_Arc)
    var_52 = python_code_.DOT_RecordNodeShape()
    var_53 = python_code_.DOT_PointNodeShape()
    python_code_.DOT_Arc(
        decorate=var_4,
        constraint=var_53,
        group=b"\x8e\xd4\x9a,\xb2@\xe2p\x072g\xcf",
        minlen=var_52,
        sameHead=var_45,
        sameTail=var_45,
    )


def test_33():
    var_0 = python_code_.DOT_ComplexLabel
    var_1 = False
    var_2 = python_code_.DOT_ArrowShape(clipping=var_0, isPlain=var_1, size=var_0)
    assert isinstance(var_2, python_code_.DOT_ArrowShape)
    var_61 = "\r"
    var_65 = python_code_.DOT_SimpleLabel(content=var_61)
    assert isinstance(var_65, python_code_.DOT_SimpleLabel)
    var_73 = python_code_.DOT_Arc
    var_75 = True
    var_76 = "_DOT_Layer__layers15,Nodelike35"
    var_77 = "B?b\x0b3i)_\\XKDN"
    var_78 = python_code_.DOT_Nodelike()
    var_79 = python_code_.DOT_Arc(
        decorate=var_73,
        constraint=var_65,
        group=-2240,
        minlen=var_75,
        sameHead=var_76,
        sameTail=var_77,
        refers=var_78,
    )
    assert isinstance(var_79, python_code_.DOT_Arc)
    var_80 = {var_79, var_79}
    var_81 = python_code_.DOT_Layer(
        layerSeparator={True, 1805}, layers=None, layers15=var_80
    )
    assert isinstance(var_81, python_code_.DOT_Layer)


def test_34():
    var_0 = python_code_.Nodelike
    var_1 = python_code_.DOT_Label()
    var_2 = python_code_.DOT_DirectedArc(
        tail_lp=var_0,
        head_lp=['\r#W"Hn{AI*Ig', -1332.04, 434.15],
        DOT_DirectedArc46=var_1,
    )
    assert isinstance(var_2, python_code_.DOT_DirectedArc)
    var_13 = python_code_.DOT_HorizontalCompartment()
    var_14 = python_code_.DOT_Nodelike()
    var_16 = True
    var_20 = '.wVBAl2p\\J"@'
    var_21 = python_code_.DOT_Layer(
        layerSeparator=var_20, Layer28=var_14, Layer37=var_13
    )
    assert isinstance(var_21, python_code_.DOT_Layer)
    var_23 = True
    var_24 = "h\rqteq6 q"
    var_25 = -14
    var_26 = "_DOT_Graph__graph11_DOT_Arc__DOT_Arc40DOT_Nodelike41DOT_Compartment"
    var_27 = python_code_.DOT_Arc(
        decorate=var_23,
        constraint=var_16,
        group=var_24,
        minlen=var_25,
        sameHead=var_26,
        sameTail=-2625.16,
        Arc=var_21,
        referredBy=var_14,
        DOT_Arc=var_14,
        refers={},
    )
    assert isinstance(var_27, python_code_.DOT_Arc)


def test_35():
    var_3 = "_DOT_SubGraph__SubGraph"
    var_4 = python_code_.DOT_SubGraph(labelloc=var_3)
    assert isinstance(var_4, python_code_.DOT_SubGraph)
    var_6 = "_DOT_Node__DOT_Node"
    var_9 = python_code_.DOT_Nodelike()
    var_10 = python_code_.DOT_VerticalCompartment()
    var_11 = python_code_.DOT_SimpleLabel(content=-638)
    assert isinstance(var_11, python_code_.DOT_SimpleLabel)
    var_12 = -490.78
    var_16 = python_code_.DOT_Nodelike()
    var_19 = "rlCB\\+zpH8"
    var_20 = False
    var_21 = {var_16, var_16, var_16, var_9}
    var_22 = python_code_.DOT_Graph(
        type=var_10,
        rankDir=var_19,
        labeljust=var_9,
        labelloc=var_12,
        concentrate=var_20,
        boundingBox=set(),
        compound=var_20,
        nodeSeparation=var_12,
        ordering=var_6,
        size=complex(2121.8034778, -1092.0),
        ratio=var_6,
        center='dy3YAD.?Z%?E"B^o$HB',
        graph=var_21,
    )
    assert isinstance(var_22, python_code_.DOT_Graph)


def test_36():
    var_40 = tuple
    var_81 = python_code_.DOT_ComplexNodeShape()
    var_83 = "mDm SJvRxOP!"
    var_84 = -2913
    var_85 = python_code_.DOT_Nodelike()
    var_86 = python_code_.DOT_Arc(
        decorate=-4630.1,
        constraint=var_81,
        group=var_83,
        minlen=var_84,
        sameHead=var_40,
        sameTail=-613,
        Arc22=var_85,
        referredBy=var_85,
        DOT_Arc40=var_83,
    )
    assert isinstance(var_86, python_code_.DOT_Arc)


def test_37():
    var_0 = bytes
    var_40 = "W\t`S]QJ{d^"
    var_41 = python_code_.DOT_SubGraph(
        labelloc=">lG\\\\Y\\8&l)k(c6/F-", owner=set(), SubGraph=var_0
    )
    assert isinstance(var_41, python_code_.DOT_SubGraph)
    var_52 = python_code_.DOT_SimpleCompartment(content=var_40)
    assert isinstance(var_52, python_code_.DOT_SimpleCompartment)


def test_38():
    var_6 = python_code_.DOT_UndirectedArc
    var_7 = python_code_.DOT_SubGraph(labelloc="toNode", SubGraph=var_6)
    assert isinstance(var_7, python_code_.DOT_SubGraph)


@pytest.mark.xfail(strict=True)
def test_39():
    var_0 = python_code_.Nodelike
    var_13 = python_code_.DOT_HorizontalCompartment()
    var_14 = python_code_.DOT_Nodelike()
    var_16 = True
    var_20 = '.wVBl2p\\J"@'
    var_21 = python_code_.DOT_Layer(
        layerSeparator=var_20, Layer28=var_14, Layer37=var_13
    )
    assert isinstance(var_21, python_code_.DOT_Layer)
    var_28 = -1588.14355940949
    var_29 = -388.32
    var_30 = python_code_.DOT_DirectedArc(
        tail_lp=var_28,
        head_lp=var_29,
        DOT_DirectedArc49=var_0,
        DOT_DirectedArc44=-2726.44,
    )
    assert isinstance(var_30, python_code_.DOT_DirectedArc)
    python_code_.DOT_ArrowShape(
        clipping=var_0, isPlain=(), size=var_16, DOT_ArrowShape50=var_30
    )


@pytest.mark.xfail(strict=True)
def test_40():
    var_0 = python_code_.DOT_MNodeShape()
    var_1 = "nodes27,Layer37,_DOT_Arc__Arc,layers15"
    python_code_.DOT_Anchor(name=var_1, anchor=var_1)
    var_3 = python_code_.Compartment()
    var_4 = 1630
    var_5 = (
        lambda *args, **kwargs: "_DOT_Node__DOT_Node:_DOT_ArrowShape__DOT_ArrowShape50"
    )
    var_6 = python_code_.DOT_Shape(width=var_4, height=var_5, peripheries=var_1)
    assert isinstance(var_6, python_code_.DOT_Shape)
    var_7 = python_code_.DOT_MNodeShape()
    var_9 = python_code_.DOT_HorizontalCompartment()
    var_14 = python_code_.DOT_SubGraph(labelloc=var_1)
    assert isinstance(var_14, python_code_.DOT_SubGraph)
    var_15 = "_DOT_ArrowShape__DOT_ArrowShape,DOT_Label47,DOT_Label"
    var_16 = python_code_.DOT_GraphElement(color=var_15, name=-1887, style=var_15)
    assert isinstance(var_16, python_code_.DOT_GraphElement)
    var_17 = python_code_.DOT_Layer(
        layerSeparator=b" \xd4g\x12}\x97&\xdcX\x14u\xb5\xdd}\xdc`",
        Layer37=var_0,
        layers17=var_5,
    )
    assert isinstance(var_17, python_code_.DOT_Layer)
    python_code_.DOT_Graph(
        type=var_3,
        rankDir=var_5,
        labeljust=var_1,
        labelloc=var_7,
        concentrate={},
        boundingBox=var_1,
        compound={"_DOT_Layer__Layer": -1780, "_DOT_Anchor__Anchor": False},
        nodeSeparation=b"\xe1\x94\xf3l\xe7\xd7\x08\xc86\x16s",
        ordering=var_5,
        size=2424.17,
        ratio=var_9,
        center=-1128.87,
        Graph25=var_0,
        Graph=var_17,
    )


def test_41():
    var_0 = python_code_.DOT_MNodeShape
    var_2 = python_code_.DOT_DirectedArc(
        tail_lp=-1137.92,
        head_lp=472.08,
        DOT_DirectedArc49=var_0,
        DOT_DirectedArc46=None,
    )
    assert isinstance(var_2, python_code_.DOT_DirectedArc)
    var_15 = "DOT_Compartment"
    var_16 = python_code_.DOT_Label()
    var_17 = python_code_.DOT_GraphElement(
        color=var_0, name=var_2, style=var_15, GraphElement=var_16
    )
    assert isinstance(var_17, python_code_.DOT_GraphElement)


def test_42():
    var_0 = python_code_.DOT_VerticalCompartment()
    var_1 = ";\n8? H1 l"
    var_2 = "6/\x0cR%"
    var_3 = False
    var_4 = python_code_.DOT_Graph(
        type=[],
        rankDir={"?\n1#{=Ii]G\x0b|&": 188, "_DOT_Arc__Arc22": "DOT_Nodelike41"},
        labeljust=set(),
        labelloc=var_0,
        concentrate=2447,
        boundingBox=var_1,
        compound=complex(2228.96491, -1960.0),
        nodeSeparation="&![^.+CSw6d-e{LN>",
        ordering=var_2,
        size=var_2,
        ratio=var_2,
        center=var_3,
        graph11=var_2,
        Graph=842,
    )
    assert isinstance(var_4, python_code_.DOT_Graph)
    var_5 = python_code_.DOT_HorizontalCompartment()
    var_8 = python_code_.DOT_SubGraph(labelloc=var_3)
    assert isinstance(var_8, python_code_.DOT_SubGraph)
    var_9 = python_code_.DOT_VerticalCompartment()
    var_10 = lambda *args, **kwargs: False
    var_11 = python_code_.DOT_GraphElement(
        color=381, name=var_2, style=var_1, GraphElement=var_5, element=var_10
    )
    assert isinstance(var_11, python_code_.DOT_GraphElement)
    var_12 = True
    var_13 = "ux.oH^jK"
    var_14 = 2731
    var_15 = "F"
    var_16 = python_code_.DOT_Layer(layerSeparator=var_15, Layer=var_13)
    assert isinstance(var_16, python_code_.DOT_Layer)
    var_17 = python_code_.DOT_Nodelike()
    var_18 = python_code_.DOT_Arc(
        decorate=b"8g\xb0\xff\x0bM\xa0`\x0f\xb7ep)\x80",
        constraint=var_12,
        group=var_13,
        minlen=var_14,
        sameHead=var_15,
        sameTail=var_9,
        Arc=var_16,
        Arc22=set(),
        refers="_DOT_Arc__referredBy_DOT_Arc__DOT_Arc_DOT_Graph__GraphLayer",
        Arc20=False,
        DOT_Arc40=var_17,
    )
    assert isinstance(var_18, python_code_.DOT_Arc)
    python_code_.DOT_GraphElement(
        color=var_15, name=var_10, style=[1575, False], GraphElement={}
    )


@pytest.mark.xfail(strict=True)
def test_43():
    var_0 = "DOT_DirectedArc"
    var_1 = python_code_.DOT_PointNodeShape
    var_2 = python_code_.DOT_Nodelike()
    var_3 = python_code_.DOT_Arc(
        decorate=complex(1887.0, 1568.096592),
        constraint={},
        group=var_0,
        minlen=var_0,
        sameHead=var_0,
        sameTail=var_1,
        Arc20=var_1,
        DOT_Arc40=var_2,
    )
    assert isinstance(var_3, python_code_.DOT_Arc)
    var_4 = 2
    var_5 = python_code_.DOT_PolygonNodeShape(
        sides=var_0,
        skew=var_0,
        distortion=var_4,
        isRegular="",
        orientation=[-2366, 4731.91],
    )
    assert isinstance(var_5, python_code_.DOT_PolygonNodeShape)
    var_7 = python_code_.DOT_SimpleLabel(content=var_0)
    assert isinstance(var_7, python_code_.DOT_SimpleLabel)
    var_9 = python_code_.DOT_Layer(layerSeparator=var_2)
    assert isinstance(var_9, python_code_.DOT_Layer)
    var_10 = -1925.84
    var_11 = "\x0cvx"
    var_12 = 869
    var_13 = python_code_.DOT_ArrowShape(
        clipping=var_11, isPlain=var_1, size=var_12, DOT_ArrowShape=var_1
    )
    assert isinstance(var_13, python_code_.DOT_ArrowShape)
    python_code_.DOT_DirectedArc(tail_lp=var_10, head_lp=var_10, DOT_DirectedArc=var_13)


def test_44():
    var_1 = python_code_.DOT_Label()
    var_16 = "DOT_La9yer"
    var_17 = python_code_.DOT_SubGraph(labelloc=var_16)
    assert isinstance(var_17, python_code_.DOT_SubGraph)
    var_18 = python_code_.DOT_SimpleCompartment(
        content={":w[Rzb3H6]MTk9Cv>7R", "Layer,DOT_Nodelike"}
    )
    assert isinstance(var_18, python_code_.DOT_SimpleCompartment)
    var_20 = python_code_.DOT_GraphElement(
        color=var_16, name=var_16, style="^e 64bR]p", GraphElement=var_1, element=var_1
    )
    assert isinstance(var_20, python_code_.DOT_GraphElement)
