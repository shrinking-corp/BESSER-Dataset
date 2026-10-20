from python_code import sequence_description_DelimitedEventMapping
from python_code import sequence_tool_ReorderTool

def test_sequence_description_DelimitedEventMapping___init__():
    assert sequence_description_DelimitedEventMapping.__init__(sequence_description_DelimitedEventMapping('', '\x00', EventMapping=sequence_tool_ReorderTool()), '\x00\x00', '', EventMapping=sequence_tool_ReorderTool()) == None


from python_code import sequence_description_FrameMapping

def test_sequence_description_FrameMapping___init__():
    assert sequence_description_FrameMapping.__init__(sequence_description_FrameMapping('', '\x00'), '\x00\x00', '') == None


from python_code import sequence_description_MessageMapping

def test_sequence_description_MessageMapping___init__():
    assert sequence_description_MessageMapping.__init__(sequence_description_MessageMapping('', '\x00'), '\x00\x00', '') == None


from python_code import sequence_description_ReturnMessageMapping

def test_sequence_description_ReturnMessageMapping___init__():
    assert sequence_description_ReturnMessageMapping.__init__(sequence_description_ReturnMessageMapping(''), '') == None


from python_code import sequence_description_SequenceDiagramDescription

def test_sequence_description_SequenceDiagramDescription___init__():
    assert sequence_description_SequenceDiagramDescription.__init__(sequence_description_SequenceDiagramDescription('', '\x00'), '\x00\x00', '') == None


from python_code import sequence_ordering_CompoundEventEnd
from python_code import sequence_ordering_EventEndsOrdering

def test_sequence_ordering_CompoundEventEnd___init__():
    assert sequence_ordering_CompoundEventEnd.__init__(sequence_ordering_CompoundEventEnd(sequence_ordering_CompoundEventEnd=set(), EventEnd=sequence_ordering_EventEndsOrdering()), sequence_ordering_CompoundEventEnd=set(), EventEnd=sequence_ordering_EventEndsOrdering()) == None

def test_sequence_ordering_CompoundEventEnd_getSemanticEvents():
    assert sequence_ordering_CompoundEventEnd.getSemanticEvents(sequence_ordering_CompoundEventEnd(sequence_ordering_CompoundEventEnd=set(), EventEnd=sequence_ordering_EventEndsOrdering())) == None


from python_code import ordering_sequence_EObject
from python_code import sequence_ordering_EventEndsOrdering
from python_code import sequence_ordering_SingleEventEnd

def test_sequence_ordering_SingleEventEnd___init__():
    assert sequence_ordering_SingleEventEnd.__init__(sequence_ordering_SingleEventEnd(True, sequence_ordering_SingleEventEnd=ordering_sequence_EObject(), EventEnd=sequence_ordering_EventEndsOrdering()), False, sequence_ordering_SingleEventEnd=ordering_sequence_EObject(), EventEnd=sequence_ordering_EventEndsOrdering()) == None


from python_code import sequence_template_TAbstractMapping

def test_sequence_template_TAbstractMapping___init__():
    assert sequence_template_TAbstractMapping.__init__(sequence_template_TAbstractMapping('', '', '\x00\x00'), '', '', '') == None


from python_code import TExecutionStyle
from python_code import sequence_template_TConditionalExecutionStyle

def test_sequence_template_TConditionalExecutionStyle___init__():
    assert sequence_template_TConditionalExecutionStyle.__init__(sequence_template_TConditionalExecutionStyle('', sequence_template_TConditionalExecutionStyle=TExecutionStyle()), '', sequence_template_TConditionalExecutionStyle=TExecutionStyle()) == None


from python_code import TLifelineStyle
from python_code import sequence_template_TConditionalLifelineStyle

def test_sequence_template_TConditionalLifelineStyle___init__():
    assert sequence_template_TConditionalLifelineStyle.__init__(sequence_template_TConditionalLifelineStyle('', sequence_template_TConditionalLifelineStyle=TLifelineStyle()), '', sequence_template_TConditionalLifelineStyle=TLifelineStyle()) == None


from python_code import TMessageStyle
from python_code import sequence_template_TConditionalMessageStyle

def test_sequence_template_TConditionalMessageStyle___init__():
    assert sequence_template_TConditionalMessageStyle.__init__(sequence_template_TConditionalMessageStyle('', sequence_template_TConditionalMessageStyle=TMessageStyle()), '', sequence_template_TConditionalMessageStyle=TMessageStyle()) == None


from python_code import TExecutionStyle
from python_code import sequence_template_TExecutionMapping

def test_sequence_template_TExecutionMapping___init__():
    assert sequence_template_TExecutionMapping.__init__(sequence_template_TExecutionMapping('', '', False, sequence_template_TExecutionMapping68=set(), sequence_template_TExecutionMapping=set(), sequence_template_TExecutionMapping66=TExecutionStyle()), '', '', False, sequence_template_TExecutionMapping68=set(), sequence_template_TExecutionMapping=set(), sequence_template_TExecutionMapping66=TExecutionStyle()) == None


