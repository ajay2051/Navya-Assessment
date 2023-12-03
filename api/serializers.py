from rest_framework import serializers

from core.models import InformationModel


class InformationModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = InformationModel
        fields = "__all__"