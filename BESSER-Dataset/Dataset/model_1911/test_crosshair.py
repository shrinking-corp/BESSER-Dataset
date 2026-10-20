from python_code import ClassDiagram_ApplianceType_ApplianceService

def test_ClassDiagram_ApplianceType_ApplianceService___init__():
    assert ClassDiagram_ApplianceType_ApplianceService.__init__(ClassDiagram_ApplianceType_ApplianceService('\x00', 0.0), '', 0.0) == None


from python_code import ClassDiagram_BookingManager

def test_ClassDiagram_BookingManager___init__():
    assert ClassDiagram_BookingManager.__init__(ClassDiagram_BookingManager()) == None

def test_ClassDiagram_BookingManager_checkIn():
    assert ClassDiagram_BookingManager.checkIn(ClassDiagram_BookingManager(), '') == None

def test_ClassDiagram_BookingManager_assignKey():
    assert ClassDiagram_BookingManager.assignKey(ClassDiagram_BookingManager(), '', '', '') == None

def test_ClassDiagram_BookingManager_findBooking():
    assert ClassDiagram_BookingManager.findBooking(ClassDiagram_BookingManager(), '', '') == None

def test_ClassDiagram_BookingManager_checkOut():
    assert ClassDiagram_BookingManager.checkOut(ClassDiagram_BookingManager(), '') == None


from python_code import ClassDiagram_Booking_Bill

def test_ClassDiagram_Booking_Bill___init__():
    assert ClassDiagram_Booking_Bill.__init__(ClassDiagram_Booking_Bill(0.0, ClassDiagram_Booking_Bill=set()), 0.0, ClassDiagram_Booking_Bill=set()) == None


from python_code import ClassDiagram_Facility_FacilityService

def test_ClassDiagram_Facility_FacilityService___init__():
    assert ClassDiagram_Facility_FacilityService.__init__(ClassDiagram_Facility_FacilityService('\x00', 0.0), '', 0.0) == None


from python_code import ClassDiagram_IApplianceAdministration

def test_ClassDiagram_IApplianceAdministration___init__():
    assert ClassDiagram_IApplianceAdministration.__init__(ClassDiagram_IApplianceAdministration()) == None

def test_ClassDiagram_IApplianceAdministration_removeAppliance():
    assert ClassDiagram_IApplianceAdministration.removeAppliance(ClassDiagram_IApplianceAdministration(), '') == None

def test_ClassDiagram_IApplianceAdministration_editApplianceType():
    assert ClassDiagram_IApplianceAdministration.editApplianceType(ClassDiagram_IApplianceAdministration(), '') == None

def test_ClassDiagram_IApplianceAdministration_addApplianceService():
    assert ClassDiagram_IApplianceAdministration.addApplianceService(ClassDiagram_IApplianceAdministration(), '', '') == None

def test_ClassDiagram_IApplianceAdministration_editAppliance():
    assert ClassDiagram_IApplianceAdministration.editAppliance(ClassDiagram_IApplianceAdministration(), '') == None

def test_ClassDiagram_IApplianceAdministration_addAppliance():
    assert ClassDiagram_IApplianceAdministration.addAppliance(ClassDiagram_IApplianceAdministration(), '') == None

def test_ClassDiagram_IApplianceAdministration_removeApplianceType():
    assert ClassDiagram_IApplianceAdministration.removeApplianceType(ClassDiagram_IApplianceAdministration(), '') == None

def test_ClassDiagram_IApplianceAdministration_removeApplianceService():
    assert ClassDiagram_IApplianceAdministration.removeApplianceService(ClassDiagram_IApplianceAdministration(), '') == None

def test_ClassDiagram_IApplianceAdministration_editApplianceService():
    assert ClassDiagram_IApplianceAdministration.editApplianceService(ClassDiagram_IApplianceAdministration(), '') == None

def test_ClassDiagram_IApplianceAdministration_addApplianceType():
    assert ClassDiagram_IApplianceAdministration.addApplianceType(ClassDiagram_IApplianceAdministration(), '') == None


from python_code import ClassDiagram_IBillManager

def test_ClassDiagram_IBillManager___init__():
    assert ClassDiagram_IBillManager.__init__(ClassDiagram_IBillManager()) == None

def test_ClassDiagram_IBillManager_getAmount():
    assert ClassDiagram_IBillManager.getAmount(ClassDiagram_IBillManager(), '') == None

def test_ClassDiagram_IBillManager_pay():
    assert ClassDiagram_IBillManager.pay(ClassDiagram_IBillManager(), '', '') == None

def test_ClassDiagram_IBillManager_findBill():
    assert ClassDiagram_IBillManager.findBill(ClassDiagram_IBillManager(), '') == None

def test_ClassDiagram_IBillManager_createReceipt():
    assert ClassDiagram_IBillManager.createReceipt(ClassDiagram_IBillManager(), '') == None

def test_ClassDiagram_IBillManager_addPurchesedService():
    assert ClassDiagram_IBillManager.addPurchesedService(ClassDiagram_IBillManager(), '', '', '') == None


