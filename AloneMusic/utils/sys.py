
import time
import psutil

from AloneMusic.misc import _boot_
from AloneMusic.utils.formatters import get_readable_time


async def bot_sys_stats():
    bot_uptime = int(time.time() - _boot_)
    UP = f"{get_readable_time(bot_uptime)}"
    CPU = f"{psutil.cpu_percent(interval=0.5)}%"
    RAM = f"{psutil.virtual_memory().percent}%"

    try:
        disk_percent = psutil.disk_usage("/tmp").percent
    except Exception:
        disk_percent = psutil.disk_usage(".").percent

    DISK = f"{disk_percent}%"

    return UP, CPU, RAM, DISK


async def bot_up_time():
    bot_up_time = int(time.time() - _boot_)
    BOT_UP = f"{get_readable_time(bot_up_time)}"
    return BOT_UP
