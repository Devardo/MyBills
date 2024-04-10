from providers import Providers
from parser import extract_text
from textract import textract_data

# Test to determine if provider name can be found in invoice

response = textract_data()
lines = extract_text(response, extract_by="LINE")
providers = [provider['Name'] for provider in Providers]

def get_provider():
    for provider in providers:
        if provider in lines:
            return provider
    return None

provider = get_provider()

print(provider)