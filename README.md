# Personal_projects
<p>This repository contains personal projects I did in my free time and during my CS Masters's degree.</p>
 <p align="justify">
<strong>Kaggle_My_Solo_Competition_Notebooks:(06/2023)</strong> <br />
This file contains notebooks I submitted to Kaggle competitions. Kaggle_Titanic_Ensembles (Top_6%).ipynb was my first notebook, and I achieved a ranking within the top 6% with a 0.79425 leader score by using an Ensemble of SVC, RFC, XGBoost, and CatBoost classifiers. Kaggle_Titanic_Final_RFC_SVC_XGB.ipynb is my second notebook. I used RFC, XGB and SVC classifiers and my SVC in this notebook managed to get a 0.79186 leader score. I performed extensive data exploration with visualisation and feature engineering in my second notebook. For feature evaluation and selection, I used a combination of statistical and wrapper methods. Such that; I utilised gridsearchcv with an exhaustive feature selection to finalise feature lists and determine starting parameters for the models. This notebook is publicly available and open for comments on my Kaggle page. 
My Kaggle page: https://www.kaggle.com/pelinkeskin  <br/>
 </p>
 <p align="justify">
<strong>AI_flappybird_player_Deep_Reinforcement_Learning:(04/2023)</strong> <br /> 
I completed this project as part of an assignment in one of my modules during my Masters. The project involved training an AI agent that plays the Flappy Bird game using deep reinforcement learning. In this project, I used Stable Baselines 3 to train a neural network to control the bird in the Flappy Bird environment (https://github.com/markub3327/flappy-bird-gymnasium). I used an actor-critic algorithm with (PPO) proximal policy optimisation to create the network to train a vector agent and an Image stack agent to play the flappy bird game. To train the vector agent, I used FlappyBird-v0 environment, and I used MlpPolicy, the other hyperparameters of the network, for training the PPO agent provided to us in the assignment. To train the image stack agent, I used FlappyBird-rgb-v0 environment but resized images to 64*128, changed to grey-scale and stacked 4 frames together, and I used CnnPolicy, the other hyperparameters of the network for training the PPO agent provided to us in the assignment. The number of trainable weights and biases in the vector agent model was 10,179, and in the image stack agent model was 4,955,619. Therefore, training took a very long time, and even after 500.000-time step models were undertrained, I didn't continue training due to computational limitations. The best performance evaluated for 30 episodes after training for  500,000 timesteps  was 11.83 mean award of  image stack agent. 
  <br/>
 </p>
  <p align="justify">
<strong>Interactive_Dashboard_Vega-Lite (Nuclear Explosions Across the Globe):(04/2023)</strong> <br /> 
I created an interactive dashboard using Vega-Lite for visual storytelling as part of an assignment for my CS master's degree. My aim was to allow users to explore the relationship between countries that deploy nuclear devices, the purposes of detonations, the methods of deployment, explosion yields, and locations of the explosions. To use the tool, download the HTML file in this folder, open it with the browser and enjoy using this interactive tool. The dataset used for this visualisation tool was adapted from the 2019 Tidy Tuesday Collection dataset: https://github.com/rfordatascience/tidytuesday/tree/master/data/2019/2019-08-20
The record of my visual storytelling through the utilisation of this dashboard is currently accessible at: https://youtu.be/KpmABg-ydCg <br/>
 </p>
 <p align="justify">
<strong>image_classification_with_CNN:(03/2023)</strong> <br /> 
I completed this project as part of an assignment in one of my modules during my Masters. The project involved building a deep convolutional neural network model to recognise monkey species from disparate images. The monkey species classification tasks from Kaggle https://www.kaggle.com/slothkong/10-monkey-species/home involved recognising 10 species of monkey from disparate image types. My task was to build an accurate classification model for this scenario using different types of CNN models. I first trained the LeNet type CNN model, then replaced the convolutional layers with the VGG-16 model (pre-trained on the Image Net dataset) and improved accuracy. Weighted average accuracy score: 0.72.
  <br/>
 </p>
 <p align="justify">
<strong>self-built GradientBoostingRegressor:(03/2023)</strong> <br />
I completed this project as part of an assignment in one of my modules during my Masters. The project involved creating a gradient-boosting regressor for continuous prediction problems by inheriting from appropriate scikit-learn base classes. The implementation allowed the subsampling of rows in the samples and included a learning rate hyperparameter. I tested my self-built algorithm against sklearn Adaboost regressor on commonlitreadabilityprize dataset's bag of words and sentence embedding representations. After tuning the hyperparameters for both models, my self-built gradient boosting regressor showed slightly better prediction performance than sklearn's AdaBoost algorithm. The dataset used in the project is available at: https://www.kaggle.com/competitions/commonlitreadabilityprize.
 <br/>
  </p>
 <p align="justify">
<strong>JobAdsWordFreqEval:(12/2022)</strong> <br />
Self-designed small-scale text analytics study to assess word frequencies across data analytics job ads at LinkedIn, which helps gain insight into the common traits employers currently look for in data analytics roles.  <br />
  </p>
 <p align="justify">
<strong>Multi-Layer_Neural_Network_from_Scratch :(12/2022)</strong> <br />
I implemented a Multi-Layer Neural Network from Scratch with Python for one of my modules during my Masters. The implemented network was a shallow multilayer neural network of 1 hidden layer. The network could take any number of inputs, any number of outputs, and any number of hidden units. Learning implemented by backpropagation using batch gradient descent. The network is implemented to be flexible. It can handle regression and classification tasks and utilise different activation functions for hidden and output units depending on the user’s choice. In the classification task, the network used a leaky rectified linear unit activation function for hidden layer activation. For output layer activations, it used sigmoid activation functions for binary classification and softmax activation functions for multiclass classification. The network used a log loss cost function to observe training performance for classification. For regression, output wasn’t activated, and for the hidden layer, the user was given a choice to select from various activation functions: sigmoid function, hyperbolic tangent function, leaky rectified linear unit function, and binary step function. The network used the square error cost function to observe training performance for regression. Implemented network tested on two classification tasks, which were to predict XOR function, letter recognition and one regression task to approximate a sin function. Test results are available in separate notebooks. Source of the dataset for letter recognition: http://archive.ics.uci.edu/ml/datasets/Letter+Recognition  <br/>
  </p>
<p align="justify">
<strong>Big_Data_Exploration_Hadoop_PySpark:(12/2022)</strong> <br />
This is a combination of two projects I made for one of my modules during my Masters to gain practical experience in using big data management tools, Hadoop and Spark. To complete Hadoop tasks, I loaded 3 books to HDFS and write map-reduce tasks with Python to analyse books. To complete PySpark tasks, I analysed the wordle game dataset extracted from Twitter  by utilising a sparks multiprocessing framework with RDDs and Dataframes. 
 <br /> 
</p>
 <p align="justify">
<strong>Time-Related_Feature_Engineering :(11/2022)</strong> <br />
I built Time-Related Feature Engineering Pipelines with Python to predict traffic volumes. I completed this project as part of an assignment in one of my modules during my Masters.  I performed time-related feature engineering by encoding time features using cyclic_spline_transformer and used wrapper strategy with sequential forward selection for feature selection. I built a predictive model using Stochastic Gradient Descent regression with polynomial transformation and achieved 85% accuracy in predicting traffic volumes. Dataset Source: https://archive.ics.uci.edu/ml/datasets/Metro+Interstate+Traffic+Volume  <br />
  </p>
<p align="justify">
<strong>DBMS_BASH :(11/2021)</strong> <br />
I implemented a small database management system in Bash for one of my modules during my Masters. Data exchange between client and server for data entry and query provided through pipes. The system supported concurrent execution and protected against synchronisation problems with the effective use of semaphores. The system was able to create a database, create a table, insert rows in tables at existing databases and allowed to query the tables at targeted databases as a whole or with column indexes to display content. <br /> 
</p>
 <p align="justify">
<strong>codewars_solns :(on-going)</strong> <br />
This folder contains small scripts I write to solve various coding challenges in Codewars in my free time.<br />
 </p>
