# Import sqrt for calculating distance between points
from math import sqrt

# PART 1: COUNTER CLASS
class Counter:
    def __init__(self):
        """Initialize the counter with value = 0"""
        self.value = 0

    def incr(self):
        """Increment value by 1"""
        self.value += 1

    def decr(self):
        """Decrement value by 1"""
        self.value -= 1

    def incrby(self, n):
        """Increment value by n (any integer)"""
        self.value += n

    def decrby(self, n):
        """Decrement value by n"""
        self.value -= n


class Triangle:
    def __init__(self):
        """Create a new triangle with an empty list of points"""
        self.points = []

    def add_point(self, x, y):
        """Add a point (x, y) to the triangle"""
        self.points.append((x, y))

    def _distance(self, p1, p2):
        """Private helper: calculate Euclidean distance between two points"""
        dx = p1[0] - p2[0] # difference in x-coordinates
        dy = p1[1] - p2[1] # difference in y-coordinates
        return sqrt(dx**2 + dy**2)  # Pythagoras theorem

    def perimeter(self):
        """Calculate and return the perimeter of the triangle"""
        if len(self.points) != 3:
            return 0 # Not a valid triangle
        
        # Calculate all three sides
        a = self._distance(self.points[0], self.points[1])
        b = self._distance(self.points[1], self.points[2])
        c = self._distance(self.points[2], self.points[0])
        return a + b + c

    # === OLD VERSION (commented out) ===
    # def is_equal(self, other):
    #     return sorted(self.points) == sorted(other.points)

    # === NEW VERSION: RENAMED TO __eq__ (LATEST) ===
    def __eq__(self, other):
        return sorted(self.points) == sorted(other.points)


if __name__ == "__main__":
    print("=== COUNTER DEMO ===")
    c = Counter()
    c.incr()
    c.incrby(3)
    c.decr()
    c.decrby(2)
    print("Final value:", c.value)  # → 2

    print("\n=== TRIANGLE DEMO ===")
 
 # --- Triangle t1: (0,0), (0,3), (4,0)
    t1 = Triangle()
    t1.add_point(0, 0)
    t1.add_point(0, 3)
    t1.add_point(4, 0)
    print("t1 perimeter:", round(t1.perimeter(), 2))

# --- Triangle t2: (1,2), (2,1), (1,5) ---
    t2 = Triangle()
    t2.add_point(1, 2)
    t2.add_point(2, 1)
    t2.add_point(1, 5)
    print("t2 perimeter:", round(t2.perimeter(), 2))

# Compare t1 and t2 (different points)
    print("t1 == t2?", t1 == t2)


# --- Triangle t3: same points as t2 -
    t3 = Triangle()
    t3.add_point(1, 2)
    t3.add_point(2, 1)
    t3.add_point(1, 5)

    # === OLD OPERATIONS (commented) ===
    # print("t1 == t3?", t1 == t3)
    # print("t1.is_equal(t3):", t1.is_equal(t3))
    # print("t3.is_equal(t1):", t3.is_equal(t1))

    # === NEW OPERATION: Using __eq__ ===
    print("t1 == t3?", t1 == t3)  # → False