from python_code import ClassDiagram_IBooking

def test_ClassDiagram_IBooking___init__():
    assert ClassDiagram_IBooking.__init__(ClassDiagram_IBooking()) == None

def test_ClassDiagram_IBooking_getBookings():
    assert ClassDiagram_IBooking.getBookings(ClassDiagram_IBooking(), '') == None

def test_ClassDiagram_IBooking_editBooking():
    assert ClassDiagram_IBooking.editBooking(ClassDiagram_IBooking(), '') == None

def test_ClassDiagram_IBooking_cancelBooking():
    assert ClassDiagram_IBooking.cancelBooking(ClassDiagram_IBooking(), '') == None

def test_ClassDiagram_IBooking_findBooking():
    assert ClassDiagram_IBooking.findBooking(ClassDiagram_IBooking(), '') == None

def test_ClassDiagram_IBooking_createBooking():
    assert ClassDiagram_IBooking.createBooking(ClassDiagram_IBooking(), '', '', '', '') == None

def test_ClassDiagram_IBooking_findAvailableRooms():
    assert ClassDiagram_IBooking.findAvailableRooms(ClassDiagram_IBooking(), '', '', '') == None


from python_code import ClassDiagram_IFacilityAdministration

def test_ClassDiagram_IFacilityAdministration___init__():
    assert ClassDiagram_IFacilityAdministration.__init__(ClassDiagram_IFacilityAdministration()) == None

def test_ClassDiagram_IFacilityAdministration_addFacility():
    assert ClassDiagram_IFacilityAdministration.addFacility(ClassDiagram_IFacilityAdministration(), '', '') == None

def test_ClassDiagram_IFacilityAdministration_addService():
    assert ClassDiagram_IFacilityAdministration.addService(ClassDiagram_IFacilityAdministration(), '', '', '') == None

def test_ClassDiagram_IFacilityAdministration_editFacility():
    assert ClassDiagram_IFacilityAdministration.editFacility(ClassDiagram_IFacilityAdministration(), '') == None

def test_ClassDiagram_IFacilityAdministration_removeFacility():
    assert ClassDiagram_IFacilityAdministration.removeFacility(ClassDiagram_IFacilityAdministration(), '') == None

def test_ClassDiagram_IFacilityAdministration_addFacilityType():
    assert ClassDiagram_IFacilityAdministration.addFacilityType(ClassDiagram_IFacilityAdministration(), '') == None

def test_ClassDiagram_IFacilityAdministration_removeService():
    assert ClassDiagram_IFacilityAdministration.removeService(ClassDiagram_IFacilityAdministration(), '') == None

def test_ClassDiagram_IFacilityAdministration_editFacilityType():
    assert ClassDiagram_IFacilityAdministration.editFacilityType(ClassDiagram_IFacilityAdministration(), '') == None

def test_ClassDiagram_IFacilityAdministration_editService():
    assert ClassDiagram_IFacilityAdministration.editService(ClassDiagram_IFacilityAdministration(), '') == None

def test_ClassDiagram_IFacilityAdministration_removeFacilityType():
    assert ClassDiagram_IFacilityAdministration.removeFacilityType(ClassDiagram_IFacilityAdministration(), '') == None


from python_code import ClassDiagram_IFacilityManager

def test_ClassDiagram_IFacilityManager___init__():
    assert ClassDiagram_IFacilityManager.__init__(ClassDiagram_IFacilityManager()) == None

def test_ClassDiagram_IFacilityManager_findBookedService():
    assert ClassDiagram_IFacilityManager.findBookedService(ClassDiagram_IFacilityManager(), '', '') == None

def test_ClassDiagram_IFacilityManager_findBookedServices():
    assert ClassDiagram_IFacilityManager.findBookedServices(ClassDiagram_IFacilityManager(), '') == None


from python_code import ClassDiagram_IGuestManager

def test_ClassDiagram_IGuestManager___init__():
    assert ClassDiagram_IGuestManager.__init__(ClassDiagram_IGuestManager()) == None

def test_ClassDiagram_IGuestManager_editGuestRecord():
    assert ClassDiagram_IGuestManager.editGuestRecord(ClassDiagram_IGuestManager(), '') == None

def test_ClassDiagram_IGuestManager_createGuestRecord():
    assert ClassDiagram_IGuestManager.createGuestRecord(ClassDiagram_IGuestManager(), '', '', '', '', '') == None

def test_ClassDiagram_IGuestManager_removeGuestRecord():
    assert ClassDiagram_IGuestManager.removeGuestRecord(ClassDiagram_IGuestManager(), '') == None

def test_ClassDiagram_IGuestManager_findGuests():
    assert ClassDiagram_IGuestManager.findGuests(ClassDiagram_IGuestManager(), '', '') == None

def test_ClassDiagram_IGuestManager_findGuest():
    assert ClassDiagram_IGuestManager.findGuest(ClassDiagram_IGuestManager(), '') == None


from python_code import ClassDiagram_IHotelAdministration

def test_ClassDiagram_IHotelAdministration___init__():
    assert ClassDiagram_IHotelAdministration.__init__(ClassDiagram_IHotelAdministration()) == None

