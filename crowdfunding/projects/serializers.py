from rest_framework import serializers
from .models import Project, Pledge, Categories


class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')

    class Meta:
        model = Pledge
        fields = ['amount', 'comment', 'anonymous', 'pledge_date', 'project', 'supporter']


class PledgeDetailSerializer(PledgeSerializer):

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.project = validated_data.get('project', instance.project)
        instance.supporter = validated_data.get('supporter', instance.supporter)
        instance.save()
        return instance

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = ['title', 'description']


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ['owner', 'title', 'description','goal','image', 'is_open', 'date_created', 'category']


class ProjectDetailSerializer(serializers.ModelSerializer):        
    pledges = PledgeSerializer(many=True, read_only=True, required=False)
    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ['owner', 'title', 'description', 'goal', 'image', 'is_open', 'date_created', 'pledges', 'category']

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
        


