from pathlib import Path

REPORT_PATH = Path("assets/images/promptfoo_report.html")


def fix_html_language() -> None:
    if not REPORT_PATH.exists():
        raise FileNotFoundError(f"Promptfoo report not found: {REPORT_PATH}")

    html = REPORT_PATH.read_text(encoding="utf-8")

    # Already fixed
    if '<html lang="en">' in html:
        print('Promptfoo report already contains lang="en".')
        return

    # Standard generated HTML
    if "<html>" in html:
        html = html.replace(
            "<html>",
            '<html lang="en">',
            1,
        )

    # Handle <html ...> without an existing lang attribute
    elif "<html" in html:
        opening_tag_end = html.find(">")
        opening_tag = html[: opening_tag_end + 1]

        if "lang=" not in opening_tag:
            fixed_opening_tag = opening_tag.replace(
                "<html",
                '<html lang="en"',
                1,
            )

            html = fixed_opening_tag + html[opening_tag_end + 1 :]

        else:
            print("An HTML lang attribute already exists.")
            return

    else:
        raise RuntimeError(
            "Could not locate the <html> element in the Promptfoo report."
        )

    REPORT_PATH.write_text(html, encoding="utf-8")

    print(f'Accessibility fix applied: <html lang="en"> -> {REPORT_PATH}')


if __name__ == "__main__":
    fix_html_language()
