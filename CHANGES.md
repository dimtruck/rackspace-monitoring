rackspace-monitoring v0.3.0 - 2012-07-23:

* Add new agent related methods.
  [Ryan Phillips]

* Remove `ex_delete_children` argument from the `delete_entity` method.

rackspace-monitoring v0.2.10 - 2012-07-18:

- Fix a bug with forcing base_url in the driver constructor.
  [Jessica Lucci]

rackspace-monitoring v0.2.9 - 2012-06-13:

* Add get_monitoring_zone method.
* Add ex_traceroute method.

rackspace-monitoring v0.2.8 - 2012-05-31:

* Fix agent token creation.
  [Ryan Philips]

rackspace-monitoring v0.2.7 - 2012-05-30:

* Fix a bug with parsing object id from the URL in the response header which
  could occur in some rare conditions.

rackspace-monitoring v0.2.6 - 2012-05-29:

* Modify the connection class is it works with Libcloud 0.9.0 and above
* Add new `test_existing_check` method

rackspace-monitoring v0.2.5 - 2012-04-04:

* Change apache-libcloud dependency version to be < 0.9.0

rackspace-monitoring v0.2.4 - 2012-03-29:

* Add __str__ method to validation error and latest alarm state class.
* Add new test_notification and test_existing_notification method

rackspace-monitoring v0.2.3 - 2012-01-21:

* Update parsing an object if from the Location header so it work with the new
  URLs which contain tenant ids.
* Add missing 'target_hostname' kwargs to *_check methods.

rackspace-monitoring v0.2.2 - 2012-01-04:

 * Fix a bug in update_check.

rackspace-monitoring v0.2.1 - 2011-12-22:

* Make all the create, update and delete methods take an optional 'who' and
  'why' keyword arguments.

rackspace-monitoring v0.2.0 - 2011-12-15:

 * Update 'alarm history' endpoint. It has been renamed from 'alarm history'
   to 'alarm notification history'.

 * Don't error out if entity has no IP addresses.
   [Caleb Groom]

 * Make sure it works with Python 2.5 and 3

rackspace-monitoring v0.1.0 - 2011-12-14:

 * Initial release.
