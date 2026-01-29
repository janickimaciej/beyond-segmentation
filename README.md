## Environment

In order to run scripts included in this project, create a Python environment and install required packages, e.g.:

```bash
python -m venv env
. env/bin/activate
pip install -r requirements.txt
```

## Data Acquisition and Preprocessing

Model is trained on CMP dataset with images cropped to individual facades. Navigate to data directory and run:

```bash
./prepare_dataset.sh
```

The script will download CMP dataset, preprocess it and split into training, validation and test set.

## Model Preparation

The project uses a modified YOLOv8 detection model. In order to use the model with loss terms defined in this project, navigate to model directory and run:

```bash
./prepare_model.sh
```

## Training

Navigate to model directory. Set the desired number of epochs in train.py script. Then run:

```bash
./train.sh
```

Results will be saved in model/ultralytics/runs/detect/train* directory (subsequent trainings will save results in train, train2, etc).

## Inference

Navigate to model directory. Set training_dir variable in infer.py to training results directory name (e.g. "train"). Then run:

```bash
./infer.sh
```

Results will be saved in model/ultralytics/runs/detect/infer_* (where * denotes the value of the training_dir variable).

## Evaluation Metrics
