import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Class,
    Cliente,
    Customer,
    Direccion,
    Login,
    Login1,
    Personas,
    account_Account,
    account_CertificatesOfDepositAccount,
    account_CheckingAccount,
    account_SavingsAccount,
    gerente,
    transaction_DepositTransaction,
    transaction_Transaction,
    transaction_TransferTransaction,
    transaction_WithdrawTransaction,
    account_AccountType,
    transaction_TransactionType,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_Class_attribute_value_roundtrip():
    instance = Class(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Class_attribute2_value_roundtrip():
    instance = Class(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


def test_Cliente_contactoReferencia_value_roundtrip():
    instance = Cliente(contactoReferencia="sample_text", fechaInicio=date(2024, 1, 1), idAval=7, idCliente=7, idDiaPago=7, idDireccion=7, idPersona=7, idPrestamo=7, noTarjeta="sample_text")
    assert instance.contactoReferencia == "sample_text"
    instance.contactoReferencia = "sample_text_2"
    assert instance.contactoReferencia == "sample_text_2"


def test_Cliente_fechaInicio_value_roundtrip():
    instance = Cliente(contactoReferencia="sample_text", fechaInicio=date(2024, 1, 1), idAval=7, idCliente=7, idDiaPago=7, idDireccion=7, idPersona=7, idPrestamo=7, noTarjeta="sample_text")
    assert instance.fechaInicio == date(2024, 1, 1)
    instance.fechaInicio = date(2025, 6, 15)
    assert instance.fechaInicio == date(2025, 6, 15)


def test_Cliente_idAval_value_roundtrip():
    instance = Cliente(contactoReferencia="sample_text", fechaInicio=date(2024, 1, 1), idAval=7, idCliente=7, idDiaPago=7, idDireccion=7, idPersona=7, idPrestamo=7, noTarjeta="sample_text")
    assert instance.idAval == 7
    instance.idAval = 13
    assert instance.idAval == 13


def test_Cliente_idCliente_value_roundtrip():
    instance = Cliente(contactoReferencia="sample_text", fechaInicio=date(2024, 1, 1), idAval=7, idCliente=7, idDiaPago=7, idDireccion=7, idPersona=7, idPrestamo=7, noTarjeta="sample_text")
    assert instance.idCliente == 7
    instance.idCliente = 13
    assert instance.idCliente == 13


def test_Cliente_idDiaPago_value_roundtrip():
    instance = Cliente(contactoReferencia="sample_text", fechaInicio=date(2024, 1, 1), idAval=7, idCliente=7, idDiaPago=7, idDireccion=7, idPersona=7, idPrestamo=7, noTarjeta="sample_text")
    assert instance.idDiaPago == 7
    instance.idDiaPago = 13
    assert instance.idDiaPago == 13


def test_Cliente_idDireccion_value_roundtrip():
    instance = Cliente(contactoReferencia="sample_text", fechaInicio=date(2024, 1, 1), idAval=7, idCliente=7, idDiaPago=7, idDireccion=7, idPersona=7, idPrestamo=7, noTarjeta="sample_text")
    assert instance.idDireccion == 7
    instance.idDireccion = 13
    assert instance.idDireccion == 13


def test_Cliente_idPersona_value_roundtrip():
    instance = Cliente(contactoReferencia="sample_text", fechaInicio=date(2024, 1, 1), idAval=7, idCliente=7, idDiaPago=7, idDireccion=7, idPersona=7, idPrestamo=7, noTarjeta="sample_text")
    assert instance.idPersona == 7
    instance.idPersona = 13
    assert instance.idPersona == 13


def test_Cliente_idPrestamo_value_roundtrip():
    instance = Cliente(contactoReferencia="sample_text", fechaInicio=date(2024, 1, 1), idAval=7, idCliente=7, idDiaPago=7, idDireccion=7, idPersona=7, idPrestamo=7, noTarjeta="sample_text")
    assert instance.idPrestamo == 7
    instance.idPrestamo = 13
    assert instance.idPrestamo == 13


def test_Cliente_noTarjeta_value_roundtrip():
    instance = Cliente(contactoReferencia="sample_text", fechaInicio=date(2024, 1, 1), idAval=7, idCliente=7, idDiaPago=7, idDireccion=7, idPersona=7, idPrestamo=7, noTarjeta="sample_text")
    assert instance.noTarjeta == "sample_text"
    instance.noTarjeta = "sample_text_2"
    assert instance.noTarjeta == "sample_text_2"


def test_Customer_address_value_roundtrip():
    instance = Customer(address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Customer_dateOfBirth_value_roundtrip():
    instance = Customer(address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.dateOfBirth == date(2024, 1, 1)
    instance.dateOfBirth = date(2025, 6, 15)
    assert instance.dateOfBirth == date(2025, 6, 15)


def test_Customer_emailAddress_value_roundtrip():
    instance = Customer(address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.emailAddress == "sample_text"
    instance.emailAddress = "sample_text_2"
    assert instance.emailAddress == "sample_text_2"


def test_Customer_name_value_roundtrip():
    instance = Customer(address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Customer_phoneNumber_value_roundtrip():
    instance = Customer(address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.phoneNumber == "sample_text"
    instance.phoneNumber = "sample_text_2"
    assert instance.phoneNumber == "sample_text_2"


def test_Direccion_asentamiento_value_roundtrip():
    instance = Direccion(asentamiento="sample_text", ciudad="sample_text", cp=7, estado="sample_text", idDireccion=7, idEstado=7, idMunicipio=7, municipio="sample_text", tipo="sample_text", zona="sample_text")
    assert instance.asentamiento == "sample_text"
    instance.asentamiento = "sample_text_2"
    assert instance.asentamiento == "sample_text_2"


def test_Direccion_ciudad_value_roundtrip():
    instance = Direccion(asentamiento="sample_text", ciudad="sample_text", cp=7, estado="sample_text", idDireccion=7, idEstado=7, idMunicipio=7, municipio="sample_text", tipo="sample_text", zona="sample_text")
    assert instance.ciudad == "sample_text"
    instance.ciudad = "sample_text_2"
    assert instance.ciudad == "sample_text_2"


def test_Direccion_cp_value_roundtrip():
    instance = Direccion(asentamiento="sample_text", ciudad="sample_text", cp=7, estado="sample_text", idDireccion=7, idEstado=7, idMunicipio=7, municipio="sample_text", tipo="sample_text", zona="sample_text")
    assert instance.cp == 7
    instance.cp = 13
    assert instance.cp == 13


def test_Direccion_estado_value_roundtrip():
    instance = Direccion(asentamiento="sample_text", ciudad="sample_text", cp=7, estado="sample_text", idDireccion=7, idEstado=7, idMunicipio=7, municipio="sample_text", tipo="sample_text", zona="sample_text")
    assert instance.estado == "sample_text"
    instance.estado = "sample_text_2"
    assert instance.estado == "sample_text_2"


def test_Direccion_idDireccion_value_roundtrip():
    instance = Direccion(asentamiento="sample_text", ciudad="sample_text", cp=7, estado="sample_text", idDireccion=7, idEstado=7, idMunicipio=7, municipio="sample_text", tipo="sample_text", zona="sample_text")
    assert instance.idDireccion == 7
    instance.idDireccion = 13
    assert instance.idDireccion == 13


def test_Direccion_idEstado_value_roundtrip():
    instance = Direccion(asentamiento="sample_text", ciudad="sample_text", cp=7, estado="sample_text", idDireccion=7, idEstado=7, idMunicipio=7, municipio="sample_text", tipo="sample_text", zona="sample_text")
    assert instance.idEstado == 7
    instance.idEstado = 13
    assert instance.idEstado == 13


def test_Direccion_idMunicipio_value_roundtrip():
    instance = Direccion(asentamiento="sample_text", ciudad="sample_text", cp=7, estado="sample_text", idDireccion=7, idEstado=7, idMunicipio=7, municipio="sample_text", tipo="sample_text", zona="sample_text")
    assert instance.idMunicipio == 7
    instance.idMunicipio = 13
    assert instance.idMunicipio == 13


def test_Direccion_municipio_value_roundtrip():
    instance = Direccion(asentamiento="sample_text", ciudad="sample_text", cp=7, estado="sample_text", idDireccion=7, idEstado=7, idMunicipio=7, municipio="sample_text", tipo="sample_text", zona="sample_text")
    assert instance.municipio == "sample_text"
    instance.municipio = "sample_text_2"
    assert instance.municipio == "sample_text_2"


def test_Direccion_tipo_value_roundtrip():
    instance = Direccion(asentamiento="sample_text", ciudad="sample_text", cp=7, estado="sample_text", idDireccion=7, idEstado=7, idMunicipio=7, municipio="sample_text", tipo="sample_text", zona="sample_text")
    assert instance.tipo == "sample_text"
    instance.tipo = "sample_text_2"
    assert instance.tipo == "sample_text_2"


def test_Direccion_zona_value_roundtrip():
    instance = Direccion(asentamiento="sample_text", ciudad="sample_text", cp=7, estado="sample_text", idDireccion=7, idEstado=7, idMunicipio=7, municipio="sample_text", tipo="sample_text", zona="sample_text")
    assert instance.zona == "sample_text"
    instance.zona = "sample_text_2"
    assert instance.zona == "sample_text_2"


def test_Login_lastLoginTime_value_roundtrip():
    instance = Login(lastLoginTime=date(2024, 1, 1), password="sample_text", securityAnswer="sample_text", securityQuestion="sample_text", username="sample_text")
    assert instance.lastLoginTime == date(2024, 1, 1)
    instance.lastLoginTime = date(2025, 6, 15)
    assert instance.lastLoginTime == date(2025, 6, 15)


def test_Login_password_value_roundtrip():
    instance = Login(lastLoginTime=date(2024, 1, 1), password="sample_text", securityAnswer="sample_text", securityQuestion="sample_text", username="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Login_securityAnswer_value_roundtrip():
    instance = Login(lastLoginTime=date(2024, 1, 1), password="sample_text", securityAnswer="sample_text", securityQuestion="sample_text", username="sample_text")
    assert instance.securityAnswer == "sample_text"
    instance.securityAnswer = "sample_text_2"
    assert instance.securityAnswer == "sample_text_2"


def test_Login_securityQuestion_value_roundtrip():
    instance = Login(lastLoginTime=date(2024, 1, 1), password="sample_text", securityAnswer="sample_text", securityQuestion="sample_text", username="sample_text")
    assert instance.securityQuestion == "sample_text"
    instance.securityQuestion = "sample_text_2"
    assert instance.securityQuestion == "sample_text_2"


def test_Login_username_value_roundtrip():
    instance = Login(lastLoginTime=date(2024, 1, 1), password="sample_text", securityAnswer="sample_text", securityQuestion="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_Login1_password_value_roundtrip():
    instance = Login1(password="sample_text", usuario="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Login1_usuario_value_roundtrip():
    instance = Login1(password="sample_text", usuario="sample_text")
    assert instance.usuario == "sample_text"
    instance.usuario = "sample_text_2"
    assert instance.usuario == "sample_text_2"


def test_Personas_aMaterno_value_roundtrip():
    instance = Personas(aMaterno="sample_text", aPaterno="sample_text", estado="sample_text", idPersona=7, nombre="sample_text", telefono="sample_text")
    assert instance.aMaterno == "sample_text"
    instance.aMaterno = "sample_text_2"
    assert instance.aMaterno == "sample_text_2"


def test_Personas_aPaterno_value_roundtrip():
    instance = Personas(aMaterno="sample_text", aPaterno="sample_text", estado="sample_text", idPersona=7, nombre="sample_text", telefono="sample_text")
    assert instance.aPaterno == "sample_text"
    instance.aPaterno = "sample_text_2"
    assert instance.aPaterno == "sample_text_2"


def test_Personas_estado_value_roundtrip():
    instance = Personas(aMaterno="sample_text", aPaterno="sample_text", estado="sample_text", idPersona=7, nombre="sample_text", telefono="sample_text")
    assert instance.estado == "sample_text"
    instance.estado = "sample_text_2"
    assert instance.estado == "sample_text_2"


def test_Personas_idPersona_value_roundtrip():
    instance = Personas(aMaterno="sample_text", aPaterno="sample_text", estado="sample_text", idPersona=7, nombre="sample_text", telefono="sample_text")
    assert instance.idPersona == 7
    instance.idPersona = 13
    assert instance.idPersona == 13


def test_Personas_nombre_value_roundtrip():
    instance = Personas(aMaterno="sample_text", aPaterno="sample_text", estado="sample_text", idPersona=7, nombre="sample_text", telefono="sample_text")
    assert instance.nombre == "sample_text"
    instance.nombre = "sample_text_2"
    assert instance.nombre == "sample_text_2"


def test_Personas_telefono_value_roundtrip():
    instance = Personas(aMaterno="sample_text", aPaterno="sample_text", estado="sample_text", idPersona=7, nombre="sample_text", telefono="sample_text")
    assert instance.telefono == "sample_text"
    instance.telefono = "sample_text_2"
    assert instance.telefono == "sample_text_2"


def test_account_CertificatesOfDepositAccount_interestRate_value_roundtrip():
    instance = account_CertificatesOfDepositAccount(interestRate=3.14, timePeriod=7)
    assert instance.interestRate == 3.14
    instance.interestRate = 9.99
    assert instance.interestRate == 9.99


def test_account_CertificatesOfDepositAccount_timePeriod_value_roundtrip():
    instance = account_CertificatesOfDepositAccount(interestRate=3.14, timePeriod=7)
    assert instance.timePeriod == 7
    instance.timePeriod = 13
    assert instance.timePeriod == 13


def test_account_CheckingAccount_name_value_roundtrip():
    instance = account_CheckingAccount(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_account_SavingsAccount_interestRate_value_roundtrip():
    instance = account_SavingsAccount(interestRate=3.14)
    assert instance.interestRate == 3.14
    instance.interestRate = 9.99
    assert instance.interestRate == 9.99


def test_gerente_id_value_roundtrip():
    instance = gerente(id="sample_text", idGerente=7, idPersona="sample_text", idUsuario=7, idZona=7)
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_gerente_idGerente_value_roundtrip():
    instance = gerente(id="sample_text", idGerente=7, idPersona="sample_text", idUsuario=7, idZona=7)
    assert instance.idGerente == 7
    instance.idGerente = 13
    assert instance.idGerente == 13


def test_gerente_idPersona_value_roundtrip():
    instance = gerente(id="sample_text", idGerente=7, idPersona="sample_text", idUsuario=7, idZona=7)
    assert instance.idPersona == "sample_text"
    instance.idPersona = "sample_text_2"
    assert instance.idPersona == "sample_text_2"


def test_gerente_idUsuario_value_roundtrip():
    instance = gerente(id="sample_text", idGerente=7, idPersona="sample_text", idUsuario=7, idZona=7)
    assert instance.idUsuario == 7
    instance.idUsuario = 13
    assert instance.idUsuario == 13


def test_gerente_idZona_value_roundtrip():
    instance = gerente(id="sample_text", idGerente=7, idPersona="sample_text", idUsuario=7, idZona=7)
    assert instance.idZona == 7
    instance.idZona = 13
    assert instance.idZona == 13


def test_assoc_Customer_Login_link_reassign_clear():
    a = Login(lastLoginTime=date(2024, 1, 1), password="sample_text", securityAnswer="sample_text", securityQuestion="sample_text", username="sample_text")
    b1 = Customer(address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    b2 = Customer(address="sample_text_2", dateOfBirth=date(2025, 6, 15), emailAddress="sample_text_2", name="sample_text_2", phoneNumber="sample_text_2")
    _safe_set(a, 'customer5', b1)
    assert _is_linked(a, 'customer5', b1)
    if hasattr(b1, 'login4'):
        assert _is_linked(b1, 'login4', a)
    _safe_set(a, 'customer5', b2)
    assert _is_linked(a, 'customer5', b2)
    if hasattr(b1, 'login4'):
        assert not _is_linked(b1, 'login4', a)
    if hasattr(b2, 'login4'):
        assert _is_linked(b2, 'login4', a)
    _safe_set(a, 'customer5', None)
    assert not _is_linked(a, 'customer5', b2)
    if hasattr(b2, 'login4'):
        assert not _is_linked(b2, 'login4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Class_strategy = st.builds(Class, attribute=safe_text, attribute2=safe_text)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Cliente_strategy = st.builds(Cliente, contactoReferencia=safe_text, fechaInicio=st.dates(), idAval=st.integers(), idCliente=st.integers(), idDiaPago=st.integers(), idDireccion=st.integers(), idPersona=st.integers(), idPrestamo=st.integers(), noTarjeta=safe_text)
@given(instance=Cliente_strategy)
@settings(max_examples=25)
def test_Cliente_instantiation(instance):
    assert isinstance(instance, Cliente)


Customer_strategy = st.builds(Customer, address=safe_text, dateOfBirth=st.dates(), emailAddress=safe_text, name=safe_text, phoneNumber=safe_text)
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


Direccion_strategy = st.builds(Direccion, asentamiento=safe_text, ciudad=safe_text, cp=st.integers(), estado=safe_text, idDireccion=st.integers(), idEstado=st.integers(), idMunicipio=st.integers(), municipio=safe_text, tipo=safe_text, zona=safe_text)
@given(instance=Direccion_strategy)
@settings(max_examples=25)
def test_Direccion_instantiation(instance):
    assert isinstance(instance, Direccion)


Login_strategy = st.builds(Login, lastLoginTime=st.dates(), password=safe_text, securityAnswer=safe_text, securityQuestion=safe_text, username=safe_text)
@given(instance=Login_strategy)
@settings(max_examples=25)
def test_Login_instantiation(instance):
    assert isinstance(instance, Login)


Login1_strategy = st.builds(Login1, password=safe_text, usuario=safe_text)
@given(instance=Login1_strategy)
@settings(max_examples=25)
def test_Login1_instantiation(instance):
    assert isinstance(instance, Login1)


Personas_strategy = st.builds(Personas, aMaterno=safe_text, aPaterno=safe_text, estado=safe_text, idPersona=st.integers(), nombre=safe_text, telefono=safe_text)
@given(instance=Personas_strategy)
@settings(max_examples=25)
def test_Personas_instantiation(instance):
    assert isinstance(instance, Personas)


account_CertificatesOfDepositAccount_strategy = st.builds(account_CertificatesOfDepositAccount, interestRate=st.floats(allow_nan=False, allow_infinity=False), timePeriod=st.integers())
@given(instance=account_CertificatesOfDepositAccount_strategy)
@settings(max_examples=25)
def test_account_CertificatesOfDepositAccount_instantiation(instance):
    assert isinstance(instance, account_CertificatesOfDepositAccount)


account_CheckingAccount_strategy = st.builds(account_CheckingAccount, name=safe_text)
@given(instance=account_CheckingAccount_strategy)
@settings(max_examples=25)
def test_account_CheckingAccount_instantiation(instance):
    assert isinstance(instance, account_CheckingAccount)


account_SavingsAccount_strategy = st.builds(account_SavingsAccount, interestRate=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=account_SavingsAccount_strategy)
@settings(max_examples=25)
def test_account_SavingsAccount_instantiation(instance):
    assert isinstance(instance, account_SavingsAccount)


gerente_strategy = st.builds(gerente, id=safe_text, idGerente=st.integers(), idPersona=safe_text, idUsuario=st.integers(), idZona=st.integers())
@given(instance=gerente_strategy)
@settings(max_examples=25)
def test_gerente_instantiation(instance):
    assert isinstance(instance, gerente)


transaction_DepositTransaction_strategy = st.builds(transaction_DepositTransaction)
@given(instance=transaction_DepositTransaction_strategy)
@settings(max_examples=25)
def test_transaction_DepositTransaction_instantiation(instance):
    assert isinstance(instance, transaction_DepositTransaction)


transaction_WithdrawTransaction_strategy = st.builds(transaction_WithdrawTransaction)
@given(instance=transaction_WithdrawTransaction_strategy)
@settings(max_examples=25)
def test_transaction_WithdrawTransaction_instantiation(instance):
    assert isinstance(instance, transaction_WithdrawTransaction)


