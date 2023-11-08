from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class BaseModel(models.Model):
    u_id=models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta :
        abstract=True
class UserDetails(BaseModel):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_userdetails')
    phone_number=models.IntegerField(default=0)
    zip=models.IntegerField(default=0)
    city=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    gender=models.CharField(max_length=100)
    voter_number=models.IntegerField(default=0)
    profile_img=models.ImageField(upload_to='profile_images')
    voter_img=models.ImageField(upload_to='voter_images')
    status=models.CharField(default=False,max_length=100)

class AvailableElection(BaseModel):
    election_name=models.CharField(max_length=250)
    start_time=models.DateField(auto_now_add=True)
    end_time=models.DateField(auto_now_add=False)
class Candidate(BaseModel):
    election_name=models.ForeignKey(AvailableElection,on_delete=models.CASCADE,related_name='candidate_election_name')
    name=models.CharField(max_length=100)
    party_name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    party_img=models.ImageField(upload_to='party_images')
    candidate_img=models.ImageField(upload_to='candi_images',null=True)
    vote_count=models.IntegerField(default=0)
class Vote(BaseModel):
    election_name=models.ForeignKey(AvailableElection,on_delete=models.CASCADE,related_name='election_name_vote')
    candidate_name=models.ForeignKey(Candidate,on_delete=models.CASCADE,related_name='candidate_votes')
    user=models.ManyToManyField(User)
    def total_vote(self):
        return self.user.count()