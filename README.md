# Training a CNN model for traffic light detection in Isaac Sim

In this tutorial series, we'll be training a traffic-light-detecting CNN model and integrating it onto our robot car in Isaac Sim 5.1.0. We'll start by using Isaac Sim Replicator feature to create our training data, then we'll process the data to then train our CNN detection model. Finally, we'll implement it onto our self-driving robot car simulation and have it navigate through a demo environment to see how well our model performs.

These guides assume you have already installed Visual Studio Code and have some basic knowledge of Isaac Sim 5.1.0, ROS2 Jazzy, OpenCV, and PyTorch.

In Part 1, we'll cover the process of generating synthetic training data using Isaac Sim Replicator. This includes preparing the simulation environment, configuring Replicator, setting up automatic annotations, and fine-tuning the data generation process to produce a suitable dataset for training our traffic light detection model.

### Part 1
- Repository contains an Isaac Sim scene and the replicator code. 
