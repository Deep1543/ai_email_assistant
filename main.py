import streamlit as st
from email_reader import read_unread_emails
from summarizer import summarize_text
from responder import suggest_reply
from dotenv import load_dotenv
import os


load_dotenv()

st.set_page_config(page_title="Email Assistant", page_icon=":email:", layout="wide")
st.title("Email Assistant")

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

if st.button("fetch and summarize under emails"):
    with st.spinner("Fetching unread emails..."):
        emails = read_unread_emails(EMAIL_USER, EMAIL_PASS)
        
        if not emails:
            st.error("No unread emails found.")

        else:
            for i, email_data in enumerate(emails):
                with st.expander(f"Email #{i+1}: {email_data['subject']}"):
                    st.markdown(f"**From:** {email_data['from']}")
                st.markdown("**Body:**")
                st.code(email_data["body"][:1000] + "...", language='markdown')

                if st.button(f"🧠 Summarize Email #{i+1}", key=f"sum_{i}"):
                    summary = summarize_text(email_data["body"])
                    st.success("Summary:")
                    st.write(summary)

                if st.button(f"✉️ Suggest Reply to Email #{i+1}", key=f"rep_{i}"):
                    reply = suggest_reply(email_data["body"])
                    st.info("Suggested Reply:")
                    st.write(reply)
                
            
           
