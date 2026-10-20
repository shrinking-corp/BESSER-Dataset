from python_code import dbmodel_ClassOrDuplicate

def test_dbmodel_ClassOrDuplicate___init__():
    assert dbmodel_ClassOrDuplicate.__init__(dbmodel_ClassOrDuplicate('', '', '\x00\x00'), '', '', '') == None

