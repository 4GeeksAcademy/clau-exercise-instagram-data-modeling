import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    alias = Column(String(250))
    nombre = Column(String(250))
    apellido = Column(String(250))
    mail = Column(String(250))
    
    comment = relationship('Comment', backref = 'user')
    post = relationship('Post', backref = 'user')
    follower = relationship('Follower', backref = 'user')



class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type = Column(String(250))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))

   

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    media = relationship('Media', backref = 'post')
    comment = relationship('Comment', backref = 'post')
   


                        

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))

    

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))


# class User_Follower(Base):
#     __tablename__ = 'user_follower'
#     id = Column(Integer, primary_key=True)
#     follower_id = Column(Integer, ForeignKey('follower.id'))
#     user_id = Column(Integer, ForeignKey('user.id'))



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e


# CREATE TABLE `follower_user` (
#   `follower_id` INT NOT NULL,
#   `user_id` INT NOT NULL,
#   PRIMARY KEY (`follower_id`, `user_id`),
#   FOREIGN KEY (`follower_id`) REFERENCES `follower` (`id`),
#   FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
# );

# tags = db.Table('tags',
#     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
#     db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True)
# )

# class Page(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     tags = db.relationship('Tag', secondary=tags, lazy='subquery',
#         backref=db.backref('pages', lazy=True))

# class Tag(db.Model):
#     id = db.Column(db.Integer, primary_key=True)


#      media = relationship('media', backref = 'post')
#     comment = relationship('comment', backref = 'post')