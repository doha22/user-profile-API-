from rest_framework import serializers
from . import models


class helloSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=10)



#for user profile object
class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email','name','password')

        #we want to hide password & password should be write only
        # ### extra_kwargs  that name is required
        extra_kwargs = {'password':{'write_only':True}}

        # create and return new user
        def create(self,validated_data):
            user = models.UserProfile(

                email = validated_data['email'],
                name = validated_data['name']

            )

            user.valiated_password([validated_data['password']])

            #to save data in database
            user.save()

            return user

