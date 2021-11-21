import torch
import torch.nn
import joblib
import os


def prediction(values):

    model_joblib = os.path.abspath('./herokunlp/ml/linear.sav')
    names = {0: 'Setosa', 1: 'Versicolour', 2: 'Virginica'}
    urls = {0: 'https://www.gardenia.net/storage/app/public/uploads/images/detail/sAnMmr80jfbvc9qs043R1tDHBC5TDPUUaYJoi0yO.jpeg',
            1: 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Iris_versicolor_3.jpg/640px-Iris_versicolor_3.jpg',
            2: 'https://s3.amazonaws.com/eit-planttoolbox-prod/media/images/Iris-virginica--Justin-Meissen--CC-BY-SA.jpg'}
    loaded_model = joblib.load(model_joblib)

    tensor = torch.tensor([values])

    with torch.no_grad():
        y_pred = loaded_model(tensor)
        _, y_pred_test = torch.max(y_pred.data, 1)

    return names[y_pred_test.numpy()[0]], urls[y_pred_test.numpy()[0]]
