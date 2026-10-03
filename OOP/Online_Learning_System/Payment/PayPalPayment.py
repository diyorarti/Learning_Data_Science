from Topics.OOP.Online_Learning_System.Payment.Payments import Payment

class PayPalPayment(Payment):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def process_payment(self):
        return f"PayPal Processed {self.amount} {self.currency} successfully"
    
    def refund_patment(self):
        return f"PayPal refunded {self.amount} {self.currency} successfully" 