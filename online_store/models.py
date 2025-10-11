from django.contrib.auth import get_user_model  # Importeaza functia pentru a obtine modelul de utilizator activ
from django.contrib.auth.models import AbstractUser  # Importeaza clasa de baza pentru utilizator personalizat (nu este folosita direct aici)
from django.db import models  # Importeaza modulul de modele Django pentru a defini tabelele bazei de date

User = get_user_model()  # Obtine modelul de utilizator definit in proiect (poate fi customizat)


class Item(models.Model):  # Definirea modelului pentru produse (Item)
    name = models.CharField(max_length=255)  # Numele produsului, camp text cu lungime maxima 255
    description = models.TextField()  # Descrierea produsului, camp text lung
    image = models.ImageField(upload_to='item_images')  # Imaginea produsului, salvata in folderul 'item_images'
    price = models.DecimalField(max_digits=8, decimal_places=2)  # Pretul produsului, numar zecimal cu maxim 8 cifre si 2 zecimale

    def __str__(self):  # Metoda pentru afisarea reprezentarii ca text a obiectului
        return self.name  # Returneaza numele produsului


class Cart(models.Model):  # Definirea modelului pentru cosul de cumparaturi
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Legatura catre utilizatorul care detine cosul (stergerea utilizatorului sterge si cosul)
    items = models.ManyToManyField(Item, related_name='carts')  # Relatie de tip many-to-many cu produsele din cos

    def __str__(self):  # Metoda pentru afisarea reprezentarii ca text a obiectului
        return f'Cart for {self.user.email}'  # Returneaza un text cu emailul utilizatorului


class Order(models.Model):  # Definirea modelului pentru comenzi
    STATE_CHOICES = (  # Optiuni pentru starea comenzii
        ('Ordered', 'Ordered'),  # Comanda a fost plasata
        ('In delivery', 'In delivery'),  # Comanda este in livrare
        ('Delivered', 'Delivered'),  # Comanda a fost livrata
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Legatura catre utilizatorul care a plasat comanda
    items = models.ManyToManyField(Item, related_name='orders')  # Relatie de tip many-to-many cu produsele din comanda
    date = models.DateField(auto_now_add=True)  # Data plasarii comenzii, setata automat la crearea obiectului
    state = models.CharField(max_length=20, choices=STATE_CHOICES)  # Starea comenzii, aleasa din optiunile definite
    first_name = models.CharField(max_length=150, blank=True)  # Prenumele destinatarului, optional
    last_name = models.CharField(max_length=150, blank=True)  # Numele destinatarului, optional
    city = models.CharField(max_length=150, blank=True)  # Orasul destinatarului, optional
    country = models.CharField(max_length=150, blank=True)  # Tara destinatarului, optional
    address_details = models.TextField(blank=True)  # Detalii suplimentare despre adresa, optional

    def __str__(self):  # Metoda pentru afisarea reprezentarii ca text a obiectului
        return f'Order {self.id} by {self.user.email}'  # Returneaza un text cu ID-ul comenzii si emailul utilizatorului
