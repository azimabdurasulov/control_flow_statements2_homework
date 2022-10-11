def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    max = a 
    if max < b:
        if max < c:
            max = max
        else:
            max = c

    else:
        if c < b:
            max = c
        else:
            max = b

    return max

print(main(9, 0, 7))