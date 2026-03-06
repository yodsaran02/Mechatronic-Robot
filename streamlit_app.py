import json
import time

import serial
import streamlit as st

def update_servo():
        if "ser" not in st.session_state:
                st.error("Serial connection is not initialized.")
                return
        servo_data = {
                "s0": int(st.session_state.s0),
                "s1": int(st.session_state.s1),
                "s2": int(st.session_state.s2),
                "s3": int(st.session_state.s3),
                "s4": int(st.session_state.s4)
        }
        json_string = json.dumps(servo_data) + "\n"
        st.session_state.ser.write(json_string.encode("utf-8"))
        st.session_state.ser.flush()
        st.success(f"Sent: {json_string.strip()}")

st.set_page_config(page_title="Serial JSON Sender", layout="centered")
st.title("Arduino Serial JSON Sender")

port = st.text_input("Serial port", value="/dev/cu.usbserial-120")
baud_rate = st.number_input("Baud rate", min_value=300, max_value=2_000_000, value=115200, step=100)

s0 = st.slider("s0", 0, 1000, 100, key="s0", on_change=update_servo)
s1 = st.slider("s1", 0, 1000, 100, key="s1", on_change=update_servo)
s2 = st.slider("s2", 0, 1000, 100, key="s2", on_change=update_servo)
s3 = st.slider("s3", 0, 1000, 100, key="s3", on_change=update_servo)
s4 = st.slider("s4", 0, 1000, 100, key="s4", on_change=update_servo)

servo_data = {"s0": int(s0), "s1": int(s1), "s2": int(s2), "s3": int(s3), "s4": int(s4)}
st.code(json.dumps(servo_data), language="json")

if "ser" not in st.session_state:
        st.session_state.ser = serial.Serial(port, int(baud_rate), timeout=2)
