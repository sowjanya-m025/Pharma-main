import os
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ToolTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.chdir(ROOT)

    def test_clinical_trials_filter_by_molecule(self):
        from tools.mock_clinical_tool import get_clinical_trials
        trials = get_clinical_trials("paracetamol")
        self.assertEqual(len(trials), 1)
        self.assertEqual(trials[0]["phase"], "Phase 3")
        self.assertEqual(get_clinical_trials("unknown-molecule"), [])

    def test_patents_filter_by_molecule(self):
        from tools.mock_patent_tool import get_patents
        patents = get_patents("Amoxicillin")
        self.assertEqual(patents[0]["patent_number"], "US9876543B2")

    def test_trade_data_splits_exports_and_imports(self):
        from tools.mock_exim_tool import get_trade_data
        self.assertEqual(len(get_trade_data("Paracetamol")["exports"]), 1)
        self.assertEqual(len(get_trade_data("Ibuprofen")["imports"]), 1)
        self.assertEqual(get_trade_data("Paracetamol")["imports"], [])

    def test_market_data_all_and_filtered(self):
        from tools.mock_iqvia_tool import get_market_data
        self.assertEqual(len(get_market_data()), 2)
        self.assertEqual(get_market_data("cardiology")[0]["CAGR"], "3.8%")

    def test_data_loader_works_from_any_directory(self):
        from utils.data_loader import load_json
        with tempfile.TemporaryDirectory() as other:
            old = os.getcwd()
            os.chdir(other)
            try:
                self.assertIn("patents", load_json("mock_patent_data.json"))
            finally:
                os.chdir(old)

    def test_report_generator_handles_awkward_input(self):
        from utils.report_generator import create_pdf_report
        with tempfile.TemporaryDirectory() as tmp:
            old = os.getcwd()
            os.chdir(tmp)
            try:
                path = create_pdf_report("Ibuprofen/Aspirin?\n" + "x" * 300,
                                         "model said a < b & <unclosed")
                self.assertTrue(os.path.exists(path))
                self.assertGreater(os.path.getsize(path), 500)
                self.assertTrue(path.startswith("reports/"))
                self.assertNotIn("\n", path)
            finally:
                os.chdir(old)


if __name__ == "__main__":
    unittest.main()
