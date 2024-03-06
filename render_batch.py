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
            "prompt": "ובשביל להבין למה מחיר הדלק כל כך עלה, צריך לחזור שנתיים אחרונית.",
            "recordings": [
                {
                    "title": f"mms",
                    "audio_path": f"samples/mms/mms_2.wav",
                    "name": f"mms1"
                },
                {
                    "title": f"robo",
                    "audio_path": f"samples/roboshaul/robo_2.wav",
                    "name": f"robo1"
                },
                {
                    "title": f"valle robo",
                    "audio_path": f"samples/word_roboshaul/roboshaul_roboshaul_top_50_temp_1_sample_1_2.wav",
                    "name": f"v-robo1"
                },
                {
                    "title": f"valle osim",
                    "audio_path": f"samples/word_osim/osim_osim_top_50_temp_1_sample_1_2.wav",
                    "name": f"v-osim1"
                }
            ]
        },

        {
            "prompt": "תגידו, גנבו לכם פעם את האוטו ופשוט ידעתם שאין טעם להגיש תלונה במשטרה",
            "recordings": [
                {
                    "title": f"mms",
                    "audio_path": f"samples/mms/mms_4.wav",
                    "name": f"mms2"
                },
                {
                    "title": f"robo",
                    "audio_path": f"samples/roboshaul/robo_4.wav",
                    "name": f"robo2"
                },
                {
                    "title": f"valle robo",
                    "audio_path": f"samples/word_roboshaul/roboshaul_roboshaul_top_50_temp_1_sample_3_0.wav",
                    "name": f"v-robo2"
                },
                {
                    "title": f"valle osim",
                    "audio_path": f"samples/word_osim/osim_osim_top_50_temp_1_sample_3_2.wav",
                    "name": f"v-osim2"
                }
            ]
        },

        {
            "prompt": "מה שבהגדרה משאיר את הכלכלה ההונגרית מאחור, אפילו ביחס למדינות כמו פולין",
            "recordings": [
                {
                    "title": f"mms",
                    "audio_path": f"samples/mms/mms_5.wav",
                    "name": f"mms3"
                },
                {
                    "title": f"robo",
                    "audio_path": f"samples/roboshaul/robo_5.wav",
                    "name": f"robo3"
                },
                {
                    "title": f"valle robo",
                    "audio_path": f"samples/word_roboshaul/roboshaul_roboshaul_top_50_temp_1_sample_4_1.wav",
                    "name": f"v-robo3"
                },
                {
                    "title": f"valle osim",
                    "audio_path": f"samples/word_osim/osim_osim_top_50_temp_1_sample_4_0.wav",
                    "name": f"v-osim3"
                }
            ]
        },

        {
            "prompt": "הדרבי תמיד היה המשחק הכי חשוב, אך בשנים האחרונות הוא נעשה כמעט הדבר היחיד שחשוב",
            "recordings": [
                {
                    "title": f"mms",
                    "audio_path": f"samples/mms/mms_6.wav",
                    "name": f"mms4"
                },
                {
                    "title": f"robo",
                    "audio_path": f"samples/roboshaul/robo_6.wav",
                    "name": f"robo4"
                },
                {
                    "title": f"valle robo",
                    "audio_path": f"samples/word_roboshaul/roboshaul_roboshaul_top_50_temp_1_sample_5_0.wav",
                    "name": f"v-robo4"
                },
                {
                    "title": f"valle osim",
                    "audio_path": f"samples/word_osim/osim_osim_top_50_temp_1_sample_5_0.wav",
                    "name": f"v-osim4"
                }
            ]
        },

        {
            "prompt": "כשני שלישים מייצור הסוללות העולמי מתרחשים בסין לעומת עשרה אחוזים בארצות הברית",
            "recordings": [
                {
                    "title": f"mms",
                    "audio_path": f"samples/mms/mms_10.wav",
                    "name": f"mms5"
                },
                {
                    "title": f"robo",
                    "audio_path": f"samples/roboshaul/robo_10.wav",
                    "name": f"robo5"
                },
                {
                    "title": f"valle robo",
                    "audio_path": f"samples/word_roboshaul/roboshaul_roboshaul_top_50_temp_1_sample_9_2.wav",
                    "name": f"v-robo5"
                },
                {
                    "title": f"valle osim",
                    "audio_path": f"samples/word_osim/osim_osim_top_50_temp_1_sample_9_1.wav",
                    "name": f"v-osim5"
                }
            ]
        },
    ]


    html = template.render(
        page_title="Hebrew TTS",
        form_url="https://script.google.com/macros/s/AKfycbw1f06tdnuvXvye-dU59qvTOlp5UDR2AaB2vXBu_Rrtyqh849tD2nYJ9aMzhJYdrnW4iw/exec",
        form_id=1,
        questions=questions
    )

    print(html)


if __name__ == "__main__":
    main()
