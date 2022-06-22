from torch.utils.data import DataLoader, Dataset
from nltk.stem.porter import PorterStemmer
import torch.nn as nn
import numpy as np
import torch
import json
import nltk

def Training(JsonFile, IgnoreWords, device, numEpochs, batchSize, learningRate, hiddenSize, PTHfileLocation):
    Stemmer = PorterStemmer()
    class NeuralNet(nn.Module):
        def __init__(self, input_size, hidden_size, num_classes):
            super(NeuralNet, self).__init__()
            self.l1 = nn.Linear(input_size, hidden_size) 
            self.l2 = nn.Linear(hidden_size, hidden_size) 
            self.l3 = nn.Linear(hidden_size, num_classes)
            self.relu = nn.ReLU()
        
        def forward(self, x):
            out = self.l1(x)
            out = self.relu(out)
            out = self.l2(out)
            out = self.relu(out)
            out = self.l3(out)
            return out

    def Tokenize(sentence):
        return nltk.word_tokenize(sentence)

    def stem(word):
        return Stemmer.stem(word.lower())

    def bagOfWords(TokenizedSentence, words):
        sentence_words = [stem(word) for word in TokenizedSentence]
        bag = np.zeros(len(words), dtype=np.float32)
        for idx, w in enumerate(words):
            if w in sentence_words: 
                bag[idx] = 1

        return bag

    with open(JsonFile, 'r') as f:
        intents = json.load(f)

    AllWords = []
    Tags = []
    xy = []

    for intent in intents["intents"]:
        tag = intent["tag"]
        Tags.append(tag)

        for pattern in intent["patterns"]:
            w = Tokenize(pattern)
            AllWords.extend(w)
            xy.append((w, tag))

    AllWords = [stem(w) for w in AllWords if w not in IgnoreWords]

    Tags = sorted(set(Tags))
    AllWords = sorted(set(AllWords))

    Xtrain = []
    Ytrain = []

    for (pattern_sentence, tag) in xy:
        Bag = bagOfWords(pattern_sentence, AllWords)
        Xtrain.append(Bag)

        Label = Tags.index(tag)
        Ytrain.append(Label)


    Xtrain = np.array(Xtrain)
    Ytrain = np.array(Ytrain)

    inputSize = len(Xtrain[0])
    outputSize = len(Tags)

    class ChatDataSet(Dataset):
        def __init__(self):
            self.nSamples = len(Xtrain)
            self.XData = Xtrain
            self.YData = Ytrain

        def __getitem__(self, index) :
            return self.XData[index],  self.YData[index]

        def __len__(self):
            return self.nSamples

    dataset = ChatDataSet()

    trainLoader = DataLoader(dataset = dataset, batch_size = batchSize, shuffle = True, num_workers = 0)

    model = NeuralNet(inputSize, hiddenSize, outputSize).to(device=device)

    Criterion = nn.CrossEntropyLoss()
    Optimizer = torch.optim.Adam(model.parameters(), lr=learningRate)

    for epoch in range(numEpochs):
        for (words, labels) in trainLoader:
            words = words.to(device)
            labels = labels.to(dtype = torch.long).to(device)
            outputs = model(words)
            loss = Criterion(outputs, labels)
            Optimizer.zero_grad()
            loss.backward()
            Optimizer.step()

        if (epoch+1) % 100 == 0:
            print(f"Epoch [{epoch+1}]/numEpochs: {numEpochs}, Loss = {loss.item():.4f}")

    print(f"\nFinal Loss: {loss.item():.4f}\n")

    data = {
    "model_state": model.state_dict(),
    "input_size": inputSize,
    "hidden_size": hiddenSize,
    "output_size": outputSize,
    "all_words": AllWords,
    "tags": Tags
    }

    torch.save(data, PTHfileLocation)

    print(f'training complete. file saved to {PTHfileLocation}\n')
    
    return f"{loss.item():.4f}"