from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Tables
from .serializers import TableSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def tables_list(request):
    if request.method == 'GET':
        spreadsheet = Tables.objects.all()

        posts = request.GET.get('post', None)
        if posts is not None:
            spreadsheet = spreadsheet.filter(
                spreadsheet__icontains=spreadsheet)

        spreadsheet_serializer = TableSerializer(spreadsheet, many=True)
        return JsonResponse(spreadsheet_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    elif request.method == 'POST':
        spreadsheet_data = JSONParser().parse(request)
        spreadsheet_serializer = TableSerializer(data=spreadsheet_data)
        if spreadsheet_serializer.is_valid():
            spreadsheet_serializer.save()
            return JsonResponse(spreadsheet_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(spreadsheet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Tables.objects.all().delete()
        return JsonResponse({'message': '{} Tables were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def table_detail(request, pk):
    # find tutorial by pk (id)
    try:
        spreadsheet = Tables.objects.get(pk=pk)
    except Tables.DoesNotExist:
        return JsonResponse({'message': 'The table does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        spreadsheet_serializer = TableSerializer(spreadsheet)
        return JsonResponse(spreadsheet_serializer.data)

    elif request.method == 'PUT':
        spreadsheet_data = JSONParser().parse(request)
        spreadsheet_serializer = TableSerializer(
            spreadsheet, data=spreadsheet_data)
        if spreadsheet_serializer.is_valid():
            spreadsheet_serializer.save()
            return JsonResponse(spreadsheet_serializer.data)
        return JsonResponse(spreadsheet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        spreadsheet.delete()
        return JsonResponse({'message': 'Table was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
