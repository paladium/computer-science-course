# InstagramClone

In this homework, we will make an instagram clone. The application will consist of 4 pages:
- Login
- Register
- User profile
- Upload image
- Feed

## Login
Login page will contain the username and password form fields. The form will be posted to the server, which will check whether username and password exist. If the data entered was correct, the cookie will be set with the current username. The user will be redirected to his profile: ```/profile/paladium```, where paladium is the username.

## Register
The user will enter his username and password, the form will be posted to the server, where the data will be saved to the JSON file. The user will be redirected to login page.

## Profile Page
Profile page of any user can be visited like this ```/profile/<username>```, where username can be the username of any user.

Profile page will contain the username of the user and his posted images. The images should be displayed using Bootstrap grid (3-4 items per row).

## Upload image
The upload page, should contain the title of the post and the image that will be uploaded. The form will be posted to the server.

The image will be saved as file and the title and filename will be added to json file named images.json:
```json
[
    {
        "id": 123456,
        "title": "Me from work",
        "filename": "d616b98f-de67-4220-bb70-745bbe42078b.png",
        "username": "paladium",
        "date": 1608449524
    }
]
```

> Additional points, if you can make a select on the upload page with 2-3 filters available. The image will then go to the server and the filter will be applied using Pillow library.

## Feed page
The feed will contain images posted sorted by newest first (where the value of date field is the highest).

Each post will contain the title, image and the link to user profile who posted it.

## Notes
Make screenshots of the final application and include them into README.md.

Make a requirements.txt file, which will contain the dependecies for your project. At least it will contain:
```txt
flask
```
If you decide to implement the image filtering using Pillow, it will also contain that library.

The deadline for the project is 2 weeks.