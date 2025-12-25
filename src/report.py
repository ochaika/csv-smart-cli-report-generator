def build_report(rows, report_format="summary"):
    if not rows:
        return ["CSV is empty"]

    columns = rows[0].keys()

    lines = [
        "CSV REPORT",
        "==========",
        f"Rows count: {len(rows)}",
        f"Columns: {', '.join(columns)}",
    ]

    if report_format == "full":
        lines.append("")
        lines.append("All rows:")
        for row in rows:
            lines.append(str(row))

    return lines
