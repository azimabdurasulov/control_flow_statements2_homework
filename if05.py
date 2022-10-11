def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    x1 = n % 10
    n //= 10 

    x2 = n % 10
    n //= 10

    x3 = n % 10
    n //= 10

    x4 = n % 10
    n //= 10

    x5 = n % 10
    n //= 10

    max = x1 

    if max < x2:
        max = x2

    if max < x3:
        max = x3

    if max < x4:
        max = x4

    if max < x5:
        max = x5 
    
    return max

print(main(89874))