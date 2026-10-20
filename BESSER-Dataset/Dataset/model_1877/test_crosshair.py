from python_code import Classes_BuisnessLogicLayer_PaymentHandler

def test_Classes_BuisnessLogicLayer_PaymentHandler___init__():
    assert Classes_BuisnessLogicLayer_PaymentHandler.__init__(Classes_BuisnessLogicLayer_PaymentHandler()) == None

def test_Classes_BuisnessLogicLayer_PaymentHandler_makePayment():
    assert Classes_BuisnessLogicLayer_PaymentHandler.makePayment(Classes_BuisnessLogicLayer_PaymentHandler(), '', '') == None


from python_code import Classes_BuisnessLogicLayer_PaymentInfo
from python_code import PaymentHandler

def test_Classes_BuisnessLogicLayer_PaymentInfo___init__():
    assert Classes_BuisnessLogicLayer_PaymentInfo.__init__(Classes_BuisnessLogicLayer_PaymentInfo(False, 0, 0, 0, Classes_BuisnessLogicLayer_PaymentInfo=PaymentHandler()), False, 0, 0, 0, Classes_BuisnessLogicLayer_PaymentInfo=PaymentHandler()) == None


from python_code import Classes_Buissnesslayer_Address

def test_Classes_Buissnesslayer_Address___init__():
    assert Classes_Buissnesslayer_Address.__init__(Classes_Buissnesslayer_Address('\x00\x00', 0, '', ''), '', 0, '', '') == None


from python_code import Classes_Buissnesslayer_Booking

def test_Classes_Buissnesslayer_Booking___init__():
    assert Classes_Buissnesslayer_Booking.__init__(Classes_Buissnesslayer_Booking(0, 0, 0, '', '\x00', '', '', False, True, '', False, Classes_Buissnesslayer_Booking=set(), Classes_Buissnesslayer_Booking11=set()), 0, 0, 0, '', '', '', '', False, True, '\x00', False, Classes_Buissnesslayer_Booking=set(), Classes_Buissnesslayer_Booking11=set()) == None


from python_code import Booking
from python_code import Classes_Buissnesslayer_BookingHandler
from python_code import Classes_Buissnesslayer_Employee
from python_code import Classes_Interactionlayer_LoginController
from python_code import Database
from python_code import GUIController
from python_code import PaymentHandler
from python_code import User
from python_code import UserHandler

def test_Classes_Buissnesslayer_Employee___init__():
    assert Classes_Buissnesslayer_Employee.__init__(Classes_Buissnesslayer_Employee(0, '', User47=Classes_Interactionlayer_LoginController(logincontroller=GUIController(), Classes_Interactionlayer_LoginController=User(), Classes_Interactionlayer_LoginController49=PaymentHandler(), logincontroller51=UserHandler()), User=Classes_Buissnesslayer_BookingHandler(Classes_Buissnesslayer_BookingHandler=Booking(), Classes_Buissnesslayer_BookingHandler16=Booking(), bookinghandler=set(), Classes_Buissnesslayer_BookingHandler20=Database(), Classes_Buissnesslayer_BookingHandler22=UserHandler())), 0, '', User47=Classes_Interactionlayer_LoginController(logincontroller=GUIController(), Classes_Interactionlayer_LoginController=User(), Classes_Interactionlayer_LoginController49=PaymentHandler(), logincontroller51=UserHandler()), User=Classes_Buissnesslayer_BookingHandler(Classes_Buissnesslayer_BookingHandler=Booking(), Classes_Buissnesslayer_BookingHandler16=Booking(), bookinghandler=set(), Classes_Buissnesslayer_BookingHandler20=Database(), Classes_Buissnesslayer_BookingHandler22=UserHandler())) == None


from python_code import Booking
from python_code import Classes_Buissnesslayer_BookingHandler
from python_code import Classes_Buissnesslayer_Guest
from python_code import Classes_Interactionlayer_LoginController
from python_code import Database
from python_code import GUIController
from python_code import PaymentHandler
from python_code import User
from python_code import UserHandler

