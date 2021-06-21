# Video Streamer

<h4 align="center">
    Live stream the training process of ML-Agents (toolkit for Reinforcement Learning with Unity Engine) using the virtual screen from Google Colab to Twitch.
</h4>

## Installation

```bash
!pip install mlagents-video-streamer
```

-   Configure the video streamer.

    ```python
    import videostreamer
    videostreamer.config()
    ```

-   Activate the twitch streamer.

    ```python
    xorg, ffmpeg = videostreamer.twitchStreamer('<your-twitch-secret-key>')
    ```

-   To capture the running process, use the subprocess library.

    The below example shows how to capture the training process in the case of ML-Agents:

    ```python
    import subprocess
    from random import randrange

    train = subprocess.run(["mlagents-learn", "config.yaml", "--run-id=train-1", "--env=3DBall_example/3DBall.x86_64", "--base-port=" + str(randrange(9000, 9999))], cwd="/content/", stdout=subprocess.PIPE)
    ```
