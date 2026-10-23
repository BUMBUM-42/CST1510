"""
RECORD CHECK  -  my version
===========================

Name  :Abaasa Kaije
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""



class Record:
    def __init__(self, label, value, limit):
        """Define label limit and value"""
        self.label = label
        self.value = value
        self.limit = limit

records = [Record("srv-01", 87.0, 100.0), 
           Record("srv-02", 95.0, 100.0), 
           Record("srv-03", 120.0, 100.0) ]   # replace with your code

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    
    # your report lines go here

    print( f"GB used: {record.value}")
    print( f"Total GB: {record.limit}")
print("=" * 34)


