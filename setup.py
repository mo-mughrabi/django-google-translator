import os
from setuptools import setup, find_packages

f = open(os.path.join(os.path.dirname(__file__), 'README.txt'))
readme = f.read()
f.close()


setup(
    name='django-google-translator',
    version='0.1',
    description='django-google-translator is a reusable Django application for translating .PO files through Google API.',
    long_description=readme,
    author='Mo Mughrabi',
    author_email='mo.mughrabi@gmail.com',
    url='https://github.com/mo-mughrabi/django-google-translator/tree/master',
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        ],
)