from itertools import count


def beginHtml():
    return str(''' <!DOCTYPE html>
<html>
<style>
     p {
        line-height: 2;
        margin-top: 0;
        margin-bottom: 0;
    }
    
      .customIndent {
        padding-left: 1em;
    }
    

    .error {
        position: relative;
        display: inline-block;
        border-bottom: 1px dotted black;
        color: red;
    }
    
    .redeclared {
        position: relative;
        display: inline-block;
        border-bottom: 1px dotted black;
        color: blue;
    }
    
    .notinic {
        position: relative;
        display: inline-block;
        border-bottom: 1px dotted black;
        color: orange;
    }
    .aninh {
        position: relative;
        display: inline-block;
        border-bottom: 1px dotted black;
        color: green;
    }
    
    .code {
        position: relative;
        display: inline-block;
    }
    
    .error .errortext,
    .redeclared .redeclaredtext,
    .notinic .notinictext, .aninh .aninhtext  {
        visibility: hidden;
        width: 200px;
        background-color: #555;
        color: #fff;
        text-align: center;
        border-radius: 6px;
        padding: 5px 0;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        margin-left: -40px;
        opacity: 0;
        transition: opacity 0.3s;
    }
    
    .error .errortext::after,
    .redeclared .redeclaredtext::after,
    .notinic .notinictext::after, .aninh .aninh::after {
        content: "";
        position: absolute;
        top: 100%;
        left: 20%;
        margin-left: -5px;
        border-width: 5px;
        1 border-style: solid;
        border-color: #555 transparent transparent transparent;
    }
    
    .error:hover .errortext,
    .redeclared:hover .redeclaredtext,
    .notinic:hover .notinictext, .aninh:hover .aninhtext {
        visibility: visible;
        opacity: 1;
    }

    table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body >

  ''')


def finalData( ):
    r = beginHtml() + '<h1 class="w3-center"> <div class ="w3-teal">System Dependency Graph</div><img class="scale-down" src="../src/doctest-output/sdg.gv.png" style="width:1000px;"></h1>'
    return r + str('''</body></html>''')

