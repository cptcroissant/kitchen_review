import torch
import re


def predict_example(sentence, tokenizer, model):
    trigger_words = r'хуй|хуё|хуе|пизд|пидор|говно|хует|ебало|поебота|говно|ебат|гнойн|уебск|долбое|херовый|херня'
    if not re.findall(r'[А-я]', sentence):
        return 'по русски пиши, а!'
    if re.findall(trigger_words, sentence):
        return 'у нас тут культурное общество, убирай мат'
    if len(sentence.split()) <= 1:
        return 'напиши больше слов'

    tokens = tokenizer.tokenize(sentence)
    tokens = tokens[:510]
    indexed = [2] + tokenizer.convert_tokens_to_ids(tokens) + [3]
    tensor = torch.LongTensor(indexed).to('cpu')
    tensor = tensor.unsqueeze(0)
    prediction = torch.sigmoid(model(tensor))
    res = round(prediction.item(), 4)
    if res <= 0.3 :
        ans = "Комментарий отрицательный"
    elif 0.3 < res <= 0.5:
        ans = "Комментарий скорее отрицательный"
    elif 0.5 < res <= 0.7:
        ans = "Комментарий скорее положительный"
    elif res >= 0.7:
        ans = "Комментарий положительный"

    return str(ans) + ', ' + str(round(prediction.item(), 4))
