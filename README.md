# Colorization black and white photo-video
**Note: Python 2.x is not supported**
<img src="https://camo.githubusercontent.com/ba2171fe9ab58bba2f169b740c35c26bd3cb4241/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f70796261646765732e737667" alt="versions" data-canonical-src="https://img.shields.io/pypi/pyversions/pybadges.svg" style="max-width:100%;">

### Python packages
* numpy
* OpenCv
* PyQt5
* imageio

[![](tmp/color.jpg)]( https://youtu.be/s0WRdNgKHTQ "")




Clone the master branch of the respository using git clone -b master --single-branch https://github.com/RashadGarayev/ColorizeImage.git


```cd ColorizeImage```

Install the required packages by executing the following command.

`$ pip3 install -r requirements.txt`
### Usage

### Installation caffe model
`$ cd models/` 

`$ wget http://eecs.berkeley.edu/~rich.zhang/projects/2016_colorization/files/demo_v2/colorization_release_v2.caffemodel -O ./models/colorization_release_v2.caffemodel`

`$ cd ..`

`$ python3 main.py` 

---------------------------------------------------------------------------------------------------------------------------
#### Tested


![Conv](tmp/color.jpg)      ![Conv](tmp/color1.jpg)
