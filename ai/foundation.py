from transformers import pipeline, AutoTokenizer

class LMMistral:
    """Class for loading and using Mistral language model."""

    def __init__(self):
        """Initialize LMMistral with Mistral-7B-Instruct-v0.2 base model."""
        base_model = "mistralai/Mistral-7B-Instruct-v0.2"
        tokenizer = AutoTokenizer.from_pretrained(base_model, trust_remote_code=True)
        self.pipe = pipeline(task="text-generation", model=base_model, tokenizer=tokenizer, max_length=200)