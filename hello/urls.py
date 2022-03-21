from django.urls import path
from . import views
from .views import FriendList, FriendDetail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('list', FriendList.as_view()),
    path('detail/<int:pk>', FriendDetail.as_view()),
    path('find', views.find, name="find"),
]

urlpatterns += static(settings.MEDIA_URL, document_ROOT=settings.MEDIA_ROOT)