
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from apiapp import views as api_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),
    path('api/token/', TokenObtainPairView.as_view(), name='login'),

    path('listview/', api_views.ListView.as_view(), name="list-view"), 
    path('detailview/<int:classroom_id>/', api_views.DetailView.as_view(), name="details-views"),
    path('view/<int:classroom_id>/update/', api_views.UpdateView.as_view(), name="update-views"),
    path('view/<int:classroom_id>/cancel/', api_views.DeleteClass.as_view(), name="delete-view"),
    path('api/token/', TokenObtainPairView.as_view(), name='login'),
    path('create/<int:classroom_id>/', api_views.CreateView.as_view(), name='create-view'),
]
if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
