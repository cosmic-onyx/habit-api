from datetime import datetime
from loguru import logger

from habit.models import Habit


class HabitRepository:
    def __init__(self):
        self.model = Habit

    def get_now_time_habits(self):
        now_time = f"{datetime.now().time().strftime("%H:%M")}:00"
        logger.info(now_time)
        queryset = self.model.objects.filter(
            execution_time=now_time
        )
        logger.info(queryset)
        return queryset