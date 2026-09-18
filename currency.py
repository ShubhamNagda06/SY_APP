import re

text = """
The invoice contains ₹500, ₹1,250, Rs. 5000 and Rs 12,500.
"""

pattern = r'(?:₹|Rs\.?)\s?\d{1,3}(?:,\d{3})*(?:\.\d+)?|\bRs\.?\s?\d+'

currency_values = re.findall(pattern, text)

print("Currency values found:")
for value in currency_values:
    print(value)