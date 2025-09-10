from rest_framework import serializers
from .models import Profile, Project, Work, Skill, Link

class SkillSerializer(serializers.ModelSerializer):
    class Meta: model = Skill; fields = ["id","name"]

class LinkSerializer(serializers.ModelSerializer):
    class Meta: model = Link; fields = ["github","linkedin","portfolio"]

class ProjectSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    skill_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, source="skills", queryset=Skill.objects.all()
    )
    class Meta: model = Project; fields = ["id","title","description","links","skills","skill_ids"]

class WorkSerializer(serializers.ModelSerializer):
    class Meta: model = Work; fields = ["id","company","role","start","end","description"]

class ProfileSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    skill_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, source="skills", queryset=Skill.objects.all(), required=False
    )
    links = LinkSerializer()
    work = WorkSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ["id","name","email","education","skills","skill_ids","links","work"]

    def create(self, validated_data):
        links_data = validated_data.pop("links", {})
        link = Link.objects.create(**links_data) if links_data else None
        skills = validated_data.pop("skills", [])
        profile = Profile.objects.create(links=link, **validated_data)
        if skills: profile.skills.set(skills)
        return profile

    def update(self, instance, validated_data):
        links_data = validated_data.pop("links", None)
        skills = validated_data.pop("skills", None)
        for attr, val in validated_data.items(): setattr(instance, attr, val)
        if links_data:
            if instance.links: 
                for a,v in links_data.items(): setattr(instance.links, a, v)
                instance.links.save()
            else:
                instance.links = Link.objects.create(**links_data)
        if skills is not None: instance.skills.set(skills)
        instance.save()
        return instance
