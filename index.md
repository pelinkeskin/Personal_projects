---
layout: default
---

# Personal Projects

<p>This repository contains personal projects I did in my free time and during my CS Masters's degree.</p>

### [Kaggle Forecasting Mini-Course Sales](https://github.com/pelinkeskin/Personal_projects/tree/main/Kaggle_Forecasting_Mini-Course_Sales) (07/2023)
This folder contains my submission for the [Kaggle Forecasting Mini-Course Sales competition](https://www.kaggle.com/competitions/playground-series-s3e19). This competition involved forecasting sales with synthetically generated time series datasets. Unfortunately, [This post](https://www.kaggle.com/competitions/playground-series-s3e19/discussion/425538) revealed that this dataset had data construction errors on the test set which is being used to calculate the leaderboard scores. Such that, all countries had different base levels for the target feature at the train set but the same base level in the test set. There was no way to predict this other than probing the public leaderboard and no way to adjust to this other than shifting predictions up and down to match flawed test data. I shifted my predictions because that would no longer be predictive modelling, but some contestants did to score high on the leaderboard. As a result, while the leaderboard scores might be unreliable in assessing the performance of the developed models, I enjoyed practicing time features engineering and experimenting with Prophet and CatBoost for forecasting with time-series data.  This notebook is publicly available and open for comments on [Kaggle](https://www.kaggle.com/code/pelinkeskin/prophet-catboost-ensemble)

### [Kaggle ConnectX RL Competition](https://github.com/pelinkeskin/Personal_projects/tree/main/Kaggle_ConnectX_ML_Competition) (07/2023) 
This folder contains my submission for the [Kaggle ConnectX Reinforcement Learning competition](https://www.kaggle.com/competitions/connectx/overview). The ConnectX competition involves training an AI agent to play Connect4, and contestants are required to submit their agent in a Python file for evaluation on the leaderboard. This leaderboard is updated dynamically to include scores from all submissions. Within the ConnectX_LeaderScore_Apprx300.ipynb notebook,I have developed an AI agent that currently holds a position of approximately 300 on the leaderboard. The agent was trained using the Stable_baseline3 PPO algorithm for 1 million timesteps in the Gymnasium environment, with linear learning-rate decay. I have created a function that enables dynamic prediction of the agent's actions by passing trained action network parameters (transforms, weights, biases) to an equivalent deep neural network developed using PyTorch that returns predictions. This notebook is publicly available and open for comments on [Kaggle](https://www.kaggle.com/code/pelinkeskin/deep-rl-with-stable-baseline3-and-gymnasium-ppo).

### [Exploratory data analysis on Kaggle Datasets](https://github.com/pelinkeskin/Personal_projects/tree/main/EDAonKaggleDatasets) (07/2023) 
This folder contains notebooks I created for exploratory data analysis and visualisation of interesting datasets obtained from Kaggle. 
AI,ML,DS,BigData_Jobs_Analysis.ipynb: I analyzed the [Scraped Data on AI, ML, DS & Big Data Jobs](https://www.kaggle.com/datasets/joyshil0599/data-science-jobs-comprehensive-dataset) dataset to gather useful insights on job prospects in AI, ML, DS, and Big Data. This notebook is publicly available and open for comments on [Kaggle](https://www.kaggle.com/code/pelinkeskin/analysing-the-data-on-ai-ml-ds-big-data-jobs).

### [Kaggle Titanic ML Competition](https://github.com/pelinkeskin/Personal_projects/tree/main/Kaggle_Titanic_ML_Competition) (06/2023)
This folder contains notebooks I submitted to the [Kaggle Titanic Machine Learning competition](https://www.kaggle.com/competitions/titanic). Titanic competition is about developing a model that makes binary classifications from tabular data of Titanic's passengers.  Kaggle_Titanic_Ensembles(Top_6%).ipynb was my first notebook, and I achieved a ranking within the top 6% with a 0.79425 leader score by using an Ensemble of SVC, RFC, XGBoost, and CatBoost classifiers. Kaggle_Titanic_Final_RFC_SVC_XGB.ipynb is my second notebook. I used RFC, XGB and SVC classifiers and my SVC in this notebook managed to get a 0.79186 leader score. I performed extensive data exploration with visualisation and feature engineering in my second notebook. I used a combination of statistical and wrapper methods for feature evaluation and selection. I utilised gridsearchcv with an exhaustive feature selection to finalise feature lists and determine starting parameters for the models. This notebook is publicly available and open for comments on [Kaggle](https://www.kaggle.com/code/pelinkeskin/randomforest-supportvector-xgboost).

### [AI_flappybird_player_Deep_Reinforcement_Learning](https://github.com/pelinkeskin/Personal_projects/tree/main/AI_flappybird_player_Deep_Reinforcement_Learning) (04/2023)
I completed this project as part of an assignment in one of my modules during my Masters. The project involved training an AI agent that plays the Flappy Bird game using deep reinforcement learning. In this project, I used Stable Baselines 3 to train a neural network to control the bird in the [Flappy Bird environment](https://github.com/markub3327/flappy-bird-gymnasium). I used an actor-critic algorithm with (PPO) proximal policy optimisation to create the network to train a vector agent and an Image stack agent to play the flappy bird game. To train the vector agent, I used the FlappyBird-v0 environment and MlpPolicy, the other hyperparameters of the network, for training the PPO agent provided to us in the assignment. To train the image stack agent, I used FlappyBird-rgb-v0 environment but resized images to 64*128, changed to grey-scale and stacked four frames together, and I used CnnPolicy, the other hyperparameters of the network for training the PPO agent provided to us in the assignment. The number of trainable weights and biases in the vector agent model was 10,179, and in the image stack agent model was 4,955,619. Therefore, training took a very long time, and even after 500.000-time step models were undertrained, I didn't continue training due to computational limitations. The best performance evaluated for 30 episodes after training for  500,000 timesteps was 11.83 mean award of image stack agent. 

### [Building an Interactive dashboard with Vega-Lite to visualise nuclear explosions worldwide](https://github.com/pelinkeskin/Personal_projects/tree/main/Interactive_dashboard_Vega-Lite) (04/2023)
I created an interactive dashboard using Vega-Lite for visual storytelling as part of an assignment for my CS master's degree. I aimed to allow users to explore the relationship between countries that deploy nuclear devices, the purposes of detonations, the methods of deployment, explosion yields, and locations of the explosions. To use the tool, download the HTML file in this folder, open it with the browser and enjoy using this interactive tool. The dataset used for this visualisation tool was adapted from [the 2019 Tidy Tuesday Collection dataset](https://github.com/rfordatascience/tidytuesday/tree/master/data/2019/2019-08-20). The record of my visual storytelling through the utilisation of this dashboard is currently accessible on [youtube](https://youtu.be/KpmABg-ydCg)

### [Deep Learning: Building CNN to recognise monkey species from disparate images](https://github.com/pelinkeskin/Personal_projects/tree/main/image_classification_with_CNN) (03/2023)
I completed this project as part of an assignment in one of my modules during my Masters. The project involved building a deep convolutional neural network model to recognise monkey species from disparate images. [The monkey species classification tasks from Kaggle](https://www.kaggle.com/slothkong/10-monkey-species/home) involved identifying ten species of monkeys from disparate image types. My task was to build an accurate classification model for this scenario using different CNN models. I first trained the LeNet type CNN model, then replaced the convolutional layers with the VGG-16 model (pre-trained on the Image Net dataset) and improved accuracy—weighted average accuracy score: 0.72.

### [Building Gradient Boosting Regressor from Scratch with Python](https://github.com/pelinkeskin/Personal_projects/tree/main/self-built_GradientBoosting_Regressor) (03/2023)
I completed this project as part of an assignment in one of my modules during my Masters. The project involved creating a gradient-boosting regressor for continuous prediction problems by inheriting from appropriate scikit-learn base classes. The implementation allowed the subsampling of rows in the samples and included a learning rate hyperparameter. I tested my self-built algorithm against sklearn Adaboost regressor on [commonlitreadabilityprize dataset](https://www.kaggle.com/competitions/commonlitreadabilityprize) 's bag of words and sentence embedding representations. After tuning the hyperparameters for both models, my self-built gradient boosting regressor showed slightly better prediction performance than sklearn's AdaBoost algorithm. 

### [A small study to assess word frequencies across data analytics job ads](https://github.com/pelinkeskin/Personal_projects/tree/main/JobAdsWordFreqEval) (12/2022)
I created this notebook to gain insight into the common traits employers currently look for in data analytics roles by examining a set of job ads posted on Linkedin.

### [Building Multi-Layer Neural Network from Scratch with Python](https://github.com/pelinkeskin/Personal_projects/tree/main/Multi-Layer_Neural_Network_from_Scratch) (12/2022)
I implemented a Multi-Layer Neural Network from Scratch with Python for one of my modules during my Masters. The implemented network was a shallow multi-layer neural network of 1 hidden layer. The network could take any number of inputs, any number of outputs, and any number of hidden units. Learning implemented by backpropagation using batch gradient descent. The network is implemented to be flexible. It can handle regression and classification tasks and utilise different activation functions for hidden and output units depending on the user's choice. In the classification task, the network used a leaky rectified linear unit activation function for hidden layer activation. For output layer activations, it used sigmoid activation functions for binary classification and softmax activation functions for multiclass classification. The network used a log loss cost function to observe training performance for classification. For regression, output wasn't activated, and for the hidden layer, the user was given a choice to select from various activation functions: sigmoid function, hyperbolic tangent function, leaky rectified linear unit function, and binary step function. The network used the square error cost function to observe training performance for regression. Implemented network tested on two classification tasks, which were to predict XOR function, letter recognition and one regression task to approximate a sin function. Test results are available in separate notebooks. [Source of the dataset for letter recognition](http://archive.ics.uci.edu/ml/datasets/Letter+Recognition)

### [Analysing Books with Hadoop & Data Exploration with PySpark](https://github.com/pelinkeskin/Personal_projects/tree/main/Big_Data_Exploration_Hadoop_PySpark) (12/2022)
This is a combination of two projects I made for one of my modules during my Masters to gain practical experience in using big data management tools, Hadoop and Spark. To complete Hadoop tasks, I loaded three books to HDFS and wrote map-reduce tasks with Python to analyse books. To complete PySpark tasks, I analysed the wordle game dataset extracted from Twitter  by utilising a sparks multiprocessing framework with RDDs and Dataframes. 

### [Building Time-Related Feature Engineering Pipelines with Python](https://github.com/pelinkeskin/Personal_projects/tree/main/Time-Related_Feature_Engineering) (11/2022)
I built Time-Related Feature Engineering Pipelines with Python to predict [traffic volumes](https://archive.ics.uci.edu/ml/datasets/Metro+Interstate+Traffic+Volume ). I completed this project as part of an assignment in one of my modules during my Masters.  I performed time-related feature engineering by encoding time features using cyclic_spline_transformer and used wrapper strategy with sequential forward selection for feature selection. I built a predictive model using Stochastic Gradient Descent regression with polynomial transformation and achieved 85% accuracy in predicting traffic volumes.

### [Designing a Data Warehouse & Association Rule Mining using SQL and Python](https://github.com/pelinkeskin/Personal_projects/tree/main/DatawareHousing_AssociationRule_Mining) (10/2022)
I completed these tasks as part of an assignment in one of my modules during my Masters. This folder contains two notebooks; In Data_Warehousing_practice.ipynb I created a database and made a set of OLAP queries to explore the data. Then I defined a fact constellation schema diagram for the data warehouse with facts, dimensions, and measures and addressed steps for specific OLAP operations to perform  to answer a particular query. Then use PostgreSQL Python and its libraries and define a set of functions to operate the data warehouse. In Association_Rule_Mining_Practice.ipynb,  I cleaned and transformed an online retail dataset for association rule mining, then mined association rules using Apriori and FP-growth algorithms.

### [Implementing a small Database Management System with Bash](https://github.com/pelinkeskin/Personal_projects/tree/main/DBMS_BASH) (11/2021)
I implemented a small database management system in Bash for one of my modules during my Masters. Data exchange between client and server for data entry and query provided through pipes. The system supported concurrent execution and protected against synchronisation problems with the effective use of semaphores. The system was able to create a database, create a table, insert rows in tables at existing databases and allowed to query the tables at targeted databases as a whole or with column indexes to display content.

### [My CodeWars Solutions](https://github.com/pelinkeskin/Personal_projects/tree/main/codewars_solns) (on-going)
This folder contains small scripts I write to solve various coding challenges in Codewars in my free time.