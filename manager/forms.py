# from django import forms
# from manager.models import StoolCategory, StoolManufacturer, StoolMaterial, Stool, StoolCustomer, StoolOrder, StoolOrderItem, StoolReview
#
# class StoolCategoryForm(forms.ModelForm):
#     class Meta:
#         model = StoolCategory
#         fields = ['name', 'description']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
#         }
#         labels = {
#             'name': 'Название категории',
#             'description': 'Описание',
#         }
#
# class StoolManufacturerForm(forms.ModelForm):
#     class Meta:
#         model = StoolManufacturer
#         fields = ['name', 'country', 'website']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'country': forms.TextInput(attrs={'class': 'form-control'}),
#             'website': forms.URLInput(attrs={'class': 'form-control'}),
#         }
#         labels = {
#             'name': 'Название производителя',
#             'country': 'Страна',
#             'website': 'Веб-сайт',
#         }
#
# class StoolMaterialForm(forms.ModelForm):
#     class Meta:
#         model = StoolMaterial
#         fields = ['name', 'description']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
#         }
#         labels = {
#             'name': 'Название материала',
#             'description': 'Описание',
#         }
#
# class StoolForm(forms.ModelForm):
#     class Meta:
#         model = Stool
#         fields = ['name', 'category', 'manufacturer', 'materials', 'price', 'stock', 'description', 'dimensions', 'is_available', 'image']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'category': forms.Select(attrs={'class': 'form-control'}),
#             'manufacturer': forms.Select(attrs={'class': 'form-control'}),
#             'materials': forms.SelectMultiple(attrs={'class': 'form-control'}),
#             'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
#             'stock': forms.NumberInput(attrs={'class': 'form-control'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
#             'dimensions': forms.TextInput(attrs={'class': 'form-control'}),
#             'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#             'image': forms.FileInput(attrs={'class': 'form-control'}),
#         }
#         labels = {
#             'name': 'Название табуретки',
#             'category': 'Категория',
#             'manufacturer': 'Производитель',
#             'materials': 'Материалы',
#             'price': 'Цена',
#             'stock': 'Количество на складе',
#             'description': 'Описание',
#             'dimensions': 'Размеры (ДxШxВ)',
#             'is_available': 'В наличии',
#         }
#
# class StoolCustomerForm(forms.ModelForm):
#     class Meta:
#         model = StoolCustomer
#         fields = ['first_name', 'last_name', 'email', 'phone', 'address']
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'phone': forms.TextInput(attrs={'class': 'form-control'}),
#             'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
#         }
#         labels = {
#             'first_name': 'Имя',
#             'last_name': 'Фамилия',
#             'email': 'Email',
#             'phone': 'Телефон',
#             'address': 'Адрес',
#         }
#
# class StoolOrderForm(forms.ModelForm):
#     class Meta:
#         model = StoolOrder
#         fields = ['customer', 'status']
#         widgets = {
#             'customer': forms.Select(attrs={'class': 'form-control'}),
#             'status': forms.Select(attrs={'class': 'form-control'}),
#         }
#         labels = {
#             'customer': 'Клиент',
#             'status': 'Статус',
#         }
#
# class StoolOrderItemForm(forms.ModelForm):
#     class Meta:
#         model = StoolOrderItem
#         fields = ['order', 'stool', 'quantity', 'price']
#         widgets = {
#             'order': forms.Select(attrs={'class': 'form-control'}),
#             'stool': forms.Select(attrs={'class': 'form-control'}),
#             'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
#             'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
#         }
#         labels = {
#             'order': 'Заказ',
#             'stool': 'Табуретка',
#             'quantity': 'Количество',
#             'price': 'Цена за единицу',
#         }
#
# class StoolReviewForm(forms.ModelForm):
#     class Meta:
#         model = StoolReview
#         fields = ['stool', 'customer', 'rating', 'comment']
#         widgets = {
#             'stool': forms.Select(attrs={'class': 'form-control'}),
#             'customer': forms.Select(attrs={'class': 'form-control'}),
#             'rating': forms.Select(attrs={'class': 'form-control'}),
#             'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
#         }
#         labels = {
#             'stool': 'Табуретка',
#             'customer': 'Клиент',
#             'rating': 'Рейтинг (1-5)',
#             'comment': 'Комментарий',
#         }