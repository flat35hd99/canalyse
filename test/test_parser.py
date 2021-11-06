import unittest
import os

# from canalyse.parser import ConductivityParser as conpas
from canalyse.parser import conductivity_parser


class TestParser(unittest.TestCase):
    def test_conductivity_parser(self):
        parser = conductivity_parser()
        reference_file = (
            f"{os.path.dirname(os.path.abspath(__file__))}/assets/conductivity.dot"
        )
        df = parser().run(reference_file)
        # Has header expected
        reference_header = ["source", "target", "conductivity"]
        assert all(df.columns == reference_header)
