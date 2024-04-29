from providers import Providers
from parser import extract_text
import json

#Test to determine if provider name can be found in invoice
providers = [provider['Name'] for provider in Providers]

def get_provider(lines):
    for provider in providers:
        if provider in lines:
            return provider
    return None



