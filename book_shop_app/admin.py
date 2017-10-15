from django.contrib import admin
from book_shop_app.models import Customer, Employee, Order, PublishingHouse, Comment, Book, MoreAboutOrder

admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Order)
admin.site.register(PublishingHouse)
admin.site.register(Comment)
admin.site.register(Book)
admin.site.register(MoreAboutOrder)
