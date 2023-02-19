from rest_framework import serializers

from splitapp.models import UserProfile


class userserializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('__all__')
