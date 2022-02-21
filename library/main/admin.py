from django.contrib.admin import *
from .models import *
# Register your models here.

@register(Book)
class BookAdmin(ModelAdmin):
    pass
@register(Cover)
class CoverAdmin(ModelAdmin):
    pass
@register(Author)
class AuthorAdmin(ModelAdmin):
    pass