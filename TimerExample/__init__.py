import datetime
import logging
import azure.functions as func

from config_loader import get_setting


def main(mytimer: func.TimerRequest) -> None:
    schedule = get_setting("TIMER_SCHEDULE")
    utc_timestamp = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
    if mytimer.past_due:
        logging.warning('The timer is past due!')
    logging.info(f'Timer trigger function ran at {utc_timestamp} with schedule {schedule}')
