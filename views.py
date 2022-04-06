from math import ceil
from django.shortcuts import render

from website.models import Blogs_Articles, PostClassifiedJob, Vehicles, NFT

# Create your views here.

def Home(request):
    template_name = "website/index.html"
    return render(request, template_name)

def About(request):
    template_name = "website/about.html"
    return render(request, template_name)

def Blog(request):
    template_name = "website/blog.html"
    allblogs=[]
    blogs=Blogs_Articles.objects.all()
    #blogslength=len(blogs)
    #slides=blogslength // 4 + ceil((blogslength / 4) - (blogslength // 4))
    #allblogs.append([blogs,range(1,slides),slides])
    context={'blogs':blogs}
    return render(request, template_name,context)

def Cart(request):
    template_name = "website/cart.html"
    return render(request, template_name)

def Category(request,name):
    categorywiseproduct=[]
    print("yeh name hay",name)
    template_name = "website/category.html"
    brandprod=Vehicles.objects.filter(category__icontains=name)
    print("Yeh all product hain",brandprod)
    brandproductlength=len(brandprod)
    slides=brandproductlength // 4 + ceil((brandproductlength / 4) - (brandproductlength // 4))
    categorywiseproduct.append([brandprod,range(1,slides),slides])
    context={'allproduct':categorywiseproduct}
    return render(request, template_name,context)

def Checkout(request):
    template_name = "website/checkout.html"
    return render(request, template_name)

def Contact(request):
    template_name = "website/contact-2.html"
    return render(request, template_name)

def Faq(request):
    template_name = "website/faq.html"
    return render(request, template_name)

def Jobs(request):
    alljobs=PostClassifiedJob.objects.all()
    context={'alljobs':alljobs}
    template_name = "website/jobs.html"
    return render(request, template_name, context)

def Login(request):
    template_name = "website/login.html"
    return render(request, template_name)

def nft(request):
    template_name = "website/nft.html"
    allnft=NFT.objects.all()
    context={'allnft':allnft}
    return render(request, template_name,context)

def Product_Category(request):
    template_name = "website/product-category.html"
    return render(request, template_name)

def Product(request):
    template_name = "website/product.html"
    return render(request, template_name)

def Single(request):
    #blogdetails=[]
    blogdetails=Blogs_Articles.objects.all()
    # bloglength=len(relatedblog)
    # slides=bloglength//4 + ceil((bloglength / 4) - (bloglength // 4))
    # blogdetails.append([relatedblog,range(1,slides),slides])
    context={'blogdetails':blogdetails}
    template_name = "website/single.html"
    return render(request, template_name,context)

def Wishlist(request):
    template_name = "website/wishlist.html"
    return render(request, template_name)
