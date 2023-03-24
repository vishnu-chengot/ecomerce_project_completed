from django.shortcuts import render
from .serializer import StudentSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from .models import Student

# Create your views here.
@api_view(['POST'])
def add_student(request):
    
    params = request.data
    serialized_data = StudentSerializer(data = params)
    if serialized_data.is_valid():
        serialized_data.save()
        status_code = 201
        msg = 'student added'
        
    else:
        status_code = 403
        msg = 'Form error'

    context = {
        'message':msg,
        'statuscode':status_code
    }
    return Response(context)
    
@api_view(['GET'])    
def view_student(request):
    stud = Student.objects.all()
    serialized_data = StudentSerializer(stud,many = True)
    return Response({'student_list':serialized_data.data})

@api_view(['DELETE'])  
def delete_student(request,sid):
    try:
        stud = Student.objects.get(id = sid)
        stud.delete()
        msg = 'deleted'
    except:
        msg = 'Student not found'

    return Response({'message',msg})

@api_view(['PUT'])
def update_student(request,sid):
    params = request.data
    try:
        stud = Student.objects.get(id = sid)
        serialized_data = StudentSerializer(stud,data = params)
        if serialized_data.is_valid():
            serialized_data.save()
            msg = 'updated'
    except:
        msg = 'student not found'
    return Response({'message':msg})
