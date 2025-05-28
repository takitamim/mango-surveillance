from django.urls import path
from . import views

app_name = 'surveillance'

urlpatterns = [
    path('', views.home, name='home'),
    path('growers/', views.GrowerListView.as_view(), name='grower_list'),
    path('growers/create/', views.GrowerCreateView.as_view(), name='grower_create'),
    path('growers/<int:pk>/', views.GrowerDetailView.as_view(), name='grower_detail'),
    path('growers/<int:pk>/edit/', views.GrowerUpdateView.as_view(), name='grower_update'),
    path('growers/<int:pk>/delete/', views.GrowerDeleteView.as_view(), name='grower_delete'),
    path('plants/', views.PlantListView.as_view(), name='plant_list'),
    path('plants/create/', views.PlantCreateView.as_view(), name='plant_create'),
    path('plants/<int:pk>/', views.PlantDetailView.as_view(), name='plant_detail'),
    path('plants/<int:pk>/edit/', views.PlantUpdateView.as_view(), name='plant_update'),
    path('plants/<int:pk>/delete/', views.PlantDeleteView.as_view(), name='plant_delete'),
    path('records/', views.RecordListView.as_view(), name='record_list'),
    path('records/create/', views.RecordCreateView.as_view(), name='record_create'),
    path('records/<int:pk>/', views.RecordDetailView.as_view(), name='record_detail'),
    path('records/<int:pk>/edit/', views.RecordUpdateView.as_view(), name='record_update'),
    path('records/<int:pk>/delete/', views.RecordDeleteView.as_view(), name='record_delete'),
]