from setuptools import  find_packages, setup
def grt_requirments (filename):
    r=[]
    with open(filename) as f:
        r= f.readlines()
        r=[req.replace('\n', '') for req in r]
    if '-e.' in r:
        r.remove('-e.')
    return r

         


setup(
    name='my_package',
    version='0.1',
    packages=find_packages(),
    author='Ayaz',
    author_email="skayazali77@gmail.com",
    install_requires=grt_requirments('requirments.txt')
)



