# Training a CNN model for traffic light detection in Isaac Sim

In this tutorial series, we'll be training a traffic-light-detecting CNN model and integrating it onto our robot car in Isaac Sim 5.1.0. We'll start by using Isaac Sim Replicator feature to create our training data, then we'll process the data to then train our CNN detection model. Finally, we'll implement it onto our self-driving robot car simulation and have it navigate through a demo environment to see how well our model performs.

These guides assume you have already installed Visual Studio Code and have some basic knowledge of Isaac Sim 5.1.0, ROS2 Jazzy, OpenCV, and PyTorch.

In Part 3, we'll be deploying our traffic light CNN onto our simulated Isaac Sim 5.1.0 autonomous car, having it drive through multiple traffic lights while making sure it follows them well.

### Part 1
- Repository contains an Isaac Sim scene and the replicator code.

### Part 2
- Repository contains full model training pipeline notebooks.

### Part 3
- Repository contains the full simulation scene + accompanying assets for a simulation-based deployment.
- The car's ROS2 control code is at https://github.com/Alexledev/TrafficLightDetectionROS2
