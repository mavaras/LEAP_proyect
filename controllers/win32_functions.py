# ===============WIN32 CONTROL FUNCTIONS===============
# == actions
# == keyboard functions


import sys
import time
import ctypes
import win32con, win32gui


# needed variables
EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible

opened_windows_names = []


def get_opened_windows_list():
	""" returns an array with all opened windows titles"""
	global opened_windows_names
	EnumWindows(EnumWindowsProc(foreach_window), 0)
	return opened_windows_names


def foreach_window(hwnd, lParam):
	""" this is passed as argument when we call EnumWindows
	Fills titles array with current opened windows names
	:param hwnd: Window handle
	"""

	global opened_windows_names
	if IsWindowVisible(hwnd):
		length = GetWindowTextLength(hwnd)
		buff = ctypes.create_unicode_buffer(length + 1)
		GetWindowText(hwnd, buff, length + 1)
		if buff.value != "":
			opened_windows_names.append(buff.value)

	return True


def bring_window_to_top(hwnd):
	""" bring to front hwnd window
	:param hwnd: Window handle"""
	win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
	win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)


def minimize_window(hwnd):
	""" minimizes hwnd window
	:param hwnd: Window handle"""
	win32gui.CloseWindow(hwnd)


def close_window(hwnd):
	""" closes hwnd window
	:param hwnd: Window handle"""
	win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)


def get_current_window_hwnd():
	""" return current window hwnd
	:return: window handle"""
	return win32gui.GetForegroundWindow()


def get_current_window_name():
	""" returns currently on top window name
	:return: window name"""
	hwnd = get_current_window_hwnd()
	length = GetWindowTextLength(hwnd)
	buff = ctypes.create_unicode_buffer(length + 1)
	GetWindowText(hwnd, buff, length + 1)
	# print("buff.value: "+buff.value.encode('latin1'))
	return buff.value


# return unicode(win32gui.GetWindowText(win32gui.GetForegroundWindow()), errors="ignore")

