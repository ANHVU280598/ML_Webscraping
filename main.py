import webbrowser
import time
import pygetwindow as gw
import pyautogui
from PIL import ImageChops
import os

# Utility: Compare screenshots
def screenshots_are_similar(img1, img2, threshold=5):
    diff = ImageChops.difference(img1, img2).getbbox()
    return diff is None  # True if no visual difference

# Create images directory if it doesn't exist
os.makedirs("images", exist_ok=True)

# Step 1: Open the browser window
webbrowser.open("https://walmart.com")

# Step 2: Wait for the browser to open and load
time.sleep(8)

# Step 3: Find the browser window by its title
windows = gw.getWindowsWithTitle("Walmart | Save Money. Live better.")

if windows:
    window = windows[0]
    window.activate()
    time.sleep(1)

    left, top, width, height = window.left, window.top, window.width, window.height

    # Initial screenshot
    prev = pyautogui.screenshot(region=(left, top, width, height))
    prev.save("images/scroll_000.png")
    print("Saved: images/scroll_000.png")

    scroll_count = 1

    while True:
        pyautogui.scroll(-800)
        time.sleep(1.5)

        curr = pyautogui.screenshot(region=(left, top, width, height))
        filename = f"images/scroll_{scroll_count:03d}.png"
        curr.save(filename)
        print(f"Saved: {filename}")

        if screenshots_are_similar(prev, curr):
            print("Reached bottom of the page.")
            break

        prev = curr
        scroll_count += 1

    # Step 7: Close browser window
    window.close()

else:
    print("Browser window not found. Make sure the browser is open and title matches.")
