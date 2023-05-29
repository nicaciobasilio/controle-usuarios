from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

class Usuario(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        verbose_name="E-mail do usuário",
        max_length=194,
        unique=True,
    )

    is_active = models.BooleanField (
        verbose_name="O usuário está ativo",
        default=True,
    )

    is_staff = models.BooleanField (
        verbose_name="O usuário pertence a equipe de desenvolvimento",
        default=False,
    )

    is_superuser = models.BooleanField(
        verbose_name="O usuário é um super usuário",
        default=False,
    )

    USERNAME_FIELD = "email" 

    class meta: 
	    verbose_name="insira um nome para identificar no Django admin"
	    verbose_name_plural="insira o nome acima no plural"
	    db_table = "nome que constará no banco de dados"
    
    def __str__(self):
        return self.email