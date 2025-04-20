from setuptools import find_packages,setup

from typing import List


e="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of requirements
    '''
    ans=[]
    with open(file_path) as obj:
        ans=obj.readlines()
        ans=[req.replace("\n","") for req in ans ]

        if e in ans:
            ans.remove(e)
    return ans

setup(

    name="ML PROJECT",
    version ='0.0.1',
    author="Naman",
    author_email="namangupta060504@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt")
)