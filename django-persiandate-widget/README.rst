=====
ویدجت ورود تاریخ جلالی در جنگو
=====

در بعضی مواقع مطلوب است که برای کادر ورود اطلاعات تاریخ بدون نیاز به دانش کاربر تاریخ به صورت مطلوب به سرور اطلاع داده شده و ثبت شود، در واقع هدف اصلی ساخت این ویدجت نمایش تاریخ به شکل شمسی و همچنین سازگاری آن با مدل تاریخ های قبلی است، این ویدجت بدین گونه عمل می کند که اطلاعات درون خود را به قالب شمسی به کاربر نمایش می دهد
بدین معنی که در صورتی که از طرف سرور اطلاعات اولیه ای به کادر وارد شود آن اطلاعات از میلادی به شمسی تبدیل می شود
در صورت عدم وجود آن نیز تاریخ امروز نمایش داده می شود

همچنین این ویدجت در حین ثبت داده ی خود نیز دوباره آن را از قالب شمسی به میلادی تبدیل می کند و بدین ترتیب تاریخ در جنگو با فرمت صحیح ذخیره می شود


برای شروع
-----------

1.Install this package from here or python package index::
	
	python -m pip install django-persiandate-widget

2. Add "persiandate-widget" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'persiandate',
    )

3. Include the PersianDateInput in your project forms.py like this::

	from django import forms
    from persiandate.widgets import PersianDateInput
	class my_form(forms.Form)
		...
		my_date = forms.DateField(widget=PersianDateInput())
		...

نیازمندی ها
-----------
1.10<jquery<2


نکات
-----------
Jquery javascript file must be included before the datefield or the widget will not work



