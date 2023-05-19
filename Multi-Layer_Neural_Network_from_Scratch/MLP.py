import numpy as np
import math
import collections.abc
import matplotlib.pyplot as plt

#paramlist=[epochs,learning_rate,num_inputs,num_hidden,num_output]
#weights=[weight_input_hidden_array, weight_hidden_output_array]
#biases=[bias_input_hidden_array, bias_hidden_output_array]
#hidden activation: only valid if task is regression default is "sigmoid" can be set to "Tanh",  "ReLU", "binaryStep".
#task: a parameter to decide output layer activation default is "regression" if regression output layer is activated by linear activation function.
class MLP:
    def __init__(self,input_train,target_train, paramlist,
                 hidden_activation="sigmoid", task="regression",
                 mute=False,weights=None, biases=None):
        self.task=task
        self.input_train=input_train
        self.target_train=target_train
        self.mute=mute
        self.hidden_activation=hidden_activation
        self.weights=weights
        self.biases=biases

        self.epochs, self.learning_rate=paramlist[0],paramlist[1]
        self.num_inputs,self.num_hidden,self.num_output=paramlist[2],paramlist[3],paramlist[4]
        if self.weights==None:
            if task=="classification":
                self.weight_input_hidden = np.random.uniform(0, 0.5, (self.num_hidden, self.num_inputs))
                self.weight_hidden_output = np.random.uniform(0, 0.5, (self.num_output, self.num_hidden))
            elif task=="regression":
                self.weight_input_hidden = np.random.normal(loc=0, scale=0.25, size=(self.num_hidden, self.num_inputs))
                self.weight_hidden_output = np.random.normal(loc=0, scale=0.25, size=(self.num_output, self.num_hidden))
        else:
            self.weight_input_hidden = self.weights[0]
            self.weight_hidden_output = self.weights[1]

        if self.biases == None:
            self.bias_input_hidden = np.zeros(self.num_hidden)
            self.bias_hidden_output = np.zeros(self.num_output)
        else:
            self.bias_input_hidden = self.biases[0]
            self.bias_hidden_output = self.biases[1]

        self.predictions_hidden_all=np.zeros(shape=(len(self.input_train), self.num_hidden))
        self.predictions_output_all = np.zeros(shape=(len(self.input_train), self.num_output))

        self.act_hidden, self.act_output = None, None

    ##possible activation functions
    def softmax(self, predictions):
        # softmax for multiclass output activation
        m = max(predictions)
        temp = [math.exp(p - m) for p in predictions]
        total = sum(temp)
        return [t / total for t in temp]

    def activate(self,x):
        # sigmoid for binary output activation
        # sigmoid for hidden activation  causes vanishing gradient problem.
        return 1 / (1 + math.exp(-x))

    def sigmoid_derivative(self,x):
        return self.activate(x) * (1.0 - self.activate(x))

    def ReLU(self,pred):
        #leeky ReLu for hidden activation
        if pred > 0:
            return pred
        else:
            return 0.01 * pred

    def Tanh(self, x):
        # Tanh for hidden activation
        # Tanh  for hidden activation also causes vanishing gradient problem.
        return np.tanh(x)

    def Tanh_grad(self,x):
        # Tanh derivative for error derivative hidden
        return 1. - np.tanh(x) ** 2

    def binaryStep(self,x):
        #It returns '0' is the input is less then zero otherwise, return one
        return np.heaviside(x, 1)

    def cost_function(self, activations, targets):
        # Log loss is undefined for a=0 or a=1, so activations are clipped to max(eps, min(1 - eps, p)).
        eps = 1e-15
        activations = np.clip(activations, eps, 1 - eps)
        # will use log loss for cost function
        #print(f"activations: {activations}, targets: {targets}")
        if len(self.predictions_output_all[0]) > 1:
            #print(f"activations: {activations}, targets: {targets}")
            losses = [-t * math.log(a) - (1 - t) * math.log(1 - a) for a, t in zip(activations, targets)]
            return sum(losses)
        else:
            loss = -targets * math.log(activations[0]) - (1 - targets) * math.log(1 - activations[0])
            return loss

    def feed_forward(self,input_train):
        # calculate predicitons for hidden layer
        predictions_hidden_all_index = 0
        for vector in input_train:
            predictions_hidden_vector = []
            for weights, bias in zip(self.weight_input_hidden, self.bias_input_hidden):
                #print(f"weights:{weights}")
                #print(f"bias:{bias}")
                predictions_hidden_vector.append(sum((weights * vector)) + bias)
            self.predictions_hidden_all[predictions_hidden_all_index] = predictions_hidden_vector
            predictions_hidden_all_index += 1

        if self.task == "classification":
            # activate hidden layer with rectified leaky linear unit(ReLU)
            self.act_hidden = np.vectorize(self.ReLU)(self.predictions_hidden_all)
        elif self.task=="regression":
            if self.hidden_activation=="sigmoid":
                # activate hidden layer with sigmoid
                self.act_hidden = np.vectorize(self.activate)(self.predictions_hidden_all)
            elif self.hidden_activation=="Tanh":
                # activate hidden layer with Tanh
                self.act_hidden = np.vectorize(self.Tanh)(self.predictions_hidden_all)
            elif self.hidden_activation=="binaryStep":
                self.act_hidden = np.vectorize(self.binaryStep)(self.predictions_hidden_all)
            elif self.hidden_activation=="ReLU":
                self.act_hidden = np.vectorize(self.ReLU)(self.predictions_hidden_all)
            else:
                raise ValueError("entered activation function is undefined")
        else:
            raise ValueError("entered task is undefined")

        # calculate prediction for output layer based on activations of hidden layer
        predictions_output_all_index = 0
        for vector in self.act_hidden:
            predictions_output_vector = []
            for weights, bias in zip(self.weight_hidden_output, self.bias_hidden_output):
                predictions_output_vector.append(sum((weights * vector)) + bias)
            self.predictions_output_all[predictions_output_all_index] = predictions_output_vector
            predictions_output_all_index += 1

        if self.task=="classification":
            if len(self.predictions_output_all[0]) > 1:
                # activate output layer with softmax in case of multiclass clasification
                self.act_output = [self.softmax(p) for p in self.predictions_output_all]
            else:
                # sigmoid activation in case of binary clasification
                self.act_output = np.vectorize(self.activate)(self.predictions_output_all)
        elif self.task=="regression":
            # no activation in case of regression ( linear activation)
            self.act_output=self.predictions_output_all


    def calc_cost(self,act_output,target_train, task):
        if task=="classification":
            cost = sum([self.cost_function(a, t) for a, t in zip(act_output, target_train)]) / len(act_output)
            return cost
        elif task == "regression":
            cost = sum([(p - t) ** 2 for p, t in zip(act_output, target_train)]) / len(act_output)
            return cost[0]

    def back_propogation(self,input_train,target_train):
        ##back propogation starts
        # calculate error derivates for output layer
        errors_deriv_output = self.act_output - target_train

        # calculate the gradient for weights and biases from hidden to output
        #transposing weights matrix
        weight_hidden_output_T = np.transpose(self.weight_hidden_output)
        #multiplying transposed weights matrix by error derivates for output layer
        if self.task=="classification":
            #then element wise multipling this matrix by hidden layer predictions and running through leaky ReLU derivative
            errors_deriv_hidden = [[sum([d * w for d, w in zip(deltas, weights)]) * (0.01 if p <= 0 else 1)
                                    for weights, p in zip(weight_hidden_output_T, pred)]
                                   for deltas, pred in zip(errors_deriv_output, self.predictions_hidden_all)]
        elif self.task == "regression":
            if self.hidden_activation == "sigmoid":
                # then element wise multipling this matrix by hidden layer predictions and running through sigmoid derivative
                errors_deriv_hidden = [[sum([d * w for d, w in zip(deltas, weights)]) * (self.sigmoid_derivative(p))
                                        for weights, p in zip(weight_hidden_output_T, pred)]
                                       for deltas, pred in zip(errors_deriv_output, self.predictions_hidden_all)]
            elif self.hidden_activation == "Tanh":
                # then element wise multipling this matrix by hidden layer predictions and running through sigmoid derivative
                errors_deriv_hidden = [[sum([d * w for d, w in zip(deltas, weights)]) * (self.Tanh_grad(p))
                                        for weights, p in zip(weight_hidden_output_T, pred)]
                                       for deltas, pred in zip(errors_deriv_output, self.predictions_hidden_all)]
            elif self.hidden_activation == "binaryStep":
                # then element wise multipling this matrix by hidden layer predictions and running through step derivative
                # at p = 0 derivative of step function is infinite,
                # since derivative is 0 everywhere it is not useful for neural networks
                # because gradient descent can't adjust weights
                errors_deriv_hidden = [[sum([d * w for d, w in zip(deltas, weights)]) * (0 if p != 0 else 1)
                                        for weights, p in zip(weight_hidden_output_T, pred)]
                                       for deltas, pred in zip(errors_deriv_output, self.predictions_hidden_all)]
            elif self.hidden_activation == "ReLU":
                # then element wise multipling this matrix by hidden layer predictions and running through leaky ReLU derivative
                errors_deriv_hidden = [[sum([d * w for d, w in zip(deltas, weights)]) * (0.01 if p <= 0 else 1)
                                        for weights, p in zip(weight_hidden_output_T, pred)]
                                       for deltas, pred in zip(errors_deriv_output, self.predictions_hidden_all)]

        # calculate error derivatives for the hidden layer
        act_hidden_T = np.transpose(self.act_hidden)
        errors_deriv_output_T = np.transpose(errors_deriv_output)
        # weight_hidden_output_deltas contains the deltas for the weights from hidden to output
        weight_hidden_output_deltas = [[sum([d * a for d, a in zip(deltas, act)]) for deltas in errors_deriv_output_T]
                                       for act in act_hidden_T]
        # bias_hidden_output_deltas contains the deltas for the output layer biases.
        bias_hidden_output_deltas = [sum([d for d in deltas]) for deltas in errors_deriv_output_T]

        # calculate the gradient for weights and biases from input to hidden
        input_train_T = np.transpose(input_train)
        errors_deriv_hidden_T = np.transpose(errors_deriv_hidden)
        # weight_input_hidden_deltas contains the deltas for the weights from input to hidden
        weight_input_hidden_deltas = [[sum([d * a for d, a in zip(deltas, act)]) for deltas in errors_deriv_hidden_T]
                                      for act in input_train_T]
        # bias_input_hidden_deltas contains the deltas for the output layer biases.
        bias_input_hidden_deltas = [sum([d for d in deltas]) for deltas in errors_deriv_hidden_T]

        # update weights and biases
        # updating hidden to output
        weight_hidden_output_deltas_T = np.transpose(weight_hidden_output_deltas)
        for y in range(self.num_output):
            for x in range(self.num_hidden):
                self.weight_hidden_output[y][x] -= self.learning_rate * weight_hidden_output_deltas_T[y][x] / len(input_train)
            self.bias_hidden_output[y] -= self.learning_rate * bias_hidden_output_deltas[y] / len(input_train)

        # updating input to hidden
        weight_input_hidden_deltas_T = np.transpose(weight_input_hidden_deltas)
        for y in range(self.num_hidden):
            for x in range(self.num_inputs):
                self.weight_input_hidden[y][x] -= self.learning_rate * weight_input_hidden_deltas_T[y][x] / len(input_train)
            self.bias_input_hidden[y] -= self.learning_rate * bias_input_hidden_deltas[y] / len(input_train)

    def train(self):
        mute=self.mute
        input_train = self.input_train
        target_train = self.target_train
        if mute == False:
            print(f"weights @ start, input->hidden : {self.weight_input_hidden}")
            print(f"weights@ start, hidden->output : {self.weight_hidden_output}")
        x, y = [], []
        for epoch in range(self.epochs):
            ##feed forward starts
            MLP.feed_forward(self, input_train)
            act_output = self.act_output
            task= self.task
            ##cost calculation
            cost=self.calc_cost(act_output,target_train, task)
            #list(map('{:.4f}'.format,cost))
            if mute== False:
                print(f"epoch:{epoch} cost:{cost:.4f}")
            ##back propogation starts
            self.back_propogation(input_train,target_train)
            x.append(epoch)
            y.append(cost)
        if mute == False:
            fig, ax = plt.subplots(figsize=(11, 3))
            ax.plot(x, y)
            print(f"weights after training, input->hidden : {self.weight_input_hidden}")
            print(f"weights after training, hidden->output : {self.weight_hidden_output}")

    def test(self, input_test):
        predictions_hidden_all = np.zeros(shape=(len(input_test), self.num_hidden))
        predictions_hidden_all_index = 0
        for vector in input_test:
            predictions_hidden_vector = []
            for weights, bias in zip(self.weight_input_hidden, self.bias_input_hidden):
                predictions_hidden_vector.append(sum((weights * vector)) + bias)
            predictions_hidden_all[predictions_hidden_all_index] = predictions_hidden_vector
            predictions_hidden_all_index += 1
        if self.task == "classification":
            # activate hidden layer with rectified leaky linear unit(ReLU)
            act_hidden = np.vectorize(self.ReLU)(predictions_hidden_all)
        elif self.task == "regression":
            if self.hidden_activation == "sigmoid":
                # activate hidden layer with sigmoid
                act_hidden = np.vectorize(self.activate)(predictions_hidden_all)
            elif self.hidden_activation == "Tanh":
                # activate hidden layer with Tanh
                act_hidden = np.vectorize(self.Tanh)(predictions_hidden_all)
            elif self.hidden_activation == "binaryStep":
                act_hidden = np.vectorize(self.binaryStep)(predictions_hidden_all)
            elif self.hidden_activation == "ReLU":
                act_hidden = np.vectorize(self.ReLU)(predictions_hidden_all)

        predictions_output_all = np.zeros(shape=(len(input_test), self.num_output))
        predictions_output_all_index = 0
        for vector in act_hidden:
            predictions_output_vector = []
            for weights, bias in zip(self.weight_hidden_output, self.bias_hidden_output):
                predictions_output_vector.append(sum((weights * vector)) + bias)
            predictions_output_all[predictions_output_all_index] = predictions_output_vector
            predictions_output_all_index += 1

        if self.task=="classification":
            if len(self.predictions_output_all[0]) > 1:
                # activate output layer with softmax in case of multiclass clasification
                act_output = [self.softmax(p) for p in predictions_output_all]
            else:
                # sigmoid activation in case of binary clasification
                act_output = np.vectorize(self.activate)(predictions_output_all)
        elif self.task=="regression":
            # no activation in case of regression ( linear activation)
            act_output=predictions_output_all

        return act_output

    def xor_test(self,input_test, target_test):
        # Testing network for XOR function
        mute = self.mute
        act_output=self.test(input_test)
        correct = 0
        counter = 1
        for a, t in zip(act_output, target_test):
            if max(a) < 0.5:
                result = 0
            else:
                result = 1
            if result == t:
                correct += 1
            elif mute == False:
                print(f"counter: {counter}")
                print(f"activation: {result}")
                print(f"target: {t}")
            counter += 1
        print(f"Correct: {correct}/{len(act_output)} ({correct / len(act_output):%})")

    def sin_test(self,input_test, target_test):
        mute=self.mute
        # Testing network for sin function
        predictions=self.test(input_test)
        correct = 0
        counter = 1
        for p, t in zip(predictions, target_test):
            if round(max(p),1) == round(t,1):
                correct += 1
            elif mute == False:
                print(f"counter: {counter}")
                print(f"activation: {round(max(p),2)}")
                print(f"target: {round(t,2)}")
            counter += 1
        print(f"Correct: {correct}/{len(predictions)} ({correct / len(predictions):%})")
        if mute == False:
            x=[x for x in range(len(predictions))]
            y1=predictions
            y2=target_test
            plt.figure(figsize=(11, 3))
            plt.plot(x, y1, label="act_output")
            plt.plot(x, y2, label="target_test")
            plt.xlabel("target #")
            plt.ylabel("value")
            plt.legend()
            plt.show()

    def letter_test(self,input_test, target_test):
        # Testing network for XOR function
        mute = self.mute
        act_output=self.test(input_test)
        #def classify(x):
            #if x >0.5:
                #return 1
            #else:
                #return 0
        #result= np.vectorize(classify)(act_output)
        correct = 0
        counter = 1
        for a, t in zip(act_output, target_test):
            if  np.argmax(a) == np.argmax(t):
                correct += 1
            elif mute == False:
                print(f"counter: {counter}")
                print(f"activation: {a}")
                print(f"target: {t}")
            counter += 1
        print(f"Correct: {correct}/{len(act_output)} ({correct / len(act_output):%})")












