#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import pytest
import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    AbstractTableModel,
    ArrayList_Instruction_,
    ArrayList_Integer_,
    ArrayList_Interrupter_,
    ArrayList_ProcessData_,
    ArrayList_ProgramFileData_,
    CPU,
    Class,
    Clock,
    Dispatcher,
    Enum,
    Font,
    Hard_Drive,
    IO_Device,
    Instruction_Calculate,
    Instruction_CloseBracket,
    Instruction_DecrementPointer,
    Instruction_DecrementValue,
    Instruction_Exit,
    Instruction_IO,
    Instruction_IncrementPointer,
    Instruction_IncrementValue,
    Instruction_Instruction_Interface,
    Instruction_OpenBracket,
    Instruction_Out,
    Instruction_Print,
    Instruction_Yield,
    Interrupter_Interface,
    JFrame,
    JLabel,
    JScrollPane,
    JTable,
    JTextArea,
    JTextField,
    JobFileData,
    Main,
    Memory,
    Memory__,
    Object,
    Operating_System,
    Page,
    Page__,
    Process,
    ProcessData,
    ProcessState,
    ProcessTableModel,
    ProgramFileData,
    Prompt,
    Request,
    Scheduler,
    Task_Manager,
    annotations,
    date,
    datetime,
    time,
)


def test_0():
    python_code_.Instruction_Calculate(time=complex(922.7384617, -709.466414))
    var_29 = lambda *args, **kwargs: "Instruction_Exit.Process"
    var_30 = python_code_.JScrollPane()
    var_31 = python_code_.JLabel()
    python_code_.Task_Manager(
        contactTable=var_29,
        scrollPane=var_30,
        numberOfProcesses=var_31,
        amountofFreeMemory=var_31,
        amountofUsedMemory=var_31,
    )


@pytest.mark.xfail(strict=True)
def test_1():
    var_0 = python_code_.Memory(memory=None, table=None, operating_System35=None)
    var_2 = python_code_.ProgramFileData(
        name=var_0, memory="LQo qxnuU;Y'.", instructions=var_0
    )
    var_3 = "U'#sYE1\x0cB@Tq"
    python_code_.Hard_Drive(memory=var_3, request48=var_2)
    var_8 = python_code_.ArrayList_ProgramFileData_()
    python_code_.JobFileData(programs=var_8, startTimes=None, programFileData46=var_2)


def test_2():
    var_0 = python_code_.Instruction_IncrementPointer()
    python_code_.JobFileData(programs=var_0, startTimes=None)
    python_code_.Hard_Drive(memory=653)


def test_3():
    var_0 = python_code_.Clock(clockCycle=set(), operating_System29="DG5(kLX(N~O'O")
    var_1 = python_code_.Instruction_IO
    var_2 = -3801
    var_3 = python_code_.ProcessData(
        name={-2576.8, "S!dr<", True},
        startTime={-107.65},
        instructions=var_1,
        memory=var_2,
    )
    python_code_.JobFileData(programs=var_1, startTimes=None, programFileData46=var_3)
    var_5 = python_code_.Instruction_OpenBracket()
    var_6 = ""
    var_7 = python_code_.Process(
        processState=var_0,
        registers=var_6,
        name=var_1,
        memoryUseage={
            "page43": "nMuS+>:\na&m~",
            "&Dk\r!C_W/\x0c*": -439,
            "u<`": "Z^,{n*k4wU\x0cH",
        },
        processTableModel19=var_6,
        task_Manager25=True,
        iO5="operating_System37",
    )
    var_8 = "qp^+Vv1e0l*u^#<\x0b"
    var_9 = python_code_.Instruction_IO()
    var_10 = python_code_.Process(
        processState=var_7,
        registers=var_1,
        name=var_8,
        memoryUseage={-1922, "ry|p\x0c\x0cq<NMF{n))*K", False},
        iO5=var_9,
    )
    python_code_.Scheduler(
        newQueue=var_5, readyQueue=var_7, ioQueue=var_10, identifier=var_8
    )


def test_4():
    var_0 = lambda *args, **kwargs: 3
    python_code_.IO_Device(counter=var_0)
    python_code_.Request(
        startAddress=(-213.63,), endAddress=complex(-4613.1, 1416.5), processID=None
    )
    python_code_.Page(
        owner=[],
        attribute=b"\xadQ<\x02\xb3\xf7,\x0f\xcd\xa9\xa3",
        free=var_0,
        process42="Instruction_IO._ProcessData__instruction15.operating_System23",
    )
    python_code_.Hard_Drive(memory=b"/\xef\x95\xeeI\x88\xd3j>")


def test_5():
    var_0 = "page43"
    var_1 = 0
    var_2 = python_code_.Process(
        processState=None,
        registers=[1761.13, "<Xs%Ro| {a!7,L", "[DiikDas=<CiV0"],
        name=var_0,
        memoryUseage=var_1,
    )
    var_3 = lambda *args, **kwargs: []
    python_code_.Scheduler(
        newQueue={"sssG.3?8s86": -3009},
        readyQueue=b'(h\xf1\xef\xca\x86"\x90&\xd3\n\xd0',
        ioQueue=var_2,
        identifier=var_3,
    )
    var_5 = "ozQq]\\D\x0b$aKy"
    python_code_.ProgramFileData(name=var_5, memory={False}, instructions=[])


def test_6():
    var_13 = -1346
    var_14 = python_code_.Instruction_Exit()
    python_code_.Process(
        processState=None,
        registers=None,
        name=b"\xf4\x17\x81\x88\xf6\x9c\\\n",
        memoryUseage=var_13,
        processTableModel19=[],
        exit9=var_14,
    )
    python_code_.Instruction_Calculate(time=complex(922.7384617, -709.466414))
    var_21 = python_code_.Instruction_DecrementValue()
    var_24 = -64
    var_27 = "SA4*\nfC"
    var_28 = python_code_.ProgramFileData(
        name=var_27,
        memory=var_13,
        instructions=var_21,
        instruction44=None,
        jobFileData47=var_24,
    )
    assert isinstance(var_28, python_code_.ProgramFileData)


def test_7():
    python_code_.Clock(clockCycle=set(), operating_System29="DG5(kLX(N~O'O")
    var_1 = python_code_.Instruction_IO
    var_2 = -3801
    python_code_.ProcessData(
        name={-2576.8, "S!dr<", True},
        startTime={-107.65},
        instructions=var_1,
        memory=var_2,
    )


def test_8():
    var_1 = bool
    var_2 = -611
    var_5 = python_code_.Memory(
        memory=None, table=complex(1172.0, -1806.6970463), operating_System35=var_1
    )
    python_code_.IO_Device(counter=var_2)
    var_7 = python_code_.JFrame()
    var_8 = python_code_.Font()
    var_9 = 0
    var_10 = -1307
    python_code_.Prompt(
        queuePosition=var_1,
        frame=var_7,
        commandLine=(),
        frameFont=var_8,
        output=var_1,
        MAX_COMMAND_LENGTH=var_9,
        OUTPUT_HEIGHT=(),
        OUTPUT_WIDTH=[-1129.1, False, "6[ls=cD!abykw6_2"],
        FONT_SIZE=var_10,
    )
    var_12 = python_code_.CPU(registers=var_5, interruptQueue=var_2)
    python_code_.Process(
        processState=var_1,
        registers=-109.13,
        name=var_12,
        memoryUseage=var_1,
        task_Manager25={},
        page43=var_7,
    )
    var_24 = 45
    python_code_.ProcessData(
        name=var_12,
        startTime=False,
        instructions=None,
        memory=var_24,
        instruction15=var_7,
    )


