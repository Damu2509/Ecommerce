from django.shortcuts import render, get_object_or_404,redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, ListView

from .models import ItemCategories, ItemDetail

from .forms import RegisterForm

from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin


class CategoryList(ListView):

    model = ItemCategories
    template_name = 'product/item_categories.html'

class ItemDetail(DetailView):
    model = ItemDetail
    template_name = 'product/item_detail.html'

class Item(DetailView):
    model = ItemCategories
    template_name = 'product/items.html'
    paginate_by =2

def itemCategories(request):

    context = { 'fashion':[
         {
        'title' : "Best Sellers",
        'image_url' : "https://m.media-amazon.com/images/I/41TXCe7NGML._AC_SY200_.jpg"
    },
    {
    
            'title' : "Men's Wear",
            'image_url' : "https://images-na.ssl-images-amazon.com/images/G/31/img21/Fashion/Event/SS21Flip/PC_Changes/FinalspotlightScroll/mens_t_shirt._SY530_QL85_.png"
      },
    {
        'title' : "Women's Fashion",
        'image_url' : "https://m.media-amazon.com/images/I/91Nfpvp1yhL._AC_UL320_.jpg"
    },
   ]
    }

    return render(request,'product/items.html', context)



def itemCreate(response):

    if response.method == "POST":

        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect("%i" %t.id)

    else:
        form = CreateNewList()

    return render(response, 'product/items.html', {'form':form})
    
    
def trial(request):

      model = ItemCategories
      template_name="product/sample.html"
    
      context = { 'fashion':[
         {
        'title' : "Best Sellers",
        'image_url' : "https://m.media-amazon.com/images/I/41TXCe7NGML._AC_SY200_.jpg"
    },
    {
    
            'title' : "Men's Wear",
            'image_url' : "https://images-na.ssl-images-amazon.com/images/G/31/img21/Fashion/Event/SS21Flip/PC_Changes/FinalspotlightScroll/mens_t_shirt._SY530_QL85_.png"
      },
    {
        'title' : "Women's Fashion",
        'image_url' : "https://m.media-amazon.com/images/I/91Nfpvp1yhL._AC_UL320_.jpg"
    },
   ]
    }

      return render(request, 'product/sample.html', context)



        

