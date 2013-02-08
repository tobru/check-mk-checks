# check-mk-checks - Checks for Check_MK

Some additional checks for [http://mathias-kettner.de/check_mk.html](Check_MK)

They all feature automatic inventory and documentation

# Included checks

## SNMP

* brocade_bgp
* brocade_cpu
* brocade_fan
* brocade_mem
* brocade_psu
* brocade_temp

## Agent

* not yet available

# How to use them

Just run `rake prepare[0.1]` and `rake build`. This creates a Debian package
which can be easily deployed to the monitoring server.

All checks are documented. Run `cmk -M` to see the documentation.

# Credits

All checks are inspired by the original distributed checks.
Credits to the writer of them.

# License / Author

The checks are written by

* Tobias Brunner <tobias.brunner@nine.ch>

Licensed under GNU GPL, Copyright 2013 Tobias Brunner

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
