from datetime import date

def days_diff(a, b):
    day_1 = date(a[0], a[1], a[2])
    day_2 = date(b[0], b[1], b[2])
    return abs((day_1 - day_2).days)


if __name__ == "__main__":
    print("Example:")
    print(days_diff((2014, 1, 1), (2014, 8, 1)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 1)) == 211
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")