
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




