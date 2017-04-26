from django.db import models


class AyantDroit(models.Model):
    nom = models.CharField(max_length=200)
    diminutif = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nom)


class Droit(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nom)


class Genre(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nom)


class Langue(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nom)


class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nom)


class Rating(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nom)


class Contenu(models.Model):
    titreVf = models.CharField(max_length=500)
    titreVo = models.CharField(max_length=500)
    ayantDroit = models.ManyToManyField(AyantDroit)
    codeAyantDroit = models.CharField(max_length=100, blank=True, null=True)
    droits = models.ManyToManyField(Droit)
    vodStart = models.DateField(blank=True, null=True)
    vodEnd = models.DateField(blank=True, null=True)
    svodStart = models.DateField(blank=True, null=True)
    svodEnd = models.DateField(blank=True, null=True)
    realisateur = models.TextField(blank=True, null=True)
    casting = models.TextField(blank=True, null=True)
    paysProduction = models.TextField(blank=True, null=True)
    anneeProduction = models.IntegerField(blank=True, null=True)
    rating = models.ForeignKey(Rating, related_name="rating")
    synopsis = models.TextField(blank=True, null=True)
    genre = models.ForeignKey(Genre, related_name="genre")
    sousGenre = models.ForeignKey(Genre, related_name="sousgenre")
    dateSortieVideo = models.DateField(blank=True, null=True)
    imdb = models.URLField(max_length=500, blank=True, null=True)
    visuel = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.titreVf)


class Film(Contenu):
    categorie = models.ForeignKey(Categorie)
    dateSortieSalle = models.DateField(blank=True, null=True)
    duree = models.DurationField(blank=True, null=True)


class Serie(Contenu):
    format = models.DurationField()


class Catalogue(models.Model):
    nom = models.CharField(max_length=500)
    visuel = models.CharField(max_length=500, blank=True, null=True)
    contenus = models.ManyToManyField(Contenu)

    def __str__(self):
        return str(self.nom)