from python_code import rk_RungeKutta

def test_rk_RungeKutta___init__():
    assert rk_RungeKutta.__init__(rk_RungeKutta(0.0), 0.0) == None

