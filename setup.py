from setuptools import setup, find_packages

setup(
    name='huex',
    version='0.1.2',
    author='s1lvx',
    author_email='silva@cfsilva.com',
    description='A powerful and lightweight CLI based tool for the Conbee II',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/s1lvax/huex',
    packages=find_packages(),
    install_requires=[
        'requests',
        'prettytable',
    ],
    entry_points={
        'console_scripts': [
            'huex=huex.main:main',
        ],
    },
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
    ],
    keywords='cli conbee2 zigbee huelights hue',
)
