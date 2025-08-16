import tkinter as tk
import ctypes
import win32gui
import win32con

TRANSPARENCY = 128  # 0 (прозрачное) — 255 (непрозрачное)

def make_window_clickthrough(hwnd, alpha):
    # Установить расширенные стили окна
    styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    styles |= win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles)
    
    # Установить альфа-прозрачность
    win32gui.SetLayeredWindowAttributes(hwnd, 0, alpha, win32con.LWA_ALPHA)

def main():
    # Получаем разрешение экрана
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)

    # Создаём окно
    root = tk.Tk()
    root.title("Overlay")
    root.overrideredirect(True)  # без рамок и заголовков
    root.attributes("-topmost", True)  # всегда сверху
    root.geometry(f"{screen_width}x{screen_height}+0+0")  # вручную разворачиваем
    root.configure(bg='black')  # цвет фона

    root.update_idletasks()  # применяем изменения

    # Получаем дескриптор окна по заголовку
    hwnd = ctypes.windll.user32.FindWindowW(None, "Overlay")
    if hwnd:
        make_window_clickthrough(hwnd, TRANSPARENCY)
    else:
        print("Не удалось получить дескриптор окна.")

    root.mainloop()

if __name__ == "__main__":
    main()
