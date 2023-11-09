from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tlgbot',
    version='1.3',  
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='GDLegions',
    author_email='usaboy2133@tuta.io',
    description='TLGBot is a Python library for creating Telegram bots with ease. This library simplifies the interaction with the Telegram Bot API, allowing you to send messages, edit group descriptions, and more.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    project_urls={
        'Documentation': 'https://github.com/GDLegions/tlgbot/blob/main/README.md',
        'GitHub Repository': 'https://github.com/GDLegions/tlgbot',
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
