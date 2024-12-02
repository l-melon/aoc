with open("input.txt") as f:
    lines = [list(map(int, line.strip().split())) for line in f]


def is_safe_report(report):
    increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))

    valid_differences = all(
        1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1)
    )

    return valid_differences and (increasing or decreasing)


def count_safe_reports(data):
    return sum(1 for report in data if is_safe_report(report))


safe_reports = count_safe_reports(lines)
print(safe_reports)
