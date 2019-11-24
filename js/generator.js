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

            html = "<\/dt>\r\n<dd class=\"accordion-content accordionItem is-collapsed\" id=\"accordion2\" aria-hidden=\"true\">\r\n<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi eu interdum diam. Donec interdum porttitor risus non bibendum. Maecenas sollicitudin eros in quam imperdiet placerat. Cras justo purus, rhoncus nec lobortis ut,\r\n                    iaculis vel ipsum. Donec dignissim arcu nec elit faucibus condimentum. Donec facilisis consectetur enim sit amet varius. Pellentesque justo dui, sodales quis luctus a, iaculis eget mauris. <\/p>\r\n                <p>Aliquam dapibus, ante quis fringilla feugiat, mauris risus condimentum massa, at elementum libero quam ac ligula. Pellentesque at rhoncus dolor. Duis porttitor nibh ut lobortis aliquam. Nullam eu dolor venenatis mauris placerat\r\n                    tristique eget id dolor. Quisque blandit adipiscing erat vitae dapibus. Nulla aliquam magna nec elementum tincidunt.<\/p>\r\n            <\/dd>\r\n            <dt>\r\n          <a href=\"#accordion3\" aria-expanded=\"false\" aria-controls=\"accordion3\" class=\"accordion-title accordionTitle js-accordionTrigger\">\r\n " + jsonObject[i].name + "     <\/a>\r\n        <\/dt>"

            var result = document.getElementById('search-result').innerHTML += html



        }


    }
});

// je fait le rendu