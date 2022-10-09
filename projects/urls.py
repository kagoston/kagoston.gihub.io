from django.urls import path
from projects import views

# dynamically generate these URLs depending on the project
urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),

]