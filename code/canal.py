class canal:
    def __init__(self, p_error, p_loss, max_delay=0):
        self.p_error = p_error
        self.p_loss = p_loss
        self.max_delay = max_delay

    #simuler la transmission d'une trame à travers le canal
    #def transmit(self, frame):
    #    pass  # à implémenter