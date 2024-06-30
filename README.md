# Pomodoro Timer


<p align = "center">

<img src="https://github.com/Amina-Sagheer/pomodoro/assets/172102325/a74dbb3b-a36f-4ff8-868a-fb35290b1be0" alt="pomodoro_gif" width="500" height="500">

</p>

This is a Pomodoro Timer application built using Python and Tkinter. It helps manage work sessions and breaks using the Pomodoro Technique, improving productivity and focus.

## Features

- **Work Sessions**: 25 minutes of focused work.
- **Short Breaks**: 5 minutes of break after each work session.
- **Long Break**: 20 minutes of break after completing four work sessions.
- **Reset Functionality**: Allows you to reset the timer and start a new cycle.
- **Visual and Textual Timer Display**: Displays the remaining time and session type.

## How to Use

1. **Start the Timer**: Click the "Start" button to begin a work session.
2. **Reset the Timer**: Click the "Reset" button to stop the timer and reset the display to "00:00".

### Work and Break Sessions:

- The timer will start with a 25-minute work session.
- After the work session, a 5-minute break will start automatically.
- This cycle repeats four times, and after the fourth work session, a 20-minute long break will occur.
- The timer will reset after the long break.

## Code Overview

### Global Variables

- `i`: A counter to track the number of work sessions completed.
- `TIMER`: A variable to hold the reference to the `after` job, allowing it to be canceled later.

### Functions

- **count_down(count)**:
    Updates the timer display every second and schedules itself to be called again after one second.

- **reset()**:
    Stops the timer and resets the display to "00:00".

- **start_timer()**:
    Manages the Pomodoro timer cycles, alternating between work and break sessions.

### UI Elements

- **window**: The main Tkinter window.
- **label**: Displays the text "TIMER".
- **canvas**: Displays the tomato image and the timer text.
- **start_button**: Button to start the timer.
- **reset_button**: Button to reset the timer.
- **label2**: Displays a checkmark.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
