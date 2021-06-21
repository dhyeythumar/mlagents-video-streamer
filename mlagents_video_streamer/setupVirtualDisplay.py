import platform
import urllib
import shutil
import pathlib
import stat
import subprocess
import re
import os

os.environ['DISPLAY'] = ":0"

def download(url, path):
    try:
        with urllib.request.urlopen(url) as response:
            with open(path, 'wb') as outfile:
                shutil.copyfileobj(response, outfile)
    except Exception as e:
        print("Failed to download", url)
        raise (e)


def config_xorg():
    download("http://us.download.nvidia.com/tesla/460.32.03/NVIDIA-Linux-x86_64-460.32.03.run", "nvidia.run")
    pathlib.Path("nvidia.run").chmod(stat.S_IXUSR)
    subprocess.run(["./nvidia.run", "--no-kernel-module", "--ui=none"], input="1\n", check=True, universal_newlines=True)

    subprocess.run(["nvidia-xconfig",
                    "-a",
                    "--allow-empty-initial-configuration",
                    "--virtual=1920x1080",
                    "--busid", "PCI:0:4:0"],
                   check=True)

    with open("/etc/X11/xorg.conf", "r+") as f:
        conf = f.read()
        conf = re.sub('(Section "Device".*?)(EndSection)',
                      '\\1    MatchSeat      "seat-1"\n\\2',
                      conf, 1, re.DOTALL)
        f.seek(0)
        f.truncate()
        f.write(conf)


def installer(packages):
    try:
        import apt
        import apt.debfile

        cache = apt.Cache()
        cache.update()
        cache.open(None)
        cache.commit()
        for package in packages:
            pkg = cache[package]
            if pkg.is_installed:
                print(f"{package} is already installed !")
            else:
                print(f"Installing {package} ...")
                pkg.mark_install()
        cache.commit()
    except Exception as e:
        print("Exception :: {}".format(e))
        print("-"*100)
        print("Got an exception while installing following [{}] list of packages.".format(" ".join(packages)))

def SetupVirtualDisplay(force=False):
    # Stop the exec for Windows OS & macOS
    system = platform.system()
    if system in ["Windows", "Darwin", "Java"] is not None:
        print("You are using {} platform & this Virtual Display Setup is only required for Google Colab!\n\
        You have to install ffmpeg manually from 'https://ffmpeg.org/download.html'".format(system))
        if force is False:
            return

    packages = ["ffmpeg", "xvfb", "xserver-xorg", "mesa-utils", "xinit", "xdotool",
                "linux-generic", "xterm", "htop", "xloadimage", "libgtk2.0-0", "libgconf-2-4"]
    installer(packages)
    print("Installed all the required packages.")
    config_xorg()
    print("xorg setup is done.")


# ---- Note ----
# I don't know how the package will react on OS platforms except Linux.
