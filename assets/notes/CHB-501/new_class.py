import os


class Course:
    def __init__(self, code, default_lecturer):
        self.code = code
        self.default_lecturer = default_lecturer
        self.class_record = f'{code}/class_record.csv'
        self.syllabus = f'{code}/syllabus.md'


from datetime import date


class Lecture:

    def __init__(self, course, topic, lecturer=None, recording=None, date=date.today()):
        self.course = course
        self.date = date
        if lecturer:
            self.lecturer = lecturer
        else:
            self.lecturer = course.default_lecturer
        self.recording = recording
        self.title = topic
        f = open(f'{course.code}/class_record.csv', 'a')
        f.write(f'\n{date},{lecturer},{topic},{recording},')
        f.close()
        os.idea


chb501 = Course('CHB-501', 'Dr. Shruti Trivedi')
a = Lecture(chb501, 'introduction')