from python_code import ColorDescription
from python_code import sequence_template_TExecutionStyle

def test_sequence_template_TExecutionStyle___init__():
    assert sequence_template_TExecutionStyle.__init__(sequence_template_TExecutionStyle('', sequence_template_TExecutionStyle=ColorDescription(), sequence_template_TExecutionStyle72=ColorDescription()), '', sequence_template_TExecutionStyle=ColorDescription(), sequence_template_TExecutionStyle72=ColorDescription()) == None


from python_code import TLifelineStyle
from python_code import sequence_template_TLifelineMapping
from python_code import style_NodeStyleDescription

def test_sequence_template_TLifelineMapping___init__():
    assert sequence_template_TLifelineMapping.__init__(sequence_template_TLifelineMapping('', sequence_template_TLifelineMapping=set(), sequence_template_TLifelineMapping52=style_NodeStyleDescription(), sequence_template_TLifelineMapping54=TLifelineStyle(), sequence_template_TLifelineMapping56=style_NodeStyleDescription(), sequence_template_TLifelineMapping59=set()), '', sequence_template_TLifelineMapping=set(), sequence_template_TLifelineMapping52=style_NodeStyleDescription(), sequence_template_TLifelineMapping54=TLifelineStyle(), sequence_template_TLifelineMapping56=style_NodeStyleDescription(), sequence_template_TLifelineMapping59=set()) == None


from python_code import ColorDescription
from python_code import sequence_template_TLifelineStyle

def test_sequence_template_TLifelineStyle___init__():
    assert sequence_template_TLifelineStyle.__init__(sequence_template_TLifelineStyle('', sequence_template_TLifelineStyle=ColorDescription()), '', sequence_template_TLifelineStyle=ColorDescription()) == None


from python_code import TMessageStyle
from python_code import sequence_template_TMessageMapping

def test_sequence_template_TMessageMapping___init__():
    assert sequence_template_TMessageMapping.__init__(sequence_template_TMessageMapping('\x00\x00', '', sequence_template_TMessageMapping=TMessageStyle(), sequence_template_TMessageMapping78=set()), '', '', sequence_template_TMessageMapping=TMessageStyle(), sequence_template_TMessageMapping78=set()) == None


from python_code import ColorDescription
from python_code import sequence_template_TMessageStyle

def test_sequence_template_TMessageStyle___init__():
    assert sequence_template_TMessageStyle.__init__(sequence_template_TMessageStyle('\x00\x00', '', '', '', sequence_template_TMessageStyle=ColorDescription()), '', '', '', '', sequence_template_TMessageStyle=ColorDescription()) == None


from python_code import TBasicMessageMapping
from python_code import sequence_template_TReturnMessageMapping
from python_code import sequence_template_TSequenceDiagram

def test_sequence_template_TReturnMessageMapping___init__():
    assert sequence_template_TReturnMessageMapping.__init__(sequence_template_TReturnMessageMapping('', sequence_template_TReturnMessageMapping=TBasicMessageMapping(), TMessageMapping=sequence_template_TSequenceDiagram('', '', sequence_template_TSequenceDiagram=set(), sequence_template_TSequenceDiagram49=set())), '', sequence_template_TReturnMessageMapping=TBasicMessageMapping(), TMessageMapping=sequence_template_TSequenceDiagram('', '', sequence_template_TSequenceDiagram=set(), sequence_template_TSequenceDiagram49=set())) == None


from python_code import sequence_template_TSequenceDiagram

def test_sequence_template_TSequenceDiagram___init__():
    assert sequence_template_TSequenceDiagram.__init__(sequence_template_TSequenceDiagram('', '', sequence_template_TSequenceDiagram=set(), sequence_template_TSequenceDiagram49=set()), '', '', sequence_template_TSequenceDiagram=set(), sequence_template_TSequenceDiagram49=set()) == None


from python_code import sequence_template_TSequenceDiagram
from python_code import sequence_template_TSourceTargetMessageMapping

def test_sequence_template_TSourceTargetMessageMapping___init__():
    assert sequence_template_TSourceTargetMessageMapping.__init__(sequence_template_TSourceTargetMessageMapping('\x00', '', False, sequence_template_TSourceTargetMessageMapping=set(), TMessageMapping=sequence_template_TSequenceDiagram('', '', sequence_template_TSequenceDiagram=set(), sequence_template_TSequenceDiagram49=set())), '', '', False, sequence_template_TSourceTargetMessageMapping=set(), TMessageMapping=sequence_template_TSequenceDiagram('', '', sequence_template_TSequenceDiagram=set(), sequence_template_TSequenceDiagram49=set())) == None

