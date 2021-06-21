from setuptools import setup
import os

description = "Capture a video using the virtual screen in Google Colab & broadcast the live stream to youtube/twitch."

README_path = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), 'README.md')
if os.path.exists(README_path):
    with open(README_path, encoding='utf-8') as f:
        long_description = f.read()
    long_description_content_type = 'text/markdown'
else:
    print("No Readme.md")
    long_description = description
    long_description_content_type = 'text/plain'

setup(
    name="mlagents-video-streamer",
    version="1.0",
    author="Dhyey Thumar",
    author_email="dhyeythumar@gmail.com",
    py_modules=['videostreamer'],
    url="https://github.com/Dhyeythumar/video-streamer",

    description=description,
    long_description=long_description,
    long_description_content_type=long_description_content_type,

    classifiers=[
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries"
    ]
)
