...

@app.post('/')
async def root(body: Input):
    t0 =  np.array([[body.pclass]])
    t1 =  np.array([[body.sibsp]])
    t2 =  np.array([[body.parch]])
    scaler_age = joblib.load('age.scaler')
    scaled = scaler_age.transform(np.array([[body.age,]]))
    t3 =  np.array([[ scaled[0] ]])
    t4 =  np.array([[1 if body.gender == "M" else 0]])
    t5 =  np.array([[1 if body.gender == "F" else 0]])
    t6 =  np.array([[1 if body.embarked == "C" else 0]])
    t7 =  np.array([[1 if body.embarked == "Q" else 0]])
    t8 =  np.array([[1 if body.embarked == "S" else 0]])

    result = np.concatenate((t0, t1, t2, t3, t4, t5, t6, t7, t8, ), axis=1).astype(np.float32)

    input_name = model.get_inputs()[0].name
    label_name = model.get_outputs()[0].name
    prediction = model.run([label_name], {input_name: prediction})[0]

    return Output(prediction=prediction)