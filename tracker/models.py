from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Circunscripcion(models.Model):
	num = models.IntegerField(unique=True, primary_key=True)
	capacidad = models.FloatField()

	def __unicode__(self):
		return u'%s' % (self.num)


class Camion(models.Model):
	ficha = models.CharField(max_length=20, unique=True, primary_key=True)
	tipo_camion = models.CharField(max_length=20)
	capacidad = models.IntegerField()

	def __unicode__(self):
		return u'%s' % (self.ficha)


class Transfer(models.Model):
	camion = models.ForeignKey(Camion)
	viaje = models.IntegerField()
	ton_aproximado = models.IntegerField()

	def __unicode__(self):
		return u'%s' % (self.camion)


class TransferComlursa(models.Model):
	camion = models.ForeignKey(Camion)
	circunscripcion = models.ForeignKey(Circunscripcion)
	viaje = models.IntegerField()
	ton_aproximado = models.IntegerField()

	def __unicode__(self):
		return u'%s' % (self.camion)

class opeDuquesa(models.Model):
	id = models.AutoField(primary_key=True)
	date = models.DateField()
	camion = models.ForeignKey(Camion)
	circunscripcion = models.ForeignKey(Circunscripcion)
	ton = models.FloatField()

	def __unicode__(self):
		return u'%s' % (self.date)

class Compania(models.Model):
	nombre = models.CharField(max_length=20)
	camiones_owned = models.ManyToManyField(Camion)

	def __unicode__(self):
		return u'%s' % (self.nombre)







