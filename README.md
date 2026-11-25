# Age Calculator

A simple command-line Age Calculator written in Python. It calculates a person's age in **years, months, and days** using their date of birth.

## Features

- Accepts date of birth in `YYYY-MM-DD` format.
- Calculates age in years, months, and days.
- Uses the current system date automatically.
- Rejects dates in the future.
- Handles invalid date input with a clear error message.
- Uses Python's built-in `datetime` module; no third-party packages are required.

## Requirements

- Python 3.7 or later
- No external libraries required

## How to Run

1. Download or clone this repository.
2. Open a terminal or command prompt in the project folder.
3. Run:

   ```bash
   python project.py
   ```

   On some systems, use:

   ```bash
   python3 project.py
   ```

4. Enter your date of birth when prompted, using `YYYY-MM-DD`.

## Example

```text
today's date is: 2026-11-25
Enter your birth date in YYYY-MM-DD format: 2004-06-15
your date of birth is: 2004-06-15
your age today is: 22 years, 5 months, and 10 days
```

*The displayed age will change depending on the date you run the program and the date of birth you enter.*

## Project Structure

```text
Age-Calculator/
├── project.py
├── README.md
└── .gitignore
```

## Screenshot

A screenshot is optional for this command-line project. To add one, run the program, capture the terminal showing a sample successful calculation, save the image as `screenshot.png` in this repository, and add the following to this README:

```markdown
![Age Calculator running in the terminal](screenshot.png)
```

## Concepts Used

- Python functions
- `datetime.date`
- User input with `input()`
- Conditional statements
- Exception handling (`try-except`)
- Date arithmetic

## Future Improvements

- Add a graphical user interface (GUI).
- Display the user's next birthday and days remaining.
- Add more automated tests for different dates and leap years.

## License

This project is available for personal learning and educational use. Add a formal license if you want to specify permissions for reuse and distribution.
