from django.db import models



class Register(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    conf_password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.email
    


class BookSlot(models.Model):
    user = models.ForeignKey('Register', on_delete=models.CASCADE, related_name='bookings')
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    slottype = models.CharField(max_length=100)
    trainee = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    TRAINEE_MAPPING = {
        "Yoga": ["Anjali Sharma", "Vikram Singh", "Meena Roy"],
        "Zumba": ["Rohit Mehra", "Kajal Desai", "Ajay Nair"],
        "Strength": ["Priya Kapoor", "Manoj Rana", "Divya Arora"],
        "Cardio": ["Arjun Verma", "Sunita Sharma", "Nikhil Sood"],
        "Hiit": ["Sneha Rao", "Amit Das", "Tina Bansal"],
        "Pilates": ["Rahul Das", "Nidhi Gupta", "Karan Joshi"]
    }
    
    def get_random_trainee(self):
        if self.slottype in self.TRAINEE_MAPPING:
            trainees = self.TRAINEE_MAPPING[self.slottype]
            return trainees[0]
        return None
    
    
    


   
        
