from rest_framework import serializers
from .models import Project, Pledge


class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')

    class Meta:
        model = Pledge
        fields = '__all__'


class PledgeDetailSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')

    class Meta:
        model = Pledge
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.amount = validated_data('amount', instance.amount)
        instance.comment = validated_data('comment', instance.comment)
        instance.anonymous = validated_data('anonymous', instance.anonymous)
        instance.project_id = validated_data('project_id', instance.project_id)
        instance.supporter_id = validated_data('supporter_id', instance.supporter_id)
        instance.save()
        return instance


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Project
        fields = '__all__'


class ProjectDetailSerializer(ProjectSerializer):        
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance
