import os
import sys
import threading
import numpy as np
from NeuralNet import FeedForwardNeuralNet

__author__ = 'pezzati'

from Network import *
from AI import AI
from threading import Thread
from queue import Queue


class Controller:
    def __init__(self, name):
        self.sending_flag = True
        self.conf = {}
        self.network = None
        self.queue = Queue()
        self.world = World(queue=self.queue)
        self.client = AI(name)
        self.argNames = ["AICHostIP", "AICHostPort", "AICToken", "AICRetryDelay"]
        self.argDefaults = ["127.0.0.1", 7099, "00000000000000000000000000000000", "1000"]
        self.turn_num = 0
        self.preprocess_flag = False

    def start(self):
        self.read_settings()
        self.network = Network(ip=self.conf[self.argNames[0]],
                               port=self.conf[self.argNames[1]],
                               token=self.conf[self.argNames[2]],
                               message_handler=self.handle_message)
        self.network.connect()

        def run():
            while self.sending_flag:
                event = self.queue.get()
                self.queue.task_done()
                message = {
                    'name': Event.EVENT,
                    'args': [{'type': event.type, 'args': event.args}]
                }
                if World.DEBUGGING_MODE and World.LOG_FILE_POINTER is not None:
                    World.LOG_FILE_POINTER.write('------send message to server-----\n ' + message.__str__())
                self.network.send(message)

        Thread(target=run, daemon=True).start()

    def terminate(self):
        if World.LOG_FILE_POINTER is not None:
            World.LOG_FILE_POINTER.write('finished')
            World.LOG_FILE_POINTER.flush()
            World.LOG_FILE_POINTER.close()
        print("finished!")
        self.network.close()
        self.sending_flag = False

    def read_settings(self):
        if os.environ.get(self.argNames[0]) is None:
            for i in range(len(self.argNames)):
                self.conf[self.argNames[i]] = self.argDefaults[i]
        else:
            for i in range(len(self.argNames)):
                self.conf[self.argNames[i]] = os.environ.get(self.argNames[i])

    def handle_message(self, message):
        if message[ServerConstants.KEY_NAME] == ServerConstants.MESSAGE_TYPE_INIT:
            self.world._handle_init_message(message)
            threading.Thread(target=self.launch_on_thread(self.client.preprocess, 'init', self.world, [])).start()
        elif message[ServerConstants.KEY_NAME] == ServerConstants.MESSAGE_TYPE_PICK:
            new_world = World(world=self.world)
            new_world._handle_pick_message(message)
            threading.Thread(target=self.launch_on_thread(self.client.pick, 'pick', new_world,
                                                          [new_world.current_turn])).start()
        elif message[ServerConstants.KEY_NAME] == ServerConstants.MESSAGE_TYPE_TURN:
            new_world = World(world=self.world)
            new_world._handle_turn_message(message)
            if new_world.current_phase == Phase.MOVE:
                threading.Thread(target=self.launch_on_thread(self.client.move, 'move', new_world,
                                                              [new_world.current_turn,
                                                               new_world.move_phase_num])).start()
            elif new_world.current_phase == Phase.ACTION:
                threading.Thread(target=self.launch_on_thread(self.client.action, 'action', new_world,
                                                              [new_world.current_turn])).start()
        elif message[ServerConstants.KEY_NAME] == ServerConstants.MESSAGE_TYPE_SHUTDOWN:
            self.terminate()

    def launch_on_thread(self, action, name, new_world, args):
        action(new_world)
        new_world.queue.put(Event(name + '-end', args))


if __name__ == '__main__':
    c1 = Controller("p1")
    c2 = Controller("p2")
    t1 = threading.Thread(target=c1.start, args=())
    t2 = threading.Thread(target=c2.start, args=())

    #starting thread 1
    t1.start()
    #starting thread 2
    t2.start()
    if len(sys.argv) > 1 and sys.argv[1] == '--verbose':
       World.DEBUGGING_MODE = True

    # X_train = np.arange(0, 1, 0.1).reshape(1,10)
    # X_test = np.arange(0, 1, 0.1).reshape(1,10)
    # y_test = np.array(0.9).reshape(1,1)
    # y_train = np.array(0.9).reshape(1,1)
    # nn = FeedForwardNeuralNet(is_training_on=True)
    # nn.clearAll()
    # nn.addLayer(ActivationFunction="relu", hidden_dim=8, input_dim=10,name="hidden_1")
    # nn.addLayer(ActivationFunction="relu", hidden_dim=5, input_dim=8, name="hidden_2")
    # nn.addLayer(ActivationFunction="relu", hidden_dim=3, input_dim=5, name="hidden_3")
    # nn.addLayer(ActivationFunction="relu", hidden_dim=1, input_dim=3, name="hidden_4")
    # #nn.feed_train_data(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test)
    # #nn.train(saving_directory="C:/Users/yousef/Desktop/AI Comp 2019/saved models",
    # #         n_epochs=100,batch_size=1)
    #
    # X = np.arange(0,1,0.1)
    # nn.restore_model("C:/Users/yousef/Desktop/AI Comp 2019/saved models/Session#1/epoch#85")
    # print(nn.process(X))