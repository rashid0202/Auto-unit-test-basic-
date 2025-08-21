# test_add.py
# We will use pytest framework for automation testing.

from add import adding    # Importing the add() function from our add.py file


# Test case 1: two positive numbers
def test_add_positive_numbers():
    # Arrange – prepare test data
    a = 4
    b = 6
    
    # Act – call the function with above data
    result = adding(a, b)

    # Assert – check the actual result equals the expected result
    assert result == 10    # ✅ test will pass because 4+6 = 10


# Test case 2: two negative numbers
def test_add_negative_numbers():
    a = -2
    b = -5
    result = adding(a, b)
    assert result == -7    # checking that -2 + -5 = -7


# Test case 3: positive and negative number
def test_add_positive_and_negative():
    a = 7
    b = -3
    result = adding(a, b)
    assert result == 4     # 7 + (-3) = 4


# Test case 4: adding zeros
def test_add_zero():
    a = 0
    b = 0
    result = adding(a, b)
    assert result == 0     # 0 + 0 must give 0


# Test case 5: floating point numbers
def test_add_float_numbers():
    a = 2.5
    b = 3.2
    result = adding(a, b)
    assert result == 5.7   # 2.5 + 3.2 = 5.7


# Test case 6: large numbers
def test_add_large_numbers():
    a = 1000000
    b = 2000000
    result = adding(a, b)
    assert result == 3000000  # 1,000,000 + 2,000,000 = 3,000,000
