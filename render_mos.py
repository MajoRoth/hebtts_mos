#!/usr/bin/env python3
"""Generate forms for human evaluation."""
from pathlib import Path

from jinja2 import FileSystemLoader, Environment


def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("mos.html.jinja2")

    wavs = sorted(Path('samples').glob("*wav"))
    html = template.render(
        page_title="MOS",
        form_url="https://script.google.com/macros/s/AKfycbxbVMQc6QRjAAZsEBjWesC0RScmRRuJAO4_i-wpDWeU86_b3x24Ge1o1CmH1qCiwKqUxA/exec",
        form_id=1,
        questions=[
            {
                "title": f"recording {i+1}",
                "audio_path": f"{p}",
                "name": f"q{i}"
            } for i, p in enumerate(wavs)
        ]
    )

    print(html)


if __name__ == "__main__":
    main()
