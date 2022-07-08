from django.contrib import admin, messages
from django.contrib.auth.models import User
from .models import Movie, Director, Actor
from django.db.models import QuerySet
# Register your models here.

# admin.site.register(Director)
admin.site.register(Actor)

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('first_name', )}

class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating' 

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 79', 'Высокий'),
            ('>=80', 'Выысочайший'),
        ]

    def queryset(self, request, queryset):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'от 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        if self.value() == 'от 60 до 79':
            return queryset.filter(rating__gte=60).filter(rating__lt=80)
        if self.value() == '>=80':
            return queryset.filter(rating__gt=80)
        return queryset

@admin.register(Movie)

class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ['name', 'director', 'rating', 'year', 'budget', 'slug', 'rating_ststus']
    list_editable = ['director', 'rating', 'year', 'budget']
    ordering = ['-rating'] #сортировка
    filter_horizontal = ['actors']
    list_per_page = 10      #отобраение на каждом странице
    actions = ['set_dollars', 'set_euro']
    search_fields = ['name', 'rating']  #__startswith будет искать по 
    list_filter =  ['name', 'currency', RatingFilter, 'year']
 
    @admin.display(ordering='rating', description='Статус')
    def rating_ststus(self, mov: Movie):
        if mov.rating < 50:
            return 'Хуйня'
        if mov.rating < 70:
            return 'Разок можно глянуть'
        if mov.rating <= 85:
            return 'зачет'
        return 'Топ'

    @admin.action(description='Установить валюту в доллар')
    def set_dollars(self, request, qr: QuerySet):
        count_update = qr.update(currency=Movie.USD)
        self.message_user(
            request,
            f'Было обновлено {count_update} записей'
        )

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, qr: QuerySet):
        count_update = qr.update(currency=Movie.EUR)
        self.message_user(
            request,
            f'Было обновлено {count_update} записей',
            messages.ERROR
        )


