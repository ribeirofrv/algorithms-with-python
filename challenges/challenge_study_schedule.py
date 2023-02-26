# def study_schedule(permanence_period, target_time):
#     if type(target_time) is not int:
#         return None

#     count = 0
#     for start_time, end_time in permanence_period:
#         if type(start_time) is not int or type(end_time) is not int:
#             return None
#         elif start_time <= target_time <= end_time:
#             count += 1
#     return count

def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None

    counts = {}
    for start_time, end_time in permanence_period:
        if not isinstance(start_time, int) or not isinstance(end_time, int):
            return None
        for i in range(start_time, end_time + 1):
            counts[i] = counts.get(i, 0) + 1

    return counts.get(target_time, 0)
