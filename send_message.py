import smtplib
import configparser

configurations = configparser.ConfigParser()
configurations.read('config_file')

username = configurations['Credentials']['username']
password = configurations['Credentials']['password']
fromAddress = configurations['Credentials']['from_address']

def send_text_message(toAddress, message):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromAddress, toAddress, message)
    server.quit()
