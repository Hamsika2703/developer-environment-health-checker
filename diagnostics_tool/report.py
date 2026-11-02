import json
import csv
from diagnostics_tool.exceptions import ReportError


class ReportGenerator:

    def save_json_report(self, results):
        try:
            with open("diagnostics_report.json", "w") as file:
                json.dump(results, file, indent=4)

        except Exception as error:
            raise ReportError(
                f"JSON report failed: {error}"
            )

    def save_csv_report(self, results):
        try:
            with open(
                "diagnostics_report.csv",
                "w",
                newline=""
            ) as file:

                fieldnames = [
                    "check",
                    "status",
                    "details"
                ]

                writer = csv.DictWriter(
                    file,
                    fieldnames=fieldnames
                )

                writer.writeheader()
                writer.writerows(results)

        except Exception as error:
            raise ReportError(
                f"CSV report failed: {error}"
            )


def save_json_report(results):
    generator = ReportGenerator()
    generator.save_json_report(results)


def save_csv_report(results):
    generator = ReportGenerator()
    generator.save_csv_report(results)