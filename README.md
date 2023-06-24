# Intelligent-Transportation-System
 My Bachlor Graduation Project
This system aims to monitor and analyze the movement of vehicles in real-time, detect traffic congestion, and predict traffic flow using computer vision and deep learning techniques.

## How It Works
### Data Collection:
<ul>
<li>Video footage from traffic light cameras is captured.</li>
<li>The video stream is received and processed by the system.</li>
</ul>

### Vehicle Detection:

<ul>
<li>YOLOv7 is used for vehicle detection in each frame of the video.</li>
<li>Detected vehicles are assigned unique identifiers and their coordinates are tracked.</li>
</ul>

### Vehicle Tracking:

<ul>
<li>The SORT (Simple Online and Realtime Tracking) algorithm is used for vehicle tracking.</li>
<li>Kalman filtering is utilized to estimate vehicle positions and handle occlusions.</li>
</ul>

### Data Extraction:
<ul>
<li>The system extracts relevant data for each vehicle, including its ID, type, and centroid coordinates in each frame.</li>
</ul>

### Traffic Flow Prediction:

<ul>
<li>Pre-processed data is used to develop a traffic flow prediction model.</li>
<li>Gated Recurrent Units (GRU) model was used for traffic flow prediction.</li>
<li>The training data is divided into chunks, and MinMax scalar is applied for data pre-processing.</li>
</ul>

### Route Recommendation:

<ul>
<li>Based on the traffic flow predictions, the system determines the usability of different routes.</li>
<li>If the predicted traffic congestion exceeds a certain threshold, the system suggests avoiding the route.</li>
</ul>

## Features and Benefits
<ul>
<li>Real-time monitoring and analysis of road traffic.</li>
<li>Accurate vehicle detection and tracking.</li>
<li>Reliable traffic flow predictions based on historical data.</li>
<li>Route recommendations to avoid congested areas.</li>
<li>Potential to enhance road safety and reduce CO2 emissions.</li>
</ul>

## Requirements
<ul>
<li>Python 3.x</li>
<li>OpenCV</li>
<li>PyTorch and TensorFlow (for machine vision models)</li>
<li>Scikit-learn (for data pre-processing)</li>
<li>NumPy, Pandas (for data manipulation)</li>
<li>Matplotlib (for visualization)</li>
</ul>
