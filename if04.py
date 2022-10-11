def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    if a == b:
        answer = 0

    else:
        if a > b:
            answer = a
        else:
            answer = b

    return answer 

print(main(5, 2))