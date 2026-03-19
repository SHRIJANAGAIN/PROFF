# Sample loading script for SKT OMNI SUPREME
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "Shrijanagain/SKT_OMNI_SUPREME"
tokenizer = AutoTokenizer.from_pretrained(model_id)
# Model is gated, requires access approval
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", trust_remote_code=True)

print("SKT OMNI SUPREME 1.1T Loaded Successfully.")
