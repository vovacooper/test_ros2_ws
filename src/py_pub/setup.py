import os
from glob import glob
from setuptools import setup

package_name = 'py_pub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[        
        # Install marker file in the package index
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),        
        # Include our package.xml file
        (os.path.join('share', package_name), ['package.xml']),
        # Include all launch files.
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*.yaml')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = py_pub.publisher_member_function:main', 
            'talker2 = py_pub.publisher_member_function2:main',            
        ],
    },
)
