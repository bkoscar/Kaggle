from fastapi import FastAPI
import joblib
import uvicorn


app = FastAPI()

@app.post('/api/predictions')
def get_prediction():
    return {'Hello world'}



if __name__ == '__main__':
    uvicorn.run('main:app', host = 'localhost', port=5000, reload = True)