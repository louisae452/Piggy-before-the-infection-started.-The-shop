
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




