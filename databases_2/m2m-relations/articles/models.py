from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=128,
                            verbose_name='Тэг')
    members = models.ManyToManyField(Article,
                                     through='Relationship',
                                     through_fields=('tag', 'article'))

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name


class Relationship(models.Model):
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.DO_NOTHING)
    is_main = models.BooleanField(verbose_name='Основной',
                                  blank=False,
                                  default=False)
