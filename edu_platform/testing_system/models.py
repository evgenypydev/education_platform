from django.db import models
from mentorship.models import Specialization, Teacher
from mixins import DateTimeMixin

__all__ = {"Image", "Course", "Topic", "Article", "Test", "Question", "Answer"}


class Image(models.Model):
    image = models.ImageField(null=True, blank=True)


class Course(models.Model, DateTimeMixin):
    title = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_DEFAULT, default="specialization")

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"


class Topic(models.Model, DateTimeMixin):
    title = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.SET_DEFAULT, default="course")
    index_number = models.IntegerField()
    image = models.ManyToManyField(Image, blank=True, null=True)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "topic"
        verbose_name_plural = "topics"


class Article(models.Model, DateTimeMixin):
    title = models.CharField(max_length=100)
    content = models.FileField(blank=True, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.pk} - {self.title} - {self.author}"

    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"


class Test(models.Model, DateTimeMixin):
    title = models.CharField(max_length=100)
    description = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    is_open = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "test"
        verbose_name_plural = "tests"


class Question(models.Model, DateTimeMixin):
    content = models.CharField(max_length=250)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk} - {self.content}"

    class Meta:
        verbose_name = "question"
        verbose_name_plural = "questions"


class Answer(models.Model, DateTimeMixin):
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk} - {self.text}"

    class Meta:
        verbose_name = "answer"
        verbose_name_plural = "answers"
