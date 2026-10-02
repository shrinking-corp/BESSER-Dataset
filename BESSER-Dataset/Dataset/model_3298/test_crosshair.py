from python_code import standard_DiseaseModel

def test_standard_DiseaseModel___init__():
    assert standard_DiseaseModel.__init__(standard_DiseaseModel(0.0, '', '', '', 0.0, False, False, 0.0), 0.0, '', '', '\x00', 0.0, False, False, 0.0) == None

def test_standard_DiseaseModel_initializeDiseaseState():
    assert standard_DiseaseModel.initializeDiseaseState(standard_DiseaseModel(0.0, '', '', '', 0.0, False, False, 0.0), '') == None

def test_standard_DiseaseModel_createDiseaseModelLabel():
    assert standard_DiseaseModel.createDiseaseModelLabel(standard_DiseaseModel(0.0, '', '', '', 0.0, False, False, 0.0)) == None

def test_standard_DiseaseModel_getAdjustedBackgroundMortalityRate():
    assert standard_DiseaseModel.getAdjustedBackgroundMortalityRate(standard_DiseaseModel(0.0, '', '', '', 0.0, False, False, 0.0), '') == None

def test_standard_DiseaseModel_createDiseaseModelLabelValue():
    assert standard_DiseaseModel.createDiseaseModelLabelValue(standard_DiseaseModel(0.0, '', '', '', 0.0, False, False, 0.0)) == None

def test_standard_DiseaseModel_getAdjustedBackgroundBirthRate():
    assert standard_DiseaseModel.getAdjustedBackgroundBirthRate(standard_DiseaseModel(0.0, '', '', '', 0.0, False, False, 0.0), '') == None

def test_standard_DiseaseModel_createInfector():
    assert standard_DiseaseModel.createInfector(standard_DiseaseModel(0.0, '', '', '', 0.0, False, False, 0.0)) == None

def test_standard_DiseaseModel_createDiseaseModelState():
    assert standard_DiseaseModel.createDiseaseModelState(standard_DiseaseModel(0.0, '', '', '', 0.0, False, False, 0.0)) == None

from python_code import standard_DiseaseModelLabelValue

def test_standard_DiseaseModelLabelValue___init__():
    assert standard_DiseaseModelLabelValue.__init__(standard_DiseaseModelLabelValue(0.0, 0.0, 0.0), 0.0, 0.0, 0.0) == None

def test_standard_DiseaseModelLabelValue_add():
    assert standard_DiseaseModelLabelValue.add(standard_DiseaseModelLabelValue(0.0, 0.0, 0.0), '') == None

def test_standard_DiseaseModelLabelValue_set():
    assert standard_DiseaseModelLabelValue.set(standard_DiseaseModelLabelValue(0.0, 0.0, 0.0), '') == None

def test_standard_DiseaseModelLabelValue_sub():
    assert standard_DiseaseModelLabelValue.sub(standard_DiseaseModelLabelValue(0.0, 0.0, 0.0), '') == None

def test_standard_DiseaseModelLabelValue_scale():
    assert standard_DiseaseModelLabelValue.scale(standard_DiseaseModelLabelValue(0.0, 0.0, 0.0), '') == None

def test_standard_DiseaseModelLabelValue_zeroOutPopulationCount():
    assert standard_DiseaseModelLabelValue.zeroOutPopulationCount(standard_DiseaseModelLabelValue(0.0, 0.0, 0.0)) == None

from python_code import standard_IntegrationDecorator

def test_standard_IntegrationDecorator___init__():
    assert standard_IntegrationDecorator.__init__(standard_IntegrationDecorator()) == None

def test_standard_IntegrationDecorator_isDeterministic():
    assert standard_IntegrationDecorator.isDeterministic(standard_IntegrationDecorator()) == None

from python_code import standard_SEIR

def test_standard_SEIR___init__():
    assert standard_SEIR.__init__(standard_SEIR(0.0), 0.0) == None

def test_standard_SEIR_getAdjustedIncubationRate():
    assert standard_SEIR.getAdjustedIncubationRate(standard_SEIR(0.0), '') == None

from python_code import standard_SEIRLabel
from python_code import standard_SEIRLabelValue

