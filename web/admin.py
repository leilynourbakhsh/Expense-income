from django.contrib import admin
from .models import Expense
from .models import income
from .models import Token
# Register your models here.

admin.site.register(Expense)
admin.site.register(income)
admin.site.register(Token)
