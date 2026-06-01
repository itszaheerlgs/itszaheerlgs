from datetime import datetime
import pytz

def generate_clock_svg():
    manila_tz = pytz.timezone('Asia/Manila')
    now = datetime.now(manila_tz)
    time_str = now.strftime("%I:%M %p")
    date_str = now.strftime("%b %d, %Y")

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="360" height="40">
  <rect width="360" height="40" rx="7" fill="#0b1f3a"/>
  <text x="14" y="26" font-family="monospace,sans-serif" font-size="15"
        fill="#FFD700" xml:space="preserve">&#127477;&#127469; Manila  {time_str}  ·  {date_str}</text>
</svg>"""

    with open("manila_time.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"SVG updated: {time_str} | {date_str}")

if __name__ == "__main__":
    generate_clock_svg()
