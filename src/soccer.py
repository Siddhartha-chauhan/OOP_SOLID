# soccer.py
from calculator import Calculator
from data_extractor import DataExtractor
from data_analyzer import DataAnalyzer

# Named column indices
TEAM = 1
GOALS_FOR = 6
GOALS_AGAINST = 8

def skip_line(line: str) -> bool:
    return line.startswith('#') or line.startswith('Team') or not line[0].isdigit()

def parse_line(record: dict) -> dict:
    return record

# Build components
extractor = DataExtractor(skip_line, parse_line)
analyzer = DataAnalyzer('team', 'for', 'against')
calc = Calculator(extractor, analyzer)

# Run
team, diff = calc.run('data/football.dat', {
    'team': TEAM,
    'for': GOALS_FOR,
    'against': GOALS_AGAINST
})

print(f"Soccer: Team '{team}' has smallest F-A diff: {diff}")