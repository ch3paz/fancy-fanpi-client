#!/usr/bin/python3

import math
import time
import configparser
from sht_sensor import Sht

# Read settings from file
ffpi_configparser = configparser.RawConfigParser()
ffpi_configfilepath = r'ffpi_settings.config'
ffpi_configparser.read(ffpi_configfilepath)

sht_sensor_clock = int(ffpi_configparser.get('ffpi_sht_settings', 'sensorclockpin'))
sht_sensor_1_data = int(ffpi_configparser.get('ffpi_sht_settings', 'sensor1datapin'))

# Config the pins where the SHT75 are connected
# Sht(clockpin, datapin)
sht_sensor = Sht(sht_sensor_clock, sht_sensor_1_data)


def sht75_read_sensors():
    # Read sensor
    sht_temperature = sht_sensor.read_t()
    sht_humidity = sht_sensor.read_rh()
    sht_dewpoint = sht_sensor.read_dew_point()
    sht_absolute = 216.7 * (sht_humidity / 100.0 * 6.112 *
                            math.exp(17.62 * sht_temperature /
                                     (243.12 + sht_temperature)) /
                            (273.15 + sht_temperature))

    hval_sensor = format(sht_humidity, "2.1f")
    tval_sensor = format(sht_temperature, "2.1f")
    dval_sensor = format(sht_dewpoint, "2.1f")
    aval_sensor = format(sht_absolute, "2.1f")

    # Json for pushing to influxdb
    data_json = [{
        "measurement": "Roofcollect",
        "tags": {
            "Location": "Roof",
        },
        "time": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "fields": {
            "RH": hval_sensor,
            "T": tval_sensor,
            "DP": dval_sensor,
            "AH": aval_sensor,
        }
    }]

    return data_json