def test_9():
    python_code_.Clock(clockCycle=4453, operating_System29=None)
    var_5 = python_code_.Instruction_OpenBracket()
    var_6 = ""
    python_code_.Process(
        processState=var_5,
        registers=var_6,
        name=var_6,
        memoryUseage=1,
        iO5=None,
        exit9=None,
    )


def test_10():
    var_22 = python_code_.Hard_Drive
    var_23 = "processTableModel17-operating_System2-operating_System29-_ProgramFileData__instruction44"
    var_24 = -244
    var_26 = python_code_.Instruction_Out()
    var_27 = python_code_.Process(
        processState=var_22,
        registers=var_22,
        name=var_23,
        memoryUseage=var_24,
        processTableModel19=var_26,
        task_Manager25=False,
        page43=var_23,
    )
    assert isinstance(var_27, python_code_.Process)
    python_code_.Hard_Drive(memory=653)


@pytest.mark.xfail(strict=True)
def test_11():
    var_12 = python_code_.JLabel()
    var_13 = -1346
    var_14 = python_code_.Instruction_Exit()
    var_15 = python_code_.Process(
        processState=None,
        registers=None,
        name=b"\xf4\x17\x81\x88\xf6\x9c\\\n",
        memoryUseage=var_13,
        processTableModel19=[],
        exit9=var_14,
    )
    python_code_.Task_Manager(
        contactTable=4139.06,
        scrollPane=False,
        numberOfProcesses=[],
        amountofFreeMemory=var_12,
        amountofUsedMemory="Vkkfrcsh",
        process24=var_15,
    )


def test_12():
    var_0 = python_code_.Clock(clockCycle=2307, operating_System29=None)
    var_1 = python_code_.Dispatcher
    var_6 = ""
    python_code_.Process(
        processState=var_0,
        registers=var_6,
        name=var_1,
        memoryUseage={
            "page43": "nMuS+>:\na&m~",
            "&Dk\r!C_W/\x0c*": -439,
            "u<`": "Z^,{n*k4wU\x0cH",
        },
        processTableModel19=var_6,
        task_Manager25=True,
        iO5="operating_System37",
    )


def test_13():
    var_22 = python_code_.Hard_Drive
    var_24 = -104
    var_25 = "Ifnstruction_IO"
    python_code_.ProcessTableModel(
        columnNames=var_25, processList=set(), numberProcesses=var_24
    )
    python_code_.Process(
        processState=var_22,
        registers=var_25,
        name="",
        memoryUseage=var_24,
        exit9=var_24,
    )


@pytest.mark.xfail(strict=True)
def test_14():
    var_22 = python_code_.Hard_Drive
    var_23 = "processTableModel17-operating_System2-operating_System29-_ProgramFileData__instruction44"
    var_24 = -244
    var_25 = "Instruction_IO"
    var_26 = python_code_.ProcessTableModel(
        columnNames=var_25, processList=set(), numberProcesses=var_24
    )
    python_code_.Process(
        processState=var_22,
        registers=var_22,
        name=var_23,
        memoryUseage=var_24,
        processTableModel19=var_26,
        task_Manager25=False,
        page43=var_23,
    )


def test_15():
    var_1 = python_code_.Object()
    var_3 = python_code_.Instruction_Exit()
    var_5 = python_code_.Instruction_CloseBracket()
    var_6 = lambda *args, **kwargs: "k(4M~TS.ai"
    python_code_.Process(
        processState=var_1,
        registers=var_5,
        name={584, 10.28, False},
        memoryUseage=-761,
        page43=var_6,
    )
    var_9 = 619
    python_code_.ProcessTableModel(
        columnNames=var_5,
        processList=1924,
        numberProcesses=var_9,
        process18={"xw~": True, "{WM<ky},/Mv<\x0c,f&.:u": 1103},
    )
    var_11 = 3
    python_code_.Instruction_Calculate(time=var_11)
    python_code_.Page(owner=var_6, attribute=var_3, free=var_6)
    var_14 = python_code_.JLabel()
    var_31 = python_code_.Prompt
    var_35 = python_code_.JTable()
    var_36 = python_code_.JScrollPane()
    var_37 = python_code_.JLabel()
    python_code_.Task_Manager(
        contactTable=var_35,
        scrollPane=var_36,
        numberOfProcesses=var_14,
        amountofFreeMemory=var_14,
        amountofUsedMemory=var_37,
    )
    var_40 = -2846
    python_code_.Clock(clockCycle=var_40)
    var_46 = "4p*nZG"
    python_code_.CPU(registers=var_46, interruptQueue=var_31)
    var_62 = "Yq\\!m\x0bmaEQ\x0bQBV"
    var_63 = "_CPU__operating_System31"
    python_code_.ProcessTableModel(
        columnNames=var_62, processList=var_63, numberProcesses=var_35
    )


@pytest.mark.xfail(strict=True)
def test_16():
    python_code_.Instruction_Calculate(time=complex(922.7384617, -709.466414))
    var_29 = lambda *args, **kwargs: "Instruction_Exit.Process"
    var_30 = python_code_.JScrollPane()
    var_37 = 1297
    var_39 = python_code_.Page(owner=var_29, attribute=var_30, free=var_37)
    python_code_.Memory(memory=None, table=None, page50=var_39, operating_System35={})


@pytest.mark.xfail(strict=True)
def test_17():
    var_0 = lambda *args, **kwargs: 3
    python_code_.IO_Device(counter=var_0)
    python_code_.Request(
        startAddress=(-213.63,), endAddress=complex(-4613.1, 1416.5), processID=None
    )
    var_5 = "[*\x0b[A8ZG%|q]L:UeTVR"
    python_code_.Page(owner=var_0, attribute=var_5, free=var_0, memory51=None)
    var_35 = python_code_.Font()
    var_36 = -1777
    var_37 = -492
    var_38 = python_code_.Prompt(
        queuePosition=var_37,
        frame=1301.52,
        commandLine=var_0,
        frameFont=var_35,
        output=var_0,
        MAX_COMMAND_LENGTH=var_36,
        OUTPUT_HEIGHT=var_36,
        OUTPUT_WIDTH=var_37,
        FONT_SIZE=var_37,
    )
    var_41 = python_code_.Prompt
    var_42 = 1
    var_43 = python_code_.Memory(
        memory=var_37, table=var_36, page50={-266.73, -600.74, False}
    )
    python_code_.IO_Device(counter=var_37, operating_System39=265.7)
    var_45 = python_code_.JTable()
    var_46 = python_code_.JScrollPane()
    var_47 = python_code_.JLabel()
    python_code_.Task_Manager(
        contactTable=var_45,
        scrollPane=var_46,
        numberOfProcesses=var_47,
        amountofFreeMemory=var_47,
        amountofUsedMemory=var_47,
    )
    var_50 = -2846
    var_53 = 457
    var_54 = 3668
    var_55 = python_code_.Clock(clockCycle=var_50)
    var_56 = "4p*nZG"
    var_57 = python_code_.CPU(registers=var_56, interruptQueue=var_41)
    var_58 = python_code_.Main()
    var_59 = python_code_.Instruction_Out()
    python_code_.Operating_System(
        MEMORY_SIZE=var_0,
        PAGE_SIZE=None,
        NUMBER_OF_REGISTERS=var_47,
        INSTRUCTION_REGISTER=var_37,
        PROC_BASE_REGISTER=var_54,
        PROC_LIMIT_REGISTER=var_53,
        PROCESS_ID_REGISTER=var_42,
        PROC_BASE_POINTER=var_0,
        PROC_DATA_POINTER=var_50,
        QUANTUM=var_36,
        clock=var_55,
        cpu=var_57,
        dispatcher=None,
        memory=var_43,
        scheduler=var_53,
        device=[-2219.91, "\\P"],
        hardDrive=668.18,
        prompt=var_38,
        taskManager=None,
        prompt20=var_38,
        main26=var_58,
        cPU30=var_57,
        exit7=[],
        calculate11="~J}\t\x0c\nZH3u %=w`",
        out13=var_59,
    )


