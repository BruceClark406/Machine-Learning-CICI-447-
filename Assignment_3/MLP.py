class MLP():
    #input-> #data_as_2dList, number_of_hidden_layers, number_of_hidden_nodes_in_each_layer
    def __init__(self, data, outputs, hidden_layers, hidden_nodes):
        self.data = data
        self.outputs = outputs
        self.hidden_layers = hidden_layers
        self.hidden_nodes = hidden_nodes
        
        if (len(hidden_nodes) != hidden_layers):
            raise Exception ("we need to know how many nodes are in each hidden layer")

        self.weight_matricies = []

        weight_matricies.append(np.random.rand(len(self.data[0]), hidden_nodes[0]))

        for i in range(hidden_layers-1):
            #layer = np.ones([hidden_nodes, hidden_nodes])*0.3
            layer = np.random.rand(hidden_nodes[i+1], hidden_nodes[i+2])
            weight_matricies.append(layer)

        weight_matrices.append(np.random.rand(hidden_nodes[-1], outputs))

        print(weight_matrices)
