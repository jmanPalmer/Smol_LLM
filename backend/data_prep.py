from datasets import load_dataset

ds = load_dataset("mlabonne/orca-agentinstruct-1M-v1-cleaned")

# Save the dataset to a JSON Lines file
ds["train"].to_json("DataSet.jsonl")

print("Done")