@pytest.mark.xfail(strict=True)
def test_18():
    var_22 = python_code_.Hard_Drive
    var_26 = python_code_.Instruction_Out()
    var_36 = -12
    var_38 = python_code_.Dispatcher()
    var_39 = python_code_.Hard_Drive(memory=653)
    var_41 = python_code_.JLabel()
    var_45 = 1573
    var_46 = -978
    var_47 = 1242
    var_48 = -2638
    var_49 = python_code_.Clock(clockCycle=var_48)
    var_50 = python_code_.IO_Device(counter=var_22)
    var_51 = python_code_.Prompt(
        queuePosition=var_36,
        frame=var_22,
        commandLine=var_22,
        frameFont=var_36,
        output=var_46,
        MAX_COMMAND_LENGTH=(),
        OUTPUT_HEIGHT=-3680,
        OUTPUT_WIDTH=var_48,
        FONT_SIZE=var_45,
    )
    var_52 = python_code_.JTable()
    var_53 = python_code_.Task_Manager(
        contactTable=var_52,
        scrollPane=var_41,
        numberOfProcesses="\x0c",
        amountofFreeMemory=(1515.46, True),
        amountofUsedMemory=-1655,
    )
    python_code_.Operating_System(
        MEMORY_SIZE=var_36,
        PAGE_SIZE=var_45,
        NUMBER_OF_REGISTERS=(True, 1397, False),
        INSTRUCTION_REGISTER="ng|'5p(f7)",
        PROC_BASE_REGISTER=var_36,
        PROC_LIMIT_REGISTER=var_46,
        PROCESS_ID_REGISTER=b"=hN\xea\x12\xd2'zd\x0fJ\xd0",
        PROC_BASE_POINTER=var_47,
        PROC_DATA_POINTER=var_39,
        QUANTUM=(),
        clock=var_49,
        cpu={},
        dispatcher=var_38,
        memory=0,
        scheduler=598,
        device=var_50,
        hardDrive=[-3232, 605, 3503],
        prompt=var_51,
        taskManager=var_53,
        cPU30=var_26,
        dispatcher32=var_38,
        out13=(),
        iO_Device38=var_50,
    )


@pytest.mark.xfail(strict=True)
def test_19():
    var_0 = python_code_.Instruction_CloseBracket()
    var_1 = python_code_.Instruction_DecrementValue()
    var_3 = hash
    var_4 = -1696
    var_5 = -3131
    var_6 = python_code_.Clock(clockCycle=var_4, operating_System29=True)
    var_7 = "'~'Si4sr:3#"
    var_8 = python_code_.Instruction_IO()
    var_9 = python_code_.Instruction_Exit()
    var_10 = python_code_.Process(
        processState=var_6,
        registers=var_7,
        name=var_3,
        memoryUseage=var_0,
        iO5=var_8,
        exit9=var_9,
    )
    var_11 = 1144
    var_12 = python_code_.Scheduler(
        newQueue=var_3, readyQueue=var_3, ioQueue=var_10, identifier=var_11
    )
    var_13 = python_code_.JFrame()
    var_14 = python_code_.JTextArea()
    var_15 = -4201
    python_code_.Prompt(
        queuePosition=var_7,
        frame=var_13,
        commandLine=var_3,
        frameFont=var_12,
        output=var_14,
        MAX_COMMAND_LENGTH=3998,
        OUTPUT_HEIGHT=var_15,
        OUTPUT_WIDTH=var_1,
        FONT_SIZE=var_1,
        operating_System21=var_5,
    )
    python_code_.CPU(registers=var_7, interruptQueue=complex(-2443.825931, -9.65))
    python_code_.Hard_Drive(memory=653)
    var_22 = python_code_.JTable()
    var_23 = python_code_.JLabel()
    python_code_.Task_Manager(
        contactTable=var_22,
        scrollPane=True,
        numberOfProcesses={"N2&hEq]ljRh9s=htl b": 886.28, "xnM=tM|H": ";b AN1<J"},
        amountofFreeMemory=var_12,
        amountofUsedMemory=var_23,
        process24=var_10,
    )


def test_20():
    var_0 = python_code_.Instruction_IO()
    python_code_.Clock(clockCycle=-1898)
    var_4 = python_code_.Instruction_Print()
    var_8 = python_code_.Hard_Drive
    var_9 = True
    python_code_.Page(owner=var_0, attribute=var_8, free=var_9, memory51=-362)
    var_11 = ""
    python_code_.Hard_Drive(memory=var_11, operating_System41=var_4)
    python_code_.Hard_Drive(memory=653)


def test_21():
    var_1 = bool
    var_2 = -611
    python_code_.Memory(
        memory=None, table=complex(1172.0, -1806.6970463), operating_System35=var_1
    )
    python_code_.IO_Device(counter=var_2)


def test_22():
    var_0 = python_code_.Memory(memory=None, table=None, operating_System35=None)
    python_code_.ProgramFileData(name=var_0, memory="LQo qxnuU;Y'.", instructions=var_0)
    python_code_.IO_Device(counter=-1517)
    python_code_.Hard_Drive(memory=b"/\xef\x95\xeeI\x88\xd3j>")


def test_23():
    var_0 = lambda *args, **kwargs: 3
    python_code_.IO_Device(counter=var_0)
    var_2 = python_code_.AbstractTableModel()
    python_code_.Request(
        startAddress=(-213.63,), endAddress=complex(-4613.1, 1416.5), processID=None
    )
    var_66 = python_code_.Hard_Drive
    var_67 = "processTableModel17-operating_System2-operating_System29-_ProgramFileData__instruction44"
    var_68 = -244
    var_70 = python_code_.Instruction_Out()
    var_71 = python_code_.Process(
        processState=var_66,
        registers=var_66,
        name=var_67,
        memoryUseage=var_68,
        processTableModel19=var_70,
        task_Manager25=False,
        page43=var_67,
    )
    assert isinstance(var_71, python_code_.Process)
    python_code_.Hard_Drive(memory=653)
    python_code_.Memory(
        memory=-1579.53, table=None, page50=var_2, operating_System35=var_66
    )


