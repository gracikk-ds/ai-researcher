"""Daemon script to run entrypoint.py once per day at 9:00 am.

SECURITY NOTE: This script uses subprocess to run trusted local code only.
"""

import datetime
import subprocess  # noqa: S404
import time
from typing import List

from apscheduler.schedulers.background import BackgroundScheduler
from loguru import logger

LOG_FILE = "daemon.log"


def build_command() -> List[str]:
    """
    Build the command to run the entrypoint CLI.

    Start date is a day before the current date. End date is the current date.

    Returns:
        List[str]: The command and arguments as a list.
    """
    start_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    end_date = datetime.datetime.now().strftime("%Y-%m-%d")
    return [
        "python",
        "src/entrypoint.py",
        "--start-date",
        start_date,
        "--end-date",
        end_date,
    ]


def run_job() -> None:
    """Run the entrypoint CLI and log output."""
    cmd = build_command()
    with open(LOG_FILE, "a") as log:
        log.write(f"\n--- Running at {datetime.datetime.now()} ---\n")
        process = subprocess.Popen(cmd, stdout=log, stderr=log)  # noqa: S603
        process.wait()
        log.write(f"--- Finished at {datetime.datetime.now()} ---\n")


def main() -> None:
    """Schedule the job to run daily at 9:00 am using APScheduler."""
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_job, "cron", hour=8, minute=0)
    scheduler.start()
    logger.info("Scheduler started. Job will run daily at 8:00 am.")
    try:
        while True:  # noqa: WPS457
            time.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        logger.info("Scheduler stopped.")


if __name__ == "__main__":
    main()
