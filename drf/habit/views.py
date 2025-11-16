from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle

from habit.models import Habit, HabitLog
from habit.serializers import HabitSerializer, HabitLogSerializer


class HabitAPIThrottle(UserRateThrottle):
    """
    Кастомный throttle для ограничения частоты запросов к API
    """
    scope = 'habit_throttle'
    rate = '15/m'


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = "__all__"
    throttle_classes = [HabitAPIThrottle]

    def perform_create(self, serializer):
        from auth_user.models import AuthUser
        user = AuthUser.objects.get(id=self.request.user.id)
        serializer.save(user=user)

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitLogViewSet(viewsets.ModelViewSet):
    serializer_class = HabitLogSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = "__all__"
    throttle_classes = [HabitAPIThrottle]
    search_fields = ('is_done',)
    filterset_fields = ('is_done',)

    def perform_create(self, serializer):
        from habit.models import Habit
        habit_id = self.kwargs.get('habit_pk')
        habit = Habit.objects.get(id=habit_id)
        serializer.save(habit=habit)

    def get_queryset(self):
        habit_id = self.kwargs.get('habit_pk')
        return HabitLog.objects.filter(habit=habit_id)