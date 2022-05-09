...

@app.post('/')
async def root(body: Input):
    t9 =  np.array([[body.has_credit_card]])
    t10 =  np.array([[body.is_active_member]])
    scaler = joblib.load('churn.scaler')
    scaled = scaler.transform(np.array([[body.credit_score,body.age,body.tenure,body.balance,body.num_of_products,body.estimated_salary,]]))
    t0 =  np.array([ [scaled[0, 0]] ])
    t5 =  np.array([ [scaled[0, 1]] ])
    t6 =  np.array([ [scaled[0, 2]] ])
    t7 =  np.array([ [scaled[0, 3]] ])
    t8 =  np.array([ [scaled[0, 4]] ])
    t11 =  np.array([ [scaled[0, 5]] ])
    t1 =  np.array([[1 if body.geography == "Germany" else 0]])
    t2 =  np.array([[1 if body.geography == "Spain" else 0]])
    t3 =  np.array([[1 if body.geography == "France" else 0]])
    labeller_gender = joblib.load('geo.encoder')
    labelled =  labeller_gender.transform(np.array([[body.gender,]]))
    t4 =  np.array([[ labelled[0] ]])

    result = np.concatenate((t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, ), axis=1).astype(np.float32)

    prediction = model.predict(x=result).tolist()[0]

    return Output(prediction=prediction)
