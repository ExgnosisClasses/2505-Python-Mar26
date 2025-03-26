# Lab 1: Working with Date and Time

In this lab, you'll explore how Python handles dates, times, timestamps, and durations using the `datetime` and `time` modules. Each task presents a practical problem with a solution and explanation tailored for testers.

---

## Get the Current Date and Time

### Problem:
Log the current datetime when a test starts.

### Solution:

```python
from datetime import datetime

start_time = datetime.now()
print("Test started at:", start_time)
```

---

## Format a Datetime for Reports

### Problem:
Format the current datetime to look like "2025-03-24 14:00:00".

### Solution:

```python
formatted = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Formatted start time:", formatted)
```

---

## Parse a String into a Datetime

### Problem:
A test log line contains the string "2025-03-24T13:30:00". Convert it to a `datetime` object.

### Solution:

```python
from datetime import datetime

log_entry = "2025-03-24T13:30:00"
parsed = datetime.strptime(log_entry, "%Y-%m-%dT%H:%M:%S")
print("Parsed datetime:", parsed)
```

---

## Calculate Time Since a Step Started

### Problem:
You recorded a test step start time. Now you want to see how long it took.

### Solution:

```python
from datetime import datetime
import time

start = datetime.now()
time.sleep(2)
end = datetime.now()
duration = end - start

print("Step duration:", duration)
print("Total seconds:", duration.total_seconds())
```

---

## Get a Timestamp and Convert Back

### Problem:
You want to convert the current time to a Unix timestamp and back.

### Solution:

```python
from datetime import datetime

ts = datetime.now().timestamp()
print("Unix timestamp:", ts)

converted = datetime.fromtimestamp(ts)
print("Converted back:", converted)
```

---

## Time Zone Aware Datetime

### Problem:
Create a datetime that includes timezone information (UTC).

### Solution:

```python
from datetime import datetime, timezone

utc_now = datetime.now(timezone.utc)
print("UTC datetime:", utc_now)
```

---

## Add Days and Hours to the Current Time

### Problem:
You want to generate a test expiration date 3 days and 4 hours from now.

### Solution:

```python
from datetime import datetime, timedelta

expiry = datetime.now() + timedelta(days=3, hours=4)
print("Expiry datetime:", expiry)
```

---

## Delay a Step with `time.sleep()`

### Problem:
Simulate a delay in your test to mimic a wait for a system response.

### Solution:

```python
import time

print("Waiting for system to respond...")
time.sleep(1.5)
print("Continuing test...")
```

---
