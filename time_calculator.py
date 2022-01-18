def parse_time(time):
    colon = time.find(":")
    hours = time[:colon]
    minutes = time[colon+1: colon +3]
    hours = int(hours)
    minutes = int(minutes)
    return(hours, minutes)

def define_day_of_week(dayOfWeek, days_gone):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    i = 0
    for day in days:
        if day == dayOfWeek:
            break
        i += 1
    i += days_gone
    if i > 6:
        i = (i + 1) % 7 - 1
    return(", " + days[i])

def count_hours_minutes(start, duration):
    s_hours, s_minutes = parse_time(start)
    d_hours, d_minutes = parse_time(duration)
    r_hours = 0

    r_minutes = s_minutes + d_minutes
    r_hours = s_hours + d_hours
    
    if r_minutes >= 60:
        r_minutes = r_minutes - 60
        r_hours += 1
    return(r_hours, r_minutes)


def add_time(start, duration, dayOfWeek=None):

    pm_am = start[len(start) - 2]
    days_gone = 0
    r_hours, r_minutes = count_hours_minutes(start, duration)

    while r_hours > 12:
        r_hours -= 12
        if pm_am == 'A':
            pm_am = "P"
        elif pm_am == "P":
            pm_am = 'A'
            days_gone += 1
    if r_hours == 12:
        if pm_am == 'A':
            pm_am = "P"
        elif pm_am == "P":
            pm_am = 'A'
    if r_hours == 12 and pm_am == "A":
        days_gone += 1
    if r_minutes < 10:
        r_minutes = "0" + str(r_minutes)
    new_time = str(r_hours) + ":" + str(r_minutes) + " " + pm_am + "M"

    if dayOfWeek:
        new_time = new_time + define_day_of_week(dayOfWeek.capitalize(), days_gone)

    if days_gone == 1:
        new_time = new_time + " (next day)"
    elif days_gone > 1:
        new_time = new_time + " (" + str(days_gone) + " days later)"
    return new_time


print(add_time("11:59 PM", "24:05", "Wednesday"))