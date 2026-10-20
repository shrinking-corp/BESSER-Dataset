from python_code import pimm_AbstractVertex

def test_pimm_AbstractVertex___init__():
    assert pimm_AbstractVertex.__init__(pimm_AbstractVertex(''), '') == None


from python_code import pimm_FunctionPrototype
from python_code import pimm_HRefinement

def test_pimm_FunctionPrototype___init__():
    assert pimm_FunctionPrototype.__init__(pimm_FunctionPrototype('', pimm_FunctionPrototype=pimm_HRefinement(), pimm_FunctionPrototype39=pimm_HRefinement(), pimm_FunctionPrototype41=set()), '', pimm_FunctionPrototype=pimm_HRefinement(), pimm_FunctionPrototype39=pimm_HRefinement(), pimm_FunctionPrototype41=set()) == None


from python_code import pimm_Dependency
from python_code import pimm_ISetter

def test_pimm_ISetter___init__():
    assert pimm_ISetter.__init__(pimm_ISetter(ISetter=pimm_Dependency(), setter=set()), ISetter=pimm_Dependency(), setter=set()) == None

def test_pimm_ISetter_getValue():
    assert pimm_ISetter.getValue(pimm_ISetter(ISetter=pimm_Dependency(), setter=set())) == None


from python_code import pimm_Parameterizable

def test_pimm_Parameterizable___init__():
    assert pimm_Parameterizable.__init__(pimm_Parameterizable(pimm_Parameterizable=set()), pimm_Parameterizable=set()) == None

def test_pimm_Parameterizable_getInputParameters():
    assert pimm_Parameterizable.getInputParameters(pimm_Parameterizable(pimm_Parameterizable=set())) == None


from python_code import pimm_visitor_PiMMVisitable

def test_pimm_visitor_PiMMVisitable___init__():
    assert pimm_visitor_PiMMVisitable.__init__(pimm_visitor_PiMMVisitable()) == None

def test_pimm_visitor_PiMMVisitable_accept():
    assert pimm_visitor_PiMMVisitable.accept(pimm_visitor_PiMMVisitable(), '') == None


from python_code import pimm_visitor_PiMMVisitor

def test_pimm_visitor_PiMMVisitor___init__():
    assert pimm_visitor_PiMMVisitor.__init__(pimm_visitor_PiMMVisitor()) == None

def test_pimm_visitor_PiMMVisitor_visit():
    assert pimm_visitor_PiMMVisitor.visit(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitISetter():
    assert pimm_visitor_PiMMVisitor.visitISetter(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitExpression():
    assert pimm_visitor_PiMMVisitor.visitExpression(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitRoundBufferActor():
    assert pimm_visitor_PiMMVisitor.visitRoundBufferActor(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitFunctionParameter():
    assert pimm_visitor_PiMMVisitor.visitFunctionParameter(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitConfigInputPort():
    assert pimm_visitor_PiMMVisitor.visitConfigInputPort(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitHRefinement():
    assert pimm_visitor_PiMMVisitor.visitHRefinement(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitDataOutputPort():
    assert pimm_visitor_PiMMVisitor.visitDataOutputPort(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitDataPort():
    assert pimm_visitor_PiMMVisitor.visitDataPort(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitDataOutputInterface():
    assert pimm_visitor_PiMMVisitor.visitDataOutputInterface(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitActor():
    assert pimm_visitor_PiMMVisitor.visitActor(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitAbstractVertex():
    assert pimm_visitor_PiMMVisitor.visitAbstractVertex(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitDependency():
    assert pimm_visitor_PiMMVisitor.visitDependency(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitBroadcastActor():
    assert pimm_visitor_PiMMVisitor.visitBroadcastActor(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitConfigOutputPort():
    assert pimm_visitor_PiMMVisitor.visitConfigOutputPort(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitFifo():
    assert pimm_visitor_PiMMVisitor.visitFifo(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitDataInputInterface():
    assert pimm_visitor_PiMMVisitor.visitDataInputInterface(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitForkActor():
    assert pimm_visitor_PiMMVisitor.visitForkActor(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitFunctionPrototype():
    assert pimm_visitor_PiMMVisitor.visitFunctionPrototype(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitJoinActor():
    assert pimm_visitor_PiMMVisitor.visitJoinActor(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitPort():
    assert pimm_visitor_PiMMVisitor.visitPort(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitInterfaceActor():
    assert pimm_visitor_PiMMVisitor.visitInterfaceActor(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitRefinement():
    assert pimm_visitor_PiMMVisitor.visitRefinement(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitPiGraph():
    assert pimm_visitor_PiMMVisitor.visitPiGraph(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitDelay():
    assert pimm_visitor_PiMMVisitor.visitDelay(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitDataInputPort():
    assert pimm_visitor_PiMMVisitor.visitDataInputPort(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitParameterizable():
    assert pimm_visitor_PiMMVisitor.visitParameterizable(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitExecutableActor():
    assert pimm_visitor_PiMMVisitor.visitExecutableActor(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitParameter():
    assert pimm_visitor_PiMMVisitor.visitParameter(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitConfigOutputInterface():
    assert pimm_visitor_PiMMVisitor.visitConfigOutputInterface(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitAbstractActor():
    assert pimm_visitor_PiMMVisitor.visitAbstractActor(pimm_visitor_PiMMVisitor(), '') == None

def test_pimm_visitor_PiMMVisitor_visitConfigInputInterface():
    assert pimm_visitor_PiMMVisitor.visitConfigInputInterface(pimm_visitor_PiMMVisitor(), '') == None

