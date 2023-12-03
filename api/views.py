from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from api.serializers import InformationModelSerializers


class InformationAPIView(APIView):

    def get(self, request):
        """
        This function is used to retrieve all user information from database.
        :param self:
        :param request:
        :return: User Information
        """
        try:
            information = InformationModelSerializers.Meta.model.objects.all()
            serializer = InformationModelSerializers(information, many=True)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"data": serializer.data,
                         "message": "Data Retrieved Successfully"},
                        status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        This function is used to post user information and save it to database
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer = InformationModelSerializers(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({"data": serializer.data,
                                 "message": "Information Uploaded Successfully"},
                                status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
