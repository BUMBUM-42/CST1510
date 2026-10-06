"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

Record_Check = input("Enter your hostname: ")      
used = 87
total = 120
difference = total - used   
percent = (used / total) * 100   
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {Record_Check}")
print("=" * 34)
print(f"used - {used:>.2f}")
print(f"total - {total:>.2f}")
print(f"free - {difference:>.2f}")
print(f"percent - {percent:>.2f}%")
print("=" * 34)
