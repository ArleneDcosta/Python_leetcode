from typing import List, Tuple

def min_steps(button_values: List[int], target: int) -> int:
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  

    for i in range(1, target + 1):
        for value in button_values:
            if i - value >= 0:
                dp[i] = min(dp[i], dp[i - value] + 1)

    return dp[target] if dp[target] != float('inf') else 0

def parse_time(buttons: List[str]) -> Tuple[List[int], List[int]]:
    hours_button = []
    minutes_button = []
    for time in buttons:
        hours, minutes = map(int, time.split(":"))
        hours_button.append(hours)
        minutes_button.append(minutes)
    return hours_button, minutes_button

def calculate_time_difference(current: str, desired: str) -> Tuple[int, int]:
    current_hours, current_minutes = map(int, current.split(":"))
    desired_hours, desired_minutes = map(int, desired.split(":"))

    hour_diff = (desired_hours - current_hours) % 24
    if desired_minutes < current_minutes:
        hour_diff = (hour_diff - 1) % 24
    minute_diff = (desired_minutes - current_minutes) % 60

    return hour_diff, minute_diff

def time_adjustment_problem(buttons: List[str], timelist: List[Tuple[str, str]]) -> int:
    hours_button, minutes_button = parse_time(buttons)
    total_presses = 0

    for current_time, desired_time in timelist:
        hour_diff, minute_diff = calculate_time_difference(current_time, desired_time)
        total_presses += min_steps(hours_button, hour_diff)
        total_presses += min_steps(minutes_button, minute_diff)


    return total_presses

if __name__ == '__main__':
    buttons = ["1:00", "00:15", "00:5", "00:1"]
    timelist = [("12:30", "14:00"), ("22:45", "01:00"), ("11:59", "12:01")]
    result = time_adjustment_problem(buttons, timelist)
    print(result)
