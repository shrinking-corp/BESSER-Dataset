from python_code import units_Angle

def test_units_Angle___init__():
    assert units_Angle.__init__(units_Angle()) == None

def test_units_Angle_toRad():
    assert units_Angle.toRad(units_Angle()) == None

def test_units_Angle_print():
    assert units_Angle.print(units_Angle()) == None


from python_code import units_AngleUnit

def test_units_AngleUnit___init__():
    assert units_AngleUnit.__init__(units_AngleUnit()) == None

def test_units_AngleUnit_toRad():
    assert units_AngleUnit.toRad(units_AngleUnit(), '') == None


from python_code import units_Centimeter

def test_units_Centimeter___init__():
    assert units_Centimeter.__init__(units_Centimeter()) == None

def test_units_Centimeter_toCm():
    assert units_Centimeter.toCm(units_Centimeter(), '') == None

def test_units_Centimeter_getSymbol():
    assert units_Centimeter.getSymbol(units_Centimeter()) == None


from python_code import units_Degree

def test_units_Degree___init__():
    assert units_Degree.__init__(units_Degree()) == None

def test_units_Degree_getSymbol():
    assert units_Degree.getSymbol(units_Degree()) == None

def test_units_Degree_toRad():
    assert units_Degree.toRad(units_Degree(), '') == None


from python_code import units_Foot

def test_units_Foot___init__():
    assert units_Foot.__init__(units_Foot()) == None

def test_units_Foot_getSymbol():
    assert units_Foot.getSymbol(units_Foot()) == None

def test_units_Foot_toCm():
    assert units_Foot.toCm(units_Foot(), '') == None


from python_code import units_Gradian

def test_units_Gradian___init__():
    assert units_Gradian.__init__(units_Gradian()) == None

def test_units_Gradian_getSymbol():
    assert units_Gradian.getSymbol(units_Gradian()) == None

def test_units_Gradian_toRad():
    assert units_Gradian.toRad(units_Gradian(), '') == None


from python_code import units_Inch

def test_units_Inch___init__():
    assert units_Inch.__init__(units_Inch()) == None

def test_units_Inch_getSymbol():
    assert units_Inch.getSymbol(units_Inch()) == None

def test_units_Inch_toCm():
    assert units_Inch.toCm(units_Inch(), '') == None


from python_code import units_Length

def test_units_Length___init__():
    assert units_Length.__init__(units_Length()) == None

def test_units_Length_print():
    assert units_Length.print(units_Length()) == None

def test_units_Length_toCm():
    assert units_Length.toCm(units_Length()) == None


from python_code import units_LengthUnit

def test_units_LengthUnit___init__():
    assert units_LengthUnit.__init__(units_LengthUnit()) == None

def test_units_LengthUnit_toCm():
    assert units_LengthUnit.toCm(units_LengthUnit(), '') == None


from python_code import units_Meter

def test_units_Meter___init__():
    assert units_Meter.__init__(units_Meter()) == None

def test_units_Meter_toCm():
    assert units_Meter.toCm(units_Meter(), '') == None

def test_units_Meter_getSymbol():
    assert units_Meter.getSymbol(units_Meter()) == None


from python_code import units_Millimeter

def test_units_Millimeter___init__():
    assert units_Millimeter.__init__(units_Millimeter()) == None

def test_units_Millimeter_toCm():
    assert units_Millimeter.toCm(units_Millimeter(), '') == None

def test_units_Millimeter_getSymbol():
    assert units_Millimeter.getSymbol(units_Millimeter()) == None


from python_code import units_Radian

def test_units_Radian___init__():
    assert units_Radian.__init__(units_Radian()) == None

def test_units_Radian_toRad():
    assert units_Radian.toRad(units_Radian(), '') == None

def test_units_Radian_getSymbol():
    assert units_Radian.getSymbol(units_Radian()) == None


from python_code import units_Turn

def test_units_Turn___init__():
    assert units_Turn.__init__(units_Turn()) == None

def test_units_Turn_getSymbol():
    assert units_Turn.getSymbol(units_Turn()) == None

def test_units_Turn_toRad():
    assert units_Turn.toRad(units_Turn(), '') == None


from python_code import units_Yard

def test_units_Yard___init__():
    assert units_Yard.__init__(units_Yard()) == None

def test_units_Yard_toCm():
    assert units_Yard.toCm(units_Yard(), '') == None

def test_units_Yard_getSymbol():
    assert units_Yard.getSymbol(units_Yard()) == None

