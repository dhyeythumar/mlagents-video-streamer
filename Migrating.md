## Migrating from v1.0 to v2.0

### Important changes

-   Replace `videostreamer` with `mlagents_video_streamer`.
-   Use `SetupVirtualDisplay()` instead of `config()`.
-   `twitchStreamer()` function has been removed, so use object given by `VideoStreamer` class.
-   Previously `twitchStreamer()` only took secret key, but now `VideoStreamer()` takes an dictonary in the following format **only**:
    ```python
    stream_info = {
    "URL": "rtmp://live.twitch.tv/app/", # example of Twitch URL
    "secret": "--- secret here ---"
    }
    ```
-   `start()` method by the `VideoStreamer` class should be used, before starting the training process.
-   `close()` method by the `VideoStreamer` class should be used, to close the video stream gracefully.
