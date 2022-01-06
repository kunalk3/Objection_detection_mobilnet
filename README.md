<div align="right">
<img src="https://user-images.githubusercontent.com/41562231/141720820-090897f9-f564-45e2-9265-15c1269db795.png" height="120" width="900">
</div>

# __Objection Detection__ (using mobilnet)
Object detection is a computer technology related to computer vision and image processing that deals with detecting instances of the semantic objects of a certain class (such as humans, buildings, or cars) in digital images and videos. __MobilenetSSD__ is an object detection model that computes the bounding box and category of an object from an input image. This Single Shot Detector (SSD) object detection model uses Mobilenet as backbone and can achieve fast object detection optimized for mobile devices.

<div align="center">
  <a href="https://github.com/kunalk3/Objection_detection_mobilnet/issues"><img src="https://img.shields.io/github/issues/kunalk3/Objection_detection_mobilnet" alt="Issues Badge"></a>
  <a href="https://github.com/kunalk3/Objection_detection_mobilnet/graphs/contributors"><img src="https://img.shields.io/github/contributors/kunalk3/Objection_detection_mobilnet?color=872EC4" alt="GitHub contributors"></a>
  <a href="https://www.python.org/downloads/release/python-390/"><img src="https://img.shields.io/static/v1?label=python&message=v3.9&color=faff00" alt="Python 3.9"</a>
  <a href="https://github.com/kunalk3/Objection_detection_mobilnet/blob/main/LICENSE"><img src="https://img.shields.io/github/license/kunalk3/Objection_detection_mobilnet?color=019CE0" alt="License Badge"/></a>
  <a href="https://github.com/kunalk3/Objection_detection_mobilnet"><img src="https://img.shields.io/badge/lang-eng-ff1100"></img></a>
  <a href="https://github.com/kunalk3/Objection_detection_mobilnet"><img src="https://img.shields.io/github/last-commit/kunalk3/Objection_detection_mobilnet?color=309a02" alt="GitHub last commit">
</div>
  
