import tkinter as tk
from tkinter import font as tkFont
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class BubbleSort:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bubble Sort Visualization")
        # Üst bilgi (Header)
        header_font = tkFont.Font(family="Helvetica", size=12, weight="bold")
        self.header_label = tk.Label(self.root, text="Bubble Algorithm by Mehmet Kahya", font=header_font, pady=10)
        self.header_label.pack()

        # Üst kısım: Kullanıcı girişi ve düğme
        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(pady=10)

        self.entry_label = tk.Label(self.entry_frame, text="Enter numbers separated by commas:")
        self.entry_label.pack()

        self.entry = tk.Entry(self.entry_frame)
        self.entry.pack()

        self.button = tk.Button(self.entry_frame, text="Sort", command=self.print_result)
        self.button.pack(pady=5)

        # Orta kısım: Sonuç etiketi ve grafikler
        self.result_frame = tk.Frame(self.root)
        self.result_frame.pack(pady=10)

        self.result_label = tk.Label(self.result_frame, text="")
        self.result_label.pack()

        self.figure = Figure(figsize=(6, 6), dpi=100)
        self.plot1 = self.figure.add_subplot(211)
        self.plot2 = self.figure.add_subplot(212)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.result_frame)
        self.canvas.get_tk_widget().pack()

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.result_frame)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack()

        # Alt kısım: Footer
        self.footer_frame = tk.Frame(self.root)
        self.footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

        bold_font = tkFont.Font(family="Helvetica", size=10, weight="bold")

        self.footer_label = tk.Label(self.footer_frame, text="Bubble Sort Visualization - © 2024 Mehmet Kahya", bd=1, relief=tk.SUNKEN, anchor=tk.CENTER, font=bold_font)
        self.footer_label.pack(side=tk.BOTTOM, fill=tk.X)

    def sort(self, arr):
        n = len(arr)
        swaps = 0
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swaps += 1
        return arr, swaps

    def print_result(self):
        arr = [int(num) for num in self.entry.get().split(',')]
        sorted_arr, swaps = self.sort(arr[:])

        self.result_label.config(text=f"First List: {arr}\nSorted List: {sorted_arr}\nNumber of swaps: {swaps}")

        self.plot1.clear()
        self.plot1.bar(range(len(arr)), arr, color='r')
        self.plot1.set_title('Unsorted Array')
        self.plot1.set_xticks(range(0, len(arr), max(1, len(arr)//10)))
        self.plot1.set_yticks(range(min(arr), max(arr) + 1, max(1, (max(arr)-min(arr))//10)))
        self.plot1.set_xlabel('Index')
        self.plot1.set_ylabel('Value')

        self.plot2.clear()
        self.plot2.bar(range(len(sorted_arr)), sorted_arr, color='g')
        self.plot2.set_title('Sorted Array')
        self.plot2.set_xticks(range(0, len(sorted_arr), max(1, len(sorted_arr)//10)))
        self.plot2.set_yticks(range(min(sorted_arr), max(sorted_arr) + 1, max(1, (max(sorted_arr)-min(sorted_arr))//10)))
        self.plot2.set_xlabel('Index')
        self.plot2.set_ylabel('Value')

        self.figure.tight_layout()
        self.canvas.draw()

    def run(self):
        self.root.mainloop()

def main():
    bubble_sort = BubbleSort()
    bubble_sort.run()

if __name__ == "__main__":
    main()
