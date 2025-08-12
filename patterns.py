#patterns.py
removespecial=r'[^a-zA-Z0-9\s]'
integer = r'\b\d+\b'
dec = r'\b\d+\.\d+\b'
all_numbers = r'^[+-]?(?:\d+\.?\d*|\.\d+)$'
percentages = r'\b\d+(\.\d+)?%'
urls = r'((?:https?://|www\.)[^\s]+)'
emails = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
phone = r'\+?\d[\d\s\-\.\(\)]{7,}\d'

