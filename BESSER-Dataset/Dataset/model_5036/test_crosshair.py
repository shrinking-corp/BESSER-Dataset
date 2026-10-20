from python_code import rental_Car

def test_rental_Car___init__():
    assert rental_Car.__init__(rental_Car(''), '') == None


from python_code import rental_Device

def test_rental_Device___init__():
    assert rental_Device.__init__(rental_Device('\x00\x00', 0, 0, 0), '', 0, 0, 0) == None

