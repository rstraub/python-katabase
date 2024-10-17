from fizzbuzz import fizzbuzz


def test_should_return_number():
    assert fizzbuzz(1) == "1"


def test_should_return_fizz_if_divisible_by_three():
    assert fizzbuzz(3) == "Fizz"


def test_should_return_buzz_if_divisible_by_five():
    assert fizzbuzz(5) == "Buzz"


def test_should_return_fizzbuzz_if_divisible_by_five_and_three():
    assert fizzbuzz(15) == "FizzBuzz"

