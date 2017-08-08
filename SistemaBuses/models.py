from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Cliente(models.Model):
    cedula = models.CharField(primary_key=True, max_length=13)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    genero = models.CharField(max_length=1)
    fecha_nacimiento = models.DateField()
    reserva = models.ManyToManyField('Reserva')
    user = models.ForeignKey(User)
    def __str__(self):
        return self.user.first_name + self.user.last_name


class Bus(models.Model):
    modelo_bus = models.CharField(max_length=45)
    placa_bus = models.CharField(max_length=7)
    capacidad_bus = models.PositiveSmallIntegerField()
    asiento = models.ManyToManyField('Asiento')

    def __str__(self):
        return self.modelo_bus + str(self.capacidad_bus)


class Asiento(models.Model):
    numero_asiento = models.PositiveSmallIntegerField()
    estado_asiento = models.CharField(max_length=1)

    def __str__(self):
        return str(self.numero_asiento) + str(self.estado_asiento)


class Reserva(models.Model):
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    ruta = models.ForeignKey('Ruta')
    def __str__(self):
        return self.fecha_reserva


class Ruta(models.Model):
    ciudad_partidad = models.CharField(max_length=45)
    ciudad_llegada = models.CharField(max_length=45)
    hora = models.TimeField()
    fecha = models.DateField()
    costo_destino = models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return self.ciudad_partidad + " " + self.ciudad_llegada