from django.shortcuts import render


from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

# status import http reponse status code
from rest_framework import status

from rest_framework.authentication import  TokenAuthentication
from rest_framework import filters

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import models
from . import serializers

from . import permission
# Create your views here.

class HelloApiView(APIView):


    serializer_class = serializers.helloSerializer

    def get(self , request , format = None):
        # return list of  apiview features

# uses http methods as (get , post , patch , put , delete)

        #this an_apiview will return these features inside it
        an_apiview = [

            'uses http methods as (get , post , patch , put , delete)' ,
            'similar to django view',
            'mapped manually to URLS'
        ]

    # returns json of that an_apiview
        return Response({'message':'hello!', 'an_apiview': an_apiview})




  # create post function which get the requested data and show it
    def post(self , request):
        """ create message using name """
        serializer = serializers.helloSerializer(data = request.data)


        # validate the data :
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)

            #return message with name in json format ## IN RESPONSE OBJ
            return Response({'message': message})
        # if data not valid
        else:

            # HTTP_400_BAD_REQUEST is standard statues code for bad request
            return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)


# updating the objects
    def put(self ,request, pk = None):
        """ handle updating the objects """

        return Response({'method ': 'put'})


 # patch : update only fields which provided in the request

    def patch(self , request , pk = None ):
        """ update only fields which provided in the request"""
        return Response({'method':'patch'})



    def delete(self, request , pk = None):
        """ delete objects """
        return Response ({'method': 'delete'})

############################################################################################################################
# USING VIEWSET which make interface of API with backend

class helloViewSet(viewsets.ViewSet):

    serializer_class = serializers.helloSerializer


  # LIST ALL OF OBJS IN SYSTEM as get method
    def list(self,request):

        #return hello message
        a_view =[
            'users actions (list ,create , retieve , update , partial_update )',
            'automaically maps urls using routers '
        ]

        return Response({'message':'hello !!!', 'a_viewset':a_view})

    ## write create fn as post method
    def create(self,request):
        """ create message """

        serializer = serializers.helloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'hello {0}'.format(name)

            return Response({'message':message})
        else:
            return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)


# retrieve fn get specific obj by id as db
# retrive fn as get in http method

    def retrieve(self,request , pk=None):
        """ getting obj by its id """
        return Response({'HTTP method':'GET'})


# update fn as put in http method

    def update(self,request,pk= None):
        """ updating objects"""

        return Response({'HTTP method':'PUT'})


# partial_update fn as patch in http method
    def partial_update(self,request,pk = None):
        """ updating part of object"""

        return Response({'HTTP method':'PATCH'})

#destroy fn as delete in http method
    def destroy(self,request ,pk=None):
        """ removing an objedct"""
        return Response({'HTTP method':'DELETE'})






class  UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer

    #list all objects from database
    queryset = models.UserProfile.objects.all()

    #make authenticaion , using one token authentication
    # , MEANS TUPLE
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permission.UpdateOwnProfile,)

    # make search
    # make tuple
    filter_backends = (filters.SearchFilter,)
    # allow user search by name , email
    search_fields = ('name','email',)


# login class
class loginViewSet(viewsets.ViewSet):
    """ check email , password and return authenticated token"""
    serializer_class =AuthTokenSerializer

    # make create fn (http post)
    def create(self,request):

        #call post fn
        return ObtainAuthToken().post(request)