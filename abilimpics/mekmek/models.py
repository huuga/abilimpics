from django.db import models


# Create your models here.
# class Contributor(models.Model):
#     full_name = models.CharField('ФИО', max_length=100)
#     date_of_birth = models.CharField('Дата рождения', max_length=10)
#     disease = models.CharField('Заболевание', max_length=50)
#     studying_now = models.CharField('Обучается в данное время', max_length=5)
#     graduate = models.CharField('Уровень образования', max_length=20)
#     graduate_year = models.CharField('Планируемый год окончания образовательной организации', max_length=5)
#
#     def __str__(self):
#         return self.full_name
#
#     class Meta:
#         verbose_name = 'Участник'
#         verbose_name_plural = 'Участники'
