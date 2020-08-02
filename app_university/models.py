from django.db import models


#Модель, отвечающая за должности факультета
class FacultyPosition(models.Model):
    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    position_title = models.CharField(max_length=70)
    priority = models.IntegerField()

    def __str__(self):
        return self.position_title


#Модель, отвечающая за должности ректората
class RectoratePosition(models.Model):

    class Meta:
        verbose_name = "Должность ректората"
        verbose_name_plural = "Должности ректората"
        
    position_title = models.CharField(verbose_name="Должность", max_length=70)
    belong_id = models.IntegerField(verbose_name="В подчинении у")

    def __str__(self):
        return self.position_title


#Модель, отвечающая за сотрудников, состоящие в ректорате
class Rectorate(models.Model):
    pass


#Модель, отвечающая за сотрудников, состоящие в факультете
class Faculty(models.Model):

    class Meta:
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"

    name_faculty = models.CharField(verbose_name="Название факультета", max_length=100)
    header_faculty = models.OneToOneField('Employee', verbose_name="Декан", on_delete=models.SET_NULL, blank=True, null=True)
    belong_rectorate = models.ForeignKey(RectoratePosition, verbose_name="В подчинении у", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name_faculty


#Модель, отвечающая за сотрудников, состоящие в кафедре
class Cathedra(models.Model):

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедры"

    name_cathedra = models.CharField(verbose_name="Назваине кафедры", max_length=100)
    header_cathedra = models.OneToOneField('Employee', verbose_name="Заведущий кафедрой", on_delete=models.SET_NULL, blank=True, null=True)
    fk_faculty = models.ForeignKey(Faculty, verbose_name="Факультет", on_delete=models.CASCADE)

    def __str__(self):
        return self.name_cathedra


# Модель сотрудника
class Employee(models.Model):

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
    
    surname = models.CharField(verbose_name="Фамилия", max_length=70)
    name = models.CharField(verbose_name="Имя", max_length=70)
    last_name = models.CharField(verbose_name="Отчество", max_length=70)
    birthday = models.DateField(verbose_name="День рождение")
    photo = models.ImageField(verbose_name="Фото", blank=True)

    fk_cathedra = models.ForeignKey(Cathedra, verbose_name="Кафедра", null=True, on_delete=models.SET_NULL)
    fk_position = models.ForeignKey(FacultyPosition, verbose_name="Должность на кафедре", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{} {} {}".format(self.surname, self.name, self.last_name)