def test_Classes_Buissnesslayer_Guest___init__():
    assert Classes_Buissnesslayer_Guest.__init__(Classes_Buissnesslayer_Guest(0, User47=Classes_Interactionlayer_LoginController(logincontroller=GUIController(), Classes_Interactionlayer_LoginController=User(), Classes_Interactionlayer_LoginController49=PaymentHandler(), logincontroller51=UserHandler()), User=Classes_Buissnesslayer_BookingHandler(Classes_Buissnesslayer_BookingHandler=Booking(), Classes_Buissnesslayer_BookingHandler16=Booking(), bookinghandler=set(), Classes_Buissnesslayer_BookingHandler20=Database(), Classes_Buissnesslayer_BookingHandler22=UserHandler())), 0, User47=Classes_Interactionlayer_LoginController(logincontroller=GUIController(), Classes_Interactionlayer_LoginController=User(), Classes_Interactionlayer_LoginController49=PaymentHandler(), logincontroller51=UserHandler()), User=Classes_Buissnesslayer_BookingHandler(Classes_Buissnesslayer_BookingHandler=Booking(), Classes_Buissnesslayer_BookingHandler16=Booking(), bookinghandler=set(), Classes_Buissnesslayer_BookingHandler20=Database(), Classes_Buissnesslayer_BookingHandler22=UserHandler())) == None


from python_code import Classes_Buissnesslayer_Room

def test_Classes_Buissnesslayer_Room___init__():
    assert Classes_Buissnesslayer_Room.__init__(Classes_Buissnesslayer_Room(0), 0) == None


from python_code import Address
from python_code import BookingHandler
from python_code import Classes_Buissnesslayer_User
from python_code import LoginController
from python_code import UserHandler

def test_Classes_Buissnesslayer_User___init__():
    assert Classes_Buissnesslayer_User.__init__(Classes_Buissnesslayer_User('', '\x00', Classes_Buissnesslayer_User=LoginController(), Classes_Buissnesslayer_User26=UserHandler(), Classes_Buissnesslayer_User29=Address(), User31=BookingHandler()), '\x00\x00', '', Classes_Buissnesslayer_User=LoginController(), Classes_Buissnesslayer_User26=UserHandler(), Classes_Buissnesslayer_User29=Address(), User31=BookingHandler()) == None

def test_Classes_Buissnesslayer_User_bookRoom():
    assert Classes_Buissnesslayer_User.bookRoom(Classes_Buissnesslayer_User('', '', Classes_Buissnesslayer_User=LoginController(), Classes_Buissnesslayer_User26=UserHandler(), Classes_Buissnesslayer_User29=Address(), User31=BookingHandler()), '') == None

def test_Classes_Buissnesslayer_User_attemptCheckOut():
    assert Classes_Buissnesslayer_User.attemptCheckOut(Classes_Buissnesslayer_User('', '', Classes_Buissnesslayer_User=LoginController(), Classes_Buissnesslayer_User26=UserHandler(), Classes_Buissnesslayer_User29=Address(), User31=BookingHandler()), '') == None

def test_Classes_Buissnesslayer_User_cancelBooking():
    assert Classes_Buissnesslayer_User.cancelBooking(Classes_Buissnesslayer_User('', '', Classes_Buissnesslayer_User=LoginController(), Classes_Buissnesslayer_User26=UserHandler(), Classes_Buissnesslayer_User29=Address(), User31=BookingHandler()), '') == None

def test_Classes_Buissnesslayer_User_changeBooking():
    assert Classes_Buissnesslayer_User.changeBooking(Classes_Buissnesslayer_User('', '', Classes_Buissnesslayer_User=LoginController(), Classes_Buissnesslayer_User26=UserHandler(), Classes_Buissnesslayer_User29=Address(), User31=BookingHandler()), '', '') == None

def test_Classes_Buissnesslayer_User_attemptCheckIn():
    assert Classes_Buissnesslayer_User.attemptCheckIn(Classes_Buissnesslayer_User('', '', Classes_Buissnesslayer_User=LoginController(), Classes_Buissnesslayer_User26=UserHandler(), Classes_Buissnesslayer_User29=Address(), User31=BookingHandler()), '') == None


from python_code import Classes_Buissnesslayer_UserHandler
from python_code import Database
from python_code import LoginController

