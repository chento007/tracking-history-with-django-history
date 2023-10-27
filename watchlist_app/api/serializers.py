from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.model_history import History


class HistoricalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = History.history.model
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"



class ReviewSerializer(serializers.ModelSerializer):

    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('watchlist',)


class WatchListSerializer(serializers.ModelSerializer):

    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):

    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"
    
    
    # watchlist = serializers.StringRelatedField(many=True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie-detail',
    #     lookup_field='id'
    # )
