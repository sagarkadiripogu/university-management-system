import time
from datetime import datetime
def greet():
    print("=================================================")
    print("===> Welcome to University Management System <===")
    print("=================================================")
    print()
    x=datetime.now()
    print("LOGIN TIME:")
    print(f"Date: {x.date()}")
    print(f"Time: {x.time()}")
    