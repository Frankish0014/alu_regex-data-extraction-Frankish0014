Form field validations.

1. Email addresses:

^[a-zA-Z0-9._%+_]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

2. URLs:

^https:\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\/[^\s]*)?$


3. Phone numbers (Various formate)

^(\(\d{3}\)|\d{3})[-. ]\d{3}[-. ]\d{4}$


4. Credit Card numbers
^\d{4}[-. ]\d{4}[-. ]\d{4}[-. ]\d{4}$

5. Time

^([01]?[0-9]|2[0-3]):[0-5][0-9]$


6. Html Tags
<[^>]+>

7. HashTags
#\w+

8. Currency amounts

^[^\d\s-]?\d{1,3}(,\d{3})*(\.\d{2})?$|^[^\d\s-]?\d+(\.\d{2})?$
