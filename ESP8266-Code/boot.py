# boot.py
import gc
import esp
import network
import time

esp.osdebug(None)
gc.collect()

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect("OPPO A95", "bebe@2024")

    print("Connecting WiFi...")
    for _ in range(15):
        if wlan.isconnected():
            break
        time.sleep(1)

    print("WiFi connected")
    print("IP:", wlan.ifconfig()[0])
    return wlan

# ---- BOOT ----
wlan = connect_wifi()

# đợi hệ thống ổn định
time.sleep(2)

# gọi main thủ công
try:
    import main
except Exception as e:
    print("MAIN ERROR:", e)

