from setuptools import find_packages,setup


x = '-e .'

def get_requirements ( file_path:str)->list[str]:
    requirements =[]
    with open(file_path) as f:
        requirements = [req.replace("\n"," ") for req in f.readlines()]

        if x in requirements:
            requirements.remove(x)
    return requirements



setup(
    name="mlproject",
    version="0.0.1",
    author="Guru",
    author_email="gurpremsingh9@gmail.com",
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages(),
)



























