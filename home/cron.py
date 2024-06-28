from .models import Renter, Transaction, Properties
import datetime

def my_cron_job():
    renterData = Renter.objects.only('id','name','property')
    for i in renterData:
        tra = Transaction()
        tra.renter = i.name
        tra.dues = int(Properties.objects.get(property = i.property).only('rent'))
        tra.balance -= tra.dues
        tra.date = datetime.date.today()
        tra.save()