import threading
from collections import deque
import time
import input_wrapper
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import sys

# glaobal Constants
# TODO: make these constants configurable
keybind1 = "x"
keybind2 = "c"
targetHz = 1000
drawFPS = 60
secondsKept = 2
lineColor = '#FFFFFF'
bgColor = '#000000'
thinTopBottomLineColor = '#808080'
thinLineThickness = 0.2

# two deques to store the analog values of the keys, initialized to 0
key1_deque = deque([0] * (targetHz * secondsKept), maxlen=(targetHz * secondsKept))
key2_deque = deque([0] * (targetHz * secondsKept), maxlen=(targetHz * secondsKept))



def poll_keys(wp):
	result = wp.read_full_buffer()
	key1_deque.append(result[0])
	key2_deque.append(result[1])

def update_key_loop(id, stop):
	#init wooting sdk wrapper
	wp = input_wrapper.Wrapper(input_wrapper.get_usb_code(keybind1), input_wrapper.get_usb_code(keybind2))

	interval = 1 / targetHz
	next_call = time.time()
	
	while True:
		# poll the keys at the target rate, and sleep until the next poll
		current_time = time.time()
		if current_time >= next_call:
			poll_keys(wp)   #acutally poll the keys
			next_call += interval
			sleep_time = next_call - time.time()
			if sleep_time > 0:
				time.sleep(sleep_time)
		if stop():
			sys.exit(0)
	

def update_plot():
	global key1_deque, key2_deque, ax1, ax2

	# Update the plots
	ax1.clear()
	ax1.plot(key1_deque, color=lineColor)
	ax1.set(ylim=(-0.01,1.01))
	ax1.axis('off')  # Remove the axes

	ax2.clear()
	ax2.plot(key2_deque,  color=lineColor)
	ax2.set(ylim=(-0.01,1.01))
	ax2.axis('off')  # Remove the axes

	ax1.axhline(y=0, color=thinTopBottomLineColor, linestyle='-', linewidth=thinLineThickness)
	ax1.axhline(y=1, color=thinTopBottomLineColor, linestyle='-', linewidth=thinLineThickness)
	ax2.axhline(y=0, color=thinTopBottomLineColor, linestyle='-', linewidth=thinLineThickness)
	ax2.axhline(y=1, color=thinTopBottomLineColor, linestyle='-', linewidth=thinLineThickness)

	

	# Draw the canvas
	canvas.draw()

	# Schedule the next update
	frame_interval = 1000 / drawFPS
	root.after(int(frame_interval), update_plot)  # Update every 100 milliseconds (0.1 second)

def _quit():
	global stop_threads, key_thread
	stop_threads = True
	root.quit()
	root.destroy() 

if __name__ == "__main__":
	stop_threads = False
	key_thread = threading.Thread(target=update_key_loop, args=(id, lambda: stop_threads)).start()


	# Create the main window
	root = tk.Tk()
	root.protocol("WM_DELETE_WINDOW", _quit)
	root.title("woot-overlay")
	root.geometry("800x200")

	# Create a frame for the plots
	frame = ttk.Frame(root)
	frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

	# Create a matplotlib figure
	fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))
	fig.subplots_adjust(left=0, right=1, top=0.9, bottom=0.1)
	fig.patch.set_facecolor(bgColor)

	# Integrate the figure into the tkinter canvas
	canvas = FigureCanvasTkAgg(fig, master=frame)
	canvas.draw()
	canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=0, pady=0)

	# Start updating the plots
	update_plot()

	# Start the tkinter main loop
	root.mainloop()

	

