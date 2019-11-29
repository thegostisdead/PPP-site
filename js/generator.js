var JSONURL = 'https://raw.githubusercontent.com/thegostisdead/PPP-site/master/data/data.json?token=AGDVOKSAABARP2PORYV56US54PUBA'

var getJSON = function(url, callback) {

    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'json';

    xhr.onload = function() {

        var status = xhr.status;

        if (status == 200) {
            callback(null, xhr.response);
        } else {
            callback(status);
        }
    };

    xhr.send();
};


// je récupère la liste des métiers
jsonObject = ""

getJSON(JSONURL, function(err, data) {

    if (err != null) {
        console.error(err);
    } else {

        jsonObject = data

        console.log(jsonObject);

        for (let i = 0; i < jsonObject.length; i++) {
            console.log(jsonObject[i])

            html ="<p>nom: " + jsonObject[i].name + "<\/p>"

            var result = document.getElementById('search-result').innerHTML += html



        }


    }
});

// je fait le rendu
