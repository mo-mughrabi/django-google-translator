from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from ...utils import Google
import os, polib

class Command(BaseCommand):
    args = ''
    help = 'This command will build strings from the locale files'

    def handle(self, *args, **options):


        self.stdout.write('Loading LOCALE_PATH from django settings..\n')
        locale_paths    = getattr(settings, 'LOCALE_PATHS', None)

        if locale_paths is None:
            raise CommandError('LOCALE_PATH is not defined in django settings')

        languages           = getattr(settings, 'LANGUAGES', None)
        default_language    = getattr(settings, 'LANGUAGE_CODE', None)
        if not (languages or default_language):
            raise CommandError('LANGUAGES or LANGUAGE_CODE is not defined in django settings')

        if not default_language in tuple([c for c,n in languages]):
            raise CommandError('LANGUAGE_CODE does not exists in LANGUAGES')

        languages = tuple([c for c, n in languages if c != default_language])

        self.stdout.write('Loading PO files..\n')

        for language in languages:
            for locale_path in locale_paths:
                    po = polib.pofile(self.load_po_files(locale_path, language))
                    for entry in po:
                        translation = Google(entry.msgid, default_language, language)
                        entry.msgstr=translation.output
                        self.stdout.write('String %s is translated to %s' % (entry.msgid, translation.output))
                    po.save()



    def load_po_files(self, locale_path, language):
        """

        """

        return os.path.join(locale_path, language, 'LC_MESSAGES', 'django.po')
