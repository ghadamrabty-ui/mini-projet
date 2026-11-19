
from django.db import models


class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='categories/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        ordering = ['nom']


class Ressource(models.Model):

    TYPE_CHOICES = [
        ('Cours', 'Cours'),
        ('Tutoriel', 'Tutoriel'),
        ('Document', 'Document'),
        ('Video', 'Vidéo'),
        ('Livre', 'Livre'),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField()

    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES
    )

    image = models.ImageField(
        upload_to='ressources/',
        blank=True,
        null=True
    )

    url = models.URLField()

    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE,
        related_name='ressources'
    )

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = "Ressource"
        verbose_name_plural = "Ressources"
        ordering = ['-date_creation']
