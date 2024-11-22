PyTrig is a custom Python module offering a wide range of trigonometric, logarithmic, and general mathematical functions.
Designed for precision and flexibility, PyTrig is perfect for advanced mathematical computations.

Available Functions
Constants
PyTrig provides the following mathematical constants:

mat.pi: Value of π (3.141592653589793)
mat.e: Value of e (2.718281828459045)
mat.phi: Value of the golden ratio (1.618033988749895)
General Math Functions
pytrig.root(x, y)
Returns the yth root of x.
Example: pytrig.root(27, 3) → 3.0

pytrig.log(base, x)
Returns the logarithm of x with base base.
Example: pytrig.log(2, 8) → 3.0

pytrig.factorial(n)
Returns n!
Example: pytrig.factorial(5) → 120

pytrig.gcd(a, b)
Computes the greatest common divisor (GCD) of a and b.
Example: pytrig.gcd(12, 18) → 6

pytrig.lcm(a, b)
Computes the least common multiple (LCM) of a and b.
Example: pytrig.lcm(4, 6) → 12

pytrig.ceil(x)
Returns the ceiling of x.
Example: pytrig.ceil(4.2) → 5

pytrig.floor(x)
Returns the floor of x.
Example: pytrig.floor(4.8) → 4

pytrig.exp(a, terms)
Approximates e^a using a Taylor series with the given number of terms.
Example: pytrig.exp(1, 10) → 2.71828...

pytrig.dist(x, y, x1, y1)
Returns the Euclidean distance between two points (x, y) and (x1, y1).
Example: pytrig.dist(0, 0, 3, 4) → 5.0

Trigonometric Functions
pytrig.to_radians(degrees)
Converts degrees to radians.
Example: pytrig.to_radians(180) → 3.14159...

pytrig.normalize_angle(x)
Normalizes an angle (in radians) to the range [0, 2π).
Example: pytrig.normalize_angle(7) → 0.71681...

pytrig.sin(x, terms)
Computes the sine of x (in radians) using a Taylor series.
Example: pytrig.sin(3.14159 / 2, 10) → 1.0

pytrig.cos(x, terms)
Computes the cosine of x (in radians) using a Taylor series.
Example: pytrig.cos(3.14159, 10) → -1.0

pytrig.tan(x, terms)
Computes the tangent of x (in radians) as sin(x) / cos(x).
Example: pytrig.tan(3.14159 / 4, 10) → 1.0

Hyperbolic Functions
pytrig.sinh(x, terms)
Computes the hyperbolic sine of x.
Example: pytrig.sinh(1, 10) → 1.1752...

pytrig.cosh(x, terms)
Computes the hyperbolic cosine of x.
Example: pytrig.cosh(1, 10) → 1.5430...

pytrig.tanh(x, terms)
Computes the hyperbolic tangent of x.
Example: pytrig.tanh(1, 10) → 0.76159...

Inverse Trigonometric Functions
pytrig.arcsin(x, terms)
Computes the arcsine of x (for -1 ≤ x ≤ 1) using a series expansion.
Example: pytrig.arcsin(0.5, 10) → 0.523598...

pytrig.arccos(x, terms)
Computes the arccosine of x (for -1 ≤ x ≤ 1).
Example: pytrig.arccos(0.5, 10) → 1.047197...

pytrig.arctan(x, terms)
Computes the arctangent of x.
Example: pytrig.arctan(1, 10) → 0.785398...

Inverse Hyperbolic Functions
pytrig.arsinh(x)
Computes the inverse hyperbolic sine of x.
Example: pytrig.arsinh(1) → 0.88137...

pytrig.arcosh(x)
Computes the inverse hyperbolic cosine of x (for x ≥ 1).
Example: pytrig.arcosh(1) → 0.0

pytrig.artanh(x)
Computes the inverse hyperbolic tangent of x (for -1 < x < 1).
Example: pytrig.artanh(0.5) → 0.549306...

Logarithmic Functions
pytrig.ln(x, terms)
Computes the natural logarithm of x using a series expansion.
Example: pytrig.ln(2, 50) → 0.693147...
