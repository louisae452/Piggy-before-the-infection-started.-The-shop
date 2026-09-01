
### Automated testing.

The following tests were carried out:


#### Checkout app.

##### Forms

|Date|Form|Test|Result|Follow-up|
|:----|:----|:------|:------|:-------|
|24/08/2026|UserForm|Form is valid when all fields are filled in correctly|Pass||
|24/08/2026|UserForm|Form is not valid when first_name is missing|Pass||
|24/08/2026|UserForm|Form is not valid when last_name is missing|Pass||
|24/08/2026|OrderForm|Form is valid when all required fields are filled in correctly|Pass||
|24/08/2026|OrderForm|Form is not valid when email is missing|Pass||
|24/08/2026|OrderForm|Form is not valid when email is incorrect|Pass||
|24/08/2026|OrederForm|Form is not valid when street_address1 is missing|Pass||
|24/08/2026|OrderForm|Form is not valid when town is missing|Pass||
|24/08/2026|OrderForm|Form is not valid when postcode is missing|Pass||

##### Views

|Date|View|Test|Result|Follow-up|
|:----|:----|:------|:------|:-------|
|26/08/2026|checkout|Checkout populates form data from authenticated user|Pass||
|26/08/2026|checkout|Checkout serves empty form for unauthenticated user|Pass||
|26/08/2026|payment_success|Missing session id and order id redirects with error|Pass||





#### Products app.

##### Forms

|Date|Form|Test|Result|Follow-up|
|:----|:----|:------|:------|:-------|
|24/08/2026|RatingForm|Form is valid when all fields are filled in correctly|Pass||
|24/08/2026|RatingForm|Form is not valid when title is missing|Pass||
|24/08/2026|RatingForm|Form ia not valid when comment is missing|Pass||

###### Views

|Date|View|Test|Result|Follow-up|
|:----|:----|:------|:------|:-------|
|25/08/2026|home_page|Home page loads successfully with an active homepage|Pass||
|25/08/2026|home_page|Hpme page loads successfully without an active homepage|Pass||
|25/08/2026|home_page|Home page loads successfully wiht many active homepages|Pass||
|25/08.2026|all_products|All products page loads successfully when there are no products|Pass||
|25/08/2026|all_products|First page displays 8 products when 10 products are available. Next page button is available|Pass||
|25/08/2026|all_products|Second page displays 2 products when 10 products are available. Previous page button is available|Pass||
|25/08/2026|all_products|When an invalid page is requested, first displays|Pass||
|25/08/2026|plushes|Page loads succcessfully when there are no products|Pass||
|25/08/2026|plushes|First page displays 8 products when 10 products are available. Previous page buton is not available. Next page button is available|Pass||
|25/08/2026|plushes|Second page displays 2 products when 10 products are available. Previous page button is available. Next page button is not available|Pass||
|25/08/2026|plushes|First page loads when an invalid page is requested|Pass||
|25/08/2026|prints|Page loads when there are no products|Pass||
|25/08/2026|prints|First page displays 8 items when 10 are available. Previous page button is unavailable. Next page button is available|Pass||
|25/08/2026|prints|Second page displays 2 items when 8 are available. Previous page button is available. Next page button is unavailable|Pass||
|25/08/2026|prints|First page loads when an invalid page is requested|Pass||
|25/08/2026|product_detail|Page loads. Ratings average is calculated|Pass||
|25/08/2026|product_detail|Page loads when there are no ratings. Rating average is 0|Pass||
|25/08/2026|product_detail|Ratings section first page loads 4 items when 6 are available. Previous button is unavailable. Next button is available|Pass||
|25/08/2026|product_detail|Ratings section second page loads 2 items when 6 are available. Previous page button is available. Next page button is unavailable|Pass||
|25/08/2026|proudct_detail|View retuns 404 page if product slug does not exist|Pass||
|25/08/2025|rate_product|Page loads with rating form|Pass||
|25/08/2026|update_review|Page loads with the required review|Pass||
|25/08/2026|update_review|A user cannot update someone else's review|Pass|||










