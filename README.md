# PingDaemon

**PingDaemon** is a lightweight Python-based uptime keeper that periodically pings specified URLs to prevent web services from going idle. It is ideal for keeping Render, Vercel, or other web apps awake on free hosting plans that automatically sleep after inactivity.

---

## Features

* Periodically sends HTTP requests to multiple URLs.
* Logs uptime status and HTTP response codes.
* Works cross-platform (Windows, macOS, Linux).
* Can run silently in the background or as a startup task.
* Customizable ping interval and site list.

---

## Requirements

* Python 3.8 or newer
* `requests` library

Install the dependency using:

```bash
pip install requests
```

---

## Installation

1. Clone or download this repository.
2. Place the file `pingdaemon.py` in any directory on your system.
3. Open a terminal in that directory.

---

## Configuration

Open `pingdaemon.py` and edit the `URLS` list to include your own site URLs:

```python
URLS = [
    "https://tune-trainer-bot.onrender.com",
    "https://scene-radar.onrender.com",
    "https://updevted.onrender.com",
    "https://daily-scope-news.vercel.app",
    "https://algographbot.onrender.com",
    "https://gigarandobot.onrender.com",
]
```

You can also adjust the ping interval (default: 300 seconds or 5 minutes):

```python
PING_INTERVAL = 300
```

---

## Usage

### Run manually

In your terminal:

```bash
python pingdaemon.py
```

You will see logs in the console and a file named `ping_daemon.log` will be created to store timestamped results.

### Run silently (background mode)

#### Windows

Run:

```bash
pythonw pingdaemon.py
```

This runs the script without a console window.

To make it start automatically:

1. Open **Task Scheduler**.
2. Create a new task.
3. Set the **Action** to run:

   * Program/script: `pythonw.exe`
   * Add arguments: `"C:\path\to\pingdaemon.py"`
4. Set the **Trigger** to run *At startup* or *At login*.
5. Choose *Run whether user is logged on or not*.

#### macOS / Linux

Run:

```bash
nohup python3 pingdaemon.py > /dev/null 2>&1 &
```

This detaches the process so it continues running even after the terminal is closed.

To verify it’s running:

```bash
ps aux | grep pingdaemon
```

---

## Logs

All activity is logged to `ping_daemon.log` in the same directory.
Each entry includes:

* Timestamp
* Log level (INFO, WARNING, ERROR)
* URL and HTTP status

Example log entry:

```
2025-10-17 16:15:01 | INFO | https://scene-radar.onrender.com is up (200)
```

---

## Stopping the Daemon

If running interactively, press `Ctrl + C`.
If running in the background:

* On Windows, stop it through Task Manager or Task Scheduler.
* On macOS/Linux, use:

  ```bash
  pkill -f pingdaemon.py
  ```

---

## Best Practices

* Use a 5–10 minute interval to avoid overloading servers.
* Keep the script running only on reliable devices (e.g., desktop or Raspberry Pi).
* Regularly check the log file to confirm uptime.

---

## License

This project is released under the MIT License. You are free to use, modify, and distribute it with attribution.

