from setuptools import setup

setup(name='pencilvania',
      version='0.1',
      description='Create stylized images suitable for a pen plotter',
      url='http://github.com/ewfuentes/pencilvania',
      author='Erick Fuentes',
      author_email='fuentes.erick@gmail.com',
      license='MIT',
      packages=['pencilvania'],
      install_requires=["torch"],
      zip_safe=False)