#### Profiles app.

##### Forms.

|Date|Form|Test|Result|Follow-up|
|:----|:----|:------|:------|:-------|
|24/08/2026|UserForm|Form is valid when all fields are filled in correctly|Pass||
|24/08/2026|UserForm|Form is not valid when first_name is missing|Pass||
|24/08/2026|UserForm|Form is not valid when last_name is missing|Pass||
|24/08/2026|EmailForm|Form is valid when email filled in correctly|Pass||
|24/08/2026|ProfileForm|Form is valid when all required fields are filled in correctly|Pass||
|24/-8/2026|ProfileForm|Form is not valid when street_address1 is missing|Pass||
|24/08/2026|ProfileForm|Form is not valid when town is missing|Pass||
|24/08/2026|ProfileForm|Form is not valid when postcode is missing|Pass||

##### Views

|Date|View|Test|Result|Follow-up|
|:----|:----|:------|:------|:-------|
|26/08/2026|profile|Unathenticated users are redirected to login screen|Pass||
|26/08/2026|profile|Authenticated users can access the page|Pass||
|26/08/2026|profile|Personal information is saved|Pass||
|26/08/2026|profile|Shipping information is saved|Pass||
|26/08/2026|order_history|Page requires login|Pass||
|26/08/2026|order_history|Logged in users get a list of their orders form newest to oldest|Pass||
|26/08/2026|past_order_detail|Page requires login|Pass||
|26/08/2026|past_order_detail|Order owner can see the order|Pass||
|26/08/2026|past_order_detail|Logged in user cannot access someone else's order|Pass||
|26/08/2026|past_order_detail|Logged in user cannot access guest orders|Pass||
|26/08/2026|past_order_detail|Invalid order throws 404 error|Pass||


### Shopping_bag app.

#### Views

|Date|View|Test|Result|Follow-up|
|:----|:----|:------|:------|:-------|
|26/08/2026|shopping_bag|Shopping bag loads and show the bag items|Pass||
|26/08/2026|add_to_basket|View redirects to the original page|Pass||
|26/08/2026|add_to_basket|A new ShopItems record is created|Pass||
|26/08/2026|update_bag|New quantity is saved|Pass||


### Manual testing.

#### Authentiction.

##### Register page.

|Date|Test|Method|Expected result|Result|Follow up|
|:--|:--|:--|:--|:--|:--|
|31/08/2026|Register page loads|Navigate to site. Click on Register button|Register page loads|Pass| |
|31/08/2026|log in link on register page works|In register page, click on log in link|Log in page loads|Pass| |
|31/08/2026|Register account|In register page, fill in fields with suitable information.|Verify your email address page loads with sent email message. Admin panel shows email address as unverified. Email is sent to user with a link to verify password. Link leads to verify password link. On clicking, log in page loads with success message. Email address appears as verified in admin panel|Pass| |
|31/08/2026|No username|In register page, fill in all fields except username. Click on register.|User is prompted to fill username field|Pass| |
|31/08/2026|No email address|In register page, fill in all fields except email. Click on register.|User is prompted to fill email field.|Pass| |
|31/08/2026|No password|In register page, fill in all fields except password. Click on register. |User is prompted to fill password field.|Pass| |
|31/08/2026|Password does not match|In register page, fill the fields. Ensure the confirm password field does not match the original password.|The register page loads again with the filled in username and email.|Pass| |
|31/08/2206|New user registers with an already registered username|In register page, fill in user name with an already existing user's username. Fill in the rest of the fields and save.|A user with that user name already exists message apperars|Pass| |
|31/08/2026|New user registers with already registered email address|In register page, fill the email with an already existing email address. Fill the other fields and Register.| Verify your email address page loads with message. An email is sent to the email address. The email advises the email address is already in use and prompts the user to follow forgotten password protocol if needed.The link leads to password reset link.|Pass| |


