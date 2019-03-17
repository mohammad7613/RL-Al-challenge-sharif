import numpy as np
import datetime
import time
import os, os.path
##  handy functions :)
def next_batch(x,y,size):
    indices = np.random.randint(0,len(y),size)
    return np.take(x, indices,axis =0) , np.take(y, indices,axis =0)

def  relu(X):
    return np.maximum(X,np.zeros(len(X)))


## Layer Class
class FeedForwardLayer:
    input_dim=0
    hidden_dim=0
    ActivationFunction = "None"
    name =""
    def __init__(self,ActivationFunction,input_dim,hidden_dim,name):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.ActivationFunction = ActivationFunction
        self.name = name
        self.w = np.random.randn(hidden_dim, input_dim)*0.01
        self.b = np.zeros(hidden_dim)
        return

    def process(self,data):
        self.z = np.dot(self.w,data) + self.b
        self.a =np.zeros(self.z.shape[0])
        if self.ActivationFunction == "relu":
            self.a = relu(self.z)
        if self.ActivationFunction == "None":
            self.a = np.copy(self.z)
        if self.ActivationFunction == "tanh":
            self.a = np.tanh(self.z)
        if self.ActivationFunction == "sigmoid":
            self.a = 1/(1+np.exp(self.z))
        return self.a

def neuron_layer(X, n_neurons, name, activation=None):
    import tensorflow as tf
    with tf.name_scope(name):
        n_inputs = int(X.get_shape()[1])
        stddev = 2 / np.sqrt(n_inputs)
        init = tf.random.truncated_normal((n_inputs, n_neurons), stddev=stddev)
        W = tf.Variable(init, name="weights")
        b = tf.Variable(tf.zeros([n_neurons]), name="biases")
        z = tf.matmul(X, W) + b
    if activation == "relu":
        return tf.nn.relu(z)
    else:
        return z

## Main Neural Net Class
class FeedForwardNeuralNet:
    layers = []
    tf_layers = []
    is_training_on = False

    def __init__(self,is_training_on = False):
        np.random.seed(42)
        self.is_training_on = is_training_on
        if is_training_on is True:
            import tensorflow as tf
            tf.reset_default_graph()
        return

    def addLayer(self,ActivationFunction,input_dim,hidden_dim,name):
        self.layers.append(FeedForwardLayer(ActivationFunction,input_dim,hidden_dim,name))
        return

    def clearAll(self):
        self.layers.clear()
        self.tf_layers.clear()
        if self.is_training_on is True:
            import tensorflow as tf
            tf.reset_default_graph()
        return

    def process(self,X):
        results =[]
        for data in X:
            result = data
            for layer in self.layers:
                result =layer.process(result)
            results.append(result)
        return results

    def save_model(self, saving_directory, epoch_number):
        # managing logs:
        log_file_pointer = saving_directory + "/log.txt"
        file= open(log_file_pointer,'a+')
        n = len(os.listdir(saving_directory))
        if epoch_number == 0:
            file.write("saving a new session at :{} \nin folder Session#{}\n".format(datetime.datetime.now(), n))
        file.write("saving epoch {} at {}:\n".format(epoch_number,datetime.datetime.now()))
        file.close()
        # creating a new directory and saving the medel parameters:
        if epoch_number ==0:
            dir = saving_directory + "/Session#{}".format(n)
            os.mkdir(dir)
            dir = saving_directory + "/Session#{}/epoch#{}".format(n,epoch_number)
            os.mkdir(dir)
        else:
            dir = saving_directory + "/Session#{}/epoch#{}".format(n-1, epoch_number)
            os.mkdir(dir)
        for layer in self.layers:
            np.save(dir + "/"+layer.name+"_biases", layer.b)
            np.save(dir + "/"+layer.name+"_weights", layer.w)
        return

    def restore_model(self, restore_directory):
        for layer in self.layers:
            layer.b = np.load(restore_directory + "/" + layer.name + "_biases.npy")
            layer.w = np.load(restore_directory + "/" + layer.name + "_weights.npy")
        return

    def feed_train_data(self, X_train, y_train, X_test, y_test):
        if self.is_training_on is False:
            raise ValueError("Sorry,training is off for this Neural Net!")
            return
        import tensorflow as tf

        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test
        with tf.name_scope("dnn"):
            for layer in self.layers:
                if len(self.tf_layers) == 0:
                    self.X = tf.placeholder(tf.float32, shape=(None, layer.input_dim), name="X")
                    self.tf_layers.append(neuron_layer(self.X, layer.hidden_dim, layer.name, activation=layer.ActivationFunction))
                else:
                    last_layer = self.tf_layers[len(self.tf_layers) - 1]
                    self.tf_layers.append(neuron_layer(last_layer, layer.hidden_dim, layer.name, activation=layer.ActivationFunction))
            self.y = tf.placeholder(tf.float32, shape=(None), name="y")
            with tf.name_scope("loss"):
                self.error =tf.reduce_sum( tf.square(self.tf_layers[len(self.tf_layers)-1] - self.y))
                self.loss = tf.reduce_mean(tf.sqrt(self.error),name = "loss")

    def train(self,saving_directory, n_epochs, batch_size, learning_rate=0.01, saving_rate=0.05):
        if self.is_training_on is False:
            raise ValueError("Sorry,training is off for this Neural Net!")
            return
        import tensorflow as tf
        save_step_size = int(n_epochs * saving_rate)
        with tf.name_scope("train"):
            optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)
            training_op = optimizer.minimize(self.loss)
        init = tf.global_variables_initializer()
        with tf.Session() as sess:
            init.run()
            for epoch in range(n_epochs):
                for iteration in range(len(self.X_train) // batch_size):
                    X_batch, y_batch = next_batch(self.X_train, self.y_train, batch_size)
                    sess.run(training_op, feed_dict={self.X: X_batch, self.y: y_batch})
                # updating the shell parameters to match the real tensorflow parameters:
                for layer in self.layers:
                    layer.b=tf.get_default_graph().get_tensor_by_name("dnn/"+layer.name+"/biases:0").eval()
                    layer.w=tf.get_default_graph().get_tensor_by_name("dnn/"+layer.name+"/weights:0").eval().transpose()
                loss_train = self.loss.eval(feed_dict={self.X: X_batch, self.y: y_batch})
                loss_test = self.loss.eval(feed_dict={self.X: self.X_test, self.y: self.y_test})

                print(epoch, "Train loss:", loss_train, "Test loss:", loss_test)

                # saving model parameters:
                if epoch % save_step_size == 0:
                    self.save_model(saving_directory=saving_directory,epoch_number=epoch)
        return

