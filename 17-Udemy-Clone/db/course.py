class CourseManager:
    #Init method to accept db as parameter and save it as variable
    def __init__(self, db):
        self.db = db
    #Make a new function - list_all order by rating desc
    def list_all(self):
        cursor = self.db.get_cursor()
        cursor.execute("SELECT * FROM Courses ORDER BY Rating")
        myresult = cursor.fetchall()
        return myresult
    #Method - create_course, which accepts the parameters for course: name, description, image_url, price & rating
    #Returns the inserted course id
    def create_course(self):
        #TODO
        pass

    #Method - get course by id
    def get_course_by_id(self, id):
        #TODO
        pass

    #Method - delete the course by id
    def delete_course_by_id(self, id):
        #TODO
        pass

