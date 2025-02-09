from typing import List

def merge_intervals(schedule):
    i = 1
    res = []
    res.append(schedule[0])
    while( i < len(schedule)):
        last_interval = res[-1]
        curr_interval = schedule[i]
        if last_interval[0] <= curr_interval[0] and last_interval[1] <= curr_interval[1]:
            if last_interval[1] > curr_interval[0]:
                res[len(res)-1][1] = curr_interval[1]
            else:
                res.append(curr_interval)
        elif last_interval[0] >= curr_interval[0] and last_interval[1] <= curr_interval[1]:
            if last_interval[1] > curr_interval[0]:
                res[len(res)-1][0] = curr_interval[0]

        i += 1
    print(res)
    return res

def get_free_time(schedule):
    work_schedule = []
    res_schedule = []
    for ele in schedule:
        work_schedule += ele
    work_schedule = sorted(work_schedule,key = lambda x:x[0])

    merged_work_schedule = merge_intervals(work_schedule)
    if len(merged_work_schedule) == 1:
        return -1
    else:
        i = 0
        while(i < (len(merged_work_schedule) -1)):
            res_schedule.append([merged_work_schedule[i][1],merged_work_schedule[i+1][0]])
            i += 1
    return res_schedule


if __name__ == "__main__":
    schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
    print(get_free_time(schedule))

    schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
    print(get_free_time(schedule))