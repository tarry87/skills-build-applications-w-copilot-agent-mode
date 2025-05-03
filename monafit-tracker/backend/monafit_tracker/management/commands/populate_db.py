from django.core.management.base import BaseCommand
from monafit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):
        # Clear existing data using QuerySet.delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users (UUIDs are automatically generated)
        users = [
            User(username='Superman', email='superman@heroes.com', password='password123'),
            User(username='Batman', email='batman@heroes.com', password='password123'),
            User(username='WonderWoman', email='wonderwoman@heroes.com', password='password123'),
        ]
        User.objects.bulk_create(users)

        # Fetch the created users
        superman = User.objects.get(username='Superman')
        batman = User.objects.get(username='Batman')
        wonderwoman = User.objects.get(username='WonderWoman')

        # Create teams and associate members
        justice_league = Team.objects.create(name='Justice League')
        justice_league.members.add(superman, batman, wonderwoman)

        # Create activities with timedelta durations
        activities = [
            Activity(user=superman, activity_type='Flying', duration=timedelta(hours=1)),
            Activity(user=batman, activity_type='Martial Arts', duration=timedelta(hours=2)),
            Activity(user=wonderwoman, activity_type='Lasso Training', duration=timedelta(hours=1, minutes=30)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard
        leaderboard = [
            Leaderboard(user=superman, score=100),
            Leaderboard(user=batman, score=90),
            Leaderboard(user=wonderwoman, score=95),
        ]
        Leaderboard.objects.bulk_create(leaderboard)

        # Create workouts
        workouts = [
            Workout(name='Strength Training', description='Build super strength'),
            Workout(name='Endurance Training', description='Increase stamina'),
            Workout(name='Agility Training', description='Improve reflexes'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
