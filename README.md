# <h1 align="center"> <b>Real-Time Hand Gesture Recognition and Augmented Reality (AR) Interface Using Computer Vision and Machine Learning</b><br></h1>
This project presents a real-time hand gesture recognition system combined with augmented reality (AR) visualizations, user interface (UI) control, and voice command integration. The system leverages computer vision (CV) and machine learning techniques to detect, track, and recognize hand gestures using the MediaPipe framework, implemented in a Python environment with OpenCV for video processing and visualization. This project has potential applications in human-computer interaction (HCI), augmented reality, and assistive technologies.

## Table of Contents
1. Overview
2. System Architecture
3. Functional Modules
4. Dependencies and Installation
5. Running the System
6. Future Improvements
## Objective Overview
The primary objective of this project is to develop an end-to-end pipeline for hand gesture recognition and tracking, augmented reality overlays, and real-time data visualization. The system identifies specific hand gestures based on detected landmark positions and translates these gestures into commands for controlling on-screen elements. Additionally, it integrates voice command recognition to expand the interaction capabilities and allow multimodal communication.

### System Architecture
This system is structured in a modular pipeline, as illustrated in Figure 1 below.

+-----------------+        +----------------+        +-------------------+
|  Video Capture  | -----> | Gesture Recognition | -----> | UI Control & AR Display |
+-----------------+        +----------------+        +-------------------+
                                        |
                             +-----------------+
                             | Voice Command   |
                             +-----------------+
                             |
                             V
                      +-------------------+
                      | Data Visualization |
                      +-------------------+

