# src/calculator.py
class Calculator:
    """Orchestrates Extractor + Analyzer (DIP)."""
    def __init__(self, extractor, analyzer):
        self.extractor = extractor
        self.analyzer = analyzer

    def run(self, file_path: str, columns: dict) -> tuple:
        records = self.extractor.extract(file_path, columns)
        return self.analyzer.analyze(records)