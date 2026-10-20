from python_code import zhu_Triggers
from python_code import zhu_TriggersSeparated

def test_zhu_TriggersSeparated___init__():
    assert zhu_TriggersSeparated.__init__(zhu_TriggersSeparated('', '\x00', zhu_TriggersSeparated=zhu_Triggers()), '\x00\x00', '', zhu_TriggersSeparated=zhu_Triggers()) == None

