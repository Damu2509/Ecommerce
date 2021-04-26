from django.urls import path,include 
from .views import(
    product_detail_view,
    product_create_view,
    raw_create_view,
    product_delete_view,
    product_list_view,

    functiondetailview,
    ProductRawList,
    Inherited,
    
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductDeleteView,)

app_name = 'product'

urlpatterns = [ 
    path('detail/<int:id>/', product_detail_view, name = 'detail'),
    path('create/', product_create_view, name = 'create'),
    path('raw-form/', raw_create_view, name = 'raw-form'),

    path('delete/<int:id>/', product_delete_view, name = 'delete-view'),
    path('list/', product_list_view, name = 'list-view'),



    path('classview/', ProductListView.as_view(), name = 'ProductListViews'),
    path('detailview/<int:id>/', ProductDetailView.as_view(), name = 'ProductDetailViews'),
    path('createview/', ProductCreateView.as_view(), name = 'ProductCreateViews'),
    path('deleteview/<int:id>/', ProductDeleteView.as_view(), name = 'ProductDeleteViews'),
    path('<int:id>/', functiondetailview.as_view(template_name = 'product/product_detail.html'), name = 'functionbasediews'),
    path('raw/', ProductRawList.as_view(template_name = 'product/product_list.html'), name = 'functionbasediews'),
    path('inherited/', Inherited.as_view(), name = 'ProductListViews'),




]