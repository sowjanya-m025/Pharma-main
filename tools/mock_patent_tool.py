"""Mock patent database lookup (reads data/mock_patent_data.json)."""
from utils.data_loader import load_json


def get_patents(molecule):
    """Return all patents whose molecule matches ``molecule`` (case-insensitive)."""
    patents = load_json("mock_patent_data.json")["patents"]
    return [p for p in patents if p["molecule"].lower() == molecule.strip().lower()]
