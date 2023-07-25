
import smtplib
import email
import os

def send_email_with_image(to_email, image_file):

    from_email = 'ceremonie.essec.tunis.2023@gmail.com'  # email address
    password = 'cztkiyyndbfwgmwn'            # email password
    smtp_server = 'smtp.gmail.com'           # SMTP server
    smtp_port = 587                          # SMTP server port

    msg = email.message.EmailMessage()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = 'Invitation à la cérémonie de remise des diplômes'

    body = """L'Ecole Supérieure des Sciences Economiques et Commerciales de Tunis est ravie de vous convier à la cérémonie de remise des diplômes de l'année universitaire 2022/2023 !\n
     Après des années d'efforts, de travail acharné et de dévouement, le moment est enfin venu de célébrer votre réussite et votre passage à une étape suivante de votre vie.\n 
     NB: \n
     1. Chaque étudiant pourra être accompagné par au maximum deux membres de sa famille.\n
     2. Deux vérifications des invitations auront lieu: la première au niveau de l'entrée principale et la deuxième au niveau de l'entrée de la salle.\n
     Cordialement."""
    
    body2 = """L'Ecole Supérieure des Sciences Economiques et Commerciales de Tunis est ravie de vous convier à la cérémonie de remise des diplômes de l'année universitaire 2022/2023 !\n
     Après une année d'efforts, de travail acharné et de dévouement, le moment est enfin venu de célébrer votre excellence.\n 
     NB: \n
     1. Chaque étudiant pourra être accompagné par au maximum deux membres de sa famille.\n
     2. Deux vérifications des invitations auront lieu: la première au niveau de l'entrée principale et la deuxième au niveau de l'entrée de la salle.\n
     Cordialement."""
    msg.set_content(body)

    with open(image_file, 'rb') as f:
        image_data = f.read()
        msg.add_attachment(image_data, maintype='image', subtype='jpeg', filename=os.path.basename(image_file))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
        print(f"Email sent to: {to_email} file name : {image_file}")
    except Exception as e:
        print(f"Error sending email to {to_email}: {str(e)}")

def main():
    email_list_file = 'C:/Users/waelg/OneDrive/Bureau/sending/mails.txt'
    image_folder = 'C:/Users/waelg/OneDrive/Bureau/sending/images'

    with open(email_list_file, 'r') as f:
        emails = f.read().splitlines()

    image_files = [os.path.join(image_folder, file) for file in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, file))]

    if len(emails) != len(image_files):
        print("Number of emails and images do not match.")
        return

    for email, image_file in zip(emails, image_files):
        send_email_with_image(email, image_file)

if __name__ == '__main__':
    main()
