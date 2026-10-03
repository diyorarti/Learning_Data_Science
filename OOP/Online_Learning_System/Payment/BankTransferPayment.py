from Topics.OOP.Online_Learning_System.Payment.Payments import Payment

class BankTransferPayment(Payment):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def process_payment(self):
        return f"BankTransfer Processed {self.amount} {self.currency} successfully"
    
    def refund_patment(self):
        return f"BankTransfer refunded {self.amount} {self.currency} successfully" 