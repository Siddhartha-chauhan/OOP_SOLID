# src/data_analyzer.py
from typing import Tuple, List, Dict

class DataAnalyzer:
    """Only calculates the minimum difference."""
    def __init__(self,
                 key_field: str,
                 val1_field: str,
                 val2_field: str):
        self.key_field = key_field
        self.val1_field = val1_field
        self.val2_field = val2_field

    def analyze(self, records: List[Dict]) -> Tuple[str, int]:
        min_diff = float('inf')
        result_key = None
        for rec in records:
            v1 = int(rec[self.val1_field].rstrip('*'))
            v2 = int(rec[self.val2_field].rstrip('*'))
            diff = abs(v1 - v2)
            if diff < min_diff:
                min_diff = diff
                result_key = rec[self.key_field]
        return result_key, min_diff