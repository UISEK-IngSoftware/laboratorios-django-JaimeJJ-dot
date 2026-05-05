from django.db import models

class Trainer (models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birthday = models.DateField()
    level = models.IntegerField(default=1)
    
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
class Pokemon(models.Model):
    name = models.CharField(max_length=30, null=False)
    POKEMONS_TYPES = [
        ('F', 'Fire'),
        ('W', 'Water'),
        ('G', 'Grass'),
        ('E', 'Electric'),
        ('P', 'Psychic'),
        ('I', 'Ice'),
        ('D', 'Dragon'),
        ('Da', 'Dark'),
        ('Fa', 'Fairy'),
    ]
    
    type = models.CharField(max_length=50, choices=POKEMONS_TYPES, null=False)
    height = models.IntegerField()
    weight = models.IntegerField()
    defense = models.IntegerField()
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    picture = models.ImageField(upload_to="pokemon_images")
    

    def __str__(self):
        return self.name
