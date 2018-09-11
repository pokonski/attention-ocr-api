import tensorflow as tf
import os

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def load_graph(frozen_graph_filename):
    # We load the protobuf file from the disk and parse it to retrieve the
    # unserialized graph_def
    with tf.gfile.GFile(frozen_graph_filename, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

    # Then, we import the graph_def into a new Graph and returns it
    with tf.Graph().as_default() as graph:
        # The name var will prefix every op/nodes in your graph
        # Since we load everything in a new graph, this is not needed
        tf.import_graph_def(graph_def, name="prefix")
    return graph

def get_model_api():
    graph = load_graph("exported-model-frozen/frozen_graph.pb")

    input = graph.get_tensor_by_name('prefix/input_image_as_bytes:0')
    prediction = graph.get_tensor_by_name('prefix/prediction:0')

    session_conf = tf.ConfigProto(
        device_count={'CPU' : 1, 'GPU' : 0},
        allow_soft_placement=True,
        log_device_placement=False
    )

    # We launch a Session
    sess = tf.Session(graph=graph, config=session_conf)
    #image = open(directory + "/" + filename, "rb")
    def model_api(image):
        out = sess.run(prediction, feed_dict={
            input: [image]
        })

        return out
    return model_api
