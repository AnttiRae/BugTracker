from django.test import TestCase
from app.models import Bug, Comment
from django.contrib.auth.models import User

# Create your tests here.

class UserProfileTest(TestCase):
    def setUp(self):
        user = User.objects.create_user('antti', 'antti@antti.fi', 'password')
        user.save()
        Bug.objects.create(title='moi', priority='High', description='moirjens', reported_by=user)

    def testWritingUserProfile(self):
        userProfile = User.objects.get(username='antti')
        print(userProfile)
        userProfile.bio = 'morjesta asdadad'
        userProfile.save()
        print(userProfile.bio)