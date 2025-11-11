# src/data_extractor.py
from typing import List, Dict, Callable

class DataExtractor:
    def __init__(self,
                 skip_line: Callable[[str], bool],
                 parse_line: Callable[[Dict], Dict]):
        self.skip_line = skip_line
        self.parse_line = parse_line

    def extract(self, file_path: str, columns: Dict[str, int]) -> List[Dict]:
        print(f"\n[EXTRACTOR] Reading: {file_path}")
        records = []
        try:
            with open(file_path, encoding="utf-8") as f:
                for i, line in enumerate(f, 1):
                    line = line.strip()
                    if not line or self.skip_line(line):
                        continue
                    parts = line.split()
                    if len(parts) <= max(columns.values()):
                        continue
                    record = {k: parts[v] for k, v in columns.items()}
                    record = self.parse_line(record)
                    records.append(record)
                    if i <= 3:
                        print(f"  Record {i}: {record}")
            print(f"[EXTRACTOR] Done → {len(records)} records\n")
            return records
        except FileNotFoundError:
            print(f"[ERROR] NOT FOUND: {file_path}")
            raise