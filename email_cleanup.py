import imaplib
import email
from email.header import decode_header
import datetime
import time

# ==========================================
# USER CONFIGURATION
# ==========================================

# Since your email is @gmail.com, we MUST use Google's servers
IMAP_SERVER = "imap.gmail.com" 
EMAIL_USER = "daddy.davis.601@gmail.com"

# 🔴 STEP 1: PASTE YOUR GOOGLE APP PASSWORD BELOW
# Go to Google Account -> Security -> 2-Step Verification -> App Passwords
EMAIL_PASS = "Myfamilylovesme1$" 

# 🔴 STEP 2: SET TO FALSE WHEN READY TO DELETE
DRY_RUN = True 

# Gmail Trash Folder
TRASH_FOLDER = "[Gmail]/Trash" 

# RULES
BLOCKED_SENDERS = [
    "newsletter@example.com",
    "spam@marketing.com",
    "no-reply@annoying-service.com"
]

BLOCKED_KEYWORDS = [
    "limited time offer",
    "clearance sale",
    "unsubscribe"
]

DAYS_OLD = 30

# ==========================================

def connect_to_mail():
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_USER, EMAIL_PASS)
        return mail
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return None

def get_date_limit(days):
    date_limit = datetime.date.today() - datetime.timedelta(days=days)
    return date_limit.strftime("%d-%b-%Y")

def move_to_trash(mail, email_ids):
    if not email_ids:
        return
    ids_str = b','.join(email_ids)
    
    if DRY_RUN:
        print(f"   ⚠️ [DRY RUN] Would move {len(email_ids)} emails to {TRASH_FOLDER}")
    else:
        mail.copy(ids_str, TRASH_FOLDER)
        mail.store(ids_str, '+FLAGS', '\\Deleted')
        print(f"   ✅ Moved {len(email_ids)} emails to {TRASH_FOLDER}")

def clean_old_emails(mail):
    if DAYS_OLD == 0:
        return
    print(f"\n🔍 Searching for emails older than {DAYS_OLD} days...")
    date_criteria = get_date_limit(DAYS_OLD)
    status, messages = mail.search(None, f'(BEFORE "{date_criteria}")')
    
    if status != "OK" or not messages[0]:
        print("   No emails found matching criteria.")
        return

    email_ids = messages[0].split()
    print(f"   Found {len(email_ids)} emails older than {DAYS_OLD} days.")
    move_to_trash(mail, email_ids)

def clean_spam_keywords(mail):
    print(f"\n🔍 Searching for blocked senders and keywords (Fast Mode)...")
    status, messages = mail.search(None, 'ALL')
    
    if status != "OK" or not messages[0]:
        print("   Inbox is empty or search failed.")
        return

    email_ids = messages[0].split()
    ids_to_trash = []
    
    # Process last 100 emails
    batch = email_ids[-100:] 
    
    for e_id in batch:
        try:
            _, msg_data = mail.fetch(e_id, "(BODY.PEEK[HEADER])")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject_raw = msg["Subject"]
                    subject = "No Subject"
                    if subject_raw:
                        decoded_list = decode_header(subject_raw)
                        subject_fragments = []
                        for text, encoding in decoded_list:
                            if isinstance(text, bytes):
                                fragment = text.decode(encoding if encoding else "utf-8", errors="ignore")
                            else:
                                fragment = text
                            subject_fragments.append(fragment)
                        subject = "".join(subject_fragments)
                    
                    sender = msg.get("From")
                    if not sender: sender = "Unknown"
                    
                    is_spam = False
                    if any(blocked in sender for blocked in BLOCKED_SENDERS):
                        print(f"   Found blocked sender: {sender}")
                        is_spam = True
                        
                    if not is_spam and any(keyword.lower() in subject.lower() for keyword in BLOCKED_KEYWORDS):
                        print(f"   Found keyword match: '{subject}'")
                        is_spam = True
                        
                    if is_spam:
                        ids_to_trash.append(e_id)
        except Exception as e:
            print(f"   Error reading email ID {e_id}: {e}")
            continue

    if ids_to_trash:
        move_to_trash(mail, ids_to_trash)
    else:
        print("   No keyword/sender matches found in the batch.")

def main():
    print("--- 📧 Email Cleanup Script Started ---")
    if DRY_RUN:
        print("--- 🛡️ DRY RUN MODE: NO EMAILS WILL BE DELETED ---")

    mail = connect_to_mail()
    if mail:
        mail.select("INBOX")
        clean_old_emails(mail)
        clean_spam_keywords(mail)
        if not DRY_RUN:
            mail.expunge()
        mail.close()
        mail.logout()
        print("\n--- ✅ Cleanup Finished ---")

if __name__ == "__main__":
    main()