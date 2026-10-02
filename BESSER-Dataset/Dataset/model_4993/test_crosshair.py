from enum import Enum
from python_code import BoundTypeEnum
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(BoundTypeEnum.MustExceed, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(BoundTypeEnum.MustExceed, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(BoundTypeEnum.MustExceed, '', 0, '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(BoundTypeEnum.MustExceed, 0)

def test_Enum___new___2():
    assert Enum.__new__(BoundTypeEnum.MustExceed, 'MustExceed') == BoundTypeEnum.MustExceed

from enum import Enum
from python_code import CalculationTypeEnum
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(CalculationTypeEnum.Python, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(CalculationTypeEnum.Python, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(CalculationTypeEnum.Python, '', '', 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(CalculationTypeEnum.Python, 0)

def test_Enum___new___2():
    assert Enum.__new__(CalculationTypeEnum.Python, 'Python') == CalculationTypeEnum.Python

from enum import Enum
from python_code import CustomGeometryInputOperationEnum
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(CustomGeometryInputOperationEnum.Union, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(CustomGeometryInputOperationEnum.Union, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(CustomGeometryInputOperationEnum.Union, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(CustomGeometryInputOperationEnum.Union, 0)

def test_Enum___new___2():
    assert Enum.__new__(CustomGeometryInputOperationEnum.Union, 'Union') == CustomGeometryInputOperationEnum.Union

from enum import Enum
from python_code import DataTypeEnum
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(DataTypeEnum.Integer, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(DataTypeEnum.Real, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(DataTypeEnum.Real, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(DataTypeEnum.Real, 0)

def test_Enum___new___2():
    assert Enum.__new__(DataTypeEnum.Real, 'Real') == DataTypeEnum.Real

from enum import Enum
from python_code import DimensionTypeEnum
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(DimensionTypeEnum.Matrix, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(DimensionTypeEnum.Vector, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(DimensionTypeEnum.Vector, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(DimensionTypeEnum.Matrix, 0)

def test_Enum___new___2():
    assert Enum.__new__(DimensionTypeEnum.Matrix, 'Matrix') == DimensionTypeEnum.Matrix

from enum import Enum
from python_code import DirectionalityEnum
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(DirectionalityEnum.out, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(DirectionalityEnum.out, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(DirectionalityEnum.out, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(DirectionalityEnum.in_, 0)

def test_Enum___new___2():
    assert Enum.__new__(DirectionalityEnum.out, 'out') == DirectionalityEnum.out

from enum import Enum
from python_code import DoDDistributionStatementEnum
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(DoDDistributionStatementEnum.StatementE, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(DoDDistributionStatementEnum.StatementB, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(DoDDistributionStatementEnum.StatementB, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(DoDDistributionStatementEnum.StatementE, 0)

def test_Enum___new___2():
    assert Enum.__new__(DoDDistributionStatementEnum.StatementC, 'StatementA') == DoDDistributionStatementEnum.StatementA

from enum import Enum
from python_code import FileFormat
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(FileFormat.AP_214, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(FileFormat.STL, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(FileFormat.STL, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(FileFormat.STL, 0)

def test_Enum___new___2():
    assert Enum.__new__(FileFormat.STL, 'STL') == FileFormat.STL

from enum import Enum
from python_code import FunctionEnum
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(FunctionEnum.clock, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(FunctionEnum.clock, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(FunctionEnum.clock, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(FunctionEnum.clock, 0)

def test_Enum___new___2():
    assert Enum.__new__(FunctionEnum.clock, 'clock') == FunctionEnum.clock

from enum import Enum
from python_code import GeometryQualifierEnum
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(GeometryQualifierEnum.BoundaryOnly, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(GeometryQualifierEnum.BoundaryOnly, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(GeometryQualifierEnum.BoundaryOnly, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(GeometryQualifierEnum.BoundaryOnly, 0)

def test_Enum___new___2():
    assert Enum.__new__(GeometryQualifierEnum.BoundaryOnly, 'BoundaryOnly') == GeometryQualifierEnum.BoundaryOnly

from enum import Enum
from python_code import GlobalConstraintTypeEnum
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(GlobalConstraintTypeEnum.BoardEdgeSpacing, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(GlobalConstraintTypeEnum.BoardEdgeSpacing, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(GlobalConstraintTypeEnum.BoardEdgeSpacing, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(GlobalConstraintTypeEnum.BoardEdgeSpacing, 0)

def test_Enum___new___2():
    assert Enum.__new__(GlobalConstraintTypeEnum.BoardEdgeSpacing, 'BoardEdgeSpacing') == GlobalConstraintTypeEnum.BoardEdgeSpacing

from enum import Enum
from python_code import IntervalMethod
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(IntervalMethod.IntervalLength, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(IntervalMethod.IntervalLength, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(IntervalMethod.IntervalLength, '', '', 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(IntervalMethod.IntervalLength, 0)

def test_Enum___new___2():
    assert Enum.__new__(IntervalMethod.IntervalLength, 'IntervalLength') == IntervalMethod.IntervalLength

from enum import Enum
from python_code import JobManagerToolSelection
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(JobManagerToolSelection.Dymola_2014, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(JobManagerToolSelection.Dymola_2014, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(JobManagerToolSelection.Dymola_2014, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(JobManagerToolSelection.Dymola_2013, 0)

def test_Enum___new___2():
    assert Enum.__new__(JobManagerToolSelection.Dymola_2013, 'Dymola_2013') == JobManagerToolSelection.Dymola_2013

from enum import Enum
from python_code import LayerEnum
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(LayerEnum.Top, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(LayerEnum.Top, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(LayerEnum.Top, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(LayerEnum.Top, 0)

def test_Enum___new___2():
    assert Enum.__new__(LayerEnum.Top, 'Top') == LayerEnum.Top

from enum import Enum
from python_code import LayerRangeEnum
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(LayerRangeEnum.Bottom, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(LayerRangeEnum.Either, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(LayerRangeEnum.Either, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(LayerRangeEnum.Top, 0)

def test_Enum___new___2():
    assert Enum.__new__(LayerRangeEnum.Top, 'Top') == LayerRangeEnum.Top

from enum import Enum
from python_code import ModelType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ModelType.ESMoL, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ModelType.ESMoL, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ModelType.ESMoL, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ModelType.ESMoL, 0)

def test_Enum___new___2():
    assert Enum.__new__(ModelType.ESMoL, 'ESMoL') == ModelType.ESMoL

from enum import Enum
from python_code import PartIntersectionEnum
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(PartIntersectionEnum.None_, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PartIntersectionEnum.None_, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PartIntersectionEnum.None_, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PartIntersectionEnum.None_, 0)

def test_Enum___new___2():
    assert Enum.__new__(PartIntersectionEnum.None_, 'None_') == PartIntersectionEnum.None_

from enum import Enum
from python_code import PortDirectionality
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(PortDirectionality.out, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PortDirectionality.out, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PortDirectionality.in_, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PortDirectionality.out, 0)

def test_Enum___new___2():
    assert Enum.__new__(PortDirectionality.out, 'out') == PortDirectionality.out

from enum import Enum
from python_code import RangeConstraintTypeEnum
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(RangeConstraintTypeEnum.Exclusion, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(RangeConstraintTypeEnum.Exclusion, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(RangeConstraintTypeEnum.Inclusion, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(RangeConstraintTypeEnum.Exclusion, 0)

def test_Enum___new___2():
    assert Enum.__new__(RangeConstraintTypeEnum.Exclusion, 'Exclusion') == RangeConstraintTypeEnum.Exclusion

from enum import Enum
from python_code import RedeclareTypeEnum
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(RedeclareTypeEnum.Class, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(RedeclareTypeEnum.Class, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(RedeclareTypeEnum.Class, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(RedeclareTypeEnum.Class, 0)

def test_Enum___new___2():
    assert Enum.__new__(RedeclareTypeEnum.Class, 'Class') == RedeclareTypeEnum.Class

from enum import Enum
from python_code import RelativeLayerEnum
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(RelativeLayerEnum.Same, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(RelativeLayerEnum.Same, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(RelativeLayerEnum.Same, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(RelativeLayerEnum.Same, 0)

def test_Enum___new___2():
    assert Enum.__new__(RelativeLayerEnum.Same, 'Same') == RelativeLayerEnum.Same

from enum import Enum
from python_code import RelativeRotationEnum
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(RelativeRotationEnum.r0, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(RelativeRotationEnum.r90, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(RelativeRotationEnum.r90, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(RelativeRotationEnum.r0, 0)

def test_Enum___new___2():
    assert Enum.__new__(RelativeRotationEnum.r0, 'r0') == RelativeRotationEnum.r0

from enum import Enum
from python_code import RotationEnum
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(RotationEnum.r90, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(RotationEnum.r0, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(RotationEnum.r90, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(RotationEnum.r0, 0)

def test_Enum___new___2():
    assert Enum.__new__(RotationEnum.r0, 'r0') == RotationEnum.r0

from enum import Enum
from python_code import SimpleFormulaOperation
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(SimpleFormulaOperation.Addition, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(SimpleFormulaOperation.Minimum, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(SimpleFormulaOperation.Minimum, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(SimpleFormulaOperation.Minimum, 0)

def test_Enum___new___2():
    assert Enum.__new__(SimpleFormulaOperation.Minimum, 'Maximum') == SimpleFormulaOperation.Maximum

from enum import Enum
from python_code import SystemCDataTypeEnum
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(SystemCDataTypeEnum.bool, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(SystemCDataTypeEnum.bool, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(SystemCDataTypeEnum.bool, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(SystemCDataTypeEnum.bool, 0)

def test_Enum___new___2():
    assert Enum.__new__(SystemCDataTypeEnum.bool, 'bool') == SystemCDataTypeEnum.bool

from python_code import avm_CalculatedValue

def test_avm_CalculatedValue___init__():
    assert avm_CalculatedValue.__init__(avm_CalculatedValue('', '\x00'), '\x00\x00', '') == None

from python_code import avm_ComplexFormula

def test_avm_ComplexFormula___init__():
    assert avm_ComplexFormula.__init__(avm_ComplexFormula('', avm_ComplexFormula=set()), '', avm_ComplexFormula=set()) == None

from python_code import avm_Component

def test_avm_Component___init__():
    assert avm_Component.__init__(avm_Component('', '', '', '', '', '', avm_Component=set(), avm_Component2=set(), avm_Component4=set(), avm_Component6=set(), avm_Component8=set(), avm_Component10=set(), avm_Component12=set(), avm_Component14=set(), avm_Component16=set()), '', '', '', '', '', '', avm_Component=set(), avm_Component2=set(), avm_Component4=set(), avm_Component6=set(), avm_Component8=set(), avm_Component10=set(), avm_Component12=set(), avm_Component14=set(), avm_Component16=set()) == None
