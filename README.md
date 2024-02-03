# Library Management System

# ERD Diagram
<img src="https://github.com/Harsh-Naicker/library_management/blob/master/erd.png">
Note: `checkout/` in Checkout model is not supposed to be nullable. I forgot to add it earlier so django needed me to add a default or make it nullable

Postman collection has been provided to test the three completed endpoints which are 'reserve/', 'checkout/' and 'return/'

As explained in the video, the original plan was to create an event based system using Kafka.
Was going to create a pubsub model to push and consume events whenever a book is returned to automatically look for queued reservations and do a checkout from the system

The design of the models supports all the required analytics computation.