<div align="center">   
  
  [![Windows](https://img.shields.io/badge/WindowsOS-000000?style=flat-square&logo=windows&logoColor=white)](https://www.microsoft.com/en-in/)
  [![Visual Studio Code](https://img.shields.io/badge/VSCode-0078d7.svg?style=flat-square&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
  [![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?style=flat-square&logo=Jupyter&logoColor=white)](https://jupyter.org/)
  [![Pycharm](https://img.shields.io/badge/Pycharm-41c907.svg?style=flat-square&logo=Pycharm&logoColor=white)](https://www.jetbrains.com/pycharm/)
  [![Colab](https://img.shields.io/badge/Colab-F9AB00.svg?style=flat-square&logo=googlecolab&logoColor=white)](https://colab.research.google.com/?utm_source=scs-index/)
  [![Spyder](https://img.shields.io/badge/Spyder-838485.svg?style=flat-square&logo=spyder%20ide&logoColor=white)](https://www.spyder-ide.org/)
  [![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg?style=flat-square&logo=spyder%20ide&logoColor=white)](https://share.streamlit.io/)
</div>
  
<div align="center">
  
  [![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat&logo=linkedin&logoColor=white&color=0078d7)](https://www.linkedin.com/in/kunalkolhe3/)
  [![Github Badge](https://img.shields.io/badge/Github-Profile-informational?style=flat&logo=github&logoColor=white&color=black)](https://github.com/kunalk3/)
  [![Gmail Badge](https://img.shields.io/badge/Gmail-Profile-informational?style=flat&logo=Gmail&logoColor=white&color=e44e4e)](mailto:kunalkolhe333@gmail.com)
  [![Facebook Badge](https://img.shields.io/badge/Facebook-Profile-informational?style=flat&logo=facebook&logoColor=white&color=0078d7)](https://www.facebook.com/kunal.kolhe.98/)
  [![Instagram Badge](https://img.shields.io/badge/Instagram-Profile-informational?style=flat&logo=Instagram&logoColor=white&color=c90076)](https://www.instagram.com/kkunalkkolhe/)
</div>
  
---
  
## :wrench: Overview:
- The SSD architecture is a single convolution network that learns to predict bounding box locations and classify these locations in one pass. Hence, SSD can be trained end-to-end. By using SSD, we only need to take one single shot to detect multiple objects within the image, while regional proposal network (RPN) based approaches such as R-CNN series that need two shots, one for generating region proposals, one for detecting the object of each proposal. Thus, SSD is much faster compared with two-shot RPN-based approaches.
- Mobilenet SSD takes a (3,300,300) image as input and outputs (1,3000,4) boxes and (1,3000,21) scores. Boxes contains offset values (cx,cy,w,h) from the default box. 

![img1](https://user-images.githubusercontent.com/41562231/148023095-f1c2481c-ab97-46c6-9e92-439ad4afe881.JPG)

- Create __virtual environment__ `python -m venv VIRTUAL_ENV_NAME` and activate it `.\VIRTUAL_ENV_NAME\Scripts\activate`.
- Install necessary library for this project from the file `requirements.txt` or manually install by `pip`.
  ```
  pip install -r requirements.txt
  ```
  To create project library requirements, use below command,
  ```
  pip freeze > requirements.txt
  ```
- ```python
    # Below are the clsses that model can detect live
    CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow",
            "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
  ```
- Run app.py python file
  ``` 
  python run app.py
  ```
  
---  

## :bulb: Demo
#### :bookmark: _Output_ - 
https://user-images.githubusercontent.com/41562231/148024403-02a1a55d-d4b3-4354-b1df-bf51d4beaa8b.mp4


---  
  
## :bookmark: Directory Structure 
```bash
    .                                           # Root directory
    ├── ssd                                     # Model directory
    │   ├── MobileNetSSD_deploy.caffemodel      # MobileNetSSD Model
    │   └── MobileNetSSD_deploy.prototxt.txt    # prototype data file
    ├── static                                  # Website data
    │   ├── css                                 # Css effect files
    │   ├── downloads                           # Resultant files
    │   ├── fonts                               # Fonts files
    │   ├── img                                 # Static images
    │   ├── js                                  # Javascript effect files
    │   ├── uploads                             # Upload files for object dettection
    ├── templates                               # Template directory
    │   ├── index.html                          # Index page
    │   ├── error_404.html                      # Error page
    ├── Aptfile                                 # Apt-based dependencies (Heroku: compile + runtime)
    ├── Procfile                                # App init (init: app + server: gunicorn)
    ├── app.py                                  # Application main file
    ├── classes.py                              # Object detection handler with model and classes
    ├── requirements.txt                        # Project requirements library with versions
    ├── README.md                               # Project README file
    └── LICENSE                                 # Project License file
```
---  

## :cloud: Live Application
__Live Aplication__ is running on heroku cloud platform, you can access from below.
  
[Live App](https://object-detection-app-k1.herokuapp.com/)
  
---
  
### :iphone: Connect with me
`You say freak, I say unique. Don't wait for an opportunity, create it.`
  
__Let’s connect, share the ideas and feel free to ping me...__
  
<div align="center"> 
  <p align="left">
    <a href="https://linkedin.com/in/kunalkolhe3" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/linkedin.svg" alt="kunalkolhe3" height="30" width="40"/></a>
    <a href="https://github.com/kunalk3/" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg" alt="kunalkolhe3" height="30" width="40"/></a>
    <a href="https://fb.com/kunal.kolhe.98" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/facebook.svg" alt="kunal.kolhe.98" height="30" width="40"/></a>
    <a href="mailto:kunalkolhe333@gmail.com" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/gmail.svg" alt="kunalkolhe333" height="30" width="40"/></a>
    <a href="https://instagram.com/kkunalkkolhe" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/instagram.svg" alt="kkunalkkolhe" height="30" width="40"/></a>
    <a href="https://www.hackerrank.com/kunalkolhe333" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/hackerrank.svg" alt="kunalkolhe333" height="30" width="40"/></a>
  </p>
</div>
  
<div align="left">
<img src="https://user-images.githubusercontent.com/41562231/141720940-53eb9b25-777d-4057-9c2d-8e22d2677c7c.png" height="120" width="900">
</div>
