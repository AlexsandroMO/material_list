from django.db import models
from django.contrib.auth import get_user_model


class Produto(models.Model):

    produto = models.CharField(max_length=255, verbose_name='PRODUTO')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.produto


class Tipo(models.Model): #Lista de Funcionários

    tipo = models.CharField(max_length=255, verbose_name='TIPO')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tipo
    

class Material(models.Model): #Lista de Funcionários

    material = models.CharField(max_length=255, verbose_name='MATERIAL')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.material  


class Altura(models.Model): #Lista de Funcionários

    altura = models.CharField(max_length=255, verbose_name='ALTURA')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.altura


class Largura(models.Model): #Lista de Funcionários

    largura = models.CharField(max_length=255, verbose_name='LARGURA')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.largura
    

class Caract(models.Model): #Lista de Funcionários

    caract = models.CharField(max_length=255, verbose_name='CARACTERÍSTICAS')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caract
    

class Bitola_PEC(models.Model): #Lista de Funcionários

    bitola_pec = models.CharField(max_length=255, verbose_name='BITOLA PEÇAS')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bitola_pec


class Bitola_CAB(models.Model): #Lista de Funcionários

    bitola_cab = models.CharField(max_length=255, verbose_name='BITOLA CABO')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bitola_cab
    

class Tipo_Forn(models.Model): #Lista de Funcionários

    tipo_forn = models.CharField(max_length=255, verbose_name='TIPO FORNECIMENTO')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tipo_forn
    


class Unidade(models.Model): #Lista de Funcionários

    unidade = models.FloatField(max_length=255, verbose_name='UNIDADE')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.unidade





#control_acting = models.ForeignKey(material_code, on_delete=models.CASCADE, verbose_name='ÁREA')
#photo = models.FileField(upload_to='uploads/photos/', blank=True, null=True, verbose_name='FOTO')
#user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='USUÁRIO')

