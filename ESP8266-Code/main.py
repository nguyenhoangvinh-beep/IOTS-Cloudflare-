import socket
import machine

led1 = machine.Pin(5, machine.Pin.OUT)
led2 = machine.Pin(4, machine.Pin.OUT)

s = socket.socket()
s.bind(('', 80))
s.listen(1)

print("ESP Web Server running...")

while True:
    conn, addr = s.accept()
    request = conn.recv(1024).decode()

    if "/led1/on" in request:
        led1.on()
    if "/led1/off" in request:
        led1.off()
    if "/led2/on" in request:
        led2.on()
    if "/led2/off" in request:
        led2.off()

    # Get current statuses
    led1_status = "on" if led1.value() else "off"
    led2_status = "on" if led2.value() else "off"

    response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nLED1=" + led1_status + "\r\nLED2=" + led2_status + "\r\n"
    conn.send(response)
    conn.close()

