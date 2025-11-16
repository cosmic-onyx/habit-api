from rest_framework_nested.routers import NestedSimpleRouter

from habit.views import HabitViewSet, HabitLogViewSet
from utils.custom_router import EnhancedAPIRouter


habit_router = EnhancedAPIRouter()

habit_router.register(
    'habits',
    HabitViewSet,
    basename='habits'
)

habit_log_router = NestedSimpleRouter(
    habit_router,
    r'habits',
    lookup='habit'
)

habit_log_router.register(
    r'logs',
    HabitLogViewSet,
    basename="habit-log"
)

habit_router.register(
    '',
    habit_log_router,
    'nested'
)
