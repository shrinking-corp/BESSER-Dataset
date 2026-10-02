#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    Class,
    EnrollPatient_Controller,
    PatientBO,
    PatientDAO,
    PatientTO,
    PlanDAO,
    StateDAO,
    StateDAO1,
    annotations,
    date,
    datetime,
    time,
)


def test_0():
    python_code_.StateDAO()


def test_1():
    var_3 = python_code_.PlanDAO()
    var_7 = -382
    var_8 = "EJ2vwGi TzMfy"
    var_9 = python_code_.EnrollPatient_Controller
    python_code_.PatientTO(
        patient_id=var_7,
        first_name=var_8,
        last_name=var_9,
        password=var_8,
        date_of_birth=var_3,
        email=[],
        contact_no=var_7,
        state_id=True,
        plan_id=var_7,
    )
