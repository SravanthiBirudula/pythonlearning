#
domains = ['www.google.com', 'www.facebook.com', 
           'localhost','openai.com',
           'WWW.SRAVANTHI.COM']

cleaned_domains= [d.lower() for d in domains if '.' in d]
print(cleaned_domains)