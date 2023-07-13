# print("Start simulator (SITL)")
import dronekit_sitl
# sitl = dronekit_sitl.start_default()
# connection_string = sitl.connection_string()
connection_string = "tcp:127.0.0.1:5762"

import sys

if sys.version_info.major == 3 and sys.version_info.minor >= 10:
    import collections
    setattr(collections, "MutableMapping", collections.abc.MutableMapping)

# Import DroneKit-Python
from dronekit import connect, VehicleMode

# Connect to the Vehicle.
print("Connecting to vehicle on: %s" % (connection_string,))
vehicle = connect(connection_string, wait_ready=True, timeout=50)

# Get some vehicle attributes (state)
print("Get some vehicle attribute values:")
print(" GPS: %s" % vehicle.gps_0)
print(" Battery: %s" % vehicle.battery)
print(" Last Heartbeat: %s" % vehicle.last_heartbeat)
print(" Is Armable?: %s" % vehicle.is_armable)
print(" System status: %s" % vehicle.system_status.state)
print(" Mode: %s" % vehicle.mode.name)    # settable

msg = vehicle.message_factory.command_long_encode(
    1, 0,
    65000,
    0,
    1,
    2,
    3.0,
    0,0,0,0)
vehicle.send_mavlink(msg)

# Close vehicle object before exiting script
vehicle.close()

# Shut down simulator
# sitl.stop()
print("Completed")