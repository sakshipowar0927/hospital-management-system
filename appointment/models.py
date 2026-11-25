


from django.db import models


class doctor(models.Model):
    did = models.AutoField(primary_key=True)
    dn = models.CharField(max_length=100)
    sp = models.CharField(max_length=200)
    dcon= models.IntegerField(max_length=10)
    e = models.EmailField()

class patient(models.Model):
    pid = models.AutoField(primary_key=True)
    pnm = models.CharField(max_length=100)
    m= models.TextField(max_length=100)
    con= models.CharField(max_length=10)
    a = models.IntegerField(max_length=2)

class appointment(models.Model):
    aid = models.AutoField(primary_key=True)
    pnm = models.CharField(max_length=100)
    dnm= models.CharField(max_length=100)
    d = models.DateField()
    t = models.TimeField()
    c = models.CharField(max_length=100)

    class Meta:
        db_table = 'appointment'








