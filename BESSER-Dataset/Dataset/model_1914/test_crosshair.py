from python_code import ClassDiagram_ApplianceType_ApplianceService

def test_ClassDiagram_ApplianceType_ApplianceService___init__():
    assert ClassDiagram_ApplianceType_ApplianceService.__init__(ClassDiagram_ApplianceType_ApplianceService('\x00', 0.0), '', 0.0) == None


from python_code import ClassDiagram_IServiceBooking

def test_ClassDiagram_IServiceBooking___init__():
    assert ClassDiagram_IServiceBooking.__init__(ClassDiagram_IServiceBooking()) == None

def test_ClassDiagram_IServiceBooking_cancelBookedService():
    assert ClassDiagram_IServiceBooking.cancelBookedService(ClassDiagram_IServiceBooking(), '') == None

def test_ClassDiagram_IServiceBooking_findBookedService():
    assert ClassDiagram_IServiceBooking.findBookedService(ClassDiagram_IServiceBooking(), '') == None

def test_ClassDiagram_IServiceBooking_bookFacilityService():
    assert ClassDiagram_IServiceBooking.bookFacilityService(ClassDiagram_IServiceBooking(), '', '', '', '', '') == None

def test_ClassDiagram_IServiceBooking_getBookedServices():
    assert ClassDiagram_IServiceBooking.getBookedServices(ClassDiagram_IServiceBooking(), '') == None

def test_ClassDiagram_IServiceBooking_findAvailableServices():
    assert ClassDiagram_IServiceBooking.findAvailableServices(ClassDiagram_IServiceBooking(), '', '') == None

