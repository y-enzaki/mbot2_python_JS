import cyberpi

mes = cyberpi.mesh_broadcast.get("message")
a = (mes / 201 - 100)
b = (mes % 201 - 100)
cyberpi.mbot2.drive_power(a, b)
c = ((mbot2.EM_get_angle("EM1") % 360 + 360)) % 360
d = ((mbot2.EM_get_angle("EM2") % 360 + 360)) % 360
cyberpi.mesh_broadcast.set("message", (c * 360 + d))