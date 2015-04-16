from django.db import models

# Create your models here.

class LoginInfo(models.Model):
    survey_id = models.CharField(max_length=15)
    user_password = models.CharField(max_length=15)
    member_password = models.CharField(max_length=15)
    leader_password = models.CharField(max_length=15)

    def __str__(self):
    	return "%s: %s, %s, %s"%(self.survey_id, self.user_password, self.member_password, self.leader_password) 

class MemberResponse(models.Model):
    which_login = models.ForeignKey(LoginInfo)
    name = models.CharField(max_length=100, default = 'null')
    numMatches = models.IntegerField(default=0)
    prefs = models.CharField(max_length=300, default = 'null')
    conflicts = models.CharField(max_length=300, default = 'null')

    def __str__(self):
    	return "%s, %s: %d\t%s"%(str(self.which_login), self.name, self.numMatches, self.prefs)

class LeaderResponse(models.Model):
    which_login = models.ForeignKey(LoginInfo)
    name = models.CharField(max_length=100, default = 'null')
    numMatches = models.IntegerField(default=0)
    prefs = models.CharField(max_length=300, default = 'null')

    def __str__(self):
    	return "%s, %s: %d\t%s"%(str(self.which_login), self.name, self.numMatches, self.prefs)