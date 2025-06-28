
#from transformers import AutoTokenizer, AutoModelForSequenceClassification 

#checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
#tokenizer = AutoTokenizer.from_pretrained(checkpoint)
#model = AutoModelForSequenceClassification.from_pretrained(checkpoint)

sequence = "I've been waiting for a HuggingFace course my whole life."



#token = tokenizer.tokenize(sequence)
#token_ids = tokenizer.convert_tokens_to_ids(token)
#input_ids = torch.tensor([token_ids])
#print(token_ids)
#output = model(input_ids)
#print("Logits:", output.logits)



#model_inputs = tokenizer(sequence)
#print(model_inputs["input_ids"])

#tokens = tokenizer.tokenize(sequence)
#ids = tokenizer.convert_tokens_to_ids(tokens)
#print(ids)
#print(tokenizer.decode(model_inputs["input_ids"]))
#print(tokenizer.decode(ids))

#from datasets import load_dataset
#from transformers import AutoTokenizer, DataCollatorWithPadding

#raw_datasets = load_dataset("glue", "mrpc")
#checkpoint = "bert-base-uncased"
#tokenizer = AutoTokenizer.from_pretrained(checkpoint)


#def tokenize_function(example):
 #   return tokenizer(example["sentence1"], example["sentence2"], truncation=True)


#tokenized_datasets = raw_datasets.map(tokenize_function, batched=True)
#data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

def get_sentiment():
    return 0