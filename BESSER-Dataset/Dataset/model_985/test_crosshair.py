from python_code import cfg_cfg
from python_code import cfg_edge
from python_code import cfg_node

def test_cfg_node___init__():
    assert cfg_node.__init__(cfg_node('', cfg_node=cfg_cfg(), cfg_node4=cfg_edge(), target=set(), source=set(), node=cfg_edge(), cfg_node12=cfg_edge(), node14=cfg_edge()), '', cfg_node=cfg_cfg(), cfg_node4=cfg_edge(), target=set(), source=set(), node=cfg_edge(), cfg_node12=cfg_edge(), node14=cfg_edge()) == None

