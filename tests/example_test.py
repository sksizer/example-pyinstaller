def add_numbers(a: int, b: int) -> int:
    return a + b


def test_add_numbers() -> None:
    assert add_numbers(2, 3) == 5
    assert add_numbers(0, 5) == 5
    assert add_numbers(-1, 1) == 0
