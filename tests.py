import pytest
from main import is_prime

def test_small_primes():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True

def test_small_non_primes():
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(4) == False

def test_large_prime():
    assert is_prime(1999) == True

def test_large_non_prime():
    assert is_prime(1000) == False
    assert is_prime(1020) == False

def test_edge_cases():
    assert is_prime(-1) == False
    assert is_prime(-10) == False
