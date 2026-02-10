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
    blocked = False

    for finding in results:
        severity = finding.get("extra", {}).get("severity", "INFO")
        risk = classify_risk(severity)
        title = finding.get("check_id")

        if risk == "CRITICAL":
            print(f"🚫 CRITICAL FOUND: {title}")
            blocked = True

        elif risk == "HIGH":
            print(f"⚠ HIGH FOUND: {title}")

        elif risk == "LOW":
            print(f"🟢 LOW: {title}")

    return not blocked


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python enforce_policy.py semgrep.json")
        sys.exit(1)

    with open(sys.argv[1], "r") as f:
        data = json.load(f)

    results = data.get("results", [])

    allowed = enforce_semgrep_policy(results)

    if not allowed:
        print("\n❌ Merge blocked due to CRITICAL vulnerabilities.")
        sys.exit(1)
    else:
        print("\n✅ Security policy passed.")
        sys.exit(0)
