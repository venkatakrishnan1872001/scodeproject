from django.shortcuts import render

# Create your views here.


from .serializers import (BlogSerializer,ScodedetailSerializer)

from .models import (Blog,Scodedetail)

from django.shortcuts import render

# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
import ast
import copy
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets


#############################   blog List   #########################################

class BlogList(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        response_data = {
            "success": "true",
            "message": "BlogList retrieved successfully",
            "SpecificationList": serializer.data,
        }
        return Response(response_data)


##########################################   end code ######################################


#######################################  blog by id #######################################3

class BlogDetailbyID(generics.RetrieveAPIView):
    serializer_class = BlogSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            blog_id = request.query_params.get('blog_id')
            blogInstance = Blog.objects.get(id=blog_id)

            if not blog_id:
                return Response({"success":"false","message":"id field is required"})

            blog_serializer = self.serializer_class(blogInstance)

            response_data = {
                'success': 'true',
                'message': 'Blog details retrieved successfully.',
                'response': {
                    **blog_serializer.data,
                        
                }
            }

        except Blog.DoesNotExist:
            return Response({"success":"false","message":"blog not exist"})

        return Response(response_data)
    

    ##########################################  end code  ##########################################
    

    
###############################################   service list  #####################################

from rest_framework.pagination import PageNumberPagination

class ScodeServiceList(generics.ListAPIView):
    queryset = Scodedetail.objects.all()
    #queryset = Scodedetail.objects.exclude(para='')
    serializer_class = ScodedetailSerializer

    pagination_class = PageNumberPagination

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        response_data = {
            "success": "true",
            "message": "Scode service details retrieved successfully",
            "ScodeDetail": serializer.data,
        }
        return Response(response_data)
    


####################################################   end code  #######################################