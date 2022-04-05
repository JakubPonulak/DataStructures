{% include navigation.html %}

# Create Task Documentation

## Replit Runtime

{% include ct_embed.html %}

## Code Snippets
```
<input type="text" id="SearchInput" onkeyup="SearchMain(list = websitePages, textcolor = '#7051fc', nullcolor = '#e30202', SearchID = 'SearchInput', ResultID = 'SearchResult', DebugMode = false)" placeholder="Search for pages" title="Search for pages">
    <!-- here the search function is called with "onkeyup", meaning whenever a key input is let go.
    This allows users to make searches without hitting a submit button -->
    <br>
    <p id="SearchResult"></p>
```
```
let websitePages =
            [
                {"name":"Hamza", "path":"/hamza/"},
                {"name":"Jakub", "path":"/jakub/"},
                {"name":"Kevin", "path":"/kevin/"},
                {"name":"Sreeja", "path":"/sreeja/"},
                {"name":"Tristan", "path":"/tristan/"},
                {"name":"Math", "path":"/class_topics/math"},
                {"name":"History", "path":"/class_topics/history"},
                {"name":"Science", "path":"/class_topics/sci"},
                {"name":"Literature", "path":"/class_topics/lit"},
                {"name":"Periodic Table", "path":"/periodictable/"},
                {"name":"AP Chemistry", "path":"/chem/"},
                {"name":"Physics", "path":"/physics/"},
                {"name":"API Collection", "path":"/api_collection/"},
                {"name":"CRUD", "path":"/crud/"},
                {"name":"Async CRUD", "path":"/crud_api/"},
                {"name":"Search (Database)", "path":"/crud/search/"},
                {"name":"Login", "path":"/login/"},
                {"name":"Sign Up", "path":"/register/"},
                {"name":"Forums", "path":"/forums"},
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
```

[Create Task Runtime](https://replit.com/@JakubPonulak/Create-Task-Runtime#index.html)
