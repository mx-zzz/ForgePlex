import tensorflow as tf
import os

import os
import tensorflow as tf

def get_model_info(model_path):


    print(model_path)

    pb_file_path = model_path

    if not os.path.exists(pb_file_path):
        raise FileNotFoundError(f"Path {pb_file_path} does not exist.")
    if not os.path.exists(os.path.join(pb_file_path, 'saved_model.pb')):
        raise FileNotFoundError(f"saved_model.pb not found in {pb_file_path}.")

    # Load the model
    model = tf.saved_model.load(pb_file_path)

    # Get the concrete function (SignatureDef) from the model
    concrete_func = model.signatures['serving_default']

    # Get input details
    input_details = concrete_func.inputs

    # Get output details
    output_details = concrete_func.outputs

    # Extract information
    model_info = {
        "inputs": [],
        "outputs": []
    }

    for input_tensor in input_details:
        input_info = {
            "name": input_tensor.name,
            "shape": input_tensor.shape.as_list(),
            "dtype": input_tensor.dtype.name
        }
        model_info["inputs"].append(input_info)

    for output_tensor in output_details:
        output_info = {
            "name": output_tensor.name,
            "shape": output_tensor.shape.as_list(),
            "dtype": output_tensor.dtype.name
        }
        model_info["outputs"].append(output_info)

    return model_info


