from django.contrib import admin
from watchlist_app.models import WatchList,StreamPlatform,User,Review
from watchlist_app.model_history import History
# Register your models here.
admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Review)
admin.site.register(History)