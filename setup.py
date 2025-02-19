#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup

install_requires = [
    "alembic>=1.6.5",
    "amqp>=5.0.6",
    "attrs>=21.2.0",
    "Babel>=2.9.1",
    "billiard>=3.6.4.0",
    "blinker>=1.4",
    "celery>=5.1.2",
    "certifi>=2021.5.30",
    "charset-normalizer>=2.0.3",
    "click>=7.1.2",
    "click-didyoumean>=0.0.3",
    "click-log>=0.3.2",
    "click-plugins>=1.1.1",
    "click-repl>=0.2.0",
    "dnspython>=2.1.0",
    "email-validator>=1.1.3",
    "Flask>=2.0.1",
    "Flask-Alembic>=2.0.1",
    "flask-allows @ git+https://github.com/flaskbb/flask-allows.git@master#egg=flask-allows",
    "Flask-BabelPlus>=2.2.0",
    "Flask-Caching>=1.10.1",
    "Flask-DebugToolbar>=0.11.0",
    "flask-debugtoolbar-warnings>=0.1.0",
    "Flask-Limiter>=1.4",
    "Flask-Login>=0.5.0",
    "Flask-Mail>=0.9.1",
    "flask-redis>=0.4.0",
    "Flask-SQLAlchemy>=2.5.1",
    "Flask-Themes2>=1.0.0",
    "flask-whooshee>=0.8.1",
    "Flask-WTF>=0.15.1",
    "flaskbb-plugin-conversations>=1.1.0",
    "flaskbb-plugin-portal>=1.2.0",
    "greenlet>=1.1.3",
    "idna>=3.2",
    "itsdangerous>=2.0.1",
    "Jinja2>=3.0.1",
    "kombu>=5.1.0",
    "limits>=1.5.1",
    "Mako>=1.1.4",
    "MarkupSafe>=2.0.1",
    "mistune>=0.8.4",
    "Pillow>=9.5.0",
    "pluggy>=0.13.1",
    "prompt-toolkit>=3.0.19",
    "Pygments>=2.9.0",
    "PyJWT>=2.1.0",
    "python-dateutil>=2.8.2",
    "python-editor>=1.0.4",
    "pytz>=2021.1",
    "redis>=3.5.3",
    "requests>=2.26.0",
    "six>=1.16.0",
    "SQLAlchemy>=1.4.21",
    "SQLAlchemy-Utils>=0.37.8",
    "Unidecode>=1.2.0",
    "urllib3>=1.26.6",
    "vine>=5.0.0",
    "wcwidth>=0.2.5",
    "Werkzeug>=2.0.1",
    "Whoosh>=2.7.4",
    "WTForms>=2.3.3",
    "WTForms-SQLAlchemy>=0.2",
]

extras_require = {"postgres": ["psycopg2-binary"]}

tests_require = ["py", "pytest", "pytest-cov", "cov-core", "coverage"]

setup(
    install_requires=install_requires,
    extras_require=extras_require,
    tests_require=tests_require
)
