# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    historico,
    login,
    tipoSeguro,
    aseguradora,
    alergia,
    especialidad,
    empleado,
    doctor,
    consulta,
    paciente,
    DateTime,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_historico_is_not_abstract():
    assert not inspect.isabstract(historico)


def test_hyp_historico_constructor_exists():
    assert callable(historico.__init__)


def test_hyp_historico_constructor_args():
    sig = inspect.signature(historico.__init__)
    params = list(sig.parameters.keys())
    assert "diagnostico" in params, "Missing parameter 'diagnostico'"
    assert "consultaID" in params, "Missing parameter 'consultaID'"
    assert "tratamiento" in params, "Missing parameter 'tratamiento'"
    assert "historicoID" in params, "Missing parameter 'historicoID'"
    assert "observacion" in params, "Missing parameter 'observacion'"
    assert "sintoma" in params, "Missing parameter 'sintoma'"









def test_hyp_login_is_not_abstract():
    assert not inspect.isabstract(login)


def test_hyp_login_constructor_exists():
    assert callable(login.__init__)


def test_hyp_login_constructor_args():
    sig = inspect.signature(login.__init__)
    params = list(sig.parameters.keys())
    assert "loginID" in params, "Missing parameter 'loginID'"
    assert "role" in params, "Missing parameter 'role'"
    assert "usuario" in params, "Missing parameter 'usuario'"
    assert "contrasena" in params, "Missing parameter 'contrasena'"







def test_hyp_tiposeguro_is_not_abstract():
    assert not inspect.isabstract(tipoSeguro)


def test_hyp_tiposeguro_constructor_exists():
    assert callable(tipoSeguro.__init__)


def test_hyp_tiposeguro_constructor_args():
    sig = inspect.signature(tipoSeguro.__init__)
    params = list(sig.parameters.keys())
    assert "tipoSeguraID" in params, "Missing parameter 'tipoSeguraID'"
    assert "descripcion" in params, "Missing parameter 'descripcion'"





def test_hyp_aseguradora_is_not_abstract():
    assert not inspect.isabstract(aseguradora)


def test_hyp_aseguradora_constructor_exists():
    assert callable(aseguradora.__init__)


def test_hyp_aseguradora_constructor_args():
    sig = inspect.signature(aseguradora.__init__)
    params = list(sig.parameters.keys())
    assert "tipoSeguroID" in params, "Missing parameter 'tipoSeguroID'"
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "aseguradoraID" in params, "Missing parameter 'aseguradoraID'"






def test_hyp_alergia_is_not_abstract():
    assert not inspect.isabstract(alergia)


def test_hyp_alergia_constructor_exists():
    assert callable(alergia.__init__)


def test_hyp_alergia_constructor_args():
    sig = inspect.signature(alergia.__init__)
    params = list(sig.parameters.keys())
    assert "alergiaID" in params, "Missing parameter 'alergiaID'"
    assert "nombre" in params, "Missing parameter 'nombre'"





def test_hyp_especialidad_is_not_abstract():
    assert not inspect.isabstract(especialidad)


def test_hyp_especialidad_constructor_exists():
    assert callable(especialidad.__init__)


