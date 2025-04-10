import gradio as gr
import easyocr
from datetime import datetime
from datetime import timezone
from datetime import timedelta

parked_vehicles = dict()
reader = easyocr.Reader(lang_list=['en'], gpu=False)

def parking_lot_ocr(uploaded_img: str, ntd_per_sec: int=1):
    results = reader.readtext(uploaded_img, allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-',detail=0)
    entry_time = datetime.now(timezone.utc) + timedelta(hours=8)
    entry_time_str = entry_time.strftime('%Y-%m-%d %H:%M:%S')

    if len(results) == 2:
        car_plate = results[1]
    else:
        car_plate = results[0]

    if car_plate not in parked_vehicles.keys():
        parked_vehicles[car_plate] = entry_time
        return f'''                  Welcome to the parking lot {car_plate}!\n
                   Your entry time is: {entry_time_str}.\n
                   Parking fee is NT${ntd_per_sec} per second.'''
    else:
        leaveing_time = datetime.now(timezone.utc) + timedelta(hours=8)
        time_elapsed = leaveing_time - parked_vehicles[car_plate]
        seconds_elapsed = int(time_elapsed.total_seconds())
        charge_amount = seconds_elapsed * ntd_per_sec
        parked_vehicles.pop(car_plate, None)
        return f'''                   Bye {car_plate}~\n
                   Your vehicle stayed {seconds_elapsed} seconds.\n
                   You will be charged NT${charge_amount:,}.'''
        
demo = gr.Interface(fn=parking_lot_ocr,
                    inputs=gr.Image(),
                    outputs='text',
                    title='小小停車場',
                    theme='John6666/YntecDark')
demo.launch()