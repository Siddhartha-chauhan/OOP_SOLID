# src/weather.py
from calculator import Calculator
from data_extractor import DataExtractor
from data_analyzer import DataAnalyzer

# Named column indices
DAY = 0
MAX_TEMP = 1
MIN_TEMP = 2

def skip_line(line: str) -> bool:
    return line.startswith('#') or line.startswith('dy') or not line[0].isdigit()

def parse_line(record: dict) -> dict:
    return record

# Build components
extractor = DataExtractor(skip_line, parse_line)
analyzer = DataAnalyzer('day', 'max_temp', 'min_temp')
calc = Calculator(extractor, analyzer)

# Path from src/ → ../data/weather.dat
day, spread = calc.run('data/weather.dat', {
    'day': DAY,
    'max_temp': MAX_TEMP,
    'min_temp': MIN_TEMP
})

print(f"Weather: Day {day} has smallest spread: {spread}")