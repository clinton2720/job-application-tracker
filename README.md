   # JOB APPLICATION TRACKER
  #### Video Demo:  https://youtu.be/b-zag4q4Szk
  #### Description: A simple job application tracker to log when you have submitted your applications and also the ability to update or delete applications. There are four main functions, "CRUD" which creates, updates, deletes, and reads out data, which is stored in JSON.

Decided to use JSON as it seemed more complex to work with and wanted the challenge, thinking perhaps naively that CSV files were too easy to work with. As a result pretty well versed in dictionaries and lists.

## Helper Functions:
1.confirm(): This allows the user to confirm any action before its done. Decided to make confirm into a function as most of the major functions needed one and hence was best use case of just making a template. It accepts a prompt, provided by the coder when calling the function, and an expected Type. Two types which are - "y/n" which returns whether a user hit yes or no, as a form of Boolean value, and int, which returns an int, although didn't have a use for it in this program yet. Can be removed as this option is present in get_user_input, but wanted to keep the functions separate in case future upgrades require user to enter a number to confirm something.

2. get_application_input(): which accepts the details for a job application, and is used in the create and update functions. Main function for accepting data for application. Returns a dict of the entered data. id key is none as major functions require ability to change id according to scenario.

3. get_user_input() which either returns the raw string the user entered or the integer. Coder can enter expected type here as well. Mainly used for accepting job IDS which user wants to act upon. Decided to give an option to return string as well for possible future use. May have confused myself when writing confirm()

4. pretty_print(): uses tabulate library, made it to a function as showIndex and header parameters were being reused everywhere. Had trouble with displaying dicts, hence when passing dicts will have to wrap it in a list.

## Major functions:
add(): It loads the JSON file and iterates over the ids in the file and finds the largest id, adds 1 to it to assign it to the job id the user is currently trying to add to prevent duplication. Adds all other details of application like role name, company, date applied and status. Saves to a new list which is dumped into a JSON file, effectively re-writing it, as during the process saved all existing applications to a list which is dumped along with the new application, Prints the application to be added before confirmation using helper functions.

update(): Loads the file, asks user job ID to update, user enters all the details of the job application selected and updates whichever fields require an update in the process. Uses same method of saving to JSON file as add(). Decided to let user update all details for now to allow error correction, although in future modifications will give choice to update fields, to enhance user experience. Prints and confirms before taking action.

delete(): Deletes the job application selected by the user, by saving all other applications excluding selected application. Also asks confirmations and prints data out before confirming.

list(): lists out all the applications using tabulate
