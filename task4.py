import datetime
import re
import operator

f = open("input4.txt", "r")

last_fell_asleep = -1
curr_guard = -1
guard_to_times = {} # times is list of touples of sort (bool: fell asleep, minute)
guard_to_sleep_sum = {}

for l in f.read().splitlines():
    nums = re.findall(r'[0-9]+', l)

    min = int(nums[4])

    # assumption: never falls asleep or wakes up before 00:00
    if l[19] == 'G':
        curr_guard = int(nums[5])
        if not curr_guard in guard_to_times:
            guard_to_times[curr_guard] = list()
            guard_to_sleep_sum[curr_guard] = 0
    elif l[19] == 'f':
        guard_to_times[curr_guard].append((True, min))
        last_fell_asleep = min
    else: # wakes up
        guard_to_times[curr_guard].append((False, min))
        guard_to_sleep_sum[curr_guard] += min - last_fell_asleep

def part1():
    max_sleep_time = max(guard_to_sleep_sum.values())

    for guard, sleep_time in guard_to_sleep_sum.items():
        if sleep_time == max_sleep_time:
            max_sleep_guard = guard

    times = guard_to_times[max_sleep_guard]
    times.sort(key=lambda tup: tup[0])
    times.sort(key=lambda tup: tup[1])

    minute_most_asleep = -1
    max_times_overlap = -1

    curr_overlap = 0
    for t in times:
        if (t[0]):
            curr_overlap += 1
            if curr_overlap > max_times_overlap:
                max_times_overlap += 1
                minute_most_asleep = t[1]
        else:
             curr_overlap -= 1
    
    print(minute_most_asleep * max_sleep_guard)


def part2():
    guard_most_freq_asleep_on_same_min = -1
    corresponding_min = -1
    freq_asleep_on_that_min = -1

    for guard, times in guard_to_times.items():
        times.sort(key=lambda tup: tup[0])
        times.sort(key=lambda tup: tup[1])

        minute_most_asleep = -1
        max_times_overlap = -1

        curr_overlap = 0
        for t in times:
            if (t[0]):
                curr_overlap += 1
                if curr_overlap > max_times_overlap:
                    max_times_overlap += 1
                    minute_most_asleep = t[1]
            else:
                curr_overlap -= 1
        
        if max_times_overlap > freq_asleep_on_that_min:
            corresponding_min = minute_most_asleep
            freq_asleep_on_that_min = max_times_overlap
            guard_most_freq_asleep_on_same_min = guard

    print(str(guard_most_freq_asleep_on_same_min) + ", " + str(corresponding_min))
    print(corresponding_min * guard_most_freq_asleep_on_same_min)

part1()