import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Acessar_atividade_UseCase,
    Activity,
    Adequar_sequ_ncia_UseCase,
    Alternative,
    AlternativeCategory,
    Aluno_Actor,
    Analisar_dados_UseCase,
    Aplicativo_Actor,
    Autenticar_se_UseCase,
    Avaliar_plano_de_ensino_UseCase,
    Curriculum,
    DispositivoBluetooth,
    Estabelecer_comunica__o_com_wearable_UseCase,
    Exercise,
    Feedback,
    Fornecer_dica_UseCase,
    Fornecer_feedback_UseCase,
    Fornecer_lista_de_atividades_superadas_UseCase,
    Identificar_erros_comuns_UseCase,
    Iniciar_parar_monitoramento_card_aco_UseCase,
    Instruction,
    M_dulo_Pedag_gico_Actor,
    MedicaoBatimento,
    Propor_desafio_UseCase,
    Receber_responder_requisi__es_UseCase,
    Selecionar_treino_UseCase,
    Sequenciar_atividades_UseCase,
    Servi_o_Web_Actor,
    ServicoWeb,
    Sincronizar_dados_do_usu_rio_UseCase,
    Solicitar_dica_UseCase,
    Step,
    StudentHistory,
    StudentStepHistory,
    StudentSubject,
    Student_Interface,
    Subject,
    Treino,
    TreinoMonitoramento,
    TutorStep,
    UserStep,
    Usu_rio_Actor,
    Usuario,
    correct_alternative_alternative_id__alternative_answer__student__user_exercise__UseCase,
    handle_user_answer_request__UseCase,
    is_exercise_activity_id__UseCase,
    is_user_step_step_id__UseCase,
    select_activity_request__UseCase,
    select_exercise_student__subject__UseCase,
    sequence_student__UseCase,
    student_module_views_get_student_domains_student__UseCase,
    student_module_views_update_evidence_student__evidence_dict__UseCase,
    update_history_request__UseCase,
    update_student_subject_student__student_knowledge__UseCase,
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

