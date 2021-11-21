from django.shortcuts import render
from django.views.generic import TemplateView
import os
from transformers import BertTokenizer, BertModel, AutoModelForMaskedLM

import torch
import torch.nn as nn
from .forms import NameForm
from .ml.predict import prediction
from .ml.predict_text import predict_example
from .ml.gru_model import BERTGRUSentiment

HIDDEN_DIM = 256
OUTPUT_DIM = 1
N_LAYERS = 2
BIDIRECTIONAL = True
DROPOUT = 0.15
embed = BertModel.from_pretrained("cointegrated/rubert-tiny")


class IndexView(TemplateView):
    template_name = 'herokunlp/index.html'

    def get(self, request):
        form = NameForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = NameForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['input_text']

        tokenizer = BertTokenizer(vocab_file=os.path.abspath('./herokunlp/ml/vocab.txt'))
        model = BERTGRUSentiment(
            embed,
            HIDDEN_DIM,
            OUTPUT_DIM,
            N_LAYERS,
            BIDIRECTIONAL,
            DROPOUT,
            )
        model.load_state_dict(torch.load(os.path.abspath('./herokunlp/ml/rev_class_004.pt')))
        model = model.to('cpu')
        model.eval()

        result = predict_example(text, tokenizer, model)

        args = {'res': result}

        return render(request, 'herokunlp/home_2.html', args)


class ResView(TemplateView):
    template_name = 'herokunlp/home_2.html'