def test_Classes_Buissnesslayer_UserHandler___init__():
    assert Classes_Buissnesslayer_UserHandler.__init__(Classes_Buissnesslayer_UserHandler('', userhandler=Database(), userhandler35=LoginController()), '', userhandler=Database(), userhandler35=LoginController()) == None

def test_Classes_Buissnesslayer_UserHandler_identifyUser():
    assert Classes_Buissnesslayer_UserHandler.identifyUser(Classes_Buissnesslayer_UserHandler('', userhandler=Database(), userhandler35=LoginController()), 0) == None

def test_Classes_Buissnesslayer_UserHandler_isEmailValid():
    assert Classes_Buissnesslayer_UserHandler.isEmailValid(Classes_Buissnesslayer_UserHandler('', userhandler=Database(), userhandler35=LoginController()), 0) == None

def test_Classes_Buissnesslayer_UserHandler_AddNewGuest():
    assert Classes_Buissnesslayer_UserHandler.AddNewGuest(Classes_Buissnesslayer_UserHandler('', userhandler=Database(), userhandler35=LoginController()), 0) == None

def test_Classes_Buissnesslayer_UserHandler_sendEmailVerification():
    assert Classes_Buissnesslayer_UserHandler.sendEmailVerification(Classes_Buissnesslayer_UserHandler('', userhandler=Database(), userhandler35=LoginController()), 0) == None

def test_Classes_Buissnesslayer_UserHandler_CreateEmployee():
    assert Classes_Buissnesslayer_UserHandler.CreateEmployee(Classes_Buissnesslayer_UserHandler('', userhandler=Database(), userhandler35=LoginController()), 0) == None


from python_code import Classes_Datalayer_Database
from python_code import UserHandler

def test_Classes_Datalayer_Database___init__():
    assert Classes_Datalayer_Database.__init__(Classes_Datalayer_Database('', Classes_Datalayer_Database=set(), database=UserHandler(), Classes_Datalayer_Database3=set(), Classes_Datalayer_Database5=set(), Classes_Datalayer_Database7=set()), '', Classes_Datalayer_Database=set(), database=UserHandler(), Classes_Datalayer_Database3=set(), Classes_Datalayer_Database5=set(), Classes_Datalayer_Database7=set()) == None


from python_code import BookingHandler
from python_code import Classes_Interactionlayer_GUIController
from python_code import GUI
from python_code import LoginController

def test_Classes_Interactionlayer_GUIController___init__():
    assert Classes_Interactionlayer_GUIController.__init__(Classes_Interactionlayer_GUIController(Classes_Interactionlayer_GUIController=GUI(), guicontroller=LoginController(), Classes_Interactionlayer_GUIController42=BookingHandler()), Classes_Interactionlayer_GUIController=GUI(), guicontroller=LoginController(), Classes_Interactionlayer_GUIController42=BookingHandler()) == None

def test_Classes_Interactionlayer_GUIController_displayRoomsByID():
    assert Classes_Interactionlayer_GUIController.displayRoomsByID(Classes_Interactionlayer_GUIController(Classes_Interactionlayer_GUIController=GUI(), guicontroller=LoginController(), Classes_Interactionlayer_GUIController42=BookingHandler()), '') == None

def test_Classes_Interactionlayer_GUIController_displayPaymentOption():
    assert Classes_Interactionlayer_GUIController.displayPaymentOption(Classes_Interactionlayer_GUIController(Classes_Interactionlayer_GUIController=GUI(), guicontroller=LoginController(), Classes_Interactionlayer_GUIController42=BookingHandler())) == None

def test_Classes_Interactionlayer_GUIController_displayExtras():
    assert Classes_Interactionlayer_GUIController.displayExtras(Classes_Interactionlayer_GUIController(Classes_Interactionlayer_GUIController=GUI(), guicontroller=LoginController(), Classes_Interactionlayer_GUIController42=BookingHandler()), '') == None

def test_Classes_Interactionlayer_GUIController_displayRoomTypes():
    assert Classes_Interactionlayer_GUIController.displayRoomTypes(Classes_Interactionlayer_GUIController(Classes_Interactionlayer_GUIController=GUI(), guicontroller=LoginController(), Classes_Interactionlayer_GUIController42=BookingHandler())) == None