@pytest.mark.xfail(strict=True)
def test_24():
    var_0 = 2979
    var_1 = python_code_.Memory__
    var_2 = -779
    var_3 = python_code_.Clock(clockCycle=var_0)
    var_4 = "}q4_cV\x0bjX|2S8Rz\\|~"
    var_5 = python_code_.CPU(registers=var_4, interruptQueue=var_3)
    var_6 = python_code_.Dispatcher()
    var_7 = -1895
    var_8 = python_code_.IO_Device(counter=var_7, operating_System39=var_0)
    var_9 = python_code_.Hard_Drive(memory="z:{Y}Ea")
    var_10 = python_code_.JFrame()
    var_11 = python_code_.Font()
    var_12 = python_code_.JTextArea()
    var_13 = python_code_.Prompt(
        queuePosition=complex(-3572.6358, 3299.7),
        frame=var_10,
        commandLine=var_10,
        frameFont=var_11,
        output=var_12,
        MAX_COMMAND_LENGTH=var_10,
        OUTPUT_HEIGHT=var_1,
        OUTPUT_WIDTH=var_2,
        FONT_SIZE=set(),
    )
    var_14 = lambda *args, **kwargs: "Instruction_Exit.Process"
    var_15 = python_code_.JScrollPane()
    var_16 = python_code_.JLabel()
    var_17 = python_code_.Task_Manager(
        contactTable=var_14,
        scrollPane=var_15,
        numberOfProcesses=var_16,
        amountofFreeMemory=var_16,
        amountofUsedMemory=var_16,
    )
    var_18 = python_code_.Main()
    var_19 = python_code_.ArrayList_Interrupter_
    var_20 = python_code_.Instruction_Yield()
    var_21 = python_code_.Instruction_Exit()
    python_code_.Operating_System(
        MEMORY_SIZE=var_0,
        PAGE_SIZE="@HjHx?|=K,hnW",
        NUMBER_OF_REGISTERS=var_0,
        INSTRUCTION_REGISTER=var_0,
        PROC_BASE_REGISTER=var_1,
        PROC_LIMIT_REGISTER=var_2,
        PROCESS_ID_REGISTER=var_0,
        PROC_BASE_POINTER=True,
        PROC_DATA_POINTER=var_1,
        QUANTUM=2772.4,
        clock=var_3,
        cpu=var_5,
        dispatcher=var_6,
        memory=var_1,
        scheduler=var_3,
        device=var_8,
        hardDrive=var_9,
        prompt=var_13,
        taskManager=var_17,
        main26=var_18,
        cPU30=var_5,
        dispatcher32=var_19,
        memory34=False,
        yield1=var_20,
        exit7=var_21,
        calculate11=[],
        iO_Device38=var_8,
        hard_Drive40=var_5,
    )


def test_25():
    var_0 = lambda *args, **kwargs: 3
    python_code_.Request(
        startAddress=(-213.63,), endAddress=complex(-4613.1, 1416.5), processID=None
    )
    var_7 = python_code_.JTextField()
    python_code_.Page(
        owner=[],
        attribute=b"\xadQ<\x02\xb3\xf7,\x0f\xcd\xa9\xa3",
        free=var_0,
        process42="Instruction_IO._ProcessData__instruction15.operating_System23",
    )
    python_code_.IO_Device(counter=1124)
    var_25 = -52
    python_code_.CPU(
        registers=["operating_System21", 1285.62, -4714], interruptQueue={"QCB[n-"}
    )
    python_code_.Memory(memory=var_7, table=var_25)


def test_26():
    var_2 = python_code_.Instruction_Print()
    var_5 = -3131
    var_7 = "'~'Si4sr:3#"
    python_code_.CPU(registers=var_7, interruptQueue=var_2, operating_System31=var_5)
    python_code_.Hard_Drive(memory=653)


@pytest.mark.xfail(strict=True)
def test_27():
    var_1 = 3702
    python_code_.Request(startAddress=var_1, endAddress=var_1, processID=var_1)
    var_3 = python_code_.Dispatcher()
    var_4 = python_code_.Hard_Drive(memory=var_3)
    var_5 = 1
    var_6 = -2036
    var_7 = python_code_.Memory(memory=var_3, table=var_4)
    var_8 = "process4_Operating_System__iO3"
    python_code_.ProcessData(
        name=var_8, startTime=var_3, instructions=var_6, memory=var_1
    )
    var_10 = tuple
    var_11 = -1469
    var_12 = -2245
    var_13 = -3555
    var_14 = 2178
    var_15 = -695
    var_16 = 229
    var_17 = python_code_.Clock(clockCycle=var_14, operating_System29=var_16)
    var_18 = "\t%:_oP"
    var_19 = python_code_.ProcessData(
        name=var_8,
        startTime=var_18,
        instructions=var_10,
        memory=var_5,
        instruction15=True,
    )
    assert isinstance(var_19, python_code_.ProcessData)
    var_20 = 707
    var_21 = python_code_.Process(
        processState=var_7, registers=var_1, name=var_8, memoryUseage=var_20
    )
    var_22 = python_code_.Scheduler(
        newQueue=var_19,
        readyQueue=var_21,
        ioQueue=-1228.33,
        identifier=["operating_System12", "wYWG", True],
    )
    var_23 = python_code_.JTextArea()
    var_24 = 2
    var_25 = 107
    var_26 = python_code_.Prompt(
        queuePosition=(),
        frame=var_10,
        commandLine=var_10,
        frameFont=var_11,
        output=var_23,
        MAX_COMMAND_LENGTH=var_24,
        OUTPUT_HEIGHT=b"J\xba\x19\xc6IjWq\xe6\xe4\xa8",
        OUTPUT_WIDTH=var_10,
        FONT_SIZE=var_25,
    )
    var_27 = 127
    var_28 = python_code_.Clock(clockCycle=var_27)
    var_29 = python_code_.Instruction_Yield()
    var_30 = python_code_.Instruction_Exit()
    var_31 = python_code_.Instruction_Out()
    python_code_.Operating_System(
        MEMORY_SIZE=var_11,
        PAGE_SIZE=var_7,
        NUMBER_OF_REGISTERS=var_12,
        INSTRUCTION_REGISTER=var_13,
        PROC_BASE_REGISTER=var_7,
        PROC_LIMIT_REGISTER=var_14,
        PROCESS_ID_REGISTER=1317,
        PROC_BASE_POINTER=var_15,
        PROC_DATA_POINTER=var_5,
        QUANTUM=var_16,
        clock=var_17,
        cpu=var_7,
        dispatcher=var_3,
        memory=[-252.93, 948.39],
        scheduler=var_22,
        device=set(),
        hardDrive=["6DFG|0#dD/i", -1243, 92],
        prompt=var_26,
        taskManager=var_10,
        clock28=var_28,
        yield1=var_29,
        exit7=var_30,
        out13=var_31,
        scheduler36=var_22,
        iO_Device38=var_30,
    )


def test_28():
    python_code_.Clock(clockCycle=set(), operating_System29="DG5(kLX(N~O'O")


def test_29():
    python_code_.Clock(clockCycle=595, operating_System29=None)


