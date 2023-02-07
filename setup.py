from setuptools import setup

setup(
    name='s3gigillion',
    version='0.1',
    packages=['s3gigillion'],
    url='https://gigillion.com',
    license='MIT',
    author='document',
    install_requires=[
        'boto3'
    ],
    zip_safe=True,
    author_email='hello@gigillion.com',
    description='a boto3 wrapper for Gigillion S3 compatible storage.'
)
