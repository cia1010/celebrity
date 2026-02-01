import re
from dateutil import parser as dateparser

class DataCleaner:
    @staticmethod
    def clean_net_worth(value_str):
        if not value_str:
            return None
        value_str = value_str.replace('$', '').replace(',', '').strip()
        if 'B' in value_str:
            return float(value_str.replace('B', '')) * 1e9
        if 'M' in value_str:
            return float(value_str.replace('M', '')) * 1e6
        try:
            return float(value_str)
        except Exception:
            return None

    @staticmethod
    def clean_date(date_str):
        try:
            return dateparser.parse(date_str).date()
        except Exception:
            return None
