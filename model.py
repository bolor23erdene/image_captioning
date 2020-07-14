import torch
import torch.nn as nn
import torchvision.models as models


class EncoderCNN(nn.Module):
    def __init__(self, embed_size):
        super(EncoderCNN, self).__init__()
        resnet = models.resnet50(pretrained=True)
        for param in resnet.parameters():
            param.requires_grad_(False)
        
        modules = list(resnet.children())[:-1]
        self.resnet = nn.Sequential(*modules)
        self.embed = nn.Linear(resnet.fc.in_features, embed_size)

    def forward(self, images):
        features = self.resnet(images)
        features = features.view(features.size(0), -1)
        features = self.embed(features)
        return features
    

class DecoderRNN(nn.Module):
    def __init__(self, embed_size, hidden_size, vocab_size, num_layers=1):
        super(DecoderRNN, self).__init__()
        self.embed_size = embed_size
        self.hidden_size = hidden_size
        self.vocab_size = vocab_size
        self.num_layers = num_layers

        self.Embedding = nn.Embedding(self.vocab_size, self.embed_size)

        self.lstm = nn.LSTM(self.embed_size, self.hidden_size, self.num_layers, batch_first=True)

        self.hidden_2_vocab = nn.Linear(self.hidden_size, self.vocab_size) 

    
    def forward(self, features, captions):
        #hidden_state = 
        #cell_state = 

        word_embeddings = self.Embedding(captions[:,:-1])

        inputs = torch.cat((features.unsqueeze(dim=1),word_embeddings), dim=1)

        outputs, _ = self.lstm(inputs)#, (hidden_state, cell_state))

        final_outputs = self.hidden_2_vocab(outputs)

        return final_outputs
        

               
        
    def sample(self, inputs, states=None, max_len=20):
        " accepts pre-processed image tensor (inputs) and returns predicted sentence (list of tensor ids of length max_len) "
        
        captions = []

        batch_size = inputs.size(0)
        hidden = (torch.randn(1, 1, self.hidden_size).cuda(), torch.randn(1, 1, self.hidden_size).cuda())
        
        for i in range(max_len):
            out, hidden = self.lstm(inputs, hidden) 
            output_words = self.hidden_2_vocab(out)       
            output_words = output_words.squeeze(1)                 
            word  = output_words.argmax(dim=1)           
            captions.append(word.item())
            inputs = self.Embedding(word.unsqueeze(0))  
          
        return captions
