from setuptools import setup, find_packages

setup(
    name="mymath_task_x_power_y",
    version="1.0",
    packages=find_packages(),
    entry_points={"setuptools.installation": ["eggsecutable=src.main.main:main"]}
)
