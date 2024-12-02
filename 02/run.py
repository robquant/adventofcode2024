import re
import sys

def is_safe(report:list[int]) -> bool:
    diff = [report[i] - report[i - 1] for i in range(1, len(report))]
    if any(abs(d) == 0 or abs(d) > 3 for d in diff):
        return False
    if any(diff[i] * diff[i + 1] < 0 for i in range(len(diff) - 1)):
        return False
    return True


def main():
    input = "input" if len(sys.argv) == 1 else sys.argv[1]
    reports = [list(map(int, re.findall(r'\d+', line))) for line in open(input)]
    unsafe_reports = [report for report in reports if not is_safe(report)]
    safe_reports = len(reports) - len(unsafe_reports)
    print(safe_reports)

    repairable = 0
    for report in unsafe_reports:
        # print(f"Repairing report {report}")
        for i in range(len(report)):
            report_with_removed = report[:i] + report[i + 1:]
            if is_safe(report_with_removed):
                # print(f"Repaired report by removing {i}")
                repairable += 1
                break
    print(safe_reports + repairable)


if __name__ == "__main__":
    main()