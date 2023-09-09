## author: xin luo
## creat: 2023.9.1
## des: setting for the python package


from setuptools import setup
from setuptools import find_packages


VERSION = '1.0.8'


setup(
    name='pyrsimg',   # package name
    version=VERSION,  # package version
    description='Python toolkit for easy processing of remote sensing image',  # package description
    author='The pyrsimg developers',
    author_email='xinluo_xin@163.com',
    maintainer='Xin Luo',
    maintainer_email='xinluo_xin@163.com',    
    license='GPL License',  
    packages=find_packages(),  
    install_requires=['pyproj',   
                      'torch',  
                      'scikit-learn', 
                      'numpy', 
                      'opencv-python', 
                      'matplotlib', 
                      'scipy', 
                      'astropy'],   ## gdal shoule be installed by the user.
    python_requires='>=3.9',                # Minimum version requirement of the package
    )

