# Smol_LLM
Custom LLM built from scratch using sample dataset "orca-agentinstruct-1M-v1" found online, passion project to better understand LLMs behind the scenes. I will essentially be doccumenting my learning journey here and steps taken to develop the smol LLM. Again it shouldn't be perfect but I just wish for it to work so I can better understand LLMS. (May decrease data size later due to lack of resources)

**DATA GATHERING**
- Found a Git page containning a list of sample data to use
- Since we are using python, retrieved the data with : from datasets import load_dataset
                                                      ds = load_dataset("mlabonne/orca-agentinstruct-1M-v1-cleaned")
  
- Afterwards saved to a .jsonl file
- Data is already cleaned but will include a cleaning procedure as this is good practice

**TOKENIZATION**
- The goal here is to convert human language into numbers or something readable for a machine as neural networks can only work with numbers
- use re(regular expresions) library to split the texts up first 
