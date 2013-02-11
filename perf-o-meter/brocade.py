#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
#
# Autor: Tobias Brunner <tobias.brunner@nine.ch>

### brocade_bgp
def perfometer_brocade_bgp(row, check_command, perf_data):
     color = { 0: "#68f", 1: "#ff2", 2: "#f22", 3: "#fa2" }[row["service_state"]]
     routes = int(perf_data[0][1])
     return "%.0f" % routes, perfometer_logarithmic(routes, 200000, 10, color)

perfometers['check_mk-brocade_bgp'] = perfometer_brocade_bgp

### brocade_cpu
def perfometer_brocade_cpu(row, check_command, perf_data):
     color = { 0: "#68f", 1: "#ff2", 2: "#f22", 3: "#fa2" }[row["service_state"]]
     load = float(perf_data[0][1])
     return "%.1f" % load, perfometer_linear(load, color)

perfometers['check_mk-brocade_cpu'] = perfometer_brocade_cpu

### brocade_mem
def perfometer_brocade_mem(row, check_command, perf_data):
     color = { 0: "#68f", 1: "#ff2", 2: "#f22", 3: "#fa2" }[row["service_state"]]
     mem = float(perf_data[0][1])
     return "%d%%" % mem, perfometer_linear(mem, color)

perfometers['check_mk-brocade_mem'] = perfometer_brocade_mem

### brocade_temp
def perfometer_brocade_temp(row, check_command, perf_data):
     color = { 0: "#68f", 1: "#ff2", 2: "#f22", 3: "#fa2" }[row["service_state"]]
     temp = float(perf_data[0][1])
     return "%.1f" % temp, perfometer_linear(temp, color)

perfometers['check_mk-brocade_temp'] = perfometer_brocade_temp
