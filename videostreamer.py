import apt
import apt.debfile
import pathlib
import stat
import shutil
import urllib.request
import subprocess
import re
import os

os.environ['DISPLAY'] = ":0"
envc = os.environ.copy()


def install(cache, packageName):
    pkg = cache[packageName]
    if pkg.is_installed:
        print(f"{packageName} is already installed !")
    else:
        print(f"Installing {packageName} ...")
        pkg.mark_install()


def installer(packages):
    cache = apt.Cache()
    cache.update()
    cache.open(None)
    cache.commit()
    for package in packages:
        install(cache, package)
    cache.commit()


def installPackages():
    packages = ["xvfb",
                "xserver-xorg",
                "mesa-utils",
                "xinit",
                "xdotool",
                "linux-generic",
                "xterm",
                "htop",
                "i3",
                "xloadimage",
                "libgtk2.0-0",
                "libgconf-2-4"]
    installer(packages)


def download(url, path):
    try:
        with urllib.request.urlopen(url) as response:
            with open(path, 'wb') as outfile:
                shutil.copyfileobj(response, outfile)
    except:
        print("Failed to download", url)
        raise


def config_xorg():
    download("http://us.download.nvidia.com/tesla/418.67/NVIDIA-Linux-x86_64-418.67.run", "nvidia.run")
    pathlib.Path("nvidia.run").chmod(stat.S_IXUSR)
    subprocess.run(["./nvidia.run", "--no-kernel-module", "--ui=none"],
                   input="1\n", check=True, universal_newlines=True)

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


def config_i3():
    os.makedirs('/root/.config/i3/', exist_ok=True)
    shutil.move("./video-streamer/i3.conf", "/root/.config/i3/config")


def config():
    installPackages()
    print("Installed all the required packages.")
    config_xorg()
    print("xorg setup is done.")
    config_i3()
    print("i3 setup is done.")


def streamer(streamSecret, streamURL):
    xorg = subprocess.Popen(
        ["Xorg", "-seat", "seat-1", "-allowMouseOpenFail", "-novtswitch", "-nolisten", "tcp"])
    i3 = subprocess.Popen("i3", env=envc, shell=True)
    ffmpeg = subprocess.Popen(["ffmpeg", "-threads:v", "2", "-threads:a", "8", "-filter_threads", "2", "-thread_queue_size",
                               "512", "-f", "x11grab", "-s", "1920x1080", "-framerate", "30", "-i", ":0.0", "-b:v", "2400k",
                               "-minrate:v", "2400k", "-maxrate:v", "2400k", "-bufsize:v", "2400k", "-c:v", "h264_nvenc",
                               "-qp:v", "19", "-profile:v", "high", "-rc:v", "cbr_ld_hq", "-r:v", "60", "-g:v", "120",
                               "-bf:v", "3", "-refs:v", "16", "-f", "flv", streamURL + streamSecret])
    return (xorg, i3, ffmpeg)


def twitchStreamer(streamSecret, rtmpServer="rtmp://live.twitch.tv/app/"):
    return streamer(streamSecret, rtmpServer)


def youtubeStreamer(streamSecret, rtmpServer="rtmp://a.rtmp.youtube.com/live2/"):
    return streamer(streamSecret, rtmpServer)
