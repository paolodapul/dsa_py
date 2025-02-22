
from src.two_sum import two_sum


def test_two_sum():
    # Base case (expected match)
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

    # No solution case
    assert two_sum([2, 11, 15], 9) == None

    # Multiple possible pairs, should return first valid pair
    assert two_sum([3, 2, 4], 6) == [1, 2]  # Not [0, 2]

    # Duplicates in the list
    assert two_sum([3, 3], 6) == [0, 1]

    # Negative numbers
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]

    # Large numbers
    assert two_sum([1000000, 500, 1500000, -500], 999500) == [0, 3]

    # Target is sum of the first and last elements
    assert two_sum([1, 2, 3, 4, 5], 6) == [1, 3]

    # Only one element (should return None)
    assert two_sum([5], 5) == None

    # Empty list (should return None)
    assert two_sum([], 5) == None

    print("All two_sum test cases passed!")
