from setuptools import setup
import os

README_FILE = open('README')

try:
    LONG_DESCRIPTION = README_FILE.read()
finally:
    README_FILE.close()

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, 'dj_scaffold', 'conf')
DJ_SCAFFOLD_DATA = []
for path, dirs, filenames in os.walk(DATA_DIR):
    # Ignore directories that start with '.'
    for i, dir in enumerate(dirs):
        if dir.startswith('.'):
            del dirs[i]
    path = path[len(DATA_DIR) + 1:]
    DJ_SCAFFOLD_DATA.append(os.path.join('conf', path, '*.*'))
    DJ_SCAFFOLD_DATA.append(os.path.join('conf', path, '.*'))


setup(name='django-startproject',
      version='1.0a',
      author='vicalloy',
      author_email='zbirder@gmail.com',
      description=('Create a Django project layout based on vicalloy\'s'
                     'best practices.'),
      long_description=LONG_DESCRIPTION,
      packages=['dj_scaffold'],
      package_data={'dj_scaffold': DJ_SCAFFOLD_DATA},
      scripts=['bin/dj-scripts.py'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules'])
