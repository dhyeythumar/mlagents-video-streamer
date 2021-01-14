# Video Streamer

<h4 align="center">
    Live stream the training process of Reinforcement Learning using the virtual screen from Google Colaboratory to Twitch.
</h4>

## Setup Instructions

1. Clone and Install the repo in Google Colab code cell.

```bash
!git clone https://github.com/Dhyeythumar/video-streamer.git
!pip install video-streamer/
```

2. Configure the video streamer.

```python
import videostreamer
videostreamer.config()
```

3. Activate the twitch streamer.

```python
xorg, i3, ffmpeg = videostreamer.twitchStreamer('<your-twitch-secret-key>')
```

4. To capture the running process, use the subprocess library.

The below example shows how to capture the training process in the case of ML-Agents:
```python
import subprocess
from random import randrange

train = subprocess.run(["mlagents-learn", "config.yaml", "--run-id=train-1", "--env=3DBall_example/3DBall.x86_64", "--base-port=" + str(randrange(9000, 9999))], cwd="/content/", stdout=subprocess.PIPE)
```
