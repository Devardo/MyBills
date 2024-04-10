services = {'water':['Cobb County Water System'], 'light':['GreyStone Power'], 'gas':['Austell Gas'],'mobile':['Xfinity Mobile'], 'security':['ADT'], "waste" : "The Diamond Disposal"}

# This function parss the service provider dictionary to get all the listed service providers
def get_all_providers():
    all_providers = []
    for providers_lists in services.values():
        for provider in providers_lists:
            all_providers.append(provider)
    return all_providers


# This function checks gains the list of all providers to determine if the line has the provider name in it





providers =[
    {"Name": "Cobb County Water System", "Category": "Water"},
    {"Name": "Greystone Power", "Category": "Power"},
    {"Name": "Austell Gas", "Category": "Gas"},
    {"Name": "Xfinity Mobile", "Category": "Mobile"},
    {"Name": "ADT", "Category": "Security"},
    {"Name": "The Diamond Disposal", "Category": "Waste"},
   ]


my_providers = [provider['Name'] for provider in providers]

for line in lines:
    if line in my_providers:
        bill_povider = line

print ('Austell Gas' in my_providers)