@pytest.mark.xfail(strict=True)
def test_30():
    var_0 = python_code_.Dispatcher()
    var_1 = python_code_.JTable()
    var_2 = python_code_.Clock(clockCycle=None)
    var_3 = python_code_.JTextField()
    var_4 = lambda *args, **kwargs: 1988
    var_5 = 1
    var_6 = python_code_.Prompt(
        queuePosition=var_1,
        frame='"j2n',
        commandLine=var_3,
        frameFont=var_2,
        output=b"\x9b\xbc\xd1{\x9d",
        MAX_COMMAND_LENGTH=var_4,
        OUTPUT_HEIGHT=var_5,
        OUTPUT_WIDTH=var_0,
        FONT_SIZE=var_5,
    )
    var_7 = python_code_.Instruction_Instruction_Interface()
    var_8 = "D!-S\\m=/NdALE"
    var_9 = python_code_.ProcessData(
        name=var_8, startTime=-2106.93, instructions=None, memory=var_4
    )
    var_10 = python_code_.ProcessData(
        name="nb;G Ft", startTime=var_8, instructions="<\\t+J.A+", memory=var_5
    )
    var_11 = python_code_.JScrollPane()
    var_12 = python_code_.JFrame()
    var_14 = python_code_.Instruction_IO()
    var_15 = python_code_.Process(
        processState={
            "Instruction_IO": False,
            "": "xj@Nd&g(H?XM<wC)",
            "DmL\nFDGho": 2393,
        },
        registers={"\tp": 692},
        name=var_10,
        memoryUseage=var_9,
        iO5=var_14,
        page43="V/\rEO_CC3D[",
    )
    assert isinstance(var_15, python_code_.Process)
    var_16 = 4737
    var_17 = 0
    var_18 = -5706
    var_19 = python_code_.IO_Device(counter=var_7)
    var_20 = python_code_.Hard_Drive(memory=False, request48=var_9)
    var_21 = python_code_.Font()
    var_22 = python_code_.JTextArea()
    var_23 = 1955
    var_24 = 904
    var_25 = python_code_.Prompt(
        queuePosition=var_8,
        frame=var_12,
        commandLine=var_7,
        frameFont=var_21,
        output=var_22,
        MAX_COMMAND_LENGTH=None,
        OUTPUT_HEIGHT=var_23,
        OUTPUT_WIDTH=var_21,
        FONT_SIZE=var_24,
    )
    python_code_.Operating_System(
        MEMORY_SIZE=var_10,
        PAGE_SIZE=3119.81,
        NUMBER_OF_REGISTERS=var_16,
        INSTRUCTION_REGISTER=var_1,
        PROC_BASE_REGISTER=var_17,
        PROC_LIMIT_REGISTER=var_18,
        PROCESS_ID_REGISTER=var_6,
        PROC_BASE_POINTER=var_12,
        PROC_DATA_POINTER=var_17,
        QUANTUM=var_14,
        clock=var_2,
        cpu=var_4,
        dispatcher=[],
        memory=var_2,
        scheduler=var_11,
        device=var_19,
        hardDrive=var_20,
        prompt=var_25,
        taskManager=var_14,
        main26=var_8,
        clock28=var_6,
        iO3=set(),
        exit7=var_24,
        scheduler36=var_4,
        iO_Device38=var_19,
    )


@pytest.mark.xfail(strict=True)
def test_31():
    var_2 = python_code_.Instruction_Exit()
    var_3 = lambda *args, **kwargs: 3
    var_4 = "ccnfCy!=5l[mrT|OZ"
    var_5 = 456
    var_6 = 1806
    var_7 = "6nMm$nNH4t\rt"
    var_8 = 1556
    var_9 = python_code_.Dispatcher
    var_10 = 1810
    var_11 = 1
    var_12 = python_code_.CPU(registers=var_2, interruptQueue=var_4)
    var_13 = python_code_.Dispatcher()
    var_14 = python_code_.Memory(memory=var_9, table=var_13, operating_System35=var_9)
    var_15 = 2
    var_16 = python_code_.Process(
        processState=var_9, registers=var_9, name=(), memoryUseage=var_15
    )
    var_17 = python_code_.Scheduler(
        newQueue=148.11, readyQueue=var_16, ioQueue=var_16, identifier=var_4
    )
    var_18 = python_code_.Operating_System(
        MEMORY_SIZE=var_8,
        PAGE_SIZE=[
            "I\"Kyb'KYWgCf",
            False,
            "Task_Manager:ProcessTableModel:Instruction_Out:Task_Manager",
        ],
        NUMBER_OF_REGISTERS=var_2,
        INSTRUCTION_REGISTER=var_9,
        PROC_BASE_REGISTER=var_6,
        PROC_LIMIT_REGISTER=b"\xc33\xec-\xa2\xd4s\xe1N\xf0\x8f\xc3~\xbd\x88?",
        PROCESS_ID_REGISTER=var_8,
        PROC_BASE_POINTER=var_10,
        PROC_DATA_POINTER=var_11,
        QUANTUM=var_5,
        clock=var_9,
        cpu=var_12,
        dispatcher=var_13,
        memory=var_14,
        scheduler=var_17,
        device=var_5,
        hardDrive=210.64,
        prompt={
            "_IO_Device__operating_System39": -2002,
            "KH[t[!@B-4sT": False,
            "{#S/V]`": True,
        },
        taskManager=[],
        exit7=var_5,
        hard_Drive40=False,
    )
    python_code_.CPU(registers=var_7, interruptQueue=var_3, operating_System31=var_18)


@pytest.mark.xfail(strict=True)
def test_32():
    var_22 = python_code_.Hard_Drive
    var_24 = -244
    var_39 = python_code_.Hard_Drive(memory=653)
    var_43 = python_code_.ArrayList_ProgramFileData_
    var_45 = 1573
    var_46 = -978
    var_47 = 1242
    var_56 = python_code_.ArrayList_Interrupter_
    var_57 = python_code_.Instruction_Yield()
    var_58 = python_code_.Instruction_Exit()
    var_59 = "y`^LjT"
    var_60 = 537
    var_61 = python_code_.IO_Device(counter=var_57)
    var_62 = python_code_.JFrame()
    var_63 = python_code_.JTextField()
    var_64 = python_code_.JTextArea()
    var_65 = 1616
    var_66 = 994
    var_67 = python_code_.Prompt(
        queuePosition=var_45,
        frame=var_62,
        commandLine=var_63,
        frameFont=var_43,
        output=var_64,
        MAX_COMMAND_LENGTH=var_65,
        OUTPUT_HEIGHT=var_65,
        OUTPUT_WIDTH=var_47,
        FONT_SIZE=var_66,
    )
    python_code_.Operating_System(
        MEMORY_SIZE=var_59,
        PAGE_SIZE=var_43,
        NUMBER_OF_REGISTERS=var_46,
        INSTRUCTION_REGISTER=var_60,
        PROC_BASE_REGISTER=var_45,
        PROC_LIMIT_REGISTER=var_24,
        PROCESS_ID_REGISTER=var_22,
        PROC_BASE_POINTER=complex(1762.21204, 597.32089),
        PROC_DATA_POINTER=var_56,
        QUANTUM=-1445.78,
        clock=var_58,
        cpu=var_60,
        dispatcher=var_56,
        memory=var_59,
        scheduler={},
        device=var_61,
        hardDrive=var_39,
        prompt=var_67,
        taskManager=var_62,
        yield1=[1542.35],
        exit7=var_58,
        hard_Drive40=var_39,
    )


