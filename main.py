from diagnostics_tool.checks import (
    PythonVersionCheck,
    OperatingSystemCheck,
    GitInstallationCheck,
    VSCodeInstallationCheck,
    RequiredPackagesCheck,
    InternetConnectivityCheck
)

from diagnostics_tool.report import save_json_report, save_csv_report


def main():

    checks = [
        PythonVersionCheck(),
        OperatingSystemCheck(),
        GitInstallationCheck(),
        VSCodeInstallationCheck(),
        RequiredPackagesCheck(),
        InternetConnectivityCheck()
    ]

    results = []

    print("\nDEVELOPER ENVIRONMENT HEALTH CHECKER")
    print("=" * 50)

    for check in checks:
        try:
            result = check.run()
            results.append(result)

            print(f"\n[{result['status']}] {result['check']}")
            print(f"Details: {result['details']}")

        except Exception as error:
            result = {
                "check": check.name,
                "status": "FAIL",
                "details": str(error)
            }

            results.append(result)
            print(f"\n[FAIL] {check.name}")
            print(f"Error: {error}")

    print("\n" + "=" * 50)

    try:
        save_json_report(results)
        save_csv_report(results)

        print("\nReports generated successfully!")
        print("1. diagnostics_report.json")
        print("2. diagnostics_report.csv")

    except Exception as error:
        print(f"\nReport generation failed: {error}")

    passed = sum(1 for r in results if r["status"] == "PASS")
    warnings = sum(1 for r in results if r["status"] == "WARN")
    failed = sum(1 for r in results if r["status"] == "FAIL")

    print("\nFINAL SUMMARY")
    print("-" * 50)
    print(f"Total Checks : {len(results)}")
    print(f"Passed       : {passed}")
    print(f"Warnings     : {warnings}")
    print(f"Failed       : {failed}")

    print("\nEnvironment check completed!")


if __name__ == "__main__":
    main()