"""High-precision calculation of pi using the Chudnovsky series."""

from decimal import Decimal, localcontext


def calculate_pi(digits: int = 50) -> str:
    """Calculate pi to the requested number of digits after the decimal point.

    The Chudnovsky series adds roughly 14 correct decimal digits per term.
    Returns a decimal string so callers do not lose precision to float rounding.
    """
    if not isinstance(digits, int) or isinstance(digits, bool):
        raise TypeError("digits must be an integer")
    if digits < 0:
        raise ValueError("digits must not be negative")

    with localcontext() as context:
        context.prec = digits + 12
        terms = digits // 14 + 2

        total = Decimal(13591409)
        m = 1
        l = 13591409
        x = 1
        k = 6

        for i in range(1, terms):
            m = (k * k * k - 16 * k) * m // (i * i * i)
            l += 545140134
            x *= -262537412640768000
            total += Decimal(m * l) / Decimal(x)
            k += 12

        pi = (Decimal(426880) * Decimal(10005).sqrt()) / total
        return f"{pi:.{digits}f}"
