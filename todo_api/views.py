from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Todo
from .serializers import doSerializers


# Create your views here.
class APIlistView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''

        todos = Todo.objects.filter(user=request.user.id)

        selializers =doSerializers(todos,many=True)
        return Response(selializers.data, status=status.HTTP_200_OK)
    

    # 2. Create
    def post(self,request,*args, **kwargs):
        '''
        Create the Todo with given todo data
        '''

        data ={
            'task': request.data.get('task'),
            'completed': request.data.get('completed'),
            'user': request.data.get('user')
        }
        serializers = doSerializers(data=data)
        if serializers.is_valid():
            serializers.save()

            return Response(serializers.data, status=status.HTTP_201_CREATED)
        
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