##### Sign in page.

|Date|Test|Method|Expected result|Result|Follow up|
|:--|:--|:--|:--|:--|:--|
|31/08/2026|Sign in page loads|Navigate to site. Click on Log in  button|Sign in  page loads|Pass| |
|31/08/2026|Register link in sign in page|On sign in page, click on register link.|Register page loads.|Pass| |
|31/08/2026|Registered user log in|On sign in page, fill in fields for a registered, verified user and sign in.|Home page loads with success message. Main navigator bar shows Account and Log out buttons.|Pass| |
|31/08/2026|Unverified user log in|On sign in page, fill in fields for a registered, unverified user and sign in.|Verify your email address page loads with confirmation email sent message. User receives a verify your email address message.|Pass| |
|31/08/2026|Wrong username|On sign in page, fill in username with a wrong username and right password. Sign in.|Sign in page reloads.|Pass| |
|31/08/2026|Wrong password|On sign in page, fill in correct username with a wrong password.|Sign in page reloads.|Pass| |
|31/08/2026|Forgotten password|On sign in page, click on forgot your password.|Password reset loads. On filling the email address and clicking on Reset my password, Password reset email sent loads. The user receives an email prompting them to change their password. On clicking on the link, the user is directed to the change password page. On choosing a new password, change password loads with success message. The change of password is logged in the Password Reset Log model.|Pass| |

##### Log out page.

|Date|Test|Method|Expected result|Result|Follow up|
|:--|:--|:--|:--|:--|:--|
|31/08/2026| Sign out page loads|Navigate to site. While loggef in, click on Log out button|Sign out   page loads. On clicking on log out button, home page loads with success button. Log in and register buttons appear on main navigator bar.|Pass| |


#### Home page.

|Date|Test|Method|Expected result|Result|Follow up|
|:--|:--|:--|:--|:--|:--|
|31/08/2026|Home button|On any page, click on the home button on the main navigator bar.|Home page loads.|Pass| |

##### Home navigator.

|Date|Test|Method|Expected result|Result|Follow up|
|:--|:--|:--|:--|:--|:--|
|31/08/2026|All products button|On any page, click on all products button.|All products page loads.|Pass| |
|31/08/2026|Plushes button|On any page, click on plushes button.|Plushes page loads.|Pass| |
|31/08/2026|3d prints button|On any page, click on 3d prints button.|Prints page loads.|Pass| |

##### Vertical bar.

|Date|Test|Method|Expected result|Result|Follow up|
|:--|:--|:--|:--|:--|:--|
|31/08/2026|Video 1 link|On any page, click on the top video in the vertical bar.|Video loads on a new window.|Pass| |
|31/08/2026|Video 2 link|On any page, click on the bottom video in the vertical bar.|Video loads on a new window.|Pass| |

##### Main panels.

|Date|Test|Method|Expected result|Result|Follow up|
|:--|:--|:--|:--|:--|:--|
|31/08/2026|Top left panel|On home page, click on the button on the top left panel|Page gets redirected as indicated in the button|Pass|| |
|23/08/2026|Top right panel|On home page, click on the button on the top right panel|Page gets redirected as indicated in the button|Pass| |

#### All products page.

|Date|Test|Method|Expected result|Result|Follow up|
|:--|:--|:--|:--|:--|:--|
|31/08/2026|Product link|On all products page, click on a link for a product.|Product page loads.|Pass| |
|31/08/2026|Pagination. Next button.|On all products page 1, click on next page link.|Page 2 loads.|Pass| |
|31/08/2026|Pagination. Previous button.|On all products page 2, click on previous page link.|Page 1 loads.|Pass| |
|31/08/2026|Pagination. Last button.|On all products page 1, click on last page.|Last page loads.|Pass| |
|31/08/2026|Pagination. First button|On all products last page, click on first page|Page 1 loads.|Pass| |

