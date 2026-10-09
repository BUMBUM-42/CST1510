"""
RECORD CHECK  -  my version
===========================

Name  :Abaasa Kaije
Lane  :   IT    
Date  :9/10/26

Run it:   python template.py

"""
RECORD_CHECK = input("Enter hostname: ")      
used = float(input("Enter used data: "))
total =float(input("Enter total data: "))     

def status_of(percent):
    if(percent >= 100):
        """Return whether user is over limit or ok"""
        return "OVER-LIMIT"
    elif(percent >= 90):
        return "WARNING"

def check(used, total):
    """Return percent and difference"""
    difference = total - used
    percent = (used / total) * 100
    return difference, percent

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {RECORD_CHECK}")
print("=" * 34)
print(f" Used - {used:>8.2f}")
print(f" Total - {total:>8.2f}")
difference, percent = check(used, total)
print(f"free - {difference:>8.2f}")
print(f"Percent - {percent:>8.2f}%")
print(f"Status - {status_of(percent)}")
print("=" * 34)

