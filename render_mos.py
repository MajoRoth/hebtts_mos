#!/usr/bin/env python3
"""Generate forms for human evaluation."""
from pathlib import Path

from jinja2 import FileSystemLoader, Environment
import json

def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("mos.html.jinja2")

    with open("samples_gt/samples.json", 'r') as f:
        samples_json = json.load(f)

    directories = [
        'gt',
        'mms',
        'roboshaul',
        'word_osim',
        'word_shaul'
    ]

    # questions = [
    #     {
    #         "id": i,
    #         "prompt": s['prompt'],
    #         "recordings": [
    #             {
    #                 'title': d,
    #                 'audio_path': f"samples/{d}/{s['index']}.wav",
    #                 'name': f"{d}_{s['index']}"
    #             } for d in directories
    #         ]
    #     } for i, s in enumerate(samples_json)
    # ]

    questions = [
        {
            'dir': d,
            'prompt': s['prompt'],
            'title': f"dir {d}, index {s['index']}",
            'audio_path': f"samples_gt/{d}/{s['index']}.wav",
            'name': f"{d}_{s['index']}"
        } for d in directories for i, s in enumerate(samples_json)
    ]

    html = template.render(
        page_title="MOS",
        form_url="https://script.google.com/macros/s/AKfycbyUQOOuz31ueOC8q5CFJE5sTmFjVKc1yB7pSaoTJtaKJ07BeQxojBCYFT9J02KcSw89OA/exec",
        form_id=1,
        questions=questions
    )

    with open("rendered_mos.html", 'w') as f:
        f.write(html)

    print(html)

    print(html)


if __name__ == "__main__":
    main()
