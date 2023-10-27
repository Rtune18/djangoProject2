from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=450)# заголовок поста
    author = models.ForeignKey(  # Автор поста, которого выбираем в административной панели упрпавления
        'auth.User',
         on_delete=models.CASCADE, # удаление поста
    )
    body = models.TextField() # Поле нашего поста

    def __str__(self): # метод
        return self.title



