import streamlit as st

# Function to count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

# Streamlit App Title
st.title("📄🔍 Text Analyzer")

# User Input: Paragraph
paragraph = st.text_area("✍️ Enter your paragraph:", "")

if paragraph:  # Ensuring input is not empty
    # Text Analysis
    words = paragraph.split()
    total_words = len(words)
    total_characters = len(paragraph)
    total_vowels = count_vowels(paragraph)

    # Check if "Python" exists
    contains_python = "Python" in paragraph

    # Display Results
    st.markdown(f"📌 **Total Words:** {total_words} 📝")
    st.markdown(f"📌 **Total Characters:** {total_characters} 🔢")
    st.markdown(f"📌 **Number of Vowels:** {total_vowels} 🔤")

    if contains_python:
        st.success("✅ 🎉 The paragraph contains the word 'Python' 🐍.")
    else:
        st.warning("❌ ⚠ The paragraph does NOT contain the word 'Python'.")

    # Search & Replace
    search_word = st.text_input("🔎 Enter a word to search:")
    replace_word = st.text_input("✏️ Enter a word to replace it with:")

    if search_word and replace_word:
        modified_paragraph = paragraph.replace(search_word, replace_word)
        st.markdown("📝 **Modified Paragraph:**")
        st.write(modified_paragraph)

    # Uppercase & Lowercase
    st.markdown("🔠 **Uppercase Paragraph:**")
    st.write(paragraph.upper())

    st.markdown("🔡 **Lowercase Paragraph:**")
    st.write(paragraph.lower())

    # Average Word Length Calculation
    avg_word_length = round(total_characters / total_words, 2) if total_words else 0
    st.markdown(f"📏 **Average Word Length:** {avg_word_length} ✨")

else:
    st.warning("⚠️ Please enter a paragraph to analyze. ✍️")
