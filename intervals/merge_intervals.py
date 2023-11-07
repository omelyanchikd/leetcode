def merge(intervals):
    intervals.sort(key = lambda x: x[0])
    merged_intervals = []
    interval = intervals.pop(0)
    while len(intervals) > 0:
        next_interval = intervals.pop(0)
        if interval[1] < next_interval[0]:
            merged_intervals.append(interval)
            interval = next_interval
        else:
            interval = [interval[0], max(interval[1], next_interval[1])]
    merged_intervals.append(interval)
    return merged_intervals

if __name__ == '__main__':
    intervals = [[8, 3], [2, 6], [9, 10], [5, 18]]
    print(merge(intervals))