@pytest.mark.xfail(strict=True)
def test_33():
    var_0 = python_code_.Instruction_IO()
    python_code_.Clock(clockCycle=False)
    var_4 = python_code_.Instruction_Print()
    var_5 = python_code_.AbstractTableModel()
    var_8 = python_code_.Hard_Drive
    var_9 = True
    python_code_.Page(owner=var_0, attribute=var_8, free=var_9, memory51=-362)
    var_11 = ""
    python_code_.Hard_Drive(memory=var_11, operating_System41=var_4)
    var_14 = python_code_.ArrayList_ProgramFileData_()
    var_16 = python_code_.JTextArea()
    var_18 = python_code_.Object()
    var_19 = python_code_.JobFileData(programs=var_14, startTimes=None)
    var_20 = python_code_.IO_Device(counter=var_9)
    python_code_.Page(owner=var_8, attribute=var_11, free=var_9)
    var_22 = python_code_.Font()
    var_24 = -1670
    var_25 = lambda *args, **kwargs: 1473
    var_26 = python_code_.Request(
        startAddress=var_24, endAddress=var_9, processID=var_25
    )
    var_27 = "X;:Hxaw"
    var_28 = -201
    var_29 = 3822
    var_30 = 3
    var_31 = -873
    var_32 = python_code_.JTextField()
    var_33 = (
        lambda *args, **kwargs: "_Memory__page50._Operating_System__out13.Process._Process__iO5"
    )
    python_code_.Prompt(
        queuePosition=[],
        frame=var_25,
        commandLine=var_32,
        frameFont=var_33,
        output=var_16,
        MAX_COMMAND_LENGTH=var_33,
        OUTPUT_HEIGHT={},
        OUTPUT_WIDTH=var_29,
        FONT_SIZE=var_22,
    )
    var_35 = 0
    var_36 = python_code_.Interrupter_Interface
    var_37 = python_code_.CPU(
        registers=["operating_System21", 1285.62, -4714], interruptQueue={"QCB[n-"}
    )
    var_38 = python_code_.Memory(memory=var_32, table=var_29)
    var_39 = python_code_.ProcessData(
        name=var_4, startTime=var_5, instructions=var_36, memory=var_35
    )
    var_40 = python_code_.Process(
        processState={},
        registers=var_8,
        name=var_14,
        memoryUseage={},
        processTableModel19=var_26,
        iO5=var_0,
    )
    var_41 = python_code_.Scheduler(
        newQueue=var_39, readyQueue=var_40, ioQueue=var_8, identifier=var_28
    )
    var_42 = python_code_.Main()
    var_43 = python_code_.Operating_System(
        MEMORY_SIZE=var_35,
        PAGE_SIZE=var_29,
        NUMBER_OF_REGISTERS=var_36,
        INSTRUCTION_REGISTER=var_24,
        PROC_BASE_REGISTER=True,
        PROC_LIMIT_REGISTER=var_36,
        PROCESS_ID_REGISTER=var_19,
        PROC_BASE_POINTER=True,
        PROC_DATA_POINTER=var_30,
        QUANTUM=var_11,
        clock=var_36,
        cpu=var_37,
        dispatcher=-4150,
        memory=var_38,
        scheduler=var_41,
        device=var_20,
        hardDrive=var_33,
        prompt=[False, 'S}&xE"tC+_\t4', -4058.45],
        taskManager=var_18,
        processTableModel17=complex(379.0, -370.9998),
        main26=var_42,
    )
    python_code_.ProcessTableModel(
        columnNames=var_31,
        processList=var_27,
        numberProcesses=0,
        operating_System16=var_43,
        process18=var_25,
    )


@pytest.mark.xfail(strict=True)
def test_34():
    var_0 = python_code_.Clock(clockCycle=set(), operating_System29="DG5(kLX(N~O'O")
    var_1 = python_code_.Instruction_IO
    var_2 = -3801
    var_3 = python_code_.ProcessData(
        name="{)CQj(R|$Y",
        startTime=";NE",
        instructions=var_0,
        memory=var_2,
        instruction15=None,
    )
    var_4 = python_code_.JobFileData(
        programs=var_1, startTimes=None, programFileData46=var_3
    )
    var_5 = python_code_.Instruction_OpenBracket()
    var_6 = "v"
    var_7 = python_code_.Process(
        processState=var_0,
        registers=var_6,
        name=var_1,
        memoryUseage={
            "page43": "nMuS+>:\na&m~",
            "&Dk\r!C_W/\x0c*": -439,
            "u<`": "Z^,{n*k4wU\x0cH",
        },
        processTableModel19=var_6,
        task_Manager25=True,
        iO5="operating_System37",
    )
    var_8 = "qp^+Vv1e0l*u^#<\x0b"
    var_9 = python_code_.Instruction_IO()
    var_10 = python_code_.Process(
        processState=var_7,
        registers=var_1,
        name=var_8,
        memoryUseage={-1922, "ry|p\x0c\x0cq<NMF{n))*K", False},
        iO5=var_9,
    )
    var_12 = 181
    var_13 = complex
    var_14 = python_code_.Scheduler(
        newQueue=var_3, readyQueue=var_4, ioQueue=var_5, identifier=var_13
    )
    var_15 = 911
    var_16 = python_code_.JTextField()
    var_17 = python_code_.Font()
    var_18 = 218
    var_19 = python_code_.Prompt(
        queuePosition=var_15,
        frame=var_5,
        commandLine=var_16,
        frameFont=var_17,
        output=var_17,
        MAX_COMMAND_LENGTH=var_2,
        OUTPUT_HEIGHT=var_2,
        OUTPUT_WIDTH=(2073.35, -792.22, -1831.6),
        FONT_SIZE=var_18,
    )
    var_20 = python_code_.JTable()
    var_21 = python_code_.JScrollPane()
    var_22 = python_code_.Task_Manager(
        contactTable=var_20,
        scrollPane=var_21,
        numberOfProcesses=var_6,
        amountofFreeMemory=var_1,
        amountofUsedMemory=var_17,
    )
    var_23 = python_code_.Memory(memory=var_13, table=var_2)
    var_24 = python_code_.Instruction_Exit()
    var_25 = python_code_.Instruction_Out()
    python_code_.Operating_System(
        MEMORY_SIZE=var_4,
        PAGE_SIZE=var_10,
        NUMBER_OF_REGISTERS=var_1,
        INSTRUCTION_REGISTER=var_2,
        PROC_BASE_REGISTER=var_2,
        PROC_LIMIT_REGISTER=var_2,
        PROCESS_ID_REGISTER=-1,
        PROC_BASE_POINTER=var_2,
        PROC_DATA_POINTER=False,
        QUANTUM=var_12,
        clock=var_0,
        cpu=var_13,
        dispatcher=var_4,
        memory=False,
        scheduler=var_14,
        device=var_12,
        hardDrive="LiP7g/(",
        prompt=var_19,
        taskManager=var_22,
        prompt20=[-1937, "Prompt"],
        cPU30=var_1,
        memory34=var_23,
        exit7=var_24,
        calculate11=complex(-1346.930967, 2280.335),
        out13=var_25,
    )


def test_35():
    python_code_.Memory(memory=None, table=None, operating_System35=None)
    var_79 = python_code_.JLabel()
    python_code_.Instruction_Calculate(time=complex(922.7384617, -709.466414))
    python_code_.Task_Manager(
        contactTable=None,
        scrollPane=None,
        numberOfProcesses=var_79,
        amountofFreeMemory=var_79,
        amountofUsedMemory=None,
        process24=var_79,
    )


def test_36():
    python_code_.Instruction_CloseBracket()


@pytest.mark.xfail(strict=True)
def test_37():
    python_code_.Clock(clockCycle=1806, operating_System29=None)
    var_1 = python_code_.Instruction_IO
    var_15 = -1895
    python_code_.IO_Device(counter=var_15, operating_System39=var_15)
    var_17 = python_code_.Hard_Drive(
        memory="request48-_ProcessTableModel__operating_System16"
    )
    var_18 = python_code_.JFrame()
    var_19 = python_code_.Font()
    var_20 = python_code_.JTextArea()
    python_code_.Prompt(
        queuePosition=complex(-3572.6358, 3299.7),
        frame=var_18,
        commandLine=var_18,
        frameFont=var_19,
        output=var_20,
        MAX_COMMAND_LENGTH=var_18,
        OUTPUT_HEIGHT=var_1,
        OUTPUT_WIDTH=var_15,
        FONT_SIZE=set(),
    )
    var_25 = -64
    python_code_.Request(
        startAddress=var_15, endAddress=var_15, processID=var_25, hard_Drive49=var_17
    )


