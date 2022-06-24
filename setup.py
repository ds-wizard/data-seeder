from setuptools import setup, find_packages


with open('README.md') as f:
    long_description = ''.join(f.readlines())

setup(
    name='dsw_data_seeder',
    version='3.12.2',
    description='Worker for seeding DSW data',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Marek Suchánek',
    keywords='data seed database storage',
    license='Apache License 2.0',
    url='https://github.com/ds-wizard/mailer',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
    zip_safe=False,
    python_requires='>=3.9, <4',
    install_requires=[
        'click',
        'minio',
        'psycopg2',
        'PyYAML',
        'tenacity',
    ],
    entry_points={
        'console_scripts': [
            'dsw-seeder=dsw_data_seeder:main',
        ],
    },
)
