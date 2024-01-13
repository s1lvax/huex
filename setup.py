from setuptools import setup, find_packages

setup(
    name="huex",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # List your project dependencies here
        "requests>=2.31.0",
        "prettytable>=3.9.0"
    ],
    entry_points={
        "console_scripts": [
            "huex=huex.main:main",  # Adjust the path according to your project structure
        ],
    },
    
    author="s1lvx",
    author_email="silva@cfsilva.com",
    description="Powerful, lightweight CLI tool to control Hue Lights in Conbee II",
    keywords="hue lights, conbee II, CLI",
    url="https://github.com/s1lvax/huex",  # Project home page
)
