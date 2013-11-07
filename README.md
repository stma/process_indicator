process_indicator
=================

Little module to help create informative long running application.


basic usage
-----------

```python
indicator = ProgressIndicatorOnConsole()
indicator.start()

pool = Pool()
result = pool.map(func, big_data)

if (indicator.is_alive()):
    indicator.terminate()
```


future
------

* install
* connection to running processes for better info
