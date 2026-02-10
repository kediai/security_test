import json
import sys


def classify_risk(severity):
    if severity == "ERROR":
        return "CRITICAL"
    elif severity == "WARNING":
        return "HIGH"
    else:
        return "LOW"


def enforce_semgrep_policy(results):
    critical_count = 0
    high_count = 0
    low_count = 0

    for finding in results:
        severity = finding.get("extra", {}).get("severity", "INFO")
        risk = classify_risk(severity)

        if risk == "CRITICAL":
            critical_count += 1
        elif risk == "HIGH":
            high_count += 1
        else:
            low_count += 1

    print("\n🔎 Security Summary")
    print(f"🔴 Critical: {critical_count}")
    print(f"🟠 High: {high_count}")
    print(f"🟢 Low: {low_count}")

    # 🔴 CRITICAL → Block
    if critical_count > 0:
        print("\n❌ PR blocked due to CRITICAL vulnerabilities.")
        return 1

    # 🟠 HIGH → Allow but require approval
    if high_count > 0:
        print("\n⚠ HIGH vulnerabilities detected. Approval required.")
        return 0

    # 🟢 LOW → Allow
    print("\n✅ Only LOW issues detected. PR allowed.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python enforce_policy.py semgrep.json")
        sys.exit(1)

    with open(sys.argv[1], "r") as f:
        data = json.load(f)

    results = data.get("results", [])

    exit_code = enforce_semgrep_policy(results)
    sys.exit(exit_code)