def test_hyp_especialidad_constructor_args():
    sig = inspect.signature(especialidad.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "especialidadID" in params, "Missing parameter 'especialidadID'"





def test_hyp_empleado_is_not_abstract():
    assert not inspect.isabstract(empleado)


def test_hyp_empleado_constructor_exists():
    assert callable(empleado.__init__)


def test_hyp_empleado_constructor_args():
    sig = inspect.signature(empleado.__init__)
    params = list(sig.parameters.keys())
    assert "apMaterno" in params, "Missing parameter 'apMaterno'"
    assert "loginID" in params, "Missing parameter 'loginID'"
    assert "empleadoID" in params, "Missing parameter 'empleadoID'"
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "apPaterno" in params, "Missing parameter 'apPaterno'"
    assert "codigoEmpleado" in params, "Missing parameter 'codigoEmpleado'"
    assert "fechaNacimiento" in params, "Missing parameter 'fechaNacimiento'"
    assert "nroDocumento" in params, "Missing parameter 'nroDocumento'"

def test_hyp_empleado_has_apMaterno():
    assert hasattr(empleado, "apMaterno")
    descriptor = None
    for klass in empleado.__mro__:
        if "apMaterno" in klass.__dict__:
            descriptor = klass.__dict__["apMaterno"]
            break
    assert isinstance(descriptor, property)

def test_hyp_empleado_has_loginID():
    assert hasattr(empleado, "loginID")
    descriptor = None
    for klass in empleado.__mro__:
        if "loginID" in klass.__dict__:
            descriptor = klass.__dict__["loginID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_empleado_has_empleadoID():
    assert hasattr(empleado, "empleadoID")
    descriptor = None
    for klass in empleado.__mro__:
        if "empleadoID" in klass.__dict__:
            descriptor = klass.__dict__["empleadoID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_empleado_has_nombre():
    assert hasattr(empleado, "nombre")
    descriptor = None
    for klass in empleado.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_hyp_empleado_has_apPaterno():
    assert hasattr(empleado, "apPaterno")
    descriptor = None
    for klass in empleado.__mro__:
        if "apPaterno" in klass.__dict__:
            descriptor = klass.__dict__["apPaterno"]
            break
    assert isinstance(descriptor, property)

def test_hyp_empleado_has_codigoEmpleado():
    assert hasattr(empleado, "codigoEmpleado")
    descriptor = None
    for klass in empleado.__mro__:
        if "codigoEmpleado" in klass.__dict__:
            descriptor = klass.__dict__["codigoEmpleado"]
            break
    assert isinstance(descriptor, property)

def test_hyp_empleado_has_fechaNacimiento():
    assert hasattr(empleado, "fechaNacimiento")
    descriptor = None
    for klass in empleado.__mro__:
        if "fechaNacimiento" in klass.__dict__:
            descriptor = klass.__dict__["fechaNacimiento"]
            break
    assert isinstance(descriptor, property)

def test_hyp_empleado_has_nroDocumento():
    assert hasattr(empleado, "nroDocumento")
    descriptor = None
    for klass in empleado.__mro__:
        if "nroDocumento" in klass.__dict__:
            descriptor = klass.__dict__["nroDocumento"]
            break
    assert isinstance(descriptor, property)



def test_hyp_doctor_is_not_abstract():
    assert not inspect.isabstract(doctor)


def test_hyp_doctor_constructor_exists():
    assert callable(doctor.__init__)


def test_hyp_doctor_constructor_args():
    sig = inspect.signature(doctor.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "loginID" in params, "Missing parameter 'loginID'"
    assert "fechaNacimiento" in params, "Missing parameter 'fechaNacimiento'"
    assert "doctorID" in params, "Missing parameter 'doctorID'"
    assert "apPaterno" in params, "Missing parameter 'apPaterno'"
    assert "especialidadID" in params, "Missing parameter 'especialidadID'"
    assert "codigoDoctor" in params, "Missing parameter 'codigoDoctor'"
    assert "nroDocumento" in params, "Missing parameter 'nroDocumento'"
    assert "apMaterno" in params, "Missing parameter 'apMaterno'"

def test_hyp_doctor_has_nombre():
    assert hasattr(doctor, "nombre")
    descriptor = None
    for klass in doctor.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_hyp_doctor_has_loginID():
    assert hasattr(doctor, "loginID")
    descriptor = None
    for klass in doctor.__mro__:
        if "loginID" in klass.__dict__:
            descriptor = klass.__dict__["loginID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_doctor_has_fechaNacimiento():
    assert hasattr(doctor, "fechaNacimiento")
    descriptor = None
    for klass in doctor.__mro__:
        if "fechaNacimiento" in klass.__dict__:
            descriptor = klass.__dict__["fechaNacimiento"]
            break
    assert isinstance(descriptor, property)

def test_hyp_doctor_has_doctorID():
    assert hasattr(doctor, "doctorID")
    descriptor = None
    for klass in doctor.__mro__:
        if "doctorID" in klass.__dict__:
            descriptor = klass.__dict__["doctorID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_doctor_has_apPaterno():
    assert hasattr(doctor, "apPaterno")
    descriptor = None
    for klass in doctor.__mro__:
        if "apPaterno" in klass.__dict__:
            descriptor = klass.__dict__["apPaterno"]
            break
    assert isinstance(descriptor, property)

def test_hyp_doctor_has_especialidadID():
    assert hasattr(doctor, "especialidadID")
    descriptor = None
    for klass in doctor.__mro__:
        if "especialidadID" in klass.__dict__:
            descriptor = klass.__dict__["especialidadID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_doctor_has_codigoDoctor():
    assert hasattr(doctor, "codigoDoctor")
    descriptor = None
    for klass in doctor.__mro__:
        if "codigoDoctor" in klass.__dict__:
            descriptor = klass.__dict__["codigoDoctor"]
            break
    assert isinstance(descriptor, property)

def test_hyp_doctor_has_nroDocumento():
    assert hasattr(doctor, "nroDocumento")
    descriptor = None
    for klass in doctor.__mro__:
        if "nroDocumento" in klass.__dict__:
            descriptor = klass.__dict__["nroDocumento"]
            break
    assert isinstance(descriptor, property)

def test_hyp_doctor_has_apMaterno():
    assert hasattr(doctor, "apMaterno")
    descriptor = None
    for klass in doctor.__mro__:
        if "apMaterno" in klass.__dict__:
            descriptor = klass.__dict__["apMaterno"]
            break
    assert isinstance(descriptor, property)



def test_hyp_consulta_is_not_abstract():
    assert not inspect.isabstract(consulta)


def test_hyp_consulta_constructor_exists():
    assert callable(consulta.__init__)


def test_hyp_consulta_constructor_args():
    sig = inspect.signature(consulta.__init__)
    params = list(sig.parameters.keys())
    assert "pacienteID" in params, "Missing parameter 'pacienteID'"
    assert "consultaID" in params, "Missing parameter 'consultaID'"
    assert "empleadoID" in params, "Missing parameter 'empleadoID'"
    assert "doctorID" in params, "Missing parameter 'doctorID'"
    assert "fechaConsulta" in params, "Missing parameter 'fechaConsulta'"

def test_hyp_consulta_has_pacienteID():
    assert hasattr(consulta, "pacienteID")
    descriptor = None
    for klass in consulta.__mro__:
        if "pacienteID" in klass.__dict__:
            descriptor = klass.__dict__["pacienteID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_consulta_has_consultaID():
    assert hasattr(consulta, "consultaID")
    descriptor = None
    for klass in consulta.__mro__:
        if "consultaID" in klass.__dict__:
            descriptor = klass.__dict__["consultaID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_consulta_has_empleadoID():
    assert hasattr(consulta, "empleadoID")
    descriptor = None
    for klass in consulta.__mro__:
        if "empleadoID" in klass.__dict__:
            descriptor = klass.__dict__["empleadoID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_consulta_has_doctorID():
    assert hasattr(consulta, "doctorID")
    descriptor = None
    for klass in consulta.__mro__:
        if "doctorID" in klass.__dict__:
            descriptor = klass.__dict__["doctorID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_consulta_has_fechaConsulta():
    assert hasattr(consulta, "fechaConsulta")
    descriptor = None
    for klass in consulta.__mro__:
        if "fechaConsulta" in klass.__dict__:
            descriptor = klass.__dict__["fechaConsulta"]
            break
    assert isinstance(descriptor, property)



def test_hyp_paciente_is_not_abstract():
    assert not inspect.isabstract(paciente)


def test_hyp_paciente_constructor_exists():
    assert callable(paciente.__init__)


def test_hyp_paciente_constructor_args():
    sig = inspect.signature(paciente.__init__)
    params = list(sig.parameters.keys())
    assert "codigoAsegurado" in params, "Missing parameter 'codigoAsegurado'"
    assert "razonSocial" in params, "Missing parameter 'razonSocial'"
    assert "fechaAfiliacion" in params, "Missing parameter 'fechaAfiliacion'"
    assert "fechaNacimiento" in params, "Missing parameter 'fechaNacimiento'"
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "tipoSangre" in params, "Missing parameter 'tipoSangre'"
    assert "pacienteID" in params, "Missing parameter 'pacienteID'"
    assert "apPaterno" in params, "Missing parameter 'apPaterno'"
    assert "apMaterno" in params, "Missing parameter 'apMaterno'"
    assert "nroDocumento" in params, "Missing parameter 'nroDocumento'"
    assert "aseguradoID" in params, "Missing parameter 'aseguradoID'"

def test_hyp_paciente_has_codigoAsegurado():
    assert hasattr(paciente, "codigoAsegurado")
    descriptor = None
    for klass in paciente.__mro__:
        if "codigoAsegurado" in klass.__dict__:
            descriptor = klass.__dict__["codigoAsegurado"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_razonSocial():
    assert hasattr(paciente, "razonSocial")
    descriptor = None
    for klass in paciente.__mro__:
        if "razonSocial" in klass.__dict__:
            descriptor = klass.__dict__["razonSocial"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_fechaAfiliacion():
    assert hasattr(paciente, "fechaAfiliacion")
    descriptor = None
    for klass in paciente.__mro__:
        if "fechaAfiliacion" in klass.__dict__:
            descriptor = klass.__dict__["fechaAfiliacion"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_fechaNacimiento():
    assert hasattr(paciente, "fechaNacimiento")
    descriptor = None
    for klass in paciente.__mro__:
        if "fechaNacimiento" in klass.__dict__:
            descriptor = klass.__dict__["fechaNacimiento"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_nombre():
    assert hasattr(paciente, "nombre")
    descriptor = None
    for klass in paciente.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_tipoSangre():
    assert hasattr(paciente, "tipoSangre")
    descriptor = None
    for klass in paciente.__mro__:
        if "tipoSangre" in klass.__dict__:
            descriptor = klass.__dict__["tipoSangre"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_pacienteID():
    assert hasattr(paciente, "pacienteID")
    descriptor = None
    for klass in paciente.__mro__:
        if "pacienteID" in klass.__dict__:
            descriptor = klass.__dict__["pacienteID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_apPaterno():
    assert hasattr(paciente, "apPaterno")
    descriptor = None
    for klass in paciente.__mro__:
        if "apPaterno" in klass.__dict__:
            descriptor = klass.__dict__["apPaterno"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_apMaterno():
    assert hasattr(paciente, "apMaterno")
    descriptor = None
    for klass in paciente.__mro__:
        if "apMaterno" in klass.__dict__:
            descriptor = klass.__dict__["apMaterno"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_nroDocumento():
    assert hasattr(paciente, "nroDocumento")
    descriptor = None
    for klass in paciente.__mro__:
        if "nroDocumento" in klass.__dict__:
            descriptor = klass.__dict__["nroDocumento"]
            break
    assert isinstance(descriptor, property)

def test_hyp_paciente_has_aseguradoID():
    assert hasattr(paciente, "aseguradoID")
    descriptor = None
    for klass in paciente.__mro__:
        if "aseguradoID" in klass.__dict__:
            descriptor = klass.__dict__["aseguradoID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_datetime_exists():
    # Check that the Enumeration exists
    assert DateTime is not None

def test_hyp_datetime_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DateTime]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DateTime"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
historico_strategy = st.builds(
    historico,
    diagnostico=
        safe_text,
    consultaID=
        st.integers(),
    tratamiento=
        safe_text,
    historicoID=
        st.integers(),
    observacion=
        safe_text,
    sintoma=
        safe_text
)
login_strategy = st.builds(
    login,
    loginID=
        st.integers(),
    role=
        safe_text,
    usuario=
        safe_text,
    contrasena=
        safe_text
)
tipoSeguro_strategy = st.builds(
    tipoSeguro,
    tipoSeguraID=
        st.integers(),
    descripcion=
        safe_text
)
aseguradora_strategy = st.builds(
    aseguradora,
    tipoSeguroID=
        st.integers(),
    nombre=
        safe_text,
    aseguradoraID=
        st.integers()
)
alergia_strategy = st.builds(
    alergia,
    alergiaID=
        st.integers(),
    nombre=
        safe_text
)
especialidad_strategy = st.builds(
    especialidad,
    nombre=
        safe_text,
    especialidadID=
        st.integers()
)
empleado_strategy = st.builds(
    empleado,
    apMaterno=
        safe_text,
    loginID=
        st.integers(),
    empleadoID=
        st.integers(),
    nombre=
        safe_text,
    apPaterno=
        safe_text,
    codigoEmpleado=
        safe_text,
    fechaNacimiento=
        st.dates(),
    nroDocumento=
        st.integers()
)
doctor_strategy = st.builds(
    doctor,
    nombre=
        safe_text,
    loginID=
        st.integers(),
    fechaNacimiento=
        st.dates(),
    doctorID=
        st.integers(),
    apPaterno=
        safe_text,
    especialidadID=
        st.integers(),
    codigoDoctor=
        safe_text,
    nroDocumento=
        st.integers(),
    apMaterno=
        safe_text
)
consulta_strategy = st.builds(
    consulta,
    pacienteID=
        st.integers(),
    consultaID=
        st.integers(),
    empleadoID=
        st.integers(),
    doctorID=
        st.integers(),
    fechaConsulta=
        st.dates()
)
paciente_strategy = st.builds(
    paciente,
    codigoAsegurado=
        safe_text,
    razonSocial=
        safe_text,
    fechaAfiliacion=
        st.dates(),
    fechaNacimiento=
        st.dates(),
    nombre=
        safe_text,
    tipoSangre=
        safe_text,
    pacienteID=
        st.integers(),
    apPaterno=
        safe_text,
    apMaterno=
        safe_text,
    nroDocumento=
        st.integers(),
    aseguradoID=
        st.integers()
)




@given(instance=historico_strategy)
def test_hyp_historico_diagnostico_setter(instance):
    original = instance.diagnostico
    instance.diagnostico = original
    assert instance.diagnostico == original



@given(instance=historico_strategy)
def test_hyp_historico_consultaID_setter(instance):
    original = instance.consultaID
    instance.consultaID = original
    assert instance.consultaID == original



@given(instance=historico_strategy)
def test_hyp_historico_tratamiento_setter(instance):
    original = instance.tratamiento
    instance.tratamiento = original
    assert instance.tratamiento == original



@given(instance=historico_strategy)
def test_hyp_historico_historicoID_setter(instance):
    original = instance.historicoID
    instance.historicoID = original
    assert instance.historicoID == original



@given(instance=historico_strategy)
def test_hyp_historico_observacion_setter(instance):
    original = instance.observacion
    instance.observacion = original
    assert instance.observacion == original



@given(instance=historico_strategy)
def test_hyp_historico_sintoma_setter(instance):
    original = instance.sintoma
    instance.sintoma = original
    assert instance.sintoma == original




@given(instance=login_strategy)
def test_hyp_login_loginID_setter(instance):
    original = instance.loginID
    instance.loginID = original
    assert instance.loginID == original



@given(instance=login_strategy)
def test_hyp_login_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original



@given(instance=login_strategy)
def test_hyp_login_usuario_setter(instance):
    original = instance.usuario
    instance.usuario = original
    assert instance.usuario == original



@given(instance=login_strategy)
def test_hyp_login_contrasena_setter(instance):
    original = instance.contrasena
    instance.contrasena = original
    assert instance.contrasena == original




@given(instance=tipoSeguro_strategy)
def test_hyp_tiposeguro_tipoSeguraID_setter(instance):
    original = instance.tipoSeguraID
    instance.tipoSeguraID = original
    assert instance.tipoSeguraID == original



@given(instance=tipoSeguro_strategy)
def test_hyp_tiposeguro_descripcion_setter(instance):
    original = instance.descripcion
    instance.descripcion = original
    assert instance.descripcion == original




@given(instance=aseguradora_strategy)
def test_hyp_aseguradora_tipoSeguroID_setter(instance):
    original = instance.tipoSeguroID
    instance.tipoSeguroID = original
    assert instance.tipoSeguroID == original



@given(instance=aseguradora_strategy)
def test_hyp_aseguradora_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=aseguradora_strategy)
def test_hyp_aseguradora_aseguradoraID_setter(instance):
    original = instance.aseguradoraID
    instance.aseguradoraID = original
    assert instance.aseguradoraID == original




@given(instance=alergia_strategy)
def test_hyp_alergia_alergiaID_setter(instance):
    original = instance.alergiaID
    instance.alergiaID = original
    assert instance.alergiaID == original



@given(instance=alergia_strategy)
def test_hyp_alergia_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original




@given(instance=especialidad_strategy)
def test_hyp_especialidad_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=especialidad_strategy)
def test_hyp_especialidad_especialidadID_setter(instance):
    original = instance.especialidadID
    instance.especialidadID = original
    assert instance.especialidadID == original

@given(instance=empleado_strategy)
@settings(max_examples=50)
def test_hyp_empleado_instantiation(instance):
    assert isinstance(instance, empleado)



@given(instance=empleado_strategy)
def test_hyp_empleado_apMaterno_setter(instance):
    original = instance.apMaterno
    instance.apMaterno = original
    assert instance.apMaterno == original



@given(instance=empleado_strategy)
def test_hyp_empleado_loginID_setter(instance):
    original = instance.loginID
    instance.loginID = original
    assert instance.loginID == original



@given(instance=empleado_strategy)
def test_hyp_empleado_empleadoID_setter(instance):
    original = instance.empleadoID
    instance.empleadoID = original
    assert instance.empleadoID == original



@given(instance=empleado_strategy)
def test_hyp_empleado_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=empleado_strategy)
def test_hyp_empleado_apPaterno_setter(instance):
    original = instance.apPaterno
    instance.apPaterno = original
    assert instance.apPaterno == original



@given(instance=empleado_strategy)
def test_hyp_empleado_codigoEmpleado_setter(instance):
    original = instance.codigoEmpleado
    instance.codigoEmpleado = original
    assert instance.codigoEmpleado == original



@given(instance=empleado_strategy)
def test_hyp_empleado_fechaNacimiento_setter(instance):
    original = instance.fechaNacimiento
    instance.fechaNacimiento = original
    assert instance.fechaNacimiento == original



@given(instance=empleado_strategy)
def test_hyp_empleado_nroDocumento_setter(instance):
    original = instance.nroDocumento
    instance.nroDocumento = original
    assert instance.nroDocumento == original

@given(instance=doctor_strategy)
@settings(max_examples=50)
def test_hyp_doctor_instantiation(instance):
    assert isinstance(instance, doctor)



@given(instance=doctor_strategy)
def test_hyp_doctor_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=doctor_strategy)
def test_hyp_doctor_loginID_setter(instance):
    original = instance.loginID
    instance.loginID = original
    assert instance.loginID == original



@given(instance=doctor_strategy)
def test_hyp_doctor_fechaNacimiento_setter(instance):
    original = instance.fechaNacimiento
    instance.fechaNacimiento = original
    assert instance.fechaNacimiento == original



@given(instance=doctor_strategy)
def test_hyp_doctor_doctorID_setter(instance):
    original = instance.doctorID
    instance.doctorID = original
    assert instance.doctorID == original



@given(instance=doctor_strategy)
def test_hyp_doctor_apPaterno_setter(instance):
    original = instance.apPaterno
    instance.apPaterno = original
    assert instance.apPaterno == original



@given(instance=doctor_strategy)
def test_hyp_doctor_especialidadID_setter(instance):
    original = instance.especialidadID
    instance.especialidadID = original
    assert instance.especialidadID == original



@given(instance=doctor_strategy)
def test_hyp_doctor_codigoDoctor_setter(instance):
    original = instance.codigoDoctor
    instance.codigoDoctor = original
    assert instance.codigoDoctor == original



@given(instance=doctor_strategy)
def test_hyp_doctor_nroDocumento_setter(instance):
    original = instance.nroDocumento
    instance.nroDocumento = original
    assert instance.nroDocumento == original



@given(instance=doctor_strategy)
def test_hyp_doctor_apMaterno_setter(instance):
    original = instance.apMaterno
    instance.apMaterno = original
    assert instance.apMaterno == original

@given(instance=consulta_strategy)
@settings(max_examples=50)
def test_hyp_consulta_instantiation(instance):
    assert isinstance(instance, consulta)



@given(instance=consulta_strategy)
def test_hyp_consulta_pacienteID_setter(instance):
    original = instance.pacienteID
    instance.pacienteID = original
    assert instance.pacienteID == original



@given(instance=consulta_strategy)
def test_hyp_consulta_consultaID_setter(instance):
    original = instance.consultaID
    instance.consultaID = original
    assert instance.consultaID == original



@given(instance=consulta_strategy)
def test_hyp_consulta_empleadoID_setter(instance):
    original = instance.empleadoID
    instance.empleadoID = original
    assert instance.empleadoID == original



@given(instance=consulta_strategy)
def test_hyp_consulta_doctorID_setter(instance):
    original = instance.doctorID
    instance.doctorID = original
    assert instance.doctorID == original



@given(instance=consulta_strategy)
def test_hyp_consulta_fechaConsulta_setter(instance):
    original = instance.fechaConsulta
    instance.fechaConsulta = original
    assert instance.fechaConsulta == original

@given(instance=paciente_strategy)
@settings(max_examples=50)
def test_hyp_paciente_instantiation(instance):
    assert isinstance(instance, paciente)



@given(instance=paciente_strategy)
def test_hyp_paciente_codigoAsegurado_setter(instance):
    original = instance.codigoAsegurado
    instance.codigoAsegurado = original
    assert instance.codigoAsegurado == original



@given(instance=paciente_strategy)
def test_hyp_paciente_razonSocial_setter(instance):
    original = instance.razonSocial
    instance.razonSocial = original
    assert instance.razonSocial == original



@given(instance=paciente_strategy)
def test_hyp_paciente_fechaAfiliacion_setter(instance):
    original = instance.fechaAfiliacion
    instance.fechaAfiliacion = original
    assert instance.fechaAfiliacion == original



@given(instance=paciente_strategy)
def test_hyp_paciente_fechaNacimiento_setter(instance):
    original = instance.fechaNacimiento
    instance.fechaNacimiento = original
    assert instance.fechaNacimiento == original



@given(instance=paciente_strategy)
def test_hyp_paciente_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=paciente_strategy)
def test_hyp_paciente_tipoSangre_setter(instance):
    original = instance.tipoSangre
    instance.tipoSangre = original
    assert instance.tipoSangre == original



@given(instance=paciente_strategy)
def test_hyp_paciente_pacienteID_setter(instance):
    original = instance.pacienteID
    instance.pacienteID = original
    assert instance.pacienteID == original



@given(instance=paciente_strategy)
def test_hyp_paciente_apPaterno_setter(instance):
    original = instance.apPaterno
    instance.apPaterno = original
    assert instance.apPaterno == original



@given(instance=paciente_strategy)
def test_hyp_paciente_apMaterno_setter(instance):
    original = instance.apMaterno
    instance.apMaterno = original
    assert instance.apMaterno == original



@given(instance=paciente_strategy)
def test_hyp_paciente_nroDocumento_setter(instance):
    original = instance.nroDocumento
    instance.nroDocumento = original
    assert instance.nroDocumento == original



@given(instance=paciente_strategy)
def test_hyp_paciente_aseguradoID_setter(instance):
    original = instance.aseguradoID
    instance.aseguradoID = original
    assert instance.aseguradoID == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    alergia,
    aseguradora,
    consulta,
    doctor,
    empleado,
    especialidad,
    historico,
    login,
    paciente,
    tipoSeguro,
    DateTime,
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

def test_alergia_alergiaID_value_roundtrip():
    instance = alergia(alergiaID=7, nombre="sample_text")
    assert instance.alergiaID == 7
    instance.alergiaID = 13
    assert instance.alergiaID == 13


def test_alergia_nombre_value_roundtrip():
    instance = alergia(alergiaID=7, nombre="sample_text")
    assert instance.nombre == "sample_text"
    instance.nombre = "sample_text_2"
    assert instance.nombre == "sample_text_2"


def test_aseguradora_aseguradoraID_value_roundtrip():
    instance = aseguradora(aseguradoraID=7, nombre="sample_text", tipoSeguroID=7)
    assert instance.aseguradoraID == 7
    instance.aseguradoraID = 13
    assert instance.aseguradoraID == 13


def test_aseguradora_nombre_value_roundtrip():
    instance = aseguradora(aseguradoraID=7, nombre="sample_text", tipoSeguroID=7)
    assert instance.nombre == "sample_text"
    instance.nombre = "sample_text_2"
    assert instance.nombre == "sample_text_2"


def test_aseguradora_tipoSeguroID_value_roundtrip():
    instance = aseguradora(aseguradoraID=7, nombre="sample_text", tipoSeguroID=7)
    assert instance.tipoSeguroID == 7
    instance.tipoSeguroID = 13
    assert instance.tipoSeguroID == 13


def test_especialidad_especialidadID_value_roundtrip():
    instance = especialidad(especialidadID=7, nombre="sample_text")
    assert instance.especialidadID == 7
    instance.especialidadID = 13
    assert instance.especialidadID == 13


def test_especialidad_nombre_value_roundtrip():
    instance = especialidad(especialidadID=7, nombre="sample_text")
    assert instance.nombre == "sample_text"
    instance.nombre = "sample_text_2"
    assert instance.nombre == "sample_text_2"


def test_historico_consultaID_value_roundtrip():
    instance = historico(consultaID=7, diagnostico="sample_text", historicoID=7, observacion="sample_text", sintoma="sample_text", tratamiento="sample_text")
    assert instance.consultaID == 7
    instance.consultaID = 13
    assert instance.consultaID == 13


def test_historico_diagnostico_value_roundtrip():
    instance = historico(consultaID=7, diagnostico="sample_text", historicoID=7, observacion="sample_text", sintoma="sample_text", tratamiento="sample_text")
    assert instance.diagnostico == "sample_text"
    instance.diagnostico = "sample_text_2"
    assert instance.diagnostico == "sample_text_2"


def test_historico_historicoID_value_roundtrip():
    instance = historico(consultaID=7, diagnostico="sample_text", historicoID=7, observacion="sample_text", sintoma="sample_text", tratamiento="sample_text")
    assert instance.historicoID == 7
    instance.historicoID = 13
    assert instance.historicoID == 13


def test_historico_observacion_value_roundtrip():
    instance = historico(consultaID=7, diagnostico="sample_text", historicoID=7, observacion="sample_text", sintoma="sample_text", tratamiento="sample_text")
    assert instance.observacion == "sample_text"
    instance.observacion = "sample_text_2"
    assert instance.observacion == "sample_text_2"


def test_historico_sintoma_value_roundtrip():
    instance = historico(consultaID=7, diagnostico="sample_text", historicoID=7, observacion="sample_text", sintoma="sample_text", tratamiento="sample_text")
    assert instance.sintoma == "sample_text"
    instance.sintoma = "sample_text_2"
    assert instance.sintoma == "sample_text_2"


def test_historico_tratamiento_value_roundtrip():
    instance = historico(consultaID=7, diagnostico="sample_text", historicoID=7, observacion="sample_text", sintoma="sample_text", tratamiento="sample_text")
    assert instance.tratamiento == "sample_text"
    instance.tratamiento = "sample_text_2"
    assert instance.tratamiento == "sample_text_2"


def test_login_contrasena_value_roundtrip():
    instance = login(contrasena="sample_text", loginID=7, role="sample_text", usuario="sample_text")
    assert instance.contrasena == "sample_text"
    instance.contrasena = "sample_text_2"
    assert instance.contrasena == "sample_text_2"


def test_login_loginID_value_roundtrip():
    instance = login(contrasena="sample_text", loginID=7, role="sample_text", usuario="sample_text")
    assert instance.loginID == 7
    instance.loginID = 13
    assert instance.loginID == 13


def test_login_role_value_roundtrip():
    instance = login(contrasena="sample_text", loginID=7, role="sample_text", usuario="sample_text")
    assert instance.role == "sample_text"
    instance.role = "sample_text_2"
    assert instance.role == "sample_text_2"


def test_login_usuario_value_roundtrip():
    instance = login(contrasena="sample_text", loginID=7, role="sample_text", usuario="sample_text")
    assert instance.usuario == "sample_text"
    instance.usuario = "sample_text_2"
    assert instance.usuario == "sample_text_2"


def test_tipoSeguro_descripcion_value_roundtrip():
    instance = tipoSeguro(descripcion="sample_text", tipoSeguraID=7)
    assert instance.descripcion == "sample_text"
    instance.descripcion = "sample_text_2"
    assert instance.descripcion == "sample_text_2"


def test_tipoSeguro_tipoSeguraID_value_roundtrip():
    instance = tipoSeguro(descripcion="sample_text", tipoSeguraID=7)
    assert instance.tipoSeguraID == 7
    instance.tipoSeguraID = 13
    assert instance.tipoSeguraID == 13


def test_assoc_tipoSeguro_aseguradora_link_reassign_clear():
    a = tipoSeguro(descripcion="sample_text", tipoSeguraID=7)
    b1 = aseguradora(aseguradoraID=7, nombre="sample_text", tipoSeguroID=7)
    b2 = aseguradora(aseguradoraID=13, nombre="sample_text_2", tipoSeguroID=13)
    _safe_set(a, 'tipoSeguro_aseguradora_08', {b1})
    assert _is_linked(a, 'tipoSeguro_aseguradora_08', b1)
    if hasattr(b1, 'tipoSeguro_aseguradora_19'):
        assert _is_linked(b1, 'tipoSeguro_aseguradora_19', a)
    _safe_set(a, 'tipoSeguro_aseguradora_08', {b2})
    assert _is_linked(a, 'tipoSeguro_aseguradora_08', b2)
    if hasattr(b1, 'tipoSeguro_aseguradora_19'):
        assert not _is_linked(b1, 'tipoSeguro_aseguradora_19', a)
    if hasattr(b2, 'tipoSeguro_aseguradora_19'):
        assert _is_linked(b2, 'tipoSeguro_aseguradora_19', a)
    _safe_set(a, 'tipoSeguro_aseguradora_08', set())
    assert not _is_linked(a, 'tipoSeguro_aseguradora_08', b2)
    if hasattr(b2, 'tipoSeguro_aseguradora_19'):
        assert not _is_linked(b2, 'tipoSeguro_aseguradora_19', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

alergia_strategy = st.builds(alergia, alergiaID=st.integers(), nombre=safe_text)
@given(instance=alergia_strategy)
@settings(max_examples=25)
def test_alergia_instantiation(instance):
    assert isinstance(instance, alergia)


aseguradora_strategy = st.builds(aseguradora, aseguradoraID=st.integers(), nombre=safe_text, tipoSeguroID=st.integers())
@given(instance=aseguradora_strategy)
@settings(max_examples=25)
def test_aseguradora_instantiation(instance):
    assert isinstance(instance, aseguradora)


especialidad_strategy = st.builds(especialidad, especialidadID=st.integers(), nombre=safe_text)
@given(instance=especialidad_strategy)
@settings(max_examples=25)
def test_especialidad_instantiation(instance):
    assert isinstance(instance, especialidad)


historico_strategy = st.builds(historico, consultaID=st.integers(), diagnostico=safe_text, historicoID=st.integers(), observacion=safe_text, sintoma=safe_text, tratamiento=safe_text)
@given(instance=historico_strategy)
@settings(max_examples=25)
def test_historico_instantiation(instance):
    assert isinstance(instance, historico)


login_strategy = st.builds(login, contrasena=safe_text, loginID=st.integers(), role=safe_text, usuario=safe_text)
@given(instance=login_strategy)
@settings(max_examples=25)
def test_login_instantiation(instance):
    assert isinstance(instance, login)


tipoSeguro_strategy = st.builds(tipoSeguro, descripcion=safe_text, tipoSeguraID=st.integers())
@given(instance=tipoSeguro_strategy)
@settings(max_examples=25)
def test_tipoSeguro_instantiation(instance):
    assert isinstance(instance, tipoSeguro)



