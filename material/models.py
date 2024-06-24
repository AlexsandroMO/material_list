from django.db import models
from django.contrib.auth import get_user_model


class TaskMaterial(models.Model): #Lista de Funções

    material_code = models.CharField(max_length=255, verbose_name='CÓDIGO')
    matetial_name = models.CharField(max_length=255, verbose_name='MATERIAL')
    material_type = models.CharField(max_length=255, verbose_name='TIPO')

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.matetial_name

'''
class Profissional(models.Model): #Lista de Funcionários

    nome = models.CharField(max_length=255, verbose_name='NOME')
    control_acting = models.ForeignKey(material_code, on_delete=models.CASCADE, verbose_name='ÁREA')
    #photo = models.FileField(upload_to='uploads/photos/', blank=True, null=True, verbose_name='FOTO')
    #user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='USUÁRIO')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
'''