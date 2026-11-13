>>> from tasks.models import NominaTrabajo
>>> NominaTrabajo.objects.create(
... nombre_trabajador="Luis",
... anio_contrato=3,
... sueldo_asignado=478.12,
... )
<NominaTrabajo: Luis>

>>> trabajador = NominaTrabajo(nombre_trabajador="María",anio_contrato=4,sueldo_asignado=475)
>>> trabajador.save()
>>> trabajador2 = NominaTrabajo(nombre_trabajador="Alberto",anio_contrato=8,sueldo_asignado=1235.46)
>>> trabajador2.save()

>>> NominaTrabajo.objects.get(nombre_trabajador="Alberto")
<NominaTrabajo: Alberto>
>>> NominaTrabajo.objects.get(pk=1)
<NominaTrabajo: Luis>

>>> NominaTrabajo.objects.filter(nombre_trabajador="María")
<QuerySet [<NominaTrabajo: María>]>

>>> NominaTrabajo.objects.exclude(anio_contrato=3)
<QuerySet [<NominaTrabajo: María>, <NominaTrabajo: Alberto>]>

>>> NominaTrabajo.objects.filter(nombre_trabajador__contains="a")
<QuerySet [<NominaTrabajo: María>]>
>>> NominaTrabajo.objects.filter(nombre_trabajador__contains="i")
<QuerySet [<NominaTrabajo: Luis>]>
>>> NominaTrabajo.objects.filter(nombre_trabajador__icontains="a")
<QuerySet [<NominaTrabajo: María>, <NominaTrabajo: Alberto>]>
>>> NominaTrabajo.objects.filter(nombre_trabajador__icontains="i")
<QuerySet [<NominaTrabajo: Luis>]>

>>> NominaTrabajo.objects.filter(anio_contrato__gt=5)
<QuerySet [<NominaTrabajo: Alberto>]>
>>> NominaTrabajo.objects.filter(anio_contrato__lt=5)
<QuerySet [<NominaTrabajo: Luis>, <NominaTrabajo: María>]>
>>> NominaTrabajo.objects.filter(sueldo_asignado__gt=475)
<QuerySet [<NominaTrabajo: Luis>, <NominaTrabajo: Alberto>]>

>>> NominaTrabajo.objects.order_by("sueldo_asignado")
<QuerySet [<NominaTrabajo: María>, <NominaTrabajo: Luis>, <NominaTrabajo: Alberto>]>
>>> NominaTrabajo.objects.order_by("-sueldo_asignado")
<QuerySet [<NominaTrabajo: Alberto>, <NominaTrabajo: Luis>, <NominaTrabajo: María>]>
>>> NominaTrabajo.objects.order_by("-sueldo_asignado", "nombre_trabajador")
<QuerySet [<NominaTrabajo: Alberto>, <NominaTrabajo: Luis>, <NominaTrabajo: María>]>

>>> NominaTrabajo.objects.count()
3
>>> NominaTrabajo.objects.filter(nombre_trabajador__icontains="A").count()
2
>>> NominaTrabajo.objects.filter(nombre_trabajador="Mateo").exists()
False
>>> NominaTrabajo.objects.exists()
True

