# Description

An stripped down implementation of "fancy-fanpi" which just reads one sht75 and sends the data to the influxdb-server.

# Configuration

Adapt settings in

* ffpi_settings.config

Adapt the systemd-timer and systemd-service files, copy them to /etc/systemd/system/ and

* enable
* restart

them.

# Setup

We need the sht75-lib, influx-client and the configparser:

~~~
pip3 install sht-sensor influxdb configparser
~~~

