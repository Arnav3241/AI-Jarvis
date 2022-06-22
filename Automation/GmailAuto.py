import imaplib
import email

def mailChecker(server, emailAddress, password, mailBox, Criteria):
    imap = imaplib.IMAP4_SSL(server)
    imap.login(emailAddress, password)
    imap.select(mailBox)
    _, msgNums = imap.search(None, Criteria)
    for msg in msgNums[0].split():
        _, data = imap.fetch(msg, "(RFC822)")       
        message = email.message_from_bytes(data[0][1])
        return f"You have Recieved A New E-Mail From {message.get('From')}"
    
mailChecker("imap.gmail.com", f"arnav.singh.legendary.202@gmail.com", "Arnav@3241", "Inbox", "UNSEEN")