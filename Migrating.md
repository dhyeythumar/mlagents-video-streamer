## Migrating the package from v1.0 to v2.0

### Important changes

-   replace `videostreamer` with `mlagents_video_streamer`.
-   use `SetupVirtualDisplay()` instead of `config()`.
-   `twitchStreamer()` function has been removed, so use `VideoStreamer` class.
-   Previously `twitchStreamer()` only took secret key, but now `VideoStreamer()` takes an dictonary in the following format **only**:
    ```python
    stream_info = {
    "URL": "rtmp://live.twitch.tv/app/", # example of Twitch URL
    "secret": "--- secret here ---"
    }
    ```
-   `start()` method by the `VideoStreamer` class should be used before starting the training process.
-   `close()` method by the `VideoStreamer` class should be used to close the stream gracefully.
