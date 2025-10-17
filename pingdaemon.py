import time
import requests
import logging
from datetime import datetime

URLS = [
    "https://tune-trainer-bot.onrender.com",
    "https://sceneradar.onrender.com",
    "https://updevted.onrender.com",
    "https://daily-scope-news.vercel.app",
    "https://algographbot.onrender.com",
    "https://gigarandobot.onrender.com",
]

PING_INTERVAL = 300
LOG_FILE = "ping_daemon.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def ping_site(url):
    try:
        response = requests.get(url, timeout=60)
        if response.status_code == 200:
            logging.info(f"{url} is up ({response.status_code})")
        else:
            logging.warning(f"{url} returned status {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"{url} failed: {e}")

def ping_all_sites():
    for url in URLS:
        ping_site(url)
        time.sleep(2)

def main():
    logging.info("Ping Daemon started.")
    print("Ping Daemon running. Press Ctrl+C to stop.\n")
    while True:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Pinging all sites...")
        ping_all_sites()
        print(f"Next check in {PING_INTERVAL // 60} minutes...\n")
        time.sleep(PING_INTERVAL)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Ping Daemon stopped by user.")
        print("\nStopped by user.")
    except Exception as e:
        logging.exception(f"Unexpected error: {e}")
