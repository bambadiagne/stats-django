from django.urls import path
from . import views
urlpatterns = [
    path('articles', views.all_articles),
    path("import/<str:model_name>",views.import_articles_,name="import_model"),
    path("products",views.all_products)
]
