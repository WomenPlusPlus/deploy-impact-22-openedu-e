

# Self-Supervised Euphemism Detection and Identification for Content Moderation

## Table of Contents
- [Introduction](#Introduction)
- [Data](#Data)
- [Code](#Code)


## Introduction
This sub-unit aims to: __Euphemism Detection__ and __Euphemism Identification__ to support the content Moderation.


## Data
Due to the license issue, we will not distribute the dataset ourselves, but we will direct the readers to their respective sources.  

## Code
### 1. Fine-tune the BERT model. 
Please refer to [this link from Hugging Face](https://github.com/huggingface/transformers/tree/master/examples/language-modeling) to fine-tune a BERT on a raw text corpus.

You may download our pre-trained BERT model on the `reddit` text corpus (from the Drug dataset) [here](https://drive.google.com/file/d/1kLZ0IWchWywXaxs61Vk6-eFmlx2rexU3/view?usp=sharing). Please unzip it and put it under `data/`.

### 2. Euphemism Detection and Euphemism Identification
```
python ./Main.py --dataset sample --target drug  
```
You may find other tunable arguments --- `c1`, `c2` and `coarse` to specify different classifiers for euphemism identification. 
Please go to `Main.py` to find out their meanings. 


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
