
import time
import ctypes
import pyautogui

# Windows power management constants
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

def keep_laptop_awake():
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
    )

def restore_power_settings():
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS
    )

def main():
    total_hours = 4
    interval_seconds = 30

    total_seconds = total_hours * 60 * 60
    start = time.time()

    print("=" * 40)
    print(" LAPTOP KEEP AWAKE AUTOMATION")
    print("=" * 40)
    print(f"Duration: {total_hours} hours")
    print("Cursor movement: Every 30 seconds")
    print("Press Ctrl+C to stop anytime.")
    print()

    keep_laptop_awake()

    try:
        while time.time() - start < total_seconds:

            x, y = pyautogui.position()

            # Tiny cursor movement and return
            pyautogui.moveTo(x + 2, y, duration=0.1)
            pyautogui.moveTo(x, y, duration=0.1)

            elapsed = int(time.time() - start)
            remaining = total_seconds - elapsed

            print(
                f"Running... | "
                f"Elapsed: {elapsed // 60} min | "
                f"Remaining: {remaining // 60} min",
                end="\r"
            )

            time.sleep(interval_seconds)

    except KeyboardInterrupt:
        print("\nStopped manually by user.")

    finally:
        restore_power_settings()
        print("\nLaptop keep-awake automation stopped.")

if __name__ == "__main__":
    main()
