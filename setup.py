from setuptools import setup, find_packages

setup(
    name="mymath_task_x_power_y",
    version="1.2",
    packages=find_packages(),
    data_files=[('.', ["__main__.py", "ReadMe.md", 'setup.py', 'requirements.txt'])],
    entry_points={"setuptools.installation": ["eggsecutable=src.main.main:main"]}
)
