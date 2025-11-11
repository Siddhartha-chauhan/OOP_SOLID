## OOP and SOLID

### 1. OOP Tasks

**Counter Class**  
A stateful object with an integer `value` initialized to `0`. Implements incremental/decremental operations:
- `incr()` → `value += 1`
- `decr()` → `value -= 1`
- `incrby(n)` → `value += n`
- `decrby(n)` → `value -= n`

**Triangle Class**  
Manages a list of 2D points. Key methods:
- `add_point(x, y)` → appends `(x, y)` to internal list
- `perimeter()` → computes total length of triangle sides using Euclidean distance
- `__eq__(other)` → compares two triangles by point set (order-independent equality)

---

### 2. SOLID – Data Munging (Kata04)

**Objective**:  
Parse `weather.dat` and `football.dat` to find:
- Day with smallest temperature spread (`Max - Min`)
- Team with smallest goal difference (`F - A`)

**Development Flow**:
1. **Spike** → Rapid prototype (`spike.py`) to confirm logic and data format
2. **Refactor** → 5 modular classes adhering to SOLID

**Classes & Responsibilities**:
| Class | Role |
|------|------|
| `DataExtractor` | Reads file, skips headers, extracts columns |
| `DataAnalyzer`  | Computes absolute difference, finds minimum |
| `Calculator`    | Orchestrates extraction → analysis |

**SOLID Compliance**:
- **SRP**: Each class has one job
- **OCP**: New datasets via configuration
- **DIP**: `Calculator` depends on abstractions
- **ISP**: Minimal, focused methods
- **No Magic Numbers**: Column indices named (e.g., `DAY = 0`, `GOALS_FOR = 6`)

**Outcome**: Clean, testable, extensible code from a validated spike.

