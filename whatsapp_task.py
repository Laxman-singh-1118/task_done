import streamlit as st
import webbrowser
import time

st.title("Bulk WhatsApp Message Sender")

numbers = st.text_area("Enter phone numbers (with country code, one per line or comma separated):")
message = st.text_area("Enter your message:")

if st.button("Send Message(s)"):
    # Split numbers by comma or newline
    raw_numbers = numbers.replace(",", "\n").split("\n")
    phone_numbers = [num.strip() for num in raw_numbers if num.strip()]
    
    if not phone_numbers:
        st.warning("Please enter at least one phone number.")
    elif not message.strip():
        st.warning("Please enter a message.")
    else:
        st.success(f"Opening WhatsApp Web for {len(phone_numbers)} number(s)...")
        for phone in phone_numbers:
            url = f"https://web.whatsapp.com/send?phone={phone}&text={message}"
            webbrowser.open_new_tab(url)
            time.sleep(1)  # Small delay to avoid browser overload
        st.info("Please check your browser tabs and press Enter to send each message.") 