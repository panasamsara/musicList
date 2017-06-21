from django.db import models

class Article(models.Model):
    song_name = models.CharField('歌名', max_length=32, null=False)
    singer = models.CharField('歌手', max_length=32, null=True)
    createTime = models.DateTimeField('添加时间', auto_now=True)