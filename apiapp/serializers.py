from rest_framework import serializers
from classes.models import Classroom
class ListViewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['subject', 'year', 'teacher']


class DetailViewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = '__all__'

class CreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		exclude = ['teacher']

class UpdateViewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = '__all__'