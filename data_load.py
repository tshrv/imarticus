course_data = {
    'title': 'Introduction to Machine Learning',
    'thumbnail': 'course_thumbnails/IMG_20211029_132950.jpg'
}
# create course from admin panel

from courses.models import Course, Module, Lecture
course_id = 1
module_data = [
    {
        'course_id': course_id,
        'title': 'Introduction to Machine Learning',
        'position_in_sequence': 1
    },
    {
        'course_id': course_id,
        'title': 'Concepts of Machine Learning',
        'position_in_sequence': 2
    },
    {
        'course_id': course_id,
        'title': 'Applications of Machine Learning',
        'position_in_sequence': 3
    },
    {
        'course_id': course_id,
        'title': 'Neural Networks and Deep Learning',
        'position_in_sequence': 4
    }, 
    {
        'course_id': course_id,
        'title': 'Applications of Deep Learning',
        'position_in_sequence': 5
    }
]
# create module objects
module_ids = []
for module in module_data:
    obj = Module.objects.create(**module)
    module_ids.append(obj.id)
module_id_1, module_id_2, module_id_3, module_id_4, module_id_5 = module_ids

# module_id_1=1
# module_id_2=2
# module_id_3=3
# module_id_4=4
# module_id_5=5

lecture_data = [
    {
        'module_id': module_id_1,
        'title': 'What is Machine Learning?',
        'duration': 261,
        'position_in_sequence': 1
    },
    {
        'module_id': module_id_2,
        'title': 'Rent Cost of Flat',
        'duration': 207,
        'position_in_sequence': 1
    },
    {
        'module_id': module_id_2,
        'title': 'Linear Regression',
        'duration': 287,
        'position_in_sequence': 2
    },
    {
        'module_id': module_id_2,
        'title': 'Polymer Regression',
        'duration': 255,
        'position_in_sequence': 3
    },
    {
        'module_id': module_id_3,
        'title': 'Spam Email Filter',
        'duration': 418,
        'position_in_sequence': 1
    },
    {
        'module_id': module_id_3,
        'title': 'Recommendation of App',
        'duration': 433,
        'position_in_sequence': 2
    },
    {
        'module_id': module_id_4,
        'title': 'Applciation of ML in College Admission',
        'duration': 405,
        'position_in_sequence': 1
    },
    {
        'module_id': module_id_4,
        'title': 'Applciation of ML in College Admission II',
        'duration': 287,
        'position_in_sequence': 2
    },
    {
        'module_id': module_id_4,
        'title': 'Neural Network',
        'duration': 214,
        'position_in_sequence': 3
    },
    {
        'module_id': module_id_4,
        'title': 'Recognizing Hand Written Digits',
        'duration': 182,
        'position_in_sequence': 4
    },
    {
        'module_id': module_id_4,
        'title': 'Recognizing Hand Written Digits II',
        'duration': 223,
        'position_in_sequence': 5
    },
    {
        'module_id': module_id_5,
        'title': 'Deep Learning',
        'duration': 314,
        'position_in_sequence': 1
    },
]

# create lecture objects
lecture_ids = []
for lecture in lecture_data:
    obj = Lecture.objects.create(**lecture)
    lecture_ids.append(obj.id)
