from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from app.utils import preprocess
from app.inference import run_inference
from app.evaluate import evaluate_calibration  

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict(
    file: UploadFile = File(...),
    n_samples: int = 30,
    true_label: int = None   
):
    image = preprocess(file.file)
    result = run_inference(image, n_samples, true_label=true_label)
    return result