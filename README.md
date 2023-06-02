# Personal_projects
<p>This repository contains personal projects I did in my free time and during my CS Masters's degree in UCD .</p>

<strong>DBMS_BASH :</strong> <br />
I implemented a small database management system in Bash for one of my modules during my Masters. Data exchange between client and server for data entry and query provided through pipes. The system supported concurrent execution and protected against synchronisation problems with the effective use of semaphores. The system was able to create a database, create a table, insert rows in tables at existing databases and allowed to query the tables at targeted databases as a whole or with column indexes to display content. <br />

<strong>JobAdsWordFreqEval :</strong> <br />
Small-scale text analytics study to assess word frequencies across data analytics job ads at LinkedIn, which helps gain insight into the common traits employers currently look for in data analytics roles.  <br />

<strong>Multi-Layer_Neural_Network_from_Scratch :</strong> <br />
I implemented a Multi-Layer Neural Network from Scratch with Python for one of my modules during my Masters. The implemented network was a shallow multilayer neural network of 1 hidden layer. The network could take any number of inputs, any number of outputs, and any number of hidden units. Learning implemented by backpropagation using batch gradient descent. The network is implemented to be flexible. It can handle regression and classification tasks and utilise different activation functions for hidden and output units depending on the user’s choice. In the classification task, the network used a leaky rectified linear unit activation function for hidden layer activation. For output layer activations, it used sigmoid activation functions for binary classification and softmax activation functions for multiclass classification. The network used a log loss cost function to observe training performance for classification. For regression, output wasn’t activated, and for the hidden layer, the user was given a choice to select from various activation functions: sigmoid function, hyperbolic tangent function, leaky rectified linear unit function, and binary step function. The network used the square error cost function to observe training performance for regression. Implemented network tested on two classification tasks, which were to predict XOR function, letter recognition and one regression task to approximate a sin function. Test results are available in separate notebooks. Source of the dataset for letter recognition: http://archive.ics.uci.edu/ml/datasets/Letter+Recognition  <br/>

<strong>Time-Related_Feature_Engineering :</strong> <br />
I built Time-Related Feature Engineering Pipelines in this notebook with Python to predict traffic volumes. This is a project for an assignment in the ML course I studied during my Master's in CS.  I performed time-related feature engineering by encoding time features using cyclic_spline_transformer and used wrapper strategy with sequential forward selection for feature selection. I built a predictive model using Stochastic Gradient Descent regression with polynomial transformation and achieved 85% accuracy in predicting traffic volumes. Dataset Source: https://archive.ics.uci.edu/ml/datasets/Metro+Interstate+Traffic+Volume  <br />

<strong>codewars_solns :</strong> <br />
This folder contains small scripts I write to solve various coding challenges in Codewars in my free time.<br />

<strong>Interactive_dashboard_Vega-Lite:</strong> <br />
I created an interactive dashboard using Vega-Lite for visual storytelling as part of an assignment for my CS master's degree. My aim was to allow users to explore the relationship between countries that deploy nuclear devices, the purposes of detonations, the methods of deployment, explosion yields, and locations of the explosions. 
The dataset used for this visualisation tool was adapted from the 2019 Tidy Tuesday Collection dataset: https://github.com/rfordatascience/tidytuesday/tree/master/data/2019/2019-08-20
The video explanation is available at: https://youtu.be/KpmABg-ydCg