...

# app
app = FastAPI()

# model format
sess = rt.InferenceSession("titanic.onnx")
input_name = sess.get_inputs()[0].name
label_name = sess.get_outputs()[0].name

# input format
class Input(BaseModel):
	pclass : float
	sibsp : float
	parch : float
	age : float
	sex : str
	embarked : str

# output format
class Output(BaseModel):
	prediction : float

# endpoint
@app.post('/')
async def root(body : Input):

	# ---- pipelines begin ----
	# normal
	p_1 = np.array([[body.pclass, body.sibsp, body.parch]], dtype=np.float32)

	# scaled
	scaler = joblib.load('age.scaler')
	p_2 = scaler.transform(np.array([[body.age]], dtype=np.float32))

	# encoded
	p_3 = np.array([[1 if body.sex == "M" else 0, 1 if body.sex == "F" else 0]], dtype=np.float32)
	p_4 = np.array([[1 if body.sex == "C" else 0, 1 if body.sex == "Q" else 0, 1 if body.sex == "S" else 0]], dtype=np.float32)
	
	# aggregation
	p_final = np.concatenate((p_1, p_2, p_3, p_4), axis=1)
	
	# ---- pipelines end ----

    # model prediction
	prediction = sess.run([label_name], {input_name: p_final})[0]

	return Output(prediction=prediction)
