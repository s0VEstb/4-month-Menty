from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import HelloView, MainView , FunView, PostListView, PostDetailView, PostCreateView, PostUpdateView, AddReviewView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main_view'),
    path('hello/', HelloView.as_view(), name='hello_view'),
    path('fun/', FunView.as_view(), name='fun_view'),
    path('posts/', PostListView.as_view(), name='post_list_view'),
    path('posts/<int:post_id>/edit/', PostUpdateView.as_view(), name='post_update_view'),
    path('posts/create/', PostCreateView.as_view(), name='post_create_view'),
    path('posts/<int:post_id>/', PostDetailView.as_view(), name='post_detail_view'),
    path('posts/<int:post_id>/add_review/', AddReviewView.as_view(), name='add_review')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
