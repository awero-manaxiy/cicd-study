def is_prime(n:int) -> bool:
    """Determines if the number is prime or not"""

    if not(isinstance(n, int)):
        raise ValueError(f'Expected int, found {type(n)}!')
    
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
        
    return True
