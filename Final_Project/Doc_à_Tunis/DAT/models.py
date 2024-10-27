from django.db import models


class Resp_Insp(models.Model):
    nom = models.CharField(max_length=32)
    prenoms = models.CharField(max_length=130)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    password = models.CharField(max_length=128)  
    photo = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.nom
    
    class Meta: 
        verbose_name = "Responsable d'inspection"
        verbose_name_plural = "Responsables d'inspection"


class Resp_Prod(models.Model):
    nom = models.CharField(max_length=32)
    prenoms = models.CharField(max_length=130)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    password = models.CharField(max_length=128)  
    photo = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.nom
    
    class Meta: 
        verbose_name = "Responsable de production"
        verbose_name_plural = "Responsables de production"


class Jury(models.Model):
    code = models.CharField(max_length=10, unique=True)
    nom = models.CharField(max_length=32)
    prenoms = models.CharField(max_length=130)
    phone = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    date_naissance = models.DateField()  
    password = models.CharField(max_length=128) 
    photo = models.ImageField(null=True, blank=True, upload_to='images/')
    president = models.BooleanField()

    def __str__(self):
        return self.nom
    
    class Meta: 
        verbose_name = "Jury"
        verbose_name_plural = "Jurys"

class Realisateur(models.Model):
    code = models.CharField(max_length=10, unique=True)
    nom = models.CharField(max_length=32)
    prenoms = models.CharField(max_length=130)
    email = models.EmailField(unique=True)
    date_naissance = models.DateField()  
    photo = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.nom
    
    class Meta: 
        verbose_name = "Réalisateur"
        verbose_name_plural = "Réalisateurs"


class Producteur(models.Model):
    code = models.CharField(max_length=10, unique=True)
    nom = models.CharField(max_length=32)
    prenoms = models.CharField(max_length=130)
    email = models.EmailField(unique=True)
    date_naissance = models.DateField()  
    photo = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.nom
    
    class Meta: 
        verbose_name = "Producteur"
        verbose_name_plural = "Producteurs"


class Documentaire(models.Model):
    code = models.CharField(max_length=10, unique=True)
    titre = models.CharField(max_length=32)
    sortie = models.DateField(unique=True)  
    sujet = models.TextField()
    realisateur = models.ForeignKey(Realisateur, on_delete=models.CASCADE)
    producteur = models.ForeignKey(Producteur, on_delete=models.CASCADE)
    note = models.FloatField()
    like = models.IntegerField(default=0) 
    cover = models.ImageField(null=True, blank=True, upload_to='images/')
    
    def __str__(self):
        return self.titre
    
    class Meta: 
        verbose_name = "Documentaire"
        verbose_name_plural = "Documentaires"


class Planning_Item(models.Model):
    documentaire = models.ForeignKey(Documentaire, on_delete=models.CASCADE)
    heure = models.TimeField()


class Planning(models.Model):
    date = models.DateField()
    planning_item_1 = models.ForeignKey(Planning_Item, on_delete=models.CASCADE, related_name='planning_item_1')  
    planning_item_2 = models.ForeignKey(Planning_Item, on_delete=models.CASCADE, related_name='planning_item_2')  
    planning_item_3 = models.ForeignKey(Planning_Item, on_delete=models.CASCADE, related_name='planning_item_3')  
