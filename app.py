import streamlit as st
import random

st.set_page_config(page_title="Memory Card Game", layout="centered")
st.title("🃏 Memory Card Game")

# Initialize session state
if 'cards' not in st.session_state:
    emojis = ["🍎","🍌","🍇","🍉","🍓","🍒","🥝","🍍"]
    st.session_state.cards = emojis*2
    random.shuffle(st.session_state.cards)
    st.session_state.flipped = [False]*16
    st.session_state.first_card = None
    st.session_state.matches = 0

def flip_card(index):
    if st.session_state.flipped[index]:
        return
    st.session_state.flipped[index] = True

    if st.session_state.first_card is None:
        st.session_state.first_card = index
    else:
        # Check match
        if st.session_state.cards[st.session_state.first_card] != st.session_state.cards[index]:
            # No match: flip back after next rerun
            st.session_state.flipped[st.session_state.first_card] = False
            st.session_state.flipped[index] = False
        else:
            st.session_state.matches += 1
        st.session_state.first_card = None

# Display cards as buttons
cols = st.columns(4)
for i in range(16):
    with cols[i%4]:
        if st.button(st.session_state.cards[i] if st.session_state.flipped[i] else "❓", key=i):
            flip_card(i)

# Win message
if st.session_state.matches == 8:
    st.success("🎉 You matched all pairs!")
