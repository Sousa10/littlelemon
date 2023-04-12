# littlelemon
Backend developer capstone project

# Endpoints
GET /reservation/menu - See all the menu items
GET, POST, PUT, DELETE /reservation/menu/1 - See, update, create and delete specific menu item
GET /reservation/booking/tables/ - See all the reservations
GET, PUT, DELETE /reservation/booking/tables/1 - See specific table reservation
POST /reservation/booking/tables/ - Create reservation with payload({
	"name": "Rui & Sinira",
	"no_of_guest": 2,
	"booking_date": "2023-04-22 20:44:01"
})

POST /auth/users - register user adding username, email and password in payload
GET /auth/users - see all users with admin token
GET /auth/users/me - see current logged user
POST /auth/token/login - login a user and get token