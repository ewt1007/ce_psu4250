"""Platform-independent helpers for 24-hour alarm clock logic."""

from dataclasses import dataclass
from datetime import datetime, time, timedelta
from typing import FrozenSet, Iterable, Optional


def parse_military_time(value: str) -> time:
	"""Parse a zero-padded HH:MM or HH:MM:SS value."""
	parts = value.split(":")
	if len(parts) not in (2, 3) or any(
		len(part) != 2 or not part.isdigit() for part in parts
	):
		raise ValueError("Expected 24-hour time in HH:MM or HH:MM:SS format")
	hour, minute = int(parts[0]), int(parts[1])
	second = int(parts[2]) if len(parts) == 3 else 0
	return time(hour, minute, second)


def format_military_time(value: time, include_seconds: bool = False) -> str:
	"""Format a time as zero-padded 24-hour text."""
	return value.strftime("%H:%M:%S" if include_seconds else "%H:%M")


@dataclass(frozen=True)
class Alarm:
	"""An alarm; weekdays use Monday=0 through Sunday=6.

	Set weekdays to None to repeat every day. An empty set never repeats.
	"""

	at: time
	weekdays: Optional[FrozenSet[int]] = None
	enabled: bool = True
	label: str = ""

	def __post_init__(self) -> None:
		if self.weekdays is not None and any(
			day not in range(7) for day in self.weekdays
		):
			raise ValueError("Weekdays must be between 0 (Monday) and 6 (Sunday)")


def next_scheduled_alarm(
	alarms: Iterable[Alarm], now: Optional[datetime] = None
) -> Optional[datetime]:
	"""Find the next enabled alarm occurrence, including one due right now."""
	current = now if now is not None else datetime.now().astimezone()
	next_occurrence = None

	for alarm in alarms:
		if not alarm.enabled:
			continue
		for offset in range(8):
			alarm_date = current.date() + timedelta(days=offset)
			if alarm.weekdays is not None and alarm_date.weekday() not in alarm.weekdays:
				continue
			occurrence = datetime.combine(alarm_date, alarm.at).replace(
				tzinfo=current.tzinfo
			)
			if occurrence < current:
				continue
			if next_occurrence is None or occurrence < next_occurrence:
				next_occurrence = occurrence
			break

	return next_occurrence


def seconds_until(target: datetime, now: Optional[datetime] = None) -> float:
	"""Return seconds until target; negative means the target has passed."""
	current = now if now is not None else datetime.now(target.tzinfo)
	return (target - current).total_seconds()


def alarm_is_due(alarm: Alarm, now: Optional[datetime] = None) -> bool:
	"""Return whether an enabled alarm matches the current minute and day."""
	current = now if now is not None else datetime.now().astimezone()
	return (
		alarm.enabled
		and current.hour == alarm.at.hour
		and current.minute == alarm.at.minute
		and (alarm.weekdays is None or current.weekday() in alarm.weekdays)
	)
