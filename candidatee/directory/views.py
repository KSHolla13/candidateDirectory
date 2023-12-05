from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serializers import *

# Create your views here.

class  CandidateDirectoryAV(APIView):
    def get(self, request):
        querys = CandidateDirectory.objects.all()
        serializer = CandidateDirectorySerializer(querys, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = CandidateDirectorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class CandidateDirectoryDetailAV(APIView):
    def get(self, request, pk):
        try:
            query = CandidateDirectory.objects.get(pk=pk)
        except CandidateDirectory.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CandidateDirectorySerializer(query,context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        query = CandidateDirectory.objects.get(pk=pk)
        serializer = CandidateDirectorySerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        query =CandidateDirectory.objects.get(pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)