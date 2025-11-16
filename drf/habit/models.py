from django.db import models

from auth_user.models import AuthUser


class Habit(models.Model):
    user = models.ForeignKey(
        AuthUser,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    title = models.CharField(
        max_length=100,
        verbose_name="Название"
    )
    repeat = models.CharField(
        max_length=50,
        verbose_name="Переодичность"
    )
    execution_time = models.TimeField(
        verbose_name="Время напоминания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    class Meta:
        ordering = ['created_at', 'title']
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return self.title


class HabitLog(models.Model):
    habit = models.ForeignKey(
        Habit,
        on_delete=models.CASCADE,
        verbose_name="Привычка"
    )
    is_done = models.CharField(
        max_length=10,
        blank=True,
        default="не сделано",
        verbose_name="Статус"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    class Meta:
        ordering = ["habit__created_at"]
        verbose_name = "Журнал привычки"
        verbose_name_plural = "Журналы привычек"

    def __str__(self):
        return f"{self.habit.title}: {self.is_done}"