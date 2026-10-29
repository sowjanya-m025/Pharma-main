"""Mock IQVIA-style market data lookup (reads data/mock_market_data.json)."""
from utils.data_loader import load_json


def get_market_data(therapy_area=None):
    """Return market data for one therapy area, or all areas when ``None``."""
    areas = load_json("mock_market_data.json")["therapy_areas"]
    if therapy_area is None:
        return areas
    return [a for a in areas if a["name"].lower() == therapy_area.strip().lower()]
