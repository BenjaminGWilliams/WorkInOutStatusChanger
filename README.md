# WorkInOutStatusChanger

A script to change status on work intranet to custom messages. This is best called on an automatic time trigger with Windows Task Scheduler.


## Arguments:

```
InOut.py
Commands:
-h: Brings up help (This), or
-i: Set to in, or
-f: Finished for the day, or
-o 'LOCATION','TIME TO ADD': Puts status to 'LOCATION' and adds specified 'TIME'.>"If -o is called must provide 'LOCATION' and 'TIME TO ADD'
TIME must be in the following list:
'Qtr' - 15 mins
'mQtr' - negative 15 mins"
'Half' - 30 mins
'Hour' - an hour
'Day' - a day"
```



    

## Usage example

* Set status to 'IN'

```
"C:\path\to\python\pythonw.exe" "E:\path\to\script\InOut.py" -i
```

* Set status to "Coffee Room" for 15 minutes

```
"C:\path\to\python\pythonw.exe" "E:\path\to\script\InOut.py" -o "Coffee Room,Qtr"
```

* Set status to 'AT LUNCH' for one hour

```
"C:\path\to\python\pythonw.exe" "E:\path\to\script\InOut.py" -o "AT LUNCH,Hour"
```

* Set status to "Finished for the Day" until 8am the next working day

```
"C:\path\to\python\pythonw.exe" "E:\path\to\script\InOut.py" -f
```
