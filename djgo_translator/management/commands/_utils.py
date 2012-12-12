from django.utils.translation import import_module

class Google(object):
    """
    Google(object) Class:


    """

    def __init__(self, _from_language=None, _to_language=None):
        self.from_language  =   _from_language
        self.to_language    =   _to_language
       