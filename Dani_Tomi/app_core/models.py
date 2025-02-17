from django.db import models

# Create your models here.

class Gasto(models.Model):
    choices_metodos = [('1','Mecado Pago'),
                        ('2', 'Cuenta DNI'),
                        ('3','Efectivo')
                    ]
    monto = models.IntegerField(default=0)
    referencia = models.CharField(max_length=50)
    metodo_de_pago = models.CharField(max_length=50, choices=choices_metodos)
