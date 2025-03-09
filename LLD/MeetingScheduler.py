import threading
import time
from datetime import datetime, timedelta

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class Meeting:
    def __init__(self, meeting_id, title, start_time, end_time, participants):
        self.meeting_id = meeting_id
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.participants = participants

class MeetingScheduler:
    def __init__(self):
        self.meetings = {}
        self.lock = threading.Lock()

    def schedule_meeting(self, meeting_id, title, start_time, end_time, participants):
        with self.lock:
            if meeting_id in self.meetings:
                print(f"Meeting ID {meeting_id} already exists.")
                return False
            meeting = Meeting(meeting_id, title, start_time, end_time, participants)
            self.meetings[meeting_id] = meeting
            print(f"Meeting '{title}' scheduled successfully.")
            return True

    def update_meeting(self, meeting_id, title=None, start_time=None, end_time=None, participants=None):
        with self.lock:
            if meeting_id not in self.meetings:
                print(f"Meeting ID {meeting_id} not found.")
                return False
            meeting = self.meetings[meeting_id]
            if title:
                meeting.title = title
            if start_time:
                meeting.start_time = start_time
            if end_time:
                meeting.end_time = end_time
            if participants:
                meeting.participants = participants
            print(f"Meeting ID {meeting_id} updated successfully.")
            return True

    def cancel_meeting(self, meeting_id):
        with self.lock:
            if meeting_id in self.meetings:
                del self.meetings[meeting_id]
                print(f"Meeting ID {meeting_id} canceled.")
                return True
            print(f"Meeting ID {meeting_id} not found.")
            return False

    def list_meetings(self):
        with self.lock:
            return list(self.meetings.values())

class NotificationSystem:
    def __init__(self, scheduler):
        self.scheduler = scheduler

    def send_notification(self, meeting):
        for user in meeting.participants:
            print(f"Notification: Reminder for meeting '{meeting.title}' to user {user.name}")

    def start_notification_service(self):
        def notification_worker():
            while True:
                current_time = datetime.now()
                with self.scheduler.lock:
                    for meeting in self.scheduler.list_meetings():
                        if meeting.start_time - timedelta(minutes=10) <= current_time <= meeting.start_time:
                            self.send_notification(meeting)
                time.sleep(60)

        threading.Thread(target=notification_worker, daemon=True).start()

# Example Usage
if __name__ == "__main__":
    scheduler = MeetingScheduler()
    notification_system = NotificationSystem(scheduler)
    notification_system.start_notification_service()

    user1 = User(1, "Alice")
    user2 = User(2, "Bob")

    start_time = datetime.now() + timedelta(minutes=15)
    end_time = start_time + timedelta(hours=1)

    scheduler.schedule_meeting(101, "Project Sync", start_time, end_time, [user1, user2])

    time.sleep(30)
