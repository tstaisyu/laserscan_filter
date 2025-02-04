from setuptools import find_packages, setup

package_name = 'laserscan_filter'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/config', ['config/laser_filter_params.yaml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='taisyu',
    maintainer_email='t_shiba117@yahoo.co.jp',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'laser_filter_node = laserscan_filter.laser_filter_node:main'
        ],
    },
)
