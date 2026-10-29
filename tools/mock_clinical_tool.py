"""Mock clinical-trial registry lookup (reads data/mock_clinical_data.json)."""
from utils.data_loader import load_json


def get_clinical_trials(molecule):
    """Return all trials whose molecule matches ``molecule`` (case-insensitive)."""
    trials = load_json("mock_clinical_data.json")["clinical_trials"]
    return [t for t in trials if t["molecule"].lower() == molecule.strip().lower()]
