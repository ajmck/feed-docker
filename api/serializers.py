from core.models import Post, Comment, Meshblock
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class MeshblockSerializer(GeoFeatureModelSerializer):
    total_upvotes = serializers.IntegerField(read_only=True)
    total_downvotes = serializers.IntegerField(read_only=True)
    vote_total = serializers.IntegerField(read_only=True)
    name_or_id = serializers.StringRelatedField(read_only=True)
    count_posts = serializers.IntegerField(read_only=True)
    score_cell = serializers.FloatField(read_only=True)

    class Meta:
        model = Meshblock
        geo_field = "geom"
        fields = "__all__"


class PostSerializer(serializers.HyperlinkedModelSerializer):
    total_upvotes = serializers.IntegerField(read_only=True)
    total_downvotes = serializers.IntegerField(read_only=True)
    vote_total = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        # exclude = ['moderation']

    def create(self, validated_data):
        return Post.objects.create(**validated_data)


class PostGeoJsonSerializer(GeoFeatureModelSerializer):
    total_upvotes = serializers.IntegerField(read_only=True)
    total_downvotes = serializers.IntegerField(read_only=True)
    vote_total = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        geo_field = "post_location"
        fields = '__all__'
