import streamlit as st
from datetime import datetime
from twilio.rest import Client

# Set up Twilio credentials
account_sid = 'your_account_sid'  # Replace with your Twilio account SID
auth_token = 'your_auth_token'  # Replace with your Twilio auth token
client = Client(account_sid, auth_token)

# Define the booking form
st.title('Welcome to Namma Yatri!')
st.subheader('Auto Booking')
name = st.text_input('Enter your name')
phone = st.text_input('Enter your phone number')
destination = st.text_input('Enter your destination')
date = st.date_input('Select the date')

# Define the submit button action
if st.button('Book Now'):
    # Create a booking record in the database
    booking_reference_number = 'NY' + str(len(name) + len(phone) + len(destination) + len(str(date)))
    booking_confirmation_message = f'Thank you for booking with Namma Yatri! Your booking reference number is {booking_reference_number}. Your booking to {destination} on {date.strftime("%d/%m/%Y")} is confirmed.'

    # Send a WhatsApp message to the user with the booking confirmation
    message = client.messages.create(
        from_='whatsapp:+14155238886',  # Replace with your Twilio phone number
        body=booking_confirmation_message,
        to=f'whatsapp:{phone}'
    )

    # Send a WhatsApp message to the Namma Yatri admin with the booking details
    admin_phone_number = 'whatsapp:+1234567890'  # Replace with the admin's phone number
    booking_details_message = f'New booking received:\nName: {name}\nPhone: {phone}\nDestination: {destination}\nDate: {date.strftime("%d/%m/%Y")}\nBooking Reference Number: {booking_reference_number}'
    message = client.messages.create(
        from_='whatsapp:+14155238886',  # Replace with your Twilio phone number
        body=booking_details_message,
        to=admin_phone_number
    )

    # Show a success message to the user
    st.success(f'Your booking to {destination} on {date.strftime("%d/%m/%Y")} is confirmed. Your booking reference number is {booking_reference_number}.')

# Add some additional information to the web page
st.markdown('---')
st.subheader('About Namma Yatri')
st.write('Namma Yatri is a Bangalore-based transportation company that provides high-quality auto rickshaw services to customers. Our aim is to make transportation in Bangalore safe, convenient, and affordable.')
st.write('Please note that our auto rickshaws are equipped with GPS tracking and we take passenger safety very seriously. All of our drivers are trained professionals who undergo regular background checks and are provided with personal protective equipment.')
