from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'main'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('post_detail/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
   # path('tag_detail/<int:pk>/', views.TagDetail.as_view(), name='tag_detail'),
    path('add_comment/<int:pk>/', views.AddComment.as_view(), name='add_comment'),
    path('post_create/', views.PostCreate.as_view(), name='post_create'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

