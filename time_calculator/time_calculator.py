HOUR = 60
HOURS_12 = 720
DAY = 1440
WEEK_DAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
    )


def time_to_min(time):
    time = time.split(":")
    return int(time[0]) * 60 + int(time[1])


def format_time(time):
    hours, minutes, suffix = (0, 0, "")
    ret_val = "{}:{} {}"
    if time // 60 > 12:
        hours = str((time - HOURS_12) // 60)
        minutes = (time - HOURS_12) % 60
        suffix = "PM"
    else:
        hours = time // 60
        minutes = time % 60
        suffix = "AM"

    # Check 24.00 and 12.00 situations, when suffix changes
    if time // 60 == 0:
        hours += 12
        suffix = "AM" 
    elif time // 60 == 12:
        suffix = "PM"

    minutes = "0" + str(minutes) if minutes < 10 else str(minutes)
    return ret_val.format(hours, minutes, suffix)


def add_time(start, duration, day=None):
    ret_val = "{}{} {}"
    days_passed_promt = ""

    start_time = start.split()
    start_time[0] = time_to_min(start_time[0])
    if start_time[1] == "PM": 
        start_time[0] = start_time[0] + HOURS_12
    start_time = start_time[0]
    end_time = start_time + time_to_min(duration)
    days_passed = end_time // DAY

    formated_time = format_time(end_time % DAY)
    if day is None:
        day = ""
    else:
        day = day.capitalize()
        day_index = WEEK_DAYS.index(day)
        day_index += days_passed
        day = ", {}".format(WEEK_DAYS[day_index])

    if days_passed == 1:
        days_passed_promt = "(next day)"
    elif days_passed > 1:
        days_passed_promt = "({} days later)".format(days_passed)

    return ret_val.format(formated_time, day, days_passed_promt)


print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))
