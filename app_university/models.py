from django.db import models
from pytils.translit import slugify


#Модель, отвечающая за должности факультета
class FacultyPositionModel(models.Model):
    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    position_title = models.CharField(max_length=70)

    def __str__(self):
        return self.position_title


#Модель, отвечающая за подразделение ректората
class RectorateModel(models.Model):

    class Meta:
        verbose_name = "Ректорат"
        verbose_name_plural = "Ректорат"
        
    position_title = models.CharField(verbose_name="Должность", max_length=70)
    header_rectorate = models.OneToOneField('EmployeeModel', related_name="rectorate", null=True, blank=True, on_delete=models.SET_NULL)
    belong_id = models.ForeignKey('RectorateModel', blank=True, null=True, verbose_name="В подчинении у", on_delete=models.SET_NULL)

    # Перед сохранением мы неявно меняем связное поле OneToOne у сотрудника(если он существует), для обратной связи.
    def save(self, *argv, **kwargs):

        if not self.id is None:
            employee = RectorateModel.objects.get(id=self.id)
            if self.header_rectorate:
                if employee.header_rectorate is not None:
                    EmployeeModel.objects.filter(id=employee.header_rectorate.id).update(rectorate_position=None)
                EmployeeModel.objects.filter(id=self.header_rectorate.id).update(rectorate_position=self.id)
            elif employee.header_rectorate is not None:
                EmployeeModel.objects.filter(id=employee.header_rectorate.id).update(rectorate_position=None)

        super().save(*argv, **kwargs)

    def __str__(self):
        return self.position_title


#Модель, отвечающая за сотрудников, состоящие в факультете
class FacultyModel(models.Model):

    class Meta:
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"

    name_faculty = models.CharField(verbose_name="Название факультета", max_length=100)
    header_faculty = models.OneToOneField('EmployeeModel', related_name="faculty", null=True, blank=True, on_delete=models.SET_NULL)
    belong_rectorate = models.ForeignKey(RectorateModel, related_name="leads", verbose_name="В подчинении у", on_delete=models.SET_NULL, null=True)
    slug = models.SlugField('ЧПУ', max_length=255, blank=True)

    # Перед сохранением мы неявно меняем связное поле OneToOne у сотрудника(если он существует), для обратной связи.
    def save(self, *argv, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_faculty)

        if not self.id is None:
            employee = FacultyModel.objects.get(id=self.id)
            if self.header_faculty:
                if employee.header_faculty is not None:
                    EmployeeModel.objects.filter(id=employee.header_faculty.id).update(faculty_position=None)
                EmployeeModel.objects.filter(id=self.header_faculty.id).update(faculty_position=self.id)
            elif employee.header_faculty is not None:
                EmployeeModel.objects.filter(id=employee.header_faculty.id).update(faculty_position=None)

        super().save(*argv, **kwargs)
    
    def get_absolute_url(self):
        return self.slug

    def __str__(self):
        return self.name_faculty


#Модель, отвечающая за сотрудников, состоящие в кафедре
class CathedraModel(models.Model):

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедры"

    name_cathedra = models.CharField(verbose_name="Назваине кафедры", max_length=100)
    header_cathedra = models.OneToOneField('EmployeeModel', null=True, blank=True, on_delete=models.SET_NULL)
    fk_faculty = models.ForeignKey(FacultyModel, related_name="cathedra", verbose_name="Факультет", on_delete=models.CASCADE)
    slug = models.SlugField('ЧПУ', max_length=255, blank=True)

    # Перед сохранением мы неявно меняем связное поле OneToOne у сотрудника(если он существует), для обратной связи.
    def save(self, *args, **kwords):
        if not self.slug:
            self.slug = slugify(self.name_cathedra)
    
        if self.fk_faculty:
            EmployeeModel.objects.filter(fk_cathedra=self.id).update(fk_faculties=self.fk_faculty)

        if not self.id is None:
            employee = CathedraModel.objects.get(id=self.id)
            if self.header_cathedra:
                if employee.header_cathedra is not None:
                    EmployeeModel.objects.filter(id=employee.header_cathedra.id).update(cathedra_position=None)
                EmployeeModel.objects.filter(id=self.header_cathedra.id).update(cathedra_position=self.id)
            elif employee.header_cathedra is not None:
                EmployeeModel.objects.filter(id=employee.header_cathedra.id).update(cathedra_position=None)

        super().save(*args, **kwords)

    def __str__(self):
        return self.name_cathedra


# Модель сотрудника
class EmployeeModel(models.Model):

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    #Основные поля
    surname = models.CharField(verbose_name="Фамилия", max_length=70)
    name = models.CharField(verbose_name="Имя", max_length=70)
    last_name = models.CharField(verbose_name="Отчество", max_length=70)
    birthday = models.DateField(verbose_name="День рождение")
    photo = models.ImageField(verbose_name="Фото", blank=True)

    #Поля для обратной связи с подразделениями. По умолчанию скрыты и не меняются вручную 
    rectorate_position = models.OneToOneField(RectorateModel, editable=False, related_name="rectorate", null=True, blank=True, on_delete=models.SET_NULL)
    faculty_position = models.OneToOneField(FacultyModel, editable=False, related_name="faculty", null=True, blank=True, on_delete=models.SET_NULL)
    cathedra_position = models.OneToOneField(CathedraModel, editable=False, related_name="cathedra", null=True, blank=True, on_delete=models.SET_NULL)
    #----------------------------------
    #Внешние ключи для принадлежности к подразделениям
    fk_faculties = models.ForeignKey(FacultyModel, null=True, blank=True, on_delete=models.SET_NULL)
    fk_cathedra = models.ForeignKey(CathedraModel, related_name="employees", blank=True, verbose_name="Кафедра", null=True, on_delete=models.SET_NULL)
    #Внешний ключ для определения должности
    fk_position = models.ForeignKey(FacultyPositionModel, verbose_name="Должность", null=True, on_delete=models.SET_NULL)


    def save(self, *args, **kwords):
        self.fk_faculties = FacultyModel.objects.get(id=self.fk_cathedra.fk_faculty.id) if self.fk_cathedra else None

        if self.rectorate_position:
            RectorateModel.objects.filter(id=self.rectorate_position.id).update(header_rectorate=self.id)
        else:
            RectorateModel.objects.filter(header_rectorate=self.id).update(header_rectorate=None)

        super().save(*args, **kwords)

    def __str__(self):
        return "{} {} {}".format(self.surname, self.name, self.last_name)

