from Topics.OOP.Online_Learning_System.Payment.Payments import Payment


class CardPayment(Payment):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def process_payment(self):
        return f"Card processed {self.amount} {self.currency} successfully"
    
    def refund_patment(self):
        return f"Card refounded {self.amount} {self.currency} successfully"


