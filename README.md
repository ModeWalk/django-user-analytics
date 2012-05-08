django-user-analytics
=====================

A simple way to track (client or server) user-level events asynchronously

Features:

- A simple middleware that manages cookies
- Supports tracking the same user from various devices:
  If user logs in from say a phone and laptop, all the traffic from both devices will be associated with the same user account.
- Ties into django's built in user authentication
- Provides simple javascript library to record client-side events
- All events are recorded asynchronously through Celery (thus impact to performance will be negligible)
- Basic admin page that shows user flow