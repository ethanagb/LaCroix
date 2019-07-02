from setuptools import setup

setup(name='lacroix',
      version='0.0.3',
      description='Use LaCroix Color Palettes in Matplotlib & Seaborn',
      url='https://github.com/ethanagbaker/LaCroix',
      author='Ethan Alexander Garcia Baker',
      author_email='ethanagbaker@gmail.com',
      license='cc-by-sa',
      packages=['lacroix'],
      include_package_data=True,
      install_requires=['matplotlib'],
      zip_safe=False)
