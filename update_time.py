import os
from datetime import datetime
import pytz

def generate_clock_svg():
    manila_tz = pytz.timezone('Asia/Manila')
    now = datetime.now(manila_tz)
    time_str = now.strftime("%I:%M %p")
    date_str = now.strftime("%b %d, %Y")
    label = f"🇵🇭 Manila  {time_str}  ·  {date_str}"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="340" height="36">
  <rect width="340" height="36" rx="6" fill="#0b1f3a"/>
  <text x="12" y="24" font-family="monospace,sans-serif" font-size="14"
        fill="#FFD700" xml:space="preserve">{label}</text>
</svg>"""

    with open("manila_time.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"SVG updated: {time_str} | {date_str}")

if __name__ == "__main__":
    generate_clock_svg()
