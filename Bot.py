import zmq
import random
import time

class AuctionBot:
    def __init__(self, starting_budget):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.server_address = "tcp://localhost:5555"  #Server address
        self.socket.connect(self.server_address)
        self.budget = starting_budget
        self.current_bid = 0
        self.max_bid_increment = 10  # Max amount to increment bids
        self.safety_threshold = self.budget * 0.8  # Stop aggressive bidding after 80% of budget is used

    def receive_message(self):
        """Receives a message from the auction server."""
        try:
            return self.socket.recv_json()
        except zmq.ZMQError as e:
            print(f"Error receiving message: {e}")
            return None

    def send_message(self, message):
        """Sends a message to the auction server."""
        try:
            self.socket.send_json(message)
        except zmq.ZMQError as e:
            print(f"Error sending message: {e}")

    def bidding_strategy(self, current_price):
        """Implements a basic bidding strategy."""
        if current_price >= self.budget:
            return False  # Stop if price exceeds budget

        # If under safety threshold, bid more aggressively
        if self.current_bid < self.safety_threshold:
            bid_increment = random.randint(1, self.max_bid_increment)
        else:
            bid_increment = 1  # Be cautious when over the threshold

        new_bid = current_price + bid_increment

        if new_bid <= self.budget:
            self.current_bid = new_bid
            return new_bid
        else:
            return False  # Stop bidding if it exceeds budget

    def participate_in_auction(self):
        """Main loop where the bot participates in auctions."""
        while True:
            print("Waiting for auction updates...")
            message = self.receive_message()

            if message and 'current_price' in message:
                current_price = message['current_price']
                print(f"Current price: {current_price}")

                new_bid = self.bidding_strategy(current_price)

                if new_bid:
                    print(f"Placing bid: {new_bid}")
                    self.send_message({'bid': new_bid})
                else:
                    print(f"Out of budget or no further bidding allowed. Current price: {current_price}")

            # Pause before next bid to simulate realistic timing
            time.sleep(random.uniform(1, 3))

# # Example usage:
# if __name__ == "__main__":
#     bot = AuctionBot(starting_budget=1000)  # Start bot with a budget of 1000 units
#     bot.participate_in_auction()
