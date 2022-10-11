def main(n):
    """
    Find the index of the largest digit of the five-digit number.
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
    index = 0

    if max < x2:
        index = 2

    elif max < x3:
        index = 3

    elif max < x4:
        index = 4

    else: 
        index = 5
    
    return index

print(main(89788))