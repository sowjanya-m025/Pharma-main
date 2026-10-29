"""Mock export/import lookup (reads data/mock_exim_data.json)."""
from utils.data_loader import load_json


def get_trade_data(molecule):
    """Return ``{"exports": [...], "imports": [...]}`` entries for a molecule."""
    data = load_json("mock_exim_data.json")
    name = molecule.strip().lower()
    return {
        "exports": [e for e in data["API_Exports"] if e["molecule"].lower() == name],
        "imports": [i for i in data["API_Imports"] if i["molecule"].lower() == name],
    }
