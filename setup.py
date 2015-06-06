from setuptools import setup


setup(
    name='luffa',
    version='0.0.1',
    description='Binds multiple Slack together',
    author='rschiang',
    author_email='ren.chiang@gmail.com',
    url='https://github.com/rschiang/luffa',
    packages=('luffa',),
    scripts=('scripts/luffa',),
    install_requires=(
        'bottle',
        'slacker',
    ),
)
