import os
import unittest
from canalyse.parser import ConductivityParser
from canalyse.validator import ConductivityValidator


class TestValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.conductivity_file = (
            f"{os.path.dirname(os.path.abspath(__file__))}/assets/conductivity.dot"
        )
        return super().setUp()

    def test_deviation(self):
        parser = ConductivityParser()
        df = parser.run(self.conductivity_file)
        validator = ConductivityValidator(df)

        result = validator.deviation_is_less_than(0.005)
        assert result

        result = validator.deviation_is_more_than(0.004)
        assert result
