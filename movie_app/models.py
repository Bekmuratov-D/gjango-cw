from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
#from movie_app.models import Movie


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField()
    slug = models.SlugField(default='', null=False, blank=True)
    def __str__(self):                            # для вывода в током виде f'{self.name} - {self.rating}'
        return f'{self.first_name} {self.last_name}'
    def get_url(self):
        return reverse('show_director', args=[self.slug])
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.first_name)
    #     super(Director, self).save(*args, **kwargs)

class Actor(models.Model):
    MALE = 'М'
    FEMALE = 'Ж'
    GENDER = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER, default=MALE)
    slug = models.SlugField(default='', null=False, blank=True)
    def __str__(self):  
        if self.gender == self.MALE:                       # для вывода в током виде f'{self.name} - {self.rating}'
            return f'Актер {self.first_name} {self.last_name}'
        else:
            return f'Актриса {self.first_name} {self.last_name}'
    def get_url(self):
        return reverse('show_ane_actor', args=[self.slug])

class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CHRRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollars'),
        (RUB, 'Rubles'),
     ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)] )
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000, validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=3, choices=CHRRENCY_CHOICES, default=RUB)
    slug = models.SlugField(default='', null=False, blank=True)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True, related_name='movies')
    actors = models.ManyToManyField(Actor)


    #def save(self, *args, **kwargs):
    #    self.slug = slugify(self.name)
    #    super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):                            # для вывода в током виде f'{self.name} - {self.rating}'
        return f'{self.name} - {self.rating}% {self.year} -- {self.budget}'


