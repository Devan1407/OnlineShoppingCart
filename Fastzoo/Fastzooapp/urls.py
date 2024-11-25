from django.urls import path

from . import views
app_name='Fastzooapp'
urlpatterns = [

    path('',views.allProdCate,name='allProdCate'),
    path('<slug:c_slug>/',views.allProdCate,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatedetail')
]