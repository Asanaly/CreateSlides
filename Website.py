import streamlit as st
import random
import string
import time
from PIL import Image
from main import ListeningLoop

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

#Website part

st.set_page_config(page_title = "AutoSlideGenerator", page_icon = ":tada", layout = "wide")


while True: #Constant update loop

    #Run a function with a specific name Random
    assigned_name = get_random_string(5)

    print(assigned_name)

    ListeningLoop(assigned_name)

    st.title("It is working!")

    for i in ["jpg", "png"]:
        try:
            with Image.open(fr"D:\Scripts\ToastmastersProject\Images\{assigned_name}.{i}") as img:
                st.image(img, caption='Shit!')
        except:
            print(fr"Not succsesful with {i}")


    time.sleep(15)