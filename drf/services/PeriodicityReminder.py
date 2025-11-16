from datetime import date

from repository.HabitRepository import HabitRepository


class PeriodicityReminder:
    period_mapping = {
        "каждый день": [1, 2, 3, 4, 5, 6, 7],
        "по будням": [1, 2, 3, 4, 5],
        "по выходным": [6, 7]
    }

    def get_habits_by_period(self) -> list:
        habits = HabitRepository().get_now_time_habits()

        now_date = date.today()
        filtered_habits = []

        for habit in habits:
            repeat = habit.repeat
            weekly_list = self.period_mapping[repeat]
            week_number = now_date.isoweekday()

            if week_number in weekly_list:
                filtered_habits.append(habit)

        return filtered_habits