from .streamer import printMsg, Streamer

STREAM_INFO_ERR_MSG = "The provided Stream Info dictionary is not correctly passed!\n\
Video won't be streamed. Instead it will be stored locally @ ./videos/"

class VideoStreamer(object):
    def __init__(self, streamInfo=None):
        self.Streamer = None
        self.enabled = True
        self.streamURL = ""

        try:
            if ((streamInfo is not None) and (streamInfo["URL"] != "") and (streamInfo["secret"] != "")):
                self.streamURL = streamInfo["URL"] + streamInfo["secret"]
            else:
                printMsg(STREAM_INFO_ERR_MSG)
        except Exception as e:
            printMsg(STREAM_INFO_ERR_MSG, e)

        try:
            self.Streamer = Streamer(self.streamURL)
            printMsg("Video Streamer is ready to stream.")
        except Exception as e:
            self.enabled = False
            printMsg("Exception while creating streamer object.", e)

    def start(self):
        if self.enabled is True:
            try:
                self.Streamer.start()
                printMsg("Video Streamer/Recorder started.")
            except Exception as e:
                self.enabled = False
                printMsg("Exception while starting streamer object.", e)
        else:
            printMsg("Video Streamer is not enabled this might be due to an exception or you closed the streamer. Reinitialize the VideoStreamer object an try again.")

    def close(self):
        if self.enabled is True:
            try:
                self.Streamer.close()
                printMsg("Video Streamer successfully closed.")
            except Exception as e:
                printMsg("Exception while closing streamer object.", e)
        else:
            printMsg("Video Streamer is not enabled this might be due to an exception or you closed the streamer. Reinitialize the VideoStreamer object an try again.")