#### Plushes page.

|Date|Test|Method|Expected result|Result|Follow up|
|:--|:--|:--|:--|:--|:--|
|31/08/2026|Product link|On plushes page, click on a link for a product.|Product page loads.|Pass| |
|31/08/2026|Pagination. Next button.|On plushes page 1, click on next page link.|Page 2 loads.|Pass| |
|31/08/2026|Pagination. Previous button.|On plushes page 2, click on previous page link.|Page 1 loads.|Pass| |
|31/08/2026|Pagination. Last button.|On plushes page 1, click on last page.|Last page loads.|Pass| |
|31/08/2026|Pagination. First button|On plushes last page, click on first page|Page 1 loads.|Pass| |

#### Prints page.

|Date|Test|Method|Expected result|Result|Follow up|
|:--|:--|:--|:--|:--|:--|
|31/08/2026|Product link|On prints page, click on a link for a product.|Product page loads.|Pass| |
|31/08/2026|Pagination. Next button.|On prints page 1, click on next page link.|Page 2 loads.|Pass| |
|31/08/2026|Pagination. Previous button.|On prints page 2, click on previous page link.|Page 1 loads.|Pass| |
|31/08/2026|Pagination. Last button.|On prints page 1, click on last page.|Last page loads.|Pass| |
|31/08/2026|Pagination. First button|On prints last page, click on first page|Page 1 loads.|Pass| |

#### Product page.

|Date|Test|Method|Expected result|Result|Follow up|
|:--|:--|:--|:--|:--|:--|
|31/08/2026|Change main image|On product page, click on one of the smaller images.|The smaller image shows in the main image display.|Pass| |
|31/08/2026|See large image link|On product page, click on see large image link.|The image in the main image display opens in a new window.|Pass| |
|31/08/2026|See character link.|On product page, click on see character link.|Character's link in wikipediea opens in new window.|Pass| |
|31/08/2026|Be first to rate this product link|On product page, click on Be the first to rate this product link if available|Rate page loads.|Pass| |
|31/08/2026|Quantity arrow up|On product page, click the up arrow.|Quantity goes up by 1|Pass| |
|31/08/2026|Quantity arrow down|On product page, click on the down arrow.|Quantity goes down by 1 until the quantiy is 1.|Pass| |
|31/08/2026|Add to bag button|On product page, click on add to bag button.|The product is added to the basket. The quantity on the basket button on the main navigator bar goes up by the required amount|Pass| |
|31/08/2026|Be the first to rate this product button.|On producy page, click on be the first to rate this product if available.|Rate product page loads.|Pass| |
|31/08/2026|Rate this product button|On product page, click on rate this product button if available.|Rate page loads.|Pass| |
|31/08/2026|Update button.|Log into the site. On the product page for a products you have rated, click on update button.|Only the user's ratings show the update button. When update is clicked on, update rating page loads.|Pass| |
|31/08/2026|Pagination. Next button.|On ratings section page 1, click on next page link.|Page 2 loads.|Pass| |
|31/08/2026|Pagination. Previous button.|On ratings section page 2, click on previous page link.|Page 1 loads.|Pass| |
|31/08/2026|Pagination. Last button.|On ratings section page 1, click on last page.|Last page loads.|Pass| |
|31/08/2026|Pagination. First button|On ratings section last page, click on first page|Page 1 loads.|Pass| |

#### Rate page.

|Date|Test|Method|Expected result|Result|Follow up|
|:--|:--|:--|:--|:--|:--|
|31/08/2026|Star rating required|On a rate page, add a title and a comment. Clik on save.|Page reloads wiht message to add a star rating.|Pass| |
|31/08/2026|Title required| On a rate page, add a star rating and a comment. Click on save.|A prompt to fill the title appears.|Pass| |
|31/08/2026|Comment required.|On a rate page, add a star rating and a title. Click on save.|A prompt to fill the comment appears.|Pass| |
|31/08/2026|Logged in user rating save.|After signing in, on a rate page, add a star rating, a title and a comment. Click on save.|Rating is saved. Rating appears in rating area of product image with user name.|Pass| |
|31/08/2026|Guest user rating save.|Without signing in, on a rate page, add a star rating, a title and a comment. Click on save.|Rating is saved. Rating appears in rating area of product image credited to guest user.|Pass| |


