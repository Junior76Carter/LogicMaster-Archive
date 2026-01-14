"""
PROJECT: Universal Logic Clock
AUTHOR: Junior Software 76
DESCRIPTION: Cross-platform live clock (Android, iOS, Windows, Linux)
LOGIC: Real-time system monitoring with microsecond precision.
"""

import datetime
import time
import os

def clear_console():
    """
    LOGIC: Detects Operating System and clears the terminal screen.
    'nt' = Windows (Laptop) | 'posix' = Android/iPhone/Mac/Linux
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def start_clock():
    """
    LOGIC: Infinite loop to fetch and display real-time data.
    """
    try:
        while True:
            clear_console()
            
            # 1. Fetching raw system data
            now = datetime.datetime.now()
            
            # 2. Formatting Time (24h Format : Minutes : Seconds : Microseconds)
            current_time = now.strftime("%H:%M:%S")
            micro_sec = now.strftime("%f")[:3] # Displaying first 3 digits of ms
            
            # 3. Formatting Date (Day name, Date-Month-Year)
            day_name = now.strftime("%A")
            full_date = now.strftime("%d-%m-%Y")
            
            # 4. Professional Display Output
            print("="*50)
            print(f"   OFFICIAL OWNER: JUNIOR SOFTWARE 76")
            print(f"   ROLE: THE ARCHITECT (SYSTEM LOGIC)")
            print("="*50)
            print(f"   CURRENT DAY  : {day_name}")
            print(f"   SYSTEM DATE  : {full_date}")
            print("-" * 50)
            print(f"   LIVE TIME    : {current_time}:{micro_sec}")
            print("="*50)
            print("   STATUS: [ ACTIVE ] MONITORING SYSTEM...")
            print("   (Press Ctrl+C to terminate)")

            # Refresh rate: 0.1 seconds for smooth microsecond animation
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\n[!] System Monitor Terminated by User.")

if __name__ == "__main__":
    start_clock()
