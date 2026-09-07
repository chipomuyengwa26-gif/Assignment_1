from datetime import datetime

def find_peak_usage(logs):
    hour_counts = {}

    for timestamp in logs:
        clean_timestamp = timestamp.replace(" ", "")
        hour = datetime.fromisoformat(clean_timestamp).hour
        hour_counts[hour] = hour_counts.get(hour, 0) + 1

    if not hour_counts:
        return -1

    peak_hour = max(hour_counts, key=lambda h: (hour_counts[h], -h))
    return peak_hour


log_list = [
    "2026-09-01T08:15:00",
    "2026-09-01T08:47:22",
    "2026-09-02T17:05:10",
    "2026-09-02T08:30:00",
    "2026-09-03T23:59:59",
]

result = find_peak_usage(log_list)
print(result)