<h1 align="center">Cookbook - Milestone 3</h1>

[View the live project here.](https://cookbook-milestone.herokuapp.com)

Hello! My name is Renato, and I’m a Code Institute student. This is my third Milestone, and in this project I’m going to use HTML, CSS3, Javascript, Python, Flask, and MongoDB.
I chose to build a small blog for my third Milestone, where I can show that I’m able to use Python+Flask and MongoDB. I also love cooking by the way, this will make my work a bit more pleasant.

I hope you like this small project, ciao!


## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, the user will easily find recipes and categories. The search bar will also help in case the visitor would like to look for a recipe by a specific ingredient. 
        2. The Visitor will find the menu straight at the top divided by categories with no effort.
        3. The index has a main recipe picture at the top to welcome the visitor, and three other sections below: weekly recipes, most rated today, latest recipes.
        4. The index has a further section that shows upcoming streaming events, ready to click when the event is available, this section is an example of Live Streaming schedule to entertain the user.

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, the user will find new recipes rated on the same day and new daily/weekly recipes submitted.
        2. A returning visitor would also find new upcoming streaming videos to entertain and teach how to cook and learn about cooking secrets. 

    -   #### Frequent User Goals
        1. As a Frequent User, the user would find always new recipes and upcoming streaming videos to improve their skills as cook gradually. The Live Streaming would be like a video course with time, and also linked to Youtube videos so that the admin could gain some money from advertisements.

    -   #### ADMIN User Goals
        1. Considering that I was not yet at the point to build a community in my course, I built some sections as an admin would see in order to have CRUD operations available.
        2. In the index the admin will find a straight Click here to add a new recipe close to the search bar. With responsive design, it would be at the top.
        3. Since the webpage does not have logged users yet, the page recipe.html already includes all the functions of the CRUD operations. The user will be able to see the recipe, and as admin will have  three further well working buttons, add, edit and delete. The recipes are in MongoDB. The images are in a local folder.

-   ### Design
    -   #### Colour Scheme
        -   The website shows a mix between black, white, gold and orange (orange will sometimes change brightness).
    -   #### Typography
        -   Mainly Didact Gothic for paragraphs and Source Sans Pro for headers.

*   ### Wireframes
    -   I started with moqups.com, moqups limited the account to 200 object for a free plan that I found out to be a very small amount of objects while working on it, then I had to restart the Wireframes from scratch in HTML and CSS in local while building the structure of the website, the Wireframes at the end became the website.


## Features

-   Responsive on all device sizes


## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript] (https://en.wikipedia.org/wiki/JavaScript)
-   [Python] (https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used
-   [MongoDB] (https://www.mongodb.com/)
-   [Flask] (https://palletsprojects.com/p/flask/)
-   [EmailJS] (https://www.emailjs.com/)

1. [Heroku] (https://www.heroku.com/)
    - Heroku was used to deploy the [website] (https://cookbook-milestone.herokuapp.com). 
2. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
3. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
4. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Didact Gothic' and 'Source Sans Pro' font into the style.css file which is used on all pages throughout the project.
5. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used to add icons for rating, that includes the empty star, half star and full star. Font Awesome was also used for the user icon at the top right (Desktop Version)




## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - Congratulations! No Error Found. Tested all the CSS by direct input on the website.


### Further Testing

-   The Website was tested on Google Chrome, Firefox and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7 Plus, iPad.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   CSS for drop-down menu were adapted in order to have the same performance and look with all the browsers, mostly because of Safari that doesn't display the drop-down menu as well as the other browsers.

### These Are Not Bugs

-   Index.html: we have a link with my name at the top right of the page. It's not linked to any page, it's only an example of what the page would display when the user logs in, a link to their profile.
-   Index.html: In the section Social Links we have four images. These do not provide any link, but are an example of links to the webpage's profiles on the social networks to be followed.
-   Index.html: Upcoming Streaming section doesn't provide any link. They are an example of a working Youtube Channel for the website.
-   In the page categories, i.e. pasta.html, the star doesn't really provide a real rate, even if in MondoDB there are two values for it for future improvements.
-   In recipe.html, the page that diplayes the recipe, we have five stars to rate the recipes. The stars are an example of how the user could rate the recipe, even if in MondoDB there are two values for it for future improvements.
-   In recipe.html, the page that diplayes the recipe, we have four images, icons for the social networks, they are an example of Share It, but have no action.

## Deployment

### GitHub Pages, Heroku and Visual Studio Code

-   The [project] (https://cookbook-milestone.herokuapp.com) was deployed to GitHub Pages linked to [Heroku] (www.heroku.com).
-   Heroku manages app deployments with [Git] (https://git-scm.com/), the popular version control system.
-   To code this project I used a code editor on my computer, [Visual Studio Code] (https://www.visualstudio.com/)for [macOS] (https://en.wikipedia.org/wiki/MacOS)  

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Renato79/cookbook-milestone/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Renato79/cookbook-milestone/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/Renato79/cookbook-milestone/
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/Renato79/cookbook-milestone/
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

-   The drop-down menu was written by [Veiko](https://codepen.io/vkjgr/pens/public), please find the codepen [here](https://codepen.io/vkjgr/pen/VYMeXp)

### Content

- Text intro into the category pages:
    - Text intro in pasta.html found on [delish.com] (https://www.delish.com/cooking/recipe-ideas/g3176/weeknight-pasta-dinners/)
    - Text intro in meatandfish.html taken from allrecipes.com [1] (https://www.allrecipes.com/recipes/411/seafood/fish/) [2] (http://allrecipes.co.uk/recipes/beef-recipes.aspx?page=2)
    - Text intro in vegetarian.html taken from [bbcgoodfood.com] (https://www.bbcgoodfood.com/recipes/category/vegetarian)
    - Text intro in dessert.html taken from [bonappetit.com] (https://www.bonappetit.com/recipes/desserts/slideshow/easy-dessert-recipes)
    - Text intro in baking.html taken from [www.bbcgoodfood.com] (https://www.bbcgoodfood.com/recipes/collection/easy-baking)
- All the recipes were taken from [bbcgoodfood.com] (https://www.bbcgoodfood.com/)
- README.md used is a [Code Institute](https://codeinstitute.net/) sample and was found [here](https://github.com/Code-Institute-Solutions/SampleREADME/blob/master/README.md)

### Media

- [Wix.com:](https://www.wix.com/logo/maker) was used to create the logo.
- [Flaticon.com] (https://www.flaticon.com/categories/social-media) was used to find the Social Network icons
- [Shareicon.net] (https://www.shareicon.net/data/512x512/2015/09/26/107434_youtube_512x512.png) was used to find the Streaming icon
- Background image was taken at this [link] (http://churchofirelandhist.org/wp-content/uploads/2014/04/Silver-scale-White-Seamless-Texture-For-Website-Background.jpg)
- The picture of the loaf in the index.html, that is my picture :-) taken with a Nikon D5600, and yes I also made the loaf with my sourdough :-)

### Acknowledgements

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.