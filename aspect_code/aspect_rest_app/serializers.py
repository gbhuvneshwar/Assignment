from rest_framework import serializers


class DemoSerializers(serializers.Serializer):
	"Serializers fileds  for testing our APIView"
	name = serializers.CharField(max_length=100)
	job = serializers.CharField(max_length=100)