# Shutdown Timer

Shutdown Timer is a Python application that allows users to schedule shutdown times for Windows computers. With an intuitive interface built using PyQt5, users can easily set a specific time for their computer to shut down. The application allows users to cancel and re-schedule the timer.

## Features

- Schedule shutdown times for Windows computers.
- Intuitive interface built with PyQt5.
- Support for cancelling and re-scheduling shutdown timer.
- **Shutdown at a specific time:** Input the time in 12-hour format (hh/mm) to schedule a shutdown.
- **Shutdown after a certain duration:** Input the number of minutes after which the system should shut down.
- **Progress bar:** Displays a progress bar indicating the time remaining until shutdown.

## Requirements

- Python 3.7 - 3.9 (**3.8 recommanded**)

## Installation

1. Clone the repository

`git clone https://github.com/mursalatul/shutdown-timer-for-windows.git`

or [download](https://github.com/mursalatul/shutdown-timer-for-windows/archive/refs/heads/master.zip) the zip.

3. Install dependencies

- `python -m venv venv` creating virtual environment is optional but recommanded.
- `pip install -r requirements.txt`


## Usage

- **GUI Version**: To run the GUI version of the application, execute `shutdowntimer_gui.py`.

- **Command Line Version**: To run the command-line version of the application, execute `shutdowntimer.py`.


## Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## License

<h3>This program is licensed on GPL-3.0 license</h3> which granting you the freedom to use, modify, and redistribute the software under the same license terms. See the [LICENSE](https://github.com/mursalatul/shutdown-timer-for-windows/blob/master/LICENSE) file for details.
