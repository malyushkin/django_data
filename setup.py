from setuptools import setup, find_packages

setup(
    name="django_data",
    author="Roman Maliushkin",
    packages=find_packages(exclude=["postcards"]),
    install_requires=[
        "django",
        "geopy",
        "requests",
        "psycopg2-binary"
    ],
)
