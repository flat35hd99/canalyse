import os
import unittest
from canalyse.parser import ConductivityParser
from canalyse.validator import ConductivityValidator


class TestValidator(unittest.TestCase):
    def setUp(self) -> None:
        conductivity_file = (
            f"{os.path.dirname(os.path.abspath(__file__))}/assets/conductivity.dot"
        )
        parser = ConductivityParser()
        self.df = parser.run(conductivity_file)
        return super().setUp()

    def test_deviation(self):
        validator = ConductivityValidator(self.df)

        result = validator.deviation_is_less_than(0.005)
        assert result

        result = validator.deviation_is_more_than(0.004)
        assert result

    def test_average(self):
        validator = ConductivityValidator(self.df)

        result = validator.average_is_less_than(0.02)
        assert result

        result = validator.average_is_more_than(0.01)
        assert result
