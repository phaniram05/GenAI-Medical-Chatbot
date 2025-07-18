from setuptools import find_packages, setup

setup(
    name = "GenAI Medical Chatbot", # Package name we want to create
    version = '0.0.0',
    author = "Phani Ram Popuri",
    author_email = "saiphaniram.reachout@gmail.com",
    packages = find_packages(), # finds __init__.py and considers src as my local package
    install_requires = []
)