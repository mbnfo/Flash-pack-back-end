from rest_framework.serializers import ModelSerializer
from base.models import FlashCard, FlashPacks


class FlashSerializer(ModelSerializer):
    class Meta:
        model = FlashCard
        fields = '__all__'

class FlashPackSerializer(ModelSerializer):
    class Meta:
        model = FlashPacks
        fields = '__all__'

class PackSerializer(ModelSerializer):
    class Meta:
        model = FlashPacks
        fields = '__all__'