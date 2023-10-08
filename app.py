from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image




# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="B-Events Webpage", page_icon=":tada:", layout="wide")




def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")



# ---- LOAD ASSETS ----
lottie_video = load_lottieurl("https://lottie.host/479603f7-1b2f-460b-a7c6-e17b586aa3b1/djnGw6jJLQ.json")
img_contact_form = Image.open("images/Ionut si Dana.png")
img_lottie_animation= Image.open("images/Sebastian si Andreea.png")
img_contact1_form = Image.open("images/Sergiu si Alba.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, we are  B-Events :wave:")
    st.title("A videography company from Romania ")
    st.write("We offer professional services for your events")
    st.write("[Follow us  >](https://www.instagram.com/b_events.ro/?hl=en)")


# ---- WHAT DO WE  DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What do we do")
        st.write("##")
        st.write(
            "Our team of skilled videographers is dedicated to weaving narratives that go beyond the surface, "
            "ensuring each frame tells a unique story. From capturing the emotions of a wedding day to showcasing the energy "
            "of corporate events, our passion for visual storytelling is evident in every project we undertake."
            

            "If this sounds interesting to you, consider subscribing and turning on the notifications, "
            "so you don’t miss any content."

        )
        st.write("[YouTube Channel >](https://www.youtube.com/@bevents723)")
    with right_column:
        st_lottie(lottie_video, height=300, key="video")


# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Our Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Ionut & Dana | Wedding Clip | 2023-09-25 ")
        st.write(
            """
            
            Ionut and Dana's Magical Day
            
            Step into the enchanting world of Ionut and Dana as they embark on their journey of love and commitment. 
            Join us in celebrating the union of two souls, surrounded by the beauty of shared dreams and everlasting promises. 
            Witness the romance, joy, and heartfelt moments that make Ionut and Dana's wedding day an unforgettable chapter in their love story.
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=7_BbeOFKcEk)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Sebastian & Andreea | Wedding Clip | 2023-09-10")
        st.write(
            """
            Sebastian and Andreea's Love Story Unveiled
            
            Get ready to be swept off your feet by the love and elegance of Sebastian and Andreea's wedding day. 
            From the tender glances to the joyous laughter, every moment is a testament to their beautiful connection. 
            Join us in this cinematic journey capturing the essence of their love, as Sebastian and Andreea say "I do" and embark on a lifetime of happiness together.
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=a-DeZ_bW-Bw)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact1_form)
    with text_column:
        st.subheader("Sergiu & Alba | Wedding Clip | 2023-08-27")
        st.write(
            """
            Sergiu and Alba's Fairytale Celebration
            
            Step into a fairytale world with Sergiu and Alba as they say their vows in a breathtaking ceremony.
             Immerse yourself in the magic of their love, surrounded by the enchanting backdrop of their wedding day.
             From the first look to the dance floor, witness the romance unfold in this captivating video that encapsulates the beginning of Sergiu and Alba's happily ever after.
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=3URhr7R7S_Y)")


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Us!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/todoran.dorinel@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()