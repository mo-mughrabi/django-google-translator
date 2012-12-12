import json
from django.conf import settings
import polib, os, urllib2


class Google(object):
    """
    Google(object) Class:

    """

    def __init__(self, string, from_language, to_language):
        self._API_KEY = getattr(settings, 'GOOGLE_API_KEY', None)
        if not self._API_KEY:
            raise Exception('GOOGLE_API_KEY must be defined in settings file')

        self.string         = string
        self.from_language  = from_language
        self.to_language    = to_language
        self.transaction    = False
        self.translate()

    def __getattr__(self, output):
        try:
            if not self.transaction:
                return False
            return getattr(self, output)
        except : raise AttributeError

    def translate(self):
        text = urllib2.quote(self.string. encode('utf8'))
        data = urllib2.urlopen('https://www.googleapis.com/language/translate/v2?key=' + self._API_KEY + '&source=' + self.from_language + '&target=' + self.to_language + '&q=' + text).read()
        json_data = json.loads(data)
        self.output=json_data['data']['translations'][0]['translatedText']
        self.transaction=True