#### Update rating page.

|Date|Test|Method|Expected result|Result|Follow up|
|:--|:--|:--|:--|:--|:--|
|31/08/2026|Update button.| After logging in, navigate to a rating written by the user. Click on the update button. Change some of the fields. Click on update.|The review is updated on the ratings section of the product.|Pass| |
|31/08/2026|Delete button/ cancel.|After loggin in, navigate to a rating written by the user .Click on update. Click on delete. Cancel delete.| Delete is cancelled.|Pass| |
|31/08/2026|Delete button/ delete.|After loggin in, navigate to a rating witten by the user. Click on update. Click on delete. Confirm delete.|The review is deleted. Product page loads with success message.|Pass| |
|3108/2026|Unauthorised user.|After logging in, navigate to a rating written by the user. Click on the update button. Copy the url address. Log out. Paste the url address onto a new browser page.|403 error displays.|Pass|  |


#### Shopping basket page.

|Date|Test|Method|Expected result|Result|Follow up|
|:--|:--|:--|:--|:--|:--|
|31/08/2026|Empty basket|Go onto the site. Before adding any items, click on the shopping basket button on the main navigation bar.|Empty basket page displays.|Pass| |
|31/08/2026|Empty basket-  continue shopping button|On the empty basket page, click on continue shopping button.|All products page loads.|Pass| |
|31/08/2026|Populated basket.| Add some items to the basket . Click on basket icon on main navigator bar.|Shopping basket page loads with items added to basket.|Pass| |
|01/09/2026|Arrow up|Add some items to the basket. Naviagte to basket page. On one of the items, click on the up arrow.|The quantity goes up by one.|Pass| |
|01/09/2026|Down arrow.|Add some items to the basket. Click on basket icon on main navigator. On one of the items with a quantity higher than one, click on the down arrow.|The quantity goes down by 1 until it is 1.|Pass| |
|01/09/2026|Update button|Add some items to the basket. Click on basket icon on main navigator. Change the quantity on one of the items. Click on update.|The amounts on subtotal and total are ammended to reflect the change.|Pass| |
|01/09/2026|Remove button.|Add some items to the basket. Click on basket icon on main navigator. On one of the items, click on remove.|The item disappears. The total quantity is ammended to reflect the change.|Pass| |
|01/09/2026|Basket merge.|Log on to the site. Add some items to the basket. Log out.While not logged in, add some more items to the basket. Navigate to the shopping basket page. Click on log in and log back in.|The items in the guest basket are added to the items in the saved user basket. Total is ammended.|Pass| |
|01/09/2026|Proceed to checkout button.|On a populated basket page, click on proceed to to checkout button.|Checkout page loads.|
|01/09/2026|Continue shopping.|On a populated basket page, click on continue shopping button.|All products page loads.|Pass| |

#### Checkout page.

