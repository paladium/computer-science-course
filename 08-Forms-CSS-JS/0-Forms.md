# HTML forms
An HTML form is used to collect user input. The user input is most often sent to a server for processing.

![form](./img/form.jpg)

To create a new html form:
```html
<form>
</form>
```

## Input element
The HTML ```<input>``` element is the most used form element.

An ```<input>``` element can be displayed in many ways, depending on the type attribute.

Here are some examples:

Type|Description
----|----
```<input type="text">```|Displays a single-line text input field
```<input type="radio">```|Displays a radio button (for selecting one of many choices)
```<input type="checkbox">```|Displays a checkbox (for selecting zero or more of many choices)
```<input type="submit">```|Displays a submit button (for submitting the form)
```<input type="button">```|Displays a clickable button

## Text fields
```html
<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname">
</form>
```

## Radio buttons
```html
<form>
  <input type="radio" id="male" name="gender" value="male">
  <label for="male">Male</label><br>
  <input type="radio" id="female" name="gender" value="female">
  <label for="female">Female</label><br>
</form>
```

## Checkboxes
```html
<form>
  <input type="checkbox" id="vehicle1" name="vehicle1" value="Bike">
  <label for="vehicle1"> I have a bike</label><br>
  <input type="checkbox" id="vehicle2" name="vehicle2" value="Car">
  <label for="vehicle2"> I have a car</label><br>
  <input type="checkbox" id="vehicle3" name="vehicle3" value="Boat">
  <label for="vehicle3"> I have a boat</label>
</form>
```

## The Submit Button
The ```<input type="submit">``` defines a button for submitting the form data to a form-handler.

The form-handler is typically a file on the server with a script for processing input data.

The form-handler is specified in the form's action attribute.
```html
<form action="/create-user">
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value="John"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe"><br><br>
  <input type="submit" value="Submit">
</form>
```

## Name for input
Notice that each input field must have a ```name``` attribute to be submitted.

If the ```name``` attribute is omitted, the value of the input field will not be sent at all.

## Homework - user registration
Create a form to ask for user details: name, country of birth (select element), date of birth(date element), email (input email) age (input element), password (password input) and have the button to submit his information. The action on the form should be: /register.
 
Launch a simple server using the following command:
```bash
python -m http.server
```
Use the following link for reference of different input types: https://www.w3schools.com/html/html_form_input_types.asp