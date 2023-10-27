from watchlist_app.models import (WatchList, StreamPlatform, Review)
from rest_framework.decorators import api_view
from watchlist_app.api.serializers import (
    WatchListSerializer, StreamPlatformSerializer, ReviewSerializer,HistorySerializer,HistoricalRecordSerializer)
from watchlist_app.model_history import History


from watchlist_app.api.permissions import AdminOrReadOnly,ReviewUserOrReadOnly

from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from django.shortcuts import get_object_or_404

class TrackHistory(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HistorySerializer

    def get_queryset(self):
        # Adjust the query below to match your use case
        return History.objects.all()
    
    def retrieve(self, request, *args, **kwargs):

        instance = self.get_object()  # Get the model instance
        history = instance.history.all()  # Now you can access the history attribute
        serializer = HistoricalRecordSerializer(history, many=True)  # Serialize the historical records with the new serializer
        return Response(serializer.data)  # Return the serialized data



class StreamPlatformVS(viewsets.ViewSet):

    def list(self, request):

        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(
            queryset, many=True, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        queryset = StreamPlatform.objects.all()
        watchlist = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(
            watchlist, context={'request': request})
        return Response(serializer.data)

    def create(self, request):

        serilizer = StreamPlatformSerializer(data=request.data)

        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

# create review base on specified movie with generic


class ReviewCreate(generics.CreateAPIView):

    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):

        pk = self.kwargs.get('pkf')
        watchlist = WatchList.objects.get(pk=pk)

        review_user = self.request.user
        
        review_queryset = Review.objects.filter(
            watchlist=WatchList, review_user=review_user)

        if review_queryset.exists:
            raise ValidationError("You have already reviewed this watchlist")

        serializer.save(watchlist=watchlist, review_user=review_user)

        return super().perform_create(serializer)


# get review list with generic
class ReviewList(generics.ListCreateAPIView):

    serializer_class = ReviewSerializer
    
    permission_classes =[AdminOrReadOnly]


    def get_queryset(self):
        
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

# get review detail by id with generic


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Review.objects.all() 

    serializer_class = ReviewSerializer

    permission_classes=[ReviewUserOrReadOnly]

# class ReviewDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class StramPlatformAV(APIView):

#     def get(self, request):

#         platform = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(
#             platform, many=True, context={'request': request})
#         return Response(serializer.data)


# class StreamPlatformDetail(APIView):

#     def get(self, request, pk):
#         try:
#             platform = StreamPlatform.objects.get(pk=pk)
#         except StreamPlatform.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         serializer = StreamPlatformSerializer(
#             platform, context={'request': request})
#         return Response(serializer.data)

#     # Add other methods (e.g., put, delete) if needed.


# class WatchListAV(APIView):

#     def get(self, request):

#         watches = WatchList.objects.all()

#         serializer = WatchListSerializer(watches, many=True)

#         return Response(serializer.data)

#     def post(self, request):

#         serializer = WatchListSerializer(data=request.data)

#         if serializer.is_valid():

#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         else:

#             return Response(serializer.errors, status=400)


# class WatchDetail(APIView):

#     def get(self, request, pk):

#         try:
#             watchList = WatchList.objects.get(pk=pk)
#         except WatchList.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         serializer = WatchListSerializer(watchList)
#         return Response(serializer.data)

#     def put(self, request, pk):

#         try:

#             watchList = WatchList.objects.get(pk=pk)
#             serializer = WatchListSerializer(watchList, data=request.data)

#             if serializer.is_valid():

#                 serializer.save(pk=pk)
#                 return Response(serializer.data)

#             else:

#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTff)
#         except WatchList.DoesNotExist:

#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, pk):
#         try:
#             watchList = WatchList.objects.get(pk=pk)
#             watchList.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except WatchList.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
