from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AddedSerializer, AddedDetailSerializer, AddedSerializerUpdate
from .models import Added

class SubmitData(APIView):
    def post(self, request):
        try:
            serializer = AddedSerializer(data=request.data)
            if serializer.is_valid():
                pereval = serializer.save()
                return Response(
                    {
                        "status": 200,
                        "message": None,
                        "id": pereval.id
                    },
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {
                        "status": 400,
                        "message": "Ошибка валидации данных",
                        "errors": serializer.errors,
                        "id": None
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {
                    "status": 500,
                    "message": f"Ошибка сервера: {str(e)}",
                    "id": None
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class SubmitDataDetail(APIView):

    def get(self, request, pk):
        try:
            pereval = Added.objects.get(pk=pk)
            serializer = AddedDetailSerializer(pereval)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Added.DoesNotExist:
            return Response(
                {
                    "message": "Запись не найдена",
                    "status": 404,
                },
                status=status.HTTP_404_NOT_FOUND
            )



class SubmitDataUpdate(APIView):
    def patch(self, request, pk):
        try:
            pereval = Added.objects.get(pk=pk)
        except Added.DoesNotExist:
            return Response(
                {"state": 0, "message": "Запись не найдена."},
                status=status.HTTP_404_NOT_FOUND
            )

        if pereval.status != 'new':
            return Response(
                {"state": 0, "message": "Запись нельзя редактировать, так как она не в статусе 'new'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if 'user' in request.data:
            del request.data['user']

        serializer = AddedSerializerUpdate(pereval, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"state": 1, "message": "Запись успешно обновлена."})
        else:
            return Response(
                {"state": 0, "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )