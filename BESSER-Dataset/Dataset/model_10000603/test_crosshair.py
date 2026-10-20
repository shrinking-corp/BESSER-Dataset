from python_code import cpu_ArithmeticExecutableInstruction

def test_cpu_ArithmeticExecutableInstruction___init__():
    assert cpu_ArithmeticExecutableInstruction.__init__(cpu_ArithmeticExecutableInstruction(0, 0, 0), 0, 0, 0) == None


from python_code import cpu_IOExecutableInstruction

def test_cpu_IOExecutableInstruction___init__():
    assert cpu_IOExecutableInstruction.__init__(cpu_IOExecutableInstruction(0, 0, 0), 0, 0, 0) == None


from python_code import memory_Word

def test_memory_Word___init__():
    assert memory_Word.__init__(memory_Word(0, memory1=set()), 0, memory1=set()) == None

