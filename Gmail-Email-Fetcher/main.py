# Importing libraries
import imaplib
import email

# Gmail credentials
user = 'USER_EMAIL_ADDRESS'
password = 'USER_PASSWORD'
imap_url = 'imap.gmail.com'

# Function to get email body
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)

# Function to search emails
def search(key, value, con):
    result, data = con.search(None, key, '"{}"'.format(value))
    return data

# Function to fetch emails
def get_emails(result_bytes):
    msgs = []
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
    return msgs

# Establish SSL connection
con = imaplib.IMAP4_SSL(imap_url)

# Login to Gmail
con.login(user, password)

# Select Inbox
con.select('Inbox')

# Fetch emails from a particular sender
msgs = get_emails(search('FROM', 'MY_ANOTHER_GMAIL_ADDRESS', con))

# Process and print email content
for msg in msgs[::-1]:
    for sent in msg:
        if type(sent) is tuple:
            content = str(sent[1], 'utf-8')
            try:
                indexstart = content.find("ltr")
                data2 = content[indexstart + 5:]
                indexend = data2.find("</div>")
                print(data2[0:indexend])
            except UnicodeEncodeError:
                pass
