# Udemy clone
In this project, we will try to make a simple udemy clone (online courses) with mysql database, flask server and HTML website.

We will utilise classes for different tables in our database.

The following tables will be created:
- Courses (id, name, description, image_url, price, rating)
- Course material (id, course_id, content, order)
- Degree - (id, degree_name, description)
- Degree_Course - (id, degree_id, course_id)

The following methods are available:
- /courses - list all courses, order by rating
- /courses/:id - get course by id, show its materials as well
- /degrees - list all degrees
- /degrees/:id - show information about one degree and its courses included
- /add-course - show webpage to create a new course
- /course/:id/delete - delete the course
- /course/:id/materials/:id/update - update the course material by id

Design:
- Layout - https://getbootstrap.com/docs/4.0/examples/album/