@pytest.mark.xfail(strict=True)
def test_38():
    var_0 = python_code_.Memory(memory=None, table=909, page50="._>mX9>S3GnIp<<1E!@")
    python_code_.ProgramFileData(name=var_0, memory="LQo qxnuU;Y'.", instructions=var_0)
    var_8 = python_code_.ArrayList_ProgramFileData_()
    var_9 = python_code_.Instruction_Out
    python_code_.JobFileData(programs=var_8, startTimes=var_9)
    var_35 = "_Operating_System__hard_Drive40.Instruction_Out._Hard_Drive__operating_System41._Operating_System__task_Manager22"
    var_36 = python_code_.Process
    var_37 = python_code_.Process(
        processState=b"[\x0c\x93xN \xf8\x9fY\x03'D\xde\xb5%\xeb\xa59",
        registers=set(),
        name=var_35,
        memoryUseage=var_36,
    )
    var_38 = True
    python_code_.Page(
        owner=var_37,
        attribute="_ProgramFileData__jobFileData47",
        free=var_38,
        memory51=var_0,
        process42=[],
    )


@pytest.mark.xfail(strict=True)
def test_39():
    var_22 = python_code_.Hard_Drive
    var_23 = "processTableModel17-operating_System2-operating_System29-_ProgramFileData__instruction44"
    var_24 = -244
    var_25 = "Ivnstruction_IO"
    var_26 = python_code_.Instruction_Out()
    var_27 = python_code_.Process(
        processState=var_22,
        registers=var_22,
        name=var_23,
        memoryUseage=var_24,
        processTableModel19=var_26,
        task_Manager25=False,
        page43=var_23,
    )
    assert isinstance(var_27, python_code_.Process)
    python_code_.CPU(registers=var_25, interruptQueue=complex(-2443.825931, -9.65))
    python_code_.Hard_Drive(memory=653)
    python_code_.Page(
        owner=var_27,
        attribute="_Operating_System__calculate11",
        free=True,
        memory51=var_23,
        process42=var_27,
    )


@pytest.mark.xfail(strict=True)
def test_40():
    var_0 = python_code_.Instruction_IO()
    python_code_.Clock(clockCycle=False)
    var_2 = python_code_.Instruction_Instruction_Interface()
    var_3 = python_code_.JLabel()
    var_4 = python_code_.Instruction_Print()
    var_6 = python_code_.Dispatcher()
    var_8 = python_code_.Hard_Drive
    var_9 = False
    python_code_.Page(owner=var_0, attribute=var_8, free=var_9, memory51=-362)
    var_11 = ""
    python_code_.Hard_Drive(memory=var_11, operating_System41=var_4)
    var_57 = "Instruction_Instruction_Interface"
    var_59 = python_code_.Instruction_DecrementValue()
    var_60 = python_code_.JTextField()
    python_code_.IO_Device(counter=1124)
    var_65 = python_code_.Instruction_DecrementValue()
    var_68 = -64
    var_69 = python_code_.Request(
        startAddress=var_68, endAddress=var_68, processID=var_68
    )
    var_71 = "SA4*\nfC"
    var_72 = python_code_.ProgramFileData(
        name=var_71,
        memory=var_68,
        instructions=var_65,
        instruction44=None,
        jobFileData47=var_68,
    )
    assert isinstance(var_72, python_code_.ProgramFileData)
    var_74 = -1
    var_75 = python_code_.JFrame()
    var_76 = python_code_.Font()
    var_77 = python_code_.Prompt(
        queuePosition=var_74,
        frame=var_75,
        commandLine=var_60,
        frameFont=var_76,
        output=-3197,
        MAX_COMMAND_LENGTH=var_8,
        OUTPUT_HEIGHT=set(),
        OUTPUT_WIDTH=var_9,
        FONT_SIZE={-1588.77, False},
    )
    var_78 = -701
    var_79 = 0
    var_80 = -1851
    var_81 = python_code_.CPU(registers=var_57, interruptQueue=var_69)
    var_82 = 1280
    var_83 = python_code_.Process(
        processState=set(),
        registers=var_8,
        name=var_59,
        memoryUseage=var_82,
        processTableModel19=b"\xe2I\rxl\x9b\xa0\xe3\xf7y\xf6\x9f\x7f\xd0\x9aA",
        task_Manager25=-985,
    )
    var_84 = python_code_.Scheduler(
        newQueue=None, readyQueue=var_8, ioQueue=var_83, identifier=var_79
    )
    var_85 = python_code_.JScrollPane()
    var_86 = python_code_.Task_Manager(
        contactTable=True,
        scrollPane=var_85,
        numberOfProcesses=[-761, -2383.71, 3],
        amountofFreeMemory=var_3,
        amountofUsedMemory="Page",
    )
    var_87 = python_code_.Operating_System(
        MEMORY_SIZE=var_8,
        PAGE_SIZE=var_78,
        NUMBER_OF_REGISTERS=[],
        INSTRUCTION_REGISTER=var_74,
        PROC_BASE_REGISTER=var_78,
        PROC_LIMIT_REGISTER=var_8,
        PROCESS_ID_REGISTER=var_79,
        PROC_BASE_POINTER=var_74,
        PROC_DATA_POINTER=complex(-1261.0, -963.9934),
        QUANTUM=var_80,
        clock={True, True},
        cpu=var_81,
        dispatcher=var_6,
        memory=var_77,
        scheduler=var_84,
        device=None,
        hardDrive=var_8,
        prompt="operating_System31",
        taskManager=var_86,
        calculate11=var_2,
        out13=var_6,
    )
    python_code_.Instruction_Calculate(time=var_2, operating_System10=var_87)


def test_41():
    python_code_.Clock(clockCycle=None)
    var_32 = 1
    var_33 = python_code_.Instruction_Instruction_Interface()
    var_34 = "D!-S\\m=/NdALE"
    python_code_.Instruction_Calculate(time=var_32, operating_System10=var_33)
    var_62 = "_Clock__operating_System29"
    var_63 = "k1#}\rNm/}0\n\x0c-3p#c"
    python_code_.ProcessTableModel(
        columnNames=var_62, processList=var_63, numberProcesses=var_32
    )
    python_code_.ProcessData(
        name="nb;G Ft", startTime=var_34, instructions="<\\t+J.A+", memory=var_32
    )
    var_38 = python_code_.JFrame()
    python_code_.IO_Device(counter=var_33)
    var_47 = python_code_.Font()
    var_48 = python_code_.JTextArea()
    var_49 = 1955
    var_50 = 904
    python_code_.Prompt(
        queuePosition=var_34,
        frame=var_38,
        commandLine=var_33,
        frameFont=var_47,
        output=var_48,
        MAX_COMMAND_LENGTH=None,
        OUTPUT_HEIGHT=var_49,
        OUTPUT_WIDTH=var_47,
        FONT_SIZE=var_50,
    )


@pytest.mark.xfail(strict=True)
def test_42():
    var_0 = python_code_.Memory(memory=None, table=909, page50="._>mX9>S3GnIp<<1E!@")
    python_code_.ProgramFileData(name=var_0, memory="LQo qxnuU;Y'.", instructions=var_0)
    var_7 = python_code_.AbstractTableModel()
    var_15 = python_code_.JTextField()
    var_16 = "r,VW!l,rT)VB"
    var_17 = 1218
    python_code_.ProcessData(
        name=var_7, startTime=var_16, instructions=var_15, memory=var_17
    )
    var_21 = -922
    python_code_.Clock(clockCycle=var_21)
    var_30 = python_code_.JFrame()
    var_43 = python_code_.JTable()
    var_44 = python_code_.Instruction_Exit
    var_45 = python_code_.JLabel()
    var_46 = "_Process__iO5"
    var_47 = python_code_.Process(
        processState=None,
        registers=var_16,
        name=var_46,
        memoryUseage=var_17,
        task_Manager25=var_17,
    )
    python_code_.Task_Manager(
        contactTable=var_43,
        scrollPane=var_30,
        numberOfProcesses=var_16,
        amountofFreeMemory=var_44,
        amountofUsedMemory=var_45,
        process24=var_47,
    )


