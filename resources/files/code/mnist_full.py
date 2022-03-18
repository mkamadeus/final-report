from typing import List
from fastapi import FastAPI, UploadFile
from keras.models import load_model
from pydantic import BaseModel
import numpy as np

app = FastAPI()

# MODEL FORMAT
model = load_model("mnist.h5")

# OUTPUT FORMAT
class Output(BaseModel):
	prediction : List[float]

@app.post('/')
async def root(file : UploadFile):	
	contents = await file.read()
	
	# ---- PIPELINES BEGIN ----
	# resize image
	import io
	from PIL import Image
	stream = io.BytesIO(contents)
	img = Image.open(stream)
	img = img.resize((32,32))

	# reshape image to input
	result = np.array(img).reshape((1,32,32,1))
	print(result.shape)
	# ---- PIPELINES END ----
	
	# MODEL PREDICTION
	prediction = model.predict(x=result).tolist()[0]
	
	return Output(prediction=prediction)
