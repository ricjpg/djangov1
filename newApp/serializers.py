from rest_framework import serializers
from newApp.models import Users



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('userID',
                  'usarName',
                  'email',
                  'phone',
                  'address',
                  'gender'
                  )