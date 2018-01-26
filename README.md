Proof of concept of bokeh streaming.

**What's here**:
* loop.py generates output.txt file, populating it with a timestamp and random integer pairing every given interval while it runs
* stream.py shows summary statistics (count, mean, min, max) for a rolling block of the most recent entries from the output.txt file

**How to run** after cloning repo in local environment - requires Unix shell (e.g. Git Bash for Windows) and a virtual environment (e.g. virtualenv or pyenv) is suggested:
1. Install required packages ('pip install -r requirements.txt'). *Note that bokeh APIs are still quite unstable and I have only tested on v0.12.13*.
2. Run the loop.py program as a background process ('python loop.py &')
3. Run the app file in Bokeh ('bokeh serve --show stream.py')

Voila.
