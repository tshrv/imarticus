from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    thumbnail = models.ImageField(upload_to='course_thumbnails/', null=False, blank=False)

    class Meta:
        db_table = 'courses'
        ordering = ('title',)
    
    def __str__(self) -> str:
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False, null=False)
    title = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        db_table = 'modules'
        ordering = ('title',)

    def __str__(self) -> str:
        return self.title

class Lecture(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False, null=False)
    duration = models.PositiveIntegerField(blank=False, null=False)

    class Meta:
        db_table = 'lectures'
        ordering = ('title',)

    def __str__(self) -> str:
        return self.title