import numpy as np
class Layer:
    def __init__(self,action_layer,value_layer,op):
        self.action_layer = action_layer
        self.value_layer = value_layer
        self.op = op
        self.size = len(value_layer)
class MiniMax:
    def __init__(self,leaf_layer,branch_factor):
        self.branch_factor = branch_factor
        self.tree_height = int(np.log2(len(leaf_layer))/np.log2(branch_factor))
        self.layers = []
        if self.tree_height % 2 == 0:
            self.layers.append(Layer(action_layer=np.zeros(len(leaf_layer)), value_layer=leaf_layer, op="MAX"))
        else:
            self.layers.append(Layer(action_layer=np.zeros(len(leaf_layer)), value_layer=leaf_layer, op="MIN"))

    def backup(self):
        # implementing the main minimax algorithm:
        for i in range(self.tree_height):
            current_layer = self.layers[-1]
            if current_layer.op == "MAX":
                new_layer_op = "MIN"
            else:
                new_layer_op = "MAX"

            new_layer = Layer(np.zeros(current_layer.size // self.branch_factor),
                              np.zeros(current_layer.size // self.branch_factor), new_layer_op)
            if new_layer_op == "MIN":
                for j in range(new_layer.size):
                    start = self.branch_factor * j
                    finish = start + self.branch_factor
                    new_layer.value_layer[j] = np.min([current_layer.value_layer[k] for k in range(start,finish)])
                    new_layer.action_layer[j] = int(np.argmin([current_layer.value_layer[k] for k in range(start,finish)]))
            else:
                for j in range(new_layer.size):
                    start = self.branch_factor * j
                    finish = start + self.branch_factor
                    new_layer.value_layer[j] = np.max([current_layer.value_layer[k] for k in range(start,finish)])
                    new_layer.action_layer[j] = int(np.argmax([current_layer.value_layer[k] for k in range(start,finish)]))

            self.layers.append(new_layer)
        return
    def destruct(self):
        self.layers.clear()
    def best_action(self,history):
        state = 0
        layer = self.tree_height - len(history)
        for i in range(len(history)):
            state = state*self.branch_factor + history[i]
        return self.layers[int(layer)].value_layer[int(state)] ,  self.layers[int(layer)].action_layer[int(state)]