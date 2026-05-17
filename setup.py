from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='0.1.0',
    packages=find_packages(),
    description='A package to detect emotions and identify the dominant emotion from a specific JSON response string.',
    author='Bao Phan',
    python_requires='>=3.11',
)