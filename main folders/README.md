Sreeraj Chintham <schintha1@stevens.edu> Sanika Ramachandra chavan <schava12@stevens.edu> Saicharan Saini <ssaini1@stevens.edu>

# Our github Repo <https://github.com/Sanika1311/Project_3>

Sanika, Sreeraj and Sai Charan spent approximately 40hrs each on the project.

# Testing 
In our testing approach, we utilized input testing by generating a set of test cases consisting of various user inputs. The test cases were designed to ensure that the API behaves as expected in different scenarios, such as when an invalid ID is provided, no ID is provided, or when the correct data is returned. We also used Postman, a popular tool for testing APIs, to perform additional tests and verify the responses from the API. This testing methodology allowed us to ensure that our API was reliable, accurate, and met the requirements of the application.

# Bugs and Issues :
Our code has been thoroughly tested and we've not found any bugs. The API is functioning as intended, and providing the expected results for various user inputs. Additionally, the extensions we have implemented are working correctly.


# Bugs Resolved :
Our code encountered a 404 error which was difficult to resolve and took a significant amount of time and effort to fix. The error was caused by an unidentified issue in the code, requiring us to extensively debug and analyze the problem.


# Extensions :

1. Users and User Keys - 
This extension enables users to create a post by providing both the user ID and corresponding user key. If the user created a post, they only need to provide the user's key to delete the post. It is crucial to differentiate between the keys for the post and the user to avoid confusion.

2. User Profiles - 
This extension enables users to create a user by providing a unique part and optional non-unique parts, retrieve a user's metadata by specifying their ID or unique metadata, edit a user's metadata with their key for authentication, and include the user's unique metadata when returning data about a post associated with the user.

3. Date and Time - based range queries - 
This extension lets the users search for posts based on a start date and time, an end date and time, or both. When making such a request, the API endpoint returns a list of post information, including the post ID, message, timestamp, and any other relevant data such as user information.

4. User - based range queries - 
This extension lets the users to search for posts made by a specific user by providing the user ID as a parameter to the API endpoint. The endpoint then returns a list of post information associated with that user, including the post ID, message, timestamp, and any other relevant data such as user information. By using this extension, users can easily and quickly find posts made by a particular user without having to manually sort through all the posts on the platform.

5. Moderator role - 
This extension lets the users to create a new privileged role of 'administrator' that has the authority to delete posts not belonging to them using a distinct key called the 'moderator key'. The 'moderator key' can be added to the user's metadata as a 'moderator' flag, provided that the code already has user authentication implemented. When deleting a post through the API, users must specify whether they are using a post key or a moderator key. Additionally, the extension includes a safeguarded mechanism for generating new moderator keys to prevent unauthorized access.





