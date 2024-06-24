# ESP32 MacOS flashing script

## Setup

Install if required:

1. Install [Python 3](https://www.python.org)
2. Install [PySerial](https://pythonhosted.org/pyserial/pyserial.html#installation)
3. Install the [Silicon Labs USB to UART Bridge VCP driver](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)

Connect your COM adapter

## Run the Script

**Linux / MacOS**: Using the terminal, run `python3 run.py`.

Select the COM port

Select the firmware you wish to flash to the gateway.

Cross your fingers 🤞.

### Options

You can run *ncd_flasher.py* with *one* of the following command line options.

- `dev`: Use developer firmware URLs
- `ns`: Do not flash the spiffs
- `sota`: Use the sota firmware

**Windows**: You may run *run_ns.bat* or *run_sota.bat*.

## Contributing

TODO

## Testing

TODO

---

&copy; 2019 - 2021 National Control Devices, LLC. All rights reserved.