def test_Classes_Interactionlayer_GUIController_displayRoomsGrid():
    assert Classes_Interactionlayer_GUIController.displayRoomsGrid(Classes_Interactionlayer_GUIController(Classes_Interactionlayer_GUIController=GUI(), guicontroller=LoginController(), Classes_Interactionlayer_GUIController42=BookingHandler()), '') == None

def test_Classes_Interactionlayer_GUIController_displayBookingCancelled():
    assert Classes_Interactionlayer_GUIController.displayBookingCancelled(Classes_Interactionlayer_GUIController(Classes_Interactionlayer_GUIController=GUI(), guicontroller=LoginController(), Classes_Interactionlayer_GUIController42=BookingHandler())) == None

def test_Classes_Interactionlayer_GUIController_showAvailableRooms():
    assert Classes_Interactionlayer_GUIController.showAvailableRooms(Classes_Interactionlayer_GUIController(Classes_Interactionlayer_GUIController=GUI(), guicontroller=LoginController(), Classes_Interactionlayer_GUIController42=BookingHandler()), '', '', '', '') == None

def test_Classes_Interactionlayer_GUIController_displayBookingsByIDintbookingID():
    assert Classes_Interactionlayer_GUIController.displayBookingsByIDintbookingID(Classes_Interactionlayer_GUIController(Classes_Interactionlayer_GUIController=GUI(), guicontroller=LoginController(), Classes_Interactionlayer_GUIController42=BookingHandler()), '') == None

def test_Classes_Interactionlayer_GUIController_displayParkings():
    assert Classes_Interactionlayer_GUIController.displayParkings(Classes_Interactionlayer_GUIController(Classes_Interactionlayer_GUIController=GUI(), guicontroller=LoginController(), Classes_Interactionlayer_GUIController42=BookingHandler()), '') == None

def test_Classes_Interactionlayer_GUIController_displayDateOptions():
    assert Classes_Interactionlayer_GUIController.displayDateOptions(Classes_Interactionlayer_GUIController(Classes_Interactionlayer_GUIController=GUI(), guicontroller=LoginController(), Classes_Interactionlayer_GUIController42=BookingHandler())) == None

def test_Classes_Interactionlayer_GUIController_displayError():
    assert Classes_Interactionlayer_GUIController.displayError(Classes_Interactionlayer_GUIController(Classes_Interactionlayer_GUIController=GUI(), guicontroller=LoginController(), Classes_Interactionlayer_GUIController42=BookingHandler())) == None


from python_code import Classes_Interactionlayer_LoginController
from python_code import GUIController
from python_code import PaymentHandler
from python_code import User
from python_code import UserHandler

def test_Classes_Interactionlayer_LoginController___init__():
    assert Classes_Interactionlayer_LoginController.__init__(Classes_Interactionlayer_LoginController(logincontroller=GUIController(), Classes_Interactionlayer_LoginController=User(), Classes_Interactionlayer_LoginController49=PaymentHandler(), logincontroller51=UserHandler()), logincontroller=GUIController(), Classes_Interactionlayer_LoginController=User(), Classes_Interactionlayer_LoginController49=PaymentHandler(), logincontroller51=UserHandler()) == None

def test_Classes_Interactionlayer_LoginController_loginEmployee():
    assert Classes_Interactionlayer_LoginController.loginEmployee(Classes_Interactionlayer_LoginController(logincontroller=GUIController(), Classes_Interactionlayer_LoginController=User(), Classes_Interactionlayer_LoginController49=PaymentHandler(), logincontroller51=UserHandler()), '') == None

def test_Classes_Interactionlayer_LoginController_loginGuest():
    assert Classes_Interactionlayer_LoginController.loginGuest(Classes_Interactionlayer_LoginController(logincontroller=GUIController(), Classes_Interactionlayer_LoginController=User(), Classes_Interactionlayer_LoginController49=PaymentHandler(), logincontroller51=UserHandler()), '') == None

def test_Classes_Interactionlayer_LoginController_loginCreateGuest():
    assert Classes_Interactionlayer_LoginController.loginCreateGuest(Classes_Interactionlayer_LoginController(logincontroller=GUIController(), Classes_Interactionlayer_LoginController=User(), Classes_Interactionlayer_LoginController49=PaymentHandler(), logincontroller51=UserHandler()), '') == None