@pytest.mark.xfail(strict=True)
def test_43():
    var_0 = python_code_.Memory(memory=None, table=None, operating_System35=None)
    var_2 = python_code_.ProgramFileData(
        name=var_0, memory="LQo qxnuU;Y'.", instructions=var_0
    )
    var_3 = "U'#sYE1\x0cB@Tq"
    var_4 = python_code_.Hard_Drive(memory=var_3, request48=var_2)
    var_87 = -64
    python_code_.Request(
        startAddress=var_87, endAddress=var_87, processID=var_87, hard_Drive49=var_4
    )


def test_44():
    var_0 = lambda *args, **kwargs: 3
    var_2 = python_code_.AbstractTableModel()
    python_code_.Request(
        startAddress=-2571, endAddress=1529, processID=1965, hard_Drive49=var_2
    )
    var_7 = python_code_.JTextField()
    python_code_.Page(
        owner=[],
        attribute=b"\xadQ<\x02\xb3\xf7,\x0f\xcd\xa9\xa3",
        free=var_0,
        process42="Instruction_IO._ProcessData__instruction15.operating_System23",
    )
    python_code_.IO_Device(counter=1124)
    var_25 = -52
    python_code_.CPU(
        registers=["operating_System21", 1285.62, -4714], interruptQueue={"QCB[n-"}
    )
    python_code_.Memory(memory=var_7, table=var_25)


@pytest.mark.xfail(strict=True)
def test_45():
    var_0 = -1712
    var_1 = bool
    var_2 = -611
    var_3 = 2
    var_4 = python_code_.Dispatcher()
    var_5 = python_code_.Memory(
        memory=None, table=complex(1172.0, -1806.6970463), operating_System35=var_1
    )
    var_6 = python_code_.IO_Device(counter=var_2)
    var_7 = python_code_.JFrame()
    var_8 = python_code_.Font()
    var_9 = 0
    var_10 = -1307
    var_11 = python_code_.Prompt(
        queuePosition=var_1,
        frame=var_7,
        commandLine=(),
        frameFont=var_8,
        output=var_1,
        MAX_COMMAND_LENGTH=var_9,
        OUTPUT_HEIGHT=(),
        OUTPUT_WIDTH=[-1129.1, False, "6[ls=cD!abykw6_2"],
        FONT_SIZE=var_10,
    )
    var_12 = python_code_.CPU(registers=var_5, interruptQueue=var_2)
    var_13 = python_code_.Process(
        processState=var_1,
        registers=-109.13,
        name=var_12,
        memoryUseage=var_1,
        task_Manager25={},
        page43=var_7,
    )
    var_14 = python_code_.Scheduler(
        newQueue=var_10, readyQueue=set(), ioQueue=var_13, identifier=var_6
    )
    python_code_.Operating_System(
        MEMORY_SIZE=var_0,
        PAGE_SIZE=var_0,
        NUMBER_OF_REGISTERS={},
        INSTRUCTION_REGISTER=complex(-641.8930758, 639.3456279),
        PROC_BASE_REGISTER="*/jxG(h|n$8()#!Yr3",
        PROC_LIMIT_REGISTER=var_1,
        PROCESS_ID_REGISTER=var_2,
        PROC_BASE_POINTER=var_3,
        PROC_DATA_POINTER=var_3,
        QUANTUM=var_2,
        clock=var_2,
        cpu=var_0,
        dispatcher=var_4,
        memory=var_5,
        scheduler=(True, "X3bN\n%`\x0bg&3 h7L%pK"),
        device=var_6,
        hardDrive=complex(-3798.0, -4098.0),
        prompt=var_11,
        taskManager=b"a\x8a]\xaf\x00\x94\n*f8'\xb1",
        task_Manager22=var_4,
        cPU30=var_12,
        iO3=var_3,
        exit7=var_10,
        calculate11=var_1,
        scheduler36=var_14,
    )


@pytest.mark.xfail(strict=True)
def test_46():
    var_22 = python_code_.Hard_Drive
    var_47 = python_code_.Instruction_CloseBracket()
    var_48 = "QNd[N"
    var_49 = ",yLI%}.&S/VG.)i&"
    var_50 = python_code_.ProcessData(
        name=var_48, startTime=var_49, instructions=None, memory=True
    )
    var_51 = 184
    var_52 = python_code_.Instruction_Exit()
    var_53 = python_code_.Process(
        processState=set(),
        registers=b"d\x12,\xd1o\xc8h\xb2\xba",
        name=var_51,
        memoryUseage=var_51,
        processTableModel19=var_22,
        exit9=var_52,
    )
    var_55 = 537
    python_code_.Memory(
        memory=None, table=None, page50=var_22, operating_System35=var_47
    )
    var_61 = 801
    python_code_.Scheduler(
        newQueue=var_50,
        readyQueue={},
        ioQueue=var_53,
        identifier=var_61,
        operating_System37=var_22,
    )
    var_63 = 0
    var_64 = python_code_.Request(
        startAddress=var_63, endAddress=var_63, processID=var_55
    )
    python_code_.Hard_Drive(memory=var_50, request48=var_64)


def test_47():
    python_code_.Clock(clockCycle=set(), operating_System29="DG5(kLX(N~O'O")
    var_1 = python_code_.Instruction_IO
    var_2 = -3801
    python_code_.ProcessData(
        name={-2576.8, "S!dr<", True},
        startTime={-107.65},
        instructions=var_1,
        memory=var_2,
    )
    var_12 = python_code_.Font()
    var_34 = python_code_.JTable()
    var_35 = python_code_.JLabel()
    var_21 = python_code_.Task_Manager(
        contactTable=var_34,
        scrollPane={},
        numberOfProcesses=var_12,
        amountofFreeMemory=var_35,
        amountofUsedMemory=var_35,
        operating_System23=var_2,
        process24=-135.56,
    )
    var_22 = python_code_.JFrame()
    var_23 = python_code_.Font()
    var_24 = python_code_.JTextArea()
    python_code_.Prompt(
        queuePosition=complex(-3572.6358, 3299.7),
        frame=var_22,
        commandLine=var_22,
        frameFont=var_23,
        output=var_24,
        MAX_COMMAND_LENGTH=var_22,
        OUTPUT_HEIGHT=var_1,
        OUTPUT_WIDTH=var_2,
        FONT_SIZE=set(),
    )
    var_29 = -81
    python_code_.Request(
        startAddress=var_2, endAddress=var_2, processID=var_29, hard_Drive49=var_21
    )
    python_code_.ProcessTableModel(
        columnNames=var_1, processList=[], numberProcesses=var_2
    )


@pytest.mark.xfail(strict=True)
def test_48():
    var_1 = hash
    var_2 = "RM##!Q"
    var_3 = python_code_.Instruction_Instruction_Interface()
    var_4 = python_code_.ProgramFileData(
        name=var_2,
        memory=b"+\xf1\xc2\xcbm\xaf\xcb\x88\xed\xbb\xd2\xcfd\x8f\xf6\xcd5Op",
        instructions=var_1,
        instruction44=var_3,
    )
    python_code_.JobFileData(
        programs=b"_Y\xab\xbeO\x11\x9atl\xb9\x8d\xb7\xaf\xc8\x97b",
        startTimes=var_1,
        programFileData46=var_4,
    )
