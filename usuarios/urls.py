from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from usuarios.views import router as my_router



api = NinjaAPI()

api.add_router("/api/",my_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api.urls),

]