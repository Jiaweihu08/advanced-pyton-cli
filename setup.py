from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt') as f:
        requirements = f.read().split("\n")
    return requirements


setup(name='person',
      version='0.1',
      packages=find_packages(),
      include_package_data=True,
      install_requires=read_requirements(),
      entry_points={
          'console_scripts': ['person=person:cli']
      }
      )
