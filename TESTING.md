## Testing

## Testing User Stories

#### New User:

1. As a new user, I want to be able to navigate to the Sign-Up page to register an account and the Sign-In page to log in.

   - The sign-in/sign is included in the navigation bar to make the user experience better 
   - Navigation bar adapts as the user is logging/registering for easy navigation
   - Website layout is easy to navigate.
     <img src="" width="100%" alt=" Navigation bar with a sign-in/sign-up buttons visible ">

2. As a new user, navigate the site intuitively.

   - The navigation bar is easily accessible and visible at the top of the page.
   - The navigation bar takes the user to the correct destination and is labelled correctly.
   - The purpose of the site is easy to establish by the relevant layout and options available as well as a short description on the main page.

3. As a new user, easily access recipes.
Recipes are visible on the main page of the website.
Add Recipe button is visible and accessible through a navigation bar on the top of the page.
Edit/View/Delete Recipe buttons are visible under every recipe.
  

#### Returning User Goals:

1. As a returning player, I want to be able to access my account on the website.

   - The sign-in button is visible on top of the screen when the page loads.
   - Users can log out after accessing the logout button in the navigation bar.

2. As a returning player, I want the information I seek to be easily accessible, like recipe instructions.
   <img src="" width="100%" alt="home content responsiveness test">

   - Recipes are situated on the main page.
   - Website layout is easy to navigate to view recipes button.
   - The navigation bar is easily accessible and visible at the top of the page with other useful functions.

3. As a returning player, I expect to function without errors.

   - - The buttons on the website are all functional and labelled correctly.
   - The navigation bar takes the user to the correct destination and is labelled correctly
     <img src="" width="100%" alt="">

#### Person with an interest in cooking :

1. As a person with an interest in cooking, I want to be able to expand my knowledge by finding relevant recipes.

   - The Recipes are available on the main page of the website
   - The navigation bar is easily accessible and visible at the top of the page.

2. As a person with an interest in cooking, I want to access a recipe site where I can share and edit recipes.
   <img src="" width="100%" alt="">

   - Buttons for editing, deleting, viewing and adding recipes are visible and work correctly.
   - Uploaded recipes can be viewed on the main page 

3. As a person with an interest in cooking, I want to easily navigate the entire site intuitively.

   - The navigation bar is easily accessible and visible at the top of the page.
   - The navigation bar takes the user to the correct destination and is labelled correctly.
   - Website layout is easy to navigate.

## Manual Testing

### Common Elements Testing

Manual testing was conducted on the following elements that appear on every page:


- Clicking on the navigation bar menu items to take the user to the correct page on the
  website

<p>
  <img src="" width="100%" alt="nav-bar categories test">
  <img src="" width="100%" alt="nav-bar add recipes">
<img src="" width="100%" alt="nav-bar home">
</p>


- Clicking on Sign in/ Sign up takes the user to the correct page

<p>
  <img src="" width="100%" alt="Sign in">
  <img src="" width="100%" alt="Sign up">
</p>

- Clicking on the footer items to take the user to the correct page on the
website
Facebook
Twitter
Instagram
LinkedIn

  <p>
  <img src="" width="100%" alt=" social media test">
  </p>

### Home Page

Manual testing was conducted on the following elements of the [Home Page](recipies.html):

- The responsiveness of the page
<p>
  <img src="" width="100%" alt="home content responsiveness test">
  <img src="" width="100%" alt="add recipe page responsiveness test">
  <img src="" width="100%" alt="categories page rules responsiveness test">

</p>

- Buttons for CRUD functionality visible on the main page under every recipe (view, edit, delete)

 <p>
  <img src="" width="100%" alt="CRUD buttons">
</p>

- Add Recipe Button visible on the main page

 <p>
  <img src="" width="100%" alt="Add Recipe button">
</p>

- Recipe Description, time it takes to prepare and category are visible under every recipe

<p>
  <img src="" width="100%" alt="Recipe description, time and category">
</p>

- Buttons change background colours when hovered over

<p>
  <img src="" width="100%" alt=">
</p>

- The delete Recipe button comes up with a modal to give the user a choice to Cancel or Delete the Recipe permanently

<p>
  <img src="" width="100%" alt="The recipe delte modal">
</p>


### Category Page

Manual testing was conducted on the following elements of the [Category Page](categories.html):

- The responsiveness of the page
<p>
  <img src="" width="100%" alt="categories page responsiveness test">
</p>

- The add category button is working and taking the user to the correct page
<p>
  <img src="" width="100%" alt="categories add button">
</p>

- Delete category button is working and taking the user to a modal with Close or Delete options
<p>
  <img src="" width="100%" alt="categories delete modal">
</p>



### Add a Recipe Page

Manual testing was conducted on the following elements of the [Add a Recipe Page](add_recipe.html):

- The responsiveness of the page
<p>
  <img src="" width="100%" alt="add recipe responsiveness page">
</p>

- Form is available to fill
<p>
  <img src="" width="100%" alt="add recipe page form">
</p>

- If the recipe name submitted is the one that already exists then the page will reload and an alert come up
<p>
  <img src="" width="100%" alt="alert that name already exists">
</p>

- If the field on the form is empty a prompt will come up to fill it 
<p>
  <img src="" width="100%" alt="prompt to fill the required field">
</p>

- Submit Button takes the User back to the main page and uploads the recipe to the database, visible on the main page.
<p>
  <img src="" width="100%" alt="prompt to fill the required field">
</p>

## Automated Testing

Both manual and automated testing are used to check if the project's code is written in a way the project works correctly.
Automated testing can be performed via a Python testing framework like Pytest. I am aware of the advantages the automated testing carries like high reliability, as it is run and performed by a programme as the code is developed and it is a lot quicker as hundreds of tests can be performed against the project in a short time frame.
Although more time-consuming, I have decided to utilise the manual way of testing as the project is quite small and I didn’t have the time capacity in the project window to get automated testing set up correctly.
Manual testing checks if the project works by user stories by testing it in different browsers and resolutions. The testing can be performed manually by a potential user, code creator or another third party.

In a real-life scenario, I fully acknowledge I would use PyTest to further practice my skills with automated testing and make sure that errors are picked up early and corrected promptly.

### Code Validation

The [W3C Markup Validator](https://validator.w3.org/) service was used to validate the `HTML` and `CSS` code used.
The []() service was used to validate Python.

**Results:**

- Home Page

<p>
  <img src="" width="100%" alt=" Home Page Validator">
</p>

- Category Page

<p>
  <img src="" width="100%" alt=" Category Page Validator">
</p>

-Recipes Page

<p>
  <img src="" width="100%" alt=" Recipe Page Validation">
</p>

- CSS

<p>
  <img src="" width="100%" alt="CSS Validator">
</p>


### Browser Validation

- Chrome

<p>
  <img src="" width="100%" alt="chrome test">
</p>

- Firefox

<p>
  <img src="" width="100%" alt="firefox test">
</p>

- Safari

<p>
  <img src="" width="100%" alt="safari test">
</p>

## User testing

A few friends and family members were asked to review the page for user experience and to point out any bugs/issues. The input of this group led to small UX adjustments to improve the overall site appearance and user experience. Some of them included: Adding a Close button to the Delete modal, Adding color changes to buttons and graphics adjustments.