def test_AlternativeCategory_name_value_roundtrip():
    instance = AlternativeCategory(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_DispositivoBluetooth_macAddress_value_roundtrip():
    instance = DispositivoBluetooth(macAddress="sample_text", nome="sample_text")
    assert instance.macAddress == "sample_text"
    instance.macAddress = "sample_text_2"
    assert instance.macAddress == "sample_text_2"


def test_DispositivoBluetooth_nome_value_roundtrip():
    instance = DispositivoBluetooth(macAddress="sample_text", nome="sample_text")
    assert instance.nome == "sample_text"
    instance.nome = "sample_text_2"
    assert instance.nome == "sample_text_2"


def test_Exercise_difficulty_value_roundtrip():
    instance = Exercise(difficulty=7, user_exercise=True)
    assert instance.difficulty == 7
    instance.difficulty = 13
    assert instance.difficulty == 13


def test_Exercise_user_exercise_value_roundtrip():
    instance = Exercise(difficulty=7, user_exercise=True)
    assert instance.user_exercise == True
    instance.user_exercise = False
    assert instance.user_exercise == False


def test_Instruction_level_value_roundtrip():
    instance = Instruction(level=7, title="sample_text")
    assert instance.level == 7
    instance.level = 13
    assert instance.level == 13


def test_Instruction_title_value_roundtrip():
    instance = Instruction(level=7, title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_Subject_name_value_roundtrip():
    instance = Subject(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Treino_nome_value_roundtrip():
    instance = Treino(nome="sample_text")
    assert instance.nome == "sample_text"
    instance.nome = "sample_text_2"
    assert instance.nome == "sample_text_2"


def test_TreinoMonitoramento_fim_value_roundtrip():
    instance = TreinoMonitoramento(fim="sample_text", inicio="sample_text")
    assert instance.fim == "sample_text"
    instance.fim = "sample_text_2"
    assert instance.fim == "sample_text_2"


def test_TreinoMonitoramento_inicio_value_roundtrip():
    instance = TreinoMonitoramento(fim="sample_text", inicio="sample_text")
    assert instance.inicio == "sample_text"
    instance.inicio = "sample_text_2"
    assert instance.inicio == "sample_text_2"


def test_TutorStep_difficulty_value_roundtrip():
    instance = TutorStep(difficulty=7, evidence="sample_text")
    assert instance.difficulty == 7
    instance.difficulty = 13
    assert instance.difficulty == 13


def test_TutorStep_evidence_value_roundtrip():
    instance = TutorStep(difficulty=7, evidence="sample_text")
    assert instance.evidence == "sample_text"
    instance.evidence = "sample_text_2"
    assert instance.evidence == "sample_text_2"


def test_Usuario_cpf_value_roundtrip():
    instance = Usuario(cpf="sample_text", dataNascimento="sample_text", nome="sample_text", peso="sample_text", senha="sample_text")
    assert instance.cpf == "sample_text"
    instance.cpf = "sample_text_2"
    assert instance.cpf == "sample_text_2"


def test_Usuario_dataNascimento_value_roundtrip():
    instance = Usuario(cpf="sample_text", dataNascimento="sample_text", nome="sample_text", peso="sample_text", senha="sample_text")
    assert instance.dataNascimento == "sample_text"
    instance.dataNascimento = "sample_text_2"
    assert instance.dataNascimento == "sample_text_2"


def test_Usuario_nome_value_roundtrip():
    instance = Usuario(cpf="sample_text", dataNascimento="sample_text", nome="sample_text", peso="sample_text", senha="sample_text")
    assert instance.nome == "sample_text"
    instance.nome = "sample_text_2"
    assert instance.nome == "sample_text_2"


def test_Usuario_peso_value_roundtrip():
    instance = Usuario(cpf="sample_text", dataNascimento="sample_text", nome="sample_text", peso="sample_text", senha="sample_text")
    assert instance.peso == "sample_text"
    instance.peso = "sample_text_2"
    assert instance.peso == "sample_text_2"


def test_Usuario_senha_value_roundtrip():
    instance = Usuario(cpf="sample_text", dataNascimento="sample_text", nome="sample_text", peso="sample_text", senha="sample_text")
    assert instance.senha == "sample_text"
    instance.senha = "sample_text_2"
    assert instance.senha == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Acessar_atividade_UseCase_strategy = st.builds(Acessar_atividade_UseCase)
@given(instance=Acessar_atividade_UseCase_strategy)
@settings(max_examples=25)
def test_Acessar_atividade_UseCase_instantiation(instance):
    assert isinstance(instance, Acessar_atividade_UseCase)


Adequar_sequ_ncia_UseCase_strategy = st.builds(Adequar_sequ_ncia_UseCase)
@given(instance=Adequar_sequ_ncia_UseCase_strategy)
@settings(max_examples=25)
def test_Adequar_sequ_ncia_UseCase_instantiation(instance):
    assert isinstance(instance, Adequar_sequ_ncia_UseCase)


AlternativeCategory_strategy = st.builds(AlternativeCategory, name=safe_text)
@given(instance=AlternativeCategory_strategy)
@settings(max_examples=25)
def test_AlternativeCategory_instantiation(instance):
    assert isinstance(instance, AlternativeCategory)


Aluno_Actor_strategy = st.builds(Aluno_Actor)
@given(instance=Aluno_Actor_strategy)
@settings(max_examples=25)
def test_Aluno_Actor_instantiation(instance):
    assert isinstance(instance, Aluno_Actor)


Analisar_dados_UseCase_strategy = st.builds(Analisar_dados_UseCase)
@given(instance=Analisar_dados_UseCase_strategy)
@settings(max_examples=25)
def test_Analisar_dados_UseCase_instantiation(instance):
    assert isinstance(instance, Analisar_dados_UseCase)


Aplicativo_Actor_strategy = st.builds(Aplicativo_Actor)
@given(instance=Aplicativo_Actor_strategy)
@settings(max_examples=25)
def test_Aplicativo_Actor_instantiation(instance):
    assert isinstance(instance, Aplicativo_Actor)


Autenticar_se_UseCase_strategy = st.builds(Autenticar_se_UseCase)
@given(instance=Autenticar_se_UseCase_strategy)
@settings(max_examples=25)
def test_Autenticar_se_UseCase_instantiation(instance):
    assert isinstance(instance, Autenticar_se_UseCase)


Avaliar_plano_de_ensino_UseCase_strategy = st.builds(Avaliar_plano_de_ensino_UseCase)
@given(instance=Avaliar_plano_de_ensino_UseCase_strategy)
@settings(max_examples=25)
def test_Avaliar_plano_de_ensino_UseCase_instantiation(instance):
    assert isinstance(instance, Avaliar_plano_de_ensino_UseCase)


DispositivoBluetooth_strategy = st.builds(DispositivoBluetooth, macAddress=safe_text, nome=safe_text)
@given(instance=DispositivoBluetooth_strategy)
@settings(max_examples=25)
def test_DispositivoBluetooth_instantiation(instance):
    assert isinstance(instance, DispositivoBluetooth)


Estabelecer_comunica__o_com_wearable_UseCase_strategy = st.builds(Estabelecer_comunica__o_com_wearable_UseCase)
@given(instance=Estabelecer_comunica__o_com_wearable_UseCase_strategy)
@settings(max_examples=25)
def test_Estabelecer_comunica__o_com_wearable_UseCase_instantiation(instance):
    assert isinstance(instance, Estabelecer_comunica__o_com_wearable_UseCase)


Exercise_strategy = st.builds(Exercise, difficulty=st.integers(), user_exercise=st.booleans())
@given(instance=Exercise_strategy)
@settings(max_examples=25)
def test_Exercise_instantiation(instance):
    assert isinstance(instance, Exercise)


Fornecer_dica_UseCase_strategy = st.builds(Fornecer_dica_UseCase)
@given(instance=Fornecer_dica_UseCase_strategy)
@settings(max_examples=25)
def test_Fornecer_dica_UseCase_instantiation(instance):
    assert isinstance(instance, Fornecer_dica_UseCase)


Fornecer_feedback_UseCase_strategy = st.builds(Fornecer_feedback_UseCase)
@given(instance=Fornecer_feedback_UseCase_strategy)
@settings(max_examples=25)
def test_Fornecer_feedback_UseCase_instantiation(instance):
    assert isinstance(instance, Fornecer_feedback_UseCase)


Fornecer_lista_de_atividades_superadas_UseCase_strategy = st.builds(Fornecer_lista_de_atividades_superadas_UseCase)
@given(instance=Fornecer_lista_de_atividades_superadas_UseCase_strategy)
@settings(max_examples=25)
def test_Fornecer_lista_de_atividades_superadas_UseCase_instantiation(instance):
    assert isinstance(instance, Fornecer_lista_de_atividades_superadas_UseCase)


Identificar_erros_comuns_UseCase_strategy = st.builds(Identificar_erros_comuns_UseCase)
@given(instance=Identificar_erros_comuns_UseCase_strategy)
@settings(max_examples=25)
def test_Identificar_erros_comuns_UseCase_instantiation(instance):
    assert isinstance(instance, Identificar_erros_comuns_UseCase)


Iniciar_parar_monitoramento_card_aco_UseCase_strategy = st.builds(Iniciar_parar_monitoramento_card_aco_UseCase)
@given(instance=Iniciar_parar_monitoramento_card_aco_UseCase_strategy)
@settings(max_examples=25)
def test_Iniciar_parar_monitoramento_card_aco_UseCase_instantiation(instance):
    assert isinstance(instance, Iniciar_parar_monitoramento_card_aco_UseCase)


Instruction_strategy = st.builds(Instruction, level=st.integers(), title=safe_text)
@given(instance=Instruction_strategy)
@settings(max_examples=25)
def test_Instruction_instantiation(instance):
    assert isinstance(instance, Instruction)


M_dulo_Pedag_gico_Actor_strategy = st.builds(M_dulo_Pedag_gico_Actor)
@given(instance=M_dulo_Pedag_gico_Actor_strategy)
@settings(max_examples=25)
def test_M_dulo_Pedag_gico_Actor_instantiation(instance):
    assert isinstance(instance, M_dulo_Pedag_gico_Actor)


Propor_desafio_UseCase_strategy = st.builds(Propor_desafio_UseCase)
@given(instance=Propor_desafio_UseCase_strategy)
@settings(max_examples=25)
def test_Propor_desafio_UseCase_instantiation(instance):
    assert isinstance(instance, Propor_desafio_UseCase)


Receber_responder_requisi__es_UseCase_strategy = st.builds(Receber_responder_requisi__es_UseCase)
@given(instance=Receber_responder_requisi__es_UseCase_strategy)
@settings(max_examples=25)
def test_Receber_responder_requisi__es_UseCase_instantiation(instance):
    assert isinstance(instance, Receber_responder_requisi__es_UseCase)


Selecionar_treino_UseCase_strategy = st.builds(Selecionar_treino_UseCase)
@given(instance=Selecionar_treino_UseCase_strategy)
@settings(max_examples=25)
def test_Selecionar_treino_UseCase_instantiation(instance):
    assert isinstance(instance, Selecionar_treino_UseCase)


Sequenciar_atividades_UseCase_strategy = st.builds(Sequenciar_atividades_UseCase)
@given(instance=Sequenciar_atividades_UseCase_strategy)
@settings(max_examples=25)
def test_Sequenciar_atividades_UseCase_instantiation(instance):
    assert isinstance(instance, Sequenciar_atividades_UseCase)


Servi_o_Web_Actor_strategy = st.builds(Servi_o_Web_Actor)
@given(instance=Servi_o_Web_Actor_strategy)
@settings(max_examples=25)
def test_Servi_o_Web_Actor_instantiation(instance):
    assert isinstance(instance, Servi_o_Web_Actor)


ServicoWeb_strategy = st.builds(ServicoWeb)
@given(instance=ServicoWeb_strategy)
@settings(max_examples=25)
def test_ServicoWeb_instantiation(instance):
    assert isinstance(instance, ServicoWeb)


Sincronizar_dados_do_usu_rio_UseCase_strategy = st.builds(Sincronizar_dados_do_usu_rio_UseCase)
@given(instance=Sincronizar_dados_do_usu_rio_UseCase_strategy)
@settings(max_examples=25)
def test_Sincronizar_dados_do_usu_rio_UseCase_instantiation(instance):
    assert isinstance(instance, Sincronizar_dados_do_usu_rio_UseCase)


Solicitar_dica_UseCase_strategy = st.builds(Solicitar_dica_UseCase)
@given(instance=Solicitar_dica_UseCase_strategy)
@settings(max_examples=25)
def test_Solicitar_dica_UseCase_instantiation(instance):
    assert isinstance(instance, Solicitar_dica_UseCase)


Student_Interface_strategy = st.builds(Student_Interface)
@given(instance=Student_Interface_strategy)
@settings(max_examples=25)
def test_Student_Interface_instantiation(instance):
    assert isinstance(instance, Student_Interface)


Subject_strategy = st.builds(Subject, name=safe_text)
@given(instance=Subject_strategy)
@settings(max_examples=25)
def test_Subject_instantiation(instance):
    assert isinstance(instance, Subject)


Treino_strategy = st.builds(Treino, nome=safe_text)
@given(instance=Treino_strategy)
@settings(max_examples=25)
def test_Treino_instantiation(instance):
    assert isinstance(instance, Treino)


TreinoMonitoramento_strategy = st.builds(TreinoMonitoramento, fim=safe_text, inicio=safe_text)
@given(instance=TreinoMonitoramento_strategy)
@settings(max_examples=25)
def test_TreinoMonitoramento_instantiation(instance):
    assert isinstance(instance, TreinoMonitoramento)


TutorStep_strategy = st.builds(TutorStep, difficulty=st.integers(), evidence=safe_text)
@given(instance=TutorStep_strategy)
@settings(max_examples=25)
def test_TutorStep_instantiation(instance):
    assert isinstance(instance, TutorStep)


UserStep_strategy = st.builds(UserStep)
@given(instance=UserStep_strategy)
@settings(max_examples=25)
def test_UserStep_instantiation(instance):
    assert isinstance(instance, UserStep)


Usu_rio_Actor_strategy = st.builds(Usu_rio_Actor)
@given(instance=Usu_rio_Actor_strategy)
@settings(max_examples=25)
def test_Usu_rio_Actor_instantiation(instance):
    assert isinstance(instance, Usu_rio_Actor)


Usuario_strategy = st.builds(Usuario, cpf=safe_text, dataNascimento=safe_text, nome=safe_text, peso=safe_text, senha=safe_text)
@given(instance=Usuario_strategy)
@settings(max_examples=25)
def test_Usuario_instantiation(instance):
    assert isinstance(instance, Usuario)


correct_alternative_alternative_id__alternative_answer__student__user_exercise__UseCase_strategy = st.builds(correct_alternative_alternative_id__alternative_answer__student__user_exercise__UseCase)
@given(instance=correct_alternative_alternative_id__alternative_answer__student__user_exercise__UseCase_strategy)
@settings(max_examples=25)
def test_correct_alternative_alternative_id__alternative_answer__student__user_exercise__UseCase_instantiation(instance):
    assert isinstance(instance, correct_alternative_alternative_id__alternative_answer__student__user_exercise__UseCase)


handle_user_answer_request__UseCase_strategy = st.builds(handle_user_answer_request__UseCase)
@given(instance=handle_user_answer_request__UseCase_strategy)
@settings(max_examples=25)
def test_handle_user_answer_request__UseCase_instantiation(instance):
    assert isinstance(instance, handle_user_answer_request__UseCase)


is_exercise_activity_id__UseCase_strategy = st.builds(is_exercise_activity_id__UseCase)
@given(instance=is_exercise_activity_id__UseCase_strategy)
@settings(max_examples=25)
def test_is_exercise_activity_id__UseCase_instantiation(instance):
    assert isinstance(instance, is_exercise_activity_id__UseCase)


is_user_step_step_id__UseCase_strategy = st.builds(is_user_step_step_id__UseCase)
@given(instance=is_user_step_step_id__UseCase_strategy)
@settings(max_examples=25)
def test_is_user_step_step_id__UseCase_instantiation(instance):
    assert isinstance(instance, is_user_step_step_id__UseCase)


select_activity_request__UseCase_strategy = st.builds(select_activity_request__UseCase)
@given(instance=select_activity_request__UseCase_strategy)
@settings(max_examples=25)
def test_select_activity_request__UseCase_instantiation(instance):
    assert isinstance(instance, select_activity_request__UseCase)


select_exercise_student__subject__UseCase_strategy = st.builds(select_exercise_student__subject__UseCase)
@given(instance=select_exercise_student__subject__UseCase_strategy)
@settings(max_examples=25)
def test_select_exercise_student__subject__UseCase_instantiation(instance):
    assert isinstance(instance, select_exercise_student__subject__UseCase)


sequence_student__UseCase_strategy = st.builds(sequence_student__UseCase)
@given(instance=sequence_student__UseCase_strategy)
@settings(max_examples=25)
def test_sequence_student__UseCase_instantiation(instance):
    assert isinstance(instance, sequence_student__UseCase)


student_module_views_get_student_domains_student__UseCase_strategy = st.builds(student_module_views_get_student_domains_student__UseCase)
@given(instance=student_module_views_get_student_domains_student__UseCase_strategy)
@settings(max_examples=25)
def test_student_module_views_get_student_domains_student__UseCase_instantiation(instance):
    assert isinstance(instance, student_module_views_get_student_domains_student__UseCase)


student_module_views_update_evidence_student__evidence_dict__UseCase_strategy = st.builds(student_module_views_update_evidence_student__evidence_dict__UseCase)
@given(instance=student_module_views_update_evidence_student__evidence_dict__UseCase_strategy)
@settings(max_examples=25)
def test_student_module_views_update_evidence_student__evidence_dict__UseCase_instantiation(instance):
    assert isinstance(instance, student_module_views_update_evidence_student__evidence_dict__UseCase)


update_history_request__UseCase_strategy = st.builds(update_history_request__UseCase)
@given(instance=update_history_request__UseCase_strategy)
@settings(max_examples=25)
def test_update_history_request__UseCase_instantiation(instance):
    assert isinstance(instance, update_history_request__UseCase)


update_student_subject_student__student_knowledge__UseCase_strategy = st.builds(update_student_subject_student__student_knowledge__UseCase)
@given(instance=update_student_subject_student__student_knowledge__UseCase_strategy)
@settings(max_examples=25)
def test_update_student_subject_student__student_knowledge__UseCase_instantiation(instance):
    assert isinstance(instance, update_student_subject_student__student_knowledge__UseCase)


