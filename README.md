Proof of concept of bokeh streaming.

How to run after cloning repo in local environment - requires Unix shell (e.g. Git Bash for Windows) and a virtual environment (e.g. virtualenv or pyenv) is suggested:
1) Install required packages ('pip install -r requirements.txt')
2) Run the loop.py program as a background process ('python loop.py &')
3) Run the app file in Bokeh ('bokeh serve --show stream.py')

Voila!
