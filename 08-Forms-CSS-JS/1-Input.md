# Input
The input element has attributes that change its behaviour.

## Value attribute
The input value attribute specifies an initial value for an input field:

```html
<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value="John"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe">
</form>
```

## Readonly attribute
The input readonly attribute specifies that an input field is read-only.

A read-only input field cannot be modified (however, a user can tab to it, highlight it, and copy the text from it).

The value of a read-only input field will be sent when submitting the form!

```html
<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value="John" readonly><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe">
</form>
```

## Disabled attribute
```html
<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value="John" disabled><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe">
</form>
```

## Maxlength attribute
The input maxlength attribute specifies the maximum number of characters allowed in an input field.

```html
<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" size="50"><br>
  <label for="pin">PIN:</label><br>
  <input type="text" id="pin" name="pin" maxlength="4" size="4">
</form>
```

## Min and max attribute
The input min and max attributes specify the minimum and maximum values for an input field.

The min and max attributes work with the following input types: number, range, date, datetime-local, month, time and week.

Tip: Use the max and min attributes together to create a range of legal values.
```html
<form>
  <label for="datemax">Enter a date before 1980-01-01:</label>
  <input type="date" id="datemax" name="datemax" max="1979-12-31"><br><br>

  <label for="datemin">Enter a date after 2000-01-01:</label>
  <input type="date" id="datemin" name="datemin" min="2000-01-02"><br><br>

  <label for="quantity">Quantity (between 1 and 5):</label>
  <input type="number" id="quantity" name="quantity" min="1" max="5">
</form>
```

## Multiple attribute
The input multiple attribute specifies that the user is allowed to enter more than one value in an input field.

The multiple attribute works with the following input types: email, and file.
```html
<form>
  <label for="files">Select files:</label>
  <input type="file" id="files" name="files" multiple>
</form>
```

## Placeholder attribute
The input placeholder attribute specifies short a hint that describes the expected value of an input field (a sample value or a short description of the expected format).

The short hint is displayed in the input field before the user enters a value.

The placeholder attribute works with the following input types: text, search, url, tel, email, and password.

```html
<form>
  <label for="phone">Enter a phone number:</label>
  <input type="tel" id="phone" name="phone"
  placeholder="123-45-678">
</form>
```

## Required attribute
The input required attribute specifies that an input field must be filled out before submitting the form.

The required attribute works with the following input types: text, search, url, tel, email, password, date pickers, number, checkbox, radio, and file.

```html
<form>
  <label for="username">Username:</label>
  <input type="text" id="username" name="username" required>
</form>
```

## Homework - simple shop on forms
Make a simple html-based shop. It should have a single page for adding a new shop item.

### New item page
New item page, should contain the following form:
1. Item title - specify maxlength of 60 characters. Make it required. Name attribute: name.
2. Item price - number only, maximum value of 10000 and minimum is 0. Should be required. Name attribute: price.
3. Item description - textarea, non-required. Name attribute: description.
4. One or more image files. Allowed format: image/* (accept attribute). Name attribute: images.
5. Available stock: number only, maximum value of 100000 and minimum of 1. Required. Name attribute: availableStock.
6. Publish on - date only. Non-required. Name attribute: publishOn.
7. Submit button, which submits the form to /addItem path.

Launch the server using:
```bash
python -m http.server
```
Submit the form, make the screenshot of the console where the command was launched to verify all the data was submitted. Attach the console output to the repository README file.