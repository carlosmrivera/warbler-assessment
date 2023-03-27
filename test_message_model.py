"""Message model tests."""


import os
from unittest import TestCase

from models import db, User, Message, Follows

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"
from app import app

app.app_context().push()
db.create_all()

class MessageModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

        self.client = app.test_client()

    def test_message_model(self):
        """Does basic model work?"""

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        m = Message(
            text="test message",
            user_id=u.id
        )

        db.session.add(m)
        db.session.commit()

        # User should have 1 message
        self.assertEqual(len(u.messages), 1)
        self.assertEqual(u.messages[0].text, "test message")

    def test_message_likes(self):
        """Does it detect when a message is liked?"""

        u1 = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        u2 = User(
            email="test2@test.com",
            username="testuser2",
            password="HASHED_PASSWORD"
        )

        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        m = Message(
            text="test message",
            user_id=u1.id
        )

        db.session.add(m)
        db.session.commit()

        # User should have 1 message
        self.assertEqual(len(u1.messages), 1)
        self.assertEqual(u1.messages[0].text, "test message")

        # User should have no likes
        self.assertEqual(len(u1.likes), 0)
        self.assertEqual(len(u2.likes), 0)

        # User 2 likes message
        u2.likes.append(m)
        db.session.commit()

        # User 1 should have no likes
        self.assertEqual(len(u1.likes), 0)

        # User 2 should have 1 like
        self.assertEqual(len(u2.likes), 1)