def test_ClassDiagram_IHotelAdministration_addHotel():
    assert ClassDiagram_IHotelAdministration.addHotel(ClassDiagram_IHotelAdministration()) == None

def test_ClassDiagram_IHotelAdministration_editHotel():
    assert ClassDiagram_IHotelAdministration.editHotel(ClassDiagram_IHotelAdministration()) == None

def test_ClassDiagram_IHotelAdministration_removeHotel():
    assert ClassDiagram_IHotelAdministration.removeHotel(ClassDiagram_IHotelAdministration()) == None


from python_code import ClassDiagram_IRoomAdministration

def test_ClassDiagram_IRoomAdministration___init__():
    assert ClassDiagram_IRoomAdministration.__init__(ClassDiagram_IRoomAdministration()) == None

def test_ClassDiagram_IRoomAdministration_createRoomType():
    assert ClassDiagram_IRoomAdministration.createRoomType(ClassDiagram_IRoomAdministration()) == None

def test_ClassDiagram_IRoomAdministration_editRoomType():
    assert ClassDiagram_IRoomAdministration.editRoomType(ClassDiagram_IRoomAdministration(), '') == None

def test_ClassDiagram_IRoomAdministration_addRoom():
    assert ClassDiagram_IRoomAdministration.addRoom(ClassDiagram_IRoomAdministration(), '', '') == None

def test_ClassDiagram_IRoomAdministration_editRoom():
    assert ClassDiagram_IRoomAdministration.editRoom(ClassDiagram_IRoomAdministration(), '') == None

def test_ClassDiagram_IRoomAdministration_removeRoomType():
    assert ClassDiagram_IRoomAdministration.removeRoomType(ClassDiagram_IRoomAdministration(), '') == None

def test_ClassDiagram_IRoomAdministration_removeRoom():
    assert ClassDiagram_IRoomAdministration.removeRoom(ClassDiagram_IRoomAdministration(), '') == None


from python_code import ClassDiagram_IRoomManager

def test_ClassDiagram_IRoomManager___init__():
    assert ClassDiagram_IRoomManager.__init__(ClassDiagram_IRoomManager()) == None

def test_ClassDiagram_IRoomManager_maintenanceStatus():
    assert ClassDiagram_IRoomManager.maintenanceStatus(ClassDiagram_IRoomManager(), '') == None

def test_ClassDiagram_IRoomManager_getRoomsToClean():
    assert ClassDiagram_IRoomManager.getRoomsToClean(ClassDiagram_IRoomManager()) == None

def test_ClassDiagram_IRoomManager_findRoom():
    assert ClassDiagram_IRoomManager.findRoom(ClassDiagram_IRoomManager(), '') == None

def test_ClassDiagram_IRoomManager_cleaningStatus():
    assert ClassDiagram_IRoomManager.cleaningStatus(ClassDiagram_IRoomManager(), '') == None

def test_ClassDiagram_IRoomManager_getRoomsToMaintain():
    assert ClassDiagram_IRoomManager.getRoomsToMaintain(ClassDiagram_IRoomManager()) == None


from python_code import ClassDiagram_IServiceBooking

def test_ClassDiagram_IServiceBooking___init__():
    assert ClassDiagram_IServiceBooking.__init__(ClassDiagram_IServiceBooking()) == None

def test_ClassDiagram_IServiceBooking_findBookedService():
    assert ClassDiagram_IServiceBooking.findBookedService(ClassDiagram_IServiceBooking(), '') == None

def test_ClassDiagram_IServiceBooking_bookFacilityService():
    assert ClassDiagram_IServiceBooking.bookFacilityService(ClassDiagram_IServiceBooking(), '', '', '', '', '') == None

def test_ClassDiagram_IServiceBooking_cancelBookedService():
    assert ClassDiagram_IServiceBooking.cancelBookedService(ClassDiagram_IServiceBooking(), '') == None

def test_ClassDiagram_IServiceBooking_getBookedServices():
    assert ClassDiagram_IServiceBooking.getBookedServices(ClassDiagram_IServiceBooking(), '') == None

def test_ClassDiagram_IServiceBooking_findAvailableServices():
    assert ClassDiagram_IServiceBooking.findAvailableServices(ClassDiagram_IServiceBooking(), '', '') == None


from python_code import ClassDiagram_IStaffAdministration

def test_ClassDiagram_IStaffAdministration___init__():
    assert ClassDiagram_IStaffAdministration.__init__(ClassDiagram_IStaffAdministration()) == None

def test_ClassDiagram_IStaffAdministration_addStaff():
    assert ClassDiagram_IStaffAdministration.addStaff(ClassDiagram_IStaffAdministration()) == None

def test_ClassDiagram_IStaffAdministration_editStaff():
    assert ClassDiagram_IStaffAdministration.editStaff(ClassDiagram_IStaffAdministration()) == None

def test_ClassDiagram_IStaffAdministration_removeStaff():
    assert ClassDiagram_IStaffAdministration.removeStaff(ClassDiagram_IStaffAdministration()) == None

