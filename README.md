# ML-Agents Video Streamer

<h4 align="center">
Now you can Live Stream the Agent's learning behavior to Twitch/YouTube from Google Colab while training these Agents.
</h4>

---

<div align="center">
    <p>Try Google Colab Notebook</p>
    <p>
        <a href="https://colab.research.google.com/github/dhyeythumar/mlagents-video-streamer/blob/v2.0/Streaming ML-Agents from Colab -v2.0.ipynb">
          <img alt="colab link" src="https://colab.research.google.com/assets/colab-badge.svg" />
        </a>
    </p>
</div>

---

## What’s In This Document

-   [Installation](#installation)
-   [Imports and Usage](#imports-and-usage)
-   [License](#license)

## Installation

```bash
!pip install mlagents-video-streamer
```

And if you already have `mlagents-video-streamer` then upgrade it by this command.

```bash
!pip install --upgrade mlagents-video-streamer
```

## Imports and Usage

```python
from mlagents_video_streamer import SetupVirtualDisplay
from mlagents_video_streamer import VideoStreamer
```

-   Now Setup the Virtual Display:

    ```python
    SetupVirtualDisplay()
    ```

-   Define your live stream information:

    ```python
    # stream_info dictionary should be in this format only
    stream_info = {
        "URL": "rtmp://live.twitch.tv/app/", # example of Twitch URL
        "secret": "--- secret here ---"
    }
    ```

-   Initialize the `VideoStreamer` class with `stream_info`:

    ```python
    videoStreamer = VideoStreamer(stream_info)
    ```

    \*_If you don't pass `stream_info` then it will simply store the video locally in the `videos` directory._

-   Start the video streamer before starting with the training process:

    ```python
    videoStreamer.start()
    ```

-   Now capture the training process, using subprocess library:

    ```python
    import subprocess
    from random import randrange

    try:
        train = subprocess.run([
            "mlagents-learn", 
            "config.yaml",
            "--run-id=train-1",
            "--env=3DBall_example/3DBall.x86_64",
            "--base-port=" + str(randrange(9000, 9999))
        ],
            cwd="/content/", stdout=subprocess.PIPE)
        print("Training process has been successfully ended.")
    except Exception as e:
        print("You killed the training process in between.")
    finally:
        videoStreamer.close()
    ```

    \*_At the end don't forget to close the video streamer by using `close()` method on `videoStreamer` object as shown in the above example._

## License

Licensed under the [MIT License](./LICENSE).
