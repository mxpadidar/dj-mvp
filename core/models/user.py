from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    "Custom user model to extends the default django user."

    class Meta:
        db_table = "users"

    def __str__(self) -> str:
        return self.get_full_name() or self.username
