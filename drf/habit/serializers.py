from rest_framework import serializers

from habit.models import Habit, HabitLog
#from auth_user.serializers import UserSerializer


class HabitSerializer(serializers.ModelSerializer):
    #user = UserSerializer(read_only=True)

    class Meta:
        model = Habit
        fields = (
            'id', #'user',
            'title',
            'repeat', 'execution_time',
            'updated_at', 'created_at'
        )
        read_only_fields = ('created_at', 'updated_at')


class HabitLogSerializer(serializers.ModelSerializer):
    habit = HabitSerializer(read_only=True)

    class Meta:
        model = HabitLog
        fields = (
            'id', 'habit', 'is_done',
            'created_at',
        )