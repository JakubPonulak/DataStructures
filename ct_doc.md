{% include navigation.html %}

# Create Task Documentation

## Replit Runtime

{% include ct_embed.html %}

## Written Response

1. Provide a written response that does all three of the following:

   a. Describes the overall purpose of the program

   **The purpose of my program, a page search bar, is to enable users of our website to navigate through the website's pages more easily as compared to using the navigation bar. It allows users to type in the name of a page and instantly access a link to said page.**

   b. Describes what functionality of the program is demonstrated in the video

   **The video shows the function taking in an output, comparing it to an array, and returning varying results based on what item or items in the list match the output, if any.**

   c. Describes the input and output of the program demonstrated in the video

   **The input of the program is the search bar found on the front page of our website, while the output is the links that show up underneath the search bar after a certain word is input into the search bar. Another output is the "No Results" message when the search bar is empty.**

2. Capture and paste two program code segments you developed during the administration of this task that contain a list (or other collection type) being used to manage complexity in your program.

   a. The first program code segment must show how data have been stored in the list. 

   ```
   let websitePages =
         [
             {"name":"Hamza", "path":"/hamza/"},
             {"name":"Jakub", "path":"/jakub/"},
             {"name":"Kevin", "path":"/kevin/"},
             {"name":"Sreeja", "path":"/sreeja/"},
             {"name":"Tristan", "path":"/tristan/"},
             {"name":"Math", "path":"/math/"},
             {"name":"History", "path":"/history/"},
             {"name":"Science", "path":"/sci/"},
             {"name":"Literature", "path":"/lit/"},
             {"name":"Periodic Table", "path":"/periodictable/"},
             {"name":"AP Chemistry", "path":"/chem/"},
             {"name":"API Collection", "path":"/api_collection/"},
             {"name":"CRUD", "path":"/crud/"},
             {"name":"Async CRUD", "path":"/crud_api/"},
             {"name":"Search (Database)", "path":"/crud/search/"},
             {"name":"Login", "path":"/login/"},
             {"name":"Sign Up", "path":"/register/"},
             {"name":"Forums", "path":"/forums"},
             {"name":"Home", "path":"/"},
         ] ;
   ```
   b. The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose. 

   ```
   for (i = 0; i < list.length; i++) {
        let link = list[i].path
        let title = list[i].name
        let output = `<a href='${link}'>${title}</a>` + ' | ' 
   ```
   c.  Identify the name of the list being used in this response

   **The name of the list is "websitePages"**

   d. Describe what the data contained in the list represent in your program

   **The data stored in the list represent page names and the paths for their individual links.**

   e. Explain how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list. 

   **If I had not used a list, I would have needed to include all the page names and paths in the function, which would have made it a lot longer, and would also make adding more pages a longer process. It would also been more difficult or would require more code to classify the pages into specific categories. Using an external list (as a parameter) also allows other programers to use their own lists instead of modifying the program.**

