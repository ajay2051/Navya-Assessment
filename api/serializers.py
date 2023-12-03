from rest_framework import serializers

from core.models import InformationModel


class InformationModelSerializers(serializers.ModelSerializer):
    """
    This class serializers (ie convert the python object into JSON object) UserInformation Model.
    """
    class Meta:
        model = InformationModel
        fields = "__all__"