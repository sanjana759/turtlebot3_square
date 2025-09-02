from setuptools import setup

package_name = 'turtlebot3_square'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sanjana',
    maintainer_email='your_email@example.com',
    description='TurtleBot3 square movement',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'square_move = turtlebot3_square.square_move:main',
        ],
    },
)

