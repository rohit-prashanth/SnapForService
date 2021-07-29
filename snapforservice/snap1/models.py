from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileTable(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    SnapForService_Services = [('Snap for Beauty','Salon and makeup services for men and women at home'),
                               ('Snap for Spa','Massage therapy for men and women at home'),
                               ('Snap for Grooming','Haircut and grooming services for men and kids at home'),
                               ('Snap for Repairs','Electricians, plumbers, carpenters, AC and appliance repair'),
                               ('Snap for Cleaning','Regular and deep home cleaning solutions'),
                               ('Snap for Painting','Professional home painting services'),
                               ('Snap for Event Management','Professional weddings & party management services'),
                               ('Snap for fitness','Proffessional fitness and yoga services at home')]
    service = models.CharField(max_length=50, choices=SnapForService_Services, default='Snap for Beauty')
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

