# spike.py - Quick prototype (no OOP)
def find_min_diff(file_path, is_weather=True):
    min_diff = float('inf')
    result = None
    with open(file_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or line[0].isalpha():
                continue
            parts = line.split()
            if len(parts) < 9:
                continue
            if is_weather:
                day = parts[0]
                max_t = int(parts[1].rstrip('*'))
                min_t = int(parts[2].rstrip('*'))
                diff = abs(max_t - min_t)
                key = day
            else:
                team = parts[1]
                f_goals = int(parts[6])
                a_goals = int(parts[8])
                diff = abs(f_goals - a_goals)
                key = team
            if diff < min_diff:
                min_diff = diff
                result = key
    return result, min_diff

# Run spike
print("Spike Results:")
print("Weather:", find_min_diff('data/weather.dat', True))
print("Football:", find_min_diff('data/football.dat', False))