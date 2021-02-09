# knxgate
Serial Knxgate Python Integration on Linux

This Python Script permit to send command between serial usb UART Module knxgate (http://guidopic.altervista.org/alter/knxgate.html) to KNX Vimar bus.
The script accept 3 arguments.

Usage:
python3 /config/knxgate.py 0E 1 2A

    1st argument: Line Address
    2nd argument: ON/OFF Command
    3d argument:  Device Address

Connecting through serial you will be able to identify argument sniffing telegrams:

    1. Estabilishing connection to KNX Bus:
        minicom -D /dev/ttyACM0 -b 115200
    2. Send Logging Message to knxgate:
        @l
    3. Send ASCII logging mode command:
        @MA
   
After send this command you will be able to se KNX Telegram on KNX Bus like this:

    KNX[9]: CC
    KNX[0]: B0 10 02 00 AA 69 03 D6 01 C9 40 09 2D 00 E6
    KNX[1]: CC
    KX[2]: 8 00 AA 10 02 55 03 D5 01 C9 40 09 FD
    KNX[3]: CC
    KNX[4]: B0 10 02 00 AA 69 03 D6 01 C9 40 09 2D 00 E5
    KNX[5]: CC

Sending command between Python script you will show Telegram like this:

    Snd[09]: B0 10 0C 0D C1 E1 00 81 FF k

The telegram help you identifying the argument needed by script to activate what you need on KNX BUS:

Example:
    
    0D: Line Address (Argument 1)
    C1: Device Address (Argument 3)
    81: ON/OFF Command (Argument 2)
        80 = OFF Command -> 0
        81 = ON Command -> 1
        ON/OFF will be substitute by 0 or 1
  
More details about usage could be found here:
  http://guidopic.altervista.org/knxgate/interface.html
  
This examples show a syntax example to activate/disactivate a light device:

    command_on: 'python3 /config/knxgate.py 0D 1 C1'
    command_off: 'python3 /config/knxgate.py 0D 0 C1'

Is It possible to integrate in Home Assistant (HA) easily with the below configuration added to configuration.yaml:

    switch:
    - platform: command_line
        switches:
        taverna_light:
            command_on: 'python3 /config/knxgate.py 0E 1 01'
            command_off: 'python3 /config/knxgate.py 0E 0 01'
        lavanderia_light:
            command_on: 'python3 /config/knxgate.py 0E 1 11'
            command_off: 'python3 /config/knxgate.py 0E 0 11'

This configuration enable switch entities to HA and than you can control activation/deactivation between HA Interface.

You can also integrate HA with Alexa (https://indomus.it/guide/integrare-gratuitamente-amazon-echo-alexa-con-home-assistant-via-haaska-e-aws/) and than you could ask to Alexa to activate/deactivate your switch/light/scene.

In HA you can create automation/group or also you can use Alexa app to easily manage knx devices.

Adding this configuration in HA:

sensor:

    - platform: serial
        baudrate: 115200
        serial_port: /dev/ttyACM0

can help you to analyze telegram directly by the User Interface in realtime.
