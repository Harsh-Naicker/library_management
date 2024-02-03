# Library Management System

Implementation Plan

Models
1. Books

ID, Title, Author (Fk -> Authors), Created At

2. Book copies

ID, Fk -> Book , Created At
(A book can have multiple copies)

3. Authors

ID , AuthorName, Created At

4. Members

ID, Name, Created At

5. Reservations

ID, Book ID, Member ID, Created At, Requested At

6. Reservation Live State

ID, Reservation ID, Status, Created At, Updated At
Status can be Queued, Fulfilled

7. Reservation State History

ID, Live Status ID, Status, Created At, Updated At


To handle reservations -> Make processing Asynchronous using Kafka
Create a pubsub model


8. Checkout

ID, Book Copy ID, Created at, End Date

9. Book Checkout Status

ID, Book Copy ID, Checkout Status

Statuses: Checked Out, Available/Returned

10. Book Checkout Status History

ID, Checkout Status ID, Member ID Fk -> Member, Status
Status: Checked Out, Available / returned


Only a reservation is possible if all copies of a book have been checked out

Endpoints

`checkout/`
- Member ID
- Book ID
- End Date

Test Cases
1. A book copy is available -> Checkout that Book (Synchronous process)
2. No book copy is available -> Handle with appropriate response (Synchronous process)

`reserve/`
- Member ID
- Book ID
Works in FIFO Manner

return
- Book Copy ID

`return/`
- member_id
- book_copy_id

return
- status successful
- overdue fine

`fines/`
- member_id

Use BookAvailabilityStatus to find all books which are in checked out state. Then find their latest Checkout entry mapped to the member to fetch the end date and evaluate the fine if applicable




Add CDC Listener on Checkout Status History / Explicity push kafka events
As soon as a book is returned, listen for change in Checkout Status History.
If Status is returned, check in Reservations if any outstanding reservation exists for that book. If yes, do a system generated checkout (Asynchronous process using Kafka)
