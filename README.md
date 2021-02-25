# LoanCalculator
The repo implements a simple loan calculation and provide quotes based on the loan amount, number of payments and monthly repayment amount.
The interest rate is pre-configured and is a constant in Loan class.

## Installation

### Install Docker
Please click [here](https://docs.docker.com/get-docker/) to install [docker](https://docs.docker.com/get-docker/)

### Run following command after installing docker
``docker-compose up
``

### Go to the following url on your browser
http://0.0.0.0:8000/loan/

### API Endpoint
http://0.0.0.0:8000/loan/get-quote/

### Extra:
If developer wants to use external APIs for calculation he can do so easily as teamplate is separate from API and makes a AJAX post request to the loan calculation API.
The solution seems efficient.  Frontend and backend can easily be decoupled and frontend can be hosted sseparetly as it hits the REST API to get the loan quotes.

