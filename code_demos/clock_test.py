
from datetime import datetime, time, timedelta
from clock import (
    Alarm,
    parse_military_time,
    format_military_time,
    next_scheduled_alarm,
    seconds_until,
    alarm_is_due,
)

# 1. Test parsing and formatting
print("TEST 1: Time parsing")

parsed = parse_military_time("14:30")
assert parsed == time(14, 30)
assert parse_military_time("09:05:07") == time(9, 5, 7)
assert format_military_time(parsed) == "14:30"
assert format_military_time(parsed, True) == "14:30:00"

print("Passed!")

# 2. Test invalid time formats
print("TEST 2: Invalid time formats")

for invalid in ["2:30", "14:3", "25:00", "12:60", "abc"]:
    try:
        parse_military_time(invalid)
        raise AssertionError(f"Should have rejected {invalid}")
    except ValueError:
        pass

print("Passed!")

# 3. Test the next scheduled alarm
print("TEST 3: Next scheduled alarm")

now = datetime(2026, 10, 16, 8, 0)  # Friday, 8:00 AM

alarms = [
    Alarm(at=time(9, 30), label="Class"),
    Alarm(at=time(8, 15), label="Meeting"),
    Alarm(at=time(7, 0), label="Past alarm"),
]

next_alarm = next_scheduled_alarm(alarms, now)

assert next_alarm == datetime(2026, 10, 16, 8, 15)
print("Passed! Next alarm:", next_alarm)

# 4. Test weekday repetition
print("TEST 4: Weekday scheduling")

monday_alarm = Alarm(
    at=time(7, 0),
    weekdays=frozenset({0}),  # Monday only
    label="Monday alarm",
)

friday = datetime(2026, 10, 16, 8, 0)
expected_monday = datetime(2026, 10, 19, 7, 0)

assert next_scheduled_alarm([monday_alarm], friday) == expected_monday
print("Passed! Next Monday alarm:", expected_monday)

# 5. Test countdown
print("TEST 5: Countdown")

now = datetime(2026, 10, 16, 8, 0)
target = now + timedelta(minutes=10)

assert seconds_until(target, now) == 600
assert seconds_until(now, now) == 0
assert seconds_until(now, target) == -600

print("Passed!")

# 6. Test whether an alarm is due
print("TEST 6: Alarm triggering")

alarm = Alarm(at=time(8, 30))
assert alarm_is_due(alarm, datetime(2026, 10, 16, 8, 30))
assert not alarm_is_due(alarm, datetime(2026, 10, 16, 8, 31))

disabled_alarm = Alarm(at=time(8, 30), enabled=False)
assert not alarm_is_due(
    disabled_alarm, datetime(2026, 10, 16, 8, 30)
)

print("Passed!")

print("\nAll tests passed!")
