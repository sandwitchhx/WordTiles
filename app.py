import streamlit as st
import random

st.set_page_config(page_title="Word Unscramble Game", layout="centered")
st.title("📝 Word Unscramble Game")
st.markdown("Try to unscramble the word! 🍎🍌🍇🍊")

# Word list
words = ["apple", "banana", "grape", "orange", "strawberry", "cherry", "pineapple", "kiwi"]

# Maximum number of tries per word
MAX_TRIES = 3

# Initialize session state
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'tries' not in st.session_state:
    st.session_state.tries = 0
if 'current_word' not in st.session_state:
    st.session_state.current_word = random.choice(words)
if 'scrambled' not in st.session_state:
    word = st.session_state.current_word
    st.session_state.scrambled = ''.join(random.sample(word, len(word)))

# Display scrambled word
st.subheader("🔀 Unscramble this word:")
st.markdown(f"### {st.session_state.scrambled}")

# User input
user_guess = st.text_input("Your guess:")

if st.button("Submit"):
    st.session_state.tries += 1
    if user_guess.lower() == st.session_state.current_word:
        st.session_state.score += 1
        st.success(f"🎉 Correct! Your score: {st.session_state.score}")
        # Reset for next word
        st.session_state.current_word = random.choice(words)
        st.session_state.scrambled = ''.join(random.sample(st.session_state.current_word, len(st.session_state.current_word)))
        st.session_state.tries = 0
        st.experimental_rerun()
    else:
        remaining = MAX_TRIES - st.session_state.tries
        if remaining > 0:
            st.warning(f"❌ Wrong! Try again. Remaining attempts: {remaining}")
        else:
            st.error(f"💥 Out of tries! The word was: **{st.session_state.current_word}**")
            # Reset for next word
            st.session_state.current_word = random.choice(words)
            st.session_state.scrambled = ''.join(random.sample(st.session_state.current_word, len(st.session_state.current_word)))
            st.session_state.tries = 0
            st.experimental_rerun()

# Display current score
st.markdown(f"**Score:** {st.session_state.score}")

# Restart button
if st.button("🔄 Restart Game"):
    st.session_state.score = 0
    st.session_state.tries = 0
    st.session_state.current_word = random.choice(words)
    st.session_state.scrambled = ''.join(random.sample(st.session_state.current_word, len(st.session_state.current_word)))
    st.experimental_rerun()
