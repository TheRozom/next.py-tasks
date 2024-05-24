# 1
def gen_secs():
    for sec in range(60):
        yield sec


# 2
def gen_minutes():
    for minute in range(60):
        yield minute


# 3
def gen_hours():
    for hour in range(24):
        yield hour


# 4
def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, sec)


for gt in gen_time():
    print(gt)


# 5
def gen_years(start=2019):
    year = start
    while True:
        yield year
        year += 1


# 6
def gen_months():
    for month in range(1, 13):
        yield month


# 7
def gen_days(month, leap_year=True):
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