|Date|Test|Method|Expected result|Result|Follow up|
|:--|:--|:--|:--|:--|:--|
|01/09/2026|Back to shopping basket button.|Add some items to the basket and navigate to the checkout page. Click on Back to shopping basket button.|Shopping basket page loads.|Pass| |
|01/09/2026|Guest check out.|Without logging in, add some items to the basket and navigate to the checkout page. Fill in the fields with suitable information and click on proceed to secure Payment button.|Stripe page loads.|Pass|  |
|01/09/2026|First name missing |Add some items to the basket and navigate to the checkout page. Fill in all the required fields except First name. Click on proceed to checkout button.|A prompt to fill in the first name appears.|Pass| |
|01/09/2026|Last name missing.|Add some items to the basket and navigate to the checkout page. Fill in all the required fields except Last name. Click on proceed to checkout button.|A prompt to fill in the last name appears.|Pass| |
|01/09/2026|email missing.|Add some items to the basket and navigate to the checkout page. Fill in all the required fields except email. Click on proceed to checkout button.|A prompt to fill in the last email appears.|Pass| |
|01/09/2026|Street address 1 missing.|Add some items to the basket and navigate to the checkout page. Fill in all the required fields except street address 1. Click on proceed to checkout button.|A prompt to fill in street address 1 appears.|Pass| |
|01/09/2026|Town missing.|Add some items to the basket and navigate to the checkout page. Fill in all the required fields except town. Click on proceed to checkout button.|A prompt to fill in the town appears.|Pass| |
|01/09/2026|Postcode missing.|Add some items to the basket and navigate to the checkout page. Fill in all the required fields except postcode. Click on proceed to checkout button.|A prompt to fill in the last postcode appears.|Pass| |
|01/09/2026|Log in on page.| Add some items to the basket and navigate to the checkout page. Click on log in button and log in.|The checkout page loads in with saverd profile information.|Pass|  |
|01/09/2026|Deliver to a different address|Add some items to the basket  and navigate to the checkout page. Log in. Change the address the order is delivered to. Do not click on save address to my profile. Proceed to checkout.|Order is recorded with new address. Address on user's profile remains unchanged.|Pass| |
|01/09/2026|Save profile information.|Add some items to the basket  and navigate to the checkout page. Log in as a user with no profile. Fill in the form with the required fields. Click on save name and save address to my profile. Proceed to checkout.|Order is recorded. Information is saved on user's profile is.|Pass| |
|01/09/2026|Deliver to a different address and change address on profile|Add some items to the basket  and navigate to the checkout page. Log in. Change the address the order is delivered to. Click on save address to my profile. Proceed to checkout.|Order is recorded with new address. Address on user's profile is changed.|Pass| |
|01/09/2026|Change name on profile|Add some items to the basket  and navigate to the checkout page. Log in. Change the name the order is delivered to. Click on save save to my profile. Proceed to checkout.|Order is recorded with new address. Address on user's profile is changed.|Pass| |












#### Stripe page.

|Date|Test|Method|Expected result|Result|Follow up|
|:--|:--|:--|:--|:--|:--|
|01/09/2026|Payment goes through.|Add some items to the basket. Navigate to the checkout page and fill the form with suitable information.Click on proceed to secure payment button. On Stripe page,fill in the tester credit card information. Click on pay.|Thank you for your order page loads . An email is sent to inform the usesr the order has been successful. A new record is created in the Order model.|Pass|  |


#### Thank you page.

|Date|Test|Method|Expected result|Result|Follow up|
|:--|:--|:--|:--|:--|:--|
|01/09/2026|Print invoice button|Add some items to the basket and proceed to checkout. On the thank you for your order page, click on print invoice button.|The printer page on your device loads ready to print the invoice.|Pass| |
|01/09/2026|Continue shopping button.|Add some items to the basket and proceed to checkout. On the thank you for your order page, click on continue shopping button.|All products page loads.|


#### Profile page.

