from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(
            self,
            telegram_id=None,
            first_name=None,
            last_name=None,
            username=None,
            password=None,
            **kwargs
    ):
        if not telegram_id:
            raise ValueError('The given telegram_id must be set')

        if kwargs.get('is_superuser'):
            user = self.model(
                telegram_id=telegram_id,
                **kwargs
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, telegram_id, username, first_name, last_name, password, **kwargs):
        kwargs.setdefault('is_superuser', False)
        kwargs.setdefault('is_active', True)

        return self._create_user(
            telegram_id=telegram_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **kwargs
        )

    def create_superuser(self, telegram_id, password, **kwargs):
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_active', True)

        return self._create_user(
            telegram_id=telegram_id,
            password=password,
            **kwargs
        )