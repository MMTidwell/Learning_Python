# sending text to phones

# install Twilio if you have not already
#   https://classroom.udacity.com/courses/ud000/lessons/4156168752/concepts/47501238040

from twilio.rest import TwilioRestClient

account_sid = 'AC4c495c84bb3955bb2e0d08fa61e7229c'
auth_token = '0ec91bfa3cd93d907142aa0f0e4a9009'
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to='+18173016167', from_='+16829902841',
                                 body="Hi love bug!! Im sending this text via python code on twilio. neat!!")