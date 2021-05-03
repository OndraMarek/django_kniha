from django.db import models
from django.urls import reverse


class Zanry(models.Model):
    zanr = models.CharField(max_length=20, unique=True, verbose_name="Žánr knihy",
                            help_text='Zadejte text o maximální délce 20 znaků; text musí být jedinečný')

    class Meta:
        ordering = ["zanr"]
        verbose_name = 'Žánr knihy'
        verbose_name_plural = 'Žánr knihy'

    def __str__(self):
        return f"{self.zanr}"


class Knihy(models.Model):
    nazev = models.CharField(max_length=100, verbose_name="Název knihy", help_text='Zadejte text o maximální délce 100 znaků')
    popis = models.TextField(blank=True, null=True, verbose_name="Popis knihy")
    autor = models.CharField(max_length=100, null=True, verbose_name="Autor knihy",
                             help_text='Zadejte text o maximální délce 100 znaků')
    rok = models.IntegerField(null=True, help_text="Zadejte rok vydání knihy", verbose_name="Rok vydání")
    foto = models.ImageField(upload_to='kniha/%Y/%m/%d/', blank=True, null=True, verbose_name="Fotka knihy")
    zanry = models.ForeignKey(Zanry, on_delete=models.RESTRICT)

    class Meta:
        ordering = ["nazev"]
        verbose_name = 'Knihy'
        verbose_name_plural = 'Knihy'

    def __str__(self):
        return f"{self.nazev}"

    def get_absolute_url(self):
        """Metoda vrací URL stránky, na které se vypisují podrobné informace o zboží"""
        return reverse('detail', args=[str(self.id)])