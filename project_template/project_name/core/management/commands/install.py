from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    def _print_heading(self, text: str):
        self.stdout.write(self.style.MIGRATE_HEADING(f"\n### {text.upper()} ###\n"))

    def _create_user(self, email: str, **defaults):
        username = email.split("@")[0]
        password = email.split("@")[0]
        defaults.update(
            {
                "username": username,
                "email": email,
            }
        )
        user = User.objects.get_or_create(username=username, defaults=defaults)[0]
        user.set_password(password)
        user.save()
        self.stdout.write(
            self.style.NOTICE(
                f"Username: {username}\n"
                f"Email:    {email}\n"
                f"Password: {password}\n"
            )
        )
        return user

    def handle(self, *args, **options):
        if not settings.DEBUG:
            self.stdout.write(self.style.ERROR("Not allowed on prod."))
            return

        self._print_heading("Migrations")
        call_command("migrate")

        # self._print_heading("Fixtures")
        # call_command('loaddata', *[
        #     'fixtures/demo_data.json',
        # ])

        self._print_heading("Users")
        self._create_user("admin@example.com", is_superuser=True, is_staff=True)

        self._print_heading("All done!")
