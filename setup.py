from setuptools import setup


setup(
    name='microfarm.messaging',
    install_requires = [
        'protobuf'
    ],
    extras_require={
        'test': [
            'pytest',
        ]
    }
)