def test_standard_SEIRLabelValue___init__():
    assert standard_SEIRLabelValue.__init__(standard_SEIRLabelValue(0.0, standard_SEIRLabelValue=standard_SEIRLabel(), standard_SEIRLabelValue12=standard_SEIRLabel(), standard_SEIRLabelValue15=standard_SEIRLabel(), standard_SEIRLabelValue21=standard_SEIRLabel(), standard_SEIRLabelValue18=standard_SEIRLabel()), 0.0, standard_SEIRLabelValue=standard_SEIRLabel(), standard_SEIRLabelValue12=standard_SEIRLabel(), standard_SEIRLabelValue15=standard_SEIRLabel(), standard_SEIRLabelValue21=standard_SEIRLabel(), standard_SEIRLabelValue18=standard_SEIRLabel()) == None

from python_code import standard_SIInfector

def test_standard_SIInfector___init__():
    assert standard_SIInfector.__init__(standard_SIInfector(0.0), 0.0) == None

from python_code import standard_SILabel
from python_code import standard_SILabelValue

def test_standard_SILabelValue___init__():
    assert standard_SILabelValue.__init__(standard_SILabelValue(0.0, standard_SILabelValue=standard_SILabel(), standard_SILabelValue25=standard_SILabel(), standard_SILabelValue28=standard_SILabel(), standard_SILabelValue31=standard_SILabel(), standard_SILabelValue34=standard_SILabel()), 0.0, standard_SILabelValue=standard_SILabel(), standard_SILabelValue25=standard_SILabel(), standard_SILabelValue28=standard_SILabel(), standard_SILabelValue31=standard_SILabel(), standard_SILabelValue34=standard_SILabel()) == None

from python_code import standard_SIR

def test_standard_SIR___init__():
    assert standard_SIR.__init__(standard_SIR(0.0), 0.0) == None

def test_standard_SIR_getAdjustedImmunityLossRate():
    assert standard_SIR.getAdjustedImmunityLossRate(standard_SIR(0.0), '') == None

from python_code import standard_SIRInoculator

def test_standard_SIRInoculator___init__():
    assert standard_SIRInoculator.__init__(standard_SIRInoculator(0.0, False), 0.0, False) == None

from python_code import standard_SIRLabel
from python_code import standard_SIRLabelValue

def test_standard_SIRLabelValue___init__():
    assert standard_SIRLabelValue.__init__(standard_SIRLabelValue(0.0, standard_SIRLabelValue=standard_SIRLabel(), standard_SIRLabelValue38=standard_SIRLabel(), standard_SIRLabelValue41=standard_SIRLabel(), standard_SIRLabelValue44=standard_SIRLabel(), standard_SIRLabelValue47=standard_SIRLabel()), 0.0, standard_SIRLabelValue=standard_SIRLabel(), standard_SIRLabelValue38=standard_SIRLabel(), standard_SIRLabelValue41=standard_SIRLabel(), standard_SIRLabelValue44=standard_SIRLabel(), standard_SIRLabelValue47=standard_SIRLabel()) == None

from python_code import standard_StandardDiseaseModelLabelValue

def test_standard_StandardDiseaseModelLabelValue___init__():
    assert standard_StandardDiseaseModelLabelValue.__init__(standard_StandardDiseaseModelLabelValue(0.0), 0.0) == None

from python_code import standard_StandardDiseaseModelState

def test_standard_StandardDiseaseModelState___init__():
    assert standard_StandardDiseaseModelState.__init__(standard_StandardDiseaseModelState(0.0), 0.0) == None

from python_code import standard_StandardStochasticDiseaseModel

def test_standard_StandardStochasticDiseaseModel___init__():
    assert standard_StandardStochasticDiseaseModel.__init__(standard_StandardStochasticDiseaseModel(0.0), 0.0) == None

def test_standard_StandardStochasticDiseaseModel_computeNoise():
    assert standard_StandardStochasticDiseaseModel.computeNoise(standard_StandardStochasticDiseaseModel(0.0)) == None

from python_code import standard_StochasticDiseaseModel

def test_standard_StochasticDiseaseModel___init__():
    assert standard_StochasticDiseaseModel.__init__(standard_StochasticDiseaseModel('', '\x00'), '\x00\x00', '') == None
