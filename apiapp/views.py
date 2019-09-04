from django.shortcuts import render
from classes.models import Classroom
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from .serializers import ListViewSerializer, DetailViewSerializer, CreateSerializer, UpdateViewSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

class ListView(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ListViewSerializer


class DetailView(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = DetailViewSerializer

class CreateView(CreateAPIView):
	serializer_class = CreateSerializer
	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)

class UpdateView(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = UpdateViewSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class DeleteClass(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'