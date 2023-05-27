# from core import db
from datetime import datetime

# class ShortUrls(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     long_url = db.Column(db.String(2000), nullable=False)
#     short_id = db.Column(db.String(20), nullable=True, unique=True)
#     created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

#     def __repr__(self):
#         return f"ShortUrls('{self.long_url}', '{self.short_url}')"