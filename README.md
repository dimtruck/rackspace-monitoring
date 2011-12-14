# rackspace-monitoring

rackspace-monitoring is a Python client library for Rackspace Cloud Monitoring
built on top of [Apache Libcloud](http://libcloud.apache.org).

# Installation

`pip install rackspace-monitoring`

# Usage

```python
from pprint import pprint

from rackspace_monitoring.providers import get_driver
from rackspace_monitoring.types import Provider

Cls = get_driver(Provider.RACKSPACE)
driver = Cls('username', 'api key')
pprint(driver.list_entities())
```

# Issues, Feedback

Please use Github issues or send an email to `cmbeta@rackspace.com`.
