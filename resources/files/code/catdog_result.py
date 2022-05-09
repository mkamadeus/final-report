...

@app.post('/')
async def root(file : UploadFile):
    contents = await file.read()
    stream = io.BytesIO(contents)
    img = Image.open(stream)
    img = img.resize((160,160))

    result = np.array(img).reshape((1,160,160,3))

    prediction = model.predict(x=result).tolist()[0]

    return [Output(prediction=prediction)]
