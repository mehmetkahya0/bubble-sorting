# Bubble Sort Visualization

This project visualizes the Bubble Sort algorithm using a graphical interface built with Tkinter and Matplotlib. It allows users to input a list of numbers, sort them using Bubble Sort, and see both the original and sorted arrays in a visual format.

## Features

- User-friendly graphical interface
- Input field for entering numbers
- Displays the original and sorted arrays
- Shows the number of swaps made during sorting
- Uses bar charts to visualize the arrays

## Installation

To run this project, you need to have Python installed on your machine. Additionally, you need to install the following libraries:

- Tkinter
- Matplotlib

You can install Matplotlib using pip:

```sh
pip install matplotlib
```

## Usage

Clone the repository and navigate to the project directory:

```sh
git clone https://github.com/username/bubble-sorting.git
cd bubble-sorting
```

Run the script:

```sh
python main.py
```

## Code Overview

### `BubbleSort` Class

- **`__init__`**: Initializes the Tkinter window, sets up the UI components (header, input field, button, result display, and footer).
- **`sort`**: Implements the Bubble Sort algorithm. Takes a list of integers and returns the sorted list along with the number of swaps made.
- **`print_result`**: Handles the button click event. Reads the input numbers, sorts them, updates the result label, and plots the original and sorted arrays using Matplotlib.
- **`run`**: Starts the Tkinter main loop to run the application.

### Main Function

The main function creates an instance of the `BubbleSort` class and runs the application.

```python
def main():
    bubble_sort = BubbleSort()
    bubble_sort.run()

if __name__ == "__main__":
    main()
```

## Example

After running the script, a window will appear where you can enter a list of numbers separated by commas (e.g., `3,1,4,1,5,9,2,6,5,3,5`). Clicking the "Sort" button will display the original and sorted arrays along with the number of swaps made. The arrays are visualized using bar charts.

## Author

Mehmet Kahya @mehmetkahya0

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
