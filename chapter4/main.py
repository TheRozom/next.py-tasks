def gen_secs():
    """Generate seconds from 0 to 59."""
    for sec in range(60):
        yield sec


def gen_minutes():
    """Generate minutes from 0 to 59."""
    for minute in range(60):
        yield minute


def gen_hours():
    """Generate hours from 0 to 23."""
    for hour in range(24):
        yield hour


def gen_time():
    """
    Generate time in HH:MM:SS format.
    Utilizes generators for hours, minutes, and seconds.
    """
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, sec)


for gt in gen_time():
    print(gt)


def gen_years(start=2019):
    """
    Generate years starting from the specified year.
    
    Args:
        start (int): Starting year. Default is 2019.
    
    Yields:
        int: Years starting from the specified year.
    """
    year = start
    while True:
        yield year
        year += 1


def gen_months():
    """Generate months from 1 to 12."""
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    """
    Generate days for the given month and year, considering leap years.
    
    Args:
        month (int): Month for which days are generated.
        leap_year (bool): Boolean indicating if the year is a leap year. Default is True.
    
    Returns:
        int: Number of days in the specified month and year.
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
    Generate date and time in DD/MM/YYYY HH:MM:SS format.
    Utilizes generators for years, months, days, hours, minutes, and seconds.
    """
    for year in gen_years():
        for month in gen_months():
            leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
            for day in range(1, gen_days(month, leap_year) + 1):
                for hour in gen_hours():
                    for minute in gen_minutes():
                        for second in gen_secs():
                            yield f"{day:02d}/{month:02d}/{year} {hour:02d}:{minute:02d}:{second:02d}"


gen = gen_date()
for i in range(1, 1000001):
    next_date = next(gen)
    if i % 1000000 == 0:
        print(next_date)
