# rackspace-monitoring

rackspace-monitoring is a Python client library for Rackspace Cloud Monitoring
built on top of [Apache Libcloud](http://libcloud.apache.org).

# Installation

Library can be installed using `pip`:

```bash
pip install rackspace-monitoring
```

# Usage

```python
from pprint import pprint

from rackspace_monitoring.providers import get_driver
from rackspace_monitoring.types import Provider

Cls = get_driver(Provider.RACKSPACE)
driver = Cls('username', 'api key')
pprint(driver.list_entities())
```

# Testing, style, code coverage

## Running tests

`python setup.py test`

## Checking pep8 compliance

`python setup.py pep8`

## Genrating code coverage report

`python setup.py coverage`

# Issues, Feedback

Please use Github issue tracker or send an email to `cmbeta@rackspace.com`.
