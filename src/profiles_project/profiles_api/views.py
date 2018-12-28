from django.shortcuts import render
from rest_framework import viewsets   ##viewsets here to work w DB
from rest_framework.views import APIView ##APIView to work with Frontend
from rest_framework.response import Response
from . import serializers
from rest_framework import status

# Create your views here.

class HelloApiView(APIView):
    """Test API View."""


    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}!'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        '''
        handle updating objects
        pk stands for primary key in DB
        '''
        return Response({"method":"put"})
    def patch(self, request, pk=None):
        '''
        patch partially updates an objects
        only updates certain fields that are required within the request
        '''
        return Response({"method":"patch"})
    def delete(self, request, pk=None):

        return Response({"method":"delete"})

##############################################################
class HelloViewSet(viewsets.ViewSet):
    '''
    Test API Viewsets:
    Their names are not traditional HTTP API names, more CRUD
    '''
    def list(self, request):
        '''
        returns a hello message
        '''
        a_viewset = [
        'Uses actions (list, create, retrieve, update, partial_update)'
        'Automatically maps to URLS using Routers',
        'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
