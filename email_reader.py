import imaplib
import email
from email.header import decode_header

def read_unread_emails(username, password):
    imap_url = 'imap.gmail.com'
    emails = []

    try:
        con = imaplib.IMAP4_SSL(imap_url)
        con.login(username, password)
        con.select('inbox')

        result, data = con.search(None, 'UNSEEN')
        mail_ids = data[0].split()

        for i in mail_ids[-5:]:  # Fetch last 5 unread
            result, message = con.fetch(i, '(RFC822)')
            raw_email = message[0][1]
            msg = email.message_from_bytes(raw_email)

            subject = decode_header(msg['subject'])[0][0]
            if isinstance(subject, bytes):
                subject = subject.decode()
            from_ = msg.get("From")

            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body += part.get_payload(decode=True).decode()
            else:
                body = msg.get_payload(decode=True).decode()

            emails.append({
                "subject": subject,
                "from": from_,
                "body": body
            })

        con.logout()
    except Exception as e:
        print("Error:", e)
    return emails
