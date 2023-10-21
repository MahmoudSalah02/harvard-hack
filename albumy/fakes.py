# -*- coding: utf-8 -*-

import os
import random
import shutil


from PIL import Image
from faker import Faker
from flask import current_app
from sqlalchemy.exc import IntegrityError

from albumy.extensions import db
from albumy.models import User, Photo, Tag, Comment, Notification

fake = Faker()


def fake_admin():
    admin = User(name='Grey Li',
                 username='greyli',
                 email='admin@helloflask.com',
                 bio=fake.sentence(),
                 website='http://greyli.com',
                 is_farmer = True)
    admin.set_password('helloflask')
    notification = Notification(message='Hello, welcome to Misfit Munch.', receiver=admin)
    db.session.add(notification)
    db.session.add(admin)
    db.session.commit()


def fake_user(count=3):
    user_pics_path = 'albumy/farmerspicture'
    upload_path = current_app.config['ALBUMY_UPLOAD_PATH']
    profile_pics = ['1.jpg', '2.jpeg', '3.jpeg']
    
    for i in range(count):
        user = User(
            name=fake.name(),
            username=fake.user_name(),
            bio=fake.sentence(),
            location=fake.city(),
            website=fake.url(),
            member_since=fake.date_this_decade(),
            email=fake.email(),
            is_farmer=True
        )
        user.set_password('123456')
        
        # Profile picture filename
        profile_pic_filename = profile_pics[i % len(profile_pics)]
        
        # Copy the profile picture file to the upload directory
        shutil.copy(
            os.path.join(user_pics_path, profile_pic_filename), 
            os.path.join(upload_path, profile_pic_filename)
        )
        
        # Set the user's profile picture
        user.profile_picture = profile_pic_filename
        
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()

def fake_follow(count=30):
    for i in range(count):
        user = User.query.get(random.randint(1, User.query.count()))
        user.follow(User.query.get(random.randint(1, User.query.count())))
    db.session.commit()


# def fake_tag(count=20):
#     for i in range(count):
#         tag = Tag(name=fake.word())
#         db.session.add(tag)
#         try:
#             db.session.commit()
#         except IntegrityError:
#             db.session.rollback()


def fake_photo(count=3):
    # photos
    upload_path = current_app.config['ALBUMY_UPLOAD_PATH']
    image_files = ['cucumber.jpeg', 'lettuce.jpeg', 'tomato.jpeg']
    image_descriptions = ['slight bent cucumbers', 'small cucumbers', 'Ripe tomato']
    locations = ['Waltham, MA', 'Mansfield, MA', 'Springfield, MA']
    quantities = [10, 20, 30]
    produce_names = ['cucumber','Lettuce','Tomato']
    prices = [1.0, 2.0, 3.0]
    for i in range(count):
        print(i)

        
        index = i % len(image_files)
        filename = image_files[index]
        description = image_descriptions[index]
        location = locations[index]
        quantity = quantities[index]
        produce_name = produce_names[index]
        price = prices[index]

        # Copy the image file to the upload directory
        shutil.copy(os.path.join('albumy/produceimages', filename), os.path.join(upload_path, filename))


        photo = Photo(
            description=description,
            filename=filename,
            filename_m=filename,
            filename_s=filename,
            author=User.query.get(random.randint(1, User.query.count())),
            timestamp=fake.date_time_this_year(),
            location=location,
            quantity=quantity,
            produce_name=produce_name,
            price=price
        )

        # # tags
        # for j in range(random.randint(1, 5)):
        #     tag = Tag.query.get(random.randint(1, Tag.query.count()))
        #     if tag not in photo.tags:
        #         photo.tags.append(tag)

        db.session.add(photo)
    db.session.commit()


# def fake_collect(count=50):
#     for i in range(count):
#         user = User.query.get(random.randint(1, User.query.count()))
#         user.collect(Photo.query.get(random.randint(1, Photo.query.count())))
#     db.session.commit()


