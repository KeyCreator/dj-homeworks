from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    context = {}
    has_comment = request.session.get('reviewed_products', [])
    context['is_review_exist'] = has_comment

    if request.method == 'POST':
        # логика для добавления отзыва
        form = ReviewForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.product_id = product.id
            post.save()
            has_comment.append(product.id)
            request.session['reviewed_products'] = has_comment

            return redirect("main_page")
        context['form'] = form
    else:
        context['form'] = ReviewForm

    context['product'] = product

    print("request.session['reviewed_products']=", request.session['reviewed_products'])

    return render(request, template, context)
