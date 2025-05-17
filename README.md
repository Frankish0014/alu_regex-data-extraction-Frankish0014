Form field validations.

Check out how the various regex would work

1. Email addresses: ^[a-zA-Z0-9._%+_]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
The regext provided for this makes it possible for a user to enter any email in any formate like f.ishimwe@alustudent.com, ishimwefrank711@gmail.com or any kind, but it's mandatory to have a some charactors before the @ and after. And always there has to be characters after a dot (.) and it's not allowed to have spaces in the emails. 
And the user needs to have as many extenstions as posssible.

2. URLs: ^https:\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\/[^\s]*)?$ 
Here the user needs to have an link with https compalsory as the examples given in the assignment https://www.example and https://subdomain.example.org/page. The user needs to be keen with providing spaces in the link because they are not allowed.
otherwise every other URL could work perfectly here.

3. Phone numbers (Various formate): ^(\(\d{3}\)|\d{3})[-. ]\d{3}[-. ]\d{4}$
This will allow the user to enter any phone number with the following restrictions; The user has to begin with 3 digits if below 3 (invalid), Should be a space after 3 digits of first 2 pairs. And their should be 4 digits after the 2 pairs of 3 digits in the phone number, Not allowed to enter letters.


4. Credit Card numbers: ^\d{4}[-. ]\d{4}[-. ]\d{4}[-. ]\d{4}$
First of all we know that credit card numbers have to be 16 digits with a 4 pairs and a space between the 4 paired digits. The number of pairs shoulden't exceed 4 or bellow. And the numbers shouldn't go above or bellow 16. No letter or sign has to be included.


5. Time: ^([01]?[0-9]|2[0-3]):[0-5][0-9]$
First of all, the range of hours numbers shouldn't go beyond 23 and minutes not beyond 59. No space or letter required. And the sign has to be a colon only accepted between hour and minutes.


6. Html Tags: <[^>]+>
This will only allow entering <> signs and it's not allowed to write anything behind these signs <>, You can only write anything inside the signs <>. These are html tags.


7. HashTags: #\w+
This regex allows users to write a hashtag.
A hashtage can be written anywhere in the sentence, which is the reason I didn't include ^ sign. 

8. Currency amounts: This will allow writting currency like numbers, including optional simbols like €, $ , having commas seperating thousands and optional 2 digits after a . as decimal places.
