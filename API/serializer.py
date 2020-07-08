from rest_framework import serializers
from .models import Question
from rest_framework import routers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('__all__')