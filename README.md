# Piggy before the infection started.The shop.

VIEW THE FINISHED PROJECT HERE

Through the years, Piggy before the infection started has garnered an ever increasing group of faithful followers. 

Piggy before the infection started-The shop is the exclusive official merchandise site for the Piggy before the infection started series. 

It aims to look after the series' fans as well as increase the reach of the series.

## Business goals.

- To provide exclusive merchandise for Piggy before the infection started series.

- To increase the reach of the Piggy before the infection started series.

- To make Piggy before the infection fans feel looked after.

## User needs.

### Fans needs.

- To be able to easily browse through the items.

- To have clear information about the products offered.

- To be able to save their shopping basket and return  to it later.

- To be able to securely pay for the items bought.

- To receive updated information about the state of their order.

- To be able to write reviews and read reviews made by other users.

### Creator's needs.

- To be able to easily add, modify and delete products.

- To be able to easily add, modify and delete promotions.

- To be able to easily change the video offer panel.

- To be able to  contact users about new offers and products.

## User stories.

- As a user I want to be able to  easily  register, log in and log out of my account so that I can access the site.

- As a user I want to be able to easily change my password so that  if I forget it I can get into my account

- As a user I want to have a profile so that I can see my order history and complete checkout quickly.

- As a user I want to be updated when my order is on its way so that I can be informed.

- As a user I want to be able to navigate through the products easily so that I can see what is on offer.

- As a user I want to be able to search products by category and character so that I can find what I want easily.

- As a user I want to be able to see the specific information for the product that interests me so that I can make a decision.

- As a user I want to be able to read and write reviews so that I can see what other users think about a product before I buy and make my opinion count.

- As a user I want to be able to add items to the basket so that I can purchase them.

- As a user I want to be able to modify  items on the basket so that I can refine my purchase.

- As a user I want to  see how much I have spent so far so that I can decide whether to continue buying.

- As a user I want to be able to pay for my items securely so that my personal information is not compromised.

- As a user, I want to be able to see my order history so that I can Keep track of what I have ordered.

- As the creator I want to be able to  add, remove and modify products so that my offer is always up to date.

- As the creator I want to be able to  see a list of the items that have been sold and the state of the orders so that I can ensure a fast service.

## Plan.

From the users point of view, the site will have four main pages. The home page will show a header with buttons to log in and register and a footer with links to  appropriate sites  and newsletter registration. Once the user has logged in, the header will show buttons to log out, go to account and shopping basket.

On the body, there will be a side panel with suggested videos and a middle section which will work as a navigation to see the different categories of products and offers.

[Intitial home page wireframe. Desktop](/readme/images/wireframes/initial_home.jpg)

[Initial home page wireframe. Small screen](/readme/images/wireframes/initial_home_small.jpg)

The products page will have the same format, with the list of products on the middle section.

The individual product page will show the information about the product with a choice of pictures, the ability to add to the basket, and a rate the product section where the shopper can read and write reviews for the product.

[Initial product detail wireframe.](/readme/images/wireframes/initial_detail.jpg)

The shopping basket will show the products, quantity and final price and will allow to check out safely.

[Initial shopping basket wireframe.](/readme/images/wireframes/initial_shopping_bag.jpg)

On the creator’s side of the site, there will be features to add, modify and delete products and offers and see list of product sold on a period of time.

The account link will lead to a page where the user can see and modify their personal information, as well as see their purchase history and details about any specific order.

## Features

### Customisable homepage. 

The homepage has a structure which continues over the products templates, featuring a navigation bar at the top with links to all products, plushes, 3d prints and shopping basket and a vertical section which contains links to content related videos. 

The main area of the homepage is divided into four completely customisable sections, with the option to include a picture, a title and a link. The content of these sections is controlled by the Homepage model, which also controls the video links in the vertical section.

The videos in the vertical section on the other pages will be controlled by their respective models.

## Issues.

The email confirming the order was successfully processed currently ends up in the recipient's junk email. This is probably due to the fact that the email content is business based while the sender's email has been registered as a personal email address.



## Deployment.

When setting heorku app must run this from terminal:

heroku config:set EMAIL_HOST_PASSWORD="email-app-pwd" --app heroku-app-name

to configure the email

add stripe keys to heroku. Change local host settings.

## Use of AI.

The following features were developed using AI assistance:

- Products app: Custom context processor to dynamically inject YouTube videos into templates.

- Profiles app: PasswordResetLog model to comply with legal requirements referring to use of forgotten password feature.

- Shopping_bag app : Signals to merge anonymous and logged-in user shopping baskets.

- Shopping_bag app: Helper function to retrieve or create basket.

- settings.py: Code to record reset password requests for Heroku loggins.

## Frameworks, packages and libraries.

- Django 6.0.7

- To manage sensitive data: django-environ 

- To manage database: psycopg2 

- For enhanced authentifcation: django-allauth

- To manage deployment to heroku: gunicorn

- To manage deployment of static files: WhiteNoise

- To provide a rich text editor: django-summernote

- To serve image files: cloudinary, dj3-cloudinary-storage urllib3

- To handle payments: stripe

- To run automated tests: pytest

- To convert image to webp: [ToWebP](https://towebp.io/)


- [Django-environ documentation](https://django-environ.readthedocs.io/en/latest/)

- [stripe docs](https://docs.stripe.com/get-started?locale=en-GB)

- Passwords in online services. [ico](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/security/a-guide-to-data-security/passwords-in-online-services/)

- Passwords administratoin for system owners [National Cyber Security centre](https://www.ncsc.gov.uk/collection/passwords/updating-your-approach)

- To send emails. [Resend](https://resend.com/docs/send-with-django)

- PostgreSQL JSON tutorial [Neon](https://neon.com/postgresql/tutorial/json)

- Model properties [DEV](https://dev.to/doridoro/django-model-properties-28ac)

- Effortless pagination in Django. [Medium]https://medium.com/@pirson/effortless-pagination-in-django-from-basics-to-best-practices-2bd3c0d7d710)

- Accessing and using cleaned data. [Medium](https://awstip.com/accessing-and-using-cleaned-data-making-django-forms-work-for-you-5f32a379e32b)

- Printing queries. [Mmdn](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Printing)

- Testing pagination. [BrowserStack](https://www.browserstack.com/guide/test-cases-for-pagination-functionality)

- Mock object library. [Real Python](https://realpython.com/python-mock-library/) 

- Mock and MagicMock. [Medium](https://medium.com/@snehagiranje05/unveiling-the-magic-understanding-mock-and-magicmock-in-python-ecadf1f1013c)
