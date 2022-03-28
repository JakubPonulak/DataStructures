{% include navigation.html %}

<p style="font-size: 30px">Search for pages</p>
<input style="margin: auto; width: 50%" type="text" id="SearchInput" onkeyup="SearchMain(list = websitePages, textcolor = '#c7ffd6', nullcolor = '#e30202', SearchID = 'SearchInput', ResultID = 'SearchResult', DebugMode = false)" placeholder="Search for pages" title="Search for pages">
<br>
<p style="margin: auto; width: 50% id="SearchResult"></p>
<script>
        // this is an array that includes most of our website's pages.
        // each object in the list has a name and a path.
        // the name will be checked against the user's input to check which object should be selected to return.
        // the path is used to create a link to the desired page
        let websitePages =
            [
                {"name":"HTML", "path":"/topics/html"},
                {"name":"CSS", "path":"/topics/scss"},
                {"name":"JavaScript", "path":"/topics/javascript"},
                {"name":"API Collection", "path":"/api_collection/"},
                {"name":"CRUD", "path":"/crud/"},
                {"name":"Async CRUD", "path":"/crud_api/"},
                {"name":"Search (Database)", "path":"/crud/search/"},
                {"name":"Login", "path":"/login/"},
                {"name":"Sign Up", "path":"/register/"},
                {"name":"Home", "path":"/"},
                {"name":"Games", "path":"/games/"},
                {"name":"Google Translate", "path":"/google_translate/"}
            ] ;

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
    </script>

{% include_relative README.md %}
