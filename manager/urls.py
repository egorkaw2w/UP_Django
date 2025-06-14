from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('', views.manager_home, name='manager_home'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/update/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('manufacturers/', views.manufacturer_list, name='manufacturer_list'),
    path('manufacturers/create/', views.manufacturer_create, name='manufacturer_create'),
    path('manufacturers/<int:pk>/update/', views.manufacturer_update, name='manufacturer_update'),
    path('manufacturers/<int:pk>/delete/', views.manufacturer_delete, name='manufacturer_delete'),
    path('materials/', views.material_list, name='material_list'),
    path('materials/create/', views.material_create, name='material_create'),
    path('materials/<int:pk>/update/', views.material_update, name='material_update'),
    path('materials/<int:pk>/delete/', views.material_delete, name='material_delete'),
    path('stools/', views.stool_list, name='stool_list'),
    path('stools/create/', views.stool_create, name='stool_create'),
    path('stools/<int:pk>/update/', views.stool_update, name='stool_update'),
    path('stools/<int:pk>/delete/', views.stool_delete, name='stool_delete'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/create/', views.customer_create, name='customer_create'),
    path('customers/<int:pk>/update/', views.customer_update, name='customer_update'),
    path('customers/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/<int:pk>/update/', views.order_update, name='order_update'),
    path('orders/<int:pk>/delete/', views.order_delete, name='order_delete'),
    path('order-items/', views.order_item_list, name='order_item_list'),
    path('order-items/create/', views.order_item_create, name='order_item_create'),
    path('order-items/<int:pk>/update/', views.order_item_update, name='order_item_update'),
    path('order-items/<int:pk>/delete/', views.order_item_delete, name='order_item_delete'),
    path('reviews/', views.review_list, name='review_list'),
    path('reviews/create/', views.review_create, name='review_create'),
    path('reviews/<int:pk>/update/', views.review_update, name='review_update'),
    path('reviews/<int:pk>/delete/', views.review_delete, name='review_delete'),
    path('news/', views.news_list, name='news_list'),
    path('news/create/', views.news_create, name='news_create'),
    path('news/<int:pk>/update/', views.news_update, name='news_update'),
    path('news/<int:pk>/delete/', views.news_delete, name='news_delete'),
]