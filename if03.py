def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if b >= a and b <= c:
        return b
    if a >= b and a <= c:
        return a
    if c >= a and c <= b:
        return c

print(main(2, 32, 31))