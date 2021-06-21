import subprocess
import shutil
from datetime import datetime
import os

def printMsg(feedbackMsg, errMsg=""):
    print("-"*120)
    print(feedbackMsg)
    if errMsg != "":
        print("---")
        print("[ERR] :: ", errMsg)


def touch(path):
    open(path, 'a').close()


# Capturing video with constant bitrate of 6Mbps & framerate of 60 fps
class Streamer(object):
    def __init__(self, streamURL):
        if streamURL != "":
            self.ffmpegOutput = streamURL
        else:
            __dir = "./videos"
            if not os.path.exists(__dir):
                print("\nCreating directory for storing videos {}".format(__dir))
                os.makedirs(__dir, exist_ok=True)

            __date = datetime.now().strftime("(%Y.%m.%d)-(%I.%M.%S)-%p")
            self.ffmpegOutput = os.path.join(os.path.abspath(__dir), 'video_{}.mp4'.format(__date))
            touch(self.ffmpegOutput)  # just in case

        if shutil.which("ffmpeg") is not None:
            self.backend = "ffmpeg"
        else:
            raise Exception("No ffmpeg executable found!")

    def start(self):
        self.xorg = subprocess.Popen(
            ["Xorg", "-seat", "seat-1", "-allowMouseOpenFail", "-novtswitch", "-nolisten", "tcp"])

        self.cmdline = [
            self.backend,
            "-nostats",
            "-loglevel", "error",  # suppress warnings
            '-y',
            "-threads:v", "4",
            "-filter_threads", "4",
            "-thread_queue_size", "512",

            # input
            "-f", "x11grab",
            "-s", "1920x1080",  # size of one frame
            "-framerate", "60",
            "-i", ":0.0",  # The input comes from a virual screen at 0.0

            "-b:v", "6000k",  # bitrate
            "-minrate:v", "6000k",
            "-maxrate:v", "6000k",
            "-bufsize:v", "6000k",

            # output
            "-c:v", "h264_nvenc",
            "-rc:v", "cbr_ld_hq",
            "-r:v", "60",

            # "-qp:v", "19",
            # "-g:v", "120",
            "-profile:v", "high",
            "-bf:v", "3",  # lower CRF values correspond to higher bitrates,
            "-refs:v", "16",  # reference frames to consider for motion compensation
            "-f", "flv",
            self.ffmpegOutput
        ]
        self.proc = subprocess.Popen(self.cmdline, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def close(self):
        self.xorg.kill()  # .terminate()
        self.proc.kill()
