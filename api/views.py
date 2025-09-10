from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.db.models import Count
from .models import Profile, Project, Work, Skill
from .serializers import ProfileSerializer, ProjectSerializer, WorkSerializer, SkillSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().prefetch_related("skills")
    serializer_class = ProjectSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        skill = self.request.query_params.get("skill")
        if skill:
            qs = qs.filter(skills__name__iexact=skill)
        return qs

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    @action(detail=False, methods=["get"])
    def top(self, request):
        top_qs = Skill.objects.annotate(pcount=Count("projects")).order_by("-pcount")[:10]
        return Response(SkillSerializer(top_qs, many=True).data)

@api_view(["GET"])
def health(request): return Response({"status":"ok"})
