from django.conf.urls import patterns, url , include
from rest_framework_nested import routers
from views import CategoryViewSet , SubcategoryViewSet




router = routers.SimpleRouter()
router.register(r'category',CategoryViewSet)
router.register(r'subcategory',SubcategoryViewSet)



urlpatterns = [

		url(r'^',include(router.urls)),
		
]