3. Capture and paste two program code segments you developed during the administration of this task that contain a student-developed procedure that implements an algorithm used in your program and a call to that procedure. 

   a. The first program code segment must be a student-developed procedure that:

      * Defines the procedure’s name and return type (if necessary)

      * Contains and uses one or more parameters that have an effect on the functionality of the procedure

      * Implements an algorithm that includes sequencing, selection, and iteration 

   ```

   function SearchMain(list = websitePages, textcolor = 'white',nullcolor = 'red', SearchID = 'SearchInput', ResultID = 'SearchResult', DebugMode = false, NoRText = 'No Results') {
            let input = document.getElementById(SearchID);
            let filter = input.value.toUpperCase(); // the user's input is changed to uppercase so that the search is not case-sensitive
            document.getElementById(ResultID).innerHTML = '| ' // this line makes the output blank whenever the function is called so that previous information is removed
            if (DebugMode === false) {
                for (x = 0; x < list.length; x++) { // this section goes through the items in my array and checks if the user's input is the same as any object name
                    if (list[x].name.toUpperCase().includes(filter)) { //using include function allows users to only input part of the page name instead of the whole thing
                        let link = list[x].path;
                        let title = list[x].name;
                        let output = `<a class='intlink' href='${link}'>${title}</a>` + ' | '; //this allows multiple links to be included in the result
                        document.getElementById(ResultID).innerHTML += output
                        document.getElementById(ResultID).style.color = 'grey'
                        let intlink = document.getElementsByClassName('intlink')
                        for (y = 0; y < intlink.length; y++) {
                            intlink[y].style.color = textcolor
                        }
                    }
                    if (filter === '') { //in case the user leaves the input blank, this statements causes the function to return "No Results"
                        document.getElementById(ResultID).innerHTML = NoRText
                        document.getElementById(ResultID).style.color = nullcolor
                    }
                }
            }
            else {
                for (i = 0; i < list.length; i++) {
                    let link = list[i].path
                    let title = list[i].name
                    let output = `<a href='${link}'>${title}</a>` + ' | ' //this allows multiple links to be included in the result
                    document.getElementById(ResultID).innerHTML += output
                    document.getElementById(ResultID).style.color = textcolor
                }
                document.getElementById(ResultID).innerHTML += '<br>' + `<p id='NoRText'>${NoRText}</p>`
                document.getElementById('NoRText').style.color = nullcolor
                }
        }        
   ```
   b. The second program code segment must show where your student-developed procedure is being called in your program.

   ```
   <input type="text" id="SearchInput" onkeyup="SearchMain(list = websitePages, textcolor = '#7051fc', nullcolor = '#e30202', SearchID = 'SearchInput', ResultID = 'SearchResult', DebugMode = false)" placeholder="Search for pages" title="Search for pages">
    <!-- here the search function is called with "onkeyup", meaning whenever a key input is let go.
    This allows users to make searches without hitting a submit button -->   
   ```
   c. Describe in general what the identified procedure does and how it contributes to the overall functionality of the program

   **This procedure is dependent on one parameter, "DebugMode", being set to true or false. If it is set to false, the procedure takes the user's input, changes it to be all uppercase (so that the search is not case-sensitive), and checks it agains items in the list "websitePages". If the input matches one or multiple items in the list, the procedure changes the result HTML element to show the names of the pages along with their respective links. If the input is left blank, the procedure changes the HTML elements to show "No Result". However, if "DebugMode" is set to true, the procedure returns all the items in the list along with the "No Result" message, no matter what the user's input is.**

   d. Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it.

   **The algorithm (for when "DebugMode" is set to false) uses a for loop, which uses a variable set to equal the length of "websitePages", to iterate through the items in the list "websitePages". Then, if the user's input matches part of the list, the algorithm takes the item or items from the list that match, and converts it into a link with a unique name and path, or multiple links if the input matches more than one list item. It then changes the content of the ouput (an HTML element) to be that link or group of links.**

4. Provide a written response that does all three of the following:

   a. Describes two calls to the procedure identified in written response 3. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute.

   First Call: **The user sets "DebugMode" equal to false in the parameters of the function when it is called in HTML.**

   Second Call: **The user sets "DebugMode" equal to true in the parameters of the function when it is called in HTML.**

   b. Describes what condition(s) is being tested by each call to the procedure

   Condition(s) tested by the first call: **The condition tested is if "DebugMode" is set to false, which means the program should run normally.**

   Condition(s) tested by the second call: **The condition tested is if "DebugMode" is set to anything except false (using else statement), which means the program should run in Debugging Mode.**

   c. Identifies the result of each call

   Result of the first call: **The function runs normally, which means that list items matching the user's input are printed below the search bar as a link.**

   Result of the second call: **The procedure runs in Debugging Mode, which means that all the items in the list and the "No Results" message are printed underneath the search bar. This is so that programers can test the procedure and find errors easily.**

 
# Links
[Create Task Runtime](https://replit.com/@JakubPonulak/Create-Task-Runtime#index.html)
[Personal Repository](https://github.com/JakubPonulak/DataStructures)
