import random

class Walker:
    def __init__(self, data):
        values = [item[0] for item in data]
        probs = [item[1] for item in data]
        size = len(values)
        segment = 1 / size
        
        donors = [data[i] for i in range(size) if probs[i] < segment]
        recipients = [data[i] for i in range(size) if probs[i] > segment]
        good = [data[i] for i in range(size) if probs[i] == segment]
        
        summa = sum(i[1] for i in data)
        if summa != 1:
            raise ValueError('сумма вер-тей != 1')
        
        self.size = size
        self.events = [None] * size
        self.cond_probs = [0.0] * size
        
        for event, prob in good:
            for i in range(size):
                if self.events[i] is None:
                    self.events[i] = event
                    self.cond_probs[i] = prob * size
                    break
        
        while donors and recipients:
            donor_event, donor_prob = donors.pop(0)
            recip_event, recip_prob = recipients.pop(0)
            
            for i in range(size):
                if self.events[i] is None:
                    self.events[i] = donor_event
                    self.cond_probs[i] = donor_prob * size
                    break
            
            remaining = recip_prob - (segment - donor_prob)
            if remaining > segment:
                recipients.append((recip_event, remaining))
            elif remaining < segment:
                donors.append((recip_event, remaining))
            else:
                good.append((recip_event, remaining))
        
        for event, prob in donors:
            for i in range(size):
                if self.events[i] is None:
                    self.events[i] = event
                    self.cond_probs[i] = prob * size
                    break
        
        for event, prob in recipients:
            for i in range(size):
                if self.events[i] is None:
                    self.events[i] = event
                    self.cond_probs[i] = prob * size
                    break
    
    def get_random(self):
        index = random.randint(0, self.size - 1)
        if random.random() < self.cond_probs[index]:
            return self.events[index]
        else:
            idx = (index + 1) % self.size
            return self.events[idx]