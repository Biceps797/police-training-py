class TrainingSession:
    def _init_(self, training_id, title, date, duration, instructor):
        self.training_id = training_id
        self.title = title
        self.date = date
        self.duration = duration
        self.instructor = instructor
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def _repr_(self):
        return (f"TrainingSession(id={self.training_id}, title={self.title}, "
                f"date={self.date}, duration={self.duration}, "
                f"instructor={self.instructor}, completed={self.completed})")
class TrainingScheduler:
    def _init_(self):
        self.sessions = {}
    
    def schedule_training(self, training_id, title, date):
        if training_id in self.sessions:
            raise ValueError("Training ID already exists.")
        session = TrainingSession(training_id, title, date)
        self.sessions[training_id] = session
        return session
    
    def get_training(self, training_id):
        return self.sessions.get(training_id, None)
    
    def update_training(self, training_id, title=None, date=None):
        session = self.get_training(training_id)
        if not session:
            raise ValueError("Training session not found.")
        if title:
            session.title = title
        if date:
            session.date = date
        return session
    
    def delete_training(self, training_id):
        if training_id in self.sessions:
            del self.sessions[training_id]
        else:
            raise ValueError("Training session not found.")
    
    def track_training_completion(self, training_id):
        session = self.get_training(training_id)
        if not session:
            raise ValueError("Training session not found.")
        session.mark_completed()
        return session
    
    def _repr_(self):
        return f"TrainingScheduler(sessions={self.sessions})"
import unittest

class TestTrainingScheduler(unittest.TestCase):
    def setUp(self):
        self.scheduler = TrainingScheduler()
        self.session1 = TrainingSession(1, "First Aid Training", "2024-01-15", "2 hours", "John Doe")
        self.scheduler.schedule_training(self.session1)

    def test_schedule_training(self):
        self.assertEqual(len(self.scheduler.sessions), 1)
        self.assertIn(1, self.scheduler.sessions)

    def test_update_training(self):
        self.scheduler.update_training(1, title="Advanced First Aid")
        self.assertEqual(self.scheduler.get_training(1).title, "Advanced First Aid")

    def test_delete_training(self):
        self.scheduler.delete_training(1)
        self.assertEqual(len(self.scheduler.sessions), 0)

    def test_track_completion(self):
        session = self.scheduler.track_completion(1)
        self.assertTrue(session.completed)

    def test_schedule_existing_training(self):
        with self.assertRaises(ValueError):
            self.scheduler.schedule_training(self.session1)

if __name__ == "_main_":
    unittest.main()
