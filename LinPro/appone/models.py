from django.db import models

class Ingredient(models.Model):
    CATHEGORIES =  [('Veggie','Veggie'),
                    ('Made by Animal','From Animal'),
                    ('Made of Animal','Made of Animal'),]

    name = models.CharField(max_length = 100)
    cathegory = models.CharField(max_length = 1, choices=CATHEGORIES)


class Recipes(models.Model):
    name = models.CharField(max_length = 50)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name
