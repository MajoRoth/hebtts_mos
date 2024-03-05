#!/usr/bin/env python3
"""Generate forms for human evaluation."""
from pathlib import Path

from jinja2 import FileSystemLoader, Environment


def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("batch_comparison.html.jinja2")

    # names should be unique and with correct format for app.gs
    questions = [
        {
            "prompt": "prompt 1",
            "recordings": [
                {
                    "title": f"robo",
                    "audio_path": f"samples/mms_10.wav",
                    "name": f"robo1"
                },
                {
                    "title": f"mms",
                    "audio_path": f"/samples/mms_10.wav",
                    "name": f"mms1"
                },
                {
                    "title": f"valle",
                    "audio_path": f"./samples/mms_10.wav",
                    "name": f"words1"
                },
                {
                    "title": f"alephbert",
                    "audio_path": f"/Users/amitroth/PycharmProjects/hebtts_mos/samples/mms_10.wav",
                    "name": f"alephbert1"
                }
            ]
        },

        {
            "prompt": "prompt 2",
            "recordings": [
                {
                    "title": f"robo",
                    "audio_path": f"/Users/amitroth/PycharmProjects/hebtts_mos/samples/mms_10.wav",
                    "name": f"robo2"
                },
                {
                    "title": f"mms",
                    "audio_path": f"/Users/amitroth/PycharmProjects/hebtts_mos/samples/mms_10.wav",
                    "name": f"mms2"
                },
                {
                    "title": f"valle",
                    "audio_path": f"/Users/amitroth/PycharmProjects/hebtts_mos/samples/mms_10.wav",
                    "name": f"words2"
                },
                {
                    "title": f"alephbert",
                    "audio_path": f"/Users/amitroth/PycharmProjects/hebtts_mos/samples/mms_10.wav",
                    "name": f"alephbert2"
                }
            ]
        }
    ]
    html = template.render(
        page_title="Hebrew TTS",
        form_url="https://script.google.com/macros/s/AKfycbwbk2Rtm-UhOXC4uj_XS29-SiBtKmQF_hCKtZdZgON8ZFlArsTSDm2QSkkMblVq4CZ3KQ/exec",
        form_id=1,
        questions=questions
    )

    print(html)


if __name__ == "__main__":
    main()
