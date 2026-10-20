from python_code import BankAccount

def test_BankAccount___init__():
    assert BankAccount.__init__(BankAccount('\x00', 0.0), '', 0.0) == None


from python_code import ErrorCode

def test_ErrorCode___init__():
    assert ErrorCode.__init__(ErrorCode(0, 0, 0, 0), 0, 0, 0, 0) == None


from python_code import ErrorCode
from python_code import ErrorCodeException

def test_ErrorCodeException___init__():
    assert ErrorCodeException.__init__(ErrorCodeException(ErrorCode(0, 0, 0, 0), '', ''), ErrorCode(0, 0, 0, 0), '\x00', '') == None

