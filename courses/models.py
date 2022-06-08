from django.db import models
from loguru import logger


class Course(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    thumbnail = models.ImageField(upload_to='course_thumbnails/', null=False, blank=False)

    class Meta:
        db_table = 'courses'
        ordering = ('title',)
    
    def __str__(self) -> str:
        return self.title

    @property
    def modules(self) -> models.QuerySet:
        logger.debug(type(self.module_set.all()))
        return self.module_set.all()

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False, null=False)
    title = models.CharField(max_length=255, blank=False, null=False)
    position_in_sequence = models.PositiveSmallIntegerField(default=1, null=False, blank=False)

    class Meta:
        db_table = 'modules'
        ordering = ('position_in_sequence',)

    def __str__(self) -> str:
        return self.title
    
    @property
    def lectures(self) -> models.QuerySet:
        logger.debug(type(self.lecture_set.all()))
        return self.lecture_set.all()
class Lecture(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False, null=False)
    duration = models.PositiveIntegerField(blank=False, null=False)
    position_in_sequence = models.PositiveSmallIntegerField(default=1, null=False, blank=False)

    class Meta:
        db_table = 'lectures'
        ordering = ('position_in_sequence',)

    def __str__(self) -> str:
        return self.title