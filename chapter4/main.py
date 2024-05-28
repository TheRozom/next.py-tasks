def gen_secs():
    """
    Generator function to yield seconds from 0 to 59.

    Yields:
        int: The next second in the range 0 to 59.
    """
    for sec in range(60):
        yield sec


def gen_minutes():
    """
    Generator function to yield minutes from 0 to 59.

    Yields:
        int: The next minute in the range 0 to 59.
    """
    for minute in range(60):
        yield minute


def gen_hours():
    """
    Generator function to yield hours from 0 to 23.

    Yields:
        int: The next hour in the range 0 to 23.
    """
    for hour in range(24):
        yield hour


def gen_time():
    """
    Generator function to yield time in HH:MM:SS format.

    Yields:
        str: The next time string in HH:MM:SS format.
    """
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, sec)


def gen_years(start=2019):
    """
    Generator function to yield years starting from a given year.

    Args:
        start (int): The starting year. Default is 2019.

    Yields:
        int: The next year starting from the given start year.
    """
    year = start
    while True:
        yield year
        year += 1


def gen_months():
    """
    Generator function to yield months from 1 to 12.

    Yields:
        int: The next month in the range 1 to 12.
    """
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    """
    Generator function to yield the number of days in a given month.

    Args:
        month (int): The month for which to yield the number of days.
        leap_year (bool): True if the year is a leap year, False otherwise.

    Returns:
        int: The number of days in the given month.
    """
    days_in_month = {
        1: 31,
        2: 29 if leap_year else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    return days_in_month[month]


def gen_date():
    """
    Generator function to yield dates and times from a starting point.

    Yields:
        str: The next date and time string in DD/MM/YYYY HH:MM:SS format.
    """
    for year in gen_years():
        for month in gen_months():
            leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
            for day in range(1, gen_days(month, leap_year) + 1):
                for hour in gen_hours():
                    for minute in gen_minutes():
                        for second in gen_secs():
                            yield (
                                f"{day:02d}/{month:02d}/{year} "
                                f"{hour:02d}:{minute:02d}:{second:02d}"
                            )


def main():
    """
    Main function to demonstrate the usage of the date and time generators.

    Generates and prints dates and times using nested generators.
    Prints every millionth generated date and time up to 1,000,000 times.
    """
    gen = gen_date()
    for i in range(1, 1_000_001):
        next_date = next(gen)
        if i % 1_000_000 == 0:
            print(next_date)


if __name__ == "__main__":
    main()
