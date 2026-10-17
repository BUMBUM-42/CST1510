"""
RECORD CHECK  -  my version
===========================

Name  :Abaasa Kaije
Lane  :    IT      (delete two)
Date  :17/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
records = [{"label": "R-001", "value": 87, "limit": 100},
           {"label": "R-002", "value": 120, "limit": 100},
           {"label": "R-003", "value": 45, "limit": 100}
]

def check_record(record):
    """Return whether user is over limit or ok"""
    if(record["value"] >= record["limit"]):
        return "OVER-LIMIT"
    return "OK"

def print_report(record, status):
    """Print the report for a record."""
    print(f"Record: {record["label"]} , Value: {record["value"]} , Limit: {record["limit"]} , Status: {status}")

    
for record in records:
    status = check_record(record)
    print_report(record, status)





