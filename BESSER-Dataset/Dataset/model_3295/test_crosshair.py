from python_code import standard_DemographicPopulationModel
from python_code import standard_PopulationGroup

def test_standard_PopulationGroup___init__():
    assert standard_PopulationGroup.__init__(standard_PopulationGroup('\x00', 0.0, standard_PopulationGroup=standard_DemographicPopulationModel()), '', 0.0, standard_PopulationGroup=standard_DemographicPopulationModel()) == None


from python_code import standard_PopulationInitializer

def test_standard_PopulationInitializer___init__():
    assert standard_PopulationInitializer.__init__(standard_PopulationInitializer('', '\x00'), '\x00\x00', '') == None


from python_code import standard_PopulationModel

def test_standard_PopulationModel___init__():
    assert standard_PopulationModel.__init__(standard_PopulationModel('', '', '\x00\x00'), '', '', '') == None


from python_code import standard_PopulationLabel
from python_code import standard_PopulationModelLabel

def test_standard_PopulationModelLabel___init__():
    assert standard_PopulationModelLabel.__init__(standard_PopulationModelLabel('', standard_PopulationModelLabel=standard_PopulationLabel()), '', standard_PopulationModelLabel=standard_PopulationLabel()) == None


from python_code import standard_SeasonalPopulationModel

def test_standard_SeasonalPopulationModel___init__():
    assert standard_SeasonalPopulationModel.__init__(standard_SeasonalPopulationModel(0.0, 0.0, 0.0, True), 0.0, 0.0, 0.0, True) == None


from python_code import standard_StandardPopulationInitializer

def test_standard_StandardPopulationInitializer___init__():
    assert standard_StandardPopulationInitializer.__init__(standard_StandardPopulationInitializer(0.0, False), 0.0, False) == None


from python_code import standard_StandardPopulationModel

def test_standard_StandardPopulationModel___init__():
    assert standard_StandardPopulationModel.__init__(standard_StandardPopulationModel(0.0, 0.0, ''), 0.0, 0.0, '') == None


from python_code import standard_StandardPopulationModelLabel
from python_code import standard_StandardPopulationModelLabelValue

def test_standard_StandardPopulationModelLabelValue___init__():
    assert standard_StandardPopulationModelLabelValue.__init__(standard_StandardPopulationModelLabelValue(0.0, 0.0, 0.0, 0.0, 0.0, standard_StandardPopulationModelLabelValue=standard_StandardPopulationModelLabel(), standard_StandardPopulationModelLabelValue4=standard_StandardPopulationModelLabel(), standard_StandardPopulationModelLabelValue7=standard_StandardPopulationModelLabel(), standard_StandardPopulationModelLabelValue10=standard_StandardPopulationModelLabel(), standard_StandardPopulationModelLabelValue13=standard_StandardPopulationModelLabel()), 0.0, 0.0, 0.0, 0.0, 0.0, standard_StandardPopulationModelLabelValue=standard_StandardPopulationModelLabel(), standard_StandardPopulationModelLabelValue4=standard_StandardPopulationModelLabel(), standard_StandardPopulationModelLabelValue7=standard_StandardPopulationModelLabel(), standard_StandardPopulationModelLabelValue10=standard_StandardPopulationModelLabel(), standard_StandardPopulationModelLabelValue13=standard_StandardPopulationModelLabel()) == None

def test_standard_StandardPopulationModelLabelValue_adjustDelta():
    assert standard_StandardPopulationModelLabelValue.adjustDelta(standard_StandardPopulationModelLabelValue(0.0, 0.0, 0.0, 0.0, 0.0, standard_StandardPopulationModelLabelValue=standard_StandardPopulationModelLabel(), standard_StandardPopulationModelLabelValue4=standard_StandardPopulationModelLabel(), standard_StandardPopulationModelLabelValue7=standard_StandardPopulationModelLabel(), standard_StandardPopulationModelLabelValue10=standard_StandardPopulationModelLabel(), standard_StandardPopulationModelLabelValue13=standard_StandardPopulationModelLabel()), '') == None


from python_code import standard_StochasticStandardPopulationModel

def test_standard_StochasticStandardPopulationModel___init__():
    assert standard_StochasticStandardPopulationModel.__init__(standard_StochasticStandardPopulationModel(0.0), 0.0) == None

