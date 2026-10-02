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
    EdgeProcessor,
    EdgeType,
    Enum,
    abstractmethod,
    date,
    datetime,
    dfs_DFSGraph,
    dfs_DepthFirstSearch,
    dfs_EObject,
    dfs_Edge,
    dfs_EdgeProcessor,
    dfs_Node,
    time,
)


def test_0():
    var_4 = python_code_.dfs_EdgeProcessor()
    assert var_4.dfs_EdgeProcessor0 is None


def test_1():
    var_20 = python_code_.dfs_EdgeProcessor(dfs_EdgeProcessor0=814.97)
    assert var_20.dfs_EdgeProcessor0 == pytest.approx(814.97, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_2():
    var_0 = "TIS4o[7W\x0c!K\nK`'|\r\t"
    var_7 = python_code_.dfs_Node(postTraversal=1710, preTraversal=0, target=set())
    assert isinstance(var_7, python_code_.dfs_Node)
    python_code_.dfs_Edge(type=var_0, Edge=var_7, outgoing=var_7, incoming=var_7)


def test_3():
    python_code_.dfs_Edge(type="4=xuXz", dfs_Edge=None)


def test_4():
    var_0 = "Node13"
    var_9 = python_code_.dfs_Edge(type=var_0, outgoing=var_0, edges=var_0)
    assert var_9.outgoing == "Node13"


def test_5():
    var_0 = "hU4uFgV."
    var_9 = python_code_.dfs_Edge(type=var_0, Edge=var_0, dfs_Edge=None, edges=None)
    assert isinstance(var_9, python_code_.dfs_Edge)


def test_6():
    var_0 = "Node13"
    var_8 = python_code_.dfs_Edge(
        type="isejhDb;.ti\x0c", dfs_Edge=None, incoming=None, Edge15=var_0, edges=var_0
    )
    assert isinstance(var_8, python_code_.dfs_Edge)


@pytest.mark.xfail(strict=True)
def test_7():
    var_16 = -3858
    var_0 = python_code_.dfs_Node(postTraversal=var_16, preTraversal=2938, Node13=None)
    assert isinstance(var_0, python_code_.dfs_Node)
    python_code_.dfs_Edge(type="U %E", Edge=var_0, outgoing=None, incoming=var_0)


def test_8():
    var_0 = "Ntode13"
    var_7 = python_code_.dfs_Edge(type=var_0, incoming=var_0)
    assert isinstance(var_7, python_code_.dfs_Edge)


def test_9():
    var_0 = "Node13"
    var_9 = python_code_.dfs_Edge(type=var_0, Edge=None, dfs_Edge=var_0, edges=var_0)
    assert isinstance(var_9, python_code_.dfs_Edge)


def test_10():
    var_10 = python_code_.dfs_Node(
        postTraversal=-1627, preTraversal=-1496, target={False, 875.88}, nodes=None
    )
    assert isinstance(var_10, python_code_.dfs_Node)


def test_11():
    var_10 = python_code_.dfs_Node(postTraversal=-908, preTraversal=2189)
    assert isinstance(var_10, python_code_.dfs_Node)


def test_12():
    var_10 = python_code_.dfs_Node(
        postTraversal=1091, preTraversal=-1541, source=set(), Node=None, Node13=None
    )
    assert isinstance(var_10, python_code_.dfs_Node)


def test_13():
    var_16 = -3851
    var_0 = python_code_.dfs_Node(
        postTraversal=469, preTraversal=var_16, nodes=var_16, dfs_Node=var_16
    )
    assert isinstance(var_0, python_code_.dfs_Node)


def test_14():
    var_16 = -1296.41
    var_0 = python_code_.dfs_Node(
        postTraversal=var_16, preTraversal=4465, nodes=var_16, Node13=var_16
    )
    assert isinstance(var_0, python_code_.dfs_Node)


def test_15():
    var_7 = python_code_.dfs_DepthFirstSearch
    var_8 = python_code_.dfs_Node(
        postTraversal=-820, preTraversal=3245, source={1655}, Node=var_7, Node13=None
    )
    assert isinstance(var_8, python_code_.dfs_Node)


def test_16():
    python_code_.EdgeProcessor()


def test_17():
    var_19 = python_code_.dfs_DepthFirstSearch(
        postTraversalCounter=complex(-3397.3, -17.870954), preTraversalCounter={}
    )
    assert isinstance(var_19, python_code_.dfs_DepthFirstSearch)


def test_18():
    var_0 = python_code_.dfs_EObject()
    var_1 = 1
    var_2 = set
    var_3 = python_code_.dfs_Node(
        postTraversal=-1259, preTraversal=var_1, target={var_2}, nodes=var_0
    )
    assert isinstance(var_3, python_code_.dfs_Node)
    var_4 = python_code_.dfs_EdgeProcessor(dfs_EdgeProcessor0=[False])
    assert var_4.dfs_EdgeProcessor0 == [False]
    var_5 = var_4.processNode(dfs_node=complex(-2211.2, -1522.1))
    var_6 = python_code_.dfs_DepthFirstSearch(
        postTraversalCounter=var_2, preTraversalCounter=b"\x01\xf3\x06ZX\xc3%"
    )
    assert isinstance(var_6, python_code_.dfs_DepthFirstSearch)
    var_6.incrementPreTraversalCounter()
    var_4.processEdge(dfs_edge=var_5)
    var_10 = python_code_.EdgeType.CROSS_EDGE
    var_11 = python_code_.dfs_DepthFirstSearch(
        postTraversalCounter=698, preTraversalCounter=var_1
    )
    var_6.processEdge(dfs_edge={True})
    var_13 = python_code_.dfs_DFSGraph()
    python_code_.dfs_Edge(
        type=[
            "dfs_DFSGraphdfs_EdgeProcessorNode_dfs_Node__Node18",
            "c09wSRA13\x0co",
            False,
        ],
        Edge=None,
        dfs_Edge=var_10,
        edges=var_13,
    )
    python_code_.dfs_Node(postTraversal=var_2, preTraversal=var_11, nodes=var_13)


def test_19():
    var_0 = "cQ'Aa}Od.g|"
    var_1 = python_code_.dfs_EObject
    var_2 = python_code_.dfs_Edge(
        type="xLs\tB=2w", incoming=var_1, Edge15=var_0, edges=None
    )
    assert isinstance(var_2, python_code_.dfs_Edge)
    var_4 = python_code_.dfs_Edge(type=var_1, Edge6=complex(-1098.294, -641.25859))
    assert isinstance(var_4, python_code_.dfs_Edge)
    var_5 = -1751
    var_6 = python_code_.dfs_DepthFirstSearch(
        postTraversalCounter=3535.82, preTraversalCounter=var_5
    )
    assert isinstance(var_6, python_code_.dfs_DepthFirstSearch)
    var_6.incrementPreTraversalCounter()


def test_20():
    var_0 = 329
    var_1 = set
    var_2 = python_code_.dfs_DepthFirstSearch(
        postTraversalCounter=var_0, preTraversalCounter=var_1
    )
    assert isinstance(var_2, python_code_.dfs_DepthFirstSearch)
    var_2.incrementPostTraversalCounter()
    var_4 = python_code_.dfs_EdgeProcessor()
    assert var_4.dfs_EdgeProcessor0 is None
    var_4.processNode(dfs_node=1724.21)


def test_21():
    var_0 = 329
    var_1 = set
    var_2 = python_code_.dfs_DepthFirstSearch(
        postTraversalCounter=var_0, preTraversalCounter=var_1
    )
    assert isinstance(var_2, python_code_.dfs_DepthFirstSearch)
    var_4 = python_code_.dfs_EdgeProcessor()
    assert var_4.dfs_EdgeProcessor0 is None
    var_6 = var_2.processNode(dfs_node=var_1)
    var_7 = python_code_.dfs_Node(
        postTraversal=-1773.03,
        preTraversal=var_0,
        target=var_6,
        dfs_Node=-1,
        Node={True, "j"},
    )
    assert isinstance(var_7, python_code_.dfs_Node)


def test_22():
    var_0 = python_code_.EdgeType.BACKWARD_EDGE
    var_1 = python_code_.dfs_DepthFirstSearch(
        postTraversalCounter=var_0, preTraversalCounter=b"*@Q\xc3\xe8\xe9pY"
    )
    assert isinstance(var_1, python_code_.dfs_DepthFirstSearch)
    var_3 = python_code_.dfs_EdgeProcessor()
    assert var_3.dfs_EdgeProcessor0 is None
    var_3.processNode(dfs_node=complex(1621.7400081, 3166.967))


def test_23():
    var_23 = python_code_.dfs_Node(postTraversal=-184, preTraversal=-875, nodes=None)
    assert isinstance(var_23, python_code_.dfs_Node)
    var_32 = python_code_.dfs_Edge(
        type="orlPWbg~yF[D,Kvx;!", Edge=var_23, Edge6=var_23, outgoing=None
    )
    assert isinstance(var_32, python_code_.dfs_Edge)


@pytest.mark.xfail(strict=True)
def test_24():
    var_16 = -3858
    var_0 = python_code_.dfs_Node(
        postTraversal=-610, preTraversal=var_16, target=set(), Node13=var_16
    )
    assert isinstance(var_0, python_code_.dfs_Node)
    python_code_.dfs_Edge(type="U %E", Edge=var_0, outgoing=None, incoming=var_0)


@pytest.mark.xfail(strict=True)
def test_25():
    var_4 = python_code_.dfs_EdgeProcessor()
    python_code_.dfs_EdgeProcessor(dfs_EdgeProcessor=var_4, dfs_EdgeProcessor0=var_4)
    assert isinstance(var_4.dfs_EdgeProcessor0, python_code_.dfs_EdgeProcessor)


def test_26():
    var_29 = python_code_.dfs_EdgeProcessor(dfs_EdgeProcessor=True)
    assert isinstance(var_29, python_code_.dfs_EdgeProcessor)


def test_27():
    var_0 = "Node13"
    var_4 = python_code_.dfs_Edge(type=var_0, Edge6=var_0, edges=None)
    assert isinstance(var_4, python_code_.dfs_Edge)


@pytest.mark.xfail(strict=True)
def test_28():
    var_0 = "j'j^#3_Z%Y93J1\r"
    var_4 = python_code_.dfs_EdgeProcessor(dfs_EdgeProcessor0=var_0)
    assert isinstance(var_4, python_code_.dfs_EdgeProcessor)
    python_code_.dfs_EdgeProcessor(dfs_EdgeProcessor=var_4, dfs_EdgeProcessor0=var_4)
    assert isinstance(var_4.dfs_EdgeProcessor0, python_code_.dfs_EdgeProcessor)


def test_29():
    var_15 = python_code_.dfs_Node(
        postTraversal=-2272.95,
        preTraversal={361.71, "\ng"},
        target=b"\xec\x8eS\x01cn\x83\x06\x19\x82",
        Node18=True,
    )
    assert isinstance(var_15, python_code_.dfs_Node)


@pytest.mark.xfail(strict=True)
def test_30():
    var_0 = 5319
    var_1 = python_code_.dfs_DepthFirstSearch(
        postTraversalCounter=b"\x10\xaf$2D\xef\xb5", preTraversalCounter=var_0
    )
    assert isinstance(var_1, python_code_.dfs_DepthFirstSearch)
    var_3 = python_code_.EdgeType.FORWARD_EDGE
    var_4 = python_code_.dfs_EdgeProcessor()
    assert var_4.dfs_EdgeProcessor0 is None
    var_5 = var_4.processEdge(dfs_edge=var_3)
    var_7 = python_code_.dfs_DFSGraph()
    var_8 = python_code_.dfs_Node(
        postTraversal=var_0, preTraversal=var_5, nodes=var_7, source=set(), Node18=var_5
    )
    assert isinstance(var_8, python_code_.dfs_Node)
    var_9 = python_code_.dfs_DFSGraph()
    var_10 = python_code_.dfs_Edge(
        type={"&5n;": "Ox^XM|01zwNsN\rpae!p"},
        Edge=var_8,
        Edge6="G<d",
        outgoing="2T{8{Is#?@B",
        edges=var_9,
    )
    assert var_10.outgoing == "2T{8{Is#?@B"
    var_4.processNode(dfs_node=("1vQl", "BU:[|YVG=Tg`S^N'", "_dfs_Node__source"))
    var_12 = 3
    python_code_.dfs_Node(postTraversal=-2602.56, preTraversal=var_12, Node=var_10)


@pytest.mark.xfail(strict=True)
def test_31():
    var_9 = lambda *args, **kwargs: ["dfs_Edge:DFSGraph8:incoming:dfs_EObject"]
    var_10 = python_code_.dfs_EdgeProcessor(dfs_EdgeProcessor=var_9)
    assert isinstance(var_10, python_code_.dfs_EdgeProcessor)
    python_code_.dfs_EdgeProcessor(dfs_EdgeProcessor0=var_10)


@pytest.mark.xfail(strict=True)
def test_32():
    var_16 = -3851
    var_0 = python_code_.dfs_Node(
        postTraversal=469, preTraversal=var_16, nodes=var_16, dfs_Node=var_16
    )
    assert isinstance(var_0, python_code_.dfs_Node)
    var_20 = abs
    var_21 = 3
    var_22 = python_code_.dfs_DepthFirstSearch(
        postTraversalCounter=var_0, preTraversalCounter=var_21
    )
    assert isinstance(var_22, python_code_.dfs_DepthFirstSearch)
    var_23 = var_22.incrementPreTraversalCounter()
    var_24 = python_code_.dfs_EObject()
    var_25 = python_code_.dfs_Node(
        postTraversal=var_16,
        preTraversal=var_20,
        target=var_23,
        nodes=var_21,
        dfs_Node=var_24,
        Node=var_21,
    )
    assert isinstance(var_25, python_code_.dfs_Node)
    var_26 = "E5U,;N"
    var_27 = python_code_.dfs_DFSGraph()
    python_code_.dfs_Edge(
        type=var_26,
        Edge=var_20,
        Edge6=var_0,
        outgoing=var_25,
        dfs_Edge=var_16,
        incoming=var_20,
        Edge15=var_25,
        edges=var_27,
    )


@pytest.mark.xfail(strict=True)
def test_33():
    var_16 = -3829
    var_20 = python_code_.dfs_Edge(type=var_16, Edge=False, incoming=var_16)
    assert isinstance(var_20, python_code_.dfs_Edge)
    python_code_.dfs_Node(
        postTraversal=var_16, preTraversal=-2709.31, Node=var_16, Node13=var_20
    )


@pytest.mark.xfail(strict=True)
def test_34():
    python_code_.dfs_Edge(type="[g\n", Edge6=None, outgoing=None, dfs_Edge=None)
    var_30 = python_code_.dfs_Node
    var_31 = python_code_.dfs_Edge(type=3704, Edge=var_30, Edge6=var_30)
    assert isinstance(var_31, python_code_.dfs_Edge)
    var_32 = -1
    var_33 = python_code_.dfs_DepthFirstSearch(
        postTraversalCounter={False, False, "_dfs_Edge__Edge15._dfs_Node__nodes"},
        preTraversalCounter=var_32,
    )
    assert isinstance(var_33, python_code_.dfs_DepthFirstSearch)
    var_33.processNode(dfs_node=3086.5)
    var_35 = python_code_.dfs_EdgeProcessor()
    python_code_.dfs_EdgeProcessor(dfs_EdgeProcessor=var_35)
    assert isinstance(var_35.dfs_EdgeProcessor0, python_code_.dfs_EdgeProcessor)


@pytest.mark.xfail(strict=True)
def test_35():
    var_18 = python_code_.dfs_Edge(type="l0;Q", dfs_Edge=None)
    var_19 = 1851
    python_code_.dfs_Node(
        postTraversal=var_19, preTraversal=1, source={var_18, -1}, Node13=var_18
    )
