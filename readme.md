# Django API to stimulate the behaviour of the Audio Files

### Number of endpoints: 4

1. Getting all the files related to a type:
       GET: /audioFileType

2. Creating a new file of a type:
       POST: /audioFileType/ 
    also takes a dictionary of meta data related to the file

3. Updating a file:
     PUT: /audioFileType/id
    also takes a dictionary of meta data related to the file

4. Deleting a file:
     DELETE: /audioFileType/id

   