 Auction Bot Project

Overview

This project is an Auction Bot designed to compete in real-time auctions by interacting with a server. The bot is implemented using Python and **ZeroMQ (ZMQ)** for client-server communication. It automatically places bids based on a bidding strategy and adjusts its behavior based on real-time auction updates.

Features

- Real-Time Auction Participation: Connects to an auction server and receives live updates about the current auction status.
- Automated Bidding Strategy: The bot places strategic bids to maximize its chances of winning, while ensuring that it stays within a defined budget.
- Socket Communication: Uses ZeroMQ to handle communication between the bot and the auction server.
- Randomized Bid Timing: Simulates realistic bidding behavior with varying time delays between bids.

Installation

To get started with the auction bot, you need to have Python and ZeroMQ installed on your machine.

1. **Clone the repository**:
  
    git clone https://github.com/YourUsername/auction-bot.git


2. Install the required dependencies:
    You can install ZeroMQ by running the following:
  
    pip install pyzmq


Usage

1. Update the server address:
    In the `Bot.py` file, update the server address in the `self.server_address` variable to match the address of the auction server you are using.
  
    self.server_address = "tcp://localhost:5555"  # Update with the correct server address


2. Run the bot:
    You can start the bot by running:

    python auction_bot.py
 

3. Bidding Strategy:
    - The bot places bids automatically, incrementing the current bid by a random amount (up to a defined maximum).
    - It will stop bidding if it exceeds its budget or based on its safety threshold (80% of the budget).

Bidding Strategy Details

The bot follows this strategy:
- Aggressively bids when the price is below 80% of the budget.
- Uses smaller increments when the price approaches 80% of the budget to avoid overspending.
- Stops bidding once the current price exceeds the remaining budget.

Future Improvements

- More sophisticated bidding strategies based on competitor behavior.
- Support for different auction formats.
- Enhanced logging for better analysis of bidding outcomes.

