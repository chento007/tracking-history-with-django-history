
from django.urls import path, include
from watchlist_app.api.views import (ReviewDetail,ReviewList,ReviewCreate,StreamPlatformVS,TrackHistory)
from rest_framework.routers import DefaultRouter
from rest_framework import permissions

router = DefaultRouter()

router.register('stream', StreamPlatformVS,basename="streamplatform")





urlpatterns =   [

    path("",include(router.urls)),


    path("stream/<int:pk>/review-create", ReviewCreate.as_view(),name="review-create"),
    path("stream/", ReviewList.as_view(), name="stream"),
    path('stream/<int:pk>/review', ReviewDetail.as_view(), name='streamplatform-detail'),
    path('history/<int:pk>', TrackHistory.as_view(), name='history-detail'),
    path('history/', TrackHistory.as_view(), name='history-list'),



    # path("list/", WatchListAV.as_view(), name="movie-list"),
    # path("detail/<int:pk>/", WatchDetail.as_view(), name="movie-detail"),
    # path("review/",ReviewList.as_view(),name="review-list"),
    # path("review/<int:pk>/",ReviewDetail.as_view(),name="review-detail"),
]
