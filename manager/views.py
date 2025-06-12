from django.shortcuts import render, redirect, get_object_or_404
from manager.models import StoolCategory, StoolManufacturer, StoolMaterial, Stool, StoolCustomer, StoolOrder, StoolOrderItem, StoolReview, StoolNews
from django.urls import reverse
from django.http import HttpResponseBadRequest
from django.utils import timezone
from django.db.models import Q

def manager_home(request):
    return render(request, 'manager/home.html')

# Просмотр списка категорий
def category_list(request):
    categories = StoolCategory.objects.all().order_by('name')
    return render(request, 'manager/category_list.html', {'categories': categories})

# Создание категории
def category_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name:
            StoolCategory.objects.create(name=name, description=description)
            return redirect(reverse('manager:category_list'))
    return render(request, 'manager/category_form.html', {'title': 'Добавить категорию'})

# Редактирование категории
def category_update(request, pk):
    category = get_object_or_404(StoolCategory, pk=pk)
    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.description = request.POST.get('description')
        category.save()
        return redirect(reverse('manager:category_list'))
    return render(request, 'manager/category_form.html', {'category': category, 'title': 'Изменить категорию'})

# Удаление категории
def category_delete(request, pk):
    category = get_object_or_404(StoolCategory, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect(reverse('manager:category_list'))
    return render(request, 'manager/category_confirm_delete.html', {'category': category})

# Просмотр списка производителей
def manufacturer_list(request):
    manufacturers = StoolManufacturer.objects.all().order_by('name')
    return render(request, 'manager/manufacturer_list.html', {'manufacturers': manufacturers})

# Создание производителя
def manufacturer_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        country = request.POST.get('country')
        website = request.POST.get('website')
        if name:
            StoolManufacturer.objects.create(name=name, country=country, website=website)
            return redirect(reverse('manager:manufacturer_list'))
    return render(request, 'manager/manufacturer_form.html', {'title': 'Добавить производителя'})

# Редактирование производителя
def manufacturer_update(request, pk):
    manufacturer = get_object_or_404(StoolManufacturer, pk=pk)
    if request.method == 'POST':
        manufacturer.name = request.POST.get('name')
        manufacturer.country = request.POST.get('country')
        manufacturer.website = request.POST.get('website')
        manufacturer.save()
        return redirect(reverse('manager:manufacturer_list'))
    return render(request, 'manager/manufacturer_form.html', {'manufacturer': manufacturer, 'title': 'Изменить производителя'})

# Удаление производителя
def manufacturer_delete(request, pk):
    manufacturer = get_object_or_404(StoolManufacturer, pk=pk)
    if request.method == 'POST':
        manufacturer.delete()
        return redirect(reverse('manager:manufacturer_list'))
    return render(request, 'manager/manufacturer_confirm_delete.html', {'manufacturer': manufacturer})

# Просмотр списка материалов
def material_list(request):
    materials = StoolMaterial.objects.all().order_by('name')
    return render(request, 'manager/material_list.html', {'materials': materials})

# Создание материала
def material_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name:
            StoolMaterial.objects.create(name=name, description=description)
            return redirect(reverse('manager:material_list'))
    return render(request, 'manager/material_form.html', {'title': 'Добавить материал'})

# Редактирование материала
def material_update(request, pk):
    material = get_object_or_404(StoolMaterial, pk=pk)
    if request.method == 'POST':
        material.name = request.POST.get('name')
        material.description = request.POST.get('description')
        material.save()
        return redirect(reverse('manager:material_list'))
    return render(request, 'manager/material_form.html', {'material': material, 'title': 'Изменить материал'})

# Удаление материала
def material_delete(request, pk):
    material = get_object_or_404(StoolMaterial, pk=pk)
    if request.method == 'POST':
        material.delete()
        return redirect(reverse('manager:material_list'))
    return render(request, 'manager/material_confirm_delete.html', {'material': material})

# Просмотр списка табуреток
def stool_list(request):
    stools = Stool.objects.all()
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort', 'name')
    filter_category = request.GET.get('category')

    if search_query:
        stools = stools.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
        print(f"Search applied: {search_query}, filtered stools: {stools.count()}")  # Отладка
    if filter_category and filter_category != 'all':
        stools = stools.filter(category_id=filter_category)
        print(f"Filter applied: category={filter_category}, filtered stools: {stools.count()}")  # Отладка
    if sort_by in ['name', 'price', 'stock']:
        stools = stools.order_by(sort_by)
        print(f"Sort applied: {sort_by}, count: {stools.count()}")  # Отладка
    elif sort_by == '-price':
        stools = stools.order_by('-price')
        print(f"Sort applied: -price, count: {stools.count()}")  # Отладка

    categories = StoolCategory.objects.all()
    return render(request, 'manager/stool_list.html', {
        'stools': stools,
        'categories': categories,
        'search_query': search_query,
        'sort_by': sort_by,
        'filter_category': filter_category
    })

# Создание табуретки
def stool_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        manufacturer_id = request.POST.get('manufacturer')
        materials = request.POST.getlist('materials')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        description = request.POST.get('description')
        dimensions = request.POST.get('dimensions')
        is_available = request.POST.get('is_available') == 'on'
        if name and category_id and price and stock:
            try:
                stool = Stool.objects.create(
                    name=name,
                    category_id=category_id,
                    manufacturer_id=manufacturer_id,
                    price=price,
                    stock=stock,
                    description=description,
                    dimensions=dimensions,
                    is_available=is_available
                )
                stool.materials.set(materials)
                return redirect(reverse('manager:stool_list'))
            except Exception as e:
                return HttpResponseBadRequest(f"Ошибка при создании: {e}")
    categories = StoolCategory.objects.all()
    manufacturers = StoolManufacturer.objects.all()
    materials = StoolMaterial.objects.all()
    return render(request, 'manager/stool_form.html', {
        'title': 'Добавить табуретку',
        'categories': categories,
        'manufacturers': manufacturers,
        'materials': materials
    })

# Редактирование табуретки
def stool_update(request, pk):
    stool = get_object_or_404(Stool, pk=pk)
    if request.method == 'POST':
        stool.name = request.POST.get('name')
        stool.category_id = request.POST.get('category')
        stool.manufacturer_id = request.POST.get('manufacturer')
        stool.materials.set(request.POST.getlist('materials'))
        stool.price = request.POST.get('price')
        stool.stock = request.POST.get('stock')
        stool.description = request.POST.get('description')
        stool.dimensions = request.POST.get('dimensions')
        stool.is_available = request.POST.get('is_available') == 'on'
        stool.save()
        return redirect(reverse('manager:stool_list'))
    categories = StoolCategory.objects.all()
    manufacturers = StoolManufacturer.objects.all()
    materials = StoolMaterial.objects.all()
    return render(request, 'manager/stool_form.html', {
        'stool': stool,
        'title': 'Изменить табуретку',
        'categories': categories,
        'manufacturers': manufacturers,
        'materials': materials
    })

# Удаление табуретки
def stool_delete(request, pk):
    stool = get_object_or_404(Stool, pk=pk)
    if request.method == 'POST':
        stool.delete()
        return redirect(reverse('manager:stool_list'))
    return render(request, 'manager/stool_confirm_delete.html', {'stool': stool})

# Просмотр списка клиентов
def customer_list(request):
    customers = StoolCustomer.objects.all().order_by('last_name', 'first_name')
    return render(request, 'manager/customer_list.html', {'customers': customers})

# Создание клиента
def customer_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        if first_name and last_name and email:
            try:
                StoolCustomer.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    address=address
                )
                return redirect(reverse('manager:customer_list'))
            except Exception as e:
                return HttpResponseBadRequest(f"Ошибка при создании: {e}")
    return render(request, 'manager/customer_form.html', {'title': 'Добавить клиента'})

