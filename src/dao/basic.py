from sqlalchemy import text
from model import basic_info,courses
from sqlalchemy import join

#view data
#Don't know how to join to <Mapper at 0x7f35066a75e0; Courses>. Please use the .select_from() method to establish an explicit left side, as well as providing an explicit ON clause if not present already to help resolve the ambiguity.
def get_student_info(connection):



    obj = connection.query(courses.Courses.id,courses.Courses.course_name,
                           basic_info.Basic_info.course_id.label('student_id')
                           ).outerjoin(basic_info.Basic_info,courses.Courses.id == basic_info.Basic_info.course_id).all() 
    print(obj)
    data = []
    for row in obj:
        data.append({
            'id' : row.id,
            'course_name' : row.course_name,
            'student_id':row.student_id
        })
    
    return data

''' obj = connection.query(courses.Courses.id,courses.Courses.course_name,
                           basic_info.Basic_info.course_id.label('student_id')
                           ).join(basic_info.Basic_info,courses.Courses.id == basic_info.Basic_info.course_id).all()
    #row = connection.query(basic_info.Basic_info).join(courses.Courses).ON(basic_info.Basic_info.course_id == courses.Courses.id).all()'''
#insert data
def student(id,name,course_id,connection):

    obj = basic_info.Basic_info(id = id,name = name,course_id=course_id)
    connection.add(obj)
    connection.commit()

    return{
        'id' : obj.id,
        'name' : obj.name,
        'course_id':obj.course_id
    }