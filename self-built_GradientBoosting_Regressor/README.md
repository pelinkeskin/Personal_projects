### Building Gradient Boosting Regressor from Scratch with Python
I completed this project as part of an assignment in one of my modules during my Masters. The project involved creating a gradient-boosting regressor for continuous prediction problems by inheriting from appropriate scikit-learn base classes. The implementation allowed the subsampling of rows in the samples and included a learning rate hyperparameter. I tested my self-built algorithm against sklearn Adaboost regressor on [commonlitreadabilityprize dataset](https://www.kaggle.com/competitions/commonlitreadabilityprize) 's bag of words and sentence embedding representations. After tuning the hyperparameters for both models, my self-built gradient boosting regressor showed slightly better prediction performance than sklearn's AdaBoost algorithm. 