# Редактирование клиента
def customer_update(request, pk):
    customer = get_object_or_404(StoolCustomer, pk=pk)
    if request.method == 'POST':
        customer.first_name = request.POST.get('first_name')
        customer.last_name = request.POST.get('last_name')
        customer.email = request.POST.get('email')
        customer.phone = request.POST.get('phone')
        customer.address = request.POST.get('address')
        customer.save()
        return redirect(reverse('manager:customer_list'))
    return render(request, 'manager/customer_form.html', {'customer': customer, 'title': 'Изменить клиента'})

# Удаление клиента
def customer_delete(request, pk):
    customer = get_object_or_404(StoolCustomer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect(reverse('manager:customer_list'))
    return render(request, 'manager/customer_confirm_delete.html', {'customer': customer})

# Просмотр списка заказов
def order_list(request):
    orders = StoolOrder.objects.all().order_by('-created_at')
    return render(request, 'manager/order_list.html', {'orders': orders})

# Создание заказа
def order_create(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer')
        items = request.POST.getlist('items')
        status = request.POST.get('status')
        total_price = request.POST.get('total_price')
        if customer_id and items and total_price:
            try:
                order = StoolOrder.objects.create(
                    customer_id=customer_id,
                    status=status,
                    total_price=total_price
                )
                order.items.set(items)
                return redirect(reverse('manager:order_list'))
            except Exception as e:
                return HttpResponseBadRequest(f"Ошибка при создании: {e}")
    customers = StoolCustomer.objects.all()
    stools = Stool.objects.all()
    return render(request, 'manager/order_form.html', {
        'title': 'Добавить заказ',
        'customers': customers,
        'stools': stools
    })

# Редактирование заказа
def order_update(request, pk):
    order = get_object_or_404(StoolOrder, pk=pk)
    if request.method == 'POST':
        order.customer_id = request.POST.get('customer')
        order.items.set(request.POST.getlist('items'))
        order.status = request.POST.get('status')
        order.total_price = request.POST.get('total_price')
        order.save()
        return redirect(reverse('manager:order_list'))
    customers = StoolCustomer.objects.all()
    stools = Stool.objects.all()
    return render(request, 'manager/order_form.html', {
        'order': order,
        'title': 'Изменить заказ',
        'customers': customers,
        'stools': stools
    })

# Удаление заказа
def order_delete(request, pk):
    order = get_object_or_404(StoolOrder, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect(reverse('manager:order_list'))
    return render(request, 'manager/order_confirm_delete.html', {'order': order})

# Просмотр списка элементов заказов
def order_item_list(request):
    order_items = StoolOrderItem.objects.all().order_by('order__created_at')
    return render(request, 'manager/order_item_list.html', {'order_items': order_items})

# Создание элемента заказа
def order_item_create(request):
    if request.method == 'POST':
        order_id = request.POST.get('order')
        stool_id = request.POST.get('stool')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        if order_id and stool_id and quantity and price:
            try:
                order_item = StoolOrderItem.objects.create(
                    order_id=order_id,
                    stool_id=stool_id,
                    quantity=quantity,
                    price=price
                )
                order = order_item.order
                order.items.add(order_item.stool)
                return redirect(reverse('manager:order_item_list'))
            except Exception as e:
                return HttpResponseBadRequest(f"Ошибка при создании: {e}")
    orders = StoolOrder.objects.all()
    stools = Stool.objects.all()
    return render(request, 'manager/order_item_form.html', {
        'title': 'Добавить элемент заказа',
        'orders': orders,
        'stools': stools
    })

# Редактирование элемента заказа
def order_item_update(request, pk):
    order_item = get_object_or_404(StoolOrderItem, pk=pk)
    if request.method == 'POST':
        order_item.order_id = request.POST.get('order')
        order_item.stool_id = request.POST.get('stool')
        order_item.quantity = request.POST.get('quantity')
        order_item.price = request.POST.get('price')
        order_item.save()
        return redirect(reverse('manager:order_item_list'))
    orders = StoolOrder.objects.all()
    stools = Stool.objects.all()
    return render(request, 'manager/order_item_form.html', {
        'order_item': order_item,
        'title': 'Изменить элемент заказа',
        'orders': orders,
        'stools': stools
    })

# Удаление элемента заказа
def order_item_delete(request, pk):
    order_item = get_object_or_404(StoolOrderItem, pk=pk)
    if request.method == 'POST':
        order = order_item.order
        order.items.remove(order_item.stool)
        order_item.delete()
        return redirect(reverse('manager:order_item_list'))
    return render(request, 'manager/order_item_confirm_delete.html', {'order_item': order_item})

# Просмотр списка отзывов
def review_list(request):
    reviews = StoolReview.objects.all().order_by('-created_at')
    return render(request, 'manager/review_list.html', {'reviews': reviews})

# Создание отзыва
def review_create(request):
    if request.method == 'POST':
        stool_id = request.POST.get('stool')
        customer_id = request.POST.get('customer')
        rating = request.POST.get('rating')
        if stool_id and customer_id and rating:
            try:
                review = StoolReview.objects.create(
                    stool_id=stool_id,
                    customer_id=customer_id,
                    rating=rating
                )
                return redirect(reverse('manager:review_list'))
            except Exception as e:
                return HttpResponseBadRequest(f"Ошибка при создании: {e}")
    stools = Stool.objects.all()
    customers = StoolCustomer.objects.all()
    return render(request, 'manager/review_form.html', {
        'title': 'Добавить отзыв',
        'stools': stools,
        'customers': customers
    })

# Редактирование отзыва
def review_update(request, pk):
    review = get_object_or_404(StoolReview, pk=pk)
    if request.method == 'POST':
        review.stool_id = request.POST.get('stool')
        review.customer_id = request.POST.get('customer')
        review.rating = request.POST.get('rating')
        review.save()
        return redirect(reverse('manager:review_list'))
    stools = Stool.objects.all()
    customers = StoolCustomer.objects.all()
    return render(request, 'manager/review_form.html', {
        'review': review,
        'title': 'Изменить отзыв',
        'stools': stools,
        'customers': customers
    })

# Удаление отзыва
def review_delete(request, pk):
    review = get_object_or_404(StoolReview, pk=pk)
    if request.method == 'POST':
        review.delete()
        return redirect(reverse('manager:review_list'))
    return render(request, 'manager/review_confirm_delete.html', {'review': review})

# Просмотр списка новостей
def news_list(request):
    news_items = StoolNews.objects.all().order_by('-published_at')
    return render(request, 'manager/news_list.html', {'news_items': news_items})

# Создание новости
def news_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            try:
                news = StoolNews.objects.create(
                    title=title,
                    content=content
                )
                return redirect(reverse('manager:news_list'))
            except Exception as e:
                return HttpResponseBadRequest(f"Ошибка при создании: {e}")
    return render(request, 'manager/news_form.html', {'title': 'Добавить новость'})

# Редактирование новости
def news_update(request, pk):
    news = get_object_or_404(StoolNews, pk=pk)
    if request.method == 'POST':
        news.title = request.POST.get('title')
        news.content = request.POST.get('content')
        news.save()
        return redirect(reverse('manager:news_list'))
    return render(request, 'manager/news_form.html', {'news': news, 'title': 'Изменить новость'})

# Удаление новости
def news_delete(request, pk):
    news = get_object_or_404(StoolNews, pk=pk)
    if request.method == 'POST':
        news.delete()
        return redirect(reverse('manager:news_list'))
    return render(request, 'manager/news_confirm_delete.html', {'news': news})