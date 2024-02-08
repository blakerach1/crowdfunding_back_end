from rest_framework import serializers
from .models import Project, Pledge, Category


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
        model = Category
        fields = ['title', 'description']


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    categories = serializers.SlugRelatedField(
        many=True,
        queryset=Category.objects.all(),
        slug_field='title',
    )

    class Meta:
        model = Project
        fields = ['owner', 'title', 'description','goal','image', 'is_open', 'date_created', 'categories']


class ProjectDetailSerializer(serializers.ModelSerializer):        
    pledges = PledgeSerializer(many=True, read_only=True, required=False)
    categories = serializers.SlugRelatedField(
        many=True,
        queryset=Category.objects.all(),
        slug_field='title',
    )

    class Meta:
        model = Project
        fields = ['owner', 'title', 'description', 'goal', 'image', 'is_open', 'date_created', 'pledges', 'categories']

    def update(self, instance, validated_data):
        
        instance.categories.clear()
        for category in validated_data['categories']:
            instance.categories.add(category)
        
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
       
        instance.save()

        return instance
        


