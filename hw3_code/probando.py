# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 13:00:08 2021

@author: gdiaz
"""


import tensorflow as tf
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

import numpy as np
from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784', data_home=".")
import torch
from torchvision import datasets, transforms
import torch.nn as nn
import tqdm
import torch.nn.functional as F

def train(model, train_loader, optimizer, epoch):
    # For things like dropout
    model.train()
    
    # Avg loss
    total_loss = 0
    
    # Iterate through dataset
    for data, target in tqdm.tqdm(train_loader):
        # Zero grad
        optimizer.zero_grad()

        # Forward pass
        output = model(data)
        
        # Negative log likelihood loss function
        loss = F.nll_loss(output, target)

        # Backward pass
        loss.backward()
        total_loss += loss.item()
        
        # Update
        optimizer.step()

    # Print average loss
    print("Train Epoch: {}\t Loss: {:.6f}".format(epoch, total_loss / len(train_loader)))
    
def test(model, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            output = model(data)
            test_loss += F.nll_loss(output, target, reduction='sum').item() # sum up batch loss
            pred = output.argmax(dim=1, keepdim=True) # get the index of the max log-probability
            correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(test_loader.dataset)

    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))
# See the torch DataLoader for more details.
train_loader = torch.utils.data.DataLoader(
    datasets.MNIST('./', train=True, download=True,
                   transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1307,), (0.3081,))
                   ])),
    batch_size=32, shuffle=True)

test_loader = torch.utils.data.DataLoader(
    datasets.MNIST('./', train=False,
                   transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1307,), (0.3081,))
                   ])),
    batch_size=32, shuffle=True)


for epoch in range(1, 10 + 1):
    train(model, train_loader, optimizer, epoch)
    test(model, test_loader)
