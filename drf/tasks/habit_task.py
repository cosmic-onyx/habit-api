from notifiers import get_notifier
from loguru import logger

from drf.celery import app
from services.PeriodicityReminder import PeriodicityReminder
from habit.models import Habit


@app.task(name='habit_task.remind_of_habit')
def remind_of_habit(habit_id):
    from drf.settings import TELEGRAM_BOT_TOKEN

    try:
        habit = Habit.objects.select_related('user').get(id=habit_id)

        text = f"""Напоминаю про привычку: {habit.title}"""
        receipt = habit.user.telegram_id

        logger.info(f"Отправка напоминания для привычки '{habit.title}' пользователю {receipt}")
        logger.info(
            f"{TELEGRAM_BOT_TOKEN}, {receipt}, {text}"
        )
        telegram = get_notifier('telegram')
        telegram.notify(
            token=TELEGRAM_BOT_TOKEN,
            chat_id=str(receipt),
            message=text
        )

        logger.info(f"Напоминание отправлено успешно")
    except Habit.DoesNotExist:
        logger.error(f"Привычка с ID {habit_id} не найдена")
    except Exception as e:
        logger.error(f"Ошибка при отправке напоминания: {e}", exc_info=True)


@app.task(name='habit_task.select_today_habits')
def select_today_habits():
    try:
        habits = PeriodicityReminder().get_habits_by_period()

        logger.info(f"Найдено привычек для напоминания: {len(habits) if habits else 0}")

        if habits:
            for habit in habits:
                logger.info(f"Запуск задачи напоминания для привычки '{habit.title}' (ID: {habit.id})")
                remind_of_habit.apply_async(
                    kwargs={'habit_id': habit.id}
                )
        else:
            logger.info("Нет привычек для напоминания")
    except Exception as e:
        logger.error(f"Ошибка в задаче select_today_habits: {e}", exc_info=True)