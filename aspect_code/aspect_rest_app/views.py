from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from aspect_rest_app import serializers

import requests

class DemoApiView(APIView):
    """access all demo method from demo site (https://reqres.in/)"""

    serializer_class = serializers.DemoSerializers

    def get(self, request, pk=None):
        """Return a list of DemoAPIView features"""
        
        base_url = "https://reqres.in"
        follwing_url = request.get_full_path()

        final_url = base_url + follwing_url
        
        resp = requests.get(final_url)
        an_api_view = resp.json()
        status_code = resp.status_code

        return Response({"status": status_code, "Response": an_api_view})


    def post(self, request, pk=None):

        serializer = self.serializer_class(data=request.data)

        base_url = "https://reqres.in"
        follwing_url = request.get_full_path()

        final_url = base_url + follwing_url

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            job = serializer.validated_data.get('job')
            resp = requests.post(final_url, request.data)
            status_code = resp.status_code
            post_data = resp.json()
            return Response({'status':status_code, "post_data": post_data})

        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
                )


    def put(self, request, pk=None):
        """Handling updating object"""
        serializer = self.serializer_class(data=request.data)

        base_url = "https://reqres.in"
        follwing_url = request.get_full_path()

        final_url = base_url + follwing_url

        if serializer.is_valid():            
            resp = requests.put(final_url, serializer.validated_data)
            status_code = resp.status_code
            updated_data = resp.json()
            return Response({'status':status_code, "updated_data": updated_data})            
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
                )


    def patch(self, request, pk=None):
        """Handling partilly update in object"""

        serializer = self.serializer_class(data=request.data)
        base_url = "https://reqres.in"
        follwing_url = request.get_full_path()

        final_url = base_url + follwing_url

        if serializer.is_valid():            
            resp = requests.put(final_url, serializer.validated_data)
            status_code = resp.status_code
            partially_updated_data = resp.json()
            return Response({'status':status_code, "partially_updated_data": partially_updated_data})
            
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
                )

    def delete(self, request, pk=None):

        base_url = "https://reqres.in"
        follwing_url = request.get_full_path()
        final_url = base_url + follwing_url
        deleted_obj = requests.delete(final_url)

        return Response({'status' : deleted_obj.status_code})


class RegisterApi(APIView):
    "register check here"
    
    def post(self, request):

        base_url = "https://reqres.in"
        follwing_url = request.get_full_path()
        final_url = base_url + follwing_url               


        resp = requests.post(final_url, request.data)
        status_code = resp.status_code
        post_data = resp.json()
        return Response({'status':status_code, "post_data": post_data})


class LoginApi(APIView):
    "login check here"
    
    def post(self, request):

        base_url = "https://reqres.in"
        follwing_url = request.get_full_path()
        final_url = base_url + follwing_url               


        resp = requests.post(final_url, request.data)
        status_code = resp.status_code
        post_data = resp.json()
        return Response({'status':status_code, "post_data": post_data})


