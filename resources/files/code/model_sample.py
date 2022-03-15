sess = rt.InferenceSession("titanic.onnx")
input_name = sess.get_inputs()[0].name
label_name = sess.get_outputs()[0].name
prediction = sess.run([label_name], {input_name: p_final})[0]