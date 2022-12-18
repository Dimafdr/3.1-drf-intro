from rest_framework import generics
from .models import Project, Measurement
from .serializers import ProjectSerializer, MeasurementSerializer, ProjectDetailSerializer



class ProjectCreate(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectUpdate(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectMeasurement(generics.ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectRetrieve(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer


