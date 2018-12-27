from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    '''
    serializes a name field for testing our APIView
    Django rest_framework provides many predefined fields, which we will use
    '''
    name = serializers.CharField(max_length=10)
    #this max_length is a required attribute and set to 10, thus
    #if there are more than 10 characters, it will provide an error
