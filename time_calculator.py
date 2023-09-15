def add_time(start, duration, day_of_week=None):
    # Check and extract the arguments' values
    if not isinstance(start, str):
        return "Error: The argument 'start' must be a string."
    if not isinstance(duration, str):
        return "Error: The argument 'duration' must be a string."
    if day_of_week is not None and not isinstance(day_of_week, str):
        return "Error: The argument 'day_of_week' must be a string."
    
    start_hrs = int()
    try:
        start_hrs_str = start[:start.index(":")]
        start_hrs = int(start_hrs_str)
        if start_hrs not in range(1, 13): raise ValueError
    except ValueError:
        return "Error: Missing or invalid start time's hours."
    
    start_min = int()
    try:
        start_min_str = start[ start.index(":")+1 : start.index(" ")]
        start_min = int(start_min_str)
        if start_min not in range(0, 60): raise ValueError
    except ValueError:
        return "Error: Missing or invalid start time's minutes."
    
    meridiem = str()
    try:
        meridiem = start[start.index(" ")+1:]
        meridiem = meridiem.upper()
        if meridiem != "AM" and meridiem != "PM": raise ValueError
    except ValueError:
        return "Error: Missing or invalid start time's meridiem."

    duration_hrs = int()
    try:
        duration_hrs_str = duration[:duration.index(":")]
        duration_hrs = int(duration_hrs_str)
        if duration_hrs < 0: raise ValueError
    except ValueError:
        return "Error: Missing or invalid duration's hours."
    
    duration_min = int()
    try:
        duration_min_str = duration[duration.index(":")+1:]
        duration_min = int(duration_min_str)
        if duration_min not in range(0, 60): raise ValueError
    except ValueError:
        return "Error: Missing or invalid duration's minutes."
    
    days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    if day_of_week is not None:
        day_of_week = day_of_week.capitalize()
        if day_of_week not in days_of_week:
            return "Error: Invalid day of week value."


    # Compute the result time
    padded_min = start_min + duration_min
    result_min = padded_min % 60
    result_min = str(result_min).rjust(2, "0")
    spillover_hrs = int(padded_min / 60)

    if meridiem == "PM": start_hrs = start_hrs + 12
    padded_hrs = start_hrs + duration_hrs + spillover_hrs
    result_hrs_12hfmt = padded_hrs % 12
    result_hrs_24hfmt = padded_hrs % 24
    if result_hrs_12hfmt == 0: result_hrs_12hfmt = 12

    result_meridiem = str()
    if result_hrs_24hfmt < 12:
        result_meridiem = "AM"
    else:
        result_meridiem = "PM"
    
    days_passed = int(padded_hrs / 24)
    result_days_passed = None
    if days_passed == 1:
        result_days_passed = "(next day)"
    elif days_passed > 1:
        result_days_passed = "(" + str(days_passed) + " days later)"

    result_day_of_week = str()
    if day_of_week is not None:
        day_index = days_of_week.index(day_of_week)
        result_day_index = (day_index + days_passed) % 7
        result_day_of_week = days_of_week[result_day_index]


    # Format the result time
    new_time = str(result_hrs_12hfmt) + ":" + result_min + " " + result_meridiem
    if day_of_week is not None:
        new_time = new_time + ", " + result_day_of_week
    if result_days_passed is not None:
        new_time = new_time + " " + result_days_passed


    return new_time