|Date|Test|Method|Expected result|Result|Follow up|
|:--|:--|:--|:--|:--|:--|
|01/09/2026|Page loads|Log on to the site. Click on the account button on the main navigator bar|Profilee page loads with uses's saved information|Pass| |
01/09/2026|Unauthorised user cannot access page.|Log onto site. Navigate to profile. Copy url address. Open a different browser. Paste url address|User gets directed to log in page.|Pass| |
|01/09/2026|Change personal information.|Log on to site. Navigate to profile page. Add or change personal information. Click on update button.|Page reloads with new information and success message.|Page loads with new information. No success message. Fail|Add success message|
|01/09/2026|Change personal information.|Log on to site. Navigate to profile page. Add or change personal information. Click on update button.|Page reloads with new information and success message.|Pass| |
|01/09/2026|Change shipping information.|Log on to site. Navigate to profile page. Add or change shipping information. Click on update button.|Page reloads with new information and success message.|Pass| |
|01/09/2026|Change password button|Log onto the site and navigate to profile page. Click on change password button.|Change password page loads.|Pass| |
|01/09/2026|Change password.|Log onto site and navigate to profile page. Click on change password button. Enter current and new passwords. Click on change passoword|Profile page loads with success message.|Change password loads again with no message. Fail.|Add adapter to redirect change_password to profile page.|
|01/09/2026|Change password.|Log onto site and navigate to profile page. Click on change password button. Enter current and new passwords. Click on change passoword|Profile page loads with success message.|Pass||
|01/09/2026|change email button|Log onto site and navigate to profile page. Click onchange email button.|email address page loads.|Pass| |
|01/09/2026|Add new email address|Log onto site and navigate to profile page. Click on change email button. Add a new email address and click on add email.|Email address page with confirm your email message.|Pass||
|01/09/2026|Email address make primary. Unverified email|Log onto site and navigate to profile page. Click on change email button. Select unverified email address and click on make primary button.|Page reloads with message to advise email must be verified|Pass||
|01/09-2026|Email address make primary. Verified email|Log onto site and navigate to profile page Click on change email. Select a verified email address. Click on make primary button.|Page reloads with success message.|Pass| |
|01/09/2026|Remove email. Primary address.|Log onto site and navigate to profile page. Click on change email. Select the primary email. Click on remove email.|Page reloads with message advising you cannot remove primary email.|Pass| |
|01/09/2026|Remove email. Non primary address|Log onto site and navigate to profile page. Click on change email. Select a non primary email. Click on remove email.|Page reloads with success message.|Pass| |
|01/09/2026|Re-send verification button|Log onto site and navigate to profile page. Click on change email button. Click on an unverified email address. Click on re-send verification button|Page reloads with confirmation email sent message. Confirmation email message sent.|Pass| |
|01/09/2026|Back to profile button.|Log onto site and navigate to profile page. Click on change email button. Click on back to profile button.|Profile page loads.|Pass| |
|01/09/2026|Order history link|Log onto site. Navigate to profile page. Click on Order history link.|Order history for user loads.|Pass| |

#### Order history page.

|Date|Test|Method|Expected result|Result|Follow up|
|:--|:--|:--|:--|:--|:--|
|01/09/2026|Unauthorised user cannot access page.|Log onto site. Navigate to order history. Copy url address. Open a different browser. Paste url address|User gets directed to log in page.|Pass| |
|01/09/2026|Order link|Log onto site. Navigate to order history. Click on past order link.|Past order page loads.\Pass| |

#### Past order page.

|Date|Test|Method|Expected result|Result|Follow up|
|:--|:--|:--|:--|:--|:--|
|01/09/2026|Unauthorised user cannot access page.|Log onto site. Navigate to past order page. Copy url address. Open a different browser. Paste url address|User gets directed to log in page.|Pass| |
|01/09/2026|Print invoice button.|Log onto site. Navigate to past order page. Click on print invoice button.|Printer preview page loads.|Pass| |
|01/09/2026|Continue shopping button.|Log onto site. Navigate to past order page. Click on continue shopping button.|All products page loads.|Pass| |







### User experience.

|Date|Issue|Template|View/Form|Action taken|
|:--|:--|:--|:--|:--|
|01/09/2026|It is not clear which fields are required.|checkout/checkout.html|checkout:UserForm, checkout:OrderForm|Added required class to forms.|
|01/09/2026|Change password template redirects back to itself after saving new password.|allauth change_password.html|---|Add adapter to redirect template back to profile template.|

