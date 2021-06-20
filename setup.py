from setuptools import setup
import mlagents_video_streamer
import os

description = "Live stream Unity's ML-Agents training process from Google Colab to Twitch/YouTube server."

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

VERSION = mlagents_video_streamer.__version__

setup(
    name="mlagents-video-streamer",
    author="Dhyey Thumar",
    author_email="dhyeythumar@gmail.com",
    version=VERSION,
    packages=["mlagents_video_streamer"],

    url="https://github.com/dhyeythumar/mlagents-video-streamer",
    description=description,
    long_description=long_description,
    long_description_content_type=long_description_content_type,

    keywords=["ML-Agents", "Video Streamer", "Unity Engine", "Google Colab"],
    classifiers=[
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries"],
)
