import argparse
import os

from src.loader import load_csv
from src.report import build_report

def main():
    parser = argparse.ArgumentParser(description="CSV Smart CLI")
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    parser.add_argument(
        "--format",
        choices=["summary", "full"],
        default="summary",
        help="Report format"
    )
    parser.add_argument("--output", default="report.txt", help="Output report file")

    args = parser.parse_args()

    output_dir = os.path.dirname(args.output)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    rows = load_csv(args.input)
    report_lines = build_report(rows, args.format)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    print(f"Report saved to {args.output}")

if __name__ == "__main__":
    main()
