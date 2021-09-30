# scraper-olx

<h1>Scraper Olx</h1>


<h3>How does it work?</h3>

<spanThe olx scraper consist of three stages:</spam>
<ol>
<li>Fetch inventory urls</li>
<li>Fetch inventory data from those url</li>
<li>Download the inventory url</li>
</ol>

<p>Now, I'll explain each step in detail.</p>

<h6>First Step:</h6>
<p>
Firstly, you get category or your desired search page url from the olx website.
When you give that url to the main.py, It will download all the a href tag from the link.
and a filter will seperate all item based urls from the non usable urls. 

Afterward, all those urls are saved into the database with condition that no duplicate link is being stored.
</p>

<h6>Second Step:</h6>
<p>
Second Step, its a bit tricky here. you will need to save the data of each inventory into database.
For that, you need to access each data using the script. but, as each data is different. 
So, we will have to change the entire table structure according to the page of each category.
<br/>

This step will need a little knowledge of how to code.
</p>

<h6>Third Step:</h6>
<p>
Third and the last step, is the most easy step. It downloads the images of the saved inventory
from the olx aws server and automatically saved them into their unique folder decided from their 
database primary key.
<br/>
Unlike, other step. It is fully automatic and does not require any user input.
</p>


