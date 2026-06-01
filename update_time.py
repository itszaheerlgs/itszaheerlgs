import os
import requests
from datetime import datetime
import pytz

def generate_clock_badge():
    # Set timezone to Manila
    manila_tz = pytz.timezone('Asia/Manila')
    now = datetime.now(manila_tz)
    
    # Format strings nicely
    time_str = now.strftime("%I:%M:%S %p")  # 11:05:32 AM
    date_str = now.strftime("%b %d, %Y")    # Jun 01, 2026
    
    # URL encode parameters
    encoded_label = requests.utils.quote(f"🇵🇭 Manila Time")
    encoded_message = requests.utils.quote(f"{time_str} | {date_str}")
    
    # Request badge
    badge_url = f"https://img.shields.io/badge/{encoded_label}-{encoded_message}-0b1f3a?style=for-the-badge&logo=clockify&logoColor=FFD700"
    
    try:
        response = requests.get(badge_url)
        if response.status_code == 200:
            with open("manila_time.svg", "wb") as f:
                f.write(response.content)
            print(f"Clock updated to: {time_str}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    generate_clock_badge()
