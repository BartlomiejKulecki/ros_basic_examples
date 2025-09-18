from setuptools import setup

package_name = 'minimal_subscriber_rclpy'

setup(
    name=package_name,
    version='0.19.6',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Mikael Arguedas',
    author_email='mikael@osrfoundation.org',
    maintainer='Aditya Pande, Alejandro Hernandez Cordero',
    maintainer_email='aditya.pande@openrobotics.org, alejandro@openrobotics.org',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Examples of minimal subscribers using rclpy.',
    license='Apache License, Version 2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'subscriber_old_school = minimal_subscriber_rclpy.subscriber_old_school:main',
            'subscriber_lambda = minimal_subscriber_rclpy.subscriber_lambda:main',
            'subscriber_member_function = minimal_subscriber_rclpy.subscriber_member_function:main',
        